#!/usr/bin/python3
# -------------------------------------------------------------------------------
# -*- coding: utf-8 -*-
# Name:        AIS 3USON Main QT Frontend
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

#############################
# import this project files
# ---------------------------
from qtpy.QtWidgets import QFileDialog
from qtpy.QtCore import QSize
from qtpy.QtGui import QPixmap
from qtpy.QtWidgets import QDialog
from qtpy.QtWidgets import QLineEdit
from qtpy.QtGui import QImage
from qtpy.QtWidgets import QLabel, QInputDialog
from qtpy.QtGui import QRegularExpressionValidator

from import_from_file import ImportJsonModel
from logic.data_worker import *

from models.ts_models_serv_year import tsTableServYearModel
from models.universal_delegate import tsItemDelegate
from worker.login_key_auth import generate_api_key
import json


class QOBase(QObject):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = self.parent().ui
        self.__init = False
        self.connectSlotsByName(self.ui)
        # self.connectSlotsByName(self)
        self.connectSlotsByName(SD)
        self.dm_set = set()

    @Slot(QObject)
    def connectSlotsByName(self, qui_obj: QObject):
        """
        just like QMetaObject::connectSlotsByName but for user class
            ui_obj is object with signals
        """
        ui_obj = qui_obj
        class_obj = self
        # def run_connectSlotsByName(ui_obj: QObject, class_obj):
        # print(dir(class_obj))
        methods = {name: getattr(class_obj, name) for name in dir(class_obj) if "on_" in name[0:3]}
        # methods = ifilter(inspect.ismethod, methods)
        debug(methods)
        # if ui_obj.parent():
        #     ui_obj=ui_obj.parent()
        for name, method in methods.items():
            # debug(method)
            narr = name.split("_")
            mname = "_".join(narr[1:-1])
            mcall = "_".join(narr[-1:])
            # el=ui_obj.findChildren(mname ,Qt.FindChildrenRecursively)
            el = ui_obj.findChild(QWidget, mname)
            if el is None and ui_obj.objectName() == mname:
                el = ui_obj
            if el is not None:
                # signal1=getattr(type(el), mcall)
                signal: Signal = getattr(el, mcall)
                debug("%s.%s connected to %s.%s ", class_obj, name, el.objectName(), mcall)
                try:
                    signal.connect(method)
                    debug("connected " + name)
                except:
                    debug("failed connected " + name)

        #############################
        # run in threads
        # ---------------------------
        # class_obj = self
        # Qtimer_runner(run_connectSlotsByName, 0, "run_connectSlotsByName" + str(self), qui_obj, class_obj)
        # half second faster when -
        # run_connectSlotsByName(qui_obj, self)


class clstab_debug(QOBase):
    #############################
    # check sql queries - for debug
    # ---------------------------
    @Slot()
    def on_btn_check_sql_clicked(self):
        """
        """
        ui = self.ui
        qry = QSqlQuery(SD.get_db)
        qry.exec_(ui.txt_sql.toPlainText())
        res = ""
        while qry.next():
            for i in range(qry.record().count()):
                res = res + str(qry.record().value(i))
            res = res + "\n"
        ui.txt_sql2.setPlainText(res + qry.lastError().text())
        #############################
        # set TableView
        # ---------------------------
        if res:
            table: stubQTableView = ui.test_tableView
            mdl = tsSqlTableModel("test", table)
            qset: QSettings = SD.qsettings
            qset.setValue(mdl.objectName() + "_sql_sc_version", 1)
            mdl.setQuery(qry)
            mdl.setMetaInfo()
            mdl._update_relations()
            debug(mdl.selectStatement())
            table.setModel(mdl)


class clstab_dock_people_info(QOBase):
    def __init__(self, parent):
        super().__init__(parent)
        ui = self.ui
        self.me = ui.dock_people_info


class clstab_contract_planned(QOBase):

    @Slot()
    def on_btn_paste_planned_clicked(self):
        try:
            paste_planned(self.ui.table__contracts_has_serv__where_contracts_id__by_contracts_id)
        except:
            pass


class clstab_pcat(QOBase):
    def __init__(self, parent):
        super().__init__(parent)
        self.me = self.ui.tab_pcat

    @Slot(bool)
    def on_tab_pcat_widgetVisibilityChanged(self, state):
        ui = self.ui
        cbox: myQComboBox = ui.cbx_1__dep_has_client
        table: myQTableView = ui.table_client_has_category__by_client_id
        table.set_first_filter_exact(cbox.currentText())


