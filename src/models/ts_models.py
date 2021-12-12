#!/usr/bin/python3
# -------------------------------------------------------------------------------
# -*- coding: utf-8 -*-
# Name:        AIS 3USON Custum QT Models
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

import re
#############################
# QT Libraries
# ---------------------------
# from abc import abstractmethod, ABC
# from functools import lru_cache
# from itertools import count

import qtawesome
from qtpy.QtGui import QBrush, QFont
from qtpy.QtSql import QSqlRelationalTableModel, QSqlRelation
# from thirdparty.noconflict import classmaker
#############################
# CONSTANTS
# ---------------------------
from logic.ts_get_contract_data import perc_for
from safe_shared_data import *

TABLE_FOR_DEBUG = "table__dep_has_main__where_vdate__by_vdate"


def locked_init(fn):
    @wraps(fn)
    def ret_fn(self, *args, **kwargs):
        self._dec_rlock = threading.RLock()
        return fn(self, *args, **kwargs)

    return ret_fn


def locked_call(fn):
    @wraps(fn)
    def ret_fn(self, *args, **kwargs):
        self._dec_rlock.acquire()
        try:
            return fn(self, *args, **kwargs)
        finally:
            self._dec_rlock.release()

    return ret_fn


def ClassMethodsDecorator(locked_init, locked_call):
    def decorate(cls):
        cls_src = inspect.getsource(cls)
        for attr, attr_obj in inspect.getmembers(cls, inspect.isroutine):  # cls.__dict__:  types.MethodType
            # attr=attr_obj.__name__
            # if callable(getattr(cls, attr)):
            # if attr_obj is not getattr(super(cls),attr):
            if "__init__" == attr:
                setattr(cls, attr, locked_init(attr_obj))
            elif "def " + attr + "(self" in cls_src:
                setattr(cls, attr, locked_call(attr_obj))
        return cls

    return decorate


class tsQuery(QSqlQuery):
    """Custom query with logging """

    def __init__(self, qry_str=None, db=None):
        """Constructor for tsQuery"""
        if db is None:
            db = SD.get_db
        super().__init__(qry_str, db)

    def prepare(self, query: str) -> bool:
        debug(query)
        return super().prepare(query)


class QSqlRelTableModel_extended:  # QSqlRelModelAbstract
    """
    Just Added some useful methods
    """
    #############################
    # to silent syntax highlighter
    # ---------------------------
    if False:
        def tr(self, *arg, **kwargs):
            pass
            # return super(Signal, self).tr(*arg, **kwargs)

        @abstractmethod
        def model(self):
            pass

        @abstractmethod
        def record(self):
            pass

        @abstractmethod
        def objectName(self):
            pass

        @abstractmethod
        def canFetchMore(self):
            pass

        @abstractmethod
        def fetchMore(self):
            pass

        @abstractmethod
        def match(self, index, role, value, hits, flags):
            pass

        @abstractmethod
        def selectStatement(self):
            pass

        @abstractmethod
        def relationModel(self, column: int):
            pass

        @abstractmethod
        def relation(self, column: int):
            pass

        @abstractmethod
        def data(self, index: QModelIndex, role):
            pass

    def super_model(self):
        return self

    # def sourceModel(self):
    #     return self

    def index_of_col_try(self, col_name):
        ind = self.record().indexOf(col_name)
        if ind == -1:
            try:
                ind = self.tsFieldNames.index(col_name)
            except ValueError:
                if ind == -1 and col_name[-3:] == "_id":
                    ind = self.record().indexOf(col_name[:-3])
        return ind

    def index_of_col(self, col_name, try_alias=True):
        ind = self.record().indexOf(col_name)
        if ind == -1:
            try:
                ind = self.tsFieldNames.index(col_name)
            except ValueError:
                if self.id_alias and try_alias:
                    col_name1 = ""
                    if col_name == self.id_alias:
                        col_name1 = "id"
                    elif col_name == "id":
                        col_name1 = self.id_alias
                    if col_name1:
                        ind = self.index_of_col(col_name1, False)
                        if ind >= 0:
                            return ind
                debug("model - %s don't have col - %s ", self.objectName(), col_name)
                return False
        return ind

    def fetch_all(self):
        """ TODO: """
        # debug("fetching - %s", self.objectName())
        i = count()
        new_data = False
        while self.canFetchMore():
            self.change_selection_in_progress.emit(True)
            debug("fetching --%s-- %s", next(i), self.objectName())
            # Qtimer_runner(self.fetchMore,0,self.objectName()+"fetchMore")
            # QApplication.processEvents()
            self.fetchMore()
            new_data = True
        if new_data:
            self.selected_emitted = True
            self.selected.emit()
        self.change_selection_in_progress.emit(False)
        debug("fetching done - %s - %s", self.objectName(), self.selectStatement())

    def data_rc(self, row: int, col: int, role: int = Qt.EditRole):
        return self.data(self.index(row, col), role)

    def rows_by_id(self, id, id_field="id", id1=None, id_field1="pddate", hits=-1) -> [
        QModelIndex]:
        """Return data in column col in row found by id_field("id" column by default)"""
        if id1:
            #############################
            # two primary keys
            # ---------------------------
            try:
                inds: [QModelIndex] = self.indexes_by_id(id, id_field, hits)
                id1_col = self.index_of_col(id_field1)
                inds = [x for x in inds if x.siblingAtColumn(id1_col).data(Qt.EditRole) == id1]
                ret = inds
            except IndexError:
                return None
        else:
            #############################
            # one primary key
            # ---------------------------
            try:
                inds: QModelIndex = self.indexes_by_id(id, id_field, hits)
                ret = inds
            except IndexError:
                return None
        return ret

    def data_by_id(self, id, column: int, nrow: int = 0, id_field: str = "id", role: int = Qt.EditRole, id1=None,
                   id_field1="pddate"):
        """ return column data of indexes[nrow] found by id """
        arr = self.rows_by_id(id, id_field, id1, id_field1, 1)
        if arr:
            return arr[nrow].siblingAtColumn(column).data(role)
        return None

    def indexes_by_id(self, item, id_field="id", hits=-1) -> [QModelIndex]:  # TODO: rename
        col = self.index_of_col(id_field)
        return self.match_with_fetch(self.index(0, col), item, Qt.EditRole, hits, Qt.MatchExactly)
        # return self.match(self.index(0, col), Qt.EditRole, item, 1, Qt.MatchExactly)

    def index_by_id(self, item, id_field="id") -> [QModelIndex]:  # TODO: rename
        col = self.index_of_col(id_field)
        return self.match_with_fetch(self.index(0, col), item, Qt.EditRole, 1, Qt.MatchExactly)
        # return self.match(self.index(0, col), Qt.EditRole, item, 1, Qt.MatchExactly)

    def id_of_related(self, row, col, role=Qt.EditRole):
        value = self.data_rc(row, col, Qt.DisplayRole)
        if value:
            inds = self.ind_of_related_by_id(value, col, role)
            return inds[0].siblingAtColumn(0).data(role)
        else:
            return None

    def ind_of_related_by_id(self, id_, col, role=Qt.EditRole):
        """Find QModelIndex, try to fetch more record before returning [empty] """
        rel_mdl: tsSqlTableModel = self.relationModel(col)
        rel_col_name = self.relation(col).displayColumn()
        rcol = rel_mdl.fieldIndex(rel_col_name)
        return self.match_with_fetch(rel_mdl.index(0, rcol), id_, role, 1)
        # return rel_mdl.match(rel_mdl.index(0, rcol), role, id_, flags=Qt.MatchExactly)

    def id_of_related_by_value(self, value, col=0, role=Qt.EditRole):
        rel_mdl: tsSqlTableModel = self.relationModel(col)
        if not rel_mdl:
            error("Not a relation!!! in model - %s, column - %s", self.objectName(), col)
            return
        rel_col_name = self.relation(col).displayColumn()
        rcol = rel_mdl.fieldIndex(rel_col_name)
        try:
            inds = match_with_fetch(rel_mdl, rel_mdl.index(0, rcol), value, Qt.DisplayRole, 1)
            if inds:
                return inds[0].siblingAtColumn(0).data(role)
            else:
                return
        #     inds = rel_mdl.match(rel_mdl.index(0, rcol), role, value, flags=Qt.MatchExactly)
        #     return inds[0].siblingAtColumn(0).data(role)
        # except (KeyError, IndexError):  # TODO: raise SqlNotFound
        #     if rel_mdl.canFetchMore():  # TODO: maybe use query?
        #         while rel_mdl.canFetchMore():
        #             rel_mdl.fetchMore()
        #         return self.id_of_related_by_value(value, col, role)
        #     debug("Error: KeyError, IndexError %s of model %s", col, self.objectName())
        #     return
        except AttributeError:
            debug("AttributeError - possible not a relation column %s of model %s", col, self.objectName())
            debug("AttributeError - statement - %s", self.selectStatement())
            return

    def match_with_fetch(self, index, value, role=Qt.EditRole, hits=1, flags=Qt.MatchExactly) -> [QModelIndex]:
        """
        :param index: where to start(and column) - can be index of relation model(not only self.index())
        :return: [QModelIndex]
        """
        inds = self.match(index, role, value, hits, flags)
        if inds:
            return inds
        else:  # TODO: raise SqlNotFound
            if self.canFetchMore():
                while self.canFetchMore():
                    self.fetchMore()
                return self.match_with_fetch(index, value, role, hits, flags)
            # debug("Error: not found val -  %s in model %s", value, self.objectName())
            return []


