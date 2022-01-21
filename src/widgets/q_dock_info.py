#!/usr/bin/python3
# -------------------------------------------------------------------------------
# -*- coding: utf-8 -*-
# Name:        AIS 3USON infoQDockWidget
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

from queue import LifoQueue
from widgets.q_combo_box_with_data_mapper import *
from qtpy.QtWidgets import QDockWidget


class Worker(QObject):
    """ Work in thread"""
    resultReady: Signal = Signal()  # str, list

    def __init__(self, parent=None, run_func=None):
        super().__init__(parent)
        self.run_func = run_func
        self.resutls = {}
        self.results_lock = QRecursiveMutex()
        self.resutls[""] = []
        self.queue = LifoQueue()

    @Slot()
    @Slot(str, list)
    def do_work(self, key="", args=None):
        # debug("thread called")
        # get one arg - list, and convert it into list or args for run_func # TODO: support of **kwargs

        try:
            if args:
                with QMutexLocker(self.results_lock):
                    args2 = args.copy()
                self.resutls[key] = self.run_func(*args2)
                self.queue.put(self.resutls[key])
                self.resultReady.emit()
            else:
                # with QMutexLocker(self.results_lock):
                self.resutls[key] = self.run_func()
                self.queue.put(self.resutls[key])
                self.resultReady.emit()
        except:
            critical("error in thread - %s", self.parent().objectName())


@add_method(Worker)
def _get_money_in_month(client_id, vdate):
    # TODO: if isVisible()
    # servform_id = self.servform_id
    res = []
    if client_id and vdate:  # and servform_id
        month = vdate.month()
        year = vdate.year()
        _, endday = calendar.monthrange(year, month)
        start = QDate(year, month, 1)
        end = QDate(year, month, endday)
        sql = """
            call contract_pay_inmonth(?, ?, ?)
        """
        # .format(client_id, start.toString(SQL_DATE_FORMAT), end.toString(SQL_DATE_FORMAT))  # , servform_id
        #############################
        # get data and store it in self._get_money_in_month
        # ---------------------------
        qry = QSqlQuery(SD.get_db)
        qry.prepare(sql)
        qry.addBindValue(client_id)
        qry.addBindValue(start.toString(SQL_DATE_FORMAT))
        qry.addBindValue(end.toString(SQL_DATE_FORMAT))
        ok = qry.exec_()
        if ok:
            res = []
            while qry.next():
                d = dict()
                for i in range(qry.record().count()):
                    d[qry.record().fieldName(i)] = qry.value(i)
                res.append(d)
            if not res:
                res.append({"to_pay": 0, "perc": 0, "quantity": 0, "client_id": client_id, "servform_id": 0, "contracts": 0,
                            "contracts_id": 0, "startdate": 0, "enddate": 0, "vdate_m": start.month(),
                            "vdate_y": start.year()})
        else:
            error("connection error _get_money_in_month()")
    return res