class clstab_workers(QOBase):
    def __init__(self, parent):
        super().__init__(parent)
        ui = self.ui
        self.me: myQWidget = ui.tab_workers
        # self.__init = False
        self.dep_has_worker: myQTableView = ui.table_dep_has_worker__by_worker_id

    @Slot()
    def on_btn_show_qrcode_clicked(self):
        try:
            index: QModelIndex = self.dep_has_worker.selectedIndexes()[0]
            name = index.siblingAtColumn(index.model().index_of_col("dep_has_worker")).data(Qt.EditRole)
            password, key, qr_image = generate_api_key(
                name=index.siblingAtColumn(index.model().index_of_col("dep_has_worker")).data(Qt.EditRole),
                dep=index.siblingAtColumn(index.model().index_of_col("dep_id")).data(Qt.DisplayRole),
                worker_dep_id=index.siblingAtColumn(index.model().index_of_col("id")).data(Qt.EditRole),
                password=index.siblingAtColumn(index.model().index_of_col("api_key")).data(Qt.EditRole)
            )
            dep_name = index.siblingAtColumn(index.model().index_of_col("dep_id")).data(Qt.DisplayRole)
            try:
                window = QDialog(UI.main_window)
                window.setWindowModality(Qt.WindowModal)
                window.resize(600, 600)
                window.setWindowTitle("QR код работника, отделение: " + dep_name)
                verticalLayout = QVBoxLayout(window)
                qlable = QLabel(parent=window)
                verticalLayout.addWidget(qlable)
                qlable.setText("QR код работника отделения: " + name)
                qtext = QLineEdit(parent=window)
                qtext.setText(str(key))
                verticalLayout.addWidget(qtext)
                q_img_label = QLabel(parent=window)
                q_img = QImage(qr_image)
                q_img_label.setPixmap(QPixmap.fromImage(q_img))
                q_img_label.setScaledContents(1)  # TODO: check window size on small monitors
                verticalLayout.addWidget(q_img_label)
                window.show()
                window.exec()
            except:
                pass
        except IndexError:
            UI.QMessageBox.information(UI, "Не выбран работник", UI.tr("Пожалуйста выберите работника отделения"))


class clstab_admin(QOBase):
    def __init__(self, parent):
        super().__init__(parent)
        ui = self.ui
        self.me: myQWidget = ui.tab_admin
        self.__init = False
        self.pass_list = DynamicList("")

    #############################
    # Add admin tab
    # ---------------------------
    @Slot(bool)
    def on_tab_admin_widgetVisibilityChanged(self, state):
        if not self.__init:
            ui = self.ui
            self.__init = True
            ui.lineEdit_login.setValidator(QRegularExpressionValidator("[a-z]+"))
            # self.ui.cbx_1_worker__pass.setCurrentIndex(0)
            self.table: myQTableView = ui.table_dep_has_worker__by_worker_id__3
            self.table.set_first_filter_exact(ui.cbx_1_worker__pass.currentText())

    def on_btn_pw_gen_clicked(self):
        self.ui.lineEdit_pass.setText(WD.pw_gen())

    def on_btn_update_login_pass_clicked(self):
        ui = self.ui
        cbx_w: myQComboBox = ui.cbx_1_worker__pass
        # cbx_r: myQComboBox=ui.cbx_1_role__pass
        if (ui.lineEdit_login.text()
                and ui.lineEdit_login.text()
                and ui.lineEdit_pass.text() != "********"
                and ui.cbx_1_worker__pass.currentIndex() >= 0):
            # and ui.cbx_1_role__pass.currentIndex() > 0
            worker_id = cbx_w.model().data_rc(cbx_w.currentIndex(), cbx_w.model().index_of_col("id"))
            # role_id=cbx_r.currentData()
            # if ui.lineEdit_pass.text():
            sql_cmd = """
                update worker set user='{}'
                where id={};
            """.format(ui.lineEdit_login.text(), worker_id)
            debug(sql_cmd)
            ret = SD.line_query(sql_cmd)
            ret2 = SD.line_query("""
                call replace_user('{}','{}',{})
            """.format(ui.lineEdit_login.text(), ui.lineEdit_pass.text(), worker_id))
            if ret is None and ret2 == "finished":
                ui.statusBar().showMessage(self.tr("Логин работника обновлен"))
                self.pass_list[ui.cbx_1_worker__pass.currentIndex()] = ui.lineEdit_pass.text()
                ui.qle_fio_log_pass.setText(
                    ui.cbx_1_worker__pass.currentText() + "\t" +
                    ui.lineEdit_login.text() + "\t" +
                    ui.lineEdit_pass.text())
            else:
                ui.statusBar().showMessage(self.tr("Ошибка логин работника НЕ обновлен ") + str(ret) + str(ret2))
        else:
            ui.statusBar().showMessage(self.tr("Выбраны не все поля"))

    @Slot(int)
    def on_cbx_1_worker__pass_currentIndexChanged(self, ind: int):
        ui = self.ui
        cbx_pass: myQComboBox = ui.cbx_1_worker__pass
        mdl: tsSqlTableModel = cbx_pass.model()
        ui.lineEdit_login.setText(mdl.data_rc(cbx_pass.currentIndex(), mdl.index_of_col("user")))
        ui.lineEdit_pass.setText(self.pass_list[ui.cbx_1_worker__pass.currentIndex()])