class QSqlRelTableModelSelectStatus(QSqlRelTableModel_extended, QSqlRelationalTableModel):
    change_selection_in_progress: Signal = Signal(bool)  # TODO: use inner signal and then outer
    selected: Signal = Signal()

    def __init__(self, model_name, parent, db=None, set_relations=True):
        if not db:
            db = SD.get_new_dbconnect(model_name)
        super().__init__(parent, db)
        self.db = db
        self.qry_text = ""
        self._init = False
        self._unselectable_items_by = []
        self.setObjectName(model_name)
        self.setParent(parent)
        self._selection_in_progress = True
        self._locks = {}
        self.__lock = QMutex(QMutex.Recursive)
        self.where_used = False
        self.__update_later = False
        self.__new_where = None
        self.change_selection_in_progress.connect(self.set_selection_in_progress)
        self.selected_emitted = False
        #############################
        # init sql_column_replace
        # ---------------------------
        tr = self.tr
        self.sql_column_replace = {
            "id": tr("№  "),
            "serv_name": tr("Наименование услуги"),
            "serv_tnum": tr("№ по ведомственному перечню"),
            "year": tr("Год   "),
            "price": tr("Стоимость для обслуживаемого"),
            "price2": tr("Стоимость"),
            "price3": tr("Оплата для работника"),
            "sub_serv": tr("№ категории"),
            "sub_serv_str": tr("Категория услуги"),
            "active": tr("Используется"),
            "archive": tr("Архивный"),
            "serv_id": tr("Услуга                                           "),
            "ripso_id": tr("Рипсо         "),
            "dep_id": tr("Отделение   "),
            "contracts_id": tr("Договор     "),
            "serv": tr("Услуга                                              "),
            "ripso": tr("Рипсо       "),
            "dep": tr("Отделение     "),
            "contracts": tr("Договор    "),
            "contracts2": tr("Нов. договор(для внутр. использ.)"),
            "uslnum": tr("Кол-во услуг"),
            "SUM(uslnum)": tr("Услуг всего"),
            "category_id": tr("Категория человека"),
            "note": tr("Примечание"),
            "prim": tr("Примечание "),
            "worker": tr("Работник "),
            "worker_id": tr("Работник"),
            "ufio_id": tr("ФИО                               "),
            "ufio": tr("ФИО                                "),
            "ufio_ufio_2": tr("ФИО                                "),
            "vdate": tr("Дата оказания"),
            "create": tr("Создана     "),
            "ts": tr("Изменена   "),
            "cr_by": tr("Кем создана"),
            "overdid": tr("Переполнение"),
            "ufiobirth": tr("Дата рождения"),
            "ufioDeath": tr("Дата смерти"),
            "upd_by": tr("Кем изменена"),
            "user": tr("Логин"),
            "dep_full_name": tr("Полное название отделения"),
            "dep_puname": tr("Название как в ПУКДССО"),
            "job": tr("Должность"),
            "acronym": tr("Сокращение"),
            "total": tr("Итог по услугам"),
            "planned": tr("Положено услуг"),
            "ufio_short": tr("Фамилия и инициалы"),
            "ESRN": tr("№ ЭСРН      "),
            "snils": tr("СНИЛС            "),
            "phone": tr("Телефон        "),
            "months": tr("Кол-во месяцев"),
            "servform_id": tr("Форма обслуживания"),
            "predv_money": tr("Предв. рассчет оплаты"),
            "curFIO": tr("ФИО на дату         "),
            "psp": tr("Паспорт                             "),
            "address": tr("Адрес                           "),
            "sdd": tr("СДД     "),
            "sdd_date": tr("Дата проверки СДД"),
            "perc": tr("Проценты"),
            "worker_dep": tr("ФИО работника на отделении"),
            "from": tr("c               "),
            "till": tr("по             "),
            "role": tr("Права доступа"),
            "servform": tr("Форма обслуживания    "),
            "pcat": tr("Категория получателей СУ"),
            "tnum": tr("№ по перечню"),
            "content": tr("Содержание"),
            "workload": tr("Нагрузка"),
            "date": tr("Дата     "),
            "msg": tr("Сообщение"),
            "onlyFor": tr("только для ..."),
            "holiday": tr("Праздничные дни"),
            "complex_dep": tr("Группы отделений"),
            "category": tr("Категория"),
            "filled": tr("Выполнено"),
            "pddate": tr("Дата проверки"),  # данных
            "ippsuNum": tr("Номер ИППСУ"),
            "startdate": tr("Дата заключения договора"),
            "enddate": tr("Дата окончания договора"),
            "dep_has_worker": tr("Работник отделения"),
            "lmdate": tr("Дата утверждения ПРЖМИН"),
            "live_min_all": tr("средний ПРЖМИН"),
            "live_min_c": tr("для детей"),
            "live_min_p": tr("для пенсионеров"),
            "live_min_w": tr("для трудосп. возр."),
            "post": tr("Постановление"),
            "post_date": tr("Дата постановления"),
            "setting": tr("Свойства"),
            "value": tr("Значение"),
            "blocked": tr("Запись заблокирована"),
            "prev_uslnum": tr("Предыдущее кол-во услуг")

        }
        #############################
        # set default join mode
        # ---------------------------
        self.setJoinMode(QSqlRelationalTableModel.LeftJoin)
        self.setEditStrategy(QSqlTableModel.OnManualSubmit)
        self.model_need_update.connect(self.update_data, Qt.QueuedConnection)

    def locks(self, name):
        """Lock storage"""
        with QMutexLocker(self.__lock):
            # if not hasattr(self, "_locks"):
            #     self._locks = {}
            if name not in self._locks:
                self._locks[name] = QMutex(QMutex.Recursive)
            return self._locks[name]

    def init(self):
        """
        Replace fields names from sql_column_replace
        """
        if not self._init:
            self._init = True
            #############################
            # replace sql column names
            # ---------------------------
            for i in range(0, self.columnCount()):
                label = self.headerData(i, Qt.Horizontal)
                if label in self.sql_column_replace.keys():
                    label = self.sql_column_replace[label]
                    self.setHeaderData(i, Qt.Horizontal, label)
            debug("model %s inited", self.objectName())

    def get_index_by_id(self, id0, col=0, role=Qt.EditRole):
        return self.match(self.index(0, col), role, id0, 1, Qt.MatchContains)[0]

    def select(self):
        #############################
        # don't run if filter not set (if used)
        # ---------------------------
        if not self.filter() and self.where_used:  # or "__where_" in self.objectName()
            return False
        self.change_selection_in_progress.emit(True)
        self.__update_later = False
        debug("select start for %s", self.objectName())
        ret = super().select()
        # debug("select stop for %s", self.objectName())
        if ret:
            self.selected_emitted = False
            self.init()
            self.fetch_all()
            self.cleanup_after_inner_select()
            if not self.selected_emitted:
                self.selected_emitted = True
                self.selected.emit()
            # QTimer.singleShot(0, self.fetch_all)
            # Qtimer_runner(self.fetch_all, 0, "fetch_all_" + self.objectName())
        else:
            self.change_selection_in_progress.emit(False)  # TODO: rework this
            critical("selection failed - %s", SD.get_db.lastError().text())
        return ret

    def cleanup_after_inner_select(self):
        pass

    # def fetch_all(self):
    #     ret = super().fetch_all()
    #     return ret

    @Slot(bool)
    def set_selection_in_progress(self, val):
        self.selection_in_progress = val

    @property
    def selection_in_progress(self):
        return self._selection_in_progress

    @selection_in_progress.setter
    def selection_in_progress(self, value):
        self._selection_in_progress = value

    @property
    def new_where(self):
        return self.__new_where

    @new_where.setter
    def new_where(self, value):
        self.__update_later = True
        if value:
            self.__new_where = value
        self.model_need_update.emit()

    def update_later(self, new_where: str = ""):
        self.__update_later = True
        self.model_need_update.emit()
        self.__new_where = new_where

    @Slot()
    def update_data(self, force=False):
        if self.__new_where is not None:
            if self.__new_where != self.filter() or force:
                self.setFilter(self.__new_where)
                self.__new_where = None
            # self.select()


