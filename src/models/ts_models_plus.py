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
from threading import Lock

from qtpy.QtCore import QByteArray, QRegularExpression
from qtpy.QtSql import QSqlRelationalDelegate
from qtpy.QtWidgets import QLineEdit, QCheckBox, QSpinBox, QDoubleSpinBox, QDateTimeEdit, QDateEdit, \
    QComboBox, QPlainTextEdit, QStyledItemDelegate, QDataWidgetMapper
from qtpy.QtWidgets import QStyleOptionViewItem

from models.ts_models import *


class tsPureItemDelegate(QSqlRelationalDelegate):
    def __init__(self, parent):
        """Constructor for chkItemDelegate FOR CHECKBOX ONLY"""
        super().__init__(parent)
        self.pcindex = None
        self.cindex = None
        self.ctype = None
        self.cname = None
        self.cmodel = None

    def createEditor(self, parent: QWidget, option, index: QModelIndex):
        #############################
        # parse info
        # ---------------------------
        mdl = index.model()
        self.pcindex = index
        while isinstance(mdl, tsQsfpModel):
            index = mdl.mapToSource(index)
            mdl = index.model()
        if len(mdl.tsFieldNames) == 0:
            mdl.setMetaInfo()
        try:
            ctyp: str = mdl.tsFieldTypes[index.column()].lower()
            cnam: str = mdl.tsFieldNames[index.column()].lower()
        except IndexError:
            editor = QLineEdit(parent)
            return editor
        #############################
        # store last info
        # ---------------------------
        self.cindex = index
        self.ctype = ctyp
        self.cname = cnam
        self.cmodel = mdl
        #############################
        # create editor
        # ---------------------------
        if "tinyint" in ctyp:  # TODO: don't call for tableView !!!
            if isinstance(self.parent(), QTableView):
                return
            cbox = QCheckBox(parent)
            return cbox
        elif "varchar" in ctyp:
            editor = QLineEdit(parent)
            return editor
        elif "year" in ctyp:
            editor = QSpinBox(parent)
            editor.setMinimum(2155)
            editor.setMinimum(1901)  # TODO: make constants
            return editor
        elif cnam[-3:] == "_id":
            if "_raw" == index.model().objectName()[-4:]:
                editor = QSpinBox(parent)
                editor.setMaximum(sys.maxsize)
                editor.setMinimum(0)
            else:
                editor = super().createEditor(parent, option, index)  # WTF?
                # editor = QComboBox(self.parent())
                if not isinstance(editor, QComboBox):
                    error("createEditor unexpected widget!")
                    return editor
                try:
                    # print_model_data(editor.model())
                    while editor.model().canFetchMore():
                        editor.model().fetchMore()
                except (AttributeError, TypeError):
                    debug("Delegate: no model")
                    return editor
                if isinstance(editor.model(), QSqlTableModel):
                    emdl = editor.model()
                    ename = editor.model().objectName()
                    #############################
                    # TODO: use fitered model
                    # ---------------------------
                    if not ename:
                        _, _, ename = editor.model().selectStatement().rpartition(" FROM ")
                        ename = "rel_" + ename
                        editor.model().setObjectName(ename)
                    try:
                        from data_worker import WD
                        if WD.model_last_update(ename[4:]) > emdl.last_update:
                            editor.model().select()
                            emdl.last_update = QDateTime.currentDateTime()
                    except AttributeError:
                        editor.model().select()
                        emdl.last_update = QDateTime.currentDateTime()
                # ret = QSqlRelationalDelegate(parent).createEditor()
            return editor
        elif "int" in ctyp:
            editor = QSpinBox(parent)
            editor.setMaximum(99999)
            editor.setMinimum(0)
            return editor
        elif "float" in ctyp or "decimal" in ctyp or "double" in ctyp:
            editor = QDoubleSpinBox(parent)
            editor.setMaximum(999999)
            editor.setMinimum(0)
            editor.setDecimals(2)
            return editor
        elif "timestamp" in ctyp or "datetime" in ctyp:
            editor = QDateTimeEdit(parent)
            return editor
        elif "date" in ctyp:
            editor = QDateEdit(parent)
            return editor
        else:
            editor = QLineEdit(parent)
            return editor

    def setEditorData(self, editor, index: QModelIndex):
        # TODO: check data valid
        # if index.isValid():
        # TODO: Always directly check journal data
        #############################
        # set color
        # ---------------------------
        bg_color: QColor = index.data(Qt.BackgroundRole)
        if bg_color:
            editor.setStyleSheet("background-color: {};".format(bg_color.name()))
        else:
            editor.setStyleSheet("")
        # #############################
        # # get latest data
        # # ---------------------------
        # model: tsSqlTableModel = index.model().super_model()
        # try:
        #     if model.pending_edit[0] == index.model().mapToSuper(index):
        #         dat = model.pending_edit[1]
        #     else:
        #         raise TypeError
        # except TypeError:  # no latest data
        #     dat = index.data(Qt.EditRole)
        dat = index.data(Qt.EditRole)
        #############################
        # set data
        # ---------------------------
        if isinstance(editor, QDateEdit):
            try:
                dat = QDate(dat)
            except TypeError:
                dat = 0
            if dat:
                editor.setDate(dat)
            else:
                editor.setDate(QDate(1900, 1, 1))  # TODO: maybe use different date?
        elif isinstance(editor, QDateTimeEdit):
            dat = QDateTime(dat)
            if dat:
                editor.setDateTime(dat)
            else:
                editor.setDateTime(QDateTime(QDate(1900, 1, 1)))
        elif isinstance(editor, QCheckBox):  # not called in tableView - only QDataMapper
            if dat:
                editor.setCheckState(Qt.Checked)
            else:
                editor.setCheckState(Qt.Unchecked)
            # debug(val)
        elif isinstance(editor, QSpinBox):
            try:
                dat = int(dat)
            except (TypeError, ValueError):
                dat = 0
            editor.setValue(dat)
        elif isinstance(editor, QDoubleSpinBox):
            dat = float(dat)
            editor.setValue(dat)
        elif isinstance(editor, QLineEdit):
            editor.setText(
                str(dat))
        elif isinstance(editor, QComboBox):
            # while isinstance(index.model(), tsQsfpModel):
            #     proxy = index.model()
            #     index = proxy.mapToSource(index)
            super().setEditorData(editor, index)
            rel = index.model().super_model().relation(index.column())
            rel_mdl = editor.model()
            rel_col_name = rel.displayColumn()
            rcol = 1
            if rel_mdl.headerData(rcol, Qt.Horizontal, Qt.DisplayRole) != rel_col_name:
                return
            # rcol =  rel_mdl.fieldIndex(rel_col_name)
            # value = self.record(row).value(col)
            value = index.data(Qt.DisplayRole)
            # if value:
            try:
                rel_ind = rel_mdl.match(rel_mdl.index(0, rcol), Qt.EditRole,
                                        value, flags=Qt.MatchExactly)[0]
                editor.setCurrentIndex(rel_ind.row())
            except:  # in case relation set wrong
                try:
                    rel_ind = rel_mdl.match(rel_mdl.index(0, 0), Qt.EditRole,
                                            value, flags=Qt.MatchExactly)[0]
                    editor.setCurrentIndex(rel_ind.row())
                except:
                    error("rel_model no index found")
            # editor.setCurrentIndex(index.model().ind_of_related(dat).column())
        elif isinstance(editor, QPlainTextEdit):
            editor.setPlainText(str(dat))
        elif isinstance(editor, QWidget):
            pass
        else:
            return QStyledItemDelegate.setEditorData(
                editor, index)

    def setModelData(self, editor, model: QSortFilterProxyModel, index: QModelIndex):
        if index.isValid():
            val = None
            # old_value = index.data(Qt.EditRole)
            #############################
            # create pending journal entry
            # ---------------------------
            view = self.parent()
            smodel: tsSqlTableModel = view.model().super_model()
            SD.unsaved_view = view  # TODO: make obsolete
            sindex = index
            while sindex.model() != smodel:
                sindex = sindex.model().mapToSource(sindex)
            row_id = smodel.row_id(sindex.row())
            try:
                col_name = smodel.tsFieldNames[index.column()]
            except IndexError:
                error("unknown field -%s in view - %s ", index.column(), view)
                col_name = index.column()
            SD.start_edit(view, smodel, row_id, col_name)  # , old_value, val)
            #############################
            # set model data
            # ---------------------------
            if isinstance(editor, QPlainTextEdit):
                val = editor.toPlainText()
                ret = model.setData(index, val, Qt.EditRole)
            elif isinstance(editor, QLineEdit):
                # index.setData(editor.text(), Qt.EditRole)
                val = editor.text()
                ret = model.setData(index, val, Qt.EditRole)
            elif isinstance(editor, QCheckBox):
                val = 0
                if editor.checkState() == Qt.Checked:
                    val = 1
                # index.setData(val, Qt.EditRole)
                ret = model.setData(index, val, Qt.CheckStateRole)
            elif isinstance(editor, QSpinBox):
                val = editor.value()
                ret = model.setData(index, val, Qt.EditRole)
            elif isinstance(editor, QComboBox):
                ind = editor.currentIndex()
                ret = False
                if ind != -1:
                    val = editor.model().data(editor.model().index(ind, 0), Qt.EditRole)
                    model.setData(index, val, Qt.EditRole)
                    ret = True
                    # can't set values bigger than 256 !? WTF qt 5.12.6
                    # super().setModelData(editor, model, index)
                    # return super().setModelData(editor, model, index) # wrong by default!
                elif isinstance(editor, QDateTimeEdit):
                    val = editor.dateTime()
                    ret = model.setData(index, val, Qt.EditRole)
            elif isinstance(editor, QDateEdit):
                val = editor.date()
                ret = model.setData(index, val, Qt.EditRole)
            else:
                # val = editor.value()
                ret = super(QSqlRelationalDelegate, self).setModelData(
                    editor, model, index)
        else:  # invalid index ?
            # val = editor.value()
            ret = super(QSqlRelationalDelegate, self).setModelData(
                editor, model, index)
        return ret

    def updateEditorGeometry(self, editor: QCheckBox, option: QStyleOptionViewItem, index: QModelIndex):
        editor.setGeometry(option.rect)