class clstab_fio_dep(QOBase):
    def __init__(self, parent):
        super().__init__(parent)
        ui = self.ui
        self.me: myQWidget = ui.tab_fio_dep
        self.__init = False

    #############################
    # Add admin tab
    # ---------------------------
    @Slot(bool)
    def on_tab_fio_dep_widgetVisibilityChanged(self, state):
        # tr = self.tr
        # ui = self.ui
        if not self.__init:
            self.__init = True

    @Slot(str)
    def on_qle_fio_filter_textChanged(self, text: str):
        ui = self.ui
        tr = self.tr
        if text:
            ui.label_fio_filter.setText(tr("Используется фильтр:"))
        else:
            ui.label_fio_filter.setText(tr("Быстрый фильтр:"))

    @Slot()
    def on_btn_goto_client_from_list_clicked(self):
        ui = self.ui
        tabs: myQTabWidget = ui.tabMain
        table: myQTableView = ui.table__dep_has_client__by_client
        indexes = table.selectedIndexes()
        if len(indexes) == 1:
            uid = indexes[0].siblingAtColumn(0).data(Qt.EditRole)
            if uid:
                tabs.set_active_tab_by_name("tab_clients")
                cbxs: myQComboBox = ui.cbx_1__dep_has_client
                cbxs.set_current_index_id(uid)

    @Slot()
    def on_btn_goto_serv_from_list_clicked(self):
        ui = self.ui
        tabs: myQTabWidget = ui.tabMain
        table: myQTableView = ui.table__dep_has_client__by_client
        indexes = table.selectedIndexes()
        if len(indexes) == 1:
            uid = indexes[0].siblingAtColumn(0).data(Qt.EditRole)
            if uid:
                tabs.set_active_tab_by_name("tab_add_serv")
                cbxs: myQComboBox = ui.cbx_1__dep_has_client__3
                cbxd: myQComboBox = ui.cbx_1__dep_has_client__2
                cbxs.set_current_index_id(uid)
                cbxd.set_current_index_id(uid)