class QSqlRelTableModelExtView(QSqlRelTableModelSelectStatus):
    """
    Extended QSqlRelationalTableModel class

    """
    model_need_update: Signal = Signal()

    def __init__(self, model_name, parent, db=None, set_relations=True):
        if not db:
            # db = SD.get_new_dbconnect(model_name)
            db = SD.get_db
        super().__init__(model_name, parent, db, set_relations)
        self.tsFieldTypes = []
        self.tsFieldNames = []
        self.chkColumns = []
        self.roColumns = []
        self.relColumns = []
        self.relroColumns = []
        self.notnullable = []
        self.hidden = []
        self._relations_used = set_relations
        self._special_row = None  # rework this
        self._first_special_row = None
        debug("created %s", model_name)
        self._meta_init = False
        self.call_template = False

    def flags(self, index):
        # try:
        col = index.column()
        fl = super().flags(index)
        if col in self.chkColumns:
            fl = fl | Qt.ItemIsUserCheckable  # | Qt::ItemIsEnabled;
            # return Qt.ItemIsEnabled | Qt.ItemIsSelectable | Qt.ItemIsUserCheckable
        if col in self.roColumns:
            fl = fl & (~Qt.ItemIsEditable)
            # self.roColumns
        if len(self._unselectable_items_by) >= 2:
            if (self._unselectable_items_by[1] == index.siblingAtColumn(
                    self._unselectable_items_by[0]).data(Qt.EditRole)):
                fl = fl & (~(Qt.ItemIsSelectable | Qt.ItemIsEnabled))
                # index.setData(Qt.AlignHCenter, Qt.TextAlignmentRole)
                # index.setData(0, Qt.UserRole - 1)  # hack!!!
        return fl

    @property
    def special_row(self):  # TODO: rename default new row
        return self._special_row  # maybe use -1 instead of None

    @special_row.setter
    def special_row(self, value):
        with QMutexLocker(self.locks("special_row")):
            #############################
            # set _first_special_row
            # ---------------------------
            # if value is None:
            #     self._first_special_row = value
            # else:
            if self._first_special_row is None:
                self._first_special_row = value
            #############################
            # set var
            # ---------------------------
            self._special_row = value

    @property
    def meta_init(self):
        return self._meta_init

    def read_into_2darray(self, fields=None):
        """
        Read model data and return 2d table (list of lists)
        """
        #############################
        # init
        # ---------------------------
        if fields is None:
            fields = []
        row_count0 = self.rowCount0()
        if self.canFetchMore():
            self.select()
        self.init()
        if not fields:
            # fields = self.tsFieldNames
            fields = [self.record().field(i).name() for i in range(self.record().count())]
        #############################
        # get data
        # ---------------------------
        ret = TableByRowsWHeader()
        ret.header = fields
        mdl_col_inds = [self.index_of_col(fld) for fld in fields]
        for r in range(row_count0):
            # with ret(i) as row:
            ret.append()
            for col, mdl_col in enumerate(mdl_col_inds):
                ret[r][col] = self.data(
                    self.index(r, mdl_col),
                    Qt.EditRole)
        # ret = list([[] for i in range(row_count0)])
        # for i, fld in enumerate(fields):
        #     col = self.fieldIndex(fld)
        #     for k in range(row_count0):
        #         ret[k].append(self.data(
        #             self.index(k, col),
        #             Qt.EditRole))
        #############################
        # if single field - return vector
        # ---------------------------
        if len(fields) == 1:
            ret = [x[0] for x in ret]
        #############################
        # return
        # ---------------------------
        return ret

    # def queryChange(self):
    #     str1 = self.query().lastQuery()
    #     inc = 80
    #     i = count(0, inc)
    #     last = next(i)
    #     tmp = str1[last:last + inc]
    #     while tmp:
    #         debug(tmp)
    #         last = next(i)
    #         tmp = str1[last:last + inc]

    def rowCount0(self) -> int:
        if self.special_row is None:
            return self.rowCount()
        else:
            return self.rowCount() - 1

    def sql_table(self):
        """ like tableName but works for various queries """
        table, _, _ = self.objectName().partition("__where")
        table = table.replace("private", "")
        if 'updatable__' not in table:
            table, _, _ = table.partition("__")
            table, _, _ = table.partition("_raw")
            if self.call_template:
                return self.objectName()
        return table

    def add_rel(self, i, label, no_id=False):
        if self._relations_used:
            try:
                shlable = label
                display_col = shlable
                if not no_id:
                    shlable = label[:-3]
                    display_col = shlable
                if label[-3:] == "_id" or no_id:
                    self.setRelation(i,
                                     QSqlRelation(shlable,
                                                  "id",
                                                  display_col))
                    #              + ", relTblAl_" + str(i) + ".id as _real_id_" + shlable)
                    # )  # + ", relTblAl_" + str(i) + ".id as _" + label - undocumented!!!
                    # if i not in self.relColumns:
                    #     self.relColumns.append(i)
            except:
                error("no relation for %s", label)

    def setFilter(self, filter: str):
        # self.init()
        # self.where_used = filter
        with QMutexLocker(self.locks("setFilter")):
            ret = super().setFilter(filter)
            if not self._meta_init:
                error("setMetaInfo double for %s", self.objectName())
                self.setMetaInfo()
            return ret

    def setMetaInfo(self):  # Reimplemented in children
        pass

    # @property
    # def where(self):
    #     return self.__new_where
    #
    # @where.setter
    # def where(self, value):
    #     self.__update_later = True
    #     if value:
    #         self.__new_where = value

    def unselectable_items_by(self, col_name="total", val=1):
        col = self.fieldIndex(col_name)
        self._unselectable_items_by = [col, val]


class QSqlTableModelExtWithMetaData(QSqlRelTableModelExtView):
    """
    Added metadata support
    """

    def __init__(self, model_name, parent, db=None, set_relations=True):
        super().__init__(model_name, parent, db, set_relations)
        self._meta_init = False
        self._init = False
        self.qry_text = ""
        self.select_statm_before_relations = ""
        self._regext_qry_line = re.compile(r'#.*$', re.MULTILINE)
        self.info: MNameParser = None
        if model_name:
            self.setObjectName(model_name)

    def setObjectName(self, name: str):
        ret = super().setObjectName(name)
        if name:
            self.info = MNameParser(name)
        return ret

    @property
    def qry_text_line(self):
        """ Return query as one line without comments"""
        return self._regext_qry_line.sub("", self.qry_text).replace("\n", " ")

    def read_meta_from_qsettings(self):
        """if sql schema didn't changed read fields from QSettings"""
        pass

    def write_meta_to_qsettings(self):
        """ write fields meta info to QSettings"""
        pass

    def setMetaInfo(self, forced=False):
        if not self._meta_init or forced:
            #############################
            # clear
            # ---------------------------
            if self.objectName() == TABLE_FOR_DEBUG:
                pass
            debug(self.objectName())
            #############################
            # read from QSettings
            # ---------------------------
            qset_red = self.read_meta_from_qsettings()
            # if self.objectName() == TABLE_FOR_DEBUG:
            #     debug(self.tsFieldNames)
            #############################
            # autodetect Meta Info
            # ---------------------------
            self._meta_info()
            # debug(self.tsFieldNames)
            #############################
            # write meta to qsettings
            # ---------------------------
            if not qset_red:
                self.write_meta_to_qsettings()
        #############################
        # add relations
        # ---------------------------
        self._update_relations()
        #############################
        # return
        # ---------------------------
        if self.tsFieldNames:
            self.info.tsFieldNames = self.tsFieldNames
            self.info.detect_info()
            self._meta_init = True
        return self._meta_init

    def check_column(self, label, type, i, isnullable=False):
        if "no" in isnullable:
            if main not in self.tableName() and (label == "worker_id" or label == 'dep_has_worker_id'):
                self.notnullable.append(i)
        if "tinyint" in type:
            self.chkColumns.append(i)
        if "id" == label:
            self.roColumns.append(i)
        if label in ["create", "ts"]:
            self.roColumns.append(i)
            # self.dateColumns.append(i)
        if label in ["cr_by", "upd_by"]:
            self.roColumns.append(i)
            self.relroColumns.append(i)
        if "_id" in label[-3:]:
            if "add_info" in self.tableName() and "contracts_id" == label:
                pass  # QTBUG-81572
            else:
                self.relColumns.append(i)
        if "_real_id" in label:
            self.hidden.append(i)

    def _update_relations(self):
        """ reapply relations"""
        #############################
        # save old data
        # ---------------------------
        if not self.select_statm_before_relations:
            self.select_statm_before_relations = self.selectStatement()
        rel_list = list(set(self.relColumns + self.relroColumns))  # deduplicate
        # rel_list.sort(reverse=True)
        #############################
        # add relations
        # ---------------------------
        for i in rel_list:
            if not self.relation(i).isValid():
                if i in self.relroColumns:
                    self.add_rel(i, self.tsFieldNames[i], no_id=True)
                else:
                    self.add_rel(i, self.tsFieldNames[i])
        # #############################
        # # parse selectStatement
        # # ---------------------------
        # self.new_sst = self.selectStatement()
        # new_sst = self.new_sst
        # new_sst, _, _ = new_sst.partition(" FROM")
        # new_sst = new_sst.replace("SELECT", "").replace(" as ", "|").replace(" ", "").replace("`", "")
        # new_sst = new_sst.split(",")

    def _meta_info(self):
        """
        Repopulate model metadata
        :return:
        """
        self.tsFieldNames = []
        self.tsFieldTypes = []
        self.relColumns = []
        self.chkColumns = []
        self.roColumns = []
        self.relroColumns = []
        self.notnullable = []
        self.hidden = []
        #############################
        # get data from _information_schema_columns
        # ---------------------------
        if self.sql_table() == self.tableName():
            if self._main_autodetect_meta_info():
                return True
            else:
                info("can't init %s - probably not enough privileges", self.objectName())
        else:
            #############################
            # try to get data
            # ---------------------------
            if not self.tsFieldNames:  # qset_red
                qry_text = (
                    "show columns from %s" % self.sql_table(),
                    """call SHOW_COL("%s") """ % self.qry_text_line,
                    """call SHOW_COL1("%s") """ % self.qry_text_line
                )
                for qtext in qry_text:
                    qry: QSqlQuery = QSqlQuery(SD.get_db)
                    res = qry.exec_(qtext)
                    if res:
                        return self._second_autodetect_meta_info(qry)
                else:
                    critical("can't detect meta info for %s - maybe empty table?", self.objectName())
        return False

    def _main_autodetect_meta_info(self):
        #############################
        # special case for _information_schema_columns table
        # ---------------------------
        debug("reading _INFORMATION_SCHEMA_COLUMNS for - %s", self.objectName())
        if self.tableName() == "_information_schema_columns":
            self.tsFieldNames = """
            TABLE_NAME, ORDINAL_POSITION, COLUMN_NAME, IS_NULLABLE, COLUMN_DEFAULT, DATA_TYPE, 
            NUMERIC_PRECISION, COLUMN_TYPE, CHARACTER_MAXIMUM_LENGTH
            """.replace("\n", "").replace("\t", "").replace(" ", "").split(",")
            self.tsFieldTypes = ['varchar(64)', 'int(10) unsigned', 'varchar(64)', 'varchar(3)',
                                 'text', 'longtext', 'bigint(10) unsigned', 'mediumtext', 'bigint(21)']
            return True
        #############################
        # ALL other tables
        # ---------------------------
        from models.ts_models_plus import tsQsfpModel_no_new
        table = tsQsfpModel_no_new(self, "_information_schema_columns")
        table.setFilterKeyColumn(0)
        table.setFilterRegularExpression("^" + self.sql_table() + "$")
        st = table.super_model()
        # self.info =
        i = 0
        for i in range((table.rowCount())):
            if i != table.data_rc(i, st.fieldIndex("ORDINAL_POSITION")) - 1:
                error("unexpected error ORDINAL_POSITION!")
            label = table.data_rc(i, st.fieldIndex("COLUMN_NAME"))
            ctype = table.data_rc(i, st.fieldIndex("DATA_TYPE"))
            isnullable = table.data_rc(i, st.fieldIndex("IS_NULLABLE"))
            self.tsFieldNames.append(label)
            self.tsFieldTypes.append(ctype.lower())
            if "no" in isnullable:
                if "main" not in self.tableName() and (label == "worker_id" or label == 'dep_has_worker_id'):
                    self.notnullable.append(i)
            if "tinyint" in ctype:
                self.chkColumns.append(i)
            if "id" == label:
                self.roColumns.append(i)
            if label in ["create", "ts"]:
                self.roColumns.append(i)
                # self.dateColumns.append(i)
            if label in ["cr_by", "upd_by"]:
                self.roColumns.append(i)
                self.relroColumns.append(i)
            if "_id" in label[-3:]:
                # if "add_info" in self.tableName() and "contracts_id" == label:
                #     pass  # QTBUG-81572
                # else:
                self.relColumns.append(i)
                #############################
                # add hidden column
                # ---------------------------
                # self.hidden.append(i)
                # self.tsFieldNames.append("_real_id_" + label[:-3])
                # self.tsFieldTypes.append("int")  # TODO: bigint main table in 32 bit systems?
        if not i:
            error("failed to read _INFORMATION_SCHEMA_COLUMNS for - %s", self.objectName())
        return i

    def _second_autodetect_meta_info(self, qry: QSqlQuery):
        debug("reading sql for - %s", self.objectName())
        ni = qry.record().indexOf('Field')
        ti = qry.record().indexOf('Type')
        i = 0
        if self.objectName() == TABLE_FOR_DEBUG:
            debug(self.objectName())
        while qry.next():
            self.tsFieldNames.append(qry.value(ni))
            self.tsFieldTypes.append(qry.value(ti))
            label = qry.value(ni)
            if "tinyint" in qry.value(ti):
                self.chkColumns.append(i)
            if "id" == label:
                self.roColumns.append(i)
            if "_id" in label:
                self.relColumns.append(i)
            if label in ["create", "ts"]:
                self.roColumns.append(i)
                # self.dateColumns.append(i)
            if label in ["cr_by", "upd_by"]:
                self.roColumns.append(i)
            i += 1
        return i
        # if not self.tsFieldNames:
        #     for i in range(0, self.columnCount()):
        #         label = self.headerData(i, Qt.Horizontal)
        #         self.tsFieldNames.append(label)
        #         self.tsFieldTypes.append(label)
        #         if label in self.sql_column_replace.keys():
        #             label = self.sql_column_replace[label]
        #             self.setHeaderData(i, Qt.Horizontal, label)


