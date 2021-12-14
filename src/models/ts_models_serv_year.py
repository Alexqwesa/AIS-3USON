#!/usr/bin/python3
# -------------------------------------------------------------------------------
# -*- coding: utf-8 -*-
# Name:        AIS 3USON Custum QT Model for served in year table
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
import decimal
from datetime import date
from threading import Thread

from qtpy.QtGui import QFontMetrics

from logic.data_worker import _data_worker
from models.orm import *
from models.ts_models import *


class BareTableModel(QAbstractTableModel):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.tsFieldNames = []
        self.tsFieldTypes = []
        self.relColumns = []
        self.chkColumns = []
        self.roColumns = [0, 1, 2, 3, 4]
        self.relroColumns = []
        self.notnullable = []
        self._inited = False
        #############################
        # constants
        # ---------------------------
        self.TOTAL_ROWS = 10
        self.tot_br_color = QBrush(TOTAL_ROW_COLOR)

    def super_model(self):
        return self

    def rowCount(self, *arg, **kwargs):
        if self.serv:
            return self.serv.rowCount0() + self.TOTAL_ROWS
        return self.TOTAL_ROWS

    def columnCount(self, *arg, **kwargs):
        return 18

    def data(self, index, role=Qt.EditRole):
        return "Bare Table Error"  # stub

    def flags(self, index):
        col = index.column()
        fl = Qt.ItemIsEditable | Qt.ItemIsEnabled
        fl = fl & (~Qt.ItemIsUserCheckable)
        # if col in self.chkColumns:
        #     fl = fl | Qt.ItemIsUserCheckable  # | Qt::ItemIsEnabled;
        # else:
        #     fl = fl & (~Qt.ItemIsUserCheckable)
        if col in self.roColumns or self.data(index, totalServ):
            fl = fl & (~Qt.ItemIsEditable)
            # self.roColumns
        # if len(self._unselectable_items_by) >= 2:
        #     if (self._unselectable_items_by[1] == index.siblingAtColumn(
        #             self._unselectable_items_by[0]).data(Qt.EditRole)):
        #         fl = fl & (~(Qt.ItemIsSelectable | Qt.ItemIsEnabled))
        #         # index.setData(Qt.AlignHCenter, Qt.TextAlignmentRole)
        #         # index.setData(0, Qt.UserRole - 1)  # hack!!!
        return fl

    def select(self):
        return False  # stub

    def headerData(self, section, orientation, role=Qt.DisplayRole):
        if role in (Qt.DisplayRole, Qt.EditRole):
            return ""
        elif role == Qt.SizeHintRole:
            if section:  # not first
                # s_hint = super().headerData(section, orientation, role)
                text = self.headerData(section, orientation, Qt.DisplayRole)
                if UI.main_window:
                    s_hint = QFontMetrics(UI.main_window.font()).size(Qt.TextIncludeTrailingSpaces,
                                                                      text)  # TextSingleLine
                else:
                    s_hint = QFontMetrics(QApplication.instance().font()).size(Qt.TextSingleLine, text)
                return s_hint
        return super().headerData(section, orientation, role)


class BareStaticTableModel(BareTableModel):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.serv: Union[tsSqlTableModel, None] = None
        self.dep_has_worker: Union[tsSqlTableModel, None] = None

    def select(self):
        if not self.serv:
            self.serv.select()
        if not self.dep_has_worker:
            self.dep_has_worker.select()
        return True

    @lru_cache(1000)
    def sid_list_for(self, row) -> [int]:
        return [int(sid) for sid in str(self.serv.index(row, 0).siblingAtColumn(
            self.serv.tsFieldNames.index("serv_id_list")).data(Qt.EditRole)).split(",")]

    @Slot()
    def clear_serv_cache(self):
        self.sid_list_for.cache_clear()

    def init_model_filter(self):
        if not self._inited:
            #############################
            # init static models
            # ---------------------------
            from logic.data_worker import WD
            self.serv = WD.models("_serv_activ")
            self.dep_has_worker = WD.models("dep_has_worker")
            #############################
            # init models
            # ---------------------------
            self.layoutAboutToBeChanged.emit()
            self.serv.selected.connect(self.updateLayout)  # used only on change year
            self.serv.selected.connect(self.clear_serv_cache)  # used only on change year
            self.dep_has_worker.selected.connect(self.updateLayout)  # never used
            #############################
            # finish
            # ---------------------------
            self.updateLayout()
            self._inited = True
        return self._inited

    @Slot()
    def updateLayout(self):
        #############################
        # update layout
        # ---------------------------
        debug("updateLayout")
        # self.insertRows(rc-1, self.rowCount()-rc)
        self.layoutAboutToBeChanged.emit()
        # self.changePersistentIndexList()
        self.layoutChanged.emit()


