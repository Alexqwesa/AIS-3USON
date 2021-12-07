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
# setup logger
# ---------------------------
# import pypyodbc as pypyodbc
# import asyncio
# from threading import Thread

import typing
from contextlib import suppress

from qtpy.QtWidgets import QInputDialog, QStyleFactory, QMainWindow
import qtawesome as qta

# logging.getLogger("3uson").setLevel(logging.DEBUG)
# logging.getLogger("3uson").setLevel(logging.INFO)


from typing import NoReturn

#############################
# QT Libraries
# ---------------------------
from qtpy import QtGui

#############################
# import this project files
# ---------------------------
from tab_classes import *
from fill_templates import PrepareDocument

#############################
# CONSTANTS
# ---------------------------
# VERSION = 2
import platform
import subprocess
#############################
# For money
# ---------------------------
import decimal

decimal.getcontext().prec = 2
#############################
# detect autogenerated files
# ---------------------------
modules = list(sys.modules.keys())  # TODO: filter
if "PyQt5" in modules:
    debug("loading PyQt5")
    UI.qtpy = "pyqt5"
elif "PySide2" in modules:
    debug("loading PySide2")
    UI.qtpy = "pyside2"
else:
    debug("Qt not found: %s ", modules)
#############################
# update autogenerated files (currently, only check time of main_window.ui)
# ---------------------------
# TODO: on fail use dynamic loading
if not getattr(sys, "frozen", False):
    uifile = os.path.getmtime(os.path.join(PROJECT_DIR, "widgets_ui", "main_window.ui"))
    pyfile = 0
    with suppress(FileNotFoundError):
        pyfile = os.path.getmtime(
            os.path.join(PROJECT_DIR, "widgets_ui", "autogenerated", "main_window_" + UI.qtpy + ".py"))
    if uifile > pyfile:
        if platform.system() == "Linux":
            os.chdir(os.path.join(PROJECT_DIR, "tools"))
            subprocess.run(os.path.join(PROJECT_DIR, "tools", "uic.sh"),
                           shell=True, stdin=None, stdout=None, stderr=None, close_fds=True)
        elif platform.system() == "Windows":
            os.chdir(os.path.join(PROJECT_DIR, "tools"))
            subprocess.run(os.path.join(PROJECT_DIR, "tools", "uic.bat"), shell=True)
        else:
            warning(" Your platform is not officially supported yet")

#############################
# load autogenerated files
# ---------------------------
if UI.qtpy == "pyqt5":
    from widgets_ui.autogenerated.main_window_pyqt5 import Ui_MainWindow
elif UI.qtpy == "pyside2":
    from widgets_ui.autogenerated.main_window_pyside2 import Ui_MainWindow


class decorate_events_with_try(QObject):
    def eventFilter(self, qobj, event):
        try:
            # return super().eventFilter(qobj, event)
            QApplication.instance().sendEvent(qobj, event)
            # QApplication.instance().postEvent(qobj, event)
            return True
        except:
            pass


class allEventFilter(QObject):
    def __init__(self, parent):
        super().__init__(parent)

    def eventFilter(self, qobj, event):
        try:
            ui = self.parent().ui
        except AttributeError:
            critical("allEventFilter self.parent().ui ")
            return True
        if event.type() == QEvent.MouseButtonRelease:
            if qobj is ui.menu_settings:
                if isinstance(qobj, QtWidgets.QMenu):
                    if qobj.activeAction():
                        qa_name = qobj.activeAction().objectName()
                        if qa_name == "qaFontSmaller" or qa_name == "qaFontBigger":
                            qobj.activeAction().trigger()
                            return True
        return super().eventFilter(qobj, event)