class QSqlRelTableModelExtWithMetaData(QSqlTableModelExtWithMetaData):
    """
    Added support for queries and dynamic queries
    """

    def __init__(self, model_name, parent, db=None, set_relations=True):
        super().__init__(model_name, parent, db, set_relations)
        self.qry_template = None
        self.call_template = None
        self.filled_template = ""
        self.last_update = None

    @property
    def id_alias(self):
        if not self.info:
            return ""
        if isinstance(self.info.id_alias, str):
            return self.info.id_alias

    def select(self):
        if not SD.unsaved or SD._recently_saved_model:
            if self.last_update and not self.where_used and not self.filled_template:
                if self.last_update.addSecs(4) > QDateTime.currentDateTime():
                    return
        self.last_update = QDateTime.currentDateTime()
        ret = super().select()
        if (self.call_template or self.qry_template):
            self.setMetaInfo(forced=True)
        return ret

    def setQuery(self, qry_obj, qry_template=None):
        # TODO: cache qry objects
        if qry_template:
            self.qry_template = qry_template
        # else:
        #     qry_template = self.qry_template
        if isinstance(qry_obj, str):
            self.filled_template = qry_obj
            sql = qry_obj
            qry_obj = QSqlQuery(SD.get_db)
            qry_obj.exec_(sql)
            qry_obj.next()
            self.qry_text = sql
        ret = super().setQuery(qry_obj)
        self.select_on_init()
        self.init()
        self.set_selection_in_progress(False)  # self.select() return False for queries, call it here? TODO:
        return ret

    def setCall(self, qry_obj, call_template=None):
        # TODO: cache qry objects
        if call_template:
            self.call_template = call_template
        # else:
        #     call_template = self.call_template
        #############################
        # prepare temporary table
        # ---------------------------
        if isinstance(qry_obj, str):
            self.filled_template = qry_obj
            sql = qry_obj
            qry_obj = QSqlQuery(SD.get_db)
            ret = qry_obj.exec_(sql)
            # if not ret: TODO:
            #     return
            #     self.qry_text=sql
            # qry_obj.next()
            # self.qry_text = sql
        #############################
        # set temporary table
        # ---------------------------
        self.where_used = False
        self._meta_init = False
        self._init = False
        qry_obj1 = QSqlQuery(SD.get_db)
        qry_obj1.exec_("select * from " + self.sql_table())
        #############################
        # setQuery
        # ---------------------------
        ret = self.setQuery(qry_obj1)
        # self.setMetaInfo()
        self.qry_text = "select * from " + self.sql_table()  # TODO: replace to selectStatement
        return ret

    def select_on_init(self):
        return self.select()

    def setTable(self, sql_table, where=None):
        #############################
        # check sql_table exist
        # ---------------------------
        if sql_table not in SD.QSqlAllTables:
            critical("SQL table not found - %s ", sql_table)
            from logic.data_worker import WD
            QMessageBox.critical(UI.main_window,
                                 self.tr("Не удалось найти таблицу"),
                                 str(sql_table),
                                 QMessageBox.StandardButton.Ok, QMessageBox.StandardButton.NoButton)
            # raise ValueError("sql_table %s not found in DataBase" % sql_table)
        #############################
        # set
        # ---------------------------
        self.qry_text = "select * from " + sql_table  # TODO: replace to selectStatement
        ret = super().setTable(sql_table)
        #############################
        # set filter
        # ---------------------------
        if "where" in self.objectName() and not where:
            where = FALSE_STR
        if where:
            self.qry_text = self.qry_text + " where " + where
            self.setFilter(where)
            self.where_used = True
        #############################
        # set meta(if no filter)
        # ---------------------------
        self.setMetaInfo()
        #############################
        # show after conversion into python type
        # ---------------------------
        # rc=self.rowCount()
        # r=self.record()
        # for fi in range(0,r.count()):
        #     f: QSqlField=r.field(fi)
        #     t = f.type()
        #     debug("  %s : %s " , r.fieldName(fi), str(t))
        self.select_on_init()
        return ret

    def edit_role_data(self, index):
        """ Relational column always return display value - this fix it """
        role = Qt.EditRole
        value = super().data(index, role)
        #############################
        # sanity checks
        # ---------------------------
        if index.column() not in self.relColumns:
            return value
        if not value:
            return 0
        #############################
        # check is relational
        # ---------------------------
        rel_mdl = self.relationModel(index.column())
        if not rel_mdl:
            return value
        rel = self.relation(index.column())
        #############################
        # check global cache for actual data
        # ---------------------------
        if isinstance(rel_mdl, QSqlTableModel):  # is it needed?
            #############################
            # get relation data
            # ---------------------------
            col_name = self.tsFieldNames[index.column()]
            if "_id" in col_name:
                try:
                    return SD.key_val[col_name][value]
                except KeyError:
                    #############################
                    # get id by value
                    # ---------------------------
                    ret = value
                    rcol = rel_mdl.fieldIndex(rel.displayColumn())
                    try:
                        rel_ind = rel_mdl.match(rel_mdl.index(0, rcol), Qt.EditRole,
                                                value, flags=Qt.MatchExactly)[0]
                        ret = rel_ind.siblingAtColumn(0).data(Qt.EditRole)
                    except IndexError:
                        while rel_mdl.canFetchMore():  # QModelIndex()
                            rel_mdl.fetchMore()
                        try:
                            rel_ind = rel_mdl.match(rel_mdl.index(0, rcol), Qt.EditRole,
                                                    value, flags=Qt.MatchExactly)[0]
                            ret = rel_ind.siblingAtColumn(0).data(Qt.EditRole)
                        except IndexError:
                            ret = value
                        # error("rel_model 1 no index found")  # TODO - not an error in total reports
                    #############################
                    # update cache
                    # ---------------------------
                    with SD.key_lock:
                        SD.key_val[col_name][value] = ret
                        SD.key_id[col_name][ret] = value
                    return ret
        elif isinstance(rel_mdl, QAbstractTableModel):
            # TODO:
            header = [rel_mdl.headerData(i, Qt.Horizontal, Qt.DisplayRole) for i in
                      range(rel_mdl.columnCount())]
        return value

    def data(self, index: QModelIndex, role: int = Qt.DisplayRole):
        if not index.isValid():
            return
        #############################
        # Qt.EditRole - return id for relation
        # ---------------------------
        elif role == Qt.EditRole:
            if self._relations_used:
                return self.edit_role_data(index)
            return super().data(index, role)
        #############################
        # Qt.DisplayRole for relation col
        # ---------------------------
        elif index.column() in self.chkColumns and role == Qt.DisplayRole:
            return
        elif index.column() in self.relColumns and self._relations_used and role == Qt.DisplayRole:
            value = super().data(index, role)
            #############################
            # WTF?? for some reason relation is half broken for temporary tables
            # ---------------------------
            if self.filled_template or \
                    self.call_template or \
                    self.qry_template or \
                    super().data(index, Qt.EditRole) == value:
                try:  # TODO: use self.display_value_by_id(col, value)
                    value = int(value)
                    rel_mdl = self.relationModel(index.column())
                    rcol = 0  #
                    # rcol=rel_mdl.fieldIndex(rel.displayColumn())
                    try:
                        rel_ind = rel_mdl.match(rel_mdl.index(0, rcol), Qt.EditRole,
                                                value, flags=Qt.MatchExactly)[0]
                    except Exception as err:
                        debug("{}".format(err))
                        # error("rel_model 2 no index found")  # TODO - not an error in total reports
                        return value
                    rel = self.relation(index.column())
                    return rel_ind.siblingAtColumn(rel_mdl.fieldIndex(rel.displayColumn())).data(Qt.DisplayRole)
                except (ValueError, TypeError):
                    pass
            return value
        #############################
        # roleSQL
        # ---------------------------
        elif role == roleSQL:
            res = self.edit_role_data(index)
            res = data_sql_format(res)
            return res
        #############################
        # put checkBox
        # ---------------------------
        elif role == Qt.CheckStateRole:
            if index.column() in self.chkColumns:
                # return
                mark = self.edit_role_data(index)  # index.data(Qt.EditRole)
                if mark:  # no partially checked in sql
                    return Qt.Checked
                else:
                    return Qt.Unchecked
            else:
                return
        #############################
        # ToolTipRole
        # ---------------------------
        elif role == Qt.ToolTipRole:
            dat = index.data(Qt.EditRole)
            if isinstance(dat, QDate):
                return dat.toString("dd.MM.yyyy")
            else:
                return str(index.data(Qt.DisplayRole)) + "(id={})".format(index.data(Qt.EditRole))
        return super().data(index, role)

    def display_value_by_id(self, col, value_id):
        """ Get display value from relation table """
        try:
            value_id = int(value_id)
            # col = index.column()
            rel_mdl = self.relationModel(col)
            rcol = 0  # ID_COL_IN_SQL_TABLE
            # rcol=rel_mdl.fieldIndex(rel.displayColumn())
            try:
                rel_ind = rel_mdl.match(rel_mdl.index(0, ID_COL_IN_SQL_TABLE), Qt.EditRole,
                                        value_id, flags=Qt.MatchExactly)[0]
            except Exception as err:
                debug("{}".format(err))
                # error("rel_model 2 no index found")  # TODO - not an error in total reports
                return value_id
            rel = self.relation(col)
            return rel_ind.siblingAtColumn(rel_mdl.fieldIndex(rel.displayColumn())).data(Qt.DisplayRole)
        except (ValueError, TypeError):
            pass
            return "Relation lookup error - probably not critical - press F5 to fix"


