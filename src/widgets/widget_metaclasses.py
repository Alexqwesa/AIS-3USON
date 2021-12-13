#!/usr/bin/python3
# -------------------------------------------------------------------------------
# -*- coding: utf-8 -*-
# Name:        AIS 3USON meta code for custom Qt widgets
# Purpose:     This is the glue that hold together widgets and models
#
# Author:      Savin Alexander Viktorovich aka alexqwesa
# Created:     2019
# Copyright:   Savin Alexander Viktorovich aka alexqwesa
# Licence:     LGPL 3
# This software is licensed under the "LGPLv3" License as described in the "LICENSE" file,
# which should be included with this package. The terms are also available at
# http://www.gnu.org/licenses/lgpl-3.0.html
# -------------------------------------------------------------------------------
import itertools

from qtpy.QtGui import QKeyEvent, QFocusEvent
from qtpy.QtCore import QTime, QEvent

from models.universal_delegate import *


class tsDirtyWidget:
    def __init__(self, parent):
        self._dirty_connected = False
        self._dirty = False

    def isDirty(self):
        return self._dirty

    @Slot(bool)
    def setDirty(self, dirty=True):
        """set dirty for self and all parent"""
        if self._dirty == dirty:
            return
        info("Set dirty myQTableView %s", self.objectName())
        #############################
        # set parent dirty
        # ---------------------------
        self._dirty = dirty
        par: QObject = self.parent()
        while par:
            try:
                par.setDirty(dirty)
            except:
                pass
                # debug("no _dirty property in %s", par.objectName())
            par = par.parent()
        #############################
        # set filters
        # ---------------------------
        for key, flt in self.filters.items():
            flt.setDynamicSortFilter(not dirty)

    #############################
    # to silent syntax highlighter
    # ---------------------------
    if False:
        def setModel(self, model):
            pass

        def objectName(self) -> str:
            pass

        def parent(self) -> QObject:
            pass