class clstab_client_contr(QOBase):
    def __init__(self, parent):
        super().__init__(parent)
        ui = self.ui
        self.me: myQWidget = ui.tab_client_contr
        # self.dbconnect = False
        self.__init = False

    #############################
    # Add services tab
    # ---------------------------
    @Slot(bool)
    def on_tab_client_contr_widgetVisibilityChanged(self, state):
        self._init()
        # ripso_id = SD.line_query("""
        #     select ripso_id from dep_has_ripso dhr
        #     join ripso r on r.id =  dhr.ripso_id
        #     where dep_id = {} and r.archive = 0 order by ripso_id limit 1 """.format(SD.last_dep)
        #                           )
        # , "ripso_id": ripso_id
        # self.dm.model().super_model().set_new_rec_autofill(**{
        #     "dep_id": SD.last_dep
        # })

    def _init(self):
        if (not self.__init) and SD._dbconnected:
            ui = self.ui
            self.__init = True
            cbx_contracts = ui.cbx_1_contracts__by_client_id
            #############################
            # get inited model
            # ---------------------------
            cbx_contracts.init_model()  # just to be sure
            cbx_contracts.set_val_after_filter = 1
            mdl: tsSqlTableModel = cbx_contracts.model().super_model()
            if not mdl.meta_init:
                self.__init = False
                return
            dm: tsQDataWidgetMapper = cbx_contracts.dm
            self.dm_set.add(dm)
            #############################
            # set tsQDataWidgetMapper
            # ---------------------------
            dm.addMapping(ui.qle_contracts, mdl.record().indexOf("contracts"))
            dm.addMapping(ui.cbx_0__dep_has_ripso, mdl.index_of_col("ripso_id"))
            # dm.addMapping(ui.cbx_1__dep_has_ripso, mdl.index_of_col("ripso_id"), b"currentData")
            dm.addMapping(ui.cbx_0_worker_has_dep, mdl.index_of_col("dep_id"))
            self.cbx_ripso: QComboBox = ui.cbx_0__dep_has_ripso
            self.cbx_dep: QComboBox = ui.cbx_0_worker_has_dep
            dm.addMapping(ui.de_startdate, mdl.record().indexOf("startdate"))
            dm.addMapping(ui.de_enddate, mdl.record().indexOf("enddate"))
            dm.addMapping(ui.sp_ippsuNum, mdl.record().indexOf("ippsuNum"))
            dm.addMapping(ui.pte_contracts_note, mdl.record().indexOf("note"))
            dm.addMapping(ui.chk_blocked, mdl.record().indexOf("blocked"))
            dm.addMapping(ui.chk_to_recheck, mdl.record().indexOf("to_recheck"))
            dm.addMapping(ui.dte_check_date, mdl.record().indexOf("check_date"))
            dm.addMapping(ui.qle_contracts2, mdl.record().indexOf("contracts2"))
            dm.model().beginResetModel()
            dm.model().endResetModel()

    # @Slot(int)
    # def on_cbx_1__dep_has_client_currentIndexChanged(self, ind):
    #     ui = self.ui
    #     uid = ui.cbx_1__dep_has_client.current_id()
    #     if uid and uid != SD.last_client:
    #         pass
    #         SD.set_last_client(uid)
    #         # WD.client_id_changed.emit("client_id", str(uid))
    #         cbx: myQComboBox =cbx_contracts
    #         cbx.super_model().select()
    #         # TODO: set default contract


#############################
# Main Clients Tab
# ---------------------------
class clstab_clients(QOBase):

    @Slot()
    def on_btn_goto_client__3_clicked(self):
        ui = self.ui
        tabs: myQTabWidget = ui.tabMain
        if SD.last_table in [ui.table_client__by_client, ui.table__client_has_valid_contracts__by_client,
                             ui.table__dep_has_client_by_ripso__by_client,
                             ui.table__client_has_invalid_contracts__by_client]:
            table: myQTableView = SD.last_table
            client_id = table.currentIndex().siblingAtColumn(1).data(Qt.EditRole)
            if client_id:
                tabs.set_active_tab_by_name("tab_client")
                cbox: myQComboBox = ui.cbx_1__dep_has_client
                cbox.set_current_index_id(client_id)

    @Slot()
    def on_btn_new_contract_clicked(self):
        ui = self.ui
        tabs: myQTabWidget = ui.tabMain
        if SD.last_table in [ui.table_client__by_client, ui.table__client_has_valid_contracts__by_client,
                             ui.table__dep_has_client_by_ripso__by_client,
                             ui.table__client_has_invalid_contracts__by_client]:
            table: myQTableView = SD.last_table
            client_id = table.currentIndex().siblingAtColumn(1).data(Qt.EditRole)
            if client_id:
                tabs.set_active_tab_by_name("tab_client")
                cbox: myQComboBox = ui.cbx_1__dep_has_client
                cbox.set_current_index_id(client_id)
                tabs2 = ui.tab_client
                tabs2.set_active_tab_by_name("tab_client_contr")