class MyAppConnect(QMainWindow):
    def __init__(self, parent=None):
        # QtWidgets.QMainWindow.__init__(self)
        # self.loop = asyncio.get_event_loop()
        super().__init__(parent)
        #############################
        # decorate_events_with_try
        # ---------------------------
        # self.all_events = decorate_events_with_try(self)
        # QCoreApplication.instance().installEventFilter(self.all_events)
        #############################
        # init vars
        # ---------------------------
        self._dirty = False
        self.data = TsonData(self)
        self.data.setObjectName("main_data")
        # self.config = self.data.config
        self.login_done = False
        # self.tablesRTModel = {}
        # self.tableList = {}
        # self.cbxRTModel = {}
        # self.cbxList = {}
        #############################
        # load QSettins
        # ---------------------------
        self.font_size = self.font().pointSize()
        self.readQSetting()
        #############################
        # loading UI files
        # ---------------------------
        # self.ui_init_task = asyncio.create_task(self.ui_init())
        # self.ui_init_task = self.loop.create_task(self.ui_init())
        # self.ui_init_task =self.loop.call_soon(self.ui_init)
        # self.ui_init_task = Thread(None, self.ui_init, "thd-1")  # , args=(thed[i],)
        self.ui_init()
        # self.ui_init_task.start()
        #############################
        # login_dialog init
        # ---------------------------
        self.dlg_name = "login_dialog.ui"
        ui_module = importlib.import_module(
            "widgets_ui.autogenerated." + self.dlg_name.replace(".ui", "") + "_" + UI.qtpy)

        class MW(QtWidgets.QDialog, ui_module.Ui_loginDialog):
            def __init__(self, iparent=None):
                super().__init__(iparent)
                self.setupUi(self)

        self.dlg: ui_module.Ui_loginDialog = MW()
        # self.dlg = uic.loadUi(os.path.join(PROJECT_DIR, "widgets_ui", "login_dialog.ui"))
        dlg = self.dlg
        dlg.user.setText(SD.user)
        dlg.password.setText(SD.password)
        dlg.server.setText(SD.server)
        dlg.sp_port.setValue(int(SD.port))
        dlg.pt_driver.setPlainText(SD.driver)
        dlg.sp_dep.setValue(int(SD.last_dep))
        #############################
        # ui setups
        # ---------------------------
        # self.FontG = QtWidgets.QActionGroup(self)
        # fg = self.FontG
        UI.main_window = self
        #############################
        # connect signals and slots
        # ---------------------------
        self.make_connections()

    def ui_init(self):
        class MW(QWidget, Ui_MainWindow):
            def __init__(self, parent=None):
                super().__init__(parent)
                self.setupUi(parent)

            def __getattr__(self, item):
                return self.parent().__getattribute__(item)

            def findChildren(self, arg__1: type, arg__2: QRegExp) -> typing.Iterable:
                return self.parent().findChildren(arg__1, arg__2)

            def findChild(self, arg__1: type, arg__2: QRegExp) -> typing.Iterable:
                return self.parent().findChild(arg__1, arg__2)

        # self.ui: Ui_MainWindow = uic.loadUi(os.path.join(PROJECT_DIR, "widgets_ui", "main_window.ui"), self)
        self.ui: Ui_MainWindow = MW(self)
        self.ui.action_year.setText(self.tr("Год: ") + str(SD.last_year))
        #############################
        # ui setups
        # ---------------------------
        self.tab_debug = clstab_debug(self)
        self.tab_services = clstab_services(self)
        self.tab_client = clstab_client(self)
        self.tab_fio_dep = clstab_fio_dep(self)
        self.tab_client_contr = clstab_client_contr(self)
        self.tab_ufio = clstab_ufio(self)
        self.tab_total = clstab_total(self)
        self.tab_admin_1 = clstab_admin(self)
        self.tab_journal = clstab_journal(self)
        self.tab_table_serv1 = clstab_table_serv(self)
        self.tab_dock_people_info = clstab_dock_people_info(self)

        self.ui.action_year.setText(self.tr("Год: ") + str(SD.last_year))
        #############################
        # setup Icons TODO: add resources
        # ---------------------------
        ui = self.ui
        undo_icon = qta.icon('fa5s.undo')
        redo_icon = qta.icon('fa5s.redo')
        qa_dock_people_info_icon = qta.icon('mdi.information-outline')
        people_profile = qta.icon('ei.address-book')
        worker_list = qta.icon('mdi.account')
        ui.btn_goto_ufio.setIcon(people_profile)
        ui.btn_goto_worker.setIcon(worker_list)
        ui.qa_dock_people_info.setIcon(qa_dock_people_info_icon)
        ui.action_undo.setIcon(
            QtGui.QIcon.fromTheme("edit-undo", undo_icon))
        # self.style().standardIcon(QtWidgets.QStyle.SP_ArrowBack)))
        ui.action_redo.setIcon(
            QtGui.QIcon.fromTheme("edit-redo", redo_icon))
        # self.style().standardIcon(QtWidgets.QStyle.SP_ArrowRight)))
        ui.action_discard.setIcon(
            QtGui.QIcon.fromTheme("document-revert",
                                  self.style().standardIcon(QtWidgets.QStyle.SP_DialogDiscardButton)))
        ui.action_save.setIcon(
            QtGui.QIcon.fromTheme("document-save",
                                  self.style().standardIcon(QtWidgets.QStyle.SP_DialogSaveButton)))
        #############################
        # action default state
        # ---------------------------
        ui.action_undo.setEnabled(False)
        ui.action_redo.setEnabled(False)
        ui.action_discard.setEnabled(False)
        ui.action_save.setEnabled(False)
        #############################
        # hide unfinished tabs
        # ---------------------------
        # ui.tabMain.removeTab(ui.tabMain.indexOf(ui.tab_journal))
        ui.tabMain.removeTab(ui.tabMain.indexOf(ui.tab_pyc))
        ui.tabMain.removeTab(ui.tabMain.indexOf(ui.tab_export))
        # ui.tabMain.removeTab(ui.tabMain.indexOf(ui.tab_admin))

        #############################
        # connect signals and slots
        # ---------------------------
        # QMetaObject.connectSlotsByName(self)
        self.ef = allEventFilter(self)
        ui.menu_settings.installEventFilter(self.ef)

    def isDirty(self):
        return self._dirty

    @Slot(bool)
    def setDirty(self, dirty=True):
        self._dirty = dirty
        ui = self.ui
        ui.action_discard.setEnabled(dirty)
        ui.action_save.setEnabled(dirty)
        # TODO:activate edit options here

    @Slot()
    def check_login(self):
        """ show main window (to call from login dialog)
        """
        SD.set_user(self.dlg.user.text())
        SD.set_password(self.dlg.password.text())
        SD.set_server(self.dlg.server.text())
        SD.set_port(self.dlg.sp_port.value())
        SD.set_driver(self.dlg.pt_driver.toPlainText())
        if self.main_dbconnect(dep=self.dlg.sp_dep.value()):
            self.login_done = True
            self.show()
            SD.save_conf()
        else:
            self.dlg.show()
            status: QPlainTextEdit = self.dlg.status
            if self.data.db:
                status.appendPlainText(self.data.db.lastError().text().strip())
            else:
                status.appendPlainText("no DB")

    def show(self):
        debug("show window")
        # d=self.data
        # if d.password and d.user :
        #     return self.check_login()
        if self.login_done:
            # self.ui_init_task.add_done_callback(super().show)
            # self.ui_init_task.join()
            self.set_department(SD.last_dep)
            return super().show()
            # return True
        else:
            return self.check_login()

    def make_connections(self) -> NoReturn:
        dlg = self.dlg
        dlg.btnEnter.accepted.connect(self.check_login)
        dlg.btnEnter.rejected.connect(self.close)
        SD.setDirty_changed.connect(self.setDirty)
        SD.journal.journal_changed.connect(self.journal_changed)
        # self.ui.action_undo.triggered.connect(SD.journal.undo)
        # self.ui.action_redo.triggered.connect(SD.journal.redo)
        # self.ui.action_save.triggered.connect(SD.journal.save)
        # self.ui.action_discard.triggered.connect(SD.journal.discard)

    @Slot()
    def journal_changed(self):
        """
        """
        ui = self.ui
        #############################
        # action default state
        # ---------------------------
        ui.action_undo.setEnabled(SD.journal.undo_available)
        ui.action_redo.setEnabled(SD.journal.redo_available)
        ui.action_discard.setEnabled(SD.journal.discard_available)
        ui.action_save.setEnabled(SD.journal.save_available)
        if SD.journal.save_available:  # needed?
            pass
        else:
            self.setDirty(False)

    @Slot()
    def main_dbconnect(self, dep=0):
        """connect to DB"""
        db = SD.get_db
        if db:
            SD.set_last_dep(dep)  # actual connection happens here
            self.data.db = db
            return True
        else:
            return False

    def notifiesToUsers(self):
        debug("notifiesToUsers")
        for nf in self.data.getNotifies():
            QMessageBox.information(self.parent(),
                                    self.tr("Сообщение от Администратора"), nf)

    def set_department(self, dep):
        #############################
        # required set_last_dep - cur dep
        # ---------------------------
        if dep != SD.last_dep:
            return SD.set_last_dep(dep)  # update SQL DB privileges and current dep
            self.reselect_all_models()
        #############################
        # show cur dep
        # ---------------------------
        depmdl = WD.models("dep")
        self.ui.action_curDep.setText(self.tr("Отделение: ") + depmdl.data_by_id(SD.last_dep, 1))
        self.ui.action_connected_user.setText(self.tr("Пользователь: ") + SD.user)
        SD.line_query("set role all")
        self.ui.action_connected_user.setToolTip(self.tr(
            "Вы работаете под этой учетной записью, права доступа: {}".format(SD.line_query("select CURRENT_ROLE()"))
        ))
        #############################
        # notifiesToUsers
        # ---------------------------
        # self.findTablesAndCreateModels()
        # self.findQcboxAndCreateModels()
        self.notifiesToUsers()
        # self.createUnAssignedModels()

    def readQSetting(self):
        #############################
        # set Font of app from config
        # ---------------------------
        try:
            qset = SD.qsettings
            qfont: QFont = self.font()
            qfont.setPointSize(int(qset.value("font_size", 11)))
            QtWidgets.QApplication.instance().setFont(qfont)
            self.restoreGeometry(qset.value("mw/geometry"))
            self.restoreState(qset.value("mw/windowState"))
            # qset.setValue("geometry", self.saveGeometry())
            # qset.setValue("windowState", self.saveState())
        except:
            warning("settings loading failed")