class tsFltModelSetWhere(tsDirtyWidget):
    def ts__init__(self, class_prefix="table_", default_filter=""):
        self._locks = {}
        self.__lock = QMutex(QMutex.Recursive)
        self._inited = False
        self.filters: OrderedDict = OrderedDict()  # TODO: use list
        self.__model: Union[tsSqlTableModel, None] = None
        self.__class_prefix = class_prefix
        self.info: Union[WNameParser, None] = None  # WNameParser(self.objectName())

    def locks(self, name):
        """Lock storage"""
        # debug("lock - %s", name)
        with QMutexLocker(self.__lock):
            # if not hasattr(self, "_locks"):
            #     self._locks = {}
            # name = "full"
            if name not in self._locks:
                self._locks[name] = QMutex(QMutex.Recursive)
        return self._locks[name]

    def model(self) -> tsSqlTableModel:
        pass

    def init_model(self, val=None):
        pass

    def set_model(self, model):
        """
        check model (and use fallback model if not found)
        """
        if not isinstance(model, tsSqlTableModel):
            error("not model!!")
            from logic.data_worker import WD
            mdl = WD.models("stub_model")
            mdl.setObjectName("tablestub_model" + QTime.currentTime().toString("HH:mm:ss"))
        self.__model = model
        return True

    def super_model(self) -> tsSqlTableModel:
        try:
            return self.__model.super_model()  # self.__model
        except AttributeError:
            self.__model = self.model()
            return self.__model

    def filter_model(self) -> Union[tsQsfpModel, None]:
        """

        :return: filter model(last in chain) for external usage
        """
        last_ind = len(self.filters.keys()) - 1
        if last_ind >= 0:
            return self.filterAt(last_ind)
        elif self.__model:
            return self.__model
        else:
            return None

    def filterAt(self, filter_index):
        """
        :param filter_index:
        :return: key, filter
        """
        return next(itertools.islice(self.filters.values(), filter_index, filter_index + 1))

    def add_filter_to_chain(self, col_name) -> tsQsfpModel:
        """
        Prepare filter model if needed and set column @col_name for filtering
        """
        # self.init_model()
        flt_name = self.super_model().objectName() + "_by_" + col_name
        #############################
        # column synonyms
        # ---------------------------
        # col_dict = {"you": "worker_id"}
        # if col_name in col_dict.keys():
        #     col_name = col_dict[col_name]
        #############################
        # check indexes
        # ---------------------------
        if flt_name in self.filters.keys():
            self.helper_set_filter_key_column(self.filters[flt_name], col_name)
            warning("resetting column for %s", flt_name)
            return self.filters[flt_name]
        #############################
        # insert QSortFilterProxyModel
        # ---------------------------
        newmdl = tsQsfpModel(self)
        newmdl.setObjectName(flt_name)
        mdl = self.filter_model()
        newmdl.setSourceModel(mdl)
        self.filters[flt_name] = newmdl
        self.super_model().selected.connect(newmdl.invalidate)
        self.setModel(newmdl)
        #############################
        # set filter column to col_name
        # ---------------------------
        # orig = self.convColName(col_name)
        self.helper_set_filter_key_column(newmdl, col_name)
        newmdl.dataChanged.emit(newmdl.index(0, 0), newmdl.index(0, 0))
        return newmdl

    def init_model_filter(self):
        with QMutexLocker(self.locks("init_model_filter")):
            if not self._inited:
                #############################
                # self.info init
                # ---------------------------
                self._inited = True
                self.info: WNameParser = WNameParser(self.objectName())
                self.use_relations = self.info.use_relations
                tname = self.info.full_name
                #############################
                # init model
                # ---------------------------
                from logic.data_worker import WD
                if self.__class_prefix not in tname or tname == self.__class_prefix:
                    error("Wrong table name - %s", tname)
                    mdl = WD.models("stub_model")
                    mdl.setObjectName(
                        self.__class_prefix + "stub_model" + QTime.currentTime().toString("HH:mm:ss"))  # don't use!
                    self.setModel(mdl)
                    return True
                mdl: tsSqlTableModel = WD.model_by_name(self.info.full_name, self.info.prefix, self.info.use_relations)
                #############################
                # set model
                # ---------------------------
                self.set_model(mdl)
                self.setModel(mdl.simply_sorted)
                mdl.change_selection_in_progress.connect(self.update)
                #############################
                # set filters
                # ---------------------------
                flts = tname.split("_by_")
                flts = flts[1:]
                if len(flts) >= 1:
                    flts[-1], _, _ = flts[-1].partition("__")
                    for filter_str in flts:
                        self.add_filter_to_chain(filter_str)
            return True

    def helper_set_filter_key_column(self, newmdl=None, col_name=None):
        """ Set FilterKeyColumn for proxy model of tsFltModel"""
        if not newmdl and not col_name:
            critical("helper_set_filter_key_column")
            return False
        #############################
        # init vars
        # ---------------------------
        if not col_name:
            flt_name = list(self.filters.keys())[
                list(self.filters.values()).index(newmdl)
            ]  # next(i for i, k in enumerate(self.filters.keys()) if k is newmdl)
            _, _, col_name = flt_name.rpartition("_by_")
        if not newmdl:
            flt_name = self.super_model().objectName() + "_by_" + col_name
            newmdl = self.filters[flt_name]
        smodel = newmdl.super_model()
        #############################
        # set FilterKeyColumn
        # ---------------------------
        try:
            new_col_name = col_name
            if col_name[-8:] == "_id_list":
                new_col_name = col_name[:-8]
            col = smodel.index_of_col(new_col_name)
            newmdl.setFilterKeyColumn(col)
        except ValueError:
            error("table %s with model %s has no column %s", self.objectName(), smodel.objectName(), col_name)


