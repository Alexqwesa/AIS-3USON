#!/usr/bin/python3
# -------------------------------------------------------------------------------
# -*- coding: utf-8 -*-
# Name:        AIS 3USON QComboBox child classes
# Purpose:
#
# Author:      Savin Alexander Viktorovich aka alexqwesa
# Created:     2020
# Copyright:   Savin Alexander Viktorovich aka alexqwesa
# Licence:     LGPL 3
# This software is licensed under the "LGPLv3" License as described in the "LICENSE" file,
# which should be included with this package. The terms are also available at
# http://www.gnu.org/licenses/lgpl-3.0.html
# -------------------------------------------------------------------------------
from qtpy.QtGui import QWheelEvent
from qtpy.QtWidgets import QCompleter
from widgets.ui_widgets import *


class _myQComboBox(QComboBox, tsFilteredModel):
    __metaclass__ = QComboBox


class myQComboBox(_myQComboBox):
    currentIndexChanged3: Signal = Signal(int, int, str)
    currentIndexChanged_id: Signal = Signal(int)
    currentIndexChanged_model: Signal = Signal(int, str)
    currentIndexChanged_col_id: Signal = Signal(str, int)

    def __init__(self, *a, **kw):
        super().__init__(*a, **kw)
        self.ts__init__("cbx_")
        self._dirty = False
        self.shown = False
        self.inited = False
        self.setEditable(True)
        self.highlight_wrong_text_running = False
        self.wrong_text = False
        self.sort_order = Qt.AscendingOrder
        self.default_model = None
        self.last_data_id = -1
        self.lineEdit().setClearButtonEnabled(True)
        self.delayed_emit = False
        #############################
        # TODO: last value = {}
        # ---------------------------
        self._last_value = None
        self._completer = QCompleter()
        self._completer.setCompletionMode(QCompleter.PopupCompletion)
        self._completer.setModelSorting(QCompleter.UnsortedModel)
        self._completer.setFilterMode(Qt.MatchContains)
        self._completer.setMaxVisibleItems(POPUPMaxVisibleItems)
        self._completer.setCaseSensitivity(Qt.CaseInsensitive)
        self._completer.setCompletionRole(Qt.DisplayRole)

    @Slot(QShowEvent)
    def showEvent(self, ev):
        self.init_model()
        if self.model():
            if self.super_model():
                self.apply_delayed_filters()
                self.super_model().update_data()
        ret = super().showEvent(ev)
        if self.delayed_emit is True:
            self.delayed_emit = False
            self.emit_ichanged_on_show()
        return ret

    def emit_ichanged_on_show(self):
        self.emitCurrentIndexChanged(-2)

    def wheelEvent(self, e: QWheelEvent):
        super().wheelEvent(e)
        self.lineEdit().setCursorPosition(0)

    @Slot()
    def set_default_index(self):
        if self.inited:  # and self.currentIndex() <= 0
            qset = None
            if self._last_value is None:
                qset = SD.qsettings
                text = qset.value("cboxes/" + self.objectName(), "")
                self._last_value = text
            new_ind = 1
            if self._last_value != "":
                new_ind = self.findText(self._last_value)
            self.setCurrentIndex(new_ind)
            if not qset and self._last_value:
                self.emitCurrentIndexChanged(new_ind)

    @Slot()
    def delayed_sort(self):
        Qtimer_runner(self.sort, 200, "cbox_delayed_sort")

    @Slot()
    def sort(self):
        if self.init_model():
            if self.sort_order:
                self.model().sort(self.modelColumn(), Qt.DescendingOrder)
            else:
                self.model().sort(self.modelColumn(), Qt.AscendingOrder)

    # @property
    def super_model(self) -> Union[tsSqlTableModel, None]:
        if self.init_model():
            return self.model().super_model()
        return None

    def init_model(self):
        with QMutexLocker(self.locks("init_model")):
            if not self.inited:
                # self.setModel(mdl)
                self.sort_order = self.property("sort_order")
                self.init_model_filter()
                self.inited = True  # TODO: init 3 state: False | started | True
                self.editTextChanged.connect(self.highlight_wrong_text)
                # self.model().super_model().fetch_all()  # to trigger above signals
                #############################
                # connect custum signals
                # ---------------------------
                self.model().super_model().selected.connect(self.set_default_index)
                self.model().super_model().selected.connect(self.delayed_sort)
                self.currentIndexChanged.connect(self.emitCurrentIndexChanged)
                self.emitCurrentIndexChanged(self.currentIndex())
                self.setCompleter(self._completer)
                debug("emitCurrentIndexChanged connected for %s", self.objectName())
            return True

    def setModel(self, model: tsSqlTableModel):
        #############################
        # disconnect old
        # ---------------------------
        # if self.inited:
        #     try:
        #         self.model().super_model().selected.disconnect(self.set_default_index)
        #     except RuntimeError:
        #         pass
        #     try:
        #         self.model().super_model().selected.disconnect(self.delayed_sort)
        #     except RuntimeError:
        #         pass
        #############################
        # connect
        # ---------------------------
        if hasattr(model, "sourceModel"):
            ret = super().setModel(model)
        else:
            ret = super().setModel(model.simply_sorted)
        #############################
        # get modelColumn + post connect setup
        # ---------------------------
        tname = self.objectName()
        try:
            col = int(tname[4])
        except ValueError:
            error("wrong combobox name - %s", self.objectName())
            return False
        # Qtimer_runner(self.sort, 500, "cbox_delayed_sort")
        self.setModelColumn(col)
        # self.model().super_model().selected.connect(self.set_default_index)
        Qtimer_runner(self.model().super_model().fetch_all, 300, "fetch_all" + self.model().super_model().objectName())
        #############################
        # set sorting on select
        # ---------------------------
        Qtimer_runner(self.sort, 500, "cbox_delayed_sort" + self.objectName())
        # self.setCompleter(self._completer)
        self._completer.setModel(self.model())  # TODO: maybe Qtimer_runner
        # self.model().super_model().selected.connect(self.delayed_sort)
        return ret

    def setCompleter(self, c: QCompleter):
        self._completer.setCompletionColumn(self.modelColumn())
        self._completer.setModel(self.model())
        return super().setCompleter(self._completer)

    @Slot(int, str)
    def change_model(self, id0: int, model_name: str):
        #############################
        # get new model name
        # ---------------------------
        from logic.data_worker import WD
        mdl = WD.models(model_name)
        new_model_name = mdl.data_by_id(id0, mdl.index_of_col("sql_table"))
        debug("new model - %s for - %s", new_model_name, self.objectName())
        #############################
        # set model
        # ---------------------------
        if not new_model_name:
            try:
                new_model_name = self.info.model
                debug("No model - used default in %s", self.objectName())
            except AttributeError:
                return
        model = WD.models(new_model_name)
        #############################
        # try restore current index
        # ---------------------------
        old_value = self.currentText()
        # self.model().setSourceModel(model)
        self.setModel(model)
        self.sort()
        # Qtimer_runner(self.sort, 500, "cbox_delayed_sort")
        new_ind = self.findText(old_value, Qt.MatchContains)
        if new_ind >= 0:
            self.setCurrentIndex(new_ind)

    def _emitCurrentIndexChanged(self, ind: int = -2):
        pass

    @Slot(int)
    def emitCurrentIndexChanged(self, ind: int = -2):
        """
        Re emit signal with custom parameters for model with rowCount0 != 0
        """
        #############################
        # skip if invisible
        # ---------------------------
        if not self.isVisible():
            self.delayed_emit = True
            return
        #############################
        # main
        # ---------------------------
        with QMutexLocker(self.locks("emitCurrentIndexChanged")):
            if getattr(self.super_model(), "rowCount0", 0):
                #############################
                # delay emit if selection_in_progress
                # ---------------------------
                if self.super_model().selection_in_progress:
                    if ind == -2:
                        Qtimer_runner(self.emitCurrentIndexChanged, 700, "emitCurrentIndexChanged" + self.objectName(),
                                      -2)
                    else:
                        Qtimer_runner(self.emitCurrentIndexChanged, 200, "emitCurrentIndexChanged" + self.objectName(),
                                      -2)
                    return
                #############################
                # no parameters - use currentIndex
                # ---------------------------
                if ind == -2:
                    debug("try emitCurrentIndexChanged - %s", self.objectName())
                    ind = self.currentIndex()
                    id0 = self.model().data_rc(ind, 0)
                    if id0 is None and ind != -1:
                        debug("failed emitCurrentIndexChanged - %s for %s", None, self.objectName())
                        # id0 = self.model().data_rc(ind, 0)
                        return
                    if id0 == self.last_data_id:
                        debug("emitCurrentIndexChanged id not changed - %s for %s", None, self.objectName())
                        return
                    self.last_data_id = id0
                    self.currentIndexChanged3.emit(ind, id0, self.currentText())  # TODO: not used
                    self.currentIndexChanged_id.emit(id0)
                    self.currentIndexChanged_model.emit(id0, self.model().super_model().objectName())
                    self.currentIndexChanged_col_id.emit(self.model().super_model().tsFieldNames[1] + "_id", id0)
                else:
                    #############################
                    # always delay emit - to avoid double run
                    # ---------------------------
                    Qtimer_runner(self.emitCurrentIndexChanged, 0, "emitCurrentIndexChanged" + self.objectName(), -2)
                # else:
                #     Qtimer_runner(self.emitCurrentIndexChanged, 200,
                #       "emitCurrentIndexChanged" + self.objectName(), -2)
                return

    def current_id(self, id_field="id"):
        """ Return id of record by current index"""
        if self.inited:
            cur_ind = self.currentIndex()
            mdl: tsSqlTableModel = self.model()
            try:
                colnum = mdl.super_model().index_of_col(id_field)
                id = mdl.data(mdl.index(cur_ind, colnum), Qt.EditRole)
                return id
            except ValueError:
                debug("no key %s for %s ", id_field, mdl.objectName())
                return 0
        else:
            return 0

    def current_index_data_by_col(self, col="id"):
        if self.init_model():
            return self.model().data_rc(self.currentIndex(), self.super_model().fieldIndex(col))

    def set_current_index_id(self, data):
        if self.init_model():
            ind_s = self.super_model().match_with_fetch(self.super_model().index(0, 0), data)
            mdl: tsQsfpModel = self.model()
            if len(ind_s) == 1:
                ind = mdl.mapFromSource(ind_s[0])  # TODO: go through all proxies!!!
                self.setCurrentIndex(ind.row())
                return True
        return False

    def keyPressEvent(self, e: QKeyEvent):
        #############################
        # clear field
        # ---------------------------
        self.debug_event_handler(e)
        if e.key() == Qt.Key_F2:
            self.clearEditText()
            new_ind = self.findText("", Qt.MatchExactly)
            if new_ind >= 0:
                self.setCurrentIndex(new_ind)
                return
            else:
                self.setCurrentIndex(-1)
                return
        #############################
        # ?
        # ---------------------------
        if e.key() == Qt.Key_Enter or e.key() == Qt.Key_Return:  # suppress model changes
            SD.unsaved_view = self  # needed?
        if e.key() == Qt.Key_Escape:
            self.setEditText(self.currentData(Qt.DisplayRole))
        ret = super().keyPressEvent(e)
        return ret

    def focusOutEvent(self, ev):
        ret = super().focusOutEvent(ev)
        text = self.currentText()
        new_ind = self.findText(text, Qt.MatchExactly)
        if new_ind >= 0:
            self.setCurrentIndex(new_ind)
        else:
            self.setCurrentIndex(-1)
        return ret

    def highlight_wrong_text(self, text):
        Qtimer_runner(self.highlight_wrong_text_run, 300, "htext_" + self.objectName())

    def highlight_wrong_text_run(self):
        text = self.currentText()
        if text and self.findText(text) == -1:
            if not self.wrong_text:
                self.setStyleSheet("myQComboBox { background-color: pink; }")  # TODO: use properties
                self.wrong_text = True
        else:
            if self.wrong_text:
                self.setStyleSheet("")
                self.wrong_text = False