class infoQDockWidget(QDockWidget):
    update_view_needed: Signal = Signal()
    thread_operate: Signal = Signal(str, list)

    def __init__(self, parent=None):
        super().__init__(parent)
        self.client_id = 0
        self.servform_id = 0
        self.vdate: QDate = QDate.currentDate()
        self._latest_money_in_month = []
        self.update_view_needed.connect(self.update_view, Qt.QueuedConnection)
        self.sql_thread = QThread()
        UI.qthreads.append(self.sql_thread)
        self.worker = Worker()
        self.sql_thread.setObjectName("dockinfo_sql_thread")
        # self.sql_thread.moveToThread(self.sql_thread)
        self.worker.moveToThread(self.sql_thread)
        self.worker.run_func = self.worker._get_money_in_month
        # setattr( self.worker,"run_func",  _get_money_in_month)
        self.sql_thread.start(QThread.LowPriority)
        self.thread_operate.connect(self.worker.do_work, Qt.QueuedConnection)
        self.worker.resultReady.connect(self.latest_money_in_month, Qt.QueuedConnection)
        self.lqueue = LifoQueue()
        self.worker.queue = self.lqueue
        self.to_send = [self.client_id, self.vdate]
        self.outdated = False

    # def get_money_current_month(self, model, client_id):
    #     if self.vdate:
    #         vdate = self.vdate
    #     else:
    #         vdate = QDate.currentDate()
    #     pass
    #
    # def get_money(self, client_id, vdate):
    #     pass

    def get_money_in_month(self):
        """ Main function to end work into thread"""
        if self.isVisible():
            if not self.vdate:
                self.vdate = QDate.currentDate()
            with QMutexLocker(self.worker.results_lock):
                self.to_send.clear()
                self.to_send.append(self.client_id)
                self.to_send.append(self.vdate)
            self.thread_operate.emit("", self.to_send)
            self.outdated = False
        else:
            self.outdated = True

    def show(self):
        if self.outdated:
            self.get_money_in_month()
        return super(infoQDockWidget, self).show()

    @Slot()
    # @Slot(str, list)
    def latest_money_in_month(self):  # , key="", res: list = None
        """
        """
        if self.lqueue.empty():
            return
        self._latest_money_in_month = self.lqueue.get()
        while not self.lqueue.empty():
            self._latest_money_in_month = self.lqueue.get()
        # with self.worker.results_lock:
        #     self._latest_money_in_month = copy.deepcopy(res)
        self.update_view_needed.emit()

    def get_money_in_month_data(self):
        return self._latest_money_in_month

    @Slot(int)
    def update_client_id(self, client_id: int):
        if self.client_id != client_id:
            self.client_id = client_id
            Qtimer_runner(self.get_money_in_month, 300, "get_money_in_month")

    @Slot(QDate)
    def update_vdate(self, vdate: QDate):
        if self.vdate != vdate:
            if self.vdate.month() != vdate.month() or self.vdate.year() != vdate.year():
                self.vdate = vdate
                Qtimer_runner(self.get_money_in_month, 300, "get_money_in_month")

    @Slot()
    def sub_month(self):
        if self.vdate:
            self.vdate = self.vdate.addMonths(-1)
            Qtimer_runner(self.get_money_in_month, 300, "get_money_in_month")

    @Slot()
    def recheck(self):
        Qtimer_runner(self.get_money_in_month, 450, "get_money_in_month")

    @Slot()
    def add_month(self):
        if self.vdate:
            self.vdate = self.vdate.addMonths(1)
            Qtimer_runner(self.get_money_in_month, 300, "get_money_in_month")

    @Slot()
    def update_view(self):
        from logic.data_worker import WD
        data_array = self.get_money_in_month_data()
        try:
            # ui = self.ui
            ui = self.parent().ui
            cbxsf: myQComboBox = ui.cbx_1_servform
            for i, data in enumerate(data_array):
                if i == 0:
                    ui.qle_last_fio.setText(WD.get_data_from_model_name("client", "client", data["client_id"]))
                    ui.qle_last_fio.setCursorPosition(0)
                    ui.qle_topay.setText("{0:0.2f}".format((data["to_pay"])))
                    try:
                        ui.qle_contract.setText(
                            "{} от {} до {}".format(
                                data["contracts"],
                                data["startdate"].toString(DEF_DATE_FORMAT),
                                data["enddate"].toString(DEF_DATE_FORMAT)
                            ))
                    except:
                        ui.qle_contract.setText("{}".format(data["contracts"]))
                    ui.qle_contract.setCursorPosition(0)
                    ui.qle_serv_total.setText("{}".format((data["quantity"])))
                    cbxsf.set_current_index_id(data["servform_id"])
                    cbxsf.lineEdit().setCursorPosition(0)
                    ui.qle_month.setText(
                        self.tr("{}, {}%".format(
                            QDate(data["vdate_y"], data["vdate_m"], 1).toString("MMM yyyy"),
                            str(data["perc"] * 100)
                        )))
                else:
                    ui.qle_topay.setText(ui.qle_topay.text() + " | " + "{0:0.2f}".format((data["to_pay"])))
                    try:
                        ui.qle_contract.setText(ui.qle_contract.text() + " | " +
                                                "{} от {} до {}".format(
                                                    data["contracts"],
                                                    data["startdate"].toString(DEF_DATE_FORMAT),
                                                    data["enddate"].toString(DEF_DATE_FORMAT)
                                                ))
                    except:
                        ui.qle_contract.setText("{}".format(data["contracts"]))
                    ui.qle_serv_total.setText(ui.qle_serv_total.text() + " | " + "{}".format((data["quantity"])))
                    if cbxsf.currentIndex() != data["servform_id"]:
                        cbxsf.clear()
                    ui.qle_month.setText(ui.qle_month.text() + " | " +
                                         self.tr("{}, процент: {}%".format(
                                             QDate(data["vdate_y"], data["vdate_m"], 1).toString("MMM yyyy"),
                                             str(data["perc"] * 100)
                                         )))
        except TypeError:
            pass
