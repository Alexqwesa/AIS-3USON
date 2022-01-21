#!/usr/bin/python3
# -------------------------------------------------------------------------------
# -*- coding: utf-8 -*-
# Name:        AIS 3USON Edits journal + journal table model
# Purpose:
#
# Author:      Savin Alexander Viktorovich aka alexqwesa
# Created:     2019-2021
# Copyright:   Savin Alexander Viktorovich aka alexqwesa
# Licence:     LGPL 3
# This software is licensed under the "LGPLv3" License as described in the "LICENSE" file,
# which should be included with this package. The terms are also available at
# http://www.gnu.org/licenses/lgpl-3.0.html
# -------------------------------------------------------------------------------

from datetime import datetime as dt
from collections import OrderedDict, defaultdict
from contextlib import suppress
from threading import RLock

from qtpy.QtCore import QDateTime, QAbstractTableModel, Signal, Slot
from qtpy.QtSql import QSqlQuery

from helper_func import *
from qtpy.QtWidgets import QMessageBox


class cellEdit():
    """
    Class for storing single edit of cell (== any field).
    view, model, row_id, col_name, prev, value, saved, prev_edit
    """

    def __init__(self, journal, view, model, row_id, col_name, prev, new_value):
        """"
        Constructor for cellEdit
        """
        # from models.ts_models import tsSqlTableModel
        self.id = None
        self.journal: editStorage = journal
        self.view = view
        self.model = model
        # self.model: tsSqlTableModel = model
        self._row_ind = None
        # if col_name not in model.info.ids:
        self.row_id = row_id
        self.col_name = col_name
        self.prev = prev
        self.value = new_value
        self._state = CE_PENDING
        now = dt.now()
        self.timestamp = dt.timestamp(now)
        self._prev_edit = None  # link to object or False if it First Edit (currently: new chain created on save)
        self.default_values: Union[dict, None] = None
        self.verified = {}  # TODO: all data returned from confirmed row ?
        # maybe use child cellEdit for representing this value in journal

    def save(self):
        ret = self.journal.call_submit_row.emit([self, ])
        self.journal.model_changed.emit(self.model.info.cut_name)
        self.model.saved.emit(self.model)
        self.journal.journal_changed.emit()
        return ret

    @property
    def row_id(self):
        return self.journal.inner_row_id[self._row_ind]

    @property
    def sql_query(self):
        """
        Helper method - return QSqlQuery,
        sql_query.lastQuery() to see sql statement.
        :return: QSqlQuery
        """
        if self.row_id[:4] == "new_":
            #############################
            # prepare insert from cellEdits and add default keys
            # ---------------------------
            items = {self.col_name: self.value}
            items = {**self.default_values, **items}
            #############################
            # subtract alien keys
            # ---------------------------
            for key in self.model.info.not_for_edit:
                with suppress(KeyError):
                    items.pop(key)
            #############################
            # prepare vars
            # ---------------------------
            key_list = list(items.keys())
            val_list = list(items.values())
            bind_val = ", ".join(["?" for k in key_list])
            keys = "`" + "`, `".join(key_list) + "`"
            #############################
            # prepare query
            # ---------------------------
            query = QSqlQuery(self.journal.SD.get_db)
            query.prepare("INSERT INTO {} ({}) ".format(self.model.info.sql_name, keys) +
                          " VALUES ({})".format(bind_val))
            #############################
            # bind values and exec query
            # ---------------------------
            for val in val_list:
                query.addBindValue(val)
            return query
        elif self.row_id[:4] == "row_":
            #############################
            # sql update row
            # ---------------------------
            row_ids = self.row_id[4:]
            if self.col_name in self.model.info.ids:
                row_ids = row_ids.replace(data_sql_format(self.value), data_sql_format(self.prev))
            where = " and ".join(
                [" {} = {} ".format(key, val) for key, val in zip(self.model.info.ids, row_ids.split("_"))])
            keys = "`" + self.col_name + "` = ? "
            return QSqlQuery(self.journal.SD.get_db).prepare(
                f"UPDATE {self.model.info.sql_name} SET {keys} where ( {where} )")

    @row_id.setter
    def row_id(self, new_row_id):
        #############################
        # change all edits in journal too
        # ---------------------------
        self._row_ind = self.journal.update_row_ind(self._row_ind, new_row_id)
        if self.row_id != new_row_id:
            critical(" row_id - %s error in model - %s", new_row_id, self.model.objectName())

    @property
    def prev_edit(self):
        return self._prev_edit

    @prev_edit.setter
    def prev_edit(self, value):
        if value is self:
            value = False
        self._prev_edit = value

    @property
    def state(self):
        return self._state

    @state.setter
    def state(self, value):
        if value != self._state:
            #############################
            # set new value
            # ---------------------------
            self._state = value
            #############################
            # update model
            # ---------------------------
            if self.journal and self.model:
                if CE_DISCARD <= value <= CE_DISCARD_:
                    self.model._set_by_row_id(self.row_id, self.col_name, self.prev)
                    self.journal.last_edit.cache_clear()
                self.journal.model_changed.emit(self.model.info.cut_name)
                # self.model.dataChanged.
            #############################
            # update view
            # ---------------------------
            if self.view:
                # self.view.call_update.emit()
                if hasattr(self.view, "call_activate"):
                    self.view.call_activate.emit(self.col_name)

    @property
    def state_saved(self):
        return CE_SAVED <= self.state <= CE_CONFIRMED_

    @property
    def state_commited_journal(self):
        return CE_COMMITTED <= self.state <= CE_SHADOWED_

    @property
    def col_num(self):
        return self.model.tsFieldNames.index(self.col_name)

    def last_saved_value(self):
        model_row = self.journal.model_row_cols[self.model.info.cut_name][self._row_ind]
        for ce in reversed(model_row):
            if ce.col_name == self.col_name and ce.state_saved:
                return ce.value
        for ce in model_row:
            if ce.col_name == self.col_name and ce.state_commited_journal:
                return ce.prev
        return self.prev