#############################
# Main Client Tab
# ---------------------------
class clstab_client(QOBase):

    def __init__(self, parent):
        super().__init__(parent)
        ui = self.ui
        self.me: myQWidget = ui.tab_client
        #############################
        # custom init
        # ---------------------------
        self.__init = False

    @Slot(str)
    def on_qle_table_client_filter_textChanged(self, text: str):
        ui = self.ui
        tr = self.tr
        if text:
            ui.label_client.setText(tr("Используется фильтр:"))
        else:
            ui.label_client.setText(tr("Быстрый фильтр:"))

    def _init(self):
        if not self.__init:
            self.__init = True
            tr = self.tr
            ui = self.ui
            fdm: tsQDataWidgetMapper = ui.cbx_1__dep_has_client.dm
            self.dm_set.add(fdm)
            meta_init = False
            try:
                mdl: tsSqlTableModel = fdm.model().super_model()
                meta_init = mdl.meta_init
            except AttributeError:
                return
            if not meta_init:
                self.__init = False
                return
            fdm.addMapping(ui.qle_FIO, mdl.record().indexOf("client"))
            fdm.addMapping(ui.sp_ESRN, mdl.record().indexOf("ESRN"))
            fdm.addMapping(ui.qle_SNILS, mdl.record().indexOf("snils"))
            fdm.addMapping(ui.dateEdit_birth, mdl.record().indexOf("clientbirth"))
            fdm.addMapping(ui.dateEdit_death, mdl.record().indexOf("clientDeath"))
            fdm.addMapping(ui.lineEdit_phone, mdl.record().indexOf("phone"))
            fdm.addMapping(ui.pte_note, mdl.record().indexOf("prim"))
            table_view_main_by_dep: myQTableView = ui.table_main__where_client_id__by_dep_id
            table_view_main_by_dep.init_model(True)
            table_view_main_by_dep.set_first_filter_exact(SD.last_dep)  # TODO: need complex department support here
            fdm.model().beginResetModel()
            fdm.model().endResetModel()

    @Slot()
    def on_btn_goto_serv_add_clicked(self):
        ui = self.ui
        tabs: myQTabWidget = ui.tabMain
        for fiodata in self.dm_set:
            if "client" in fiodata.super_model().tsFieldNames:
                tabs.set_active_tab_by_name("tab_add_serv")
                uid = fiodata.current_id()
                if uid:
                    cbxs: myQComboBox = ui.cbx_1__dep_has_client__3
                    cbxd: myQComboBox = ui.cbx_1__dep_has_client__2
                    cbxs.set_current_index_id(uid)
                    cbxd.set_current_index_id(uid)

    #############################
    # Add services tab
    # ---------------------------
    # noinspection PyArgumentList
    @Slot(bool)
    def on_tab_client_widgetVisibilityChanged(self, state):
        self._init()
        table: myQTableView = self.ui.table__client_has_add_info__where_client_id__by_contracts_id
        table.init_model_filter()
        table.hideColumn(0)
        table1: myQTableView = self.ui.table__client_has_add_info__where_client_id__by_client_id
        table1.init_model_filter()
        table1.hideColumn(0)


