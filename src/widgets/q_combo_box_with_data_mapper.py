#!/usr/bin/python3
# -------------------------------------------------------------------------------
# -*- coding: utf-8 -*-
# Name:        AIS 3USON View Widgets like QComboBoxWithDataMapper
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

from widgets.q_combo_box import *


class DependableQComboBox(tsDependable, myQComboBox):

    def emit_ichanged_on_show(self):
        pass


class QComboBoxWithDataMapper(myQComboBox):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.dm: tsQDataWidgetMapper = tsQDataWidgetMapper(self)
        # TODO: set unsaved data red
        # super_model(model).setDirty.connect(self.setDirty)
        # or block in selfDirty
        # why required in one case but not in another?

    def setModel(self, model: tsSqlTableModel):
        super().setModel(model)
        self.dm.setModel(super().model())
        if not isinstance(self.dm.itemDelegate(), tsItemDelegate):
            self.dm.setItemDelegate(tsItemDelegate(self.dm))
        self.set_current_id()

    def set_current_id(self):
        """ Set working id """
        model = self.model().super_model()
        if model.meta_init:
            col_name = model.tsFieldNames[self.modelColumn()]
            if col_name != "id" and col_name[-3:] != "_id":
                col_name += "_id"
            id_ = self.current_id()
            # kwarg = {col_name: self.current_id()}
            # model.set_new_rec_autofill(**kwarg)
            # model.set_new_rec_autofill(**{col_name: self.current_id()})
            #############################
            # set SQL settings
            # ---------------------------
            if col_name == "client_id":
                SD.set_last_client(id_)
            elif col_name == "contracts_id":
                SD.set_last_contr(id_)

    # @Slot(int, str)
    # def change_model(self, id0: int, model_name: str):
    #     super().change_model(id0,model_name)
    # not needed since we change source model of filter model

    @Slot(int)
    def emitCurrentIndexChanged(self, ind: int):
        """
        Re emit signal with custom parameters
            and sync indexes of comboBox and dataModel
        """
        if getattr(self.super_model(), "rowCount0", 0):
            if ind != -2:
                self.dm.setCurrentIndex(self.currentIndex())
                self.set_current_id()
            #############################
            # emit signal
            # ---------------------------
            super().emitCurrentIndexChanged(ind)

    @Slot()
    def toPrevious(self):
        self.dm.toPrevious()
        self.setCurrentIndex(self.dm.currentIndex())

    @Slot()
    def toNext(self):
        self.dm.toNext()
        self.setCurrentIndex(self.dm.currentIndex())


class DepQComboBoxWithDataMapper(QComboBoxWithDataMapper, DependableQComboBox):
    pass