class CHSTableModel(BareStaticTableModel):
    """
    Unstructured model with contract_id and skeleton data from contr_has_serv (also Qt.UserRole is implemented here)
    """

    def __init__(self, parent=None):
        super().__init__(parent)
        self._contract_id = 0
        self.contr_has_serv: Union[tsSqlTableModel, None] = None

    @property
    def contract_id(self):
        return self._contract_id

    @contract_id.setter
    def contract_id(self, value):
        self.set_contract_id(value)

    def set_contract_id(self, value):
        self._contract_id = value
        self.init_model_filter()
        if self.contr_has_serv:
            self.contr_has_serv.setFilter("contracts_id = {}".format(value))
            # self.chs_get_data.cache_clear()

    def select(self):
        super().select()
        if self.contract_id:
            self.contr_has_serv.select()
            return True

    def data_by_row(self, row, role: int = Qt.EditRole):
        return self._user_role_data(row, role)

    def data(self, index, role: int = Qt.EditRole):
        return self.data_by_row(index.row(), role)

    def _user_role_data(self, row, role: int = Qt.EditRole):  # TODO: use row instead of index
        """
        User roles data
        Warning: Should never call itself
        :param row:
        :param role:
        :return: model data
        """
        if not self.serv:
            return "Services Not Inited"
        if role == totalServ:
            return self.serv.data_rc(row, self.serv.tsFieldNames.index("total"))
        if row >= 0:
            # col = index.column()
            #############################
            # get actual data
            # ---------------------------
            if self.contr_has_serv:
                if role == leftServ:
                    try:
                        return self.chs_get_data(row, "planned") \
                               - \
                               self.chs_get_data(row, "filled")
                    except TypeError:
                        return ""
                if role == subServ:
                    return self.serv.data_rc(row, self.serv.tsFieldNames.index("sub_serv"))
                elif role == nameServ:
                    return self.serv.data_rc(row, self.serv.tsFieldNames.index("serv_text"))
                elif role == numNameServ:
                    return self.serv.data_rc(row, self.serv.tsFieldNames.index("serv"))
                elif role == priceServ:
                    return self.serv.data_rc(row, self.serv.tsFieldNames.index("price"))
                elif role == plannedServ:
                    return self.chs_get_data(row, "planned")
                elif role == filledServ:
                    return self.chs_get_data(row, "filled")
                elif role == idListServ:
                    return self.sid_list_for(row)  # serv_id_list
            return 0
        return "Wrong Row Number"

    @lru_cache(100000)
    def chs_get_data(self, row, col_name="filled"):
        """ contr_has_serv data from row and col_name """
        if not self._contract_id or not self.contr_has_serv:  # not needed ?
            return ""
        total_col = self.serv.tsFieldNames.index("total")
        col_num = self.contr_has_serv.tsFieldNames.index(col_name)
        if self.serv.data_rc(row, total_col):
            #############################
            # total row
            # ---------------------------
            sid_list = self.sid_list_for(row)
            summ = 0
            for serv_id in sid_list:
                try:
                    serv_id = int(serv_id)
                    if not self.serv.data_by_id(serv_id, total_col):
                        summ += self.contr_has_serv.data_by_id(
                            serv_id,
                            col_num, 0, "serv_id", Qt.EditRole,
                            self.contract_id, "contracts_id")
                except TypeError:
                    pass
            return summ
        else:
            #############################
            # ordinary row
            # ---------------------------
            serv_id = self.serv.data_rc(row, self.serv.tsFieldNames.index("id"))
            return self.contr_has_serv.data_by_id(
                serv_id,
                self.contr_has_serv.tsFieldNames.index(col_name), 0, "serv_id", Qt.EditRole,
                self.contract_id, "contracts_id")

    def init_model_filter(self):
        if not self._inited:
            super().init_model_filter()
            #############################
            # init models
            # ---------------------------
            from logic.data_worker import WD
            # self.contr_has_serv = WD.models("_contracts_has_serv_raw__where_contracts_id_table_year",
            #                                 "_contracts_has_serv",
            #                                 "contracts_id={}".format(self._contract_id), False)
            self.contr_has_serv = QSqlRelTableModelExtWithMetaData(
                "_contracts_has_serv_raw__where_contracts_id_table_year", self, None, False)
            self.contr_has_serv.setTable("_contracts_has_serv", "contracts_id = {}".format(self._contract_id))
            # self.contr_has_serv.setFilter()
            self.contr_has_serv.select()
        self.contr_has_serv.selected.connect(self.chs_get_data.cache_clear)
        return True

    # @Slot()
    # def clear_serv_cache(self):
    #     super().clear_serv_cache()
    #     self.chs_get_data.cache_clear()


class GroupedMainData(tsSqlTableModelWithColors):  # QSqlRelTableModelExtWithMetaData, tsSqltRelTableModelEdit
    def __init__(self, name="", parent=None):
        super().__init__(name, parent, None, False)
        self.worker_columns = {}
        self.WD: _data_worker = None

    def setObjectName(self, name: str):
        ret = super().setObjectName(name)
        self.info.read_only = True
        return ret

    def data_month(self, month, serv_id, dep_has_worker_id="all"):
        """ Count services in month filtered by dep_has_worker_id """
        # note: currently dep_id set in query where
        try:
            col = self.tsFieldNames.index("month" + str(month))
            sid = self.tsFieldNames.index("serv_id")
            wid = self.tsFieldNames.index("dep_has_worker_id")
        except ValueError:
            return 0
        ret = 0
        for i in range(self.rowCount()):
            if self.data_rc(i, sid) == serv_id:
                if dep_has_worker_id == "all" or dep_has_worker_id == self.data_rc(i, wid):
                    ret += self.data_rc(i, col)
        return ret

    def data_month_with_dep_filter(self, month, serv_id, dep_has_worker_id="all", dep_id=None):
        """ Count services in month filtered by dep_has_worker_id and dep_id """
        if not dep_id:
            dep_id = SD.last_dep
        try:
            col = self.tsFieldNames.index("month" + str(month))
            sid = self.tsFieldNames.index("serv_id")
            wid = self.tsFieldNames.index("dep_has_worker_id")
            did = self.tsFieldNames.index("dep_id")
        except ValueError:
            return ""
        ret = 0
        for i in range(self.rowCount()):
            if self.data_rc(i, sid) == serv_id:
                if dep_has_worker_id == "all" or dep_has_worker_id == self.data_rc(i, wid):
                    if dep_id == self.data_rc(i, did):
                        ret += self.data_rc(i, col)
        return ret

    def select(self):
        return super().select()

    def submitAll(self):
        #############################
        # submit
        # ---------------------------
        ret = self._submitAll()
        if ret:
            self.select()
        else:
            QMessageBox.critical(self.parent().parent(), self.tr("Ошибка"), self.tr("Не удалось сохранить изменения!"),
                                 QMessageBox.Ok)

    def _submitAll(self):
        return True

    def setFilter(self, filter_str: str):
        ret = super().setFilter(filter_str)
        self.worker_columns.clear()
        wid = self.tsFieldNames.index("dep_has_worker_id")
        col1 = self.tsFieldNames.index("month1")
        col12 = self.tsFieldNames.index("month12")
        for i in range(self.rowCount()):
            for k, mm in enumerate(range(col1, col12 + 1), 1):
                if self.data_rc(i, mm):
                    try:
                        self.worker_columns[k].add(self.data_rc(i, wid))
                    except KeyError:
                        self.worker_columns[k] = set()
                        self.worker_columns[k].add(self.data_rc(i, wid))
        return ret
    # def data(self, index: QModelIndex, role):
    #     pass