class tsSqltRelTableModelEdit(QSqlRelTableModelExtWithMetaData):
    """
    Added support for submitAll via updatable Views
    """
    unsaved: Signal = Signal(QObject)
    saved: Signal = Signal(QObject)
    setDirty: Signal = Signal(bool)
    new_row_ids_update: Signal = Signal(int, str)

    def __init__(self, model_name, parent, db=None, set_relations=True):
        super().__init__(model_name, parent, db, set_relations)
        self.new_row_ids = {}
        #############################
        # unused
        # ---------------------------
        self.dirty_ids = list()
        self.dirty_rows = list()
        self.dirty_cells = list()
        self.new_rows = []
        self.added_rows = []  # TODO: check by id
        #############################
        # regexp
        # ---------------------------
        control_chars = ''.join(map(chr, list(range(0, 32)) + list(range(127, 160))))
        self.control_char_re = re.compile("[%s]" % re.escape(control_chars))
        self.auto_empty_row_case = False
        self.pending_edit = None
        # self.prev_values = DynamicList(DynamicList(DynamicList()))
        #############################
        # connect signals
        # ---------------------------
        self.unsaved.connect(SD.set_unsaved)
        self.saved.connect(SD.set_saved)
        self.new_row_ids_update.connect(self.new_row_ids_updater)

    @Slot(int, str)
    def new_row_ids_updater(self, row: int, row_id: str):
        self.new_row_ids[row] = row_id

    def remove_control_chars(self, s: str) -> str:
        return self.control_char_re.sub('', s)

    def _set_by_row_id(self, row_id, col_name, value):
        if "new_" in row_id:
            row = int(row_id[4:])
        else:
            row = 0
            while row_id != self.row_id(row):
                row += 1
        col = self.tsFieldNames.index(col_name)
        return self._realSetData(self.index(row, col), value)

    def row_id(self, row):
        """
        Get row number and return row_ + id of record
        or new_ + row number for new string
        """
        #############################
        # get from cache
        # ---------------------------
        if row in self.new_row_ids.keys():
            ret = self.new_row_ids[row]
        #############################
        # get from id
        # ---------------------------
        elif self._first_special_row is not None and row < self._first_special_row:
            tmp = []
            for col in self.info.id_cols:
                tmp.append(super().data(self.index(row, col), roleSQL))
            ret = "row_" + "_".join(tmp)
        #############################
        # get from row number
        # ---------------------------
        else:
            ret = "new_" + str(row)
            self.new_row_ids[row] = ret
        return ret

    def select(self):
        ret = super().select()
        if ret:
            self.new_rows = []
            self.new_row_ids = {}
        self.dirty_ids.clear()
        self.dirty_rows.clear()
        self.dirty_cells.clear()
        #############################
        # primaryKey not autodetect for Views - setPrimaryKey
        # ---------------------------
        # db = SD.get_db
        sql_table, _, _ = self.objectName().partition("__")
        #############################
        # don't needed - only needed for updatable tables
        # ---------------------------
        # if self.primaryKey().name() != "PRIMARY":
        #     # if "_has_" not in sqlTable:
        #     if self.primaryKey().value(0) is None:
        #         if "main" in sql_table:
        #             # _dep_has_main
        #             indx = db.primaryIndex("main")
        #             self.setPrimaryKey(indx)
        #         elif "_dep_has_ufio" in sql_table:
        #             self.setPrimaryKey(db.primaryIndex("ufio"))
        #             # qind = QSqlIndex()
        #             # qind.append(self.record()[0])
        #             # self.setPrimaryKey(qind)
        #         elif "_dep_has_ufio_" in sql_table:
        #             self.setPrimaryKey(db.primaryIndex("contracts"))
        #         elif "_ufio_has_add_info" in sql_table:
        #             self.setPrimaryKey(db.primaryIndex("add_info"))
        #         elif "_ufio_has_contracts" in sql_table:
        #             self.setPrimaryKey(db.primaryIndex("contracts"))
        # thd: QThread = QThread(self)
        # thd.
        # thd = threading.Thread(target=runf) #, args=(, )
        # thd.start()
        # ret = True
        # TODO get return status
        # QTimer.singleShot(0, self.fetch_all)
        return ret

    def submitAll(self):
        #############################
        # submit
        # ---------------------------
        ret = SD.journal.save(0, self.info.cut_name)
        if not ret:
            QMessageBox.critical(self.parent().parent(), self.tr("Ошибка"), self.tr("Не удалось сохранить изменения!"),
                                 QMessageBox.Ok)
        return ret

    def data(self, index: QModelIndex, role: int = Qt.DisplayRole):
        if role == prevData:
            row = index.row()
            col = index.column()
            col_name = self.tsFieldNames[col]
            if self.special_row and row > self.special_row:
                pass
            else:
                return SD.journal.prev_value(self, self.row_id(index.row()), col_name)
                # TODO: implement list return for ToolTips
        else:
            ret = super().data(index, role)
            return ret

    def _realSetData(self, index, value):
        self.pending_edit = (index, value)
        if index.column() == 1:
            # if index.row()
            if self.tsFieldNames[0] == "id":
                if self.special_row and index.row() == self.special_row:
                    pass
                else:
                    # if "id" in self.col_name:
                    # from safe_shared_data import SD
                    with SD.key_lock:
                        SD.key_val[value] = index.siblingAtColumn(0).data(Qt.EditRole)
                        SD.key_id[index.siblingAtColumn(0).data(Qt.EditRole)] = value
        ret = super().setData(index, value, Qt.EditRole)
        self.pending_edit = None
        return ret

    def setData(self, index, value, role):
        #############################
        # check: is action required
        # ---------------------------
        if not index.isValid():
            return
        if index.column() in self.hidden:
            return
        # set_dirty = False
        #############################
        # hack: ignore myQCombobox edites
        # ---------------------------
        for i, view in enumerate(SD.unsaved_view):
            if view.super_model() is self:
                from widgets.q_combo_box import myQComboBox
                if isinstance(view, myQComboBox):
                    SD.unsaved_view.pop(i)
                    return
        #############################
        # checkbox role fix
        # ---------------------------
        if index.column() in self.chkColumns:
            #############################
            # change CheckStateRole role to edit role
            # ---------------------------
            if role == Qt.CheckStateRole:
                if value:  # checked and part checked - the same
                    value = 1
                else:
                    value = 0
                role = Qt.EditRole
                #############################
                # checkbox in tableView don't use delegate
                # ---------------------------
                if not SD.journal.pending_edit or SD.journal.pending_edit.model != self:
                    col_name = self.tsFieldNames[index.column()]
                    SD.start_edit(UI.last_view, self, self.row_id(index.row()), col_name)  # , old_value, val)
        #############################
        # set data
        # ---------------------------
        if role == Qt.EditRole:
            #############################
            # skip auto new row
            # ---------------------------
            if self.auto_empty_row_case:
                ret = super().setData(index, value, role)
                return ret
            #############################
            # check old data
            # ---------------------------
            old_dat = index.data(Qt.EditRole)
            if isinstance(old_dat, str):
                value = str(value)
            elif isinstance(old_dat, int):
                if value == "":
                    value = 0
                elif value is None:
                    value = ""
                else:
                    value = int(value)
            #############################
            # if value changed - set new
            # ---------------------------
            if value != old_dat:
                # set_dirty = True
                self.dirty_ids.append(SD.commit_edit(self, old_dat, value))
                ret = self._realSetData(index, value)
                if ret:
                    # super().setData(index, old_dat, prevData)
                    self.dirty_rows.append(index.row())
                    self.dirty_cells.append((index.row(), index.column()))
                    self.unsaved.emit(self)
                return ret
        return False
        # #############################
        # # enable/disable dynamic filtering
        # # ---------------------------
        # # debug("setData val = %s, ", value)
        # if set_dirty and role == Qt.EditRole and not self.auto_empty_row_case:
        #     for view in SD.unsaved_view:
        #         if view.super_model() is self:
        #             from models.ts_models_plus import tsQsfpModel
        #             mdl: tsQsfpModel = view.model()
        #             while hasattr(mdl, "setDynamicSortFilter"):
        #                 mdl.setDynamicSortFilter(False)
        #                 mdl = mdl.sourceModel()
        # ret = super().setData(index, value, role)
        # if SD.unsaved_view:
        #     if SD.unsaved_view.model().super_model() is self:
        #         mdl.setDynamicSortFilter(True)

    @Slot(QDate)
    def update_where(self, date_center: QDate):
        self.last_filter_str = "vdate between '{}' and '{}'".format(
            date_center.addDays(-CACHE_DAYS).toString(SQL_DATE_FORMAT),
            date_center.addDays(CACHE_DAYS).toString(SQL_DATE_FORMAT))
        self.update_later(self.last_filter_str)
        self.update_data()


