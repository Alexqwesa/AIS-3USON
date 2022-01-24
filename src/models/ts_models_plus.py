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

from qtpy.QtCore import QByteArray, QRegularExpression
from qtpy.QtWidgets import QDataWidgetMapper

from models.ts_models import *


class tsQDataWidgetMapper(QDataWidgetMapper):
    """ """
    # unsaved: Signal = Signal(QObject)
    # saved: Signal = Signal()
    # setDirty: Signal = Signal(bool)
    # _class_dirty: bool = False
    call_activate: Signal = Signal(str)

    def __init__(self, parent=None):
        """Constructor for tsQDataWidgetMapper"""
        super().__init__(parent)
        self._dirty = False
        self._mapped = {}
        self._init_mapped = False
        # self.setSubmitPolicy(QDataWidgetMapper.ManualSubmit)
        self.setSubmitPolicy(QDataWidgetMapper.AutoSubmit)
        # UI.main_window.setDirty.connect(self.setDirty)
        # self.setDirty.connect(QApplication.topLevelWidgets()[0].setDirty)
        # self.setDirty.connect()
        # self.setItemDelegate(tsItemDelegate(self))
        self.call_activate.connect(self.activate, Qt.QueuedConnection)

    @Slot()
    @Slot(str)
    def activate(self, col_name=""):
        model: tsSqlTableModel = self.super_model()
        if model and model.tsFieldNames:
            col = model.tsFieldNames.index(col_name)
            if col in self._mapped:
                #############################
                # activate tab with widget # TODO: activate record too!
                # ---------------------------
                widget = self._mapped[col][0]
                p = widget.parent()
                from widgets.customQWidgets import myQWidget
                while p and not isinstance(p, myQWidget):
                    p = p.parent()
                self.itemDelegate().setEditorData(widget, self.model().index(self.currentIndex(), col))
                p.activate()
                #############################
                # update
                # ---------------------------
                # widget.setFocus() # make it work!
                # widget.update()  # is needed?

    def addMapping(self, widget, section, propertyName=QByteArray()):
        self._mapped[section] = [widget, propertyName]

    def actual_mapping(self):
        for section, val in self._mapped.items():
            widget, propertyName = val
            if isinstance(widget, QComboBox):
                mdl: QSqlTableModel = self.model().super_model()
                rel_mdl = mdl.relationModel(section)
                if rel_mdl:
                    widget.setModel(rel_mdl)
                    widget.setModelColumn(rel_mdl.fieldIndex(mdl.relation(section).displayColumn()))
                    widget.installEventFilter(self.itemDelegate())
                # widget.currentIndexChanged.connect(lambda: self.itemDelegate().commitData.emit(widget))
            super().addMapping(widget, section, propertyName)

    def setCurrentIndex(self, index: int):
        if self._mapped:
            if not self._init_mapped:  # check actual mapping
                self.actual_mapping()
            ret = super().setCurrentIndex(index)
            return ret

    def current_id(self, id_field="id"):
        """cbx - any class with mapped model"""
        curfioind = self.currentIndex()
        mdl: tsSqlTableModel = self.model()
        # mdl: QSortFilterProxyModel = cbx.model()
        # TODO: super_model
        # curfioind = mdl.mapToSource(curfioind)
        try:
            colnum = mdl.super_model().index_of_col(id_field)
            id = mdl.data(mdl.index(curfioind, colnum), Qt.EditRole)
            return id
        except ValueError:
            debug("no key %s for %s ", id_field, mdl.objectName())
            return 0

    def isDirty(self):
        return self._dirty

    @Slot(bool)
    def setDirty(self, dirty=True):
        """set dirty for self and all parent"""
        if self._dirty == dirty:
            return
        info("Set dirty tsQDataWidgetMapper %s == %s", self.objectName(), dirty)
        #############################
        # set parent dirty
        # ---------------------------
        self._dirty = dirty
        # tsQDataWidgetMapper._class_dirty = dirty
        #############################
        # set filters
        # ---------------------------
        mdl = self.model()
        while hasattr(mdl, "sourceModel"):
            mdl.setDynamicSortFilter(not dirty)
            mdl = mdl.sourceModel()
        # for key, flt in self.filters.items():
        #     flt.setDynamicSortFilter(not dirty)

    def setModel(self, model):
        model.super_model().setDirty.connect(self.setDirty)
        ret = super().setModel(model)
        return ret

    def super_model(self) -> tsSqlTableModel:
        try:
            return self.model().super_model()
        except AttributeError:
            return self.model()