class tsFltModelMainMethods(tsFltModelSetWhere):
    def __init__(self, parent=None):
        super().__init__(parent)
        self._delayed_filters = []

    def ts__init__(self, class_prefix="table_", default_filter=""):
        super().ts__init__(class_prefix, default_filter)
        # super(QObject,self).__init__(parent=parent)
        self._delayed_filters = []
        self._delayed_first_filter = None
        self.inited = False  # for use in subclasses
        self.events_disabler = events_disabler(self)
        self.set_filter_data_original = self.set_filter_data
        #############################
        # behavior
        # ---------------------------
        self.set_val_after_filter = 0  # -1 - last, 1 - first

    def _set_first_filter_exact(self, val: str):
        if isinstance(val, int):  # WTF?, str signal connected to int slot? Qt bug!? qt 5.9.7 pyside2-5.15
            if self.filters:
                model_name = self.filterAt(0).objectName().partition("_by_")[2].replace("_id", "")
                return self.set_filter_data(0, val, True, model_name)
        else:
            return self.set_filter_data(0, val, True)

    @Slot(QDate)
    def update_where(self, date_center: QDate):
        if self.init_model_filter():
            mdl = self.super_model()
            mdl.last_filter_str = "vdate between '{}' and '{}'".format(
                date_center.toString(SQL_DATE_FORMAT),
                date_center.toString(SQL_DATE_FORMAT))
            mdl.update_later(mdl.last_filter_str)
            mdl.update_data()

    def _set_where(self, id0: int, model_name):
        if self.init_model_filter():
            #############################
            # get column name
            # ---------------------------
            key = self.objectName()[len(self.info.prefix):]
            debug("set filter %s  value - %s for table - %s ", key, id0, self.objectName())
            _, _, col_name = key.partition("_where_")
            col_name, _, _ = col_name.partition("__")
            #############################
            # get super model table name
            # ---------------------------
            smt_name, _, _ = self.super_model().objectName().partition("__")
            #############################
            #
            # ---------------------------
            self.super_model().set_new_rec_autofill_raw(**{col_name: id0})
            #############################
            # prepare new filter
            # ---------------------------
            val = smt_name + "." + col_name + " = " + str(id0)
            new_filter = val
            if " = " + str(id0) + " " not in self.super_model().filter():
                pass
                # if self.super_model().filter() == TRUE_STR:
                #     new_filter = val
                # elif self.super_model().filter():
                #     new_filter = val + " or " + self.super_model().filter()
                # else:
                #     new_filter = val
            else:
                # where already good, apply filter
                if self._delayed_first_filter is not None:  # TODO: par.isTabVisibleFor(self)
                    self._set_first_filter_exact(self._delayed_first_filter)
                return
            #############################
            # set filter
            # ---------------------------
            self.super_model().update_later(new_filter)
            par = self.parent()
            while not isinstance(par, QTabWidget) and par:
                par = par.parent()
            if par:
                if hasattr(par, "isTabVisibleFor"):
                    if par.isTabVisibleFor(self):  # is needed ?
                        self.super_model().update_data()
                        # QTimer.singleShot(0, self.super_model().update_data)
                else:
                    QTimer.singleShot(2000, self.super_model().update_data)
            else:  # TODO: don't call at all
                QTimer.singleShot(2000, self.super_model().update_data)
            if self._delayed_first_filter is not None:  # TODO: par.isTabVisibleFor(self)
                self._set_first_filter_exact(self._delayed_first_filter)
            return

    @Slot(QObject)
    def replace_model(self, new_model: QObject):
        pass

    @Slot(int, str)
    def set_where(self, id0: int, model_name):
        Qtimer_runner(self._set_where, 0, "temp_set_where_" + self.objectName(), id0, model_name)

    def get_filter_by_num(self, flt_num) -> Union[QSortFilterProxyModel, None]:
        #############################
        # check filter exist
        # ---------------------------
        if len(self.filters) <= flt_num:
            error("no filters set for %s ", self.objectName())
            return
        #############################
        # get filter model
        # ---------------------------
        try:
            flt = next(itertools.islice(self.filters.values(), flt_num, flt_num + 1))
            return flt
        except StopIteration:
            error("no filters set for %s ", self.objectName())
            return

    @lru_cache(1100000)
    def set_filter_data_prepare(self, flt_num, value, exact=False, get_val_from_model_name=None, role=Qt.EditRole):
        #############################
        # get filter
        # ---------------------------
        flt: tsQsfpModel = flt_num
        if isinstance(flt_num, int):
            flt = self.get_filter_by_num(flt_num)
        if flt is None:
            return False
        key = flt.objectName()
        val = value
        debug("start: set filter %s  value - %s for table - %s ", key, val, self.objectName())
        # debug("filter[%s], filter[_]_filterKeyColumn = %s, ", key, self.filters[key].filterKeyColumn())
        #############################
        # get new val from model (filter by not_visible and not_id columns)
        # ---------------------------
        _, _, mcol_name = key.partition("_by_")
        arr = []
        if get_val_from_model_name:
            if mcol_name == "id" or mcol_name[-3:] == "_id":  # TODO:  or mcol_name[-3:] == "_id"
                if value:
                    if self.use_relations:
                        from logic.data_worker import WD
                        val = WD.get_data_from_model_name(get_val_from_model_name, mcol_name, value, None, role)
                    # else:
                    #     val = value
                else:
                    val = ""
            mcol_name_full = mcol_name
            #############################
            # process list of id
            # ---------------------------
            if mcol_name_full[-8:] == "_id_list":
                from logic.data_worker import WD
                val = WD.get_data_from_model_name(get_val_from_model_name, mcol_name, value)
                mcol_name = mcol_name_full[:-8]
                if isinstance(val, int):
                    if val:
                        val = ""
                    elif self.use_relations:
                        val = WD.get_data_from_model_name(get_val_from_model_name, mcol_name, val)
                elif val is None:
                    val = ""
                elif val == "":
                    pass
                else:
                    arr = val.split(",")
                    if arr:
                        for i, id0 in enumerate(arr):
                            if self.use_relations:
                                arr[i] = WD.get_data_from_model_name(get_val_from_model_name, mcol_name, id0)
                            else:
                                arr[i] = int(id0)
                        val = arr
                    else:
                        val = ""
        return flt, val, arr, mcol_name, key

    def set_filter_data(self, flt_num, value, exact=False, get_val_from_model_name=None):
        # QApplication.processEvents() # - crash
        if self.filters:
            ret = self._set_filter_data(flt_num, value, exact, get_val_from_model_name)
            flt, val, arr, mcol_name, key = self.set_filter_data_prepare(flt_num, value, exact, get_val_from_model_name,
                                                                         Qt.DisplayRole)
            self.init_model()
            #############################
            # new record
            # ---------------------------
            if exact:
                if isinstance(val, list):
                    if len(val) == 1:
                        self.super_model().set_new_rec_autofill(**{mcol_name: val[0]})
                else:
                    self.super_model().set_new_rec_autofill(**{mcol_name: val})
            #############################
            # set selected row in QCombobox
            # ---------------------------
            if self.set_val_after_filter:
                if isinstance(self, QComboBox):
                    if self.set_val_after_filter > 0:
                        self.setCurrentIndex(1)
                    else:
                        self.setCurrentIndex(self.model().rowCount() - 2)  # minus special_row and conv to index
            return ret

    @lru_cache(1)
    def _set_filter_data(self, flt_num, value, exact=False, get_val_from_model_name=None):
        with QMutexLocker(self.locks("set_filter_data")):
            #############################
            # check inited
            # ---------------------------
            if not self.init_model_filter():
                self._set_filter_data.cache_clear()
                return None
            # lock.unlock()
            #############################
            # prepare
            # ---------------------------
            try:
                flt, val, arr, mcol_name, key = self.set_filter_data_prepare(flt_num, value, exact,
                                                                             get_val_from_model_name, Qt.DisplayRole)
            except TypeError:
                return False
            #############################
            # set1
            # ---------------------------
            if not self.use_relations and (isinstance(val, int) or isinstance(arr, list) or isinstance(arr, set)):
                debug("done1: filter %s set to %s (%s)", key, value, val)
                # if val != flt.currentFilterRegularExpression():
                flt.setFilterRegularExpression(val)
                return True  # ,  flt.get_filter_set()
            # if isinstance(mcol_name, int): # TODO:  or mcol_name[-3:] == "_id"
            #     from data_worker import WD
            #     val = WD.get_data_from_model_name(get_val_from_model_name, mcol_name, val)
            #############################
            # IF NOT A SET: setup pattern TODO: ?
            # ---------------------------
            # self.filters[key].setFilterFixedString(val)
            if exact:
                if isinstance(val, list):
                    if len(val) == 1:
                        self.super_model().set_new_rec_autofill(**{mcol_name: val[0]})
                else:
                    self.super_model().set_new_rec_autofill(**{mcol_name: val})
                # if val:  # zero string - no filter
                #     re_pattern = flt.prepareREListFixedStr(re_pattern, exact)  # "^" + re_pattern + "$"
            #############################
            # set filter
            # ---------------------------
            re_pattern = flt.prepareREListFixedStr(val, exact)
            debug("done2: filter %s set to %s (%s)", key, value, re_pattern)
            if str(re_pattern) != flt.currentFilterRegularExpression():
                flt.setFilterRegularExpressionPrepared(re_pattern)
            return True  # , re_pattern

    @Slot(str, int)
    @Slot(str, str)
    @Slot(str, QDate)
    def add_new_rec_autofill(self, name, value):
        self.init_model()
        self.super_model().set_new_rec_autofill_raw(**{name: value})

    @Slot(str, int)
    def filter_by_selection_of(self, src_table: str, col_ind: int = 1):
        self.init_model()
        #############################
        # get cells
        # ---------------------------
        from widgets.q_table_view import wsQTableView
        table: wsQTableView = self.parent().parent().findChild(wsQTableView, src_table)
        if not table:
            table = self.topLevelWidget().findChild(wsQTableView, src_table)
        inds = table.selectionModel().selectedIndexes()
        if len(inds):
            mdl = inds[0].model()  # .super_model()
            rows = set()
            dat = set()
            #############################
            # get rows
            # ---------------------------
            for i in inds:
                rows.add(i.row())
            # colind = mdl.record().indexOf("id")
            #############################
            # prepare pattern
            # ---------------------------
            # col=self.filters[key].filterKeyColumn()
            for r in rows:
                dat.add(mdl.data(mdl.index(r, col_ind), Qt.DisplayRole))
                # dat.add(mdl.data(mdl.index(r, col_ind), Qt.EditRole))
            self_mdl: tsSqlTableModel = self.super_model()
            mcol_name = self_mdl.tsFieldNames[col_ind]
            if len(rows) == 1:
                self.super_model().set_new_rec_autofill(**{
                    mdl.super_model().objectName() + "_id": next(iter(dat))
                })
            # if len(rows) == 1:
            #     self.super_model().set_new_rec_autofill(**{
            #         mdl.objectName() + "_id": mdl.data(mdl.index(r, 0), Qt.EditRole)
            #     })
            else:
                self.super_model().set_new_rec_autofill(**{mcol_name: None})
            # str_dat = ["^" + str(x) + "$" for x in dat]
            # re_pattern = "|".join(str_dat)
            #############################
            # set filter
            # ---------------------------
            flt: tsQsfpModel = next(itertools.islice(self.filters.values(), col_ind - 1, col_ind))
            flt.setFilterRegularExpressionPrepared(
                flt.prepareREListFixedStr(
                    dat, exact=True))

    def get_filter_by(self, pattern) -> Union[QSortFilterProxyModel, None]:
        for key, flt in self.filters.items():
            if pattern in key:
                return flt
        return None