# @ClassMethodsDecorator(locked_init, locked_call)
class tsSqlTableModelWithNewRow(tsSqltRelTableModelEdit):
    set_new_row: Signal = Signal(bool)

    def __init__(self, model_name, parent, db=None, set_relations=True):
        super().__init__(model_name, parent, db, set_relations)
        #############################
        # new record autofilled fields
        # ---------------------------
        self.default_values = {}
        # self.auto_empty_row_case = False
        self.delayed = {}

    def revertAll(self):
        super().revertAll()
        self.special_row = None
        self.new_empty_row()
        self.saved.emit(self)

    def select(self):
        # self._dec_rlock.acquire()
        # Qtimer_runner(self._select, 0, "select_" + self.objectName())
        return self._select()

    def _select(self):
        with QMutexLocker(self.locks("select")):
            # QMutexLocker(self.locks("removeRow special_row"))
            if self.special_row is not None:
                # select not always repopulate model, so we can't be sure is it done
                # delete row to be safe
                self.removeRow(self.special_row)
                pass
            # self.data_no_new.cache_clear()  # TODO: don't call twice
            ret = super().select()
            if ret:
                self._first_special_row = self.rowCount0()
            # self._dec_rlock.release()
            return ret

    def insert_row(self, rec: dict):
        """ Insert row from journal journal pending edit"""
        # prev_def = self.default_values
        fkey, fval = rec.popitem()
        ce = SD.journal.pending_edit
        #############################
        # add row
        # ---------------------------
        index = self.index(self.special_row, self.tsFieldNames.index(fkey))
        self.setData(index, fval, Qt.EditRole)
        #############################
        # fill whole record
        # ---------------------------
        for key, val in rec.items():
            col = self.tsFieldNames.index(key)
            self._realSetData(index.siblingAtColumn(col), val)
        ce.default_values = rec
        return ce
        # self.default_values = prev_def

    def removeRow(self, row, index=QModelIndex()):
        self.blockSignals(True)
        if row == self.special_row:
            self.special_row = None
        # if row < 0:
        #     return False
        ret = super().removeRow(row, index)
        self.blockSignals(False)
        # debug("removeRow - %s", SD.get_db.lastError().text())
        return ret

    def fetch_all(self):
        ret = super().fetch_all()
        # self.data_no_new.cache_clear()  # TODO: don't call twice
        #############################
        # new empty row
        # ---------------------------
        self.new_empty_row()
        return ret

    def submitAll(self):
        self.saved.emit(self)
        #############################
        # precheck
        # ---------------------------
        # self.init()
        if self.special_row is not None:
            self.removeRow(self.special_row)
        #############################
        # submit
        # ---------------------------
        ret = super().submitAll()
        if ret:
            SD.reselect_saved_models()
        return ret

    def setData(self, index, value, role):
        if index.row() == self.rowCount() - 1 and role == Qt.EditRole:
            if not self.auto_empty_row_case:
                self.new_rows.append(index.row())
                if isinstance(value, str) and SD.driver_type == "QMYSQL":
                    value = self.remove_control_chars(
                        value)  # QMYSQL bug ? - empty string is str==[0] (with len(str)==1)
                if value:
                    self.new_empty_row(force=True)
                    # self.special_row = index.row() + 1
                # if value is not None and index.column() > 0 and value != "":  # TODO: rework this
                #     if value:
                #         if isinstance(value, str):
                #             if value[0] != value:
                #                 self.insertRecord(-1, self.record())
                #                 self.special_row = index.row() + 1
                #         else:
                #             self.insertRecord(-1, self.record())
                #             self.special_row = index.row() + 1
        # if not self.auto_empty_row_case:
        #     self.data_no_new.cache_clear()
        #     self.data_no_new(index, role)
        ret = super().setData(index, value, role)
        # self.data_no_new(index, role)
        return ret

    def new_empty_row(self, force=False):
        """
        Add new row to model and populate it
        :return:
        """
        with QMutexLocker(self.locks("new_empty_row " + self.objectName())):
            if self.special_row is None or force:
                # if self.special_row != self.rowCount():
                rec = self.record()
                # for key, val in self.default_values.items():
                #     rec.setValue(key, val)
                self.auto_empty_row_case = True
                if self.insertRecord(-1, rec):
                    self.special_row = self.rowCount() - 1
                    self.populate_default_values()
                else:
                    self.special_row = None
                    self.auto_empty_row_case = False
                    return False
                self.auto_empty_row_case = False
                # self.data_no_new.cache_clear()
                return True

    def new_row_data(self, index, role):
        col = index.column()
        try:
            ret = self.default_values[self.tsFieldNames[col]]
        except KeyError:
            if self.tsFieldTypes and self.tsFieldTypes[col] in ["float", "decimal", "double"]:
                return 0
            return
        if role == Qt.EditRole:
            return ret
        elif role == Qt.DisplayRole:
            if col in self.relColumns:  # TODO: or col in self.relrocolumns:
                from logic.data_worker import WD
                model_name = self.tsFieldNames[col].replace("_id", "")
                ret = WD.get_data_from_model_name(model_name, self.tsFieldNames[col], ret)
            return ret
        else:
            return self.data(index, role)

    def populate_default_values(self):
        if self.special_row is None:
            #############################
            # add new row
            # ---------------------------
            self.new_empty_row()
            return
        #############################
        # repopulate exist row
        # ---------------------------
        self.auto_empty_row_case = True
        for key, val in self.default_values.items():
            col = self.index_of_col(key)
            if col >= 0:  # or better raise?
                try:
                    self.setData(self.index(self.special_row, col), val, Qt.EditRole)
                except ValueError:
                    error("populate_default_values %s ValueError $s - %s ", self.objectName(), key, val)
        self.auto_empty_row_case = False
        self.dataChanged.emit(self.index(self.special_row, 0),
                              self.index(self.special_row, self.columnCount()),
                              [Qt.EditRole, Qt.DisplayRole])

    def read_meta_from_qsettings(self):
        """if sql schema didn't changed read fields from QSettings"""
        return False
        # qset: QSettings = SD.qsettings
        # fnd_vers = qset.value(self.objectName() + "_sql_sc_version")
        # ret = False
        # if fnd_vers == SD.sql_sc_version:
        #     debug("reading QSettings for - %s", self.objectName())
        #     for name in self._fields_to_save:
        #         lname = self.objectName() + name
        #         fnd_vers = qset.value(lname + "_sql_sc_version")
        #         # debug("settings version - %s", fnd_vers)
        #         if fnd_vers == SD.sql_sc_version:
        #             ret = True
        #             try:
        #                 size = qset.beginReadArray(lname)
        #                 for i in range(size):
        #                     qset.setArrayIndex(i)
        #                     if name in ["chkColumns", "relColumns", "roColumns"]:
        #                         # getattr(self, name).append(int(qset.value("val")))
        #                         try:
        #                             getattr(self, name).append(int(qset.value("val")))
        #                         except TypeError:  # TODO: fix it
        #                             error("QSettting wrong value - %s - used 0", qset.value("val"))
        #                             debug("TypeError in config - %s, param - %s, val - %s ", self.objectName(), lname,
        #                                   qset.value("val"))
        #                             getattr(self, name).append(0)
        #                     else:
        #                         getattr(self, name).append(qset.value("val"))
        #                 qset.endArray()
        #             except TypeError:
        #                 qset.setValue(self.objectName() + "_sql_sc_version", 0)
        #                 size = qset.beginReadArray(lname)
        #                 for i in range(size):
        #                     qset.setArrayIndex(i)
        #                     qset.setValue("val", 0)
        #                 qset.endArray()
        #                 qset.sync()
        #                 debug("TypeError in config - %s, param - %s ", self.objectName(), lname)
        #                 raise TypeError
        # return ret

    def write_meta_to_qsettings(self):
        """ write fields meta info to QSettings"""
        return
        # if not self.call_template:  # not for dynamic tables
        #     qset: QSettings = SD.qsettings
        #     empty_metadata = True
        #     for name in self._fields_to_save:
        #         lname = self.objectName() + name
        #         #############################
        #         # write array
        #         # ---------------------------
        #         qset.beginWriteArray(lname)
        #         for i, val in enumerate(getattr(self, name)):
        #             empty_metadata = False
        #             qset.setArrayIndex(i)
        #             qset.setValue("val", val)
        #         qset.endArray()
        #         qset.setValue(lname + "_sql_sc_version", SD.sql_sc_version)
        #     #############################
        #     # write confirm if succeeded
        #     # ---------------------------
        #     if not empty_metadata:
        #         qset.setValue(self.objectName() + "_sql_sc_version", SD.sql_sc_version)
        #         debug("wrote %s", self.objectName() + "_sql_sc_version")
        #     else:
        #         debug("%s is empty", self.objectName() + "_sql_sc_version")

    def set_new_rec_autofill(self, **kwargs):
        new_items = kwargs
        for col_name, val in new_items.items():
            #############################
            # if relation - get int value for relation columns
            # ---------------------------
            val2 = val
            if col_name == "id":
                error("Wrong: default value for id col for - %s", self.objectName())
            else:
                if val:
                    #############################
                    # TODO: check if relation value
                    # ---------------------------
                    if (col_name[-3:] == "_id") and self.index_of_col(col_name) in self.relColumns:
                        val2 = self.id_of_related_by_value(val, self.index_of_col(col_name))
                        new_items[col_name] = val2
                        if val2 is None:
                            self.delayed['value'] = val
                            self.delayed['col_name'] = col_name
                            Qtimer_runner(self.delayed_repopulation, 1500, self.objectName() + "delayed_repopulation")
                            return  # TODO: rework this
                else:
                    if col_name not in self.default_values:
                        return
                    val2 = ""
                # if col_name in self.default_values:
                #     if self.default_values[col_name] == val2:
                #         return
        return self.set_new_rec_autofill_raw(**new_items)

    def set_new_rec_autofill_raw(self, **kwargs):
        """
        Set new values for new record
         (for relation column accept display values too)
        :param kwargs: dict of {column_name: value}
        :return:
        """
        new_items = kwargs
        if "dep_id" in self.tsFieldNames and "dep_id" not in new_items:
            new_items = {**new_items, "dep_id": SD.last_dep}
        if "ufio_id" in self.tsFieldNames and "ufio_id" not in new_items and \
                "contracts_id" in new_items and new_items["contracts_id"] and new_items["contracts_id"] > 0:
            from logic.data_worker import WD
            new_items = {**new_items,
                         "ufio_id": WD.get_data_from_model_name("contracts", "ufio_id", new_items["contracts_id"])
                         }
        for col, val in new_items.items():
            self.default_values[col] = val
        self.populate_default_values()

    def delayed_repopulation(self):
        val = self.delayed['value']
        col_name = self.delayed['col_name']
        if (col_name[-3:] == "_id") and self.index_of_col(col_name) in self.relColumns:
            value = self.id_of_related_by_value(val, self.index_of_col(col_name))
            if value:
                self.default_values[col_name] = value
                self.populate_default_values()