class MyAppMenu(MyAppConnect):

    @Slot()
    def on_action_QT_triggered(self):
        QMessageBox.aboutQt(self)

    @Slot()
    def on_qa_about_triggered(self):
        QMessageBox.information(self, self.tr("О программе АИС ТриУСОН"), self.tr("""
            АИС ТриУСОН 
            
Автоматизированная Информационная Система Учета Услуг Учреждений Социального Обслуживания Населения
            
        Система разработана в 2019-2020г.
        Разработчик - Савин Александр Викторович
        Лицензия - LGPL 3
                                """))

    @Slot()
    def on_action_update_tables_triggered(self):
        """
        """
        for mdl in list(WD.inited_models.values()):
            mdl.select()
            debug("updated model %s ", mdl.objectName())
        debug("models updated")

    @Slot()
    def on_action_update_tables_on_tab_triggered(self):
        """
        """
        self.on_action_update_tables_triggered()

    @Slot()
    def on_qa_close_app_triggered(self):
        QCoreApplication.instance().quit()

    @Slot()
    def on_qa_load_all_models_triggered(self):
        all_models = ['dep', '_dep_has_ufio', 'contracts', 'stub_model', '_contr_has_serv',
                      '_ufio_has_add_info',
                      'ufio_has_category', 'ufio', '_dep_has_ufio_by_ripso', 'dep_has_worker', 'worker', 'ripso',
                      '_g_categ_list_ufio_for_dep_for_year', 'ui_select_fiolist', '_serv_activ', '_dep_has_main',
                      'user_has_serv', 'serv', 'ripso_has_serv', 'dep_has_ripso', 'setting', 'notifies', 'holiday']
        for m in all_models:
            _ = WD.models(m)

    @Slot()
    def on_qa_menu_pd_triggered(self):
        # PrepareDocument.print_ps_agreement()
        PrepareDocument.print_doc(SD.last_ufio, QDate.currentDate().month(), SD.last_year, SD.last_dep,
                                  str(SD.last_contr),
                                  "соглашениеПД", QDate.currentDate())

    @Slot()
    def on_qa_act_triggered(self):
        month, ok = QInputDialog.getInt(self, "", self.tr(f"Выберите месяц {SD.last_year} года"),
                                        QDate.currentDate().month(), 1, 12, 1)
        if ok:
            PrepareDocument.print_doc(SD.last_ufio, month, SD.last_year, SD.last_dep, "__all__", "акт")

    @Slot()
    def on_qa_invoice_triggered(self):
        month, ok = QInputDialog.getInt(self, "", self.tr(f"Выберите месяц {SD.last_year} года"),
                                        QDate.currentDate().month(), 1, 12, 1)
        if ok:
            PrepareDocument.print_doc(SD.last_ufio, month, SD.last_year, SD.last_dep, "__all__", "квитанция")

    @Slot()
    def on_qa_contract_triggered(self):
        if SD.last_contr:
            PrepareDocument.print_doc(SD.last_ufio, 13, SD.last_year, SD.last_dep, str(SD.last_contr), "договор")
        else:
            QMessageBox.warning(UI.main_window,
                                self.tr("Не выбран договор!"),
                                self.tr("Выберите договор!"),
                                QMessageBox.StandardButton.Ok, QMessageBox.StandardButton.NoButton)

    @Slot()
    def on_qa_predv_contract_triggered(self):
        if SD.last_contr:
            PrepareDocument.print_doc(SD.last_ufio, 13, SD.last_year, SD.last_dep, str(SD.last_contr),
                                      "предварительный расчет оплаты")
        else:
            QMessageBox.warning(UI.main_window,
                                self.tr("Не выбран договор!"),
                                self.tr("Выберите договор!"),
                                QMessageBox.StandardButton.Ok, QMessageBox.StandardButton.NoButton)

    @Slot()
    def on_qa_request_triggered(self):
        PrepareDocument.print_doc(SD.last_ufio, 13, SD.last_year, SD.last_dep, str(SD.last_contr), "заявление",
                                  QDate.currentDate())

    @Slot()
    def on_qa_style_triggered(self):
        items = {}
        for k in QStyleFactory.keys():
            items[k] = k
        style, ok = QInputDialog.getItem(self, "", "Выберите стиль", list(items.values()), 0, False)
        if ok:
            qstyle = QStyleFactory.create(style)
            QApplication.setStyle(qstyle)
            QApplication.setPalette(qstyle.standardPalette())

    def reselect_all_models(self):
        return WD.reinit_models()

    @Slot()
    def on_qa_new_people_triggered(self):
        ui = self.ui
        tab = ui.tabMain.set_active_tab_by_name("tab_client")
        tab.findChild(myQTabWidget).set_active_tab_by_name("tab_people_main")
        cbox: myQComboBox = ui.cbx_1__dep_has_ufio
        # new_row = cbox.super_model().special_row
        # new_ind = cbox.super_model().index(new_row, 0)
        # flt: tsQsfpModel
        # for flt in reversed(cbox.filters):
        #     new_ind = flt.mapFromSource(new_ind)
        # cbox.setCurrentIndex(new_ind.row())
        cbox.setCurrentIndex(0)

    @Slot()
    def on_qa_tab_people_of_dep_triggered(self):
        ui = self.ui
        tab = ui.tabMain.set_active_tab_by_name("tab_fio_dep")
        tab.findChild(myQTabWidget).set_active_tab_by_name("tab_people_of_dep")

    @Slot()
    def on_qa_tab__dep_has_ufio_more_triggered(self):
        ui = self.ui
        tab = ui.tabMain.set_active_tab_by_name("tab_fio_dep")
        tab.findChild(myQTabWidget).set_active_tab_by_name("tab__dep_has_ufio_more")

    @Slot()
    def on_qa_tab_journal_triggered(self):
        ui = self.ui
        tab = ui.tabMain.set_active_tab_by_name("tab_journal")

    @Slot()
    def on_qa_tab_workers_triggered(self):
        ui = self.ui
        tab = ui.tabMain.set_active_tab_by_name("tab_admin")
        tab.findChild(myQTabWidget).set_active_tab_by_name("tab_workers")

    @Slot()
    def on_qa_tab_serv_you_triggered(self):
        ui = self.ui
        tab = ui.tabMain.set_active_tab_by_name("tab_total")
        tab = tab.findChild(myQTabWidget).set_active_tab_by_name("tab_tot_serv")
        tab.findChild(myQTabWidget).set_active_tab_by_name("tab_serv_you")

    @Slot()
    def on_qa_tab_dep_triggered(self):
        ui = self.ui
        tab = ui.tabMain.set_active_tab_by_name("tab_admin")
        tab.findChild(myQTabWidget).set_active_tab_by_name("tab_dep")

    @Slot()
    def on_qa_tab_add_serv_by_day_triggered(self):
        ui = self.ui
        tab = ui.tabMain.set_active_tab_by_name("tab_add_serv")
        tab.findChild(myQTabWidget).set_active_tab_by_name("tab_add_serv_by_day")

    @Slot()
    def on_qa_dirty_tab_unblocked_triggered(self):
        chk: QCheckBox = self.ui.qa_dirty_tab_unblocked
        SD.setDirty(SD.unsaved)

    @Slot()
    def on_qa_drop_qsettings_triggered(self):
        ui = self.ui
        qset = SD.qsettings
        qset.clear()
        qset.sync()
        self.readQSetting()

    @Slot()
    def on_qa_show_settings_triggered(self):
        ui = self.ui
        text = SD.dump_configs()
        debug(text)
        QMessageBox.information(self,
                                self.tr("Текущие настройки"), text)

    def set_current_font(self, fsize):
        qfont: QFont = self.font()
        fsize = qfont.pointSize() + fsize
        if fsize > 4:
            SD.qsettings.setValue("font_size", fsize)
            qfont.setPointSize(fsize)
            QtWidgets.QApplication.instance().setFont(qfont)

    @Slot()
    def on_qaFontSmaller_triggered(self):
        self.set_current_font(-1)
        # self.ui.qaFontSmaller.setChecked(False)

    @Slot()
    def on_qaFontBigger_triggered(self):
        self.set_current_font(+1)
        # self.ui.qaFontBigger.setChecked(False)

    @Slot()
    def on_qa_add_ufio_triggered(self):
        pass

    @Slot()
    def on_qa_add_contract_triggered(self):
        pass

    @Slot()
    def on_qa_goto_password_triggered(self):
        ui = self.ui
        tab = ui.tabMain.set_active_tab_by_name("tab_admin")
        if tab:
            _ = tab.findChild(myQTabWidget).set_active_tab_by_name("tab_password")

    @Slot()
    def on_qa_goto_back_tab_triggered(self):
        return UI.go_back_to_tab()

    @Slot()
    def on_qa_goto_forward_tab_triggered(self):
        return UI.go_back_to_tab(1)

    @Slot(bool)
    def on_qaDBDisconnect_triggered(self, val):
        SD.disconnect()

    @Slot(bool)
    def on_action_connected_user_triggered(self, val):
        wrkmdl = WD.models("worker")
        worker = wrkmdl.data_by_id(SD.line_query("select get_WID()"), 1)
        QMessageBox.information(self,
                                self.tr("Текущие пользователь"), worker)

    @Slot(bool)
    def on_qaDBconnect_triggered(self, val):
        SD.disconnect()
        self.hide()
        self.login_done = False
        dlg = self.dlg
        dlg.user.setText(SD.user)
        dlg.password.setText("")
        dlg.show()

    @Slot(bool)
    def on_qaDBReconnect_triggered(self, val):
        SD.reconnect()
        # if self.main_dbconnect():
        #     return True
        # else:
        #     self.on_qaDBconnect_triggered()
        # SD.connect()