class AllDynamicTableModel(CHSTableModel):
    """
    Init all left Dynamic tables + selection status notification
    """
    inner_change_selection_in_progress: Signal = Signal(bool)
    change_selection_in_progress: Signal = Signal(bool)

    def __init__(self, parent=None):
        super().__init__(parent)
        # self.main: Union[tsSqlTableModel, None] = None
        # self.max_pay: Union[tsSqlTableModel, None] = None
        self.gmdata: Union[GroupedMainData, None] = None

    @property
    def selection_in_progress(self):
        if not self.gmdata or \
                not self.serv or \
                not self.contr_has_serv or \
                not self.dep_has_worker:
            return True
        return self.gmdata.selection_in_progress or \
               self.serv.selection_in_progress or \
               self.contr_has_serv.selection_in_progress or \
               self.dep_has_worker.selection_in_progress
        # self.main.selection_in_progress or \

    def init_model_filter(self):
        if not self._inited:
            super().init_model_filter()
            #############################
            # init services list
            # ---------------------------
            from logic.data_worker import WD
            # self.main = WD.models("main_raw__where_contracts_id_table_year", "main",
            #                       "contracts_id = {}".format(self._contract_id), False)
            self.gmdata = GroupedMainData("_main_months", self)
            # self.max_pay = WD.models("max_pay_in_month")
            self.gmdata.setTable("_main_months", "contracts_id = {} and year1 = {} and dep_id = {}".format(
                self._contract_id, SD.last_year, SD.last_dep))
            #############################
            # emit_selection_in_progress and update layout
            # ---------------------------
            self.gmdata.change_selection_in_progress.connect(self.emit_selection_in_progress)
            # self.main.change_selection_in_progress.connect(self.emit_selection_in_progress)
            self.serv.change_selection_in_progress.connect(self.emit_selection_in_progress)
            self.contr_has_serv.change_selection_in_progress.connect(self.emit_selection_in_progress)
            self.dep_has_worker.change_selection_in_progress.connect(self.emit_selection_in_progress)
            #############################
            # fail safe ??? delete ??
            # ---------------------------
            self.inner_change_selection_in_progress.connect(self.emit_selection_in_progress)
        return True

    @Slot(bool)
    def emit_selection_in_progress(self, in_progress):
        """
        Emit True if in_progress true or some model in state selection_in_progress,
        Only emit false if all model false (not in state selection_in_progress)
        +call update_layout
        """
        if in_progress:
            # self._in_progress=True
            self.change_selection_in_progress.emit(in_progress)
        else:
            #############################
            # check is it realy false
            # ---------------------------
            # if self._in_progress != self.selection_in_progress:
            #     self._in_progress
            status = self.selection_in_progress
            if not status:
                self.updateLayout()
            self.change_selection_in_progress.emit(status)

    @Slot()
    def updateLayout(self):
        self.gmdata_serv_in_month.cache_clear()
        self.gmdata_serv_money_in_month.cache_clear()
        self.gmdata_total_money_in_month.cache_clear()
        ret = super().updateLayout()
        return ret

    def select(self):
        super().select()
        if self.contract_id:
            self.gmdata.select()
            # self.main.select()
            return True
        # self.months_columns = []
        # self.setFilter()

    # def set_contract_id(self, value):
    #     super().set_contract_id(value)
    #     # if self.main:
    #     #     self.main.setfilter("contracts_id = {}".format(value))
    #     #     # self.main.cache_clear()
    #     if self.gmdata:
    #         self.gmdata.setfilter("contracts_id = {} and year1 = {}".format(
    #             value, sd.last_year))
    #         # self.gmdata.cache_clear()

    def data_by_row(self, row, role=Qt.EditRole):
        """

        :param row: (serv_id)
        :param role: mostly used user roles
        :return:
        """
        if roleMonth12 >= role >= roleMonth1:
            return self.gmdata_serv_in_month(row, role)
        elif roleMoneyMonth12 >= role >= roleMoneyMonth1:
            if super().data_by_row(row, totalServ):
                return self.gmdata_total_money_in_month(row, role)
            else:
                return self.gmdata_serv_money_in_month(row, role)
        elif role == roleMoneyMonthYear:
            #############################
            # return moneys in year
            # ---------------------------
            ret = 0
            for month in range(1, 13):
                ret += self.gmdata_total_money_in_month(row, roleMoneyMonth0 + month)
            return ret
        elif role == roleMonthYear:
            #############################
            # return services in year
            # ---------------------------
            ret = 0
            for month in range(1, 13):
                ret += self.gmdata_serv_in_month(row, roleMonth0 + month)
            return ret
        #############################
        # ask parent class for user roles
        # ---------------------------
        elif role >= Qt.UserRole:
            return super().data_by_row(row, role)
        # elif role == Qt.CheckStateRole:
        #     if row.column() in self.chkColumns:
        #         if row.data(Qt.EditRole):
        #             return 2
        #         else:
        #             return 0
        #     return
        elif role == Qt.BackgroundRole:
            if super().data_by_row(row, totalServ):
                return self.tot_br_color
            return super().data_by_row(row, role)
        else:
            return "WRONG ROLE INDEX"

    @lru_cache(50000)
    def gmdata_total_money_in_month(self, row, role):
        sids = super().data_by_row(row, idListServ)
        ret = 0
        month = role - roleMoneyMonth0
        price_col = self.serv.tsFieldNames.index("price")
        for serv_id in sids:
            price = self.serv.data_by_id(serv_id, price_col)
            ret += self.gmdata.data_month(month, serv_id) * price
        return ret

    @lru_cache(50000)
    def gmdata_serv_money_in_month(self, row, role):
        price = super().data_by_row(row, priceServ)
        return self.gmdata_serv_in_month(row, role + roleMonth0 - roleMoneyMonth0) * price

    @lru_cache(50000)
    def gmdata_serv_in_month(self, row, role):
        sids = super().data_by_row(row, idListServ)
        ret = 0
        month = role - roleMonth0
        for serv_id in sids:
            ret += self.gmdata.data_month(month, serv_id)
        return ret