class clstab_services(QOBase):
    #############################
    # Add services tab
    # ---------------------------
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui.comboFIO = self.ui.cbx_1__dep_has_client__2
        self.ui.comboW = self.ui.cbx_1__dep_has_worker
        # self.ui.comboW2 = self.ui.
        self.ui.comboServ = self.ui.cbx_1__serv_activ__dis_total
        self.main_table: myQTableView = self.ui.table__dep_has_main__where_vdate__by_vdate
        self.main_model: tsSqlTableModel = None
        self.__init = False

    @Slot(bool)
    def on_tab_add_serv_widgetVisibilityChanged(self, state):
        """
        """
        ui = self.ui
        # models = WD.models
        if not self.__init:
            self.__init = True
            ui.qle_date.setDate(QDate.currentDate())
            # ui.qleAmount2.setValue(0)
            # ui.qleAmount.setValue(0)
            self.main_table.init_model(True)
            self.main_model = self.main_table.super_model()
            #############################
            # disallow select total services
            # ---------------------------
            debug("clstab_services init done")
            ui.comboServ.init_model()
            mdl: tsQsfpModel = ui.comboServ.model()
            mdl.super_model().unselectable_items_by()

    @Slot(int)
    def on_cbx_1__serv_activ__dis_total_currentIndexChanged(self, ind):
        # comboServ
        self.set_qle_serv_left()

    @Slot(int)
    def on_cbx_1__dep_has_client__2_currentIndexChanged(self, ind):
        # comboFio
        self.set_qle_serv_left()
        # self.upd_info_docker_for_tab(ind)

    def set_qle_serv_left(self):
        ui = self.ui
        tr = self.tr
        ui.qle_serv_left.setText(tr("выполняется запрос данных"))
        Qtimer_runner(self._set_qle_serv_left, 250, "set_qle_serv_left")

    @Slot()
    def _set_qle_serv_left(self):
        #############################
        # collect data
        # ---------------------------
        ui = self.ui
        client = get_cbox_data(ui.comboFIO)
        serv = get_cbox_data(ui.comboServ)
        vdate = ui.qle_date.date()
        #############################
        # display status for data
        # ---------------------------
        sleft, ret_status = WD.get_status_for(client, serv, vdate)
        fio = get_cbox_data(ui.comboFIO, 1)
        ret_status = ret_status + " - (" + str(fio) + ")"
        ui.qle_serv_left.setText(ret_status)
        ui.statusBar().showMessage(ret_status)

    @Slot(QDate)
    def on_qle_date_dateChanged(self, ndate=None):
        ui = self.ui
        vdate = ui.qle_date.date()
        self.set_qle_serv_left()
        #############################
        # set model where by date
        # ---------------------------
        where = " vdate between '%s' and '%s' "
        where = where % (vdate.toString(SQL_DATE_FORMAT), vdate.toString(SQL_DATE_FORMAT))
        mdl: tsSqlTableModel = self.ui.table__dep_has_main__where_vdate__by_vdate.model()
        if mdl:
            mdl = mdl.super_model()
            mdl.setFilter(where)
        else:
            Qtimer_runner(self.on_qle_date_dateChanged, 1000, "self.on_qle_date_dateChanged")

    def pre_ins_main(self, return_focus_to=None):
        ui = self.ui
        if self.main_model:
            model = self.main_model
            # view = active tab table ?
            client = get_cbox_data(ui.comboFIO)
            vdate = ui.qle_date.date()
            contract = get_contract(client, vdate, SD.last_dep)
            amount = ui.qleAmount.value()
            if amount <= 0:  # TODO: more checks
                msg = self.tr("Услуга не добавлена, введите колличество услуг")
                UI.main_window.statusBar().showMessage(msg)
            if contract == 0:
                ui.statusBar().showMessage(self.tr("Ошибка: Возможно у данного человека нет действующего"
                                                   " договора в этот день \n\n"))
                return
            elif contract < 0:
                ui.statusBar().showMessage(self.tr("Ошибка: Возможно у данного человека открыто несколько договоров"))
                return
            elif contract > 0:
                rec = {
                    "contracts_id": contract,
                    "dep_id": SD.last_dep,
                    "serv_id": get_cbox_data(ui.comboServ),
                    "vdate": vdate,
                    "dep_has_worker_id": get_cbox_data(ui.comboW),
                    "note": ui.qleNote.text(),
                    "quantity": amount,
                    "client_id": client
                }
                SD.start_edit(None, model, model.row_id(model.special_row), "client_id")
                ce = model.insert_row(rec)
                ret = True
                # SD.journal.pending_edit = cellEdit(None, model, model.row_id(model.special_row), "client_id")
                # ret, add_msg = WD.ins_main(qry_data)
                if ui.chk_autosave.checkState():
                    ret = ce.save()
                    self.ui.dock_people_info.recheck()
                #############################
                # check result
                # ---------------------------
                if ret:
                    if not ui.chkLFio.isChecked():    ui.comboFIO.setCurrentText("")
                    if not ui.chkLServ.isChecked():   ui.comboServ.setCurrentText("")
                    if not ui.chkLW.isChecked():      ui.comboW.setCurrentText("")
                    if not ui.chkLAmount.isChecked(): ui.qleAmount.setValue(0)
                    ui.qleNote.setText("")
                # cProfile.run('self.ins_main('+qry_data+')' )
                self.set_qle_serv_left()
                if return_focus_to:
                    return_focus_to.setFocus()

    @Slot()
    def on_btn_serv_bydayW_clicked(self):
        self.pre_ins_main(self.ui.comboW)

    @Slot()
    def on_btn_serv_bydayE_clicked(self):
        self.pre_ins_main(self.ui.comboServ)

    @Slot()
    def on_btn_serv_bydayA_clicked(self):
        self.pre_ins_main(self.ui.qleAmount)

    @Slot()
    def on_btn_serv_bydayQ_clicked(self):
        self.pre_ins_main(self.ui.comboFIO)

    @Slot(bool)
    def on_pb_start_serv_add_clicked(self, b_state):
        btn: QPushButton() = self.ui.pb_start_serv_add
        lbl: QLabel = self.ui.lbl_input_serv
        if b_state:
            btn.setText(self.tr("ВВОД УСЛУГ"))
            lbl.setText(self.tr("Введено:"))
        else:
            btn.setText(self.tr("НАЧАТЬ ВВОД УСЛУГ"))
            lbl.setText(self.tr("Будет введено:"))

    @Slot()
    def on_btn_goto_worker_clicked(self):
        ui = self.ui
        tabs: myQTabWidget = ui.tabMain
        tabs.set_active_tab_by_name("tab_admin")
        tabs_adm: myQTabWidget = ui.tabs_admin
        tabs_adm.set_active_tab_by_name("tab_workers")

    @Slot()
    def on_btn_goto_client_clicked(self):
        ui = self.ui
        tabs: myQTabWidget = ui.tabMain
        cbxs: myQComboBox = ui.cbx_1__dep_has_client__2
        uid = cbxs.current_id()
        if uid:
            tabs.set_active_tab_by_name("tab_clients")
            cbxs: myQComboBox = ui.cbx_1__dep_has_client
            cbxs.set_current_index_id(uid)