class tsFltModel(tsFltModelMainMethods):

    def focusInEvent(self, ev: QFocusEvent):
        UI.last_view = self
        return super().focusInEvent(ev)

    @Slot(int, int, str)
    def set_first_filter(self, ind, id0, text):  # TODO: delete it
        return self.set_filter_data(0, id0, True)

    @Slot(int, str)
    def set_second_filter(self, id0, model_name):
        return self.set_filter_data(1, id0, True, model_name)

    @Slot(int, str)
    def set_first_filter_model(self, id0, model_name):
        return self.set_filter_data(0, id0, True, model_name)

    @Slot(int, str)
    def set_second_filter_model(self, id0, model_name):
        return self.set_filter_data(1, id0, True, model_name)

    @Slot(int, str)
    def set_third_filter_model(self, id0, model_name):
        return self.set_filter_data(2, id0, True, model_name)

    @Slot(int, str)
    def set_fourth_filter_model(self, id0, model_name):
        return self.set_filter_data(3, id0, True, model_name)

    @Slot(str)
    def set_first_filter_str(self, val: str):
        return self.set_filter_data(0, val, False)

    @Slot(str)
    def set_second_filter_str(self, val: str):
        return self.set_filter_data(1, val, False)

    @Slot(QDate)
    def set_first_filter_date(self, val: QDate):
        return self.set_filter_data(0, val, True)

    @Slot(str)
    def set_first_filter_exact(self, val: str):
        if self.filters:
            ffilter_name = self.filterAt(0).objectName().partition("_by_")[2]
            if "_where_" + ffilter_name in self.objectName():
                self._delayed_first_filter = val
            else:
                return self._set_first_filter_exact(val)
        else:
            return self._set_first_filter_exact(val)

    @Slot(str)
    def set_second_filter_exact(self, val: str):
        return self.set_filter_data(1, val, True)

    @Slot(int, str)
    def set_second_filter_exact(self, val: int, model_name: str):
        filter_id = 1
        if isinstance(val, int):  # WTF?, str signal connected to int slot? Qt bug!? qt 5.9.7 pyside2-5.15
            if self.filters:
                dst_model_name = self.filterAt(filter_id).objectName().partition("_by_")[2].replace("_id", "")
                #############################
                # get id from model_name
                # ---------------------------
                if model_name != dst_model_name:
                    from logic.data_worker import WD
                    val2 = WD.get_data_from_model_name(model_name, dst_model_name + "_id", val)
                    return self.set_filter_data(filter_id, val2, True, dst_model_name)
                return self.set_filter_data(filter_id, val, True, model_name)
        else:
            return self.set_filter_data(filter_id, val, True)

    @Slot(bool)
    def disable_events(self, state):
        if state:
            self.installEventFilter(self.events_disabler)
        else:
            self.removeEventFilter(self.events_disabler)
        # QObject.blockSignals(state)

    # @force_reloader
    @reloader
    @try_wrapper
    def debug_event_handler(self, e: QKeyEvent):
        #############################
        # default for new record
        # ---------------------------
        if e.key() == Qt.Key_F4:
            mdl: tsSqlTableModel = self.model().super_model()
            if mdl.default_values:
                mdl.populate_default_values()
                debug("model - %s default_values() - %s", self.model().objectName(), mdl.default_values)
        #############################
        # reinit and select
        # ---------------------------
        if e.key() == Qt.Key_F5:
            mdl = self.model().super_model()
            mdl._meta_init = False
            mdl.select()
            mdl.init()
            debug("model - %s selected()+", mdl.objectName())
        #############################
        # force refilter local proxy models
        # ---------------------------
        if e.key() == Qt.Key_F6:
            if hasattr(self.model(), "invalidateFilter"):
                self.model().invalidateFilter()
                debug("model - %s invalidateFilter()", self.model().objectName())
        #############################
        # filter info
        # ---------------------------
        if e.key() == Qt.Key_F7:
            mdl = self.model()
            debug("=====object is %s %s =====", self.__class__.__name__, self.objectName())
            try:
                debug("modelColumn - %s", self.modelColumn())
            except AttributeError:
                pass
            while mdl:
                if isinstance(mdl, tsQsfpModel):
                    debug("filter %s = %s", mdl.objectName(), mdl.currentFilterRegularExpression())
                    mdl: tsQsfpModel = mdl.sourceModel()
                else:
                    debug("model %s ", mdl.objectName())
                    mdl = False
                    try:
                        debug("index = %s, data = %s, id0 = %s  ",
                              self.currentIndex(),
                              self.currentData(),
                              self.model().data_rc(self.currentIndex(), 0))
                    except AttributeError:
                        pass
            debug("qry_text = %s", self.model().super_model().qry_text)
            debug("selectStatement = %s", self.model().super_model().selectStatement())
        #############################
        # print model
        # ---------------------------
        elif e.key() == Qt.Key_F8:
            debug("F8=====object is %s %s =====", self.__class__.__name__, self.objectName())
            print_model_data(self.model())
        #############################
        # model info
        # ---------------------------
        elif e.key() == Qt.Key_F9:
            debug("F9=====object - %s table - %s model - %s where - %s =====", self.__class__.__name__,
                  self.objectName(),
                  self.super_model().objectName(), self.super_model().filter())
            debug("selectStatement - %s", self.super_model().selectStatement())
            debug("qry_text - %s", self.super_model().qry_text)
            debug("qry_template - %s", self.super_model().qry_template)
            print_model_data(self.model().super_model())
            print(self.super_model().default_values)
        #############################
        # drop filter
        # ---------------------------
        elif e.key() == Qt.Key_F10:
            mdl: tsQsfpModel = self.model()
            debug("F10===== - %s", mdl.currentFilterRegularExpression())
            while hasattr(mdl, "sourceModel"):
                debug("F10===== - %s", mdl.currentFilterRegularExpression())
                if mdl.filterRegularExpression() == "":
                    mdl = mdl.sourceModel()
                else:
                    mdl.setFilterRegularExpression("")
                    break
        #############################
        # add new row
        # ---------------------------
        elif e.key() == Qt.Key_F11:
            mdl: tsQsfpModel = self.model()
            debug("@@--F11=====  - %s, dynamicSortFilter - %s", mdl.currentFilterRegularExpression(),
                  mdl.dynamicSortFilter())
            mdl.setDynamicSortFilter(False)
            mdl.super_model().special_row = None
            mdl.super_model().new_empty_row()
            debug("rowCount super_model - %s, special_row E - %s D - %s", mdl.super_model().rowCount(),
                  mdl.super_model().index(mdl.super_model().special_row, 0).data(Qt.EditRole),
                  mdl.super_model().index(mdl.super_model().special_row, 0).data(Qt.DisplayRole))
            mdl.setDynamicSortFilter(True)
        #############################
        # reset filter and print model twice
        # ---------------------------
        elif e.key() == Qt.Key_F12:
            mdl: tsQsfpModel = self.model()
            debug("F12===== - %s", mdl.currentFilterRegularExpression())
            mdl.setFilterRegularExpression(mdl.currentFilterRegularExpression())
            print_model_data(self.model().super_model())
            debug("===== - %s", mdl.currentFilterRegularExpression())
            print_model_data(self.model().super_model(), Qt.EditRole, None, None)

    @Slot()
    def apply_delayed_filters(self):
        pass

    def call_after_model_changing_actions(self):
        pass