class _EditStorage(QObject):
    """Class for storing edit history.
        For every edit object there is several states:
            pending - in process of creation
            commited - added to history
            submited - submit to DB
            saved - status of submit ok, and row_id updated
            confirmed - reselected from DB
            failed - failed to submit or reselect
    """
    model_changed: Signal = Signal(str)

    def __init__(self, parent=None):
        """Constructor for editStorage"""
        super().__init__(parent)
        self.SD = parent
        # self.last_update = QDateTime.currentDateTime()
        self.lock = RLock()
        self.id_gen = count(0)
        self.back_id = 0
        self.last_id = 0
        self.global_log: {int: cellEdit} = OrderedDict()
        self.model_log = OrderedDict()
        self.model_row_cols = defaultdict(
            lambda: defaultdict(
                lambda: list()))  # and OrderDict
        self.pending_edit: Union[cellEdit, None] = None  # set()?
        self._upd_models: {str: QSqlTableModel} = {}
        self.unsaved: {int: cellEdit} = OrderedDict()
        self.undid_entries: {int: cellEdit} = {}
        #############################
        # zero element - terminator
        # ---------------------------
        # self.le_cache = LRUCache()
        self.inner_row_id = DictReverseDict()
        self.inner_row_id[0] = "ERROR"
        self.iter_row_ind = count(1)
        self.add_stop_mark()
        self.last_stop_id = 0

    def update_row_ind(self, row_ind, new_row_id):
        with self.lock:
            if not row_ind:
                #############################
                # for new edits, check existence
                # ---------------------------
                try:
                    row_ind = self.inner_row_id(new_row_id)
                except KeyError:
                    row_ind = next(self.iter_row_ind)
                    self.inner_row_id[row_ind] = new_row_id
            else:
                #############################
                # update exist
                # ---------------------------
                self.inner_row_id[row_ind] = new_row_id
            return row_ind

    def add_stop_mark(self):
        self.last_id = next(self.id_gen)
        self.global_log[self.last_id] = cellEdit(self, None, None, None, None, None, None)
        self.global_log[self.last_id].state = CE_STOP
        self.back_id = self.last_id
        self.last_stop_id = self.last_id

    def prev_value(self, model, row_id, col_name):  # TODO: maybe use cut_name
        ce: cellEdit
        for ce in reversed(self.model_log[model].values()):  # py 3.8
            if ce.col_name == col_name:
                if ce.row_id == row_id:
                    return ce.prev

    def last_value(self, model, row_id, col_name):  # TODO: maybe use cut_name
        ce: cellEdit
        for ce in reversed(self.model_log[model].values()):  # py 3.8
            if ce.col_name == col_name:
                if ce.row_id == row_id:
                    return ce.value
        return

    def last_saved_value(self, model, row_id, col_name):
        ce: cellEdit
        #############################
        # last saved value
        # ---------------------------
        for ce in reversed(self.model_log[model].values()):  # py 3.8
            if CE_SAVED <= ce.state <= CE_CONFIRMED_:
                if ce.col_name == col_name:
                    if ce.row_id == row_id:
                        return ce.value
        #############################
        # first prev value
        # ---------------------------
        for ce in self.model_log[model].values():  # py 3.8
            if ce.state < CE_SAVED:
                if ce.col_name == col_name:
                    if ce.row_id == row_id:
                        return ce.prev
        return

    def cache_clear(self):
        self.last_edit.cache_clear()

    @lru_cache(None)
    def last_edit(self, model, row_id, col_name=None):
        #############################
        # get row index from row id
        # ---------------------------
        try:
            _row_ind = self.inner_row_id(row_id)
        except KeyError:
            return False, None
        #############################
        # search edits
        # ---------------------------
        if _row_ind in self.model_row_cols[model.info.cut_name]:
            urow = self.model_row_cols[model.info.cut_name][_row_ind]
            ce: cellEdit
            for ce in reversed(urow):
                if ce.state < CE_DISCARD and ce.col_name == col_name:
                    return True, ce
        return False, None

    def _commit_edit(self, model, prev, new, added_values=None):
        """ Realisation of SD.commit_edit"""
        # :tsSqlTableModel # , col_name, orig, new_value, index
        id = next(self.id_gen)
        ce: cellEdit = self.pending_edit  # TODO check is the same
        if ce.model != model:
            debug("CellEdit model changed from %s to %s ", ce.model, model)
            ce.model = model
        ce.id = id
        ce.prev = prev
        ce.value = new
        if ce.col_name in model.info.ids:
            if "row_" in ce.row_id[:4]:
                new_row_id = ce.row_id.replace(data_sql_format(prev), data_sql_format(new))
                ce.row_id = new_row_id
        #############################
        # add to model log
        # ---------------------------
        if model not in self.model_log:
            self.model_log[model] = OrderedDict()
        self.model_log[model][id] = ce
        #############################
        # add to global log + shift counters + cleanup
        # ---------------------------
        self.global_log[id] = ce
        self.pending_edit = None
        self.last_id = id
        self.back_id = id
        #############################
        # fill model dirty rows
        # ---------------------------
        self.model_row_cols[model.info.cut_name][ce._row_ind].append(ce)
        #############################
        # check is new line: add default values
        # ---------------------------
        if added_values:
            ce.default_values = added_values
        elif "new_" in ce.row_id:
            ce.default_values = model.default_values.copy()
        #############################
        # unsaved list
        # ---------------------------
        self.unsaved[id] = ce
        ce.journal = self
        if self.last_saved_value(model, ce.row_id, ce.col_name) == ce.value:
            ce.state = CE_SAVED
        else:
            ce.state = CE_COMMITTED
        self.last_edit.cache_clear()
        return id

    def commit_edit(self, model, prev, new, added_values=None):  # , col_name, orig, new_value, index
        with self.lock:
            self.cache_clear()
            return self._commit_edit(model, prev, new, added_values)

    def start_edit(self, view, model, row_id, col_name, prev=None, new=None):
        with self.lock:
            # if model.info:
            #     if model.info:
            #         pass  # row_id rework
            self.pending_edit = cellEdit(self, view, model, row_id, col_name, prev, new)

    @property
    def last(self):
        return self.global_log[self.last_id]


