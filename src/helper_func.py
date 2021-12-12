#!/usr/bin/python3
# -------------------------------------------------------------------------------
# -*- coding: utf-8 -*-
# Name:        AIS 3USON helper functions
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
from functools import lru_cache
from inspect import signature
from typing import Union

from qtpy.QtCore import QSortFilterProxyModel, QModelIndex, QObject, QTimer, QMutexLocker, QMutex, QDate
from qtpy.QtSql import QSqlTableModel
from qtpy.QtWidgets import QTabWidget, QStackedWidget, QComboBox
from global_contsants import *
from dev.auto_reloader import *



class myQMutexLocker(QMutexLocker):
    """"""

    def __enter__(self):
        """Constructor for myQMutexLocker"""
        self.line = inspect.stack()[1].lineno
        debug("enter look %s - %s", caller_name(), self.line)
        return super().__enter__()

    def __exit__(self, exc_type, exc_val, exc_tb):
        debug("exit %s", self.line)
        return super().__exit__(exc_type, exc_val, exc_tb)


# QMutexLocker = myQMutexLocker

def is_locked(mutex: QMutex):
    if mutex.try_lock():
        mutex.unlock()
        # print("unlocked")
        return False
    else:
        # print("locked")
        return True


def data_sql_format(res):
    if isinstance(res, str):
        res = "'{}'".format(res)
    elif isinstance(res, QDate):
        res = "'{}'".format(res.toString(SQL_DATE_FORMAT))
    elif res is None:
        # use tsFieldName here
        res = "''"
    else:
        res = str(res)
    return res


def add_method(cls):
    def decorator(func):

        if "self" in signature(func).parameters.keys():
            setattr(cls, func.__name__, types.MethodType(func, cls))
            # setattr(cls, func.__name__,func)
        else:
            @wraps(func)
            def wrapper(self, *args, **kwargs):
                return func(*args, **kwargs)

            setattr(cls, func.__name__, wrapper)
            # Note we are not binding func, but wrapper which accepts self but does exactly the same as func
        return func

    return decorator


def print_ll(cur_table: list):
    return print("\n".join([str(x) for x in cur_table]))


# @reloader
def is_parent_tab_visible(widg: QWidget):
    """ Since Qt isVisible bugged for widgets on tabs"""
    par = widg.parent()
    prev_widget = widg
    while not isinstance(par, QTabWidget):
        if not isinstance(par, QStackedWidget):
            prev_widget = par
        par = par.parent()
    qtab: QTabWidget = par
    debug("%s visible = %s", qtab.objectName(), qtab.isVisible())
    debug("sub widget %s visible = %s", prev_widget.objectName(), prev_widget.isVisible())
    if prev_widget is qtab.currentWidget() and qtab.isVisible():
        if not widg.isVisible():
            error("+++++++++++qt Error - %s", widg.objectName())
        return True
    else:
        return False


class DictReverseDict(dict):
    """
    This dict support:
        [] - get value by key
        () - get key by value

    values and keys should be hashable
    """

    def __init__(self, *a, **kw):
        super().__init__(*a, **kw)
        self._reverse_dict = dict(zip(self.values(), self.keys()))

    def __call__(self, value):
        return self.reverse(value)

    def reverse(self, value):
        return self._reverse_dict[value]

    def __delitem__(self, key):
        value = super().pop(key)
        self._reverse_dict.pop(value, None)

    def __setitem__(self, key, value):
        if key in self:
            del self._reverse_dict[self[key]]  # remove old value
        super().__setitem__(key, value)
        self._reverse_dict[value] = key

    def __repr__(self):
        return f"{type(self).__name__}({super().__repr__()})"

    def update(self, items, **kwargs):
        if kwargs:
            raise NotImplementedError
        if isinstance(items, dict):
            items = items.items()
        for key, value in items:
            self[key] = value
            self._reverse_dict[value] = key

    def pop(self, key=None):
        if key in self:
            value = self[key]
            del self[key]
            del self._reverse_dict[value]
            return value
        elif key is None:
            key = next(reversed(self.keys()))
            value = self[key]
            del self[key]
            del self._reverse_dict[value]
            return value
        else:
            raise KeyError