class MyApp(MyAppMenu):  # , Ui_MainWindow
    EXIT_CODE_REBOOT = -123456789

    @Slot()
    @force_reloader
    @try_wrapper
    def on_my_test_action_triggered(self):
        function_replacer("main_pyqt_frontend", "MyApp", "test_worker")
        self.test_worker()
        # SD.journal.undo_available

    def test_worker(self):
        pass
        # function_replacer("widgets.custumQWidgets", "myQCalendar", "set_flt_ufio")
        # function_replacer("widgets.custumQWidgets", "myQCalendar", "add_new_date")
        function_replacer("widgets.custumQWidgets", "myQCalendar", "paintCell")
        function_replacer("models.ts_models", "clstab_client_contr", "on_cbx_1__dep_has_ufio_currentIndexChanged")
        function_replacer("main_pyqt_frontend", "myApp", "on_action_curDep_triggered")
        # function_replacer("widgets.custumQWidgets", "tsQsfpModel_no_new", "filterAcceptsRow")
        # res, ok = QInputDialog.getText(self, "", self.tr("Введите имя виджет"), QLineEdit.Normal,
        #                                "cldr_date_serv_insert")
        # if ok:
        #     debug("on_my_test_action_triggered")
        #     widget_replacer(res)
        #     # self.tab_client._init()

    #############################
    # Inner state
    # ---------------------------

    #############################
    # toolBar and menu
    # ---------------------------

    @Slot()
    def on_action_discard_triggered(self):
        """discard all tables in active tab
        """
        debug("on_discard_save_triggered")
        SD.journal.discard()
        # for mdl in SD.unsaved_model:
        #     mdl.revertAll()
        # if self.isDirty():
        #     for key, obj in self.tableList.items():
        #         try:
        #             if obj.isDirty():
        #                 name = key[6:]
        #                 WD.models(name).select()
        #                 WD.models(name).setDirty.emit(False)
        #                 debug("discard %s ", key)
        #         except:
        #             pass

    @Slot()
    def on_action_save_triggered(self):
        """save all tables in active tab
        """
        debug("on_action_save_triggered")
        SD.journal.save()
        # for mdl in SD.unsaved_model[:]:
        #     mdl.submitAll()

    @Slot()
    def on_qa_dock_people_info_triggered(self):
        w: QDockWidget = self.ui.dock_people_info
        chk: QCheckBox = self.ui.qa_dock_people_info
        w.setVisible(chk.isChecked())

    @Slot()
    def on_action_undo_triggered(self):
        SD.journal.undo()
        self.journal_changed()

    @Slot()
    def on_action_redo_triggered(self):
        SD.journal.redo()
        self.journal_changed()

    @Slot(bool)
    def on_dock_people_info_visibilityChanged(self, visible: bool):
        chk: QCheckBox = self.ui.qa_dock_people_info
        chk.setChecked(visible)

    @Slot()
    def on_action_curDep_triggered(self):
        ui = self.ui
        mdl = WD.models("_worker_has_dep")
        rc = mdl.rowCount0()
        if rc == 0:
            error("Не назначен отдел!")
            ui.statusBar().showMessage(self.tr("Ошибка - Нельзя сменить отделение "))
        elif rc == 1:
            # qry.first()
            ui.statusBar().showMessage(self.tr("Нельзя сменить отделение - Вам доступно лишь одно отделение"))
            # self.setDep(qry.value(index))
        else:
            items = {}
            dep_id = SD.last_dep
            # assume there is no duplicates
            for i in range(mdl.rowCount0()):
                items[mdl.data(mdl.index(i, 0), Qt.EditRole)] = (mdl.data(mdl.index(i, 1), Qt.EditRole))
            dep_name, ok = QInputDialog.getItem(self, "", "Выберите отделение", list(items.values()), 0, False)
            if ok:
                for d, val in items.items():
                    if dep_name == val:
                        dep_id = d
                #############################
                # set_department
                # ---------------------------
                self.set_department(dep_id)
                debug("new department - %s ", dep_name)

    @Slot()
    def on_action_year_triggered(self):
        ly = SD.last_year
        res, ok = QInputDialog.getInt(self, "", "Выберите год", SD.last_year, 2000, 2050, 1)
        SD.set_last_year(res)
        self.ui.action_year.setText(self.tr("Год: ") + str(SD.last_year))
        if res != ly:
            self.reselect_all_models()
            debug("new year - %s ", SD.last_year)

    @Slot()
    def setYear(self, year: int):
        """
        """
        ui = self.ui

    def on_btn_upd_fio_list(self):
        ui = self.ui
        mdl = ui.table__dep_has_ufio__by_ufio.model()
        if isinstance(mdl, tsQsfpModel):
            mdl.setFilterFixedString("")
        mdl.super_model().select()
        # TODO: reset filters
        # resetModel(mdl)

    # def findQcboxAndCreateModels(self):
    #     """init QComboBoxes"""
    #     #############################
    #     # init tables ui
    #     # ---------------------------
    #     debug("====init QComboBoxes====")
    #     ui = self.ui
    #     d = self.data
    #     cList = self.cbxList
    #     coldict = {}
    #     for cbx in self.findChildren(QtWidgets.QComboBox):  # why QTableView didn't work
    #         name = cbx.objectName()
    #         if "cbx_" == name[:4]:
    #             if name[5] == "_":
    #                 coldict[cbx.objectName()] = int(name[4])
    #                 cList[cbx.objectName()] = cbx
    #     if self.cbxRTModel is None:
    #         self.cbxRTModel = []
    #     cbxRTModel = self.cbxRTModel
    #     debug(cList)
    #     # logging.getLogger(__name__).setLevel(logging.INFO)
    #     info("ui QComboBox widgets: %s", cList.keys())
    #     thd = []
    #     models = []
    #     for i, (wname, cbx) in enumerate(cList.items()):
    #         tname = wname[6:]
    #         cbxRTModel[wname] = cbx
    #         if tname not in WD.models:
    #             models.append(tsSqlTableModel(tname, self.data, self.data.db))
    #         else:
    #             models.append(WD.models(tname))
    #         cbx.setModel(models[i])
    #         thd.append(threading.Thread(target=self.run_add_module, args=(tname, cbx, models[i])))
    #         thd[i].start()
    #     for i, (wname, cbx) in enumerate(cList.items()):
    #         thd[i].join()
    #         cbx.setModelColumn(coldict[wname])
    #     # logging.getLogger(__name__).setLevel(logging.DEBUG)
    #     debug(cbxRTModel.items())
    #
    # def findTablesAndCreateModels(self):
    #     """init tables"""
    #     #############################
    #     # init tables ui
    #     # ---------------------------
    #     ui = self.ui
    #     tList = self.tableList
    #     for tbl in self.findChildren(QtWidgets.QTableView):  # why QTableView didn't work
    #         name = tbl.objectName()
    #         if "table_" == name[:6]:
    #             tList[tbl.objectName()] = tbl
    #     tables_rt_model = self.tablesRTModel
    #     # logging.getLogger(__name__).setLevel(logging.INFO)
    #     info("ui table widgets: %s", tList.keys())
    #     debug(QtWidgets.QTableView)
    #     thd = []
    #     models = []
    #     for i, (wname, tbl) in enumerate(tList.items()):
    #         tname = wname[6:]
    #         tables_rt_model[wname] = tbl
    #         models.append(tsSqlTableModel(tname, self.data, self.data.db))
    #         tbl.setModel(models[i])
    #         thd.append(threading.Thread(target=self.run_add_module, args=(tname, tbl, models[i])))
    #         thd[i].start()
    #     for i in range(len(tList)):
    #         thd[i].join()
    #     # logging.getLogger(__name__).setLevel(logging.DEBUG)
    #     debug(tables_rt_model)

    def run_add_module(self, tname, tbl, mdl):
        model = self.data.addModel(tname, None, None, None, mdl)
        if model:
            tbl.setModel(model)

    def create_thread_for_tm(self, table, model):
        class thd_control(QObject):
            """class to control threads"""

            def __init__(self, parent):
                """Constructor for thd_control"""
                super().__init__(parent)
                # thd = QThread()

    def closeEvent(self, event):
        if SD.unsaved:
            ret = QMessageBox.warning(self, "Закрытие приложения", "Сохранить изменения?",
                                      QMessageBox.Save | QMessageBox.Discard | QMessageBox.Cancel,
                                      QMessageBox.Cancel)
            if ret == QMessageBox.Save:
                for mdl in SD.unsaved_model:
                    mdl.submitAll()
            elif ret == QMessageBox.Discard:
                for mdl in SD.unsaved_model:
                    mdl.revertAll()
            elif ret == QMessageBox.Cancel:
                event.ignore()
                return
            else:
                debug("something Wrong")
        info("closeEvent")
        SD.save_conf()
        qset = SD.qsettings
        qset.clear()  # remove all old entries
        qfont = QtWidgets.QApplication.instance().font()
        qset.setValue("font_size", qfont.pointSize())
        qset.setValue("mw/geometry", self.saveGeometry())
        qset.setValue("mw/windowState", self.saveState())
        cbox: myQComboBox
        for cbox in self.findChildren(myQComboBox):
            if cbox.inited:
                qset.setValue("cboxes/" + cbox.objectName(), cbox.currentText())
                debug("cbox saved - %s", cbox.objectName())
        qset.sync()  # not really needed?
        UI.threads_quit()
        SD.disconnect()
        return super().closeEvent(event)