class AllDynamicTableModelFilterID(AllDynamicTableModel):

    def set_contract_id(self, value):
        if self._contract_id != value:  # TODO: if check value changed needed here
            # self.change_selection_in_progress.emit(True)
            super().set_contract_id(value)
            self.setFilter()

    def setFilter(self, where=""):
        if self._contract_id:
            self.inner_change_selection_in_progress.emit(True)
            # if self.contr_has_serv:
            if self.contr_has_serv.filter() != "contracts_id = {}".format(self._contract_id):
                self.contr_has_serv.setFilter("contracts_id = {}".format(self._contract_id))
            # if self.main:
            # self.main.setFilter("contracts_id = {}".format(self._contract_id))
            self.gmdata.setFilter("contracts_id = {} and year1 = {}".format(self._contract_id, SD.last_year))
            self.inner_change_selection_in_progress.emit(False)

    def selectStatement(self):
        pass

    def setMetaInfo(self):
        pass

    def filter(self):
        pass


class YearColumnLayoutModel(AllDynamicTableModelFilterID):  # Maybe use shift columns here ?
    """
    Add column layout to model - convert index into shifted rows and qt user roles
    """

    def __init__(self, parent=None):
        super().__init__(parent)
        #############################
        # dynamic columns
        # ---------------------------
        self.months_columns = []
        self.worker_columns = []
        self.reversed_months_columns = []
        self.months_columns_new = []
        self.worker_columns_new = []
        #############################
        # column consts
        # ---------------------------
        self.COL_SERV_START = 5
        self.COL_SLEFT = 0
        self.COL_SNAME = 1
        self.COL_TARIFF = 2
        self.COL_SERV_SHOULD = 3
        self.COL_SERV_YEAR = 4

    def set_contract_id(self, value):
        super().set_contract_id(value)
        self.months_columns_new = []
        self.worker_columns_new = []

    @Slot()
    def updateLayout(self):
        # self.main_data.cache_clear()
        self.months_columns = []
        self.worker_columns = []
        # self.sum_in_month.cache_clear()
        # self.get_serv_in_month.cache_clear()
        self.gmdata_serv_worker_in_month.cache_clear()
        # self.main_data.cache_clear()
        ret = super().updateLayout()
        # self.headerDataChanged.emit(Qt.Horizontal, 0, self.columnCount())
        return ret

    def data_role_by_col(self, index: QModelIndex, role: int = Qt.EditRole):
        row = index.row() - self.TOTAL_ROWS
        #############################
        # header columns
        # ---------------------------
        col = index.column()
        if col < self.COL_SERV_START:
            if role == Qt.EditRole or role == Qt.DisplayRole:
                if col == self.COL_SLEFT:
                    return super().data_by_row(row, leftServ)
                if col == self.COL_SNAME:
                    ret = super().data_by_row(row, numNameServ)
                    return ret
                if col == self.COL_TARIFF:
                    return super().data_by_row(row, priceServ)
                if col == self.COL_SERV_SHOULD:
                    return super().data_by_row(row, plannedServ)
                if col == self.COL_SERV_YEAR:
                    return super().data_by_row(row, filledServ)
            # return  # can't return 0 because of Qt.CheckStateRole
        #############################
        # color
        # ---------------------------
        if role == Qt.BackgroundRole:
            if self.is_total_col(col):
                return QBrush(TOTAL_COL_COLOR)
        #############################
        # actual data columns
        # ---------------------------
        if not self.serv:
            return "serv not inited"
        if role == Qt.EditRole or role == Qt.DisplayRole:
            col_ = col - self.COL_SERV_START
            if self.months_columns:
                month = self.months_columns[col_]
                #############################
                # total column
                # ---------------------------
                if self.is_total_col(col):
                    return super().data_by_row(row, roleMonth0 + month)
                #############################
                # money column
                # ---------------------------
                elif self.is_money_col(col):
                    ret = super().data_by_row(row, roleMoneyMonth0 + month)
                    # if role == Qt.DisplayRole:
                    #     ret = str(ret)
                    #     if ret[-2] == ",":
                    #         ret += "0"
                    return ret
                #############################
                # worker column
                # ---------------------------
                elif self.is_worker_col(col):
                    return self.gmdata_serv_worker_in_month(row, roleMonth0 + month, self.worker_columns[col_])
                else:
                    error("wrong column - %s", col)
                    return "Error"
        if role == Qt.TextAlignmentRole:
            #############################
            # money column TextAlignment
            # ---------------------------
            # if self.is_money_col(col):
            #     return Qt.AlignRight
            if col == self.COL_SNAME:
                return Qt.AnchorLeft
            return Qt.AlignRight
        return super().data_by_row(row, role)

    @lru_cache(200000)
    def gmdata_serv_worker_in_month(self, row, role=Qt.EditRole, dep_has_woker_id="all"):
        if role == roleMonthYear:  # Not used yet
            #############################
            # return services of worker in year
            # ---------------------------
            ret = 0
            for m in range(1, 13):
                ret += self.gmdata_serv_worker_in_month(row, role, dep_has_woker_id)
            return ret
        else:
            #############################
            # return services of worker in month
            # ---------------------------
            month = role - roleMonth0
            sids = super().data_by_row(row, idListServ)
            ret = 0
            for serv_id in sids:
                ret += self.gmdata.data_month(month, serv_id, dep_has_woker_id)
            return ret

    def columnCount(self, *arg, **kwargs):
        if self.months_columns:
            return len(self.months_columns) + self.COL_SERV_START
        if not self.contract_id or self.selection_in_progress:
            self.months_columns = []
            self.worker_columns = []
            return self.COL_SERV_START
        self.months_columns = []
        self.worker_columns = []
        try:
            if self.gmdata.worker_columns:
                #############################
                # add columns in months
                # ---------------------------
                for i in range(1, 13 + 1, 1):
                    self.months_columns.append(i)
                    self.worker_columns.append("all")
                    if i in self.gmdata.worker_columns:
                        for worker in self.gmdata.worker_columns[i]:
                            self.worker_columns.append(worker)
                            self.months_columns.append(i)
                            # self.gmdata.worker_columns.append(worker)
                    self.months_columns.append(i)
                    for m, w in zip(self.months_columns_new, self.worker_columns_new):
                        if i == m:
                            self.months_columns.append(i)
                            self.worker_columns.append(w)
                    self.worker_columns.append("money")
                #############################
                # reversed list
                # ---------------------------
                self.reversed_months_columns = list(reversed(self.months_columns))
                return len(self.months_columns) + self.COL_SERV_START
            else:
                return self.COL_SERV_START
        except AttributeError:
            return self.COL_SERV_START

    def is_money_col(self, col):
        """Check unshifted column"""
        col_ = col - self.COL_SERV_START
        if col_ < 0:
            return False
        try:
            if self.worker_columns[col_] == "money":
                return True
        except IndexError:
            pass
        return False

    def is_total_col(self, col):
        col_ = col - self.COL_SERV_START
        if col_ < 0:
            return False
        try:
            if self.worker_columns[col_] == "all":
                return True
        except IndexError:
            pass
        return False

    def get_month(self, col):
        col_ = col - self.COL_SERV_START
        if col_ < 0:
            return False
        try:
            return self.months_columns[col_]
        except IndexError:
            pass
        return False

    def get_worker(self, col):
        col_ = col - self.COL_SERV_START
        if col_ < 0:
            return False
        try:
            if self.worker_columns[col_] != "money" and self.worker_columns[col_] != "all":
                return self.worker_columns[col_]
        except IndexError:
            pass
        return False

    def is_worker_col(self, col):
        col_ = col - self.COL_SERV_START
        if col_ < 0:
            return False
        try:
            if self.worker_columns[col_] != "money" and self.worker_columns[col_] != "all":
                return True
        except IndexError:
            pass
        return False

    def flags(self, index):
        flags = super().flags(index)
        col = index.column()
        if not self.is_worker_col(col):
            flags = flags & (~Qt.ItemIsEditable)
        return flags

    def headerData(self, section, orientation, role=Qt.DisplayRole):
        #############################
        # Horizontal orientation
        # ---------------------------
        if orientation == Qt.Horizontal:
            if role == Qt.DisplayRole:
                if section == self.COL_SLEFT:
                    return self.tr("Остаток")
                elif section == self.COL_SNAME:
                    return self.tr("Наименование                               .")
                elif section == self.COL_TARIFF:  # 2
                    return self.tr("Тариф")
                elif section == self.COL_SERV_SHOULD:  # 3
                    return self.tr("Положено")
                elif section == self.COL_SERV_YEAR:  # 4
                    return self.tr("Оказано")
            #############################
            # shift for subtable
            # ---------------------------
            if section >= self.COL_SERV_START:
                section_ = section - self.COL_SERV_START
                if role == Qt.DisplayRole:
                    if self.months_columns[section_] == 13:
                        return "За ГОД по контракту"
                    elif self.months_columns:
                        month_name = date(1900, self.months_columns[section_], 1).strftime('%B')  # s = section  # - 4
                        return month_name
        return super().headerData(section, orientation, role)