# @auto_reload_class_code(try_wrapper)
# @auto_reload_class_code(reloader)
class TableByRowsWHeader(list):
    """
    2d Table (list of list), with headers and useful functions:
    row_by_col_value() - return row by value of column,
    support with,
    column names are attribute - return list or element (if used in:  with _instance(row_number)),
    remove_duplicate_with_sum

    >>> dyn = DynamicList(DynamicList("stub"))
    >>> dyn[2][1] = "actual_data"
    >>> print(dyn[2][0])
    stub
    >>> for r in dyn:
    ...    print("{}".format([x for x in r]))
    ['stub', 'stub']
    ['stub', 'stub']
    ['stub', 'actual_data']
    >>> dyn.shrink_2dtable()
    >>> for r in dyn:
    ...    print("{}".format([x for x in r]))
    ['actual_data']
    """

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        object.__setattr__(self, "current_index", None)
        object.__setattr__(self, "header", [])
        # self.current_index = None
        # self.header = []
        # if isinstance(args, self.__class__):
        # for arg in args:
        #     if isinstance(arg, self.__class__):
        #         self.header += arg.header

    def __call__(self, index: int):
        if not self.header:
            raise Exception("No header in TableByRowsWHeader")
        self.current_index = index
        return self

    def append(self, obj=None) -> None:
        # if isinstance(object, list) and len(object) == 0:
        if obj is None:
            obj = []
        if self.header:
            super().append([])
            for _ in self.header:
                self[-1].append(None)
            return
        return super().append(obj)

    def insert(self, ind: int, obj: any) -> None:
        # if isinstance(object, list) and len(object) == 0:
        if self.header:
            super().insert(ind, [])
            for _ in self.header:
                self[ind].append(None)
            return
        return super().insert(ind, obj)

    def row_by_col_value(self, col: Union[int, str], value):
        """ Return index of row with data == value in column == col"""
        if isinstance(col, int):
            return self.index([x for x in self if x[col] == value][0])
        elif isinstance(col, str):
            if self.header:
                try:
                    ind = self.index([x for x in self if x[self.header.index(col)] == value][0])
                    return ind
                except IndexError:
                    return None
            else:
                raise Exception("No header in TableByRowsWHeader")

    def __getattr__(self, attr):
        if self.current_index is not None:
            #############################
            # return item in current row
            # ---------------------------
            if self.header:
                row = self.__getitem__(self.current_index)
                return row.__getitem__(self.header.index(attr))
        else:
            #############################
            # return whole column
            # ---------------------------
            if self.header:
                col = [x.__getitem__(self.header.index(attr)) for x in self]
                return col

    def __setattr__(self, attr, value):
        if attr in self.__dict__:
            return object.__setattr__(self, attr, value)
        if self.current_index is not None:
            #############################
            # return item in current row
            # ---------------------------
            if self.header:
                row = self.__getitem__(self.current_index)
                return row.__setitem__(self.header.index(attr), value)
            else:
                raise Exception("No header in TableByRowsWHeader")
        else:
            raise Exception("No current_index in TableByRowsWHeader")

    def __enter__(self):
        if not self.header:
            raise Exception("No header in TableByRowsWHeader")
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.current_index = None

    def remove_duplicate_with_sum(self, sum_cols=[], ignore_cols=[]):
        """
        :param sum_cols:    columns for sum
        :param ignore_cols: these columns just ignored, other - distinct
        :return:
        """
        rows_to_delete = set()
        #############################
        # sum duplicate and mark rows for delete
        # ---------------------------
        last_to_delete = -1
        for i in range(len(self)):
            if i > last_to_delete:
                for t, row in enumerate(self):
                    if i < t:
                        #############################
                        # compare rows
                        # ---------------------------
                        is_the_same_serv = True
                        for cell, col_name in enumerate(self.header):
                            if cell not in ignore_cols + sum_cols and col_name not in ignore_cols + sum_cols:
                                if self[i][cell] != row[cell]:
                                    is_the_same_serv = False
                                    break
                        #############################
                        # merge rows
                        # ---------------------------
                        if is_the_same_serv:
                            rows_to_delete.add(t)
                            last_to_delete = t
                            for s, col_name in enumerate(self.header):
                                if s in sum_cols or col_name in sum_cols:
                                    self[i][s] += row[s]
                        else:
                            #############################
                            # since it sorted list - skip all other
                            # ---------------------------
                            break
        #############################
        # delete rows
        # ---------------------------
        for i in range(len(self), -1, -1):
            if i in rows_to_delete:
                self.pop(i)