class tsFilteredModelWithDelay(tsFltModel):
    def set_filter_data(self, flt_num, value, exact=False, get_val_from_model_name=None):
        """ Set filter if widget visible otherwise store it for later use"""
        if self.isVisible():
            return super().set_filter_data(flt_num, value, exact, get_val_from_model_name)
        else:
            with QMutexLocker(self.locks("_delayed_filters")):
                if not hasattr(self, "_delayed_filters"):
                    self._delayed_filters = []
                # TODO: convert flt_num?
                self._delayed_filters.append([flt_num, value, exact, get_val_from_model_name])

    @Slot()
    def apply_delayed_filters(self):
        """ Apply stored filters"""
        with QMutexLocker(self.locks("_delayed_filters")):
            if not hasattr(self, "_delayed_filters"):
                self._delayed_filters = []
                return
            flt_set = {x[0] for x in self._delayed_filters}
            for flt in flt_set:
                flt_str = next(
                    (i for i in reversed(self._delayed_filters) if i[0] == flt)
                )
                super().set_filter_data(*flt_str)
            self._delayed_filters = []


class tsFilteredModel(tsFltModel):  # tsFilteredModelWithDelay
    """
    Abstract class for managing filters and add other useful functions
    """

    @Slot(bool)
    def disable_filters(self, disabled):
        if disabled:
            self.set_filter_data = lambda a, b, c="", d="", e="", f="": True
        else:
            self.set_filter_data = self.set_filter_data_original

    # def replacefilterAt(self, filter_index):
    #     """
    #     :param filter_index:
    #     :return: key, filter
    #     """
    #     return next(itertools.islice(self.filters.items(), filter_index, filter_index + 1))


class events_disabler(QObject):
    def eventFilter(self, watched: QObject, event: QEvent) -> bool:
        return True


class tsDependable:
    @Slot("QShowEvent")
    def showEvent(self, ev):
        # TODO: maybe delayed init
        if self.inited:
            if self.model():
                if self.super_model():
                    self.apply_delayed_filters()
                    self.super_model().update_data()
            return super().showEvent(ev)

    @Slot(int, str)
    def change_model(self, id0: int, model_name: str):
        return super().change_model(id0, model_name)

    def init_on_filter(self):
        self.init_model()
        if self.model():
            if self.super_model():
                self.apply_delayed_filters()
                self.super_model().update_data()

    @Slot(int, str)
    def set_where(self, id0: int, model_name):
        self.init_on_filter()
        return super().set_where(id0, model_name)


class WidgetWithMeta(tsFilteredModel, QObject):
    """
    Widget metadate storage-controller
    """

    def __init__(self, parent=None):
        """Constructor for WidgetWithMeta"""
        super().__init__(parent)