class tsQsfpModel_no_new(QSortFilterProxyModel):
    """
    3SON custum QSortFilterProxyModel
    TODO: use custum filtering (by id) for speedup
    """

    # setDirty: Signal = Signal(bool)

    def __init__(self, parent=None, model_name=None, tname=None, where=None, rel=False):
        super().__init__(parent)
        # self.setFilterRole(Qt.EditRole)
        self.setFilterRole(Qt.DisplayRole)
        self._filter_id = set()
        # self.far_cc = 0
        if model_name:
            from logic.data_worker import WD
            mdl = WD.models(model_name, tname, where, rel)
            self.setSourceModel(mdl)
            if mdl.rowCount0() < 1:
                mdl.select()
            while mdl.canFetchMore():
                mdl.fetchMore()

    def super_model(self) -> tsSqlTableModel:
        model = self
        while hasattr(model, 'sourceModel'):
            model = model.sourceModel()
        return model

    def data_rc(self, row: int, col: int, role: int = Qt.EditRole, parent=QModelIndex()):
        return self.data(self.index(row, col, parent), role)

    def mapToSuper(self, proxyIndex: QModelIndex) -> QModelIndex:
        ind = proxyIndex
        model = self
        while hasattr(model, 'mapToSource'):
            ind = model.mapToSource(ind)
            model = model.sourceModel()
        return ind

    def rowCount0(self):
        if self.super_model().special_row:
            return self.rowCount() - 1
        return self.rowCount()

    def index_of_col(self, col_name):
        """Return index of column by column name"""
        return self.super_model().index_of_col(col_name)

    @Slot(set)
    @Slot(list)
    @Slot(str)
    @Slot(int)
    def setFilterRegularExpression(self, pattern: Union[set, list, str, int]):
        if isinstance(pattern, set):
            self._filter_id = pattern
            self.invalidateFilter()
        elif isinstance(pattern, list):
            self._filter_id = {x for x in pattern}
            self.invalidateFilter()
        elif isinstance(pattern, int):
            self._filter_id = set()
            self._filter_id.add(pattern)
            self.invalidateFilter()
        else:
            self._filter_id = set()
            return super().setFilterRegularExpression(pattern)

    def get_filter_set(self):
        if self._filter_id:
            return self._filter_id
        elif self.filterRegularExpression().pattern():
            return False
        else:
            return set()

    def currentFilterRegularExpression(self) -> str:
        if self._filter_id:
            return str(self._filter_id)
        else:
            return self.filterRegularExpression().pattern()

    # def set_filter_by_id(self, id, col=0):
    #     rel_mdl = self.super_model().relationModel(col)
    #     if rel_mdl:
    #         self._filter_id = id
    #         # self.setFilterKeyColumn(col)
    #     else:
    #         self._filter_id = 0
    #         # self.setFilterKeyColumn(col)
    #         return super().setFilterRegularExpression("^" + str(id) + "$")
    @Slot()
    def invalidate(self):
        return super().invalidate()

    def filterAcceptsRow(self, row, source_parent: QModelIndex):
        # if self.far_cc == 100:
        #     QApplication.processEvents()
        #     self.far_cc = 0
        # else:
        #     self.far_cc += 1
        if self._filter_id:
            smdl: tsQsfpModel = self.sourceModel()
            dat = smdl.data(smdl.index(row, self.filterKeyColumn(), source_parent), Qt.EditRole)
            if dat in self._filter_id:
                return True
            else:
                return False
        else:
            return super().filterAcceptsRow(row, source_parent)

    # def filterAcceptsRow(self, row, src: QModelIndex):
    #     if self._filter_id:
    #         ret: bool = False
    #         mdl: tsSqlTableModel = self.super_model()
    #         rel_mdl: QSqlTableModel = mdl.relationModel(self.filterKeyColumn())
    #         if rel_mdl:
    #             ind: QModelIndex = mdl.ind_of_related(row, self.filterKeyColumn())
    #             if ind:
    #                 # debug(ind.data(Qt.EditRole))
    #                 ind = ind.siblingAtColumn(
    #                     rel_mdl.fieldIndex(
    #                         mdl.relation(
    #                             self.filterKeyColumn()
    #                         ).indexColumn()))
    #                 # debug(ind.data(Qt.EditRole))
    #                 ret = (ind.data(Qt.EditRole) == self._filter_id)
    #                 # self.invalidateFilter()
    #             else:
    #                 return ret
    #         else:
    #             index = self.sourceModel().index(row, self.filterKeyColumn(), src)
    #             ret = (index.data(Qt.EditRole) == self._filter_id)
    #         return ret
    #     else:
    #         return super().filterAcceptsRow(row, src)

    def prepareREListFixedStr(self, str_list: Union[list, set, any], exact=False):
        """
        Get list, str->[str], set and disable escape sequences in every row and return pattern_str of OR
        :param str_list:
        :param exact: use ^ and $ for every row
        :return: str
        """
        # str_dat = ""
        # str1: str = ""
        if isinstance(str_list, set):
            str_list = list(str_list)
        if not isinstance(str_list, list):
            str_list = [str_list, ]
        for i, val in enumerate(str_list):
            if isinstance(val, str):
                # debug(QRegularExpression.escape(str_list[i]))
                str_list[i] = str_list[i].replace("\\", "\\\\")
                str_list[i] = str_list[i].replace("|", "\\|")
                str_list[i] = str_list[i].replace("{", "\\{")
                str_list[i] = str_list[i].replace("(", "\\(")
                str_list[i] = str_list[i].replace(")", "\\)")
                str_list[i] = str_list[i].replace("*", "\\*")
                str_list[i] = str_list[i].replace(".", "\\.")
            elif isinstance(val, QDate):
                str_list[i] = val.toString(SQL_DATE_FORMAT)
            elif val is None:
                str_list[i] = ""
            else:
                str_list[i] = str(val).replace(".", "\\.")
        if exact:
            if len(str_list) == 1 and str_list[0] == "":
                return ""
            else:
                str_dat = ["^" + str(x) + "$" for x in str_list]
        else:
            str_dat = [str(x) for x in str_list]
        re_pattern = "|".join(str_dat)
        return re_pattern