class TsonData(QObject):
    """Manage and store Data"""

    # dbconnect: Signal = Signal(bool)

    def __init__(self, parent):
        """Constructor for 3sonData"""
        super().__init__(parent)
        debug("TsonData init")
        self.setParent(parent)
        #############################
        # load local config file
        # ---------------------------
        # self.config = SD.read_config(False)
        #############################
        # init members
        # ---------------------------
        self.db: Union[QSqlDatabase, None] = None
        self.notifies = []
        #############################
        # main models storage
        # ---------------------------
        self.models = {}

    def getNotifies(self) -> [str, ]:
        """
        """
        try:
            if self.db:
                qry = QSqlQuery(SD.get_db)
                qry.exec_("SELECT msg from notifies "
                          "WHERE archive=0")
                index = qry.record().indexOf('msg')
                while qry.next():
                    yield qry.value(index)
            else:
                return None
        except:
            return None

    def local_reports_compiler(self):
        QSqlDatabase()
        self.dbLocal = QSqlDatabase.addDatabase("QSQLITE", "conn1")
        db1 = self.dbLocal
        db1.setDatabaseName(":memory:")
        if db1.open():
            db = self.db


def main():
    info("3uson starting")
    debug("3uson debug on")
    #############################
    # start app
    # ---------------------------
    app = QtWidgets.QApplication(sys.argv)
    # SD.read_config(and_import=True)
    while True:
        WD.inited_models = {}
        SD.db_connections = {}
        SD._dbconnected = False
        main_window = MyApp()
        main_window.show()
        current_exit_code = app.exec_()
        if current_exit_code != MyApp.EXIT_CODE_REBOOT:
            break
        main_window.ui.menu_settings.removeEventFilter(main_window.ef)
        main_window.hide()
        # del WD
        # WD=_data
    sys.exit(current_exit_code)


if __name__ == "__main__":
    main()