def match_with_fetch(model, index, value, role=Qt.EditRole, hits=1, flags=Qt.MatchExactly) -> [QModelIndex]:
    """
    :param hits:
    :param flags:
    :param value:
    :param role:
    :param model:
    :param index: where to start(and column) - can be index of relation model(not only self.index())
    :return: [QModelIndex]
    """
    inds = model.match(index, role, value, hits, flags)
    if inds:
        return inds
    else:  # TODO: raise SqlNotFound
        if model.canFetchMore():  # TODO: maybe use query?
            while model.canFetchMore():
                model.fetchMore()
            return match_with_fetch(model, index, value, role, hits, flags)
        # debug("Error: not found val -  %s in model %s", value, self.objectName())
        return []


@force_reloader
def print_model_data(model: QSqlTableModel, role=Qt.DisplayRole, rcount=None, ccount=None):
    """print rcount Rows and ccount Columns from model"""
    #############################
    # info
    # ---------------------------
    if isinstance(model, QSortFilterProxyModel):
        print("filterKeyColumn= {}, dynamicSortFilter= {}, filterRole= {} ".format(model.filterKeyColumn(),
                                                                                   model.dynamicSortFilter(),
                                                                                   model.filterRole()))
        print("filterRegularExpression= %s" % model.currentFilterRegularExpression())
        print("Model= %s" % model.objectName())
        print("sourceModel= %s" % model.sourceModel().objectName())
        try:
            print("supermodel= %s , ss = " % model.super_model().objectName(), model.super_model().selectStatement())
        except AttributeError:
            pass
    model_tmp = model
    while hasattr(model_tmp, 'sourceModel'):
        model_tmp = model_tmp.sourceModel()
        print("---------------------------------------")
        try:
            print("Model= {}, filterRegularExpression= {}".format(model_tmp.objectName(),
                                                                  model_tmp.currentFilterRegularExpression()))
            print("filterKeyColumn= {}, dynamicSortFilter= {}, filterRole= {} ".format(model_tmp.filterKeyColumn(),
                                                                                       model_tmp.dynamicSortFilter(),
                                                                                       model_tmp.filterRole()))
        except AttributeError:
            print("==== filter - %s" % model_tmp.filter())
    #############################
    # init
    # ---------------------------
    if not rcount:
        rcount = model.rowCount()
    if not ccount:
        ccount = model.columnCount()
    #############################
    # check bound of model
    # ---------------------------
    if rcount > model.rowCount():    rcount = model.rowCount()
    if ccount > model.columnCount(): ccount = model.columnCount()
    #############################
    # print model head
    # ---------------------------
    res = ""
    for c in range(ccount):
        res = res + " | " + str(c) + " " \
              + str(model.headerData(c,
                                     Qt.Horizontal,
                                     Qt.DisplayRole))
        # .encode('raw_unicode_escape').decode('utf-8')
    print(res)
    #############################
    # print model data
    # ---------------------------
    for r in range(rcount):
        res = ""
        for c in range(ccount):
            ind = model.index(r, c)
            res = res + " | " + str(ind.data(
                role)).replace("QtCore.QDate", "").replace("PyQt5.", "")[:20]
        print(res)
    #############################
    # info again
    # ---------------------------
    if isinstance(model, QSortFilterProxyModel):
        print("filterKeyColumn= {}, dynamicSortFilter= {}, filterRole= {} ".format(model.filterKeyColumn(),
                                                                                   model.dynamicSortFilter(),
                                                                                   model.filterRole()))
        print("filterRegularExpression= %s" % model.currentFilterRegularExpression())
        print("Model= %s" % model.objectName())
        print("sourceModel= %s" % model.sourceModel().objectName())
    model_tmp = model
    while hasattr(model_tmp, 'sourceModel'):
        model_tmp = model_tmp.sourceModel()
        print("---------------------------------------")
        try:
            print("Model= {}, filterRegularExpression= {}".format(model_tmp.objectName(),
                                                                  model_tmp.currentFilterRegularExpression()))
            print("filterKeyColumn= {}, dynamicSortFilter= {}, filterRole= {} ".format(model_tmp.filterKeyColumn(),
                                                                                       model_tmp.dynamicSortFilter(),
                                                                                       model_tmp.filterRole()))
        except AttributeError:
            print("==== filter - %s" % model_tmp.filter())