class tsItemDelegate(tsPureItemDelegate):
    """
    Fine tuning for project models
    """

    def __init__(self, parent=None):
        super().__init__(parent)
        self.add_info_contracts = None
        self.lock = Lock()
        self.last_widget: QWidget = None

    def createEditor(self, parent: QWidget, option, index: QModelIndex):
        #############################
        # check prev editor still active
        # ---------------------------
        with self.lock:
            if self.last_widget:
                if self.last_widget.isVisible():
                    return None
        #############################
        # get editor
        # ---------------------------
        editor = super().createEditor(parent, option, index)
        #############################
        # data aware checks
        # ---------------------------
        if self.pcindex:
            if self.pcindex is index:
                if self.cmodel and self.cmodel.info:
                    if self.cmodel.info.cut_name == "main":
                        #############################
                        # don't allow change some fields after save
                        # ---------------------------
                        if self.cmodel.row_id(self.pcindex.row())[:3] != "new_":
                            if self.cname in ["serv_id", "dep_id", "contracts_id", "ufio_id"]:
                                return
                        #############################
                        # only show workers from department
                        # ---------------------------
                        if self.cname == "worker_id":
                            from data_worker import WD
                            editor.setModel(WD.models("_dep_has_workers"))
                    if self.cmodel.info.cut_name == "add_info":
                        if self.cname == "contracts_id":
                            #############################
                            # show only contracts with same ufio
                            # ---------------------------
                            if "_by_ufio_id" in self.parent().objectName() or "_where_ufio_id" in self.parent().objectName():
                                if not self.add_info_contracts:
                                    self.add_info_contracts = tsQsfpModel_no_new(self, "private_contracts", "_contracts")
                                # editor.setModelColumn(self.add_info_contracts.super_model().tsFieldNames.index("contracts"))
                                self.add_info_contracts.setFilterKeyColumn(
                                    self.add_info_contracts.super_model().tsFieldNames.index("ufio_id"))
                                self.add_info_contracts.setFilterRegularExpression(
                                    "^" + str(self.parent().super_model().default_values["ufio_id"]) + "$")
                                editor.setModel(self.add_info_contracts)
        return editor


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
                from widgets.custumQWidgets import myQWidget
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
            from data_worker import WD
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
        """Return index of column by column name"""
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

# @auto_reload_class_code(reloader)