class clstab_table_serv(QOBase):

    def __init__(self, parent=None):
        super().__init__(parent)
        self.__init = False
        self.ui = self.parent().ui
        ui = self.ui
        table: tsQTableViewYear = ui.tableViewYear
        self.table = table
        self.model = tsTableServYearModel(table)
        self.table_last_index = None
        table.setItemDelegate(tsItemDelegate(table))
        table.setModel(self.model)
        # self.table_sel_model = table.selectionModel()
        self.table._selectionChanged.connect(self.update_last_select_cell)
        self.cbx_contracts: myQComboBox = ui.cbx_1_contracts__by_client_id__2
        self.cbx_contracts.set_val_after_filter = 1

    @Slot(QItemSelection, QItemSelection)
    def update_last_select_cell(self, this, prev):
        debug(this)

    @Slot(bool)
    def on_tab_clients_widgetVisibilityChanged(self, state):
        self._init()

    def _init(self):
        if (not self.__init) and SD._dbconnected:
            ui = self.ui
            self.__init = True
            #############################
            # get inited model
            # ---------------------------
            cbx: myQComboBox = self.cbx_contracts
            cbx.init_model()  # just to be sure
            cbx.set_val_after_filter = 1
            mdl: tsSqlTableModel = cbx.model().super_model()
            if not mdl.meta_init:
                self.__init = False
                return
            dm: tsQDataWidgetMapper = cbx.dm
            self.dm_set.add(dm)
            #############################
            # set tsQDataWidgetMapper
            # ---------------------------
            dm.addMapping(ui.de_contracts, mdl.record().indexOf("check_date"))

    @Slot()
    def on_btn_add_worker_clicked(self):
        ui = self.ui
        #############################
        # get month
        # ---------------------------
        month0 = dt.now().month - 1
        try:
            selection: QItemSelectionModel = self.table.selectionModel()
            month0 = self.model.get_month(selection.currentIndex().column()) - 1
        except:
            pass
        if month0 is False:
            month0 = dt.now().month - 1
        #############################
        # get workers list (without existing workers)
        # ---------------------------
        dhw_workers = {}
        mdl = WD.models("_dep_has_worker", "_dep_has_worker")
        # mdl.select()
        worker_exist_list = self.model.workers_in_month(month0)
        for i in range(mdl.rowCount0()):
            wid = mdl.data(mdl.index(i, 0), Qt.EditRole)
            if wid not in worker_exist_list:
                dhw_workers[wid] = (mdl.data(mdl.index(i, 1), Qt.EditRole))
        #############################
        # select worker in inputDialog
        # ---------------------------
        w_name, ok = QInputDialog.getItem(self.ui, "",
                                          "Выберите работника для добавления в месяце № " + str(month0 + 1),
                                          list(dhw_workers.values()), 0, False)
        if ok:
            for d, val in dhw_workers.items():
                if w_name == val:
                    worker_id = d
                    self.model.add_worker(worker_id, month0)
                    return

    @Slot()
    def on_btn_goto_client_2_clicked(self):
        ui = self.ui
        tabs: myQTabWidget = ui.tabMain
        cbxs: myQComboBox = ui.cbx_1__dep_has_client__4
        client_id = cbxs.current_id()
        if client_id:
            tabs.set_active_tab_by_name("tab_clients")
            cbxs: myQComboBox = ui.cbx_1__dep_has_client
            cbxs.set_current_index_id(client_id)
            cbxs_contr: myQComboBox = self.cbx_contracts
            contracts_id = cbxs_contr.current_id()
            if contracts_id:
                tabs.set_active_tab_by_name("tab_client_contr")
                cbxs_contr: myQComboBox = ui.cbx_1_contracts__by_client_id
                cbxs_contr.set_current_index_id(contracts_id)

    @Slot(int)
    def on_cbx_1__dep_has_client__4_currentIndexChanged(self, ind):
        ui = self.ui
        uid = ui.cbx_1__dep_has_client__4.current_id()
        if uid and uid != SD.last_client:
            SD.set_last_client(uid)