class MNameParser:
    """
    Class for parsing model names like:
        _dep_has_main__where_vdate__by_vdate_by_serv_id

    >>> self = MNameParser("_dep_has_main__where_vdate__by_vdate_by_serv_id")
    >>> self.cut_name
    main
    >>> self.wheres
    ['vdate']
    >>> self.use_relations
    True
    """

    def __init__(self, model_name):
        self.model_name = model_name
        #############################
        # detect base_name
        # ---------------------------
        # if "__where_" in model_name:
        #     base_name, _, rpart = model_name.partition("__where_")
        #     where_name, _, _ = rpart.partition("__")
        #     # base_name = model_name + "__where_" + where_name
        # else:
        #     base_name, sep, rpart = model_name.partition("__")
        #     # _, sep, flt = (sep + rpart).partition("__by_")
        base_name, sep, rpart = self.model_name.partition("__")
        self.base_name = base_name
        self.sql_name = base_name.replace("_raw", "")
        self.sql_view = False
        self.cut_name = self.sql_name  # a shortest name of table (before check for complex tables)
        self.read_only = False
        if self.sql_name[:1] == "_":
            self.sql_view = True
            self.cut_name = self.sql_name[1:]  # additional cut  # TODO: rename it
        #############################
        # detect relations
        # ---------------------------
        self.use_relations = True
        if "_raw" in base_name:
            self.use_relations = False
        #############################
        # stub
        # ---------------------------
        self.id_alias = ""
        self.tsFieldNames = []
        self.not_for_edit = []  # fields which didn't belong to table_for_edit
        self.table_for_edit = None  # None - not inited, "" - no table
        #############################
        # set where
        # ---------------------------
        self.wheres, _, _ = _parse_right_part_of_name(self.model_name)

    def detect_info(self):  # TODO: don't depend on self.tsFieldNames
        if not self.tsFieldNames:
            return
        if self.table_for_edit is not None:  # TODO: maybe list ?
            return
        self.table_for_edit = self.cut_name  # maybe self.tsFieldNames[1]
        #############################
        # detect simple table
        # ---------------------------
        # 1 id field, assume this is whole table name TODO: two _has_
        self.table_for_edit = self.cut_name  # maybe self.tsFieldNames[1]
        self.ids = [self.tsFieldNames[0]]
        self.id_alias = self.tsFieldNames[1] + "_id"
        self.dependable = False  # maybe move to init?
        #############################
        # detect complex table
        # ---------------------------
        if "_has_" in self.table_for_edit:
            tbl0, _, tbl1 = self.cut_name.partition("_has_")
            if "_has_" in self.tsFieldNames[1]:
                pass  # already detected simple table
            elif tbl0 + "_id" in self.tsFieldNames[:2] and tbl1 + "_id" in self.tsFieldNames[:2]:
                #############################
                # table with 2 id
                # ---------------------------
                # table with 2 id fields, assume this is helper table for multi to multi connection
                self.table_for_edit = self.cut_name  # maybe self.tsFieldNames[1:2] with cut _id ?
                self.ids = [self.tsFieldNames[0], self.tsFieldNames[1]]
                self.id_alias = ""
            else:
                #############################
                # join of 2 tables
                # ---------------------------
                # assume we want to edit records of second table of table0_has_table1
                self.dependable = True
                if tbl1:  # always true except for wrong model name
                    self.table_for_edit = tbl1
                    self.cut_name = self.table_for_edit
                    if self.tsFieldNames[0] == tbl0 + "_id" and self.tsFieldNames[1] == "id":
                        self.ids = [self.tsFieldNames[1]]
                        self.id_alias = self.tsFieldNames[2] + "_id"
                        self.not_for_edit = [self.tsFieldNames[0]]
                    elif self.tsFieldNames[0] == tbl0 + "_id":
                        self.not_for_edit = [self.tsFieldNames[0]]
                    else:  # ordinary table structure
                        self.ids = [self.tsFieldNames[0]]
                        self.id_alias = self.tsFieldNames[1] + "_id"
        if "add_info" in self.table_for_edit:
            # assume add_info is always dependable table
            self.table_for_edit = "add_info"
            self.ids = ["pddate", "contracts_id"]
            self.id_alias = ["pddate", "contracts_id"]
        from safe_shared_data import SD
        self.save_to_tables = [t for t in SD.QSqlAllUpdatableTables if self.table_for_edit in t]
        self.save_to_tables.append(self.cut_name)
        self.save_to_tables.sort(key=mykey)
        self.id_cols = [self.tsFieldNames.index(fld) for fld in self.ids]
        # else:
        #     # cut everything else
        #     _, _, self.table_for_edit = self.table_for_edit.partition("_")