class PersistentStorage(_EditStorage):
    """Class for storing edit history
        Implemented save and discard changes
    """

    def __init__(self, parent=None):
        super().__init__(parent)
        self.last_update = QDateTime.currentDateTime()
        self._last_log = self.global_log

    @property
    def last_log(self):
        with self.lock:
            last_global_key = next(reversed(self.global_log.keys()))
            last_local_key = next(reversed(self._last_log.keys()))
            if last_local_key != last_global_key:
                for i in range(last_local_key, last_global_key + 1):
                    ce: cellEdit = self.global_log[i]
                    if ce.state == CE_STOP:
                        self._last_log = {}
                    self._last_log[i] = ce
            return self._last_log

    def operate_changes(self, save=True, hid=0, model_obj=""):
        global_log_changed = False
        with self.lock:
            #############################
            # get models
            # ---------------------------
            self.cache_clear()
            if model_obj:
                models = [model_obj]
            else:
                models = self.model_row_cols.keys()
            #############################
            # save models
            # ---------------------------
            for model in models:
                for row_ind, ces in self.model_row_cols[model].items():
                    last_saved_model = ces[0].model
                    if not last_saved_model.info.read_only:
                        global_log_changed = True
                        if save:
                            self.save_row(model, ces)
                        else:
                            self.discard_row(ces)
                        if last_saved_model:
                            last_saved_model.saved.emit(last_saved_model)
        #############################
        # update views
        # ---------------------------
        for view in self.SD.unsaved_view:
            view.updateLayout()  # use view.update()
            # view.update()  # TODO: add checks?
            # if action == "below":
            #     if hid == 0:  # save alla
            #         action = "all"
            # if action == "all":
            # self.global_log[eid].saved = True
        #############################
        # update log
        # ---------------------------
        if global_log_changed:
            self.add_stop_mark()
        return global_log_changed

    @Slot()
    @Slot(int)
    @Slot(int, str)
    def save(self, hid=0, model_obj=""):
        return self.operate_changes(True, hid, model_obj)

    def submit_row(self, ces: [cellEdit]):
        """
        Find updatable table by this table name and try update dirty rows by rows
        :arg: ces - list of cellEdit of one row of one model
        :return:
        """
        ce = ces[0]
        model = ce.model
        #############################
        #
        # ---------------------------
        db = self.SD.get_db
        msg = self.tr("Не удалось найти запись")  # "update row not found"
        where = ""
        ret = False
        with self.lock:
            cur_row = ce.row_id
            if ce.row_id[:4] == "row_":
                #############################
                # update row
                # ---------------------------
                row_ids = ce.row_id[4:]
                for ce in ces:  # ces here had only unique elements - it is deduplicated in save row
                    if ce.col_name in model.info.ids:
                        row_ids = row_ids.replace(data_sql_format(ce.value), data_sql_format(ce.prev))
                row_ids = row_ids.split("_")
                where = " and ".join([" {} = {} ".format(key, val) for key, val in zip(model.info.ids, row_ids)])
                db.transaction()
                for upd_table in model.info.save_to_tables:
                    upd_ret, chk_msg = self.check_query(ces, upd_table, where)
                    if upd_ret is False:
                        break
                    elif upd_ret:
                        ret, msg = self.update_query(ces, upd_table, where)
                        if ret:
                            break
                    elif chk_msg == "different":
                        msg = self.tr("Запись в базе данных была обновлена до вас")
                db.commit()
            else:
                #############################
                # set insert data
                # ---------------------------
                for upd_table in model.info.save_to_tables:
                    ret, last_insert_id_as_dict, msg = self.insert_query(ces, upd_table)
                    if ret:
                        #############################
                        # prepare where for check
                        # ---------------------------
                        where = " and ".join(
                            [f" {key} = {val} " for key, val in last_insert_id_as_dict.items()])
                        break
            #############################
            # check return status
            # ---------------------------
            if ret:
                # if cur_row in self.new_rows:
                #     self.added_rows.append(cur_row) #use id
                self.last_update = QDateTime.currentDateTime()
                debug("saving row %s of model %s ", cur_row, ce.model.objectName())
                for ce in ces:
                    ce.state = CE_SUBMITTED
                #############################
                # check saved and mark CE_SAVED
                # ---------------------------
                for upd_table in model.info.save_to_tables:
                    ret = self.check_saved(ces, upd_table, where)
                    if ret:
                        break
            else:
                self._save_error(ret, cur_row, msg)
                for ce in ces:
                    ce.state = CE_SUB_FAILED
        return True

    def save_row(self, model_cut, ces):
        #############################
        # check overshadowed edits
        # ---------------------------
        final_row = {}
        for ce in ces:
            if ce.state <= CE_COMMITTED_:  # pending test?
                if ce.col_name not in final_row:
                    final_row[ce.col_name] = ce
                    ce.prev_edit = False
                else:
                    final_row[ce.col_name].status = CE_SHADOWED
                    if ce is final_row[ce.col_name]:
                        error("ce cyclic link")
                    else:
                        ce.prev_edit = final_row[ce.col_name]
                    final_row[ce.col_name] = ce
        #############################
        # submit row
        # ---------------------------
        if final_row:
            return self.submit_row(list(final_row.values()))

    @Slot()
    @Slot(int)
    @Slot(int, str)
    def discard(self, hid=0, model_cut_=""):
        return self.operate_changes(False, hid, model_cut_)

    def discard_row(self, ces):
        for ce in reversed(ces):  # important first change discard last
            if ce.state < CE_SAVED_:
                ce.state += CE_DISCARD

    def check_saved(self, ces, upd_table, where):
        """
        """
        #############################
        # run query
        # ---------------------------
        keys = "`" + "`, `".join([c.col_name for c in ces]) + "`"
        # bind_val = ", ".join(["?" for _ in ces])
        query = QSqlQuery(self.SD.get_db)
        query.prepare(" select {} from  {}  where ( {} )".format(keys, upd_table, where))
        ret = query.exec_()
        if ret:
            if query.next():
                #############################
                # if found - compare
                # ---------------------------
                for i, ce in enumerate(ces):  # TODO: don't work with overshadowed
                    prev = ce.value
                    ce.state = CE_CONFIRMED
                    if query.value(i) != prev:
                        if query.value(i) != str(prev):
                            if query.value(i) != "'" + str(prev) + "'":
                                ce.state = CE_CON_FAILED
            else:
                ret = False
        return ret

    def update_query(self, ces, upd_table, where):
        keys = ", ".join(["`" + c.col_name + "` = ? " for c in ces])
        # bind_val = ", ".join(["?" for c in ces])
        query = QSqlQuery(self.SD.get_db)
        query.prepare(f"UPDATE {upd_table} SET {keys} where ( {where} )")
        for c in ces:
            query.addBindValue(c.value)
        ret = query.exec_()
        return ret, query.lastError().text()

    def insert_query(self, ces, upd_table):
        #############################
        # prepare insert from cellEdits and add default keys
        # ---------------------------
        items = {c.col_name: c.value for c in ces}
        items = {**ces[-1].default_values, **items}
        #############################
        # subtract alien keys
        # ---------------------------
        for key in ces[-1].model.info.not_for_edit:
            with suppress(KeyError):
                items.pop(key)
        #############################
        # prepare vars
        # ---------------------------
        key_list = list(items.keys())
        val_list = list(items.values())
        bind_val = ", ".join(["?" for k in key_list])
        keys = "`" + "`, `".join(key_list) + "`"
        #############################
        # prepare query
        # ---------------------------
        query = QSqlQuery(self.SD.get_db)
        query.prepare("INSERT INTO {} ({}) ".format(upd_table, keys) +
                      " VALUES ({})".format(bind_val))
        #############################
        # bind values and exec query
        # ---------------------------
        for val in val_list:
            query.addBindValue(val)
        ret = query.exec_()
        #############################
        # check return
        # ---------------------------
        from models.ts_models import tsSqlTableModel
        model: tsSqlTableModel = ces[0].model
        last_insert_id = []
        if ret:
            #############################
            # get new row_id
            # ---------------------------
            row = int(ces[0].row_id[len("new_"):])
            if model.info.ids[0] == "id" and len(model.info.ids[0]) == 1:
                #############################
                # from autoincrement
                # ---------------------------
                last_insert_id.append(query.lastInsertId())
            else:
                #############################
                # from record
                # ---------------------------
                for id in model.info.ids:
                    if id in key_list:
                        val = val_list[key_list.index(id)]
                        last_insert_id.append(data_sql_format(val))
                    else:
                        critical("Error can't get new id of row")
            #############################
            # update row_id of edits
            # ---------------------------
            last_insert_str = ces[0].row_id
            if last_insert_id:
                last_insert_str = "row_" + "_".join(last_insert_id)
                last_insert_id = {k: val_list[key_list.index(k)] for k in ces[0].model.info.ids}
                c: cellEdit
                for c in ces:
                    c.row_id = last_insert_str
                    c.state = CE_SAVED
            else:
                last_insert_id = dict(items.items())
                for c in ces:
                    c.state = CE_SUBMITTED
            #############################
            # update model cache new_row_ids
            # ---------------------------
            model.new_row_ids_update.emit(row, last_insert_str)
        return ret, last_insert_id, query.lastError().text()
        #############################
        # db.driver not supported?
        # ---------------------------
        # if db.driver.hasFeature(QSqlDriver.LastInsertId):
        #     last_insert_id = query.lastInsertId
        #     row = ces[0].row_id[len("new_"):]
        #     for c in ces:
        #         c.row_id = "row_" + last_insert_id
        #         c.state = CE_SAVED
        #     c.model.new_row_ids[row] = "row_" + last_insert_id
        # else:
        #     critical("DB without LastInsertId not supported yet")
        #     pass

    def check_query(self, ces, upd_table, where):
        """
        :return:
        True - the same,
        None - no connection or none value,
        False - different or multiple values
        """
        #############################
        # run query
        # ---------------------------
        keys = "`" + "`, `".join([c.col_name for c in ces]) + "`"
        # bind_val = ", ".join(["?" for _ in ces])
        query = QSqlQuery(self.SD.get_db)
        query.prepare(" select {} from  {}  where ( {} )".format(keys, upd_table, where))
        ret = query.exec_()
        if ret:
            if query.next():
                #############################
                # if found - compare
                # ---------------------------
                for i, ce in enumerate(ces):
                    prev = ce.last_saved_value()
                    if query.value(i) != prev:
                        if query.value(i) != str(prev):
                            if query.value(i) != "'" + str(prev) + "'":
                                return False, "different"
                #############################
                # check found once
                # ---------------------------
                if query.next():
                    critical("multiple return from query - %s - %s", upd_table, where)
                    return False, "not single"
                #############################
                # success
                # ---------------------------
                return True, ""
            else:
                critical("No return from query - %s - %s", upd_table, where)
                return None
        return None, "wrong query"

    def _save_error(self, ret, cur_row, msg):
        if not ret:
            debug("wrong return status row %s model - %s", cur_row, self.objectName())
        # TODO: revertbyrows
        # self.revertAll()
        errtext = msg
        error(errtext)
        if "INSERT command denied to user " in errtext:
            QMessageBox.critical(self.parent().parent(), self.tr("Отказано"),
                                 self.tr("Недостаточно прав для добавления записи"), QMessageBox.Ok)
        elif "UPDATE command denied to user " in errtext:
            QMessageBox.critical(self.parent().parent(), self.tr("Отказано"),
                                 self.tr("Недостаточно прав для изменения"), QMessageBox.Ok)
        elif "underlying table doesn't have a default value" in errtext:
            QMessageBox.critical(self.parent().parent(), self.tr("Отказано"),
                                 self.tr("Обязательное для заполнение поле - не заполнено, \n" + errtext
                                         ), QMessageBox.Ok)  # "будет предпринята попытка восстановления"
        elif "server has gone away " in errtext:
            QMessageBox.critical(self.parent().parent(), self.tr("Отказано"),
                                 self.tr("Соединение с сервером прервалось - ваши данные не сохранены, "
                                         ), QMessageBox.Ok)  # "будет предпринята попытка восстановления"
        else:
            QMessageBox.critical(self.parent().parent(), self.tr("Отказано"),
                                 errtext, QMessageBox.Ok)
        # error(self.SD.get_db.lastError().text())
        # TODO: don't show errors twice