class YearRowLayoutModel(YearColumnLayoutModel):

    def __init__(self, parent=None):
        super().__init__(parent)
        #############################
        # row consts
        # ---------------------------
        self.ROW_MONTH_NAMES = 0
        self.ROW_WORKER_NAMES = 1
        self.ROW_TOTAL_SERV = 2
        self.ROW_BM = 3
        self.ROW_TO_PAY = 4
        self.ROW_SDD = 5

    def data(self, index: QModelIndex, role: int = Qt.EditRole):
        """ There is a split between data rows and header(total) rows"""
        row = index.row()
        if row < self.TOTAL_ROWS:
            #############################
            # header table
            # ---------------------------
            return self.total_row_data(index, role)
        else:
            return self.data_role_by_col(index, role)
            #############################
            # return (shifted) data table
            # ---------------------------
            # index_shifted = index.siblingAtRow(row - self.TOTAL_ROWS)
            # return super().data(index_shifted, role)

    # def _user_role_data(self, index, role=Qt.EditRole):
    #     """ Shift data from _user_role_data"""
    #     index_shifted = index.siblingAtRow(index.row() - self.TOTAL_ROWS)
    #     return super()._user_role_data(index_shifted, role)

    #
    # def shifted_data(self, index: QModelIndex, role=Qt.EditRole):
    #     index_shifted = index.siblingAtRow(index.row() - self.TOTAL_ROWS)
    #     return super().data(index_shifted, role)
    #
    # def un_shifted_data(self, index: QModelIndex, role=Qt.EditRole):
    #     index_shifted = index.siblingAtRow(index.row() + self.TOTAL_ROWS)
    #     return self.data(index_shifted, role)

    def total_row_data(self, index: QModelIndex, role: int = Qt.EditRole):
        col = index.column()
        row = index.row()
        #############################
        # return total rows
        # ---------------------------
        # if row == 2:  # TODO: find total row by value
        #     index = index.siblingAtRow(0)
        #     row = row - 2
        #     if role == Qt.EditRole or role == Qt.DisplayRole:
        #         if col == 1:
        #             return self.serv.data_rc(row, col)
        #         if col == self.COL_SLEFT:
        #             return super().data(index, leftServ)
        #         if col == self.COL_SNAME:
        #             return self.serv.data_rc(row, col)
        #         if col == self.COL_TARIFF:
        #             return super().data(index, priceServ)
        #         if col == self.COL_SERV_SHOULD:
        #             return super().data(index, plannedServ)
        #         if col == self.COL_SERV_YEAR:
        #             return super().data(index, filledServ)
        #         # return 0
        #     else:
        #         return super().data(index, role)
        #############################
        # ROW_MONTH_NAMES
        # ---------------------------
        if row == self.ROW_MONTH_NAMES and self.months_columns:
            if col >= self.COL_SERV_START and (role == Qt.EditRole or role == Qt.DisplayRole):
                return self.months_columns[col - self.COL_SERV_START]
            else:
                return None  # TODO:
        #############################
        # ROW_WORKER_NAMES
        # ---------------------------
        elif row == self.ROW_WORKER_NAMES and self.worker_columns:
            if col >= self.COL_SERV_START and (role == Qt.EditRole or role == Qt.DisplayRole):
                col_ = col - self.COL_SERV_START
                try:
                    if self.is_total_col(col):
                        return self.tr("услуг в месяц")
                    elif self.is_money_col(col):
                        return self.tr("денег в месяц")
                    elif self.is_worker_col(col):
                        return self.dep_has_worker.data_by_id(self.worker_columns[col_],
                                                              self.dep_has_worker.tsFieldNames.index(
                                                                  "dep_has_worker"))
                    else:
                        error("wrong column - %s", col)
                        return "wrong column"
                except TypeError:
                    return "TypeError"
            else:
                return None
        return None

    # @Slot()
    # def updateLayout(self):
    #     super().updateLayout()
    #     self.headerDataChanged.emit(Qt.Vertical, 0, self.rowCount())

    def headerData(self, section, orientation, role=Qt.DisplayRole):
        #############################
        # Vertical orientation
        # ---------------------------
        if orientation == Qt.Vertical:
            if role == Qt.DisplayRole:
                if section == 0:
                    return self.tr("  ")
                if section == self.ROW_WORKER_NAMES:
                    return self.tr("Назв.")
                elif section == self.ROW_TOTAL_SERV:
                    return self.tr("Все")
                elif section == self.ROW_TO_PAY:
                    return self.tr("Платно")
                elif section == self.ROW_BM:
                    return self.tr("БытМед*%")
                elif section == self.ROW_SDD:
                    return self.tr("СДД и %")
                elif section == 6:
                    return self.tr(" ")
            #############################
            # shift for subtable
            # ---------------------------
            if section >= self.TOTAL_ROWS:
                shifted_section = section - self.TOTAL_ROWS
                if role == Qt.DisplayRole:
                    if self.serv and self.serv._init:
                        return self.serv.data_rc(shifted_section,
                                                 self.serv.tsFieldNames.index("tnum"))
                if role == Qt.ToolTipRole:
                    if self.serv and self.serv._init:
                        return self.serv.data_rc(shifted_section,
                                                 self.serv.tsFieldNames.index("serv"))
        return super().headerData(section, orientation, role)