class tsSqlTableModelWithColors(tsSqlTableModelWithNewRow):
    """ Class add cell colors to tsSqlTableModel """

    def __init__(self, model_name, parent, db=None, set_relations=True):
        super().__init__(model_name, parent, db, set_relations)
        # self.new_br = QBrush(NEW_ROW_COLOR)
        self.zero_date = QDate(1900, 1, 1)
        self.gray_brush = QBrush(QColor(Qt.gray))
        SD.journal.model_changed.connect(self.get_journal_data_cache_clear)

        @lru_cache(None)
        def _lru_edit_role_data(self, index):
            ret = super().edit_role_data(index)
            return ret

        @lru_cache(None)
        def _lru_data_no_new(self, index, role):
            return self._data_no_new(index, role)

        @lru_cache(None)
        def _lru_get_journal_data(self, index, role):
            return self._get_journal_data(index, role)

        @lru_cache(None)
        def _lru_row_id(self, row):
            ret = super().row_id(row)
            return ret

        @lru_cache(None)
        def _lru_get_index_by_id(self, id0, col, role):
            ret = super().get_index_by_id(id0, col, role)
            return ret

        @lru_cache(None)
        def _lru_data_by_id(self, id, column, nrow, id_field, role, id1, id_field1):
            ret = super().data_by_id(id, column, nrow, id_field, role, id1, id_field1)
            return ret

        @lru_cache(None)
        def _lru_data_rc(self, row, col, role):
            ret = super().data_rc(row, col, role)
            return ret

        self._lru_edit_role_data = _lru_edit_role_data
        self._lru_data_no_new = _lru_data_no_new
        self._lru_get_journal_data = _lru_get_journal_data
        self._lru_row_id = _lru_row_id
        self._lru_get_index_by_id = _lru_get_index_by_id
        self._lru_data_by_id = _lru_data_by_id
        self._lru_data_rc = _lru_data_rc
        # #############################
        # # add lru cache attributes
        # # ---------------------------
        # for attr in self.__dict__:
        #     if "_lru_" == attr[:5]:
        #         class_attr = attr[5:]
        #         method = getattr(self, class_attr)
        #         inst_method = getattr(self, attr)
        #         method.cache_info = inst_method.cache_info
        #         method.cache_clear = inst_method.cache_clear

    # @lru_cache(None)
    def edit_role_data(self, index):
        return self._lru_edit_role_data(self, index)

    # @lru_cache(None)
    def data_no_new(self, index: QModelIndex, role):
        return self._lru_data_no_new(self, index, role)

    # @lru_cache(None)
    def get_journal_data(self, index, role):
        return self._lru_get_journal_data(self, index, role)

    # @lru_cache(None)
    def row_id(self, row):
        return self._lru_row_id(self, row)

    # @lru_cache(maxsizeNone)
    def get_index_by_id(self, id0, col=0, role=Qt.EditRole):
        return self._lru_get_index_by_id(self, id0, col, role)

    # @lru_cache(None)
    def data_by_id(self, id, column: int, nrow: int = 0, id_field: str = "id", role: int = Qt.EditRole, id1=None,
                   id_field1="pddate"):
        ret = self._lru_data_by_id(self, id, column, nrow, id_field, role, id1, id_field1)
        return ret

    # @lru_cache(None)
    def data_rc(self, row: int, col: int, role: int = Qt.EditRole):
        ret = self._lru_data_rc(self, row, col, role)
        return ret

    def select(self):
        ret = super().select()
        self._lru_row_id.cache_clear()
        # self.cache_clear()
        return ret

    def cleanup_after_inner_select(self):
        """ Clean inner structure after select, but before any signal sent"""
        ret = super().cleanup_after_inner_select()
        self.cache_clear()
        return ret

    def new_empty_row(self, force=False):
        ret = super().new_empty_row(force)
        if ret:
            self._lru_row_id.cache_clear()
        return ret

    # @lru_cache(10)
    # def rowCount(self, parent=...) -> int:
    #     return super().rowCount()
    #
    # @lru_cache(10)
    # def columnCount(self, parent=...) -> int:
    #     return super().columnCount()

    def cache_clear(self):
        self._lru_row_id.cache_clear()
        self._lru_get_index_by_id.cache_clear()
        self._lru_data_no_new.cache_clear()
        self._lru_data_by_id.cache_clear()
        self._lru_data_rc.cache_clear()
        self._lru_edit_role_data.cache_clear()
        self._lru_get_journal_data.cache_clear()
        # self.rowCount.cache_clear()
        # self.columnCount.cache_clear()

    def setData(self, index, value, role):
        do_clear = False
        self._lru_row_id.cache_clear()  # TODO: rework it
        if role in (Qt.EditRole, Qt.CheckStateRole):
            # if self.special_row:
            #     if self.special_row > index.row():
            if self.special_row is not None and self.special_row != index.row():
                if index.data(role) != value:
                    do_clear = True
        ret = super().setData(index, value, role)
        # self._lru_row_id.cache_clear()
        if do_clear:
            self.cache_clear()  # TODO: skip for auto new row
        return ret

    def _data_no_new(self, index: QModelIndex, role):
        ret = super().data(index, role)
        return ret

    @Slot(str)
    def get_journal_data_cache_clear(self, model: str):
        if model == self.info.cut_name:
            # if self._dirty:
            if SD.journal.check_model_saved(self.info.cut_name):
                SD.set_saved(self)  # TODO: maybe unsaved check
            self._lru_get_journal_data.cache_clear()  # maybe delayed

    def _get_journal_data(self, index, role):
        row_id = self.row_id(index.row())
        ce: cellEdit
        found, ce = SD.journal.last_edit(self, row_id, self.tsFieldNames[index.column()])
        if found:
            # if CE_DISCARD_ > ce.state >= CE_DISCARD:
            #     pass
            if role == Qt.EditRole:
                return ce.value
            elif role == Qt.DisplayRole:
                col = index.column()
                if col in self.relColumns:
                    return self.display_value_by_id(index.column(), ce.value)
                elif col in self.chkColumns:
                    return
                return ce.value
            elif role == Qt.BackgroundRole:
                if CE_CONFIRMED_ >= ce.state >= CE_SAVED:
                    return NEW_SAVED_COLOR
                elif CE_SUBMITTED_ >= ce.state >= CE_SUBMITTED:
                    return NEW_SUBMITTED_COLOR
                elif ce.state == CE_NEWEST:
                    return NEW_FAIL_NEWEST_COLOR
                elif ce.state > CE_CONFIRMED:
                    return NEW_FAILED_COLOR
                return NEW_UNSAVED_COLOR
            elif role == Qt.CheckStateRole:
                if index.column() not in self.chkColumns:
                    return
                elif ce.value:  # no partially checked in sql
                    return Qt.Checked
                else:
                    return Qt.Unchecked
            else:
                return
        return self.data_no_new(index, role)

    def data(self, index: QModelIndex, role: int = Qt.DisplayRole):  # TODO: check canFetchMore()
        if self._selection_in_progress:
            return
        elif not index.isValid():
            return
        elif role in (Qt.DisplayRole, Qt.EditRole, Qt.BackgroundRole, Qt.CheckStateRole):
            #############################
            # return edited value (from journal)
            # ---------------------------
            # if row in self.dirty_rows:
            # if role in [Qt.EditRole, Qt.CheckStateRole]:
            row = index.row()
            if row == 255 and role == Qt.DisplayRole:
                debug("model - %s, got 255 rows", self.objectName())
            #############################
            # new default row
            # ---------------------------
            if row == self.special_row:
                if role == Qt.BackgroundRole:
                    return NEW_ROW_COLOR
                if role in (Qt.EditRole, Qt.DisplayRole):
                    ret = self.new_row_data(index, role)
                else:  # is it needed ?
                    ret = self.data_no_new(index, role)
                return ret
            #############################
            # journal check
            # ---------------------------
            return self.get_journal_data(index, role)
            #############################
            # colors
            # ---------------------------
            # elif role == Qt.BackgroundRole:
            #     if row in self.new_rows:
            #         # if row in self.dirty_rows:
            #         return NEW_UNSAVED_ROW_COLOR
            #     if row in self.new_row_ids.keys():
            #         return NEW_SAVED_ROW_COLOR
        elif role == Qt.ForegroundRole:
            if self.data(index, Qt.DisplayRole) == self.zero_date:
                return self.gray_brush
        else:
            #############################
            # return original value
            # ---------------------------
            return self.data_no_new(index, role)