def mykey(item1):
    res = item1
    if "user_has_" in item1:
        res = "_" + res
    if "dep_has_" in item1:
        res = "____" + res
    if "updatable" in item1:
        res = "__" + res
    return res


class WNameParser:
    """
    Class for parsing widget names like:
        table__dep_has_main__where_vdate__by_vdate_by_serv_id

        self.model = ""
        self.sql_table = ""
        self.wheres = []
        self.filters = []
        self.prefix = ""
        self.cbx_col = None
        self.id_alias = ""
        self.rname = ""

    >>> parsed = WNameParser("table__dep_has_main__where_vdate__by_vdate_by_serv_id")
    >>> for at in dir(parsed):
    ...    attr = getattr(parsed, at)
    ...    debug("%s = %s ", at, attr)
    """
    prefixes = ["cbx_0_", "table_", "t_sql_", "clndr_"]

    def __init__(self, name):
        #############################
        #  set vars
        # ---------------------------
        self.full_name = name
        if isinstance(name, QObject):
            self.full_name = name.objectName()
        self.model = ""
        self.sql_table = ""
        # self.wheres = []
        self.filters = []
        self.prefix = ""
        self.id_alias = ""
        self.rname = ""  # TODO: rename it
        # self.use_relations = True
        #############################
        # set cbx_col and prefix
        # ---------------------------
        self.cbx_col = None
        self.prefix = self.full_name[:6]
        if self.full_name[:4] + "0_" in WNameParser.prefixes:
            self.cbx_col = self.full_name[4]
        self.model_name = self.full_name[6:]
        #############################
        # init model info - MNameParser
        # ---------------------------
        self.model_info = MNameParser(self.model_name)
        self.sql_table = self.model_info.base_name
        self.use_relations = self.model_info.use_relations
        self.model = self.model_info.base_name
        #############################
        # parse name
        # ---------------------------
        _, self.filters, rname = _parse_right_part_of_name(self.model_name)
        if "_raw" in self.model:
            self.use_relations = False
        # if self.prefix != "t_sql_":  # Unused?
        # _, _, self.id_alias = self.sql_table.rpartition("_has_")
        # self.id_alias += "_id"
        #############################
        # parse other keys TODO: move it into MNameParser
        # ---------------------------


@lru_cache(1000)
def _parse_right_part_of_name(name):
    """ Get wheres and filters from model name"""
    name_split = name.split("__")
    wheres = []
    filters = []
    rname = ""
    name_split = name_split[1:]
    len_by = len("by_")
    len_where = len("where_")
    for i, key in enumerate(name_split):
        if "where_" in key[:len_where]:
            wheres.append(
                key[len_where:]
            )
        elif "by_" in key[:len_by]:
            for flt in key[len_by:].split("_by_"):
                filters.append(flt)
        else:
            if len(name_split) != i + 1:
                warning("probably wrong name")
            rname = key
    return wheres, filters, rname


def index_by_id(item, model: QSqlTableModel, id_field="id") -> [QModelIndex]:
    col = model.index_of_col(id_field)
    return model.match(model.index(0, col), Qt.EditRole, item, 1, Qt.MatchExactly)


def mapToSuper(proxyIndex: QModelIndex) -> QModelIndex:
    ind = proxyIndex
    model = proxyIndex.model()
    while hasattr(model, 'mapToSource'):
        ind = model.mapToSource(ind)
        model = model.sourceModel()
    return ind