class _tsYearTableAddTotalRows(YearRowLayoutModel):

    def __init__(self, parent=None):
        super().__init__(parent)
        self.contract = None
        self.contract_lock = RLock()
        self.contract_locked = False
        # self.contract_pay_data = DynamicList(DynamicList(0))
        # self.conn = SD.engine.connect()

    @lru_cache(500000)
    def total_row_data(self, index: QModelIndex, role=Qt.EditRole):
        row = index.row()
        col = index.column()
        #############################
        # count self.ROW_TOTAL_SERV
        # ---------------------------
        if row == self.ROW_TOTAL_SERV:
            try:
                if self.serv:
                    serv_index: QModelIndex = self.serv.index_by_id(0, "sub_serv")[0]
                    total_index = index.siblingAtRow(serv_index.row() + self.TOTAL_ROWS)
                    return total_index.data(role)
            except IndexError:
                return "Wrong set of services"
        #############################
        # count self.ROW_TO_PAY
        # ---------------------------
        if row == self.ROW_TO_PAY:
            if col not in [self.COL_SNAME, self.COL_TARIFF]:
                if role == Qt.EditRole or role == Qt.DisplayRole:
                    if self.is_money_col(col):
                        try:
                            return min(
                                float(self.get_data_sdd(col, C_MPAY, Qt.EditRole)),
                                self.get_paid_total(col) * self.get_data_sdd(col, C_PERC, Qt.EditRole))
                        except TypeError:
                            return self.tr("Не указан СДД")
                    return self.get_paid_total(col)
        #############################
        # count self.ROW_BM
        # ---------------------------
        if row == self.ROW_BM:
            if col not in [self.COL_SNAME, self.COL_TARIFF]:
                if role == Qt.EditRole or role == Qt.DisplayRole:
                    if self.is_money_col(col):
                        try:
                            return self.get_paid_total(col) * self.get_data_sdd(col, C_PERC, Qt.EditRole)
                        except TypeError:
                            return self.tr("Не указан СДД")
                    return self.get_paid_total(col)
        #############################
        # SDD and % and other data
        # ---------------------------
        elif row == self.ROW_SDD:
            # if col == 1: # for debug
            #     return str(self.data_in_month(12))
            # if col == 0:
            #     return str(self.data_in_month(1))
            if col >= self.COL_SERV_START:
                prev_col = col - 1
                if role == Qt.BackgroundRole:
                    if self.is_total_col(col):
                        if self.contract:
                            if self.get_data_sdd(col, C_IS_LAST):
                                return WARNING_COLOR
                    if self.is_total_col(prev_col):
                        if self.contract:
                            if not self.get_data_sdd(col, C_PERC_RIGHT):
                                return WARNING_COLOR
                if role == Qt.EditRole or role == Qt.DisplayRole:
                    if self.is_total_col(col):
                        if self.contract:
                            return str(self.get_data_sdd(col, C_SDD))
                    if self.is_total_col(prev_col):
                        if self.contract:
                            return self.get_data_sdd(col, C_PERC)
                    if self.is_money_col(col):
                        if self.contract:
                            return self.get_data_sdd(col, C_MPAY)
        else:
            return super().total_row_data(index, role)

    @Slot()
    def updateLayout(self):
        if not self.selection_in_progress:
            self.total_row_data.cache_clear()
            self.data_in_month.cache_clear()
            self.get_paid_total.cache_clear()
            self.data.cache_clear()
            super().updateLayout()

    def select(self):
        super().select()
        # if self.contract_id:
        #     thd = Thread(None, self.helper_set_contract_id, "thd-" + str(self.contract_id), args=(self.contract_id,))
        #     thd.start()
        #     return True

    def set_contract_id(self, value):
        if value > 0:
            thd = Thread(None, self.helper_set_contract_id, "thd-" + str(value), args=(value,))
            thd.start()
        super().set_contract_id(value)
        # if value > 0:
        #     thd.join()

    def helper_set_contract_id(self, contract_id):
        #############################
        # select orm
        # ---------------------------
        with self.contract_lock:
            self.contract_locked = True
            debug("start set_contract_id %s ", contract_id)
            try:
                self.contract = SD.session.query(Contracts).filter_by(id=contract_id)[0]
            except sqlalchemy.exc.OperationalError:
                debug("rollback set_contract_id %s ", contract_id)
                SD.session.rollback()
                SD.session.execute("CALL GET_PRIVILEGES")
                SD.session.execute("SET ROLE ALL")
                self.contract = SD.session.query(Contracts).filter_by(id=contract_id)[0]
            debug("end set_contract_id %s ", contract_id)
            #############################
            # clear cache
            # ---------------------------
            self.contract_locked = False
            try:
                # for i in range(12):
                #     self.contract_pay_data[i] = self.data_in_month(i)
                debug("end gathering data_in_month for contract_id - %s ", self.contract_id)
                self.data_in_month.cache_clear()
                self.get_paid_total.cache_clear()
                self.total_row_data.cache_clear()
                self.change_selection_in_progress.emit(True)
            except sqlalchemy.exc.OperationalError:
                self.helper_set_contract_id(contract_id)

    @lru_cache(100000000)
    def data(self, index: QModelIndex, role=Qt.EditRole):
        if role == Qt.CheckStateRole:
            return
        elif role == Qt.ToolTipRole or role == Qt.StatusTipRole:
            return super().data(index, Qt.DisplayRole)
        return super().data(index, role)

    @lru_cache(10000)
    def get_paid_total(self, col):  # TODO: update async
        res = 0
        for r in range(self.TOTAL_ROWS, self.rowCount()):
            paid = self.index(r, self.COL_TARIFF).data(Qt.EditRole)
            try:
                if paid > 0:
                    res += self.index(r, col).data(Qt.EditRole)
            except TypeError:
                pass
        return res

    def get_data_sdd(self, col, ai_type, role=Qt.DisplayRole):
        """
        :param col: table column
        :param ai_type: index of element in array below
            C_SDD = 0
            C_PERC = 1
            C_MPAY = 2
            C_PERC_RIGHT = 3
            C_IS_LAST = 4
        :return: one of:
            max_pay.sdd, max_pay.perc, max_pay.max_pay, max_pay.perc == max_pay.counted_perc(), new_at
        """
        col_ = col - self.COL_SERV_START
        month = self.months_columns[col_]
        ret = self.data_in_month(month)[ai_type]
        if role == Qt.EditRole:
            return ret
        if ai_type == C_SDD:
            return str(ret).replace(".", ",")
        elif ai_type == C_PERC:
            try:
                return str(ret * 100).replace(".", ",").replace(",0", "") + "%"
            except TypeError:
                return self.tr("Не указаны проценты")
        elif ai_type == C_MPAY:
            decimal.getcontext().prec = 12
            try:
                ret = decimal.Decimal(ret).quantize(decimal.Decimal('10000000.00'), rounding=decimal.ROUND_HALF_UP)
                return str(ret).replace(".", ",")
            except TypeError:
                self.tr("ошибка ")
        else:
            return ret

    @lru_cache(12)
    def data_in_month(self, month):
        debug("start data_in_month %s for contract_id - %s ", month, self.contract_id)
        if not self.contract_locked:
            with self.contract_lock:
                ret = self.contract.in_month_meta_pay(month, SD.last_year)
                # debug("end data_in_month %s ", month)
                # return self.contract_pay_data[month]
                return ret
        else:
            return [0, 0, 0, 0, 0]