class clstab_total(QOBase):
    """
    Total tab for various statistic
    """

    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = self.parent().ui
        self.tab_serv_you = clstab_serv_you(self)
        self.tab_tot_group = clstab_tot_group(self)


class clstab_journal(QOBase):
    """
    journal tab
    """

    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = self.parent().ui
        self.table = self.ui.journal_table
        self.journal_model = JournalModel()
        self.table.setModel(self.journal_model)


class clstab_tot_group(QOBase):
    """
    Total tab of dep services grouped
    """

    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = self.parent().ui
        ui = self.ui
        # self.period: qcSelectPeriod = ui.qcQSelectPeriod_tot_group

    # @Slot()
    # def on_btn_tot_group_dep_clicked(self):
    #     """
    #     Set period for table__worker_has_main__where_vdate
    #     """
    #     ui = self.ui
    #     table: myQTableView = ui.t_sql__g_serv_total_dep__where_vdate
    #     model: tsSqlTableModel = table.super_model()
    #     tsql, _, _ = model.objectName().partition("__")
    #     sql = WD.sql_query[tsql].format(*self.period.date_period_as_str(SQL_DATE_FORMAT))
    #     qry = QSqlQuery(SD.get_db)
    #     qry.exec_(sql)
    #     qry.next()
    #     model.setQuery(qry)
    #     # model.setFilter("start_vdate between '%s' and '%s' " % period)
    #     model.select()


class clstab_services_import(QOBase):
    """
    Import services from file ( which is exported in mobile client)
    """

    def __init__(self, parent=None):
        super().__init__(parent)
        self.import_model = ImportJsonModel()
        self.import_table: myQTableView = self.ui.import_table
        __init = False

    @Slot()
    def on_btn_import_services_clicked(self):
        ui = self.ui
        if not self.import_table.model():
            self.import_table.setModel(self.import_model)
        self.import_model.import_services_from_files()
        self.import_model.update_view()
        # update_view

    @Slot(bool)
    def on_tab_services_import_widgetVisibilityChanged(self, state):
        self._init()
        self.import_table.setModel(self.import_model)
        # self.import_model = ImportJsonModel()

    @Slot()
    def on_btn_import_clear_clicked(self):
        self.import_model.json_import = []
        self.import_model.update_view()

    @Slot()
    def on_btn_import_to_dbms_clicked(self):
        imain = WD.models("api_key_insert_main")
        # dhw = WD.models("dep_has_worker")
        # contracts_model = WD.models("contracts")
        for service in self.import_model.json_import:
            if service["IN"] == "New":
                rec = {
                    "contracts_id": service["contractId"],
                    # "dep_id": dhw.data_by_id(service["workerId"], dhw.index_of_col("dep_id")),
                    "serv_id": service["servId"],
                    "vdate": service["provDate"],
                    "dep_has_worker_id": service["workerId"],
                    # "note": service["uid"],
                    "uuid": service["uid"],
                    "check_api_key": service["api_key"],
                    "quantity": 1,
                    # "client_id":
                    #     contracts_model.data_by_id(service["contractId"], contracts_model.index_of_col("client_id"))
                }
                SD.start_edit(None, imain, imain.row_id(imain.special_row), "client_id")
                ce = imain.insert_row(rec)
                if ce.save():
                    service["IN"] = "Exist"

    def _init(self):
        if (not self.__init) and SD._dbconnected:
            ui = self.ui
            self.__init = True


class clstab_serv_you(QOBase):
    """
    Total tab of your services not grouped
    """
    pass