def Qtimer_runner(func: Callable, timeout: int = 400, name: any = None, *args, **kwargs) -> None:
    # QDelayer ? QRunDelayer ? QDelayedRun
    """
    Run Function once after delay, skip repeat calls while delayed
    """
    # TODO: convert to class
    # TODO: update old args on recall
    if not name:
        name = func
        error("probably error no name Qtimer_runner")
    func_with_args = FunctionWithArgs(func, *args, **kwargs)
    #############################
    # if Qtimer isActive - skip
    # ---------------------------
    try:
        if Qtimer_runner.timers[name].isActive():
            # debug("delayed action skipped - %s", func)
            Qtimer_runner.skipped_calls[name] = func
            return
    except AttributeError:
        #############################
        # init if no dict
        # ---------------------------
        Qtimer_runner.timers: dict[QTimer] = {}
        Qtimer_runner.funcs: dict[Callable] = {}
        Qtimer_runner.skipped_calls = {}
        Qtimer_runner.args = {}
        Qtimer_runner.kwargs = {}
        # debug("inited Qtimer_runner")
    except KeyError:
        # debug("new func")
        pass
    #############################
    # add timer for func_with_args
    # ---------------------------
    qtmr: QTimer = QTimer()
    Qtimer_runner.timers[name] = qtmr
    Qtimer_runner.funcs[name] = func_with_args
    qtmr.setSingleShot(True)
    qtmr.setInterval(timeout)
    qtmr.timeout.connect(func_with_args)
    qtmr.start(timeout)
    # debug("delayed action set - %s", func)


class FunctionWithArgs:
    def __init__(self, func: Callable, *args, **kwargs):
        self.func = func
        self.args = args
        self.kwargs = kwargs

    def __call__(self, *a, **b):
        return self.func(*self.args, **self.kwargs)


#############################
# dict what works like class
# ---------------------------
class AttrDict(dict):
    def __init__(self, *args, **kwargs):
        super(AttrDict, self).__init__(*args, **kwargs)
        self.__dict__ = self


#############################
# Dynamic List with table support
# ---------------------------
class DynamicList(list):
    def __init__(self, return_by_default=None, parent=None):
        super().__init__()
        self._newitem = return_by_default
        self._parent = parent
        self.cols = 0
        self.__array_of_array = False
        self.__upd_col_inwork = False
        if isinstance(self._newitem, DynamicList):
            self._newitem = self._newitem._newitem
            self.__array_of_array = True

    def __upd_col(self, newcol):
        if self.__upd_col_inwork:
            return
        self.__upd_col_inwork = True
        self.cols = newcol
        for r in self:
            lenr = len(r)
            # if lenr < newcol:
            #     _ = r[newcol]
            for i in range(lenr, newcol):
                r.__setitem__(i, r._newitem)
        self.__upd_col_inwork = False

    def shrink_2dtable(self):
        #############################
        # shrink rows from start
        # ---------------------------
        for i, row in enumerate(self[:]):
            if not [x for x in row if x != self._newitem]:
                self.remove(row)
            else:
                # stop on first non empty row
                break
        #############################
        # shrink rows from end
        # ---------------------------
        for i, row in enumerate(reversed(self[:])):
            if not [x for x in row if x != self._newitem]:
                self.remove(row)
            else:
                # stop on first non empty row
                break
        #############################
        # shrink columns from start
        # ---------------------------
        col = 0
        # row: list = []
        for _ in self[0][:]:
            column = (r[col] for r in self)
            try:
                t = next(x for x in column if x != self._newitem)
                # stop on first non empty col
                break
            except StopIteration:
                for row in self:
                    # row=row[1:]
                    row.remove(self._newitem)
                self.cols -= 1
        #############################
        # shrink columns from end
        # ---------------------------
        col = -1
        # row: list = []
        for _ in self[0][:]:
            column = (r[col] for r in self)
            try:
                t = next(x for x in column if x != self._newitem)
                # stop on first non empty col
                break
            except StopIteration:
                for row in self:
                    row.pop()
                self.cols -= 1
        return

    def __getitem__(self, index):
        if isinstance(index, slice):  # don't support slices yet
            return super().__getitem__(index)
        while index >= len(self):
            #############################
            # append if needed
            # ---------------------------
            if self.__array_of_array:
                self.append(DynamicList(self._newitem, self))  # TODO: use generators
            else:
                self.append(self._newitem)
        #############################
        # update parent
        # ---------------------------
        if self._parent:
            if self._parent.cols < len(self):
                self._parent.__upd_col(len(self))
        else:
            if index + 1 < len(self):
                self.cols = index - 1
        return super().__getitem__(index)

    def __setitem__(self, index, value):
        self.__getitem__(index)
        super().__setitem__(index, value)


def get_cbox_data(cbx: QComboBox, col=0, role=Qt.EditRole):
    row = cbx.currentIndex()
    ind = cbx.model().index(row, col)
    return cbx.model().data(ind, role)


def main():
    import doctest

    doctest.testmod()


if __name__ == "__main__":
    main()