class tsTableServYearWithSave(_tsYearTableAddTotalRows):
    unsaved: Signal = Signal(QObject)
    saved: Signal = Signal(QObject)
    setDirty: Signal = Signal(bool)

    def __init__(self, parent=None):
        super().__init__(parent)
        #############################
        # connection
        # ---------------------------
        self.table_change_history = OrderedDict()
        self.unsaved.connect(SD.set_unsaved)
        self.saved.connect(SD.set_saved)
        self.pending_edit = None

    def select(self):
        self.table_change_history.clear()
        res = super().select()
        self.updateLayout()
        return res

    def row_id(self, row):
        return row

    def setData(self, index, value, role=Qt.EditRole):
        #############################
        # only int
        # ---------------------------
        try:
            value = int(value)
        except ValueError:
            return
        #############################
        # checks worker_id, serv_id, total
        # ---------------------------
        ce: cellEdit = SD.journal.pending_edit
        wid = self.get_worker(index.column())
        if wid:
            sids = self.data_by_row(index.row() - self.TOTAL_ROWS, idListServ)
            if len(sids) == 1:
                sid = sids[0]
                rows = self.gmdata.rows_by_id(wid, "dep_has_worker_id", sid, "serv_id")
                gmdata_row = self.gmdata.special_row
                if len(rows):
                    gmdata_row = rows[0].row()
                # elif len(rows) == 0:
                #     ce.row_id = self.gmdata.row_id(self.gmdata.special_row)
                ce.row_id = self.gmdata.row_id(gmdata_row)
                gmdata_col = self.gmdata.tsFieldNames.index("month1") - 1 + self.get_month(index.column())
                ce.col_name = self.gmdata.tsFieldNames[gmdata_col]
                self.pending_edit = (index, value)
                # old_dat = index.data(Qt.EditRole)
                rec = {"serv_id": sid, "dep_has_worker_id": wid, "year1": SD.last_year,
                       "dep_id": SD.last_dep, "contracts_id": self._contract_id}
                # SD.commit_edit(self.gmdata, old_dat, value, rec)
                self.gmdata.set_new_rec_autofill_raw(**rec)
                self.gmdata.setData(self.gmdata.index(gmdata_row, gmdata_col), value, Qt.EditRole)
                # self.pending_edit = None
                if True:
                    self.gmdata.cache_clear()
                    self.gmdata_serv_in_month.cache_clear()
                    self.gmdata_serv_money_in_month.cache_clear()
                    self.gmdata_total_money_in_month.cache_clear()
                    self.updateLayout()

    def add_worker(self, dep_has_worker_id, month0=0):
        month = month0 + 1
        self.months_columns_new.append(month)
        self.worker_columns_new.append(dep_has_worker_id)
        if True:
            self.gmdata.cache_clear()
            self.gmdata_serv_in_month.cache_clear()
            self.gmdata_serv_money_in_month.cache_clear()
            self.gmdata_total_money_in_month.cache_clear()
            self.updateLayout()

    def workers_in_month(self, month0):
        """ Returns all workers in the month0 """
        wlist = []
        for col in range(len(self.months_columns)):
            if self.months_columns[col] == month0 and \
                    isinstance(self.worker_columns[col], int):
                wlist.append(self.worker_columns[col])
        return wlist

    # @lru_cache(5000000)
    # def sum_in_month(self, col_, serv_id):
    #     month = self.months_columns[col_]
    #     summ = 0
    #     for i in range(col_, self.reversed_months_columns.index(self.months_columns[col_])):
    #         col = i + self.COL_SERV_START
    #         if self.is_worker_col(col):
    #             summ = + self.get_serv_in_month(self.contract_id, serv_id, month, self.worker_columns[i],
    #                                             SD.last_dep)
    #     return summ
    #
    # @lru_cache(5000000)
    # def get_serv_in_month(self, contract_id, serv_id, month, worker_in_col, dep_id):
    #     if contract_id != self._contract_id:
    #         return False  # raise?
    #     return self.gmdata.data_month(month, serv_id, worker_in_col, dep_id != SD.last_dep)


class tsTableServYearModel(tsTableServYearWithSave):
    pass

# class OuterDataFormatter():
#     def __init__(self, parent=None):
#         self.inner_class = tsTableServYearWithSave(parent)
#         self.ic = self.inner_class
#
#     def __setattribute__(self, key, value):
#         return getattribute(self.ic, key, value)
#
#     def __getattribute__(self, item):
#         return getattribute(self.ic, item)
#
#     def data(self, index, role):
#         if role == Qt.CheckStateRole:
#             return
#         elif role == Qt.DisplayRole:
#             ret = self.ic.data(index, Qt.DisplayRole)
#             if ret:
#                 ret = str(ret)
#                 if len(ret) >= 3 and ret[-2] == ",":
#                     ret += "0"
#             return ret
#         return self.ic.data(index, role)
