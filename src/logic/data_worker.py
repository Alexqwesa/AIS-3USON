#!/usr/bin/python3
# -------------------------------------------------------------------------------
# -*- coding: utf-8 -*-
# Name:        AIS 3USON data works logic
# Purpose:
#
# Author:      Savin Alexander Viktorovich aka alexqwesa
# Created:     2019
# Copyright:   Savin Alexander Viktorovich aka alexqwesa
# Licence:     LGPL 3
# This software is licensed under the "LGPLv3" License as described in the "LICENSE" file,
# which should be included with this package. The terms are also available at
# http://www.gnu.org/licenses/lgpl-3.0.html
# -------------------------------------------------------------------------------


# logging.getLogger("3uson").setLevel(logging.DEBUG)
# logging.getLogger("3uson").setLevel(logging.INFO)

#############################
# CONSTANTS
# ---------------------------
import random
import string

from qtpy.QtCore import QRegularExpression as QRegExp

from logic.data_worker_sql_code import _data_worker_SQL_CODE
from widgets.customQWidgets import *


class _data_worker(QObject):
    """data workers functions and inner qwidgets states"""
    # vdate_changed: Signal = Signal(str, str)
    # new_model_ready: Signal = Signal(str)
    contracts_id_changed: Signal = Signal(str, str)
    serv_id_changed: Signal = Signal(str, str)
    ufio_id_changed: Signal = Signal(str, str)
    signals = {}
    __instance = None

    def __new__(cls):
        if _data_worker.__instance is None:
            _data_worker.__instance = QObject.__new__(cls)
        # _data_worker.__instance.val = val
        return _data_worker.__instance

    def __init__(self, parent=None):
        """Constructor for _data_worker"""
        super().__init__(parent)
        self._models = {}
        debug(" init _data_worker")
        self.init = False
        self.__lock = QRecursiveMutex()
        self._locks = {}
        self._old_models: {str: QSqlTableModel} = {}
        #############################
        # fill signals dict
        # ---------------------------
        if not self.signals:
            for sname in self.__annotations__:
                if "_changed" in sname:
                    sign = getattr(self, sname)
                    # if isinstance(sign, Signal):
                    self.signals[sname] = sign
        debug("WD.signals:" + str(self.signals))
        #############################
        # set sql queries dict
        # ---------------------------
        self.sql_query_class = _data_worker_SQL_CODE()
        self.sql_query = self.sql_query_class.sql_query
        self.sql_query_stub_data = self.sql_query_class.sql_query_stub_data

    def locks(self, name) -> QMutex:
        """Lock storage.
        Main usage is to lock filtered models
        """
        with QMutexLocker(self.__lock):
            # if not hasattr(self, "_locks"):
            #     self._locks = {}
            if name not in self._locks:
                self._locks[name] = QRecursiveMutex()
            return self._locks[name]

    def reinit_models(self):
        # TODO: don't update all models at once or use background thread
        self._old_models = self._models
        self._models = {}
        for name in list(WD._old_models.keys()):  # works with copy of keys list
            debug("update model %s ", name)
            mdl = WD.models(name)
            mdl.select()
            debug("updated model %s ", name)
        debug("models updated")
        return True

    #############################
    # add model
    # ---------------------------
    def add_model(self, model_name: str = None,
                  sql: str = None, sql_table: str = None,
                  where: str = None,
                  use_relations=True) -> tsSqlTableModel:
        # , model: tsSqlTableModel = None
        """ Create @model from @sql

        Args:
            self, model_name=None, sql=None,
            sqlTable=None, where=None

        Returns:
            model
        """
        #############################
        # check parameters
        # ---------------------------
        if not (sql or sql_table):
            sql_table = model_name
        if not model_name:
            model_name = sql_table
        if not model_name:
            raise ValueError("model_name not defined")
        debug("add_model %s to %s", model_name, sql_table)
        if model_name in self._models.keys():
            return self._models[model_name]
        #############################
        # create model
        # ---------------------------
        # if model is None:
        if "add_info" in model_name:
            model = bugfix_for_add_info(model_name, self, None, use_relations)
        else:
            model: tsSqlTableModel = tsSqlTableModel(model_name, self, None, use_relations)
        #############################
        # set model
        # ---------------------------
        if sql_table in WD.sql_query.keys():
            sql = WD.sql_query[sql_table].format(*WD.sql_query_stub_data[sql_table])
            #############################
            # use model name(from widget) not from sql
            # ---------------------------
            sql = sql.replace(sql_table, model_name, 1)
            if sql_table not in model_name and sql.count(sql_table) == 0:
                pass
            elif sql_table in model_name and sql.count(sql_table) == 1:
                pass
            else:
                critical("wrong query %s", sql)
            #############################
            # set model core
            # ---------------------------
            if "call " in sql[:30]:
                # model.setObjectName(sql_table)
                model.setCall(sql, WD.sql_query[sql_table])
            else:
                model.setQuery(sql, WD.sql_query[sql_table])
        elif sql_table:
            sql_table = sql_table.replace("_raw", "")
            model.setTable(sql_table, where)
        elif sql:
            model.setQuery(sql)
        #############################
        # add model to dict
        # ---------------------------
        self._models[model_name] = model
        return model

    @property
    def inited_models(self) -> dict:
        return self._models

    @inited_models.setter
    def inited_models(self, val):
        self._models = val

    def model_last_update(self, mdl_name) -> QDateTime:
        mdl: tsSqlTableModel
        last_update: QDateTime = QDateTime.currentDateTime()
        last_update.addDays(-1)
        for mdl in self.inited_models.values():
            if mdl_name == mdl.sql_table():
                if last_update < mdl.last_update:
                    last_update = mdl.last_update
        return last_update

    @staticmethod
    def pw_gen(size=6, chars=string.ascii_letters + string.digits + "+*!@%=?") -> str:
        # + string.punctuation
        chars = [c for c in chars if c != '0' and c != 'O' and c != 'l' and c != 'I']
        return ''.join(random.choice(chars) for _ in range(size))

    def models(self, model_name, tname=None, where_val=None, use_relations=True) -> tsSqlTableModel:
        """
        Get Model from pool, create if not exist, where_val - always updated

        Models defined by sql table/view names +- "_raw",
            but if there are "where" used - it used full name except widget prefix
        (because while all model loaded fully and can be reused, these models only have partial data
            and thus not eligible for reuse )

        :param model_name: unique name of model
        :param tname: sql table/view name
        :param where_val: where always updated
        :param use_relations: deprecated - use _raw
        :return: tsSqlTableModel
        """
        #############################
        # clear filter part (last part)
        # ---------------------------
        if "__where_" in model_name:
            if "__where__" in model_name:
                pass
                # noname where - full name
            else:  # named where
                model_name, _, rpart = model_name.partition("__where_")
                where_name, _, _ = rpart.partition("__")
                model_name = model_name + "__where_" + where_name
        else:
            model_name, sep, rpart = model_name.partition("__")
            # _, sep, flt = (sep + rpart).partition("__by_")
            if "_raw" in model_name:
                use_relations = False
        #############################
        # clear where part
        # ---------------------------
        # if not where:
        #     model_name, sep, where = model_name.partition("__where_")
        # else:
        #     model_name, sep, _ = model_name.partition("__where_")
        #############################
        # return model
        # ---------------------------
        with QMutexLocker(self.locks("model")):
            if model_name in self._models.keys():
                if where_val:
                    self._models[model_name].setFilter(where_val)
                return self._models[model_name]
            elif model_name in self._old_models.keys():
                self._old_models[model_name].last_update = None
                self._old_models[model_name].select()
                self._models[model_name] = self._old_models[model_name]
                self._old_models.pop(model_name)
                return self._models[model_name]
            else:
                #############################
                # create and return model
                # ---------------------------
                where_used = ("__where_" in model_name) or where_val
                if where_used and not where_val:
                    where_val = FALSE_STR
                # if where_used and not tname:
                #     tname, sep, _ = model_name.partition("__where_")
                if not tname:
                    tname, _, _ = model_name.partition("__")
                mdl = self.add_model(model_name, None, tname, where_val, use_relations)
                mdl.where_used = where_used
                return mdl

    def model_by_name(self, tname, prefix, use_relations=True) -> tsSqlTableModel:
        mname = tname[len(prefix):]
        return self.models(mname, use_relations=use_relations)

    def get_status_for(self, ufio, serv, vdate) -> [int, str]:
        tr = self.tr
        if not ufio:
            return 0, tr("укажите получателя СУ")
        if not serv:
            return 0, tr("укажите услугу")
        contr = get_contract(ufio, vdate)
        if contr > 0:
            #############################
            # get services by contract
            # ---------------------------
            qry = QSqlQuery(SD.get_db)
            qry.prepare("""select planned, filled, prim
                from contracts_has_serv 
                where  contracts_id = ? and serv_id = ? """)
            qry.addBindValue(contr)
            qry.addBindValue(serv)
            ret = qry.exec_()
            if ret:
                if qry.next():
                    res = qry.value(0) - qry.value(1)
                    res1 = str(res) + " " + str(qry.value(2))
                    return int(res), str(res1)
                else:
                    return 0, tr("в ИППСУ нет этой услуги!")
            else:
                return 0, tr(" ошибка - не удалось проверить услугу !")
        else:
            return 0, tr("Нет договора (на данную дату)")

    def get_data_from_model_name(self, model_name, mcol_name, id0, id1=None, role=Qt.EditRole, force=False) -> any:
        if not model_name:
            return None
        if model_name in self._old_models:
            return None
        model = self.models(model_name)
        if not model.selection_in_progress or force:
            #############################
            # get data
            # ---------------------------
            ret = self.get_rows_from_model_name(model_name, id0, id1)
            #############################
            # get column
            # ---------------------------
            try:
                col = model.tsFieldNames.index(mcol_name)
            except ValueError:
                col = model.tsFieldNames.index(mcol_name.replace("_id", ""))
            #############################
            # check data and return
            # ---------------------------
            if ret:
                ret = ret[0].siblingAtColumn(col)
                ret = ret.data(role)
            else:
                ret = None
            return ret
        else:
            time.sleep(2)
            # just return whatever we have...
            # TODO: make async method
            return self.get_data_from_model_name(model_name, mcol_name, id0, id1, role, True)

    # TODO: move to model all call from model cached func...
    def get_rows_from_model_name(self, model_name, id0, id1=None, id_field="id", id_field1="") -> [QModelIndex]:
        if not model_name:
            return None
        #############################
        # detect column(s)
        # ---------------------------
        if not id1 and "dep_has_" in model_name:
            pass
        elif id1 and "_has_" in model_name:
            id_field, _, id_field1 = model_name.partition("_by_")
        elif id1:
            id_field = "contracts_id"
            id_field1 = "pddate"
        #############################
        # get data and return
        # ---------------------------
        model = self.models(model_name)
        ret = model.rows_by_id(id0, id_field, id1, id_field1)
        return ret

    def ins_main(self, qry_data) -> Tuple[bool, str]:
        """

        :param: qry_data = (0 - contracts_id,
                1 - dep_id, 2 - ufio_id, 3 - serv_id,
                4 - vdate, 5 - uslnum, 6 - dep_has_worker_id, 7 - note[, 8 - worker_id]):
        :return: ret, msg
        """
        amount = qry_data[5]
        if amount <= 0:  # TODO: more checks
            msg = self.tr("Услуга не добавлена, введите колличество услуг")
            UI.main_window.statusBar().showMessage(msg)
            return False, msg
        qry_data[0] = get_contract(qry_data[2], qry_data[4], qry_data[1])
        debug(" autodetect contract for %s", qry_data)
        #############################
        # insert
        # ---------------------------
        retl = insert_main_table(qry_data)
        ret, rid, err, add_msg = retl
        #############################
        # check result
        # ---------------------------
        if ret:
            debug("new row  " + str(rid))
            msg = self.tr("Услуга добавлена - №" + str(rid)) + add_msg
            UI.main_window.statusBar().showMessage(msg)
            return ret, msg
        else:
            if "Out of range value for column 'contracts_id' at row 1" in err:
                err = self.tr("Возможно у данного человека нет действующего"
                              " договора в этот день \n\n") + err
            critical("can't add service - %s", err)
            QMessageBox.critical(UI.main_window,
                                 self.tr("Не удалось добавить услугу"),
                                 str(err),
                                 QMessageBox.StandardButton.Ok, QMessageBox.StandardButton.NoButton)
        return ret, err