class tsQsfpModel(tsQsfpModel_no_new):
    """3SON custum QSortFilterProxyModel"""

    def setFilterFixedString(self, pattern: str):
        return self.setFilterRegularExpression(pattern)

    def setFilterRegularExpressionPrepared(self, pattern):
        if isinstance(pattern, str):
            self._filter_id = set()
            if pattern == "":
                super().setFilterRegularExpression("")
            else:
                super().setFilterRegularExpression(pattern + "|^$")
            self.invalidateFilter()
        else:
            super().setFilterRegularExpression(pattern)

    @Slot(set)
    @Slot(list)
    @Slot(str)
    @Slot(int)
    def setFilterRegularExpression(self, pattern):
        if isinstance(pattern, str):
            self._filter_id = set()
            if pattern == "":
                super().setFilterRegularExpression("")
            else:
                #############################
                # fix escape characters except ^ and $ and |
                # ---------------------------
                pattern = QRegularExpression.escape(pattern)
                pattern = pattern.replace("\\|", "|")
                if pattern[:2] == "\\^":
                    pattern = pattern.replace("\\^", "^")
                if pattern[-2:] == "\\$":
                    pattern = pattern.replace("\\$", "$")
                super().setFilterRegularExpression(pattern + "|^$")
            self.invalidateFilter()
        else:
            super().setFilterRegularExpression(pattern)


class QUniqueValuesProxyModel(tsQsfpModel):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.uniq_col = "id"
        self.cols_set = set()
    @Slot()
    def invalidate(self):
        self.cols_set.clear()
        return super().invalidate()

    def filterAcceptsRow(self, row, source_parent: QModelIndex):
        smdl: tsQsfpModel = self.sourceModel()
        dat = smdl.data(smdl.index(row, self.filterKeyColumn(), source_parent), Qt.EditRole)
        if dat in self.cols_set:
            return False
        else:
            self.cols_set.add(dat)
            return True