# @auto_reload_class_code(try_wrapper)
class editStorage(PersistentStorage):
    """Class for storing edit history
        Implemented outer interface
    """
    journal_changed: Signal = Signal()
    call_submit_row: Signal = Signal(list)

    # redo_available: Signal = Signal(bool)

    def __init__(self, parent=None):
        """Constructor for editStorage"""
        super().__init__(parent)
        self.call_submit_row.connect(self.submit_row)

    def operate_changes(self, save=True, hid=0, model_obj=""):
        ret = super().operate_changes(save, hid, model_obj)
        if ret:
            self.journal_changed.emit()
        return ret

    def _commit_edit(self, model, prev, new, added_values=None):
        commit_id = super()._commit_edit(model, prev, new, added_values)
        self.undid_entries.clear()
        self.journal_changed.emit()
        return commit_id

    @property
    def undo_available(self):
        # if self.back_id and self.last_id:
        # if self.global_log[self.back_id].state < CE_STOP:
        while self.last_log[self.back_id].state >= CE_SUBMITTED and self.back_id > 0:
            self.back_id -= 1
        return self.last_log[self.back_id].state < CE_SUBMITTED
        # return False

    @property
    def discard_available(self):
        return self.undo_available

    @property
    def save_available(self):
        return self.undo_available

    @property
    def redo_available(self):
        if self.undid_entries:
            return True
        return False
        # first = next(iter(self.last_log.keys()))
        # while self.last_log[self.back_id].state >= CE_DISCARD and self.back_id > first:
        #     self.back_id -= 1
        # return self.last_id > self.back_id >= first and CE_SUBMITTED_

    def aggregate_rows_unsaved(self, model_cut="", le_id=None) -> [cellEdit]:
        eid: cellEdit
        if le_id:
            unsaved_rows = [ce for eid, ce in self.last_log if ce.state == CE_COMMITTED and eid < le_id]
        else:
            unsaved_rows = [ce for _, ce in self.last_log if ce.state == CE_COMMITTED]
        if model_cut:
            unsaved_rows = [ce for ce in unsaved_rows if ce.model.info.cut_name == model_cut]
        return unsaved_rows
        # for eid in self.unsaved:
        #     if eid.model.info.cut_name == model_cut:
        #         if
        #             model = eid.model
        # pass

    def aggregate_rows(self, model_cut, below_id=None) -> [[cellEdit], ...]:
        pass

    def change_back_id(self, step: int):
        """
        Change self.back_id by step, but skip CE_DISCARD,
         :return True if self.back_id changed
        Note: it don't add new edit entries nor discard them!
         """
        if step > 0:  # redo
            if self.back_id != self.last_id:
                self.back_id += step
                while self.global_log[self.back_id].state >= CE_DISCARD:
                    if self.back_id == self.last_id:
                        return True
                    self.back_id += step
                return True
        elif step < 0:  # undo
            if self.back_id != 0:
                if CE_STOP_ >= self.global_log[self.back_id].state >= CE_STOP:  # CE_SAVED
                    return False
                self.back_id += step
                if CE_STOP_ >= self.global_log[self.back_id].state >= CE_STOP:  # CE_SAVED
                    return True
                # if self.back_id == 0:
                #     return True
                while CE_STOP > self.global_log[self.back_id].state >= CE_DISCARD:
                    if self.back_id == 0:
                        return True
                    self.back_id += step
                return True
        else:
            critical("Error change_back_id")
        return False

    @Slot()
    def redo(self, step=1):  # on calling deactivate any active delegate without saving
        # TODO: add delegate inactivation signal
        global_log_changed = False
        with self.lock:
            #############################
            # pre checks
            # ---------------------------
            if self.undid_entries:
                undo_id, val = self.undid_entries.popitem()
                nce, bi = val
                # if undo_id != self.back_id + 1:
                #     critical("journal undid_entries wrong!!!")
                if self.change_back_id(step):
                    #############################
                    # start change
                    # ---------------------------
                    global_log_changed = True
                    #############################
                    # TODO:  overshadowed ce  change state to committed
                    # ---------------------------
                    # if nce.state <= CE_SHADOWED_:
                    nce.state = CE_DISCARD
                    #############################
                    # check prev saved
                    # ---------------------------
                    for ce in reversed(self.model_row_cols[nce.model.info.cut_name][nce._row_ind]):
                        if ce is nce:
                            pass
                        elif ce.id > self.last_stop_id:
                            if ce.col_name == nce.col_name:
                                if CE_SHADOWED <= ce.state <= CE_SHADOWED_:
                                    ce.state = CE_COMMITTED
                                    break
                        else:
                            break
                    self.last_edit.cache_clear()
                    #############################
                    # announce state
                    # ---------------------------
                    self.model_changed.emit(ce.model.info.cut_name)  # TODO: move to ce._save or state
                    self.journal_changed.emit()
                    #############################
                    # activate widget
                    # ---------------------------
                    with suppress(AttributeError):
                        nce.view.update(nce.view.model().index(nce._row_ind, nce.view.model().index_of_col(ce.col_name)))
                        nce.view.activate()
                        # TODO: move to row/col
        if global_log_changed:
            self.journal_changed.emit()

    @Slot()
    def undo(self, step=-1):  # on calling deactivate any active delegate without saving
        # TODO: add delegate inactivation signal
        global_log_changed = False
        with self.lock:
            bi = self.back_id
            uce = self.global_log[bi]
            #############################
            # only undo unsaved now
            # ---------------------------
            if CE_SHADOWED_ >= uce.state:  # right now only work with unsubmitted changes
                if self.change_back_id(step):
                    self.pending_edit = cellEdit(self, uce.view, uce.model, uce.row_id, uce.col_name,
                                                 uce.value, uce.prev)  # last two swapped
                    pce = self.pending_edit
                    undo_id = super()._commit_edit(uce.model, uce.value, uce.prev)
                    self.undid_entries[undo_id] = (pce, bi)
                    self.back_id = bi + step
                    global_log_changed = True
                    #############################
                    # check prev saved
                    # ---------------------------
                    for ce in reversed(self.model_row_cols[pce.model.info.cut_name][pce._row_ind]):
                        if ce is pce:
                            pass
                        elif ce.col_name == pce.col_name:
                            if ce.state <= CE_COMMITTED_:  # TODO: maybe stop on last_stop_id ?
                                ce.state = CE_SHADOWED
                    #############################
                    # check saved
                    # ---------------------------
                    if self.check_model_saved(pce.model.info.cut_name):
                        pce.state = CE_SAVED
                        pce.model.saved.emit(pce.model)
                    #############################
                    # if previous exist
                    # ---------------------------
                    # if self.back_id in self.global_log.keys():
                    #     uce.state = self.global_log[self.back_id].state
                    #     #############################
                    #     # TODO:  overshadowed ce change state to committed
                    #     # ---------------------------
                    #     if uce.state >= CE_SHADOWED:
                    #         uce.state = CE_COMMITTED
                    #############################
                    # announce saved state
                    # ---------------------------
                    if pce.state == CE_SAVED:
                        ce = pce
                        self.model_changed.emit(ce.model.info.cut_name)  # TODO: move to ce._save or state
                        ce.model.saved.emit(ce.model)  # TODO: call_saved
                        self.journal_changed.emit()
                    #############################
                    # activate widget
                    # ---------------------------
                    with suppress(AttributeError):
                        # uce.view.update(ModelIndex(uce.model, row_id, uce.model.indexOf(column_name)) )
                        # don't try to find index just update layout, maybe change it later
                        uce.view.updateLayout()
                        uce.view.activate()
                        # TODO: move to row/col
                    # bce = self.global_log[self.back_id]
                    # if CE_COMMITTED_ < bce.state:
                else:  # all changes saved
                    uce.model.saved.emit(uce.model)
        if global_log_changed:
            self.journal_changed.emit()

    def check_model_saved(self, cut_name):
        for col, clist in self.model_row_cols[cut_name].items():
            for ce in reversed(clist):
                if ce.id < self.last_stop_id:
                    break
                if ce.state <= CE_COMMITTED_:
                    return False
        return True