#############################
# make only one instance
# ---------------------------
WD = _data_worker()


def get_contract_sql(ufio, vdate, dep=None):
    if not dep:
        dep = SD.last_dep
    qry = QSqlQuery(SD.get_db)
    qry.prepare("select GET_CONTR (?, ?, ?) as contr")
    qry.addBindValue(ufio)
    qry.addBindValue(vdate)
    qry.addBindValue(dep)
    ret = qry.exec_()
    if ret:
        qry.next()
        return qry.value(0)
    else:
        return -1


def get_contract(ufio, vdate, dep=None):
    if not dep:
        dep = SD.last_dep
    #############################
    # init const
    # ---------------------------
    cmodel: tsSqlTableModel = WD.models("contracts")
    cstart = cmodel.tsFieldNames.index("startdate")
    cend = cmodel.tsFieldNames.index("enddate")
    blocked = cmodel.tsFieldNames.index("blocked")
    r: QModelIndex
    #############################
    # get data from model
    # ---------------------------
    crows_ = cmodel.rows_by_id(ufio, "ufio_id")
    crows = [r for r in crows_ if
             not r.siblingAtColumn(blocked).data(Qt.EditRole) and
             r.siblingAtColumn(cend).data(Qt.EditRole) >= vdate >= r.siblingAtColumn(cstart).data(Qt.EditRole)]
    #############################
    # return contract number
    # ---------------------------
    if len(crows) == 0:
        critical('Нет договора в этот период для этого человека в этом отделении %s - %s - %s', ufio, vdate, dep)
        return 0
    elif len(crows) == 1:
        return crows[0].siblingAtColumn(0).data(Qt.EditRole)
    else:
        critical("Несколько договоров в этот период для этого человека в этом отделении %s - %s - %s", ufio, vdate, dep)
        return -1