class tsSqlTableModelSSorted(tsSqlTableModelWithColors):
    def __init__(self, model_name, parent, db=None, set_relations=True):
        super().__init__(model_name, parent, db, set_relations)
        self._simply_sorted = None

    def data(self, index: QModelIndex, role: int = Qt.DisplayRole):
        ret = super().data(index, role)
        if role == Qt.DisplayRole and index.isValid():
            if self.tsFieldTypes and len(self.tsFieldTypes) > index.column():
                if self.tsFieldTypes[index.column()] in ["float", "decimal", "double"]:
                    ret = "{0:.2f}".format(ret).replace(".", ",")
            else:
                error("tsFieldTypes not inited - %s", self.objectName())
                self.setMetaInfo()
        return ret

    @property
    def simply_sorted(self):
        if not self._simply_sorted:
            from models.ts_models_plus import tsQsfpModel
            self._simply_sorted = tsQsfpModel(self)
            self._simply_sorted.setSourceModel(self)
        return self._simply_sorted


class tsSqlTableModel(tsSqlTableModelSSorted):
    """3SON custum table model"""


class bugfix_for_add_info(tsSqlTableModel):
    def __init__(self, model_name, parent, db=None, set_relations=True):
        super().__init__(model_name, parent, db, set_relations)
        if QApplication.instance():
            self.error_font: QFont = QApplication.instance().font()
            self.error_font.setStrikeOut(True)
            self.error_font.setBold(True)

    @lru_cache(None)
    def perc_for(self, index):
        """
        return percents for SDD in rows (or -1 if fail)
        :param index:
        :return:
        """
        return perc_for(index)

    def cleanup_after_inner_select(self):
        ret = super().cleanup_after_inner_select()
        self.contracts_dict.cache_clear()
        # self.lm_before.cache_clear()
        self.perc_for.cache_clear()
        return ret

    def data(self, index: QModelIndex, role):
        if self.tsFieldNames:  # we have permission to look inside
            ret = super().data(index, role)
            if index.isValid():
                if role in [Qt.DecorationRole, Qt.FontRole]:
                    if index.siblingAtColumn(self.tsFieldNames.index("pddate")).data(Qt.EditRole) and \
                            index.siblingAtColumn(self.tsFieldNames.index("contracts_id")).data(Qt.EditRole) and \
                            index.siblingAtColumn(self.tsFieldNames.index("contracts_id")).data(Qt.EditRole) > 0:
                        if self.tsFieldNames[index.column()] in ["perc"]:
                            #############################
                            # check percents
                            # ---------------------------
                            perc = index.data(Qt.EditRole)
                            if perc >= 0:
                                perc_true = self.perc_for(index)
                                if perc_true >= 0:
                                    if perc != perc_true:
                                        if role == Qt.DecorationRole:
                                            return qtawesome.icon("mdi.window-close")
                                        if role == Qt.FontRole:
                                            return self.error_font
                    # if role == Qt.SizeHintRole :
                    #     return QSize(20,20)
                if role == Qt.DisplayRole:
                    if index.column() == self.tsFieldNames.index("contracts_id"):
                        return self.contracts_dict(index.data(Qt.EditRole))
            return ret

    @lru_cache(maxsize=5000000)
    def contracts_dict(self, id0):
        try:
            from logic.data_worker import WD
            # contracts = WD.models("contracts")
            # ret = contracts.match_with_fetch(
            #     contracts.index(0, 0), id0
            # )[0].siblingAtColumn(1).data(Qt.EditRole)
            ret = WD.get_data_from_model_name("contracts", "contracts", id0)
            return ret
        except:
            return "ERROR"

    def setData(self, index, value, role):
        if self.tsFieldNames:  # we have permission to look inside
            if index.isValid() and role == Qt.EditRole:
                self.perc_for.cache_clear()
                if value and index.column() == self.tsFieldNames.index("contracts_id"):
                    from logic.data_worker import WD
                    mdl = WD.models("contracts")
                    try:
                        return super().setData(index,
                                               mdl.match_with_fetch(mdl.index(0, 1), value)[0].siblingAtColumn(0).data(
                                                   Qt.EditRole),
                                               role)
                    except IndexError:
                        pass
                elif self.auto_empty_row_case:
                    pass
                else:
                    error("wrong index - %s", self.objectName())
            return super().setData(index, value, role)
        return False