class JournalModel(QAbstractTableModel):
    def __init__(self, parent=None):
        super().__init__(parent)
        from safe_shared_data import SD
        self.journal = SD.journal
        self.journal.journal_changed.connect(self.update_view)
        self.rc = 1
        self.__col_count = count()
        self.CSTATE = next(self.__col_count)
        self.CROW = next(self.__col_count)
        self.CMODEL = next(self.__col_count)
        self.CCOL = next(self.__col_count)
        self.CPREV = next(self.__col_count)
        self.CVALUE = next(self.__col_count)
        self.CDEFAULT = next(self.__col_count)
        self.CRELATION = next(self.__col_count)
        self.CRELATION_PREV = next(self.__col_count)

    def headerData(self, section: int, orientation: Qt.Orientation, role: int = Qt.DisplayRole):
        if orientation == Qt.Horizontal and role in (Qt.DisplayRole, Qt.ToolTipRole):
            if section == self.CSTATE:
                return self.tr("Статус")
            elif section == self.CROW:
                return self.tr("ИД")
            elif section == self.CMODEL:
                return self.tr("Таблица")
            elif section == self.CCOL:
                return self.tr("Столбец")
            elif section == self.CPREV:
                return self.tr("Старое значение")
            elif section == self.CVALUE:
                return self.tr("Новое значение")
            elif section == self.CDEFAULT:
                return self.tr("Установлено по умолчанию")
            elif section == self.CRELATION:
                return self.tr("Реляционное старое")
            elif section == self.CRELATION_PREV:
                return self.tr("Реляционное новое")
        return super().headerData(section, orientation, role)

    def _update_view(self):
        debug(f"inserted {self.rowCount() - self.rc} at {self.rc}")
        # self.beginInsertRows(QModelIndex(), self.rc, self.rowCount())
        # self.rc = self.rowCount()
        # self.endInsertRows()
        self.layoutChanged.emit()
        # self.resetInternalData()

    def update_view(self):
        Qtimer_runner(self._update_view, 1000, "JournalModel")

    def rowCount(self, parent=None):
        # return self.rc
        return len(self.journal.global_log)

    def columnCount(self, parent=None):
        return self.CRELATION_PREV

    def data(self, index, role=Qt.DisplayRole):
        col = index.column()
        ce: cellEdit = self.journal.global_log[get_element_by_index(self.journal.global_log, index.row())]
        if role == Qt.DisplayRole:
            if col == self.CSTATE:
                return ce.state
            if ce.state != CE_STOP:
                if col == self.CROW:
                    return ce.row_id
                if col == self.CMODEL:
                    return ce.model.info.cut_name
                elif col == self.CCOL:
                    return ce.col_name
                elif col == self.CPREV:
                    return ce.prev
                elif col == self.CVALUE:
                    return ce.value
                elif col == self.CDEFAULT:
                    return ce.default_values
                else:
                    if ce.model.info.use_relations:
                        try:
                            mcol = ce.model.tsFieldNames.index(ce.col_name)
                            if mcol in ce.model.relColumns:
                                if col == self.CRELATION:
                                    return ce.model.display_value_by_id(mcol, ce.prev)
                                elif col == self.CRELATION_PREV:
                                    return ce.model.display_value_by_id(mcol, ce.value)
                        except IndexError:
                            pass


# @lru_cache(1)
def get_element_by_index(d: dict, ind: int):
    for i, el in enumerate(d):
        if i == ind:
            return el
    else:
        raise IndexError
        # return None