# @staticmethod
def insert_main_table(arg):
    """insert into main
        :param: arg = (0 - contracts_id,
                1 - dep_id, 2 - ufio_id, 3 - serv_id,
                4 - vdate, 5 - uslnum, 6 - dep_has_worker_id, 7 - note[, 8 - worker_id]):
        :return: ret, rid, last_error, add_msg """
    #############################
    # check holiday
    # ---------------------------
    add_msg = ""
    date: QDate = arg[4]
    try:
        if len(index_by_id(date, WD.models("holiday"), "holiday")) > 0:
            add_msg = WD.tr(" на выходной день!!!")
        if date.dayOfWeek() > 5:
            add_msg = WD.tr(" на выходной день!!!")
    except:
        pass
    qry = QSqlQuery(SD.get_db)
    qry.prepare("""insert into updatable_main (
               contracts_id, dep_id, ufio_id, serv_id,
               vdate, uslnum, dep_has_worker_id, note) 
               VALUES(?, ?, ?, ?, ?, ?, ?, ?)""")  # , worker_id
    for val in arg:
        qry.addBindValue(val)
    ret = qry.exec_()
    rid = False
    if ret:
        #############################
        # repopulate models
        # ---------------------------
        # Qtimer_runner(insert_main_table_run, 1000, "ins_main")
        insert_main_table_run()
        rid = SD.line_query("SELECT LAST_INSERT_ID();")
    return ret, rid, qry.lastError().text().strip(), add_msg


def insert_main_table_run():
    #############################
    # repopulate models
    # ---------------------------
    for mdl in list(WD.inited_models.keys()):
        if "main" in mdl:
            WD.models(mdl).update_later(WD.models(mdl).filter())
    table: myQTableView
    for table in UI.main_window.findChildren(myQTableView, QRegExp("main")):
        # for table in UI.main_window.findChildren(myQTableView, QRegularExpression("main")):
        try:
            if table.isVisible():
                debug("updated table %s ", table.objectName())
                table.super_model().select()
            else:
                table.model().super_model().update_later()
        except AttributeError:
            pass
