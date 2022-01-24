# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main_window.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *

from widgets.customQWidgets import myQTabWidget
from widgets.customQWidgets import stubQTableView
from widgets.customQWidgets import myQTableView
from widgets.customQWidgets import myQLineEdit
from widgets.customQWidgets import myQWidget
from widgets.customQWidgets import myQComboBox
from widgets.customQWidgets import myQCalendar
from widgets.customQWidgets import wsQTableView
from widgets.customQWidgets import qcSelectReport
from widgets.customQWidgets import QComboBoxWithDataMapper
from widgets.customQWidgets import myQDateEdit
from widgets.customQWidgets import add_info_QTableView
from widgets.customQWidgets import tsQTableViewYear
from widgets.customQWidgets import DepQTableView
from widgets.customQWidgets import infoQDockWidget
from widgets.customQWidgets import myQWidgetUnblockable


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1672, 760)
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        self.qaDBconnect = QAction(MainWindow)
        self.qaDBconnect.setObjectName(u"qaDBconnect")
        self.qaDBconnect.setEnabled(False)
        self.qaDBDisconnect = QAction(MainWindow)
        self.qaDBDisconnect.setObjectName(u"qaDBDisconnect")
        self.qa_close_app = QAction(MainWindow)
        self.qa_close_app.setObjectName(u"qa_close_app")
        self.qa_tab_people_of_dep = QAction(MainWindow)
        self.qa_tab_people_of_dep.setObjectName(u"qa_tab_people_of_dep")
        self.qa_tab__dep_has_client_more = QAction(MainWindow)
        self.qa_tab__dep_has_client_more.setObjectName(u"qa_tab__dep_has_client_more")
        self.qa_tab_journal = QAction(MainWindow)
        self.qa_tab_journal.setObjectName(u"qa_tab_journal")
        self.qa_tab_workers = QAction(MainWindow)
        self.qa_tab_workers.setObjectName(u"qa_tab_workers")
        self.qa_tab_serv_you = QAction(MainWindow)
        self.qa_tab_serv_you.setObjectName(u"qa_tab_serv_you")
        self.action_9 = QAction(MainWindow)
        self.action_9.setObjectName(u"action_9")
        self.action_9.setEnabled(False)
        font = QFont()
        font.setBold(True)
        font.setWeight(75)
        self.action_9.setFont(font)
        self.qa_act = QAction(MainWindow)
        self.qa_act.setObjectName(u"qa_act")
        self.qa_invoice = QAction(MainWindow)
        self.qa_invoice.setObjectName(u"qa_invoice")
        self.qa_contract = QAction(MainWindow)
        self.qa_contract.setObjectName(u"qa_contract")
        self.qa_request = QAction(MainWindow)
        self.qa_request.setObjectName(u"qa_request")
        self.action_14 = QAction(MainWindow)
        self.action_14.setObjectName(u"action_14")
        self.action_15 = QAction(MainWindow)
        self.action_15.setObjectName(u"action_15")
        self.action_15.setEnabled(False)
        self.action_15.setFont(font)
        self.action_16 = QAction(MainWindow)
        self.action_16.setObjectName(u"action_16")
        self.action_17 = QAction(MainWindow)
        self.action_17.setObjectName(u"action_17")
        self.action_18 = QAction(MainWindow)
        self.action_18.setObjectName(u"action_18")
        self.action_19 = QAction(MainWindow)
        self.action_19.setObjectName(u"action_19")
        self.action_20 = QAction(MainWindow)
        self.action_20.setObjectName(u"action_20")
        self.qa_style = QAction(MainWindow)
        self.qa_style.setObjectName(u"qa_style")
        self.qa_style.setCheckable(False)
        self.action_26 = QAction(MainWindow)
        self.action_26.setObjectName(u"action_26")
        self.qa_tab_dep = QAction(MainWindow)
        self.qa_tab_dep.setObjectName(u"qa_tab_dep")
        self.action_22 = QAction(MainWindow)
        self.action_22.setObjectName(u"action_22")
        self.action_year = QAction(MainWindow)
        self.action_year.setObjectName(u"action_year")
        self.action_curDep = QAction(MainWindow)
        self.action_curDep.setObjectName(u"action_curDep")
        self.qa_upd_fio_list = QAction(MainWindow)
        self.qa_upd_fio_list.setObjectName(u"qa_upd_fio_list")
        self.qaFontSmaller = QAction(MainWindow)
        self.qaFontSmaller.setObjectName(u"qaFontSmaller")
        self.qaFontSmaller.setCheckable(False)
        self.qaFontSmaller.setChecked(False)
        self.qaFontBigger = QAction(MainWindow)
        self.qaFontBigger.setObjectName(u"qaFontBigger")
        self.qaFontBigger.setCheckable(False)
        self.qaFontVBig = QAction(MainWindow)
        self.qaFontVBig.setObjectName(u"qaFontVBig")
        self.qaFontVBig.setCheckable(True)
        self.action_connected_user = QAction(MainWindow)
        self.action_connected_user.setObjectName(u"action_connected_user")
        self.qa_drop_qsettings = QAction(MainWindow)
        self.qa_drop_qsettings.setObjectName(u"qa_drop_qsettings")
        self.action_QT = QAction(MainWindow)
        self.action_QT.setObjectName(u"action_QT")
        self.action_save = QAction(MainWindow)
        self.action_save.setObjectName(u"action_save")
        self.action_discard = QAction(MainWindow)
        self.action_discard.setObjectName(u"action_discard")
        self.action_undo = QAction(MainWindow)
        self.action_undo.setObjectName(u"action_undo")
        self.action_redo = QAction(MainWindow)
        self.action_redo.setObjectName(u"action_redo")
        self.action_2 = QAction(MainWindow)
        self.action_2.setObjectName(u"action_2")
        self.action_2.setCheckable(True)
        self.action_23 = QAction(MainWindow)
        self.action_23.setObjectName(u"action_23")
        self.action_23.setCheckable(True)
        self.action_update_tables = QAction(MainWindow)
        self.action_update_tables.setObjectName(u"action_update_tables")
        self.action_24 = QAction(MainWindow)
        self.action_24.setObjectName(u"action_24")
        self.action_27 = QAction(MainWindow)
        self.action_27.setObjectName(u"action_27")
        self.action_25 = QAction(MainWindow)
        self.action_25.setObjectName(u"action_25")
        self.action_28 = QAction(MainWindow)
        self.action_28.setObjectName(u"action_28")
        self.action_update_tables_on_tab = QAction(MainWindow)
        self.action_update_tables_on_tab.setObjectName(u"action_update_tables_on_tab")
        self.qa_new_people = QAction(MainWindow)
        self.qa_new_people.setObjectName(u"qa_new_people")
        self.action_3 = QAction(MainWindow)
        self.action_3.setObjectName(u"action_3")
        self.action_4 = QAction(MainWindow)
        self.action_4.setObjectName(u"action_4")
        self.qa_goto_password = QAction(MainWindow)
        self.qa_goto_password.setObjectName(u"qa_goto_password")
        self.qaDBReconnect = QAction(MainWindow)
        self.qaDBReconnect.setObjectName(u"qaDBReconnect")
        self.my_test_action = QAction(MainWindow)
        self.my_test_action.setObjectName(u"my_test_action")
        self.qa_load_all_models = QAction(MainWindow)
        self.qa_load_all_models.setObjectName(u"qa_load_all_models")
        self.qa_show_settings = QAction(MainWindow)
        self.qa_show_settings.setObjectName(u"qa_show_settings")
        self.qa_menu_pd = QAction(MainWindow)
        self.qa_menu_pd.setObjectName(u"qa_menu_pd")
        self.qa_about = QAction(MainWindow)
        self.qa_about.setObjectName(u"qa_about")
        self.qa_tab_add_serv_by_day = QAction(MainWindow)
        self.qa_tab_add_serv_by_day.setObjectName(u"qa_tab_add_serv_by_day")
        self.qa_goto_back_tab = QAction(MainWindow)
        self.qa_goto_back_tab.setObjectName(u"qa_goto_back_tab")
        self.qa_predv_contract = QAction(MainWindow)
        self.qa_predv_contract.setObjectName(u"qa_predv_contract")
        self.action = QAction(MainWindow)
        self.action.setObjectName(u"action")
        self.action_6 = QAction(MainWindow)
        self.action_6.setObjectName(u"action_6")
        self.action_7 = QAction(MainWindow)
        self.action_7.setObjectName(u"action_7")
        self.qa_dock_people_info = QAction(MainWindow)
        self.qa_dock_people_info.setObjectName(u"qa_dock_people_info")
        self.qa_dock_people_info.setCheckable(True)
        self.qa_dock_people_info.setChecked(True)
        self.qa_dock_people_info.setVisible(True)
        self.qa_dock_people_info.setMenuRole(QAction.NoRole)
        self.qa_goto_forward_tab = QAction(MainWindow)
        self.qa_goto_forward_tab.setObjectName(u"qa_goto_forward_tab")
        self.qa_dirty_tab_unblocked = QAction(MainWindow)
        self.qa_dirty_tab_unblocked.setObjectName(u"qa_dirty_tab_unblocked")
        self.qa_dirty_tab_unblocked.setCheckable(True)
        self.qa_import_XLS = QAction(MainWindow)
        self.qa_import_XLS.setObjectName(u"qa_import_XLS")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setEnabled(True)
        sizePolicy1 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy1.setHorizontalStretch(4)
        sizePolicy1.setVerticalStretch(4)
        sizePolicy1.setHeightForWidth(self.centralwidget.sizePolicy().hasHeightForWidth())
        self.centralwidget.setSizePolicy(sizePolicy1)
        self.horizontalLayout_26 = QHBoxLayout(self.centralwidget)
        self.horizontalLayout_26.setObjectName(u"horizontalLayout_26")
        self.vl_centralwidget = QVBoxLayout()
        self.vl_centralwidget.setObjectName(u"vl_centralwidget")
        self.vl_centralwidget.setSizeConstraint(QLayout.SetNoConstraint)
        self.tabMain = myQTabWidget(self.centralwidget)
        self.tabMain.setObjectName(u"tabMain")
        sizePolicy2 = QSizePolicy(QSizePolicy.Ignored, QSizePolicy.Ignored)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(4)
        sizePolicy2.setHeightForWidth(self.tabMain.sizePolicy().hasHeightForWidth())
        self.tabMain.setSizePolicy(sizePolicy2)
        self.tab_add_serv = myQWidget()
        self.tab_add_serv.setObjectName(u"tab_add_serv")
        self.verticalLayout_18 = QVBoxLayout(self.tab_add_serv)
        self.verticalLayout_18.setObjectName(u"verticalLayout_18")
        self.tabs_add_serv = myQTabWidget(self.tab_add_serv)
        self.tabs_add_serv.setObjectName(u"tabs_add_serv")
        self.tabs_add_serv.setEnabled(True)
        self.tab_add_serv_by_day = myQWidget()
        self.tab_add_serv_by_day.setObjectName(u"tab_add_serv_by_day")
        self.verticalLayout_19 = QVBoxLayout(self.tab_add_serv_by_day)
        self.verticalLayout_19.setObjectName(u"verticalLayout_19")
        self.gl_tab_add_serv_by_day = QGridLayout()
        self.gl_tab_add_serv_by_day.setObjectName(u"gl_tab_add_serv_by_day")
        self.gl_tab_add_serv_by_day.setVerticalSpacing(0)
        self.btn_goto_worker = QToolButton(self.tab_add_serv_by_day)
        self.btn_goto_worker.setObjectName(u"btn_goto_worker")

        self.gl_tab_add_serv_by_day.addWidget(self.btn_goto_worker, 3, 2, 1, 1)

        self.horizontalLayout_9 = QHBoxLayout()
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.btn_qle_date_1 = QPushButton(self.tab_add_serv_by_day)
        self.btn_qle_date_1.setObjectName(u"btn_qle_date_1")
        sizePolicy3 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.btn_qle_date_1.sizePolicy().hasHeightForWidth())
        self.btn_qle_date_1.setSizePolicy(sizePolicy3)

        self.horizontalLayout_9.addWidget(self.btn_qle_date_1)

        self.qle_date = myQDateEdit(self.tab_add_serv_by_day)
        self.qle_date.setObjectName(u"qle_date")
        self.qle_date.setCalendarPopup(True)

        self.horizontalLayout_9.addWidget(self.qle_date)

        self.btn_qle_date_p1 = QPushButton(self.tab_add_serv_by_day)
        self.btn_qle_date_p1.setObjectName(u"btn_qle_date_p1")
        sizePolicy3.setHeightForWidth(self.btn_qle_date_p1.sizePolicy().hasHeightForWidth())
        self.btn_qle_date_p1.setSizePolicy(sizePolicy3)

        self.horizontalLayout_9.addWidget(self.btn_qle_date_p1)


        self.gl_tab_add_serv_by_day.addLayout(self.horizontalLayout_9, 0, 1, 1, 1)

        self.chkLAmount = QCheckBox(self.tab_add_serv_by_day)
        self.chkLAmount.setObjectName(u"chkLAmount")

        self.gl_tab_add_serv_by_day.addWidget(self.chkLAmount, 5, 3, 1, 1)

        self.cbx_1_ui_select_fiolist = myQComboBox(self.tab_add_serv_by_day)
        self.cbx_1_ui_select_fiolist.setObjectName(u"cbx_1_ui_select_fiolist")
        sizePolicy4 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Fixed)
        sizePolicy4.setHorizontalStretch(0)
        sizePolicy4.setVerticalStretch(0)
        sizePolicy4.setHeightForWidth(self.cbx_1_ui_select_fiolist.sizePolicy().hasHeightForWidth())
        self.cbx_1_ui_select_fiolist.setSizePolicy(sizePolicy4)
        self.cbx_1_ui_select_fiolist.setMinimumSize(QSize(250, 0))
        self.cbx_1_ui_select_fiolist.setEditable(True)

        self.gl_tab_add_serv_by_day.addWidget(self.cbx_1_ui_select_fiolist, 0, 4, 1, 1)

        self.chkLFio = QCheckBox(self.tab_add_serv_by_day)
        self.chkLFio.setObjectName(u"chkLFio")
        self.chkLFio.setChecked(True)

        self.gl_tab_add_serv_by_day.addWidget(self.chkLFio, 2, 3, 1, 1)

        self.label_2 = QLabel(self.tab_add_serv_by_day)
        self.label_2.setObjectName(u"label_2")

        self.gl_tab_add_serv_by_day.addWidget(self.label_2, 0, 3, 1, 1)

        self.chkLServ = QCheckBox(self.tab_add_serv_by_day)
        self.chkLServ.setObjectName(u"chkLServ")
        self.chkLServ.setChecked(True)

        self.gl_tab_add_serv_by_day.addWidget(self.chkLServ, 4, 3, 1, 1)

        self.label_34 = QLabel(self.tab_add_serv_by_day)
        self.label_34.setObjectName(u"label_34")

        self.gl_tab_add_serv_by_day.addWidget(self.label_34, 5, 0, 1, 1)

        self.cbx_1__serv_activ__dis_total = myQComboBox(self.tab_add_serv_by_day)
        self.cbx_1__serv_activ__dis_total.setObjectName(u"cbx_1__serv_activ__dis_total")
        self.cbx_1__serv_activ__dis_total.setInputMethodHints(Qt.ImhNone)
        self.cbx_1__serv_activ__dis_total.setEditable(True)
        self.cbx_1__serv_activ__dis_total.setMaxVisibleItems(15)

        self.gl_tab_add_serv_by_day.addWidget(self.cbx_1__serv_activ__dis_total, 4, 1, 1, 1)

        self.qleNote = QLineEdit(self.tab_add_serv_by_day)
        self.qleNote.setObjectName(u"qleNote")
        self.qleNote.setReadOnly(True)

        self.gl_tab_add_serv_by_day.addWidget(self.qleNote, 7, 1, 1, 3)

        self.horizontalLayout_10 = QHBoxLayout()
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.btn_serv_bydayQ = QPushButton(self.tab_add_serv_by_day)
        self.btn_serv_bydayQ.setObjectName(u"btn_serv_bydayQ")
        self.btn_serv_bydayQ.setLayoutDirection(Qt.LeftToRight)

        self.horizontalLayout_10.addWidget(self.btn_serv_bydayQ)

        self.btn_serv_bydayW = QPushButton(self.tab_add_serv_by_day)
        self.btn_serv_bydayW.setObjectName(u"btn_serv_bydayW")

        self.horizontalLayout_10.addWidget(self.btn_serv_bydayW)

        self.btn_serv_bydayE = QPushButton(self.tab_add_serv_by_day)
        self.btn_serv_bydayE.setObjectName(u"btn_serv_bydayE")

        self.horizontalLayout_10.addWidget(self.btn_serv_bydayE)

        self.btn_serv_bydayA = QPushButton(self.tab_add_serv_by_day)
        self.btn_serv_bydayA.setObjectName(u"btn_serv_bydayA")

        self.horizontalLayout_10.addWidget(self.btn_serv_bydayA)


        self.gl_tab_add_serv_by_day.addLayout(self.horizontalLayout_10, 8, 1, 1, 3)

        self.label_36 = QLabel(self.tab_add_serv_by_day)
        self.label_36.setObjectName(u"label_36")

        self.gl_tab_add_serv_by_day.addWidget(self.label_36, 8, 0, 1, 1)

        self.horizontalLayout_14 = QHBoxLayout()
        self.horizontalLayout_14.setObjectName(u"horizontalLayout_14")
        self.qleAmount = QSpinBox(self.tab_add_serv_by_day)
        self.qleAmount.setObjectName(u"qleAmount")
        self.qleAmount.setMaximum(152)

        self.horizontalLayout_14.addWidget(self.qleAmount)

        self.label_53 = QLabel(self.tab_add_serv_by_day)
        self.label_53.setObjectName(u"label_53")
        sizePolicy5 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Preferred)
        sizePolicy5.setHorizontalStretch(0)
        sizePolicy5.setVerticalStretch(0)
        sizePolicy5.setHeightForWidth(self.label_53.sizePolicy().hasHeightForWidth())
        self.label_53.setSizePolicy(sizePolicy5)

        self.horizontalLayout_14.addWidget(self.label_53)

        self.qle_serv_left = QLineEdit(self.tab_add_serv_by_day)
        self.qle_serv_left.setObjectName(u"qle_serv_left")
        sizePolicy6 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        sizePolicy6.setHorizontalStretch(0)
        sizePolicy6.setVerticalStretch(0)
        sizePolicy6.setHeightForWidth(self.qle_serv_left.sizePolicy().hasHeightForWidth())
        self.qle_serv_left.setSizePolicy(sizePolicy6)
        self.qle_serv_left.setReadOnly(True)

        self.horizontalLayout_14.addWidget(self.qle_serv_left)


        self.gl_tab_add_serv_by_day.addLayout(self.horizontalLayout_14, 5, 1, 1, 1)

        self.cbx_1__dep_has_worker = myQComboBox(self.tab_add_serv_by_day)
        self.cbx_1__dep_has_worker.setObjectName(u"cbx_1__dep_has_worker")
        self.cbx_1__dep_has_worker.setEnabled(True)
        self.cbx_1__dep_has_worker.setEditable(True)
        self.cbx_1__dep_has_worker.setMaxVisibleItems(20)

        self.gl_tab_add_serv_by_day.addWidget(self.cbx_1__dep_has_worker, 3, 1, 1, 1)

        self.label_3 = QLabel(self.tab_add_serv_by_day)
        self.label_3.setObjectName(u"label_3")

        self.gl_tab_add_serv_by_day.addWidget(self.label_3, 4, 0, 1, 1)

        self.chkLW = QCheckBox(self.tab_add_serv_by_day)
        self.chkLW.setObjectName(u"chkLW")
        self.chkLW.setChecked(True)

        self.gl_tab_add_serv_by_day.addWidget(self.chkLW, 3, 3, 1, 1)

        self.label_32 = QLabel(self.tab_add_serv_by_day)
        self.label_32.setObjectName(u"label_32")
        font1 = QFont()
        font1.setPointSize(14)
        font1.setBold(True)
        font1.setItalic(True)
        font1.setWeight(75)
        self.label_32.setFont(font1)
        self.label_32.setAlignment(Qt.AlignCenter)

        self.gl_tab_add_serv_by_day.addWidget(self.label_32, 0, 0, 1, 1)

        self.label = QLabel(self.tab_add_serv_by_day)
        self.label.setObjectName(u"label")

        self.gl_tab_add_serv_by_day.addWidget(self.label, 2, 0, 1, 1)

        self.label_33 = QLabel(self.tab_add_serv_by_day)
        self.label_33.setObjectName(u"label_33")

        self.gl_tab_add_serv_by_day.addWidget(self.label_33, 7, 0, 1, 1)

        self.label_35 = QLabel(self.tab_add_serv_by_day)
        self.label_35.setObjectName(u"label_35")

        self.gl_tab_add_serv_by_day.addWidget(self.label_35, 3, 0, 1, 1)

        self.btn_goto_client = QToolButton(self.tab_add_serv_by_day)
        self.btn_goto_client.setObjectName(u"btn_goto_client")

        self.gl_tab_add_serv_by_day.addWidget(self.btn_goto_client, 2, 2, 1, 1)

        self.cbx_1__dep_has_client__2 = myQComboBox(self.tab_add_serv_by_day)
        self.cbx_1__dep_has_client__2.setObjectName(u"cbx_1__dep_has_client__2")
        sizePolicy6.setHeightForWidth(self.cbx_1__dep_has_client__2.sizePolicy().hasHeightForWidth())
        self.cbx_1__dep_has_client__2.setSizePolicy(sizePolicy6)
        self.cbx_1__dep_has_client__2.setEditable(True)
        self.cbx_1__dep_has_client__2.setMaxVisibleItems(20)

        self.gl_tab_add_serv_by_day.addWidget(self.cbx_1__dep_has_client__2, 2, 1, 1, 1)

        self.chk_autosave = QCheckBox(self.tab_add_serv_by_day)
        self.chk_autosave.setObjectName(u"chk_autosave")
        self.chk_autosave.setChecked(True)

        self.gl_tab_add_serv_by_day.addWidget(self.chk_autosave, 8, 4, 1, 1)


        self.verticalLayout_19.addLayout(self.gl_tab_add_serv_by_day)

        self.tab__main_for_dep_by = myQTabWidget(self.tab_add_serv_by_day)
        self.tab__main_for_dep_by.setObjectName(u"tab__main_for_dep_by")
        self.tab_all_by_day = myQWidget()
        self.tab_all_by_day.setObjectName(u"tab_all_by_day")
        self.verticalLayout_20 = QVBoxLayout(self.tab_all_by_day)
        self.verticalLayout_20.setObjectName(u"verticalLayout_20")
        self.table__dep_has_main__where_vdate__by_vdate = DepQTableView(self.tab_all_by_day)
        self.table__dep_has_main__where_vdate__by_vdate.setObjectName(u"table__dep_has_main__where_vdate__by_vdate")

        self.verticalLayout_20.addWidget(self.table__dep_has_main__where_vdate__by_vdate)

        self.tab__main_for_dep_by.addTab(self.tab_all_by_day, "")
        self.tab_24 = myQWidget()
        self.tab_24.setObjectName(u"tab_24")
        self.verticalLayout_21 = QVBoxLayout(self.tab_24)
        self.verticalLayout_21.setObjectName(u"verticalLayout_21")
        self.table__dep_has_main__where_vdate__by_vdate_by_worker_id = DepQTableView(self.tab_24)
        self.table__dep_has_main__where_vdate__by_vdate_by_worker_id.setObjectName(u"table__dep_has_main__where_vdate__by_vdate_by_worker_id")

        self.verticalLayout_21.addWidget(self.table__dep_has_main__where_vdate__by_vdate_by_worker_id)

        self.tab__main_for_dep_by.addTab(self.tab_24, "")
        self.tab_7 = myQWidget()
        self.tab_7.setObjectName(u"tab_7")
        self.verticalLayout_3 = QVBoxLayout(self.tab_7)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.table__dep_has_main__where_vdate__by_vdate_by_client_id = DepQTableView(self.tab_7)
        self.table__dep_has_main__where_vdate__by_vdate_by_client_id.setObjectName(u"table__dep_has_main__where_vdate__by_vdate_by_client_id")

        self.verticalLayout_3.addWidget(self.table__dep_has_main__where_vdate__by_vdate_by_client_id)

        self.tab__main_for_dep_by.addTab(self.tab_7, "")
        self.tab_23 = myQWidget()
        self.tab_23.setObjectName(u"tab_23")
        self.verticalLayout_22 = QVBoxLayout(self.tab_23)
        self.verticalLayout_22.setObjectName(u"verticalLayout_22")
        self.table__dep_has_main__where_vdate__by_vdate_by_you = DepQTableView(self.tab_23)
        self.table__dep_has_main__where_vdate__by_vdate_by_you.setObjectName(u"table__dep_has_main__where_vdate__by_vdate_by_you")

        self.verticalLayout_22.addWidget(self.table__dep_has_main__where_vdate__by_vdate_by_you)

        self.tab__main_for_dep_by.addTab(self.tab_23, "")
        self.tab_25 = myQWidget()
        self.tab_25.setObjectName(u"tab_25")
        self.verticalLayout_23 = QVBoxLayout(self.tab_25)
        self.verticalLayout_23.setObjectName(u"verticalLayout_23")
        self.table__dep_has_main__where_vdate__by_vdate_by_serv_id = DepQTableView(self.tab_25)
        self.table__dep_has_main__where_vdate__by_vdate_by_serv_id.setObjectName(u"table__dep_has_main__where_vdate__by_vdate_by_serv_id")

        self.verticalLayout_23.addWidget(self.table__dep_has_main__where_vdate__by_vdate_by_serv_id)

        self.tab__main_for_dep_by.addTab(self.tab_25, "")

        self.verticalLayout_19.addWidget(self.tab__main_for_dep_by)

        self.tabs_add_serv.addTab(self.tab_add_serv_by_day, "")
        self.tab_add_serv_by_month = myQWidget()
        self.tab_add_serv_by_month.setObjectName(u"tab_add_serv_by_month")
        self.gridLayout_60 = QGridLayout(self.tab_add_serv_by_month)
        self.gridLayout_60.setObjectName(u"gridLayout_60")
        self.splitter = QSplitter(self.tab_add_serv_by_month)
        self.splitter.setObjectName(u"splitter")
        self.splitter.setOrientation(Qt.Vertical)
        self.widget_2 = QWidget(self.splitter)
        self.widget_2.setObjectName(u"widget_2")
        self.gridLayout_58 = QGridLayout(self.widget_2)
        self.gridLayout_58.setObjectName(u"gridLayout_58")
        self.line_2 = QFrame(self.widget_2)
        self.line_2.setObjectName(u"line_2")
        self.line_2.setFrameShape(QFrame.HLine)
        self.line_2.setFrameShadow(QFrame.Sunken)

        self.gridLayout_58.addWidget(self.line_2, 1, 0, 1, 1)

        self.gridLayout_15 = QGridLayout()
        self.gridLayout_15.setObjectName(u"gridLayout_15")
        self.gridLayout_15.setVerticalSpacing(0)
        self.horizontalLayout_19 = QHBoxLayout()
        self.horizontalLayout_19.setObjectName(u"horizontalLayout_19")

        self.gridLayout_15.addLayout(self.horizontalLayout_19, 2, 4, 1, 1)

        self.label_43 = QLabel(self.widget_2)
        self.label_43.setObjectName(u"label_43")
        sizePolicy7 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Preferred)
        sizePolicy7.setHorizontalStretch(0)
        sizePolicy7.setVerticalStretch(0)
        sizePolicy7.setHeightForWidth(self.label_43.sizePolicy().hasHeightForWidth())
        self.label_43.setSizePolicy(sizePolicy7)

        self.gridLayout_15.addWidget(self.label_43, 1, 0, 1, 1)

        self.cbx_1__dep_has_client__3 = myQComboBox(self.widget_2)
        self.cbx_1__dep_has_client__3.setObjectName(u"cbx_1__dep_has_client__3")
        sizePolicy6.setHeightForWidth(self.cbx_1__dep_has_client__3.sizePolicy().hasHeightForWidth())
        self.cbx_1__dep_has_client__3.setSizePolicy(sizePolicy6)
        self.cbx_1__dep_has_client__3.setEditable(True)

        self.gridLayout_15.addWidget(self.cbx_1__dep_has_client__3, 0, 1, 1, 3)

        self.frame_10 = QFrame(self.widget_2)
        self.frame_10.setObjectName(u"frame_10")
        self.frame_10.setFrameShape(QFrame.StyledPanel)
        self.frame_10.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_22 = QHBoxLayout(self.frame_10)
        self.horizontalLayout_22.setObjectName(u"horizontalLayout_22")
        self.frame1111111 = QFrame(self.frame_10)
        self.frame1111111.setObjectName(u"frame1111111")
        sizePolicy7.setHeightForWidth(self.frame1111111.sizePolicy().hasHeightForWidth())
        self.frame1111111.setSizePolicy(sizePolicy7)
        self.gridLayout_36 = QGridLayout(self.frame1111111)
        self.gridLayout_36.setSpacing(10)
        self.gridLayout_36.setObjectName(u"gridLayout_36")
        self.gridLayout_36.setContentsMargins(6, 6, 6, 6)
        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout_36.addItem(self.verticalSpacer, 14, 0, 1, 1)

        self.label_37 = QLabel(self.frame1111111)
        self.label_37.setObjectName(u"label_37")
        sizePolicy5.setHeightForWidth(self.label_37.sizePolicy().hasHeightForWidth())
        self.label_37.setSizePolicy(sizePolicy5)

        self.gridLayout_36.addWidget(self.label_37, 6, 0, 1, 1)

        self.lbl_input_serv = QLabel(self.frame1111111)
        self.lbl_input_serv.setObjectName(u"lbl_input_serv")

        self.gridLayout_36.addWidget(self.lbl_input_serv, 11, 0, 1, 1)

        self.chk_mouse_left = QCheckBox(self.frame1111111)
        self.chk_mouse_left.setObjectName(u"chk_mouse_left")
        self.chk_mouse_left.setChecked(True)

        self.gridLayout_36.addWidget(self.chk_mouse_left, 2, 0, 1, 2)

        self.chk_continue_input = QCheckBox(self.frame1111111)
        self.chk_continue_input.setObjectName(u"chk_continue_input")
        self.chk_continue_input.setChecked(True)

        self.gridLayout_36.addWidget(self.chk_continue_input, 4, 0, 1, 2)

        self.lcd_serv_num = QLCDNumber(self.frame1111111)
        self.lcd_serv_num.setObjectName(u"lcd_serv_num")
        self.lcd_serv_num.setAutoFillBackground(False)

        self.gridLayout_36.addWidget(self.lcd_serv_num, 11, 1, 1, 1)

        self.buttonBox = QDialogButtonBox(self.frame1111111)
        self.buttonBox.setObjectName(u"buttonBox")
        sizePolicy3.setHeightForWidth(self.buttonBox.sizePolicy().hasHeightForWidth())
        self.buttonBox.setSizePolicy(sizePolicy3)
        self.buttonBox.setStandardButtons(QDialogButtonBox.Cancel|QDialogButtonBox.Ok)

        self.gridLayout_36.addWidget(self.buttonBox, 18, 0, 1, 2)

        self.pb_start_serv_add = QPushButton(self.frame1111111)
        self.pb_start_serv_add.setObjectName(u"pb_start_serv_add")
        sizePolicy3.setHeightForWidth(self.pb_start_serv_add.sizePolicy().hasHeightForWidth())
        self.pb_start_serv_add.setSizePolicy(sizePolicy3)
        self.pb_start_serv_add.setMinimumSize(QSize(180, 0))
        self.pb_start_serv_add.setBaseSize(QSize(160, 64))
        self.pb_start_serv_add.setStyleSheet(u"  QPushButton:checked { background-color: red; \n"
"text: bold;\n"
"color: white;\n"
"border: none; \n"
" background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                        stop: 0 #ff0b0e, stop: 1 #ff979a);\n"
"    \n"
"}")
        self.pb_start_serv_add.setCheckable(True)
        self.pb_start_serv_add.setFlat(False)

        self.gridLayout_36.addWidget(self.pb_start_serv_add, 1, 0, 1, 2)

        self.chk_wheel = QCheckBox(self.frame1111111)
        self.chk_wheel.setObjectName(u"chk_wheel")
        self.chk_wheel.setChecked(True)

        self.gridLayout_36.addWidget(self.chk_wheel, 3, 0, 1, 2)

        self.label_66 = QLabel(self.frame1111111)
        self.label_66.setObjectName(u"label_66")

        self.gridLayout_36.addWidget(self.label_66, 12, 0, 1, 1)

        self.qleAmount2 = QSpinBox(self.frame1111111)
        self.qleAmount2.setObjectName(u"qleAmount2")
        sizePolicy3.setHeightForWidth(self.qleAmount2.sizePolicy().hasHeightForWidth())
        self.qleAmount2.setSizePolicy(sizePolicy3)
        self.qleAmount2.setMinimumSize(QSize(0, 0))
        self.qleAmount2.setMaximum(20)
        self.qleAmount2.setValue(0)

        self.gridLayout_36.addWidget(self.qleAmount2, 6, 1, 1, 1)

        self.lcdNumber = QLCDNumber(self.frame1111111)
        self.lcdNumber.setObjectName(u"lcdNumber")

        self.gridLayout_36.addWidget(self.lcdNumber, 12, 1, 1, 1)

        self.chk_enter_input = QCheckBox(self.frame1111111)
        self.chk_enter_input.setObjectName(u"chk_enter_input")
        sizePolicy8 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Fixed)
        sizePolicy8.setHorizontalStretch(0)
        sizePolicy8.setVerticalStretch(0)
        sizePolicy8.setHeightForWidth(self.chk_enter_input.sizePolicy().hasHeightForWidth())
        self.chk_enter_input.setSizePolicy(sizePolicy8)
        self.chk_enter_input.setChecked(True)

        self.gridLayout_36.addWidget(self.chk_enter_input, 5, 0, 1, 2)


        self.horizontalLayout_22.addWidget(self.frame1111111)

        self.clndr__dep_has_main_raw__where_calendar = myQCalendar(self.frame_10)
        self.clndr__dep_has_main_raw__where_calendar.setObjectName(u"clndr__dep_has_main_raw__where_calendar")
        sizePolicy9 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.MinimumExpanding)
        sizePolicy9.setHorizontalStretch(0)
        sizePolicy9.setVerticalStretch(0)
        sizePolicy9.setHeightForWidth(self.clndr__dep_has_main_raw__where_calendar.sizePolicy().hasHeightForWidth())
        self.clndr__dep_has_main_raw__where_calendar.setSizePolicy(sizePolicy9)
        self.clndr__dep_has_main_raw__where_calendar.setMinimumSize(QSize(450, 240))

        self.horizontalLayout_22.addWidget(self.clndr__dep_has_main_raw__where_calendar)


        self.gridLayout_15.addWidget(self.frame_10, 4, 0, 1, 5)

        self.label_40 = QLabel(self.widget_2)
        self.label_40.setObjectName(u"label_40")
        sizePolicy7.setHeightForWidth(self.label_40.sizePolicy().hasHeightForWidth())
        self.label_40.setSizePolicy(sizePolicy7)
        self.label_40.setMinimumSize(QSize(0, 0))

        self.gridLayout_15.addWidget(self.label_40, 0, 0, 1, 1)

        self.horizontalLayout_21 = QHBoxLayout()
        self.horizontalLayout_21.setObjectName(u"horizontalLayout_21")
        self.label_70 = QLabel(self.widget_2)
        self.label_70.setObjectName(u"label_70")
        sizePolicy7.setHeightForWidth(self.label_70.sizePolicy().hasHeightForWidth())
        self.label_70.setSizePolicy(sizePolicy7)

        self.horizontalLayout_21.addWidget(self.label_70)

        self.cbx_1_ui_select_fiolist__3 = myQComboBox(self.widget_2)
        self.cbx_1_ui_select_fiolist__3.setObjectName(u"cbx_1_ui_select_fiolist__3")
        self.cbx_1_ui_select_fiolist__3.setMinimumSize(QSize(250, 0))

        self.horizontalLayout_21.addWidget(self.cbx_1_ui_select_fiolist__3)


        self.gridLayout_15.addLayout(self.horizontalLayout_21, 0, 4, 1, 1)

        self.cbx_1__serv_activ__dis_total__2 = myQComboBox(self.widget_2)
        self.cbx_1__serv_activ__dis_total__2.setObjectName(u"cbx_1__serv_activ__dis_total__2")
        sizePolicy6.setHeightForWidth(self.cbx_1__serv_activ__dis_total__2.sizePolicy().hasHeightForWidth())
        self.cbx_1__serv_activ__dis_total__2.setSizePolicy(sizePolicy6)
        self.cbx_1__serv_activ__dis_total__2.setEditable(True)

        self.gridLayout_15.addWidget(self.cbx_1__serv_activ__dis_total__2, 2, 1, 1, 3)

        self.horizontalLayout_17 = QHBoxLayout()
        self.horizontalLayout_17.setObjectName(u"horizontalLayout_17")

        self.gridLayout_15.addLayout(self.horizontalLayout_17, 3, 4, 1, 1)

        self.horizontalLayout_18 = QHBoxLayout()
        self.horizontalLayout_18.setObjectName(u"horizontalLayout_18")
        self.label_67 = QLabel(self.widget_2)
        self.label_67.setObjectName(u"label_67")
        sizePolicy5.setHeightForWidth(self.label_67.sizePolicy().hasHeightForWidth())
        self.label_67.setSizePolicy(sizePolicy5)
        self.label_67.setMaximumSize(QSize(50, 16777215))

        self.horizontalLayout_18.addWidget(self.label_67)

        self.qleNote2 = myQLineEdit(self.widget_2)
        self.qleNote2.setObjectName(u"qleNote2")
        sizePolicy4.setHeightForWidth(self.qleNote2.sizePolicy().hasHeightForWidth())
        self.qleNote2.setSizePolicy(sizePolicy4)
        self.qleNote2.setMinimumSize(QSize(250, 0))
        self.qleNote2.setMaximumSize(QSize(16777215, 16777215))
        self.qleNote2.setBaseSize(QSize(0, 0))
        self.qleNote2.setReadOnly(True)

        self.horizontalLayout_18.addWidget(self.qleNote2)


        self.gridLayout_15.addLayout(self.horizontalLayout_18, 1, 4, 1, 1)

        self.label_41 = QLabel(self.widget_2)
        self.label_41.setObjectName(u"label_41")
        sizePolicy7.setHeightForWidth(self.label_41.sizePolicy().hasHeightForWidth())
        self.label_41.setSizePolicy(sizePolicy7)

        self.gridLayout_15.addWidget(self.label_41, 2, 0, 1, 1)

        self.cbx_1__dep_has_worker__2 = myQComboBox(self.widget_2)
        self.cbx_1__dep_has_worker__2.setObjectName(u"cbx_1__dep_has_worker__2")
        self.cbx_1__dep_has_worker__2.setEnabled(True)
        self.cbx_1__dep_has_worker__2.setEditable(True)

        self.gridLayout_15.addWidget(self.cbx_1__dep_has_worker__2, 1, 1, 1, 3)


        self.gridLayout_58.addLayout(self.gridLayout_15, 0, 0, 1, 1)

        self.splitter.addWidget(self.widget_2)
        self.widget_4 = QWidget(self.splitter)
        self.widget_4.setObjectName(u"widget_4")
        self.gridLayout_59 = QGridLayout(self.widget_4)
        self.gridLayout_59.setObjectName(u"gridLayout_59")
        self.tab_user_has_main = myQTabWidget(self.widget_4)
        self.tab_user_has_main.setObjectName(u"tab_user_has_main")
        self.tab_28 = myQWidget()
        self.tab_28.setObjectName(u"tab_28")
        self.verticalLayout_25 = QVBoxLayout(self.tab_28)
        self.verticalLayout_25.setObjectName(u"verticalLayout_25")
        self.table__user_has_main_today = myQTableView(self.tab_28)
        self.table__user_has_main_today.setObjectName(u"table__user_has_main_today")

        self.verticalLayout_25.addWidget(self.table__user_has_main_today)

        self.tab_user_has_main.addTab(self.tab_28, "")
        self.tab_29 = myQWidget()
        self.tab_29.setObjectName(u"tab_29")
        self.verticalLayout_26 = QVBoxLayout(self.tab_29)
        self.verticalLayout_26.setObjectName(u"verticalLayout_26")
        self.table__user_has_main_limit30 = myQTableView(self.tab_29)
        self.table__user_has_main_limit30.setObjectName(u"table__user_has_main_limit30")

        self.verticalLayout_26.addWidget(self.table__user_has_main_limit30)

        self.tab_user_has_main.addTab(self.tab_29, "")
        self.tab_am_serv_in_day = myQWidget()
        self.tab_am_serv_in_day.setObjectName(u"tab_am_serv_in_day")
        self.verticalLayout_12 = QVBoxLayout(self.tab_am_serv_in_day)
        self.verticalLayout_12.setObjectName(u"verticalLayout_12")
        self.table__dep_has_main__where_calendar__by_vdate__2 = DepQTableView(self.tab_am_serv_in_day)
        self.table__dep_has_main__where_calendar__by_vdate__2.setObjectName(u"table__dep_has_main__where_calendar__by_vdate__2")

        self.verticalLayout_12.addWidget(self.table__dep_has_main__where_calendar__by_vdate__2)

        self.tab_user_has_main.addTab(self.tab_am_serv_in_day, "")
        self.tab_17 = myQWidget()
        self.tab_17.setObjectName(u"tab_17")
        self.gridLayout_73 = QGridLayout(self.tab_17)
        self.gridLayout_73.setObjectName(u"gridLayout_73")
        self.lineEdit_15 = QLineEdit(self.tab_17)
        self.lineEdit_15.setObjectName(u"lineEdit_15")
        sizePolicy4.setHeightForWidth(self.lineEdit_15.sizePolicy().hasHeightForWidth())
        self.lineEdit_15.setSizePolicy(sizePolicy4)

        self.gridLayout_73.addWidget(self.lineEdit_15, 0, 2, 1, 1)

        self.label_serv_in = QLabel(self.tab_17)
        self.label_serv_in.setObjectName(u"label_serv_in")
        self.label_serv_in.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_73.addWidget(self.label_serv_in, 0, 1, 1, 1)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_73.addItem(self.horizontalSpacer_2, 0, 0, 1, 1)

        self.table__dep_has_main__where_calendar__by_vdate_by_client_id__2 = DepQTableView(self.tab_17)
        self.table__dep_has_main__where_calendar__by_vdate_by_client_id__2.setObjectName(u"table__dep_has_main__where_calendar__by_vdate_by_client_id__2")

        self.gridLayout_73.addWidget(self.table__dep_has_main__where_calendar__by_vdate_by_client_id__2, 1, 0, 1, 3)

        self.tab_user_has_main.addTab(self.tab_17, "")
        self.tab_18 = myQWidget()
        self.tab_18.setObjectName(u"tab_18")
        self.gridLayout_74 = QGridLayout(self.tab_18)
        self.gridLayout_74.setObjectName(u"gridLayout_74")
        self.table__dep_has_main__where_calendar__by_vdate_by_serv_id__2 = DepQTableView(self.tab_18)
        self.table__dep_has_main__where_calendar__by_vdate_by_serv_id__2.setObjectName(u"table__dep_has_main__where_calendar__by_vdate_by_serv_id__2")

        self.gridLayout_74.addWidget(self.table__dep_has_main__where_calendar__by_vdate_by_serv_id__2, 0, 0, 1, 1)

        self.tab_user_has_main.addTab(self.tab_18, "")
        self.tab_21 = myQWidget()
        self.tab_21.setObjectName(u"tab_21")
        self.gridLayout_75 = QGridLayout(self.tab_21)
        self.gridLayout_75.setObjectName(u"gridLayout_75")
        self.table__dep_has_main__where_calendar__by_vdate_by_worker_id__3 = DepQTableView(self.tab_21)
        self.table__dep_has_main__where_calendar__by_vdate_by_worker_id__3.setObjectName(u"table__dep_has_main__where_calendar__by_vdate_by_worker_id__3")

        self.gridLayout_75.addWidget(self.table__dep_has_main__where_calendar__by_vdate_by_worker_id__3, 0, 0, 1, 1)

        self.tab_user_has_main.addTab(self.tab_21, "")
        self.tab_27 = myQWidget()
        self.tab_27.setObjectName(u"tab_27")
        self.gridLayout_76 = QGridLayout(self.tab_27)
        self.gridLayout_76.setObjectName(u"gridLayout_76")
        self.table__dep_has_main__where_calendar__by_vdate_by_client_id_by_serv_id = DepQTableView(self.tab_27)
        self.table__dep_has_main__where_calendar__by_vdate_by_client_id_by_serv_id.setObjectName(u"table__dep_has_main__where_calendar__by_vdate_by_client_id_by_serv_id")

        self.gridLayout_76.addWidget(self.table__dep_has_main__where_calendar__by_vdate_by_client_id_by_serv_id, 0, 0, 1, 1)

        self.tab_user_has_main.addTab(self.tab_27, "")
        self.tab_8 = myQWidget()
        self.tab_8.setObjectName(u"tab_8")
        self.gridLayout_61 = QGridLayout(self.tab_8)
        self.gridLayout_61.setObjectName(u"gridLayout_61")
        self.textEdit_2 = QTextEdit(self.tab_8)
        self.textEdit_2.setObjectName(u"textEdit_2")

        self.gridLayout_61.addWidget(self.textEdit_2, 0, 0, 1, 1)

        self.tab_user_has_main.addTab(self.tab_8, "")

        self.gridLayout_59.addWidget(self.tab_user_has_main, 1, 0, 1, 1)

        self.line = QFrame(self.widget_4)
        self.line.setObjectName(u"line")
        self.line.setFrameShape(QFrame.HLine)
        self.line.setFrameShadow(QFrame.Sunken)

        self.gridLayout_59.addWidget(self.line, 0, 0, 1, 1)

        self.splitter.addWidget(self.widget_4)

        self.gridLayout_60.addWidget(self.splitter, 0, 0, 1, 1)

        self.tabs_add_serv.addTab(self.tab_add_serv_by_month, "")
        self.tab_add_group_services = myQWidget()
        self.tab_add_group_services.setObjectName(u"tab_add_group_services")
        self.verticalLayout_27 = QVBoxLayout(self.tab_add_group_services)
        self.verticalLayout_27.setObjectName(u"verticalLayout_27")
        self.gridLayout_17 = QGridLayout()
        self.gridLayout_17.setSpacing(20)
        self.gridLayout_17.setObjectName(u"gridLayout_17")
        self.plainTextEdit = QPlainTextEdit(self.tab_add_group_services)
        self.plainTextEdit.setObjectName(u"plainTextEdit")
        sizePolicy10 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Preferred)
        sizePolicy10.setHorizontalStretch(0)
        sizePolicy10.setVerticalStretch(1)
        sizePolicy10.setHeightForWidth(self.plainTextEdit.sizePolicy().hasHeightForWidth())
        self.plainTextEdit.setSizePolicy(sizePolicy10)
        self.plainTextEdit.setReadOnly(True)

        self.gridLayout_17.addWidget(self.plainTextEdit, 7, 0, 1, 2)

        self.groupBox_5 = QGroupBox(self.tab_add_group_services)
        self.groupBox_5.setObjectName(u"groupBox_5")
        sizePolicy11 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy11.setHorizontalStretch(1)
        sizePolicy11.setVerticalStretch(3)
        sizePolicy11.setHeightForWidth(self.groupBox_5.sizePolicy().hasHeightForWidth())
        self.groupBox_5.setSizePolicy(sizePolicy11)
        self.groupBox_5.setAutoFillBackground(False)
        self.groupBox_5.setFlat(False)
        self.gridLayout_19 = QGridLayout(self.groupBox_5)
        self.gridLayout_19.setSpacing(6)
        self.gridLayout_19.setObjectName(u"gridLayout_19")
        self.gridLayout_19.setContentsMargins(16, 20, 16, 6)
        self.tableView_2 = QTableView(self.groupBox_5)
        self.tableView_2.setObjectName(u"tableView_2")
        sizePolicy12 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy12.setHorizontalStretch(0)
        sizePolicy12.setVerticalStretch(0)
        sizePolicy12.setHeightForWidth(self.tableView_2.sizePolicy().hasHeightForWidth())
        self.tableView_2.setSizePolicy(sizePolicy12)

        self.gridLayout_19.addWidget(self.tableView_2, 5, 0, 1, 2)

        self.pushButton_10 = QPushButton(self.groupBox_5)
        self.pushButton_10.setObjectName(u"pushButton_10")

        self.gridLayout_19.addWidget(self.pushButton_10, 4, 1, 1, 1)

        self.label_8 = QLabel(self.groupBox_5)
        self.label_8.setObjectName(u"label_8")

        self.gridLayout_19.addWidget(self.label_8, 4, 0, 1, 1)

        self.lineEdit = QLineEdit(self.groupBox_5)
        self.lineEdit.setObjectName(u"lineEdit")

        self.gridLayout_19.addWidget(self.lineEdit, 3, 1, 1, 1)

        self.label_47 = QLabel(self.groupBox_5)
        self.label_47.setObjectName(u"label_47")

        self.gridLayout_19.addWidget(self.label_47, 3, 0, 1, 1)


        self.gridLayout_17.addWidget(self.groupBox_5, 0, 0, 5, 2)

        self.groupBox_6 = QGroupBox(self.tab_add_group_services)
        self.groupBox_6.setObjectName(u"groupBox_6")
        self.gridLayout_20 = QGridLayout(self.groupBox_6)
        self.gridLayout_20.setSpacing(4)
        self.gridLayout_20.setObjectName(u"gridLayout_20")
        self.gridLayout_20.setContentsMargins(16, 20, 16, 6)
        self.pushButton_11 = QPushButton(self.groupBox_6)
        self.pushButton_11.setObjectName(u"pushButton_11")

        self.gridLayout_20.addWidget(self.pushButton_11, 1, 2, 1, 1)

        self.pushButton_8 = QPushButton(self.groupBox_6)
        self.pushButton_8.setObjectName(u"pushButton_8")

        self.gridLayout_20.addWidget(self.pushButton_8, 1, 0, 1, 1)

        self.tableView_5 = QTableView(self.groupBox_6)
        self.tableView_5.setObjectName(u"tableView_5")

        self.gridLayout_20.addWidget(self.tableView_5, 3, 0, 1, 3)

        self.pushButton_9 = QPushButton(self.groupBox_6)
        self.pushButton_9.setObjectName(u"pushButton_9")

        self.gridLayout_20.addWidget(self.pushButton_9, 1, 1, 1, 1)

        self.label_38 = QLabel(self.groupBox_6)
        self.label_38.setObjectName(u"label_38")

        self.gridLayout_20.addWidget(self.label_38, 2, 0, 1, 1)


        self.gridLayout_17.addWidget(self.groupBox_6, 1, 2, 7, 2)

        self.groupBox_4 = QGroupBox(self.tab_add_group_services)
        self.groupBox_4.setObjectName(u"groupBox_4")
        sizePolicy13 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy13.setHorizontalStretch(3)
        sizePolicy13.setVerticalStretch(0)
        sizePolicy13.setHeightForWidth(self.groupBox_4.sizePolicy().hasHeightForWidth())
        self.groupBox_4.setSizePolicy(sizePolicy13)
        self.gridLayout_21 = QGridLayout(self.groupBox_4)
        self.gridLayout_21.setSpacing(4)
        self.gridLayout_21.setObjectName(u"gridLayout_21")
        self.gridLayout_21.setContentsMargins(16, 20, 16, 6)
        self.qleAmount_2 = QSpinBox(self.groupBox_4)
        self.qleAmount_2.setObjectName(u"qleAmount_2")
        self.qleAmount_2.setMaximum(152)

        self.gridLayout_21.addWidget(self.qleAmount_2, 4, 1, 1, 1)

        self.label_42 = QLabel(self.groupBox_4)
        self.label_42.setObjectName(u"label_42")

        self.gridLayout_21.addWidget(self.label_42, 4, 0, 1, 1)

        self.label_39 = QLabel(self.groupBox_4)
        self.label_39.setObjectName(u"label_39")

        self.gridLayout_21.addWidget(self.label_39, 3, 0, 1, 1)

        self.label_45 = QLabel(self.groupBox_4)
        self.label_45.setObjectName(u"label_45")

        self.gridLayout_21.addWidget(self.label_45, 5, 0, 1, 1)

        self.comboServ_2 = QComboBox(self.groupBox_4)
        self.comboServ_2.setObjectName(u"comboServ_2")
        sizePolicy6.setHeightForWidth(self.comboServ_2.sizePolicy().hasHeightForWidth())
        self.comboServ_2.setSizePolicy(sizePolicy6)
        self.comboServ_2.setInputMethodHints(Qt.ImhNone)
        self.comboServ_2.setEditable(True)
        self.comboServ_2.setMaxVisibleItems(15)

        self.gridLayout_21.addWidget(self.comboServ_2, 2, 1, 1, 1)

        self.label_44 = QLabel(self.groupBox_4)
        self.label_44.setObjectName(u"label_44")

        self.gridLayout_21.addWidget(self.label_44, 2, 0, 1, 1)

        self.qleNote_2 = QLineEdit(self.groupBox_4)
        self.qleNote_2.setObjectName(u"qleNote_2")
        self.qleNote_2.setReadOnly(True)

        self.gridLayout_21.addWidget(self.qleNote_2, 5, 1, 1, 1)

        self.comboW_2 = QComboBox(self.groupBox_4)
        self.comboW_2.setObjectName(u"comboW_2")
        self.comboW_2.setEnabled(True)
        sizePolicy6.setHeightForWidth(self.comboW_2.sizePolicy().hasHeightForWidth())
        self.comboW_2.setSizePolicy(sizePolicy6)
        self.comboW_2.setEditable(True)
        self.comboW_2.setMaxVisibleItems(15)

        self.gridLayout_21.addWidget(self.comboW_2, 3, 1, 1, 1)

        self.label_46 = QLabel(self.groupBox_4)
        self.label_46.setObjectName(u"label_46")
        self.label_46.setFont(font1)
        self.label_46.setAlignment(Qt.AlignCenter)

        self.gridLayout_21.addWidget(self.label_46, 1, 0, 1, 1)

        self.horizontalLayout_12 = QHBoxLayout()
        self.horizontalLayout_12.setObjectName(u"horizontalLayout_12")
        self.btn_qle_date_2 = QPushButton(self.groupBox_4)
        self.btn_qle_date_2.setObjectName(u"btn_qle_date_2")
        sizePolicy3.setHeightForWidth(self.btn_qle_date_2.sizePolicy().hasHeightForWidth())
        self.btn_qle_date_2.setSizePolicy(sizePolicy3)

        self.horizontalLayout_12.addWidget(self.btn_qle_date_2)

        self.qle_date_2 = QDateEdit(self.groupBox_4)
        self.qle_date_2.setObjectName(u"qle_date_2")
        self.qle_date_2.setCalendarPopup(True)

        self.horizontalLayout_12.addWidget(self.qle_date_2)

        self.btn_qle_date_p1_2 = QPushButton(self.groupBox_4)
        self.btn_qle_date_p1_2.setObjectName(u"btn_qle_date_p1_2")
        sizePolicy3.setHeightForWidth(self.btn_qle_date_p1_2.sizePolicy().hasHeightForWidth())
        self.btn_qle_date_p1_2.setSizePolicy(sizePolicy3)

        self.horizontalLayout_12.addWidget(self.btn_qle_date_p1_2)


        self.gridLayout_21.addLayout(self.horizontalLayout_12, 1, 1, 1, 1)


        self.gridLayout_17.addWidget(self.groupBox_4, 0, 2, 1, 2)

        self.label_48 = QLabel(self.tab_add_group_services)
        self.label_48.setObjectName(u"label_48")

        self.gridLayout_17.addWidget(self.label_48, 6, 0, 1, 1)


        self.verticalLayout_27.addLayout(self.gridLayout_17)

        self.pushButton_12 = QPushButton(self.tab_add_group_services)
        self.pushButton_12.setObjectName(u"pushButton_12")

        self.verticalLayout_27.addWidget(self.pushButton_12)

        self.tabs_add_serv.addTab(self.tab_add_group_services, "")
        self.tab_show_group_services = myQWidget()
        self.tab_show_group_services.setObjectName(u"tab_show_group_services")
        self.pushButton_3 = QPushButton(self.tab_show_group_services)
        self.pushButton_3.setObjectName(u"pushButton_3")
        self.pushButton_3.setGeometry(QRect(240, 140, 75, 23))
        self.tabs_add_serv.addTab(self.tab_show_group_services, "")
        self.tab_add_club_services = myQWidget()
        self.tab_add_club_services.setObjectName(u"tab_add_club_services")
        self.gridLayout_57 = QGridLayout(self.tab_add_club_services)
        self.gridLayout_57.setObjectName(u"gridLayout_57")
        self.pushButton_37 = QPushButton(self.tab_add_club_services)
        self.pushButton_37.setObjectName(u"pushButton_37")

        self.gridLayout_57.addWidget(self.pushButton_37, 0, 0, 1, 1)

        self.tabs_add_serv.addTab(self.tab_add_club_services, "")
        self.tab_table_serv = myQWidget()
        self.tab_table_serv.setObjectName(u"tab_table_serv")
        self.gridLayout_96 = QGridLayout(self.tab_table_serv)
        self.gridLayout_96.setObjectName(u"gridLayout_96")
        self.label_87 = QLabel(self.tab_table_serv)
        self.label_87.setObjectName(u"label_87")
        sizePolicy7.setHeightForWidth(self.label_87.sizePolicy().hasHeightForWidth())
        self.label_87.setSizePolicy(sizePolicy7)
        self.label_87.setMinimumSize(QSize(0, 0))

        self.gridLayout_96.addWidget(self.label_87, 0, 1, 1, 1)

        self.cbx_1_contracts__by_client_id__2 = QComboBoxWithDataMapper(self.tab_table_serv)
        self.cbx_1_contracts__by_client_id__2.setObjectName(u"cbx_1_contracts__by_client_id__2")
        sizePolicy6.setHeightForWidth(self.cbx_1_contracts__by_client_id__2.sizePolicy().hasHeightForWidth())
        self.cbx_1_contracts__by_client_id__2.setSizePolicy(sizePolicy6)
        self.cbx_1_contracts__by_client_id__2.setEditable(True)
        self.cbx_1_contracts__by_client_id__2.setProperty("sort_order", 1)

        self.gridLayout_96.addWidget(self.cbx_1_contracts__by_client_id__2, 1, 2, 1, 1)

        self.widget_6 = QWidget(self.tab_table_serv)
        self.widget_6.setObjectName(u"widget_6")

        self.gridLayout_96.addWidget(self.widget_6, 1, 0, 1, 1)

        self.label_86 = QLabel(self.tab_table_serv)
        self.label_86.setObjectName(u"label_86")
        sizePolicy14 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Minimum)
        sizePolicy14.setHorizontalStretch(0)
        sizePolicy14.setVerticalStretch(0)
        sizePolicy14.setHeightForWidth(self.label_86.sizePolicy().hasHeightForWidth())
        self.label_86.setSizePolicy(sizePolicy14)

        self.gridLayout_96.addWidget(self.label_86, 0, 11, 1, 1)

        self.chk_all_serv_ripso = QCheckBox(self.tab_table_serv)
        self.chk_all_serv_ripso.setObjectName(u"chk_all_serv_ripso")
        self.chk_all_serv_ripso.setChecked(True)

        self.gridLayout_96.addWidget(self.chk_all_serv_ripso, 1, 8, 1, 1)

        self.label_85 = QLabel(self.tab_table_serv)
        self.label_85.setObjectName(u"label_85")
        sizePolicy7.setHeightForWidth(self.label_85.sizePolicy().hasHeightForWidth())
        self.label_85.setSizePolicy(sizePolicy7)
        self.label_85.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_96.addWidget(self.label_85, 1, 1, 1, 1)

        self.btn_goto_client_2 = QPushButton(self.tab_table_serv)
        self.btn_goto_client_2.setObjectName(u"btn_goto_client_2")

        self.gridLayout_96.addWidget(self.btn_goto_client_2, 1, 12, 1, 1)

        self.label_88 = QLabel(self.tab_table_serv)
        self.label_88.setObjectName(u"label_88")

        self.gridLayout_96.addWidget(self.label_88, 1, 3, 1, 1)

        self.de_contracts = QDateTimeEdit(self.tab_table_serv)
        self.de_contracts.setObjectName(u"de_contracts")
        self.de_contracts.setReadOnly(True)

        self.gridLayout_96.addWidget(self.de_contracts, 1, 5, 1, 1)

        self.cbx_1_ui_select_fiolist__4 = myQComboBox(self.tab_table_serv)
        self.cbx_1_ui_select_fiolist__4.setObjectName(u"cbx_1_ui_select_fiolist__4")
        sizePolicy4.setHeightForWidth(self.cbx_1_ui_select_fiolist__4.sizePolicy().hasHeightForWidth())
        self.cbx_1_ui_select_fiolist__4.setSizePolicy(sizePolicy4)
        self.cbx_1_ui_select_fiolist__4.setMinimumSize(QSize(150, 0))
        self.cbx_1_ui_select_fiolist__4.setEditable(True)

        self.gridLayout_96.addWidget(self.cbx_1_ui_select_fiolist__4, 0, 12, 1, 1)

        self.cbx_1__dep_has_client__4 = myQComboBox(self.tab_table_serv)
        self.cbx_1__dep_has_client__4.setObjectName(u"cbx_1__dep_has_client__4")
        sizePolicy6.setHeightForWidth(self.cbx_1__dep_has_client__4.sizePolicy().hasHeightForWidth())
        self.cbx_1__dep_has_client__4.setSizePolicy(sizePolicy6)
        self.cbx_1__dep_has_client__4.setEditable(True)
        self.cbx_1__dep_has_client__4.setMaxVisibleItems(20)

        self.gridLayout_96.addWidget(self.cbx_1__dep_has_client__4, 0, 2, 1, 9)

        self.pushButton_4 = QPushButton(self.tab_table_serv)
        self.pushButton_4.setObjectName(u"pushButton_4")

        self.gridLayout_96.addWidget(self.pushButton_4, 1, 11, 1, 1)

        self.tableViewYear = tsQTableViewYear(self.tab_table_serv)
        self.tableViewYear.setObjectName(u"tableViewYear")

        self.gridLayout_96.addWidget(self.tableViewYear, 2, 1, 1, 13)

        self.tabs_add_serv.addTab(self.tab_table_serv, "")

        self.verticalLayout_18.addWidget(self.tabs_add_serv)

        self.tabMain.addTab(self.tab_add_serv, "")
        self.tab_fio_dep = myQWidget()
        self.tab_fio_dep.setObjectName(u"tab_fio_dep")
        sizePolicy15 = QSizePolicy(QSizePolicy.Ignored, QSizePolicy.Preferred)
        sizePolicy15.setHorizontalStretch(0)
        sizePolicy15.setVerticalStretch(0)
        sizePolicy15.setHeightForWidth(self.tab_fio_dep.sizePolicy().hasHeightForWidth())
        self.tab_fio_dep.setSizePolicy(sizePolicy15)
        self.gridLayout_37 = QGridLayout(self.tab_fio_dep)
        self.gridLayout_37.setObjectName(u"gridLayout_37")
        self.tabs_fio_dep = myQTabWidget(self.tab_fio_dep)
        self.tabs_fio_dep.setObjectName(u"tabs_fio_dep")
        self.tab_people_of_dep = myQWidget()
        self.tab_people_of_dep.setObjectName(u"tab_people_of_dep")
        self.verticalLayout_36 = QVBoxLayout(self.tab_people_of_dep)
        self.verticalLayout_36.setObjectName(u"verticalLayout_36")
        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.btn_upd_fio_list = QPushButton(self.tab_people_of_dep)
        self.btn_upd_fio_list.setObjectName(u"btn_upd_fio_list")
        self.btn_upd_fio_list.setBaseSize(QSize(0, 0))

        self.gridLayout.addWidget(self.btn_upd_fio_list, 1, 0, 1, 1)

        self.pushButton_2 = QPushButton(self.tab_people_of_dep)
        self.pushButton_2.setObjectName(u"pushButton_2")

        self.gridLayout.addWidget(self.pushButton_2, 1, 1, 1, 1)

        self.btn_goto_serv_from_list = QPushButton(self.tab_people_of_dep)
        self.btn_goto_serv_from_list.setObjectName(u"btn_goto_serv_from_list")

        self.gridLayout.addWidget(self.btn_goto_serv_from_list, 1, 3, 1, 1)

        self.btn_goto_client_from_list = QPushButton(self.tab_people_of_dep)
        self.btn_goto_client_from_list.setObjectName(u"btn_goto_client_from_list")

        self.gridLayout.addWidget(self.btn_goto_client_from_list, 1, 2, 1, 1)


        self.verticalLayout_36.addLayout(self.gridLayout)

        self.table__dep_has_client__by_client = myQTableView(self.tab_people_of_dep)
        self.table__dep_has_client__by_client.setObjectName(u"table__dep_has_client__by_client")
        self.table__dep_has_client__by_client.setEnabled(True)
        self.table__dep_has_client__by_client.setDragEnabled(True)
        self.table__dep_has_client__by_client.setSortingEnabled(True)
        self.table__dep_has_client__by_client.verticalHeader().setProperty("showSortIndicator", True)

        self.verticalLayout_36.addWidget(self.table__dep_has_client__by_client)

        self.tabs_fio_dep.addTab(self.tab_people_of_dep, "")
        self.tab_33 = myQWidget()
        self.tab_33.setObjectName(u"tab_33")
        self.gridLayout_91 = QGridLayout(self.tab_33)
        self.gridLayout_91.setObjectName(u"gridLayout_91")
        self.table__dep_has_new_client__by_client_2 = myQTableView(self.tab_33)
        self.table__dep_has_new_client__by_client_2.setObjectName(u"table__dep_has_new_client__by_client_2")

        self.gridLayout_91.addWidget(self.table__dep_has_new_client__by_client_2, 0, 0, 1, 1)

        self.tabs_fio_dep.addTab(self.tab_33, "")
        self.tab_53 = myQWidget()
        self.tab_53.setObjectName(u"tab_53")
        self.gridLayout_90 = QGridLayout(self.tab_53)
        self.gridLayout_90.setObjectName(u"gridLayout_90")
        self.table__dep_has_client_count_main_year__by_client = myQTableView(self.tab_53)
        self.table__dep_has_client_count_main_year__by_client.setObjectName(u"table__dep_has_client_count_main_year__by_client")

        self.gridLayout_90.addWidget(self.table__dep_has_client_count_main_year__by_client, 0, 0, 1, 1)

        self.tabs_fio_dep.addTab(self.tab_53, "")
        self.tab_55 = myQWidget()
        self.tab_55.setObjectName(u"tab_55")
        self.gridLayout_93 = QGridLayout(self.tab_55)
        self.gridLayout_93.setObjectName(u"gridLayout_93")
        self.table__dep_has_client_blocked_in_year__by_client_2 = myQTableView(self.tab_55)
        self.table__dep_has_client_blocked_in_year__by_client_2.setObjectName(u"table__dep_has_client_blocked_in_year__by_client_2")
        self.table__dep_has_client_blocked_in_year__by_client_2.setEnabled(True)
        self.table__dep_has_client_blocked_in_year__by_client_2.setDragEnabled(True)
        self.table__dep_has_client_blocked_in_year__by_client_2.setSortingEnabled(True)
        self.table__dep_has_client_blocked_in_year__by_client_2.verticalHeader().setProperty("showSortIndicator", True)

        self.gridLayout_93.addWidget(self.table__dep_has_client_blocked_in_year__by_client_2, 0, 0, 1, 1)

        self.tabs_fio_dep.addTab(self.tab_55, "")
        self.tab_40 = myQWidget()
        self.tab_40.setObjectName(u"tab_40")
        self.verticalLayout_37 = QVBoxLayout(self.tab_40)
        self.verticalLayout_37.setObjectName(u"verticalLayout_37")
        self.table__dep_has_client_ending__by_client = myQTableView(self.tab_40)
        self.table__dep_has_client_ending__by_client.setObjectName(u"table__dep_has_client_ending__by_client")

        self.verticalLayout_37.addWidget(self.table__dep_has_client_ending__by_client)

        self.tabs_fio_dep.addTab(self.tab_40, "")
        self.tab_39 = myQWidget()
        self.tab_39.setObjectName(u"tab_39")
        self.verticalLayout_38 = QVBoxLayout(self.tab_39)
        self.verticalLayout_38.setObjectName(u"verticalLayout_38")
        self.table__dep_has_client_ended__by_client = myQTableView(self.tab_39)
        self.table__dep_has_client_ended__by_client.setObjectName(u"table__dep_has_client_ended__by_client")

        self.verticalLayout_38.addWidget(self.table__dep_has_client_ended__by_client)

        self.tabs_fio_dep.addTab(self.tab_39, "")
        self.tab__dep_has_client_more = myQWidget()
        self.tab__dep_has_client_more.setObjectName(u"tab__dep_has_client_more")
        self.verticalLayout_39 = QVBoxLayout(self.tab__dep_has_client_more)
        self.verticalLayout_39.setObjectName(u"verticalLayout_39")
        self.table__dep_has_client_more__by_client = myQTableView(self.tab__dep_has_client_more)
        self.table__dep_has_client_more__by_client.setObjectName(u"table__dep_has_client_more__by_client")

        self.verticalLayout_39.addWidget(self.table__dep_has_client_more__by_client)

        self.tabs_fio_dep.addTab(self.tab__dep_has_client_more, "")

        self.gridLayout_37.addWidget(self.tabs_fio_dep, 2, 0, 1, 2)

        self.label_fio_filter = QLabel(self.tab_fio_dep)
        self.label_fio_filter.setObjectName(u"label_fio_filter")

        self.gridLayout_37.addWidget(self.label_fio_filter, 1, 0, 1, 1)

        self.qle_fio_filter = myQLineEdit(self.tab_fio_dep)
        self.qle_fio_filter.setObjectName(u"qle_fio_filter")

        self.gridLayout_37.addWidget(self.qle_fio_filter, 1, 1, 1, 1)

        self.tabMain.addTab(self.tab_fio_dep, "")
        self.tab_clients = myQWidget()
        self.tab_clients.setObjectName(u"tab_clients")
        self.verticalLayout_2 = QVBoxLayout(self.tab_clients)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.gridLayout_9 = QGridLayout()
        self.gridLayout_9.setObjectName(u"gridLayout_9")
        self.qle_table_client_filter = myQLineEdit(self.tab_clients)
        self.qle_table_client_filter.setObjectName(u"qle_table_client_filter")

        self.gridLayout_9.addWidget(self.qle_table_client_filter, 0, 1, 1, 1)

        self.label_client = QLabel(self.tab_clients)
        self.label_client.setObjectName(u"label_client")

        self.gridLayout_9.addWidget(self.label_client, 0, 0, 1, 1)


        self.verticalLayout_2.addLayout(self.gridLayout_9)

        self.horizontalLayout_11 = QHBoxLayout()
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.pushButton_7 = QPushButton(self.tab_clients)
        self.pushButton_7.setObjectName(u"pushButton_7")

        self.horizontalLayout_11.addWidget(self.pushButton_7)

        self.pushButton_15 = QPushButton(self.tab_clients)
        self.pushButton_15.setObjectName(u"pushButton_15")

        self.horizontalLayout_11.addWidget(self.pushButton_15)


        self.verticalLayout_2.addLayout(self.horizontalLayout_11)

        self.gridLayout_2 = QGridLayout()
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.tabs_client2 = myQTabWidget(self.tab_clients)
        self.tabs_client2.setObjectName(u"tabs_client2")
        self.tab_35 = myQWidget()
        self.tab_35.setObjectName(u"tab_35")
        self.verticalLayout_35 = QVBoxLayout(self.tab_35)
        self.verticalLayout_35.setObjectName(u"verticalLayout_35")
        self.table_client__by_client = myQTableView(self.tab_35)
        self.table_client__by_client.setObjectName(u"table_client__by_client")

        self.verticalLayout_35.addWidget(self.table_client__by_client)

        self.tabs_client2.addTab(self.tab_35, "")
        self.tab_15 = myQWidget()
        self.tab_15.setObjectName(u"tab_15")
        self.verticalLayout_9 = QVBoxLayout(self.tab_15)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.gridLayout_6 = QGridLayout()
        self.gridLayout_6.setObjectName(u"gridLayout_6")
        self.table__client_has_valid_contracts__by_client = myQTableView(self.tab_15)
        self.table__client_has_valid_contracts__by_client.setObjectName(u"table__client_has_valid_contracts__by_client")

        self.gridLayout_6.addWidget(self.table__client_has_valid_contracts__by_client, 0, 0, 1, 1)


        self.verticalLayout_9.addLayout(self.gridLayout_6)

        self.tabs_client2.addTab(self.tab_15, "")
        self.tab = myQWidget()
        self.tab.setObjectName(u"tab")
        self.horizontalLayout_8 = QHBoxLayout(self.tab)
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.table__dep_has_client_by_ripso__by_client = myQTableView(self.tab)
        self.table__dep_has_client_by_ripso__by_client.setObjectName(u"table__dep_has_client_by_ripso__by_client")

        self.horizontalLayout_8.addWidget(self.table__dep_has_client_by_ripso__by_client)

        self.tabs_client2.addTab(self.tab, "")
        self.tab_36 = myQWidget()
        self.tab_36.setObjectName(u"tab_36")
        self.gridLayout_98 = QGridLayout(self.tab_36)
        self.gridLayout_98.setObjectName(u"gridLayout_98")
        self.table__client_has_invalid_contracts__by_client = myQTableView(self.tab_36)
        self.table__client_has_invalid_contracts__by_client.setObjectName(u"table__client_has_invalid_contracts__by_client")

        self.gridLayout_98.addWidget(self.table__client_has_invalid_contracts__by_client, 1, 0, 1, 1)

        self.tabs_client2.addTab(self.tab_36, "")

        self.gridLayout_2.addWidget(self.tabs_client2, 1, 0, 1, 1)


        self.verticalLayout_2.addLayout(self.gridLayout_2)

        self.tabMain.addTab(self.tab_clients, "")
        self.tab_client = myQWidget()
        self.tab_client.setObjectName(u"tab_client")
        self.verticalLayout_30 = QVBoxLayout(self.tab_client)
        self.verticalLayout_30.setObjectName(u"verticalLayout_30")
        self.horizontalLayout_13 = QHBoxLayout()
        self.horizontalLayout_13.setObjectName(u"horizontalLayout_13")

        self.verticalLayout_30.addLayout(self.horizontalLayout_13)

        self.horizontalLayout_7 = QHBoxLayout()
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.btn_goto_serv_add = QToolButton(self.tab_client)
        self.btn_goto_serv_add.setObjectName(u"btn_goto_serv_add")

        self.horizontalLayout_7.addWidget(self.btn_goto_serv_add)

        self.label_21 = QLabel(self.tab_client)
        self.label_21.setObjectName(u"label_21")
        sizePolicy14.setHeightForWidth(self.label_21.sizePolicy().hasHeightForWidth())
        self.label_21.setSizePolicy(sizePolicy14)

        self.horizontalLayout_7.addWidget(self.label_21)

        self.btn_prev = QPushButton(self.tab_client)
        self.btn_prev.setObjectName(u"btn_prev")

        self.horizontalLayout_7.addWidget(self.btn_prev)

        self.cbx_1__dep_has_client = QComboBoxWithDataMapper(self.tab_client)
        self.cbx_1__dep_has_client.setObjectName(u"cbx_1__dep_has_client")
        sizePolicy6.setHeightForWidth(self.cbx_1__dep_has_client.sizePolicy().hasHeightForWidth())
        self.cbx_1__dep_has_client.setSizePolicy(sizePolicy6)
        self.cbx_1__dep_has_client.setEditable(True)

        self.horizontalLayout_7.addWidget(self.cbx_1__dep_has_client)

        self.btn_next = QPushButton(self.tab_client)
        self.btn_next.setObjectName(u"btn_next")

        self.horizontalLayout_7.addWidget(self.btn_next)

        self.label_23 = QLabel(self.tab_client)
        self.label_23.setObjectName(u"label_23")
        sizePolicy14.setHeightForWidth(self.label_23.sizePolicy().hasHeightForWidth())
        self.label_23.setSizePolicy(sizePolicy14)

        self.horizontalLayout_7.addWidget(self.label_23)

        self.cbx_1_ui_select_fiolist__2 = myQComboBox(self.tab_client)
        self.cbx_1_ui_select_fiolist__2.setObjectName(u"cbx_1_ui_select_fiolist__2")
        sizePolicy4.setHeightForWidth(self.cbx_1_ui_select_fiolist__2.sizePolicy().hasHeightForWidth())
        self.cbx_1_ui_select_fiolist__2.setSizePolicy(sizePolicy4)
        self.cbx_1_ui_select_fiolist__2.setMinimumSize(QSize(250, 0))

        self.horizontalLayout_7.addWidget(self.cbx_1_ui_select_fiolist__2)


        self.verticalLayout_30.addLayout(self.horizontalLayout_7)

        self.tabs_client = myQTabWidget(self.tab_client)
        self.tabs_client.setObjectName(u"tabs_client")
        self.tab_people_main = myQWidget()
        self.tab_people_main.setObjectName(u"tab_people_main")
        self.verticalLayout_13 = QVBoxLayout(self.tab_people_main)
        self.verticalLayout_13.setObjectName(u"verticalLayout_13")
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.groupBox = QGroupBox(self.tab_people_main)
        self.groupBox.setObjectName(u"groupBox")
        sizePolicy16 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy16.setHorizontalStretch(0)
        sizePolicy16.setVerticalStretch(0)
        sizePolicy16.setHeightForWidth(self.groupBox.sizePolicy().hasHeightForWidth())
        self.groupBox.setSizePolicy(sizePolicy16)
        self.groupBox.setFont(font)
        self.gridLayout_22 = QGridLayout(self.groupBox)
        self.gridLayout_22.setObjectName(u"gridLayout_22")
        self.groupBox_2 = QGroupBox(self.groupBox)
        self.groupBox_2.setObjectName(u"groupBox_2")
        sizePolicy17 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy17.setHorizontalStretch(0)
        sizePolicy17.setVerticalStretch(8)
        sizePolicy17.setHeightForWidth(self.groupBox_2.sizePolicy().hasHeightForWidth())
        self.groupBox_2.setSizePolicy(sizePolicy17)
        font2 = QFont()
        font2.setBold(False)
        font2.setWeight(50)
        self.groupBox_2.setFont(font2)
        self.verticalLayout_14 = QVBoxLayout(self.groupBox_2)
        self.verticalLayout_14.setObjectName(u"verticalLayout_14")
        self.table__client_has_add_info__where_client_id__by_client_id = myQTableView(self.groupBox_2)
        self.table__client_has_add_info__where_client_id__by_client_id.setObjectName(u"table__client_has_add_info__where_client_id__by_client_id")
        sizePolicy.setHeightForWidth(self.table__client_has_add_info__where_client_id__by_client_id.sizePolicy().hasHeightForWidth())
        self.table__client_has_add_info__where_client_id__by_client_id.setSizePolicy(sizePolicy)
        self.table__client_has_add_info__where_client_id__by_client_id.setMinimumSize(QSize(0, 0))

        self.verticalLayout_14.addWidget(self.table__client_has_add_info__where_client_id__by_client_id)


        self.gridLayout_22.addWidget(self.groupBox_2, 1, 0, 1, 1)

        self.groupBox_3 = QGroupBox(self.groupBox)
        self.groupBox_3.setObjectName(u"groupBox_3")
        sizePolicy18 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy18.setHorizontalStretch(0)
        sizePolicy18.setVerticalStretch(1)
        sizePolicy18.setHeightForWidth(self.groupBox_3.sizePolicy().hasHeightForWidth())
        self.groupBox_3.setSizePolicy(sizePolicy18)
        self.verticalLayout_15 = QVBoxLayout(self.groupBox_3)
        self.verticalLayout_15.setObjectName(u"verticalLayout_15")
        self.gridLayout_8 = QGridLayout()
        self.gridLayout_8.setObjectName(u"gridLayout_8")
        self.qle_FIO = QLineEdit(self.groupBox_3)
        self.qle_FIO.setObjectName(u"qle_FIO")

        self.gridLayout_8.addWidget(self.qle_FIO, 0, 1, 1, 1)

        self.label_22 = QLabel(self.groupBox_3)
        self.label_22.setObjectName(u"label_22")

        self.gridLayout_8.addWidget(self.label_22, 0, 0, 1, 1)

        self.gridLayout_10 = QGridLayout()
        self.gridLayout_10.setObjectName(u"gridLayout_10")
        self.label_27 = QLabel(self.groupBox_3)
        self.label_27.setObjectName(u"label_27")
        self.label_27.setMinimumSize(QSize(130, 0))
        self.label_27.setFont(font2)
        self.label_27.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_10.addWidget(self.label_27, 0, 5, 1, 1)

        self.dateEdit_death = QDateEdit(self.groupBox_3)
        self.dateEdit_death.setObjectName(u"dateEdit_death")
        sizePolicy.setHeightForWidth(self.dateEdit_death.sizePolicy().hasHeightForWidth())
        self.dateEdit_death.setSizePolicy(sizePolicy)
        self.dateEdit_death.setFont(font2)

        self.gridLayout_10.addWidget(self.dateEdit_death, 0, 6, 1, 1)

        self.label_49 = QLabel(self.groupBox_3)
        self.label_49.setObjectName(u"label_49")
        sizePolicy15.setHeightForWidth(self.label_49.sizePolicy().hasHeightForWidth())
        self.label_49.setSizePolicy(sizePolicy15)
        self.label_49.setFont(font2)
        self.label_49.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_10.addWidget(self.label_49, 1, 2, 1, 1)

        self.label_24 = QLabel(self.groupBox_3)
        self.label_24.setObjectName(u"label_24")
        self.label_24.setFont(font2)

        self.gridLayout_10.addWidget(self.label_24, 0, 0, 1, 1)

        self.label_25 = QLabel(self.groupBox_3)
        self.label_25.setObjectName(u"label_25")
        sizePolicy16.setHeightForWidth(self.label_25.sizePolicy().hasHeightForWidth())
        self.label_25.setSizePolicy(sizePolicy16)
        self.label_25.setMinimumSize(QSize(130, 0))
        self.label_25.setFont(font2)
        self.label_25.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_10.addWidget(self.label_25, 0, 2, 1, 1)

        self.label_50 = QLabel(self.groupBox_3)
        self.label_50.setObjectName(u"label_50")
        self.label_50.setFont(font2)

        self.gridLayout_10.addWidget(self.label_50, 1, 0, 1, 1)

        self.lineEdit_phone = QLineEdit(self.groupBox_3)
        self.lineEdit_phone.setObjectName(u"lineEdit_phone")
        self.lineEdit_phone.setFont(font2)

        self.gridLayout_10.addWidget(self.lineEdit_phone, 1, 3, 1, 2)

        self.dateEdit_birth = QDateEdit(self.groupBox_3)
        self.dateEdit_birth.setObjectName(u"dateEdit_birth")
        self.dateEdit_birth.setFont(font2)

        self.gridLayout_10.addWidget(self.dateEdit_birth, 0, 3, 1, 2)

        self.qle_SNILS = QLineEdit(self.groupBox_3)
        self.qle_SNILS.setObjectName(u"qle_SNILS")
        sizePolicy4.setHeightForWidth(self.qle_SNILS.sizePolicy().hasHeightForWidth())
        self.qle_SNILS.setSizePolicy(sizePolicy4)
        self.qle_SNILS.setFont(font2)

        self.gridLayout_10.addWidget(self.qle_SNILS, 1, 1, 1, 1)

        self.sp_ESRN = QSpinBox(self.groupBox_3)
        self.sp_ESRN.setObjectName(u"sp_ESRN")
        self.sp_ESRN.setFont(font2)
        self.sp_ESRN.setButtonSymbols(QAbstractSpinBox.NoButtons)
        self.sp_ESRN.setProperty("showGroupSeparator", True)
        self.sp_ESRN.setMaximum(999999999)

        self.gridLayout_10.addWidget(self.sp_ESRN, 0, 1, 1, 1)


        self.gridLayout_8.addLayout(self.gridLayout_10, 1, 1, 1, 1)

        self.pte_note = QPlainTextEdit(self.groupBox_3)
        self.pte_note.setObjectName(u"pte_note")
        sizePolicy12.setHeightForWidth(self.pte_note.sizePolicy().hasHeightForWidth())
        self.pte_note.setSizePolicy(sizePolicy12)
        self.pte_note.setMinimumSize(QSize(0, 60))
        self.pte_note.setBaseSize(QSize(0, 0))
        self.pte_note.setFont(font2)

        self.gridLayout_8.addWidget(self.pte_note, 2, 1, 1, 1)

        self.label_52 = QLabel(self.groupBox_3)
        self.label_52.setObjectName(u"label_52")
        self.label_52.setFont(font2)

        self.gridLayout_8.addWidget(self.label_52, 2, 0, 1, 1)


        self.verticalLayout_15.addLayout(self.gridLayout_8)


        self.gridLayout_22.addWidget(self.groupBox_3, 0, 0, 1, 1)


        self.verticalLayout.addWidget(self.groupBox)


        self.verticalLayout_13.addLayout(self.verticalLayout)

        self.tabs_client.addTab(self.tab_people_main, "")
        self.tab_pcat = myQWidget()
        self.tab_pcat.setObjectName(u"tab_pcat")
        self.verticalLayout_31 = QVBoxLayout(self.tab_pcat)
        self.verticalLayout_31.setObjectName(u"verticalLayout_31")
        self.gridLayout_18 = QGridLayout()
        self.gridLayout_18.setObjectName(u"gridLayout_18")
        self.table_client_has_category__by_client_id = myQTableView(self.tab_pcat)
        self.table_client_has_category__by_client_id.setObjectName(u"table_client_has_category__by_client_id")

        self.gridLayout_18.addWidget(self.table_client_has_category__by_client_id, 1, 1, 1, 1)

        self.label_54 = QLabel(self.tab_pcat)
        self.label_54.setObjectName(u"label_54")

        self.gridLayout_18.addWidget(self.label_54, 0, 0, 1, 1)

        self.label_83 = QLabel(self.tab_pcat)
        self.label_83.setObjectName(u"label_83")
        self.label_83.setTextFormat(Qt.RichText)

        self.gridLayout_18.addWidget(self.label_83, 1, 0, 1, 1)


        self.verticalLayout_31.addLayout(self.gridLayout_18)

        self.tabs_client.addTab(self.tab_pcat, "")
        self.tab_client_contr = myQWidget()
        self.tab_client_contr.setObjectName(u"tab_client_contr")
        self.verticalLayout_34 = QVBoxLayout(self.tab_client_contr)
        self.verticalLayout_34.setObjectName(u"verticalLayout_34")
        self.gridLayout_25 = QGridLayout()
        self.gridLayout_25.setObjectName(u"gridLayout_25")
        self.label_60 = QLabel(self.tab_client_contr)
        self.label_60.setObjectName(u"label_60")
        self.label_60.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_25.addWidget(self.label_60, 0, 5, 1, 1)

        self.label_59 = QLabel(self.tab_client_contr)
        self.label_59.setObjectName(u"label_59")
        self.label_59.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_25.addWidget(self.label_59, 1, 11, 1, 1)

        self.horizontalLayout_24 = QHBoxLayout()
        self.horizontalLayout_24.setObjectName(u"horizontalLayout_24")
        self.chk_to_recheck = QCheckBox(self.tab_client_contr)
        self.chk_to_recheck.setObjectName(u"chk_to_recheck")
        sizePolicy3.setHeightForWidth(self.chk_to_recheck.sizePolicy().hasHeightForWidth())
        self.chk_to_recheck.setSizePolicy(sizePolicy3)

        self.horizontalLayout_24.addWidget(self.chk_to_recheck)

        self.dte_check_date = QDateTimeEdit(self.tab_client_contr)
        self.dte_check_date.setObjectName(u"dte_check_date")
        self.dte_check_date.setEnabled(True)
        sizePolicy3.setHeightForWidth(self.dte_check_date.sizePolicy().hasHeightForWidth())
        self.dte_check_date.setSizePolicy(sizePolicy3)
        self.dte_check_date.setReadOnly(True)

        self.horizontalLayout_24.addWidget(self.dte_check_date)

        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_24.addItem(self.horizontalSpacer_3)


        self.gridLayout_25.addLayout(self.horizontalLayout_24, 0, 7, 1, 6)

        self.cbx_0__dep_has_ripso = QComboBox(self.tab_client_contr)
        self.cbx_0__dep_has_ripso.setObjectName(u"cbx_0__dep_has_ripso")
        self.cbx_0__dep_has_ripso.setEditable(True)

        self.gridLayout_25.addWidget(self.cbx_0__dep_has_ripso, 1, 12, 1, 1)

        self.label_55 = QLabel(self.tab_client_contr)
        self.label_55.setObjectName(u"label_55")
        sizePolicy7.setHeightForWidth(self.label_55.sizePolicy().hasHeightForWidth())
        self.label_55.setSizePolicy(sizePolicy7)
        self.label_55.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_25.addWidget(self.label_55, 1, 5, 1, 1)

        self.groupBox_7 = QGroupBox(self.tab_client_contr)
        self.groupBox_7.setObjectName(u"groupBox_7")
        self.groupBox_7.setFlat(False)
        self.horizontalLayout_15 = QHBoxLayout(self.groupBox_7)
        self.horizontalLayout_15.setObjectName(u"horizontalLayout_15")
        self.label_62 = QLabel(self.groupBox_7)
        self.label_62.setObjectName(u"label_62")
        self.label_62.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.horizontalLayout_15.addWidget(self.label_62)

        self.btn_prev_2 = QPushButton(self.groupBox_7)
        self.btn_prev_2.setObjectName(u"btn_prev_2")
        sizePolicy3.setHeightForWidth(self.btn_prev_2.sizePolicy().hasHeightForWidth())
        self.btn_prev_2.setSizePolicy(sizePolicy3)

        self.horizontalLayout_15.addWidget(self.btn_prev_2)

        self.cbx_1_contracts__by_client_id = QComboBoxWithDataMapper(self.groupBox_7)
        self.cbx_1_contracts__by_client_id.setObjectName(u"cbx_1_contracts__by_client_id")
        sizePolicy6.setHeightForWidth(self.cbx_1_contracts__by_client_id.sizePolicy().hasHeightForWidth())
        self.cbx_1_contracts__by_client_id.setSizePolicy(sizePolicy6)
        self.cbx_1_contracts__by_client_id.setEditable(True)
        self.cbx_1_contracts__by_client_id.setProperty("sort_order", 1)

        self.horizontalLayout_15.addWidget(self.cbx_1_contracts__by_client_id)

        self.btn_next_2 = QPushButton(self.groupBox_7)
        self.btn_next_2.setObjectName(u"btn_next_2")
        sizePolicy3.setHeightForWidth(self.btn_next_2.sizePolicy().hasHeightForWidth())
        self.btn_next_2.setSizePolicy(sizePolicy3)

        self.horizontalLayout_15.addWidget(self.btn_next_2)


        self.gridLayout_25.addWidget(self.groupBox_7, 0, 0, 2, 5)

        self.pte_contracts_note = QPlainTextEdit(self.tab_client_contr)
        self.pte_contracts_note.setObjectName(u"pte_contracts_note")
        sizePolicy19 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Ignored)
        sizePolicy19.setHorizontalStretch(0)
        sizePolicy19.setVerticalStretch(0)
        sizePolicy19.setHeightForWidth(self.pte_contracts_note.sizePolicy().hasHeightForWidth())
        self.pte_contracts_note.setSizePolicy(sizePolicy19)
        self.pte_contracts_note.setMinimumSize(QSize(0, 0))

        self.gridLayout_25.addWidget(self.pte_contracts_note, 2, 1, 2, 4)

        self.label_56 = QLabel(self.tab_client_contr)
        self.label_56.setObjectName(u"label_56")
        sizePolicy5.setHeightForWidth(self.label_56.sizePolicy().hasHeightForWidth())
        self.label_56.setSizePolicy(sizePolicy5)
        self.label_56.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_25.addWidget(self.label_56, 2, 5, 1, 1)

        self.label_61 = QLabel(self.tab_client_contr)
        self.label_61.setObjectName(u"label_61")
        sizePolicy7.setHeightForWidth(self.label_61.sizePolicy().hasHeightForWidth())
        self.label_61.setSizePolicy(sizePolicy7)
        self.label_61.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_25.addWidget(self.label_61, 2, 0, 1, 1)

        self.tab_sub_client = myQTabWidget(self.tab_client_contr)
        self.tab_sub_client.setObjectName(u"tab_sub_client")
        self.tab_contract_planned = myQWidget()
        self.tab_contract_planned.setObjectName(u"tab_contract_planned")
        self.verticalLayout_40 = QVBoxLayout(self.tab_contract_planned)
        self.verticalLayout_40.setObjectName(u"verticalLayout_40")
        self.widget_14 = QWidget(self.tab_contract_planned)
        self.widget_14.setObjectName(u"widget_14")
        self.horizontalLayout_28 = QHBoxLayout(self.widget_14)
        self.horizontalLayout_28.setObjectName(u"horizontalLayout_28")
        self.horizontalLayout_6 = QHBoxLayout()
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.btn_paste_planned = QPushButton(self.widget_14)
        self.btn_paste_planned.setObjectName(u"btn_paste_planned")
        self.btn_paste_planned.setFont(font)

        self.horizontalLayout_6.addWidget(self.btn_paste_planned)

        self.pushButton = QPushButton(self.widget_14)
        self.pushButton.setObjectName(u"pushButton")
        sizePolicy20 = QSizePolicy(QSizePolicy.Maximum, QSizePolicy.Fixed)
        sizePolicy20.setHorizontalStretch(0)
        sizePolicy20.setVerticalStretch(0)
        sizePolicy20.setHeightForWidth(self.pushButton.sizePolicy().hasHeightForWidth())
        self.pushButton.setSizePolicy(sizePolicy20)

        self.horizontalLayout_6.addWidget(self.pushButton)


        self.horizontalLayout_28.addLayout(self.horizontalLayout_6)


        self.verticalLayout_40.addWidget(self.widget_14)

        self.table__contracts_has_serv__where_contracts_id__by_contracts_id = myQTableView(self.tab_contract_planned)
        self.table__contracts_has_serv__where_contracts_id__by_contracts_id.setObjectName(u"table__contracts_has_serv__where_contracts_id__by_contracts_id")
        sizePolicy21 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Expanding)
        sizePolicy21.setHorizontalStretch(0)
        sizePolicy21.setVerticalStretch(0)
        sizePolicy21.setHeightForWidth(self.table__contracts_has_serv__where_contracts_id__by_contracts_id.sizePolicy().hasHeightForWidth())
        self.table__contracts_has_serv__where_contracts_id__by_contracts_id.setSizePolicy(sizePolicy21)

        self.verticalLayout_40.addWidget(self.table__contracts_has_serv__where_contracts_id__by_contracts_id)

        self.tab_sub_client.addTab(self.tab_contract_planned, "")
        self.tab_43 = myQWidget()
        self.tab_43.setObjectName(u"tab_43")
        self.verticalLayout_41 = QVBoxLayout(self.tab_43)
        self.verticalLayout_41.setObjectName(u"verticalLayout_41")
        self.table_main__where_client_id__by_contracts_id = myQTableView(self.tab_43)
        self.table_main__where_client_id__by_contracts_id.setObjectName(u"table_main__where_client_id__by_contracts_id")

        self.verticalLayout_41.addWidget(self.table_main__where_client_id__by_contracts_id)

        self.tab_sub_client.addTab(self.tab_43, "")
        self.tab_54 = myQWidget()
        self.tab_54.setObjectName(u"tab_54")
        self.gridLayout_92 = QGridLayout(self.tab_54)
        self.gridLayout_92.setObjectName(u"gridLayout_92")
        self.table__client_has_add_info__where_client_id__by_contracts_id = add_info_QTableView(self.tab_54)
        self.table__client_has_add_info__where_client_id__by_contracts_id.setObjectName(u"table__client_has_add_info__where_client_id__by_contracts_id")
        sizePolicy.setHeightForWidth(self.table__client_has_add_info__where_client_id__by_contracts_id.sizePolicy().hasHeightForWidth())
        self.table__client_has_add_info__where_client_id__by_contracts_id.setSizePolicy(sizePolicy)
        self.table__client_has_add_info__where_client_id__by_contracts_id.setMinimumSize(QSize(0, 0))

        self.gridLayout_92.addWidget(self.table__client_has_add_info__where_client_id__by_contracts_id, 0, 0, 1, 1)

        self.tab_sub_client.addTab(self.tab_54, "")

        self.gridLayout_25.addWidget(self.tab_sub_client, 4, 0, 1, 13)

        self.cbx_0_worker_has_dep = QComboBox(self.tab_client_contr)
        self.cbx_0_worker_has_dep.setObjectName(u"cbx_0_worker_has_dep")
        self.cbx_0_worker_has_dep.setEditable(True)

        self.gridLayout_25.addWidget(self.cbx_0_worker_has_dep, 3, 6, 1, 7)

        self.horizontalLayout_16 = QHBoxLayout()
        self.horizontalLayout_16.setObjectName(u"horizontalLayout_16")
        self.de_startdate = QDateEdit(self.tab_client_contr)
        self.de_startdate.setObjectName(u"de_startdate")
        sizePolicy22 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Ignored)
        sizePolicy22.setHorizontalStretch(0)
        sizePolicy22.setVerticalStretch(0)
        sizePolicy22.setHeightForWidth(self.de_startdate.sizePolicy().hasHeightForWidth())
        self.de_startdate.setSizePolicy(sizePolicy22)

        self.horizontalLayout_16.addWidget(self.de_startdate)

        self.label_57 = QLabel(self.tab_client_contr)
        self.label_57.setObjectName(u"label_57")
        sizePolicy5.setHeightForWidth(self.label_57.sizePolicy().hasHeightForWidth())
        self.label_57.setSizePolicy(sizePolicy5)
        self.label_57.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.horizontalLayout_16.addWidget(self.label_57)

        self.de_enddate = QDateEdit(self.tab_client_contr)
        self.de_enddate.setObjectName(u"de_enddate")
        sizePolicy8.setHeightForWidth(self.de_enddate.sizePolicy().hasHeightForWidth())
        self.de_enddate.setSizePolicy(sizePolicy8)

        self.horizontalLayout_16.addWidget(self.de_enddate)

        self.chk_blocked = QCheckBox(self.tab_client_contr)
        self.chk_blocked.setObjectName(u"chk_blocked")

        self.horizontalLayout_16.addWidget(self.chk_blocked)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_16.addItem(self.horizontalSpacer)


        self.gridLayout_25.addLayout(self.horizontalLayout_16, 2, 6, 1, 7)

        self.sp_ippsuNum = QSpinBox(self.tab_client_contr)
        self.sp_ippsuNum.setObjectName(u"sp_ippsuNum")
        self.sp_ippsuNum.setButtonSymbols(QAbstractSpinBox.NoButtons)
        self.sp_ippsuNum.setProperty("showGroupSeparator", True)
        self.sp_ippsuNum.setMaximum(999999999)
        self.sp_ippsuNum.setSingleStep(0)

        self.gridLayout_25.addWidget(self.sp_ippsuNum, 0, 6, 1, 1)

        self.label_58 = QLabel(self.tab_client_contr)
        self.label_58.setObjectName(u"label_58")
        sizePolicy5.setHeightForWidth(self.label_58.sizePolicy().hasHeightForWidth())
        self.label_58.setSizePolicy(sizePolicy5)
        self.label_58.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_25.addWidget(self.label_58, 3, 5, 1, 1)

        self.horizontalLayout_25 = QHBoxLayout()
        self.horizontalLayout_25.setObjectName(u"horizontalLayout_25")
        self.qle_contracts = myQLineEdit(self.tab_client_contr)
        self.qle_contracts.setObjectName(u"qle_contracts")
        sizePolicy23 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Maximum)
        sizePolicy23.setHorizontalStretch(0)
        sizePolicy23.setVerticalStretch(0)
        sizePolicy23.setHeightForWidth(self.qle_contracts.sizePolicy().hasHeightForWidth())
        self.qle_contracts.setSizePolicy(sizePolicy23)
        self.qle_contracts.setAlignment(Qt.AlignBottom|Qt.AlignLeading|Qt.AlignLeft)

        self.horizontalLayout_25.addWidget(self.qle_contracts)

        self.label_84 = QLabel(self.tab_client_contr)
        self.label_84.setObjectName(u"label_84")
        sizePolicy7.setHeightForWidth(self.label_84.sizePolicy().hasHeightForWidth())
        self.label_84.setSizePolicy(sizePolicy7)
        self.label_84.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.horizontalLayout_25.addWidget(self.label_84)

        self.qle_contracts2 = QLineEdit(self.tab_client_contr)
        self.qle_contracts2.setObjectName(u"qle_contracts2")
        sizePolicy6.setHeightForWidth(self.qle_contracts2.sizePolicy().hasHeightForWidth())
        self.qle_contracts2.setSizePolicy(sizePolicy6)
        self.qle_contracts2.setMinimumSize(QSize(0, 0))

        self.horizontalLayout_25.addWidget(self.qle_contracts2)


        self.gridLayout_25.addLayout(self.horizontalLayout_25, 1, 6, 1, 5)


        self.verticalLayout_34.addLayout(self.gridLayout_25)

        self.tabs_client.addTab(self.tab_client_contr, "")
        self.tab_2 = myQWidget()
        self.tab_2.setObjectName(u"tab_2")
        self.verticalLayout_33 = QVBoxLayout(self.tab_2)
        self.verticalLayout_33.setObjectName(u"verticalLayout_33")
        self.gridLayout_24 = QGridLayout()
        self.gridLayout_24.setObjectName(u"gridLayout_24")
        self.table_main__where_client_id__by_dep_id = myQTableView(self.tab_2)
        self.table_main__where_client_id__by_dep_id.setObjectName(u"table_main__where_client_id__by_dep_id")

        self.gridLayout_24.addWidget(self.table_main__where_client_id__by_dep_id, 0, 0, 1, 1)


        self.verticalLayout_33.addLayout(self.gridLayout_24)

        self.tabs_client.addTab(self.tab_2, "")
        self.tab_5 = myQWidget()
        self.tab_5.setObjectName(u"tab_5")
        self.gridLayout_97 = QGridLayout(self.tab_5)
        self.gridLayout_97.setObjectName(u"gridLayout_97")
        self.table_main__where_client_id = myQTableView(self.tab_5)
        self.table_main__where_client_id.setObjectName(u"table_main__where_client_id")

        self.gridLayout_97.addWidget(self.table_main__where_client_id, 0, 0, 1, 1)

        self.tabs_client.addTab(self.tab_5, "")

        self.verticalLayout_30.addWidget(self.tabs_client)

        self.tabMain.addTab(self.tab_client, "")
        self.tab_total = myQWidget()
        self.tab_total.setObjectName(u"tab_total")
        self.verticalLayout_6 = QVBoxLayout(self.tab_total)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.tabs_total = myQTabWidget(self.tab_total)
        self.tabs_total.setObjectName(u"tabs_total")
        self.tab_tot_serv = myQWidget()
        self.tab_tot_serv.setObjectName(u"tab_tot_serv")
        self.gridLayout_27 = QGridLayout(self.tab_tot_serv)
        self.gridLayout_27.setObjectName(u"gridLayout_27")
        self.tabs_tot_serv = myQTabWidget(self.tab_tot_serv)
        self.tabs_tot_serv.setObjectName(u"tabs_tot_serv")
        self.tab_12 = myQWidget()
        self.tab_12.setObjectName(u"tab_12")
        self.gridLayout_40 = QGridLayout(self.tab_12)
        self.gridLayout_40.setObjectName(u"gridLayout_40")
        self.report__main_for_dep__where_vdate__client_id = qcSelectReport(self.tab_12)
        self.report__main_for_dep__where_vdate__client_id.setObjectName(u"report__main_for_dep__where_vdate__client_id")
        self.gridLayout_38 = QGridLayout(self.report__main_for_dep__where_vdate__client_id)
        self.gridLayout_38.setObjectName(u"gridLayout_38")
        self.label_19 = QLabel(self.report__main_for_dep__where_vdate__client_id)
        self.label_19.setObjectName(u"label_19")

        self.gridLayout_38.addWidget(self.label_19, 2, 2, 1, 1)

        self.btn_serv_you_3 = QPushButton(self.report__main_for_dep__where_vdate__client_id)
        self.btn_serv_you_3.setObjectName(u"btn_serv_you_3")

        self.gridLayout_38.addWidget(self.btn_serv_you_3, 2, 0, 1, 1)

        self.pushButton_17 = QPushButton(self.report__main_for_dep__where_vdate__client_id)
        self.pushButton_17.setObjectName(u"pushButton_17")

        self.gridLayout_38.addWidget(self.pushButton_17, 2, 1, 1, 1)

        self.lineEdit_2 = QLineEdit(self.report__main_for_dep__where_vdate__client_id)
        self.lineEdit_2.setObjectName(u"lineEdit_2")

        self.gridLayout_38.addWidget(self.lineEdit_2, 2, 3, 1, 1)

        self.treeView = QTreeView(self.report__main_for_dep__where_vdate__client_id)
        self.treeView.setObjectName(u"treeView")

        self.gridLayout_38.addWidget(self.treeView, 1, 1, 1, 3)

        self.t_main_for_dep = QTableView(self.report__main_for_dep__where_vdate__client_id)
        self.t_main_for_dep.setObjectName(u"t_main_for_dep")

        self.gridLayout_38.addWidget(self.t_main_for_dep, 3, 0, 1, 4)

        self.frame222222222 = QFrame(self.report__main_for_dep__where_vdate__client_id)
        self.frame222222222.setObjectName(u"frame222222222")
        self.frame222222222.setFrameShape(QFrame.StyledPanel)
        self.frame222222222.setFrameShadow(QFrame.Raised)
        self.gridLayout_39 = QGridLayout(self.frame222222222)
        self.gridLayout_39.setObjectName(u"gridLayout_39")
        self.DO_NOT_USE_14 = myQTabWidget(self.frame222222222)
        self.DO_NOT_USE_14.setObjectName(u"DO_NOT_USE_14")
        sizePolicy14.setHeightForWidth(self.DO_NOT_USE_14.sizePolicy().hasHeightForWidth())
        self.DO_NOT_USE_14.setSizePolicy(sizePolicy14)
        self.DO_NOT_USE_14.setMinimumSize(QSize(300, 0))
        self.DO_NOT_USE_15 = QWidget()
        self.DO_NOT_USE_15.setObjectName(u"DO_NOT_USE_15")
        self.verticalLayout_62 = QVBoxLayout(self.DO_NOT_USE_15)
        self.verticalLayout_62.setObjectName(u"verticalLayout_62")
        self.DO_NOT_USE_16 = QGridLayout()
        self.DO_NOT_USE_16.setObjectName(u"DO_NOT_USE_16")
        self.DO_NOT_USE_16.setHorizontalSpacing(0)
        self.DO_NOT_USE_17 = QDateEdit(self.DO_NOT_USE_15)
        self.DO_NOT_USE_17.setObjectName(u"DO_NOT_USE_17")

        self.DO_NOT_USE_16.addWidget(self.DO_NOT_USE_17, 1, 1, 1, 1)

        self.DO_NOT_USE_18 = QLabel(self.DO_NOT_USE_15)
        self.DO_NOT_USE_18.setObjectName(u"DO_NOT_USE_18")
        sizePolicy5.setHeightForWidth(self.DO_NOT_USE_18.sizePolicy().hasHeightForWidth())
        self.DO_NOT_USE_18.setSizePolicy(sizePolicy5)
        self.DO_NOT_USE_18.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.DO_NOT_USE_16.addWidget(self.DO_NOT_USE_18, 1, 0, 1, 1)

        self.DO_NOT_USE_19 = QLabel(self.DO_NOT_USE_15)
        self.DO_NOT_USE_19.setObjectName(u"DO_NOT_USE_19")
        sizePolicy5.setHeightForWidth(self.DO_NOT_USE_19.sizePolicy().hasHeightForWidth())
        self.DO_NOT_USE_19.setSizePolicy(sizePolicy5)
        self.DO_NOT_USE_19.setLayoutDirection(Qt.LeftToRight)
        self.DO_NOT_USE_19.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.DO_NOT_USE_16.addWidget(self.DO_NOT_USE_19, 0, 0, 1, 1)

        self.DO_NOT_USE_20 = QDateEdit(self.DO_NOT_USE_15)
        self.DO_NOT_USE_20.setObjectName(u"DO_NOT_USE_20")

        self.DO_NOT_USE_16.addWidget(self.DO_NOT_USE_20, 0, 1, 1, 1)

        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.DO_NOT_USE_16.addItem(self.verticalSpacer_2, 2, 1, 1, 1)

        self.DO_NOT_USE_16.setColumnStretch(0, 1)
        self.DO_NOT_USE_16.setColumnStretch(1, 2)

        self.verticalLayout_62.addLayout(self.DO_NOT_USE_16)

        self.DO_NOT_USE_14.addTab(self.DO_NOT_USE_15, "")
        self.DO_NOT_USE_21 = QWidget()
        self.DO_NOT_USE_21.setObjectName(u"DO_NOT_USE_21")
        self.verticalLayout_63 = QVBoxLayout(self.DO_NOT_USE_21)
        self.verticalLayout_63.setObjectName(u"verticalLayout_63")
        self.DO_NOT_USE_22 = QGridLayout()
        self.DO_NOT_USE_22.setObjectName(u"DO_NOT_USE_22")
        self.DO_NOT_USE_23 = QLabel(self.DO_NOT_USE_21)
        self.DO_NOT_USE_23.setObjectName(u"DO_NOT_USE_23")
        self.DO_NOT_USE_23.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.DO_NOT_USE_22.addWidget(self.DO_NOT_USE_23, 0, 0, 1, 1)

        self.DO_NOT_USE_24 = QSpinBox(self.DO_NOT_USE_21)
        self.DO_NOT_USE_24.setObjectName(u"DO_NOT_USE_24")
        self.DO_NOT_USE_24.setMinimum(1950)
        self.DO_NOT_USE_24.setMaximum(2050)
        self.DO_NOT_USE_24.setValue(2019)

        self.DO_NOT_USE_22.addWidget(self.DO_NOT_USE_24, 1, 1, 1, 1)

        self.DO_NOT_USE_25 = QLabel(self.DO_NOT_USE_21)
        self.DO_NOT_USE_25.setObjectName(u"DO_NOT_USE_25")
        self.DO_NOT_USE_25.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.DO_NOT_USE_22.addWidget(self.DO_NOT_USE_25, 1, 0, 1, 1)

        self.DO_NOT_USE_26 = QComboBox(self.DO_NOT_USE_21)
        self.DO_NOT_USE_26.setObjectName(u"DO_NOT_USE_26")
        self.DO_NOT_USE_26.setEditable(True)

        self.DO_NOT_USE_22.addWidget(self.DO_NOT_USE_26, 0, 1, 1, 1)

        self.DO_NOT_USE_22.setColumnStretch(0, 1)
        self.DO_NOT_USE_22.setColumnStretch(1, 2)

        self.verticalLayout_63.addLayout(self.DO_NOT_USE_22)

        self.DO_NOT_USE_14.addTab(self.DO_NOT_USE_21, "")

        self.gridLayout_39.addWidget(self.DO_NOT_USE_14, 0, 0, 1, 1)


        self.gridLayout_38.addWidget(self.frame222222222, 0, 0, 2, 1)

        self.verticalSpacer_3 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout_38.addItem(self.verticalSpacer_3, 0, 2, 1, 1)


        self.gridLayout_40.addWidget(self.report__main_for_dep__where_vdate__client_id, 0, 0, 1, 1)

        self.tabs_tot_serv.addTab(self.tab_12, "")
        self.tab_serv_you = myQWidget()
        self.tab_serv_you.setObjectName(u"tab_serv_you")
        self.gridLayout_32 = QGridLayout(self.tab_serv_you)
        self.gridLayout_32.setObjectName(u"gridLayout_32")
        self.report__worker_has_main__where_vdate = qcSelectReport(self.tab_serv_you)
        self.report__worker_has_main__where_vdate.setObjectName(u"report__worker_has_main__where_vdate")
        self.gridLayout_41 = QGridLayout(self.report__worker_has_main__where_vdate)
        self.gridLayout_41.setObjectName(u"gridLayout_41")
        self.btn_serv_you_5 = QPushButton(self.report__worker_has_main__where_vdate)
        self.btn_serv_you_5.setObjectName(u"btn_serv_you_5")

        self.gridLayout_41.addWidget(self.btn_serv_you_5, 2, 0, 1, 1)

        self.pushButton_19 = QPushButton(self.report__worker_has_main__where_vdate)
        self.pushButton_19.setObjectName(u"pushButton_19")

        self.gridLayout_41.addWidget(self.pushButton_19, 2, 1, 1, 1)

        self.frame_2 = QFrame(self.report__worker_has_main__where_vdate)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.gridLayout_42 = QGridLayout(self.frame_2)
        self.gridLayout_42.setObjectName(u"gridLayout_42")
        self.DO_NOT_USE_53 = myQTabWidget(self.frame_2)
        self.DO_NOT_USE_53.setObjectName(u"DO_NOT_USE_53")
        sizePolicy14.setHeightForWidth(self.DO_NOT_USE_53.sizePolicy().hasHeightForWidth())
        self.DO_NOT_USE_53.setSizePolicy(sizePolicy14)
        self.DO_NOT_USE_53.setMinimumSize(QSize(300, 0))
        self.DO_NOT_USE_67 = QWidget()
        self.DO_NOT_USE_67.setObjectName(u"DO_NOT_USE_67")
        self.verticalLayout_69 = QVBoxLayout(self.DO_NOT_USE_67)
        self.verticalLayout_69.setObjectName(u"verticalLayout_69")
        self.DO_NOT_USE_68 = QGridLayout()
        self.DO_NOT_USE_68.setObjectName(u"DO_NOT_USE_68")
        self.DO_NOT_USE_68.setHorizontalSpacing(0)
        self.DO_NOT_USE_69 = QDateEdit(self.DO_NOT_USE_67)
        self.DO_NOT_USE_69.setObjectName(u"DO_NOT_USE_69")

        self.DO_NOT_USE_68.addWidget(self.DO_NOT_USE_69, 1, 1, 1, 1)

        self.DO_NOT_USE_70 = QLabel(self.DO_NOT_USE_67)
        self.DO_NOT_USE_70.setObjectName(u"DO_NOT_USE_70")
        sizePolicy5.setHeightForWidth(self.DO_NOT_USE_70.sizePolicy().hasHeightForWidth())
        self.DO_NOT_USE_70.setSizePolicy(sizePolicy5)
        self.DO_NOT_USE_70.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.DO_NOT_USE_68.addWidget(self.DO_NOT_USE_70, 1, 0, 1, 1)

        self.DO_NOT_USE_71 = QLabel(self.DO_NOT_USE_67)
        self.DO_NOT_USE_71.setObjectName(u"DO_NOT_USE_71")
        sizePolicy5.setHeightForWidth(self.DO_NOT_USE_71.sizePolicy().hasHeightForWidth())
        self.DO_NOT_USE_71.setSizePolicy(sizePolicy5)
        self.DO_NOT_USE_71.setLayoutDirection(Qt.LeftToRight)
        self.DO_NOT_USE_71.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.DO_NOT_USE_68.addWidget(self.DO_NOT_USE_71, 0, 0, 1, 1)

        self.DO_NOT_USE_72 = QDateEdit(self.DO_NOT_USE_67)
        self.DO_NOT_USE_72.setObjectName(u"DO_NOT_USE_72")

        self.DO_NOT_USE_68.addWidget(self.DO_NOT_USE_72, 0, 1, 1, 1)

        self.DO_NOT_USE_68.setColumnStretch(0, 1)
        self.DO_NOT_USE_68.setColumnStretch(1, 2)

        self.verticalLayout_69.addLayout(self.DO_NOT_USE_68)

        self.DO_NOT_USE_53.addTab(self.DO_NOT_USE_67, "")
        self.DO_NOT_USE_73 = QWidget()
        self.DO_NOT_USE_73.setObjectName(u"DO_NOT_USE_73")
        self.verticalLayout_70 = QVBoxLayout(self.DO_NOT_USE_73)
        self.verticalLayout_70.setObjectName(u"verticalLayout_70")
        self.DO_NOT_USE_74 = QGridLayout()
        self.DO_NOT_USE_74.setObjectName(u"DO_NOT_USE_74")
        self.DO_NOT_USE_75 = QLabel(self.DO_NOT_USE_73)
        self.DO_NOT_USE_75.setObjectName(u"DO_NOT_USE_75")
        self.DO_NOT_USE_75.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.DO_NOT_USE_74.addWidget(self.DO_NOT_USE_75, 0, 0, 1, 1)

        self.DO_NOT_USE_76 = QSpinBox(self.DO_NOT_USE_73)
        self.DO_NOT_USE_76.setObjectName(u"DO_NOT_USE_76")
        self.DO_NOT_USE_76.setMinimum(1950)
        self.DO_NOT_USE_76.setMaximum(2050)
        self.DO_NOT_USE_76.setValue(2019)

        self.DO_NOT_USE_74.addWidget(self.DO_NOT_USE_76, 1, 1, 1, 1)

        self.DO_NOT_USE_77 = QLabel(self.DO_NOT_USE_73)
        self.DO_NOT_USE_77.setObjectName(u"DO_NOT_USE_77")
        self.DO_NOT_USE_77.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.DO_NOT_USE_74.addWidget(self.DO_NOT_USE_77, 1, 0, 1, 1)

        self.DO_NOT_USE_78 = QComboBox(self.DO_NOT_USE_73)
        self.DO_NOT_USE_78.setObjectName(u"DO_NOT_USE_78")
        self.DO_NOT_USE_78.setEditable(True)

        self.DO_NOT_USE_74.addWidget(self.DO_NOT_USE_78, 0, 1, 1, 1)

        self.DO_NOT_USE_74.setColumnStretch(0, 1)
        self.DO_NOT_USE_74.setColumnStretch(1, 2)

        self.verticalLayout_70.addLayout(self.DO_NOT_USE_74)

        self.DO_NOT_USE_53.addTab(self.DO_NOT_USE_73, "")

        self.gridLayout_42.addWidget(self.DO_NOT_USE_53, 0, 0, 1, 1)


        self.gridLayout_41.addWidget(self.frame_2, 1, 0, 1, 1)

        self.t_main_for_dep_2 = QTableView(self.report__worker_has_main__where_vdate)
        self.t_main_for_dep_2.setObjectName(u"t_main_for_dep_2")

        self.gridLayout_41.addWidget(self.t_main_for_dep_2, 3, 0, 1, 2)


        self.gridLayout_32.addWidget(self.report__worker_has_main__where_vdate, 0, 0, 1, 1)

        self.tabs_tot_serv.addTab(self.tab_serv_you, "")
        self.tab_9 = myQWidget()
        self.tab_9.setObjectName(u"tab_9")
        self.gridLayout_34 = QGridLayout(self.tab_9)
        self.gridLayout_34.setObjectName(u"gridLayout_34")
        self.report__user_has_main__where_vdate = qcSelectReport(self.tab_9)
        self.report__user_has_main__where_vdate.setObjectName(u"report__user_has_main__where_vdate")
        self.gridLayout_43 = QGridLayout(self.report__user_has_main__where_vdate)
        self.gridLayout_43.setObjectName(u"gridLayout_43")
        self.btn_serv_you_6 = QPushButton(self.report__user_has_main__where_vdate)
        self.btn_serv_you_6.setObjectName(u"btn_serv_you_6")

        self.gridLayout_43.addWidget(self.btn_serv_you_6, 2, 0, 1, 1)

        self.pushButton_20 = QPushButton(self.report__user_has_main__where_vdate)
        self.pushButton_20.setObjectName(u"pushButton_20")

        self.gridLayout_43.addWidget(self.pushButton_20, 2, 1, 1, 1)

        self.frame_3 = QFrame(self.report__user_has_main__where_vdate)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.gridLayout_44 = QGridLayout(self.frame_3)
        self.gridLayout_44.setObjectName(u"gridLayout_44")
        self.DO_NOT_USE_79 = myQTabWidget(self.frame_3)
        self.DO_NOT_USE_79.setObjectName(u"DO_NOT_USE_79")
        sizePolicy14.setHeightForWidth(self.DO_NOT_USE_79.sizePolicy().hasHeightForWidth())
        self.DO_NOT_USE_79.setSizePolicy(sizePolicy14)
        self.DO_NOT_USE_79.setMinimumSize(QSize(300, 0))
        self.DO_NOT_USE_80 = QWidget()
        self.DO_NOT_USE_80.setObjectName(u"DO_NOT_USE_80")
        self.verticalLayout_71 = QVBoxLayout(self.DO_NOT_USE_80)
        self.verticalLayout_71.setObjectName(u"verticalLayout_71")
        self.DO_NOT_USE_81 = QGridLayout()
        self.DO_NOT_USE_81.setObjectName(u"DO_NOT_USE_81")
        self.DO_NOT_USE_81.setHorizontalSpacing(0)
        self.DO_NOT_USE_82 = QDateEdit(self.DO_NOT_USE_80)
        self.DO_NOT_USE_82.setObjectName(u"DO_NOT_USE_82")

        self.DO_NOT_USE_81.addWidget(self.DO_NOT_USE_82, 1, 1, 1, 1)

        self.DO_NOT_USE_83 = QLabel(self.DO_NOT_USE_80)
        self.DO_NOT_USE_83.setObjectName(u"DO_NOT_USE_83")
        sizePolicy5.setHeightForWidth(self.DO_NOT_USE_83.sizePolicy().hasHeightForWidth())
        self.DO_NOT_USE_83.setSizePolicy(sizePolicy5)
        self.DO_NOT_USE_83.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.DO_NOT_USE_81.addWidget(self.DO_NOT_USE_83, 1, 0, 1, 1)

        self.DO_NOT_USE_84 = QLabel(self.DO_NOT_USE_80)
        self.DO_NOT_USE_84.setObjectName(u"DO_NOT_USE_84")
        sizePolicy5.setHeightForWidth(self.DO_NOT_USE_84.sizePolicy().hasHeightForWidth())
        self.DO_NOT_USE_84.setSizePolicy(sizePolicy5)
        self.DO_NOT_USE_84.setLayoutDirection(Qt.LeftToRight)
        self.DO_NOT_USE_84.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.DO_NOT_USE_81.addWidget(self.DO_NOT_USE_84, 0, 0, 1, 1)

        self.DO_NOT_USE_85 = QDateEdit(self.DO_NOT_USE_80)
        self.DO_NOT_USE_85.setObjectName(u"DO_NOT_USE_85")

        self.DO_NOT_USE_81.addWidget(self.DO_NOT_USE_85, 0, 1, 1, 1)

        self.DO_NOT_USE_81.setColumnStretch(0, 1)
        self.DO_NOT_USE_81.setColumnStretch(1, 2)

        self.verticalLayout_71.addLayout(self.DO_NOT_USE_81)

        self.DO_NOT_USE_79.addTab(self.DO_NOT_USE_80, "")
        self.DO_NOT_USE_86 = QWidget()
        self.DO_NOT_USE_86.setObjectName(u"DO_NOT_USE_86")
        self.verticalLayout_72 = QVBoxLayout(self.DO_NOT_USE_86)
        self.verticalLayout_72.setObjectName(u"verticalLayout_72")
        self.DO_NOT_USE_87 = QGridLayout()
        self.DO_NOT_USE_87.setObjectName(u"DO_NOT_USE_87")
        self.DO_NOT_USE_88 = QLabel(self.DO_NOT_USE_86)
        self.DO_NOT_USE_88.setObjectName(u"DO_NOT_USE_88")
        self.DO_NOT_USE_88.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.DO_NOT_USE_87.addWidget(self.DO_NOT_USE_88, 0, 0, 1, 1)

        self.DO_NOT_USE_89 = QSpinBox(self.DO_NOT_USE_86)
        self.DO_NOT_USE_89.setObjectName(u"DO_NOT_USE_89")
        self.DO_NOT_USE_89.setMinimum(1950)
        self.DO_NOT_USE_89.setMaximum(2050)
        self.DO_NOT_USE_89.setValue(2019)

        self.DO_NOT_USE_87.addWidget(self.DO_NOT_USE_89, 1, 1, 1, 1)

        self.DO_NOT_USE_90 = QLabel(self.DO_NOT_USE_86)
        self.DO_NOT_USE_90.setObjectName(u"DO_NOT_USE_90")
        self.DO_NOT_USE_90.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.DO_NOT_USE_87.addWidget(self.DO_NOT_USE_90, 1, 0, 1, 1)

        self.DO_NOT_USE_91 = QComboBox(self.DO_NOT_USE_86)
        self.DO_NOT_USE_91.setObjectName(u"DO_NOT_USE_91")
        self.DO_NOT_USE_91.setEditable(True)

        self.DO_NOT_USE_87.addWidget(self.DO_NOT_USE_91, 0, 1, 1, 1)

        self.DO_NOT_USE_87.setColumnStretch(0, 1)
        self.DO_NOT_USE_87.setColumnStretch(1, 2)

        self.verticalLayout_72.addLayout(self.DO_NOT_USE_87)

        self.DO_NOT_USE_79.addTab(self.DO_NOT_USE_86, "")

        self.gridLayout_44.addWidget(self.DO_NOT_USE_79, 0, 0, 1, 1)


        self.gridLayout_43.addWidget(self.frame_3, 1, 0, 1, 1)

        self.table__dep_has_main_3 = QTableView(self.report__user_has_main__where_vdate)
        self.table__dep_has_main_3.setObjectName(u"table__dep_has_main_3")

        self.gridLayout_43.addWidget(self.table__dep_has_main_3, 3, 0, 1, 2)


        self.gridLayout_34.addWidget(self.report__user_has_main__where_vdate, 0, 0, 1, 1)

        self.tabs_tot_serv.addTab(self.tab_9, "")
        self.tab_19 = myQWidget()
        self.tab_19.setObjectName(u"tab_19")
        self.gridLayout_29 = QGridLayout(self.tab_19)
        self.gridLayout_29.setObjectName(u"gridLayout_29")
        self.label_7 = QLabel(self.tab_19)
        self.label_7.setObjectName(u"label_7")
        sizePolicy7.setHeightForWidth(self.label_7.sizePolicy().hasHeightForWidth())
        self.label_7.setSizePolicy(sizePolicy7)

        self.gridLayout_29.addWidget(self.label_7, 0, 0, 1, 1)

        self.cbx_1_dep_has_worker = myQComboBox(self.tab_19)
        self.cbx_1_dep_has_worker.setObjectName(u"cbx_1_dep_has_worker")
        sizePolicy6.setHeightForWidth(self.cbx_1_dep_has_worker.sizePolicy().hasHeightForWidth())
        self.cbx_1_dep_has_worker.setSizePolicy(sizePolicy6)
        self.cbx_1_dep_has_worker.setEditable(True)

        self.gridLayout_29.addWidget(self.cbx_1_dep_has_worker, 0, 1, 1, 1)

        self.report__main_for_dep__where_vdate__by_client_id_by_dep_has_worker_id = qcSelectReport(self.tab_19)
        self.report__main_for_dep__where_vdate__by_client_id_by_dep_has_worker_id.setObjectName(u"report__main_for_dep__where_vdate__by_client_id_by_dep_has_worker_id")
        self.gridLayout_45 = QGridLayout(self.report__main_for_dep__where_vdate__by_client_id_by_dep_has_worker_id)
        self.gridLayout_45.setObjectName(u"gridLayout_45")
        self.table__dep_has_main_4 = QTableView(self.report__main_for_dep__where_vdate__by_client_id_by_dep_has_worker_id)
        self.table__dep_has_main_4.setObjectName(u"table__dep_has_main_4")

        self.gridLayout_45.addWidget(self.table__dep_has_main_4, 3, 0, 1, 2)

        self.pushButton_21 = QPushButton(self.report__main_for_dep__where_vdate__by_client_id_by_dep_has_worker_id)
        self.pushButton_21.setObjectName(u"pushButton_21")

        self.gridLayout_45.addWidget(self.pushButton_21, 2, 1, 1, 1)

        self.btn_serv_you_7 = QPushButton(self.report__main_for_dep__where_vdate__by_client_id_by_dep_has_worker_id)
        self.btn_serv_you_7.setObjectName(u"btn_serv_you_7")

        self.gridLayout_45.addWidget(self.btn_serv_you_7, 2, 0, 1, 1)

        self.frame_4 = QFrame(self.report__main_for_dep__where_vdate__by_client_id_by_dep_has_worker_id)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setFrameShape(QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QFrame.Raised)
        self.gridLayout_46 = QGridLayout(self.frame_4)
        self.gridLayout_46.setObjectName(u"gridLayout_46")
        self.DO_NOT_USE_92 = myQTabWidget(self.frame_4)
        self.DO_NOT_USE_92.setObjectName(u"DO_NOT_USE_92")
        sizePolicy14.setHeightForWidth(self.DO_NOT_USE_92.sizePolicy().hasHeightForWidth())
        self.DO_NOT_USE_92.setSizePolicy(sizePolicy14)
        self.DO_NOT_USE_92.setMinimumSize(QSize(300, 0))
        self.DO_NOT_USE_93 = QWidget()
        self.DO_NOT_USE_93.setObjectName(u"DO_NOT_USE_93")
        self.verticalLayout_73 = QVBoxLayout(self.DO_NOT_USE_93)
        self.verticalLayout_73.setObjectName(u"verticalLayout_73")
        self.DO_NOT_USE_94 = QGridLayout()
        self.DO_NOT_USE_94.setObjectName(u"DO_NOT_USE_94")
        self.DO_NOT_USE_94.setHorizontalSpacing(0)
        self.DO_NOT_USE_95 = QDateEdit(self.DO_NOT_USE_93)
        self.DO_NOT_USE_95.setObjectName(u"DO_NOT_USE_95")

        self.DO_NOT_USE_94.addWidget(self.DO_NOT_USE_95, 1, 1, 1, 1)

        self.DO_NOT_USE_96 = QLabel(self.DO_NOT_USE_93)
        self.DO_NOT_USE_96.setObjectName(u"DO_NOT_USE_96")
        sizePolicy5.setHeightForWidth(self.DO_NOT_USE_96.sizePolicy().hasHeightForWidth())
        self.DO_NOT_USE_96.setSizePolicy(sizePolicy5)
        self.DO_NOT_USE_96.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.DO_NOT_USE_94.addWidget(self.DO_NOT_USE_96, 1, 0, 1, 1)

        self.DO_NOT_USE_97 = QLabel(self.DO_NOT_USE_93)
        self.DO_NOT_USE_97.setObjectName(u"DO_NOT_USE_97")
        sizePolicy5.setHeightForWidth(self.DO_NOT_USE_97.sizePolicy().hasHeightForWidth())
        self.DO_NOT_USE_97.setSizePolicy(sizePolicy5)
        self.DO_NOT_USE_97.setLayoutDirection(Qt.LeftToRight)
        self.DO_NOT_USE_97.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.DO_NOT_USE_94.addWidget(self.DO_NOT_USE_97, 0, 0, 1, 1)

        self.DO_NOT_USE_98 = QDateEdit(self.DO_NOT_USE_93)
        self.DO_NOT_USE_98.setObjectName(u"DO_NOT_USE_98")

        self.DO_NOT_USE_94.addWidget(self.DO_NOT_USE_98, 0, 1, 1, 1)

        self.DO_NOT_USE_94.setColumnStretch(0, 1)
        self.DO_NOT_USE_94.setColumnStretch(1, 2)

        self.verticalLayout_73.addLayout(self.DO_NOT_USE_94)

        self.DO_NOT_USE_92.addTab(self.DO_NOT_USE_93, "")
        self.DO_NOT_USE_99 = QWidget()
        self.DO_NOT_USE_99.setObjectName(u"DO_NOT_USE_99")
        self.verticalLayout_74 = QVBoxLayout(self.DO_NOT_USE_99)
        self.verticalLayout_74.setObjectName(u"verticalLayout_74")
        self.DO_NOT_USE_100 = QGridLayout()
        self.DO_NOT_USE_100.setObjectName(u"DO_NOT_USE_100")
        self.DO_NOT_USE_101 = QLabel(self.DO_NOT_USE_99)
        self.DO_NOT_USE_101.setObjectName(u"DO_NOT_USE_101")
        self.DO_NOT_USE_101.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.DO_NOT_USE_100.addWidget(self.DO_NOT_USE_101, 0, 0, 1, 1)

        self.DO_NOT_USE_102 = QSpinBox(self.DO_NOT_USE_99)
        self.DO_NOT_USE_102.setObjectName(u"DO_NOT_USE_102")
        self.DO_NOT_USE_102.setMinimum(1950)
        self.DO_NOT_USE_102.setMaximum(2050)
        self.DO_NOT_USE_102.setValue(2019)

        self.DO_NOT_USE_100.addWidget(self.DO_NOT_USE_102, 1, 1, 1, 1)

        self.DO_NOT_USE_103 = QLabel(self.DO_NOT_USE_99)
        self.DO_NOT_USE_103.setObjectName(u"DO_NOT_USE_103")
        self.DO_NOT_USE_103.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.DO_NOT_USE_100.addWidget(self.DO_NOT_USE_103, 1, 0, 1, 1)

        self.DO_NOT_USE_104 = QComboBox(self.DO_NOT_USE_99)
        self.DO_NOT_USE_104.setObjectName(u"DO_NOT_USE_104")
        self.DO_NOT_USE_104.setEditable(True)

        self.DO_NOT_USE_100.addWidget(self.DO_NOT_USE_104, 0, 1, 1, 1)

        self.DO_NOT_USE_100.setColumnStretch(0, 1)
        self.DO_NOT_USE_100.setColumnStretch(1, 2)

        self.verticalLayout_74.addLayout(self.DO_NOT_USE_100)

        self.DO_NOT_USE_92.addTab(self.DO_NOT_USE_99, "")

        self.gridLayout_46.addWidget(self.DO_NOT_USE_92, 0, 0, 1, 1)


        self.gridLayout_45.addWidget(self.frame_4, 1, 0, 1, 1)


        self.gridLayout_29.addWidget(self.report__main_for_dep__where_vdate__by_client_id_by_dep_has_worker_id, 1, 0, 1, 2)

        self.tabs_tot_serv.addTab(self.tab_19, "")
        self.tab_4 = myQWidget()
        self.tab_4.setObjectName(u"tab_4")
        self.gridLayout_54 = QGridLayout(self.tab_4)
        self.gridLayout_54.setObjectName(u"gridLayout_54")
        self.gridLayout_53 = QGridLayout()
        self.gridLayout_53.setObjectName(u"gridLayout_53")
        self.report__g_serv_total_dep_with_worker__where_vdate__by_client_id_by_dep_has_worker_id_2 = qcSelectReport(self.tab_4)
        self.report__g_serv_total_dep_with_worker__where_vdate__by_client_id_by_dep_has_worker_id_2.setObjectName(u"report__g_serv_total_dep_with_worker__where_vdate__by_client_id_by_dep_has_worker_id_2")
        self.gridLayout_104 = QGridLayout(self.report__g_serv_total_dep_with_worker__where_vdate__by_client_id_by_dep_has_worker_id_2)
        self.gridLayout_104.setObjectName(u"gridLayout_104")
        self.table__dep_has_main_10 = QTableView(self.report__g_serv_total_dep_with_worker__where_vdate__by_client_id_by_dep_has_worker_id_2)
        self.table__dep_has_main_10.setObjectName(u"table__dep_has_main_10")

        self.gridLayout_104.addWidget(self.table__dep_has_main_10, 3, 0, 1, 2)

        self.pushButton_36 = QPushButton(self.report__g_serv_total_dep_with_worker__where_vdate__by_client_id_by_dep_has_worker_id_2)
        self.pushButton_36.setObjectName(u"pushButton_36")

        self.gridLayout_104.addWidget(self.pushButton_36, 2, 1, 1, 1)

        self.btn_serv_you_22 = QPushButton(self.report__g_serv_total_dep_with_worker__where_vdate__by_client_id_by_dep_has_worker_id_2)
        self.btn_serv_you_22.setObjectName(u"btn_serv_you_22")

        self.gridLayout_104.addWidget(self.btn_serv_you_22, 2, 0, 1, 1)

        self.frame_21 = QFrame(self.report__g_serv_total_dep_with_worker__where_vdate__by_client_id_by_dep_has_worker_id_2)
        self.frame_21.setObjectName(u"frame_21")
        self.frame_21.setFrameShape(QFrame.StyledPanel)
        self.frame_21.setFrameShadow(QFrame.Raised)
        self.gridLayout_105 = QGridLayout(self.frame_21)
        self.gridLayout_105.setObjectName(u"gridLayout_105")
        self.DO_NOT_USE_274 = myQTabWidget(self.frame_21)
        self.DO_NOT_USE_274.setObjectName(u"DO_NOT_USE_274")
        sizePolicy14.setHeightForWidth(self.DO_NOT_USE_274.sizePolicy().hasHeightForWidth())
        self.DO_NOT_USE_274.setSizePolicy(sizePolicy14)
        self.DO_NOT_USE_274.setMinimumSize(QSize(300, 0))
        self.DO_NOT_USE_275 = QWidget()
        self.DO_NOT_USE_275.setObjectName(u"DO_NOT_USE_275")
        self.verticalLayout_101 = QVBoxLayout(self.DO_NOT_USE_275)
        self.verticalLayout_101.setObjectName(u"verticalLayout_101")
        self.DO_NOT_USE_276 = QGridLayout()
        self.DO_NOT_USE_276.setObjectName(u"DO_NOT_USE_276")
        self.DO_NOT_USE_276.setHorizontalSpacing(0)
        self.DO_NOT_USE_277 = QDateEdit(self.DO_NOT_USE_275)
        self.DO_NOT_USE_277.setObjectName(u"DO_NOT_USE_277")

        self.DO_NOT_USE_276.addWidget(self.DO_NOT_USE_277, 1, 1, 1, 1)

        self.DO_NOT_USE_278 = QLabel(self.DO_NOT_USE_275)
        self.DO_NOT_USE_278.setObjectName(u"DO_NOT_USE_278")
        sizePolicy5.setHeightForWidth(self.DO_NOT_USE_278.sizePolicy().hasHeightForWidth())
        self.DO_NOT_USE_278.setSizePolicy(sizePolicy5)
        self.DO_NOT_USE_278.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.DO_NOT_USE_276.addWidget(self.DO_NOT_USE_278, 1, 0, 1, 1)

        self.DO_NOT_USE_279 = QLabel(self.DO_NOT_USE_275)
        self.DO_NOT_USE_279.setObjectName(u"DO_NOT_USE_279")
        sizePolicy5.setHeightForWidth(self.DO_NOT_USE_279.sizePolicy().hasHeightForWidth())
        self.DO_NOT_USE_279.setSizePolicy(sizePolicy5)
        self.DO_NOT_USE_279.setLayoutDirection(Qt.LeftToRight)
        self.DO_NOT_USE_279.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.DO_NOT_USE_276.addWidget(self.DO_NOT_USE_279, 0, 0, 1, 1)

        self.DO_NOT_USE_280 = QDateEdit(self.DO_NOT_USE_275)
        self.DO_NOT_USE_280.setObjectName(u"DO_NOT_USE_280")

        self.DO_NOT_USE_276.addWidget(self.DO_NOT_USE_280, 0, 1, 1, 1)

        self.DO_NOT_USE_276.setColumnStretch(0, 1)
        self.DO_NOT_USE_276.setColumnStretch(1, 2)

        self.verticalLayout_101.addLayout(self.DO_NOT_USE_276)

        self.DO_NOT_USE_274.addTab(self.DO_NOT_USE_275, "")
        self.DO_NOT_USE_281 = QWidget()
        self.DO_NOT_USE_281.setObjectName(u"DO_NOT_USE_281")
        self.verticalLayout_102 = QVBoxLayout(self.DO_NOT_USE_281)
        self.verticalLayout_102.setObjectName(u"verticalLayout_102")
        self.DO_NOT_USE_282 = QGridLayout()
        self.DO_NOT_USE_282.setObjectName(u"DO_NOT_USE_282")
        self.DO_NOT_USE_283 = QLabel(self.DO_NOT_USE_281)
        self.DO_NOT_USE_283.setObjectName(u"DO_NOT_USE_283")
        self.DO_NOT_USE_283.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.DO_NOT_USE_282.addWidget(self.DO_NOT_USE_283, 0, 0, 1, 1)

        self.DO_NOT_USE_284 = QSpinBox(self.DO_NOT_USE_281)
        self.DO_NOT_USE_284.setObjectName(u"DO_NOT_USE_284")
        self.DO_NOT_USE_284.setMinimum(1950)
        self.DO_NOT_USE_284.setMaximum(2050)
        self.DO_NOT_USE_284.setValue(2019)

        self.DO_NOT_USE_282.addWidget(self.DO_NOT_USE_284, 1, 1, 1, 1)

        self.DO_NOT_USE_285 = QLabel(self.DO_NOT_USE_281)
        self.DO_NOT_USE_285.setObjectName(u"DO_NOT_USE_285")
        self.DO_NOT_USE_285.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.DO_NOT_USE_282.addWidget(self.DO_NOT_USE_285, 1, 0, 1, 1)

        self.DO_NOT_USE_286 = QComboBox(self.DO_NOT_USE_281)
        self.DO_NOT_USE_286.setObjectName(u"DO_NOT_USE_286")
        self.DO_NOT_USE_286.setEditable(True)

        self.DO_NOT_USE_282.addWidget(self.DO_NOT_USE_286, 0, 1, 1, 1)

        self.DO_NOT_USE_282.setColumnStretch(0, 1)
        self.DO_NOT_USE_282.setColumnStretch(1, 2)

        self.verticalLayout_102.addLayout(self.DO_NOT_USE_282)

        self.DO_NOT_USE_274.addTab(self.DO_NOT_USE_281, "")

        self.gridLayout_105.addWidget(self.DO_NOT_USE_274, 0, 0, 1, 1)


        self.gridLayout_104.addWidget(self.frame_21, 1, 0, 1, 1)


        self.gridLayout_53.addWidget(self.report__g_serv_total_dep_with_worker__where_vdate__by_client_id_by_dep_has_worker_id_2, 1, 0, 1, 2)

        self.cbx_1_category = myQComboBox(self.tab_4)
        self.cbx_1_category.setObjectName(u"cbx_1_category")
        sizePolicy6.setHeightForWidth(self.cbx_1_category.sizePolicy().hasHeightForWidth())
        self.cbx_1_category.setSizePolicy(sizePolicy6)
        self.cbx_1_category.setEditable(True)

        self.gridLayout_53.addWidget(self.cbx_1_category, 0, 1, 1, 1)

        self.label_74 = QLabel(self.tab_4)
        self.label_74.setObjectName(u"label_74")
        sizePolicy7.setHeightForWidth(self.label_74.sizePolicy().hasHeightForWidth())
        self.label_74.setSizePolicy(sizePolicy7)

        self.gridLayout_53.addWidget(self.label_74, 0, 0, 1, 1)


        self.gridLayout_54.addLayout(self.gridLayout_53, 0, 0, 1, 1)

        self.tabs_tot_serv.addTab(self.tab_4, "")
        self.tab_6 = myQWidget()
        self.tab_6.setObjectName(u"tab_6")
        self.verticalLayout_11 = QVBoxLayout(self.tab_6)
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.report__call_export_dep__where_period = qcSelectReport(self.tab_6)
        self.report__call_export_dep__where_period.setObjectName(u"report__call_export_dep__where_period")
        self.gridLayout_47 = QGridLayout(self.report__call_export_dep__where_period)
        self.gridLayout_47.setObjectName(u"gridLayout_47")
        self.table__dep_has_main_5 = QTableView(self.report__call_export_dep__where_period)
        self.table__dep_has_main_5.setObjectName(u"table__dep_has_main_5")

        self.gridLayout_47.addWidget(self.table__dep_has_main_5, 3, 0, 1, 2)

        self.pushButton_22 = QPushButton(self.report__call_export_dep__where_period)
        self.pushButton_22.setObjectName(u"pushButton_22")

        self.gridLayout_47.addWidget(self.pushButton_22, 2, 1, 1, 1)

        self.btn_serv_you_8 = QPushButton(self.report__call_export_dep__where_period)
        self.btn_serv_you_8.setObjectName(u"btn_serv_you_8")

        self.gridLayout_47.addWidget(self.btn_serv_you_8, 2, 0, 1, 1)

        self.frame_5 = QFrame(self.report__call_export_dep__where_period)
        self.frame_5.setObjectName(u"frame_5")
        self.frame_5.setFrameShape(QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QFrame.Raised)
        self.gridLayout_48 = QGridLayout(self.frame_5)
        self.gridLayout_48.setObjectName(u"gridLayout_48")
        self.DO_NOT_USE_105 = myQTabWidget(self.frame_5)
        self.DO_NOT_USE_105.setObjectName(u"DO_NOT_USE_105")
        sizePolicy14.setHeightForWidth(self.DO_NOT_USE_105.sizePolicy().hasHeightForWidth())
        self.DO_NOT_USE_105.setSizePolicy(sizePolicy14)
        self.DO_NOT_USE_105.setMinimumSize(QSize(300, 0))
        self.DO_NOT_USE_106 = QWidget()
        self.DO_NOT_USE_106.setObjectName(u"DO_NOT_USE_106")
        self.verticalLayout_75 = QVBoxLayout(self.DO_NOT_USE_106)
        self.verticalLayout_75.setObjectName(u"verticalLayout_75")
        self.DO_NOT_USE_107 = QGridLayout()
        self.DO_NOT_USE_107.setObjectName(u"DO_NOT_USE_107")
        self.DO_NOT_USE_107.setHorizontalSpacing(0)
        self.DO_NOT_USE_108 = QDateEdit(self.DO_NOT_USE_106)
        self.DO_NOT_USE_108.setObjectName(u"DO_NOT_USE_108")

        self.DO_NOT_USE_107.addWidget(self.DO_NOT_USE_108, 1, 1, 1, 1)

        self.DO_NOT_USE_109 = QLabel(self.DO_NOT_USE_106)
        self.DO_NOT_USE_109.setObjectName(u"DO_NOT_USE_109")
        sizePolicy5.setHeightForWidth(self.DO_NOT_USE_109.sizePolicy().hasHeightForWidth())
        self.DO_NOT_USE_109.setSizePolicy(sizePolicy5)
        self.DO_NOT_USE_109.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.DO_NOT_USE_107.addWidget(self.DO_NOT_USE_109, 1, 0, 1, 1)

        self.DO_NOT_USE_110 = QLabel(self.DO_NOT_USE_106)
        self.DO_NOT_USE_110.setObjectName(u"DO_NOT_USE_110")
        sizePolicy5.setHeightForWidth(self.DO_NOT_USE_110.sizePolicy().hasHeightForWidth())
        self.DO_NOT_USE_110.setSizePolicy(sizePolicy5)
        self.DO_NOT_USE_110.setLayoutDirection(Qt.LeftToRight)
        self.DO_NOT_USE_110.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.DO_NOT_USE_107.addWidget(self.DO_NOT_USE_110, 0, 0, 1, 1)

        self.DO_NOT_USE_111 = QDateEdit(self.DO_NOT_USE_106)
        self.DO_NOT_USE_111.setObjectName(u"DO_NOT_USE_111")

        self.DO_NOT_USE_107.addWidget(self.DO_NOT_USE_111, 0, 1, 1, 1)

        self.DO_NOT_USE_107.setColumnStretch(0, 1)
        self.DO_NOT_USE_107.setColumnStretch(1, 2)

        self.verticalLayout_75.addLayout(self.DO_NOT_USE_107)

        self.DO_NOT_USE_105.addTab(self.DO_NOT_USE_106, "")
        self.DO_NOT_USE_112 = QWidget()
        self.DO_NOT_USE_112.setObjectName(u"DO_NOT_USE_112")
        self.verticalLayout_76 = QVBoxLayout(self.DO_NOT_USE_112)
        self.verticalLayout_76.setObjectName(u"verticalLayout_76")
        self.DO_NOT_USE_113 = QGridLayout()
        self.DO_NOT_USE_113.setObjectName(u"DO_NOT_USE_113")
        self.DO_NOT_USE_114 = QLabel(self.DO_NOT_USE_112)
        self.DO_NOT_USE_114.setObjectName(u"DO_NOT_USE_114")
        self.DO_NOT_USE_114.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.DO_NOT_USE_113.addWidget(self.DO_NOT_USE_114, 0, 0, 1, 1)

        self.DO_NOT_USE_115 = QSpinBox(self.DO_NOT_USE_112)
        self.DO_NOT_USE_115.setObjectName(u"DO_NOT_USE_115")
        self.DO_NOT_USE_115.setMinimum(1950)
        self.DO_NOT_USE_115.setMaximum(2050)
        self.DO_NOT_USE_115.setValue(2019)

        self.DO_NOT_USE_113.addWidget(self.DO_NOT_USE_115, 1, 1, 1, 1)

        self.DO_NOT_USE_116 = QLabel(self.DO_NOT_USE_112)
        self.DO_NOT_USE_116.setObjectName(u"DO_NOT_USE_116")
        self.DO_NOT_USE_116.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.DO_NOT_USE_113.addWidget(self.DO_NOT_USE_116, 1, 0, 1, 1)

        self.DO_NOT_USE_117 = QComboBox(self.DO_NOT_USE_112)
        self.DO_NOT_USE_117.setObjectName(u"DO_NOT_USE_117")
        self.DO_NOT_USE_117.setEditable(True)

        self.DO_NOT_USE_113.addWidget(self.DO_NOT_USE_117, 0, 1, 1, 1)

        self.DO_NOT_USE_113.setColumnStretch(0, 1)
        self.DO_NOT_USE_113.setColumnStretch(1, 2)

        self.verticalLayout_76.addLayout(self.DO_NOT_USE_113)

        self.DO_NOT_USE_105.addTab(self.DO_NOT_USE_112, "")

        self.gridLayout_48.addWidget(self.DO_NOT_USE_105, 0, 0, 1, 1)


        self.gridLayout_47.addWidget(self.frame_5, 1, 0, 1, 1)


        self.verticalLayout_11.addWidget(self.report__call_export_dep__where_period)

        self.tabs_tot_serv.addTab(self.tab_6, "")

        self.gridLayout_27.addWidget(self.tabs_tot_serv, 0, 0, 1, 1)

        self.tabs_total.addTab(self.tab_tot_serv, "")
        self.tab_tot_group = myQWidget()
        self.tab_tot_group.setObjectName(u"tab_tot_group")
        self.verticalLayout_10 = QVBoxLayout(self.tab_tot_group)
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.tabWidget_8 = myQTabWidget(self.tab_tot_group)
        self.tabWidget_8.setObjectName(u"tabWidget_8")
        self.tab_tot_group_dep = myQWidget()
        self.tab_tot_group_dep.setObjectName(u"tab_tot_group_dep")
        self.verticalLayout_28 = QVBoxLayout(self.tab_tot_group_dep)
        self.verticalLayout_28.setObjectName(u"verticalLayout_28")
        self.report__g_serv_total_dep__where_vdate__by_client_id = qcSelectReport(self.tab_tot_group_dep)
        self.report__g_serv_total_dep__where_vdate__by_client_id.setObjectName(u"report__g_serv_total_dep__where_vdate__by_client_id")
        self.gridLayout_49 = QGridLayout(self.report__g_serv_total_dep__where_vdate__by_client_id)
        self.gridLayout_49.setObjectName(u"gridLayout_49")
        self.label_20 = QLabel(self.report__g_serv_total_dep__where_vdate__by_client_id)
        self.label_20.setObjectName(u"label_20")

        self.gridLayout_49.addWidget(self.label_20, 2, 2, 1, 1)

        self.btn_serv_you_4 = QPushButton(self.report__g_serv_total_dep__where_vdate__by_client_id)
        self.btn_serv_you_4.setObjectName(u"btn_serv_you_4")

        self.gridLayout_49.addWidget(self.btn_serv_you_4, 2, 0, 1, 1)

        self.pushButton_18 = QPushButton(self.report__g_serv_total_dep__where_vdate__by_client_id)
        self.pushButton_18.setObjectName(u"pushButton_18")

        self.gridLayout_49.addWidget(self.pushButton_18, 2, 1, 1, 1)

        self.lineEdit_3 = QLineEdit(self.report__g_serv_total_dep__where_vdate__by_client_id)
        self.lineEdit_3.setObjectName(u"lineEdit_3")

        self.gridLayout_49.addWidget(self.lineEdit_3, 2, 3, 1, 1)

        self.treeView_2 = QTreeView(self.report__g_serv_total_dep__where_vdate__by_client_id)
        self.treeView_2.setObjectName(u"treeView_2")

        self.gridLayout_49.addWidget(self.treeView_2, 1, 1, 1, 3)

        self.t_main_for_dep_3 = QTableView(self.report__g_serv_total_dep__where_vdate__by_client_id)
        self.t_main_for_dep_3.setObjectName(u"t_main_for_dep_3")

        self.gridLayout_49.addWidget(self.t_main_for_dep_3, 3, 0, 1, 4)

        self.frame_6 = QFrame(self.report__g_serv_total_dep__where_vdate__by_client_id)
        self.frame_6.setObjectName(u"frame_6")
        self.frame_6.setFrameShape(QFrame.StyledPanel)
        self.frame_6.setFrameShadow(QFrame.Raised)
        self.gridLayout_50 = QGridLayout(self.frame_6)
        self.gridLayout_50.setObjectName(u"gridLayout_50")
        self.DO_NOT_USE_27 = myQTabWidget(self.frame_6)
        self.DO_NOT_USE_27.setObjectName(u"DO_NOT_USE_27")
        sizePolicy14.setHeightForWidth(self.DO_NOT_USE_27.sizePolicy().hasHeightForWidth())
        self.DO_NOT_USE_27.setSizePolicy(sizePolicy14)
        self.DO_NOT_USE_27.setMinimumSize(QSize(300, 0))
        self.DO_NOT_USE_28 = QWidget()
        self.DO_NOT_USE_28.setObjectName(u"DO_NOT_USE_28")
        self.verticalLayout_64 = QVBoxLayout(self.DO_NOT_USE_28)
        self.verticalLayout_64.setObjectName(u"verticalLayout_64")
        self.DO_NOT_USE_29 = QGridLayout()
        self.DO_NOT_USE_29.setObjectName(u"DO_NOT_USE_29")
        self.DO_NOT_USE_29.setHorizontalSpacing(0)
        self.DO_NOT_USE_30 = QDateEdit(self.DO_NOT_USE_28)
        self.DO_NOT_USE_30.setObjectName(u"DO_NOT_USE_30")

        self.DO_NOT_USE_29.addWidget(self.DO_NOT_USE_30, 1, 1, 1, 1)

        self.DO_NOT_USE_31 = QLabel(self.DO_NOT_USE_28)
        self.DO_NOT_USE_31.setObjectName(u"DO_NOT_USE_31")
        sizePolicy5.setHeightForWidth(self.DO_NOT_USE_31.sizePolicy().hasHeightForWidth())
        self.DO_NOT_USE_31.setSizePolicy(sizePolicy5)
        self.DO_NOT_USE_31.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.DO_NOT_USE_29.addWidget(self.DO_NOT_USE_31, 1, 0, 1, 1)

        self.DO_NOT_USE_32 = QLabel(self.DO_NOT_USE_28)
        self.DO_NOT_USE_32.setObjectName(u"DO_NOT_USE_32")
        sizePolicy5.setHeightForWidth(self.DO_NOT_USE_32.sizePolicy().hasHeightForWidth())
        self.DO_NOT_USE_32.setSizePolicy(sizePolicy5)
        self.DO_NOT_USE_32.setLayoutDirection(Qt.LeftToRight)
        self.DO_NOT_USE_32.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.DO_NOT_USE_29.addWidget(self.DO_NOT_USE_32, 0, 0, 1, 1)

        self.DO_NOT_USE_33 = QDateEdit(self.DO_NOT_USE_28)
        self.DO_NOT_USE_33.setObjectName(u"DO_NOT_USE_33")

        self.DO_NOT_USE_29.addWidget(self.DO_NOT_USE_33, 0, 1, 1, 1)

        self.verticalSpacer_4 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.DO_NOT_USE_29.addItem(self.verticalSpacer_4, 2, 1, 1, 1)

        self.DO_NOT_USE_29.setColumnStretch(0, 1)
        self.DO_NOT_USE_29.setColumnStretch(1, 2)

        self.verticalLayout_64.addLayout(self.DO_NOT_USE_29)

        self.DO_NOT_USE_27.addTab(self.DO_NOT_USE_28, "")
        self.DO_NOT_USE_34 = QWidget()
        self.DO_NOT_USE_34.setObjectName(u"DO_NOT_USE_34")
        self.verticalLayout_65 = QVBoxLayout(self.DO_NOT_USE_34)
        self.verticalLayout_65.setObjectName(u"verticalLayout_65")
        self.DO_NOT_USE_35 = QGridLayout()
        self.DO_NOT_USE_35.setObjectName(u"DO_NOT_USE_35")
        self.DO_NOT_USE_36 = QLabel(self.DO_NOT_USE_34)
        self.DO_NOT_USE_36.setObjectName(u"DO_NOT_USE_36")
        self.DO_NOT_USE_36.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.DO_NOT_USE_35.addWidget(self.DO_NOT_USE_36, 0, 0, 1, 1)

        self.DO_NOT_USE_37 = QSpinBox(self.DO_NOT_USE_34)
        self.DO_NOT_USE_37.setObjectName(u"DO_NOT_USE_37")
        self.DO_NOT_USE_37.setMinimum(1950)
        self.DO_NOT_USE_37.setMaximum(2050)
        self.DO_NOT_USE_37.setValue(2019)

        self.DO_NOT_USE_35.addWidget(self.DO_NOT_USE_37, 1, 1, 1, 1)

        self.DO_NOT_USE_38 = QLabel(self.DO_NOT_USE_34)
        self.DO_NOT_USE_38.setObjectName(u"DO_NOT_USE_38")
        self.DO_NOT_USE_38.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.DO_NOT_USE_35.addWidget(self.DO_NOT_USE_38, 1, 0, 1, 1)

        self.DO_NOT_USE_39 = QComboBox(self.DO_NOT_USE_34)
        self.DO_NOT_USE_39.setObjectName(u"DO_NOT_USE_39")
        self.DO_NOT_USE_39.setEditable(True)

        self.DO_NOT_USE_35.addWidget(self.DO_NOT_USE_39, 0, 1, 1, 1)

        self.DO_NOT_USE_35.setColumnStretch(0, 1)
        self.DO_NOT_USE_35.setColumnStretch(1, 2)

        self.verticalLayout_65.addLayout(self.DO_NOT_USE_35)

        self.DO_NOT_USE_27.addTab(self.DO_NOT_USE_34, "")

        self.gridLayout_50.addWidget(self.DO_NOT_USE_27, 0, 0, 1, 1)


        self.gridLayout_49.addWidget(self.frame_6, 0, 0, 2, 1)

        self.verticalSpacer_5 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout_49.addItem(self.verticalSpacer_5, 0, 2, 1, 1)


        self.verticalLayout_28.addWidget(self.report__g_serv_total_dep__where_vdate__by_client_id)

        self.tabWidget_8.addTab(self.tab_tot_group_dep, "")
        self.tab_38 = myQWidget()
        self.tab_38.setObjectName(u"tab_38")
        self.gridLayout_7 = QGridLayout(self.tab_38)
        self.gridLayout_7.setObjectName(u"gridLayout_7")
        self.report__g_serv_total_you__where_vdate__by_client_id_2 = qcSelectReport(self.tab_38)
        self.report__g_serv_total_you__where_vdate__by_client_id_2.setObjectName(u"report__g_serv_total_you__where_vdate__by_client_id_2")
        self.gridLayout_51 = QGridLayout(self.report__g_serv_total_you__where_vdate__by_client_id_2)
        self.gridLayout_51.setObjectName(u"gridLayout_51")
        self.label_51 = QLabel(self.report__g_serv_total_you__where_vdate__by_client_id_2)
        self.label_51.setObjectName(u"label_51")

        self.gridLayout_51.addWidget(self.label_51, 2, 2, 1, 1)

        self.btn_serv_you_9 = QPushButton(self.report__g_serv_total_you__where_vdate__by_client_id_2)
        self.btn_serv_you_9.setObjectName(u"btn_serv_you_9")

        self.gridLayout_51.addWidget(self.btn_serv_you_9, 2, 0, 1, 1)

        self.pushButton_23 = QPushButton(self.report__g_serv_total_you__where_vdate__by_client_id_2)
        self.pushButton_23.setObjectName(u"pushButton_23")

        self.gridLayout_51.addWidget(self.pushButton_23, 2, 1, 1, 1)

        self.lineEdit_4 = QLineEdit(self.report__g_serv_total_you__where_vdate__by_client_id_2)
        self.lineEdit_4.setObjectName(u"lineEdit_4")

        self.gridLayout_51.addWidget(self.lineEdit_4, 2, 3, 1, 1)

        self.treeView_3 = QTreeView(self.report__g_serv_total_you__where_vdate__by_client_id_2)
        self.treeView_3.setObjectName(u"treeView_3")

        self.gridLayout_51.addWidget(self.treeView_3, 1, 1, 1, 3)

        self.t_main_for_dep_4 = QTableView(self.report__g_serv_total_you__where_vdate__by_client_id_2)
        self.t_main_for_dep_4.setObjectName(u"t_main_for_dep_4")

        self.gridLayout_51.addWidget(self.t_main_for_dep_4, 3, 0, 1, 4)

        self.frame_7 = QFrame(self.report__g_serv_total_you__where_vdate__by_client_id_2)
        self.frame_7.setObjectName(u"frame_7")
        self.frame_7.setFrameShape(QFrame.StyledPanel)
        self.frame_7.setFrameShadow(QFrame.Raised)
        self.gridLayout_52 = QGridLayout(self.frame_7)
        self.gridLayout_52.setObjectName(u"gridLayout_52")
        self.DO_NOT_USE_40 = myQTabWidget(self.frame_7)
        self.DO_NOT_USE_40.setObjectName(u"DO_NOT_USE_40")
        sizePolicy14.setHeightForWidth(self.DO_NOT_USE_40.sizePolicy().hasHeightForWidth())
        self.DO_NOT_USE_40.setSizePolicy(sizePolicy14)
        self.DO_NOT_USE_40.setMinimumSize(QSize(300, 0))
        self.DO_NOT_USE_41 = QWidget()
        self.DO_NOT_USE_41.setObjectName(u"DO_NOT_USE_41")
        self.verticalLayout_66 = QVBoxLayout(self.DO_NOT_USE_41)
        self.verticalLayout_66.setObjectName(u"verticalLayout_66")
        self.DO_NOT_USE_42 = QGridLayout()
        self.DO_NOT_USE_42.setObjectName(u"DO_NOT_USE_42")
        self.DO_NOT_USE_42.setHorizontalSpacing(0)
        self.DO_NOT_USE_43 = QDateEdit(self.DO_NOT_USE_41)
        self.DO_NOT_USE_43.setObjectName(u"DO_NOT_USE_43")

        self.DO_NOT_USE_42.addWidget(self.DO_NOT_USE_43, 1, 1, 1, 1)

        self.DO_NOT_USE_44 = QLabel(self.DO_NOT_USE_41)
        self.DO_NOT_USE_44.setObjectName(u"DO_NOT_USE_44")
        sizePolicy5.setHeightForWidth(self.DO_NOT_USE_44.sizePolicy().hasHeightForWidth())
        self.DO_NOT_USE_44.setSizePolicy(sizePolicy5)
        self.DO_NOT_USE_44.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.DO_NOT_USE_42.addWidget(self.DO_NOT_USE_44, 1, 0, 1, 1)

        self.DO_NOT_USE_45 = QLabel(self.DO_NOT_USE_41)
        self.DO_NOT_USE_45.setObjectName(u"DO_NOT_USE_45")
        sizePolicy5.setHeightForWidth(self.DO_NOT_USE_45.sizePolicy().hasHeightForWidth())
        self.DO_NOT_USE_45.setSizePolicy(sizePolicy5)
        self.DO_NOT_USE_45.setLayoutDirection(Qt.LeftToRight)
        self.DO_NOT_USE_45.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.DO_NOT_USE_42.addWidget(self.DO_NOT_USE_45, 0, 0, 1, 1)

        self.DO_NOT_USE_46 = QDateEdit(self.DO_NOT_USE_41)
        self.DO_NOT_USE_46.setObjectName(u"DO_NOT_USE_46")

        self.DO_NOT_USE_42.addWidget(self.DO_NOT_USE_46, 0, 1, 1, 1)

        self.verticalSpacer_6 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.DO_NOT_USE_42.addItem(self.verticalSpacer_6, 2, 1, 1, 1)

        self.DO_NOT_USE_42.setColumnStretch(0, 1)
        self.DO_NOT_USE_42.setColumnStretch(1, 2)

        self.verticalLayout_66.addLayout(self.DO_NOT_USE_42)

        self.DO_NOT_USE_40.addTab(self.DO_NOT_USE_41, "")
        self.DO_NOT_USE_47 = QWidget()
        self.DO_NOT_USE_47.setObjectName(u"DO_NOT_USE_47")
        self.verticalLayout_67 = QVBoxLayout(self.DO_NOT_USE_47)
        self.verticalLayout_67.setObjectName(u"verticalLayout_67")
        self.DO_NOT_USE_48 = QGridLayout()
        self.DO_NOT_USE_48.setObjectName(u"DO_NOT_USE_48")
        self.DO_NOT_USE_49 = QLabel(self.DO_NOT_USE_47)
        self.DO_NOT_USE_49.setObjectName(u"DO_NOT_USE_49")
        self.DO_NOT_USE_49.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.DO_NOT_USE_48.addWidget(self.DO_NOT_USE_49, 0, 0, 1, 1)

        self.DO_NOT_USE_50 = QSpinBox(self.DO_NOT_USE_47)
        self.DO_NOT_USE_50.setObjectName(u"DO_NOT_USE_50")
        self.DO_NOT_USE_50.setMinimum(1950)
        self.DO_NOT_USE_50.setMaximum(2050)
        self.DO_NOT_USE_50.setValue(2019)

        self.DO_NOT_USE_48.addWidget(self.DO_NOT_USE_50, 1, 1, 1, 1)

        self.DO_NOT_USE_51 = QLabel(self.DO_NOT_USE_47)
        self.DO_NOT_USE_51.setObjectName(u"DO_NOT_USE_51")
        self.DO_NOT_USE_51.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.DO_NOT_USE_48.addWidget(self.DO_NOT_USE_51, 1, 0, 1, 1)

        self.DO_NOT_USE_52 = QComboBox(self.DO_NOT_USE_47)
        self.DO_NOT_USE_52.setObjectName(u"DO_NOT_USE_52")
        self.DO_NOT_USE_52.setEditable(True)

        self.DO_NOT_USE_48.addWidget(self.DO_NOT_USE_52, 0, 1, 1, 1)

        self.DO_NOT_USE_48.setColumnStretch(0, 1)
        self.DO_NOT_USE_48.setColumnStretch(1, 2)

        self.verticalLayout_67.addLayout(self.DO_NOT_USE_48)

        self.DO_NOT_USE_40.addTab(self.DO_NOT_USE_47, "")

        self.gridLayout_52.addWidget(self.DO_NOT_USE_40, 0, 0, 1, 1)


        self.gridLayout_51.addWidget(self.frame_7, 0, 0, 2, 1)

        self.verticalSpacer_7 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout_51.addItem(self.verticalSpacer_7, 0, 2, 1, 1)


        self.gridLayout_7.addWidget(self.report__g_serv_total_you__where_vdate__by_client_id_2, 0, 0, 1, 1)

        self.tabWidget_8.addTab(self.tab_38, "")
        self.tab_44 = myQWidget()
        self.tab_44.setObjectName(u"tab_44")
        self.gridLayout_28 = QGridLayout(self.tab_44)
        self.gridLayout_28.setObjectName(u"gridLayout_28")
        self.widget_5 = QWidget(self.tab_44)
        self.widget_5.setObjectName(u"widget_5")
        self.gridLayout_101 = QGridLayout(self.widget_5)
        self.gridLayout_101.setSpacing(0)
        self.gridLayout_101.setObjectName(u"gridLayout_101")
        self.gridLayout_101.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_14 = QGridLayout()
        self.gridLayout_14.setObjectName(u"gridLayout_14")
        self.report__g_serv_total_dep_with_worker__where_vdate__by_client_id_by_dep_has_worker_id = qcSelectReport(self.widget_5)
        self.report__g_serv_total_dep_with_worker__where_vdate__by_client_id_by_dep_has_worker_id.setObjectName(u"report__g_serv_total_dep_with_worker__where_vdate__by_client_id_by_dep_has_worker_id")
        self.gridLayout_99 = QGridLayout(self.report__g_serv_total_dep_with_worker__where_vdate__by_client_id_by_dep_has_worker_id)
        self.gridLayout_99.setObjectName(u"gridLayout_99")
        self.table__dep_has_main_8 = QTableView(self.report__g_serv_total_dep_with_worker__where_vdate__by_client_id_by_dep_has_worker_id)
        self.table__dep_has_main_8.setObjectName(u"table__dep_has_main_8")

        self.gridLayout_99.addWidget(self.table__dep_has_main_8, 3, 0, 1, 2)

        self.pushButton_34 = QPushButton(self.report__g_serv_total_dep_with_worker__where_vdate__by_client_id_by_dep_has_worker_id)
        self.pushButton_34.setObjectName(u"pushButton_34")

        self.gridLayout_99.addWidget(self.pushButton_34, 2, 1, 1, 1)

        self.btn_serv_you_20 = QPushButton(self.report__g_serv_total_dep_with_worker__where_vdate__by_client_id_by_dep_has_worker_id)
        self.btn_serv_you_20.setObjectName(u"btn_serv_you_20")

        self.gridLayout_99.addWidget(self.btn_serv_you_20, 2, 0, 1, 1)

        self.frame_19 = QFrame(self.report__g_serv_total_dep_with_worker__where_vdate__by_client_id_by_dep_has_worker_id)
        self.frame_19.setObjectName(u"frame_19")
        self.frame_19.setFrameShape(QFrame.StyledPanel)
        self.frame_19.setFrameShadow(QFrame.Raised)
        self.gridLayout_100 = QGridLayout(self.frame_19)
        self.gridLayout_100.setObjectName(u"gridLayout_100")
        self.DO_NOT_USE_248 = myQTabWidget(self.frame_19)
        self.DO_NOT_USE_248.setObjectName(u"DO_NOT_USE_248")
        sizePolicy14.setHeightForWidth(self.DO_NOT_USE_248.sizePolicy().hasHeightForWidth())
        self.DO_NOT_USE_248.setSizePolicy(sizePolicy14)
        self.DO_NOT_USE_248.setMinimumSize(QSize(300, 0))
        self.DO_NOT_USE_249 = QWidget()
        self.DO_NOT_USE_249.setObjectName(u"DO_NOT_USE_249")
        self.verticalLayout_97 = QVBoxLayout(self.DO_NOT_USE_249)
        self.verticalLayout_97.setObjectName(u"verticalLayout_97")
        self.DO_NOT_USE_250 = QGridLayout()
        self.DO_NOT_USE_250.setObjectName(u"DO_NOT_USE_250")
        self.DO_NOT_USE_250.setHorizontalSpacing(0)
        self.DO_NOT_USE_251 = QDateEdit(self.DO_NOT_USE_249)
        self.DO_NOT_USE_251.setObjectName(u"DO_NOT_USE_251")

        self.DO_NOT_USE_250.addWidget(self.DO_NOT_USE_251, 1, 1, 1, 1)

        self.DO_NOT_USE_252 = QLabel(self.DO_NOT_USE_249)
        self.DO_NOT_USE_252.setObjectName(u"DO_NOT_USE_252")
        sizePolicy5.setHeightForWidth(self.DO_NOT_USE_252.sizePolicy().hasHeightForWidth())
        self.DO_NOT_USE_252.setSizePolicy(sizePolicy5)
        self.DO_NOT_USE_252.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.DO_NOT_USE_250.addWidget(self.DO_NOT_USE_252, 1, 0, 1, 1)

        self.DO_NOT_USE_253 = QLabel(self.DO_NOT_USE_249)
        self.DO_NOT_USE_253.setObjectName(u"DO_NOT_USE_253")
        sizePolicy5.setHeightForWidth(self.DO_NOT_USE_253.sizePolicy().hasHeightForWidth())
        self.DO_NOT_USE_253.setSizePolicy(sizePolicy5)
        self.DO_NOT_USE_253.setLayoutDirection(Qt.LeftToRight)
        self.DO_NOT_USE_253.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.DO_NOT_USE_250.addWidget(self.DO_NOT_USE_253, 0, 0, 1, 1)

        self.DO_NOT_USE_254 = QDateEdit(self.DO_NOT_USE_249)
        self.DO_NOT_USE_254.setObjectName(u"DO_NOT_USE_254")

        self.DO_NOT_USE_250.addWidget(self.DO_NOT_USE_254, 0, 1, 1, 1)

        self.DO_NOT_USE_250.setColumnStretch(0, 1)
        self.DO_NOT_USE_250.setColumnStretch(1, 2)

        self.verticalLayout_97.addLayout(self.DO_NOT_USE_250)

        self.DO_NOT_USE_248.addTab(self.DO_NOT_USE_249, "")
        self.DO_NOT_USE_255 = QWidget()
        self.DO_NOT_USE_255.setObjectName(u"DO_NOT_USE_255")
        self.verticalLayout_98 = QVBoxLayout(self.DO_NOT_USE_255)
        self.verticalLayout_98.setObjectName(u"verticalLayout_98")
        self.DO_NOT_USE_256 = QGridLayout()
        self.DO_NOT_USE_256.setObjectName(u"DO_NOT_USE_256")
        self.DO_NOT_USE_257 = QLabel(self.DO_NOT_USE_255)
        self.DO_NOT_USE_257.setObjectName(u"DO_NOT_USE_257")
        self.DO_NOT_USE_257.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.DO_NOT_USE_256.addWidget(self.DO_NOT_USE_257, 0, 0, 1, 1)

        self.DO_NOT_USE_258 = QSpinBox(self.DO_NOT_USE_255)
        self.DO_NOT_USE_258.setObjectName(u"DO_NOT_USE_258")
        self.DO_NOT_USE_258.setMinimum(1950)
        self.DO_NOT_USE_258.setMaximum(2050)
        self.DO_NOT_USE_258.setValue(2019)

        self.DO_NOT_USE_256.addWidget(self.DO_NOT_USE_258, 1, 1, 1, 1)

        self.DO_NOT_USE_259 = QLabel(self.DO_NOT_USE_255)
        self.DO_NOT_USE_259.setObjectName(u"DO_NOT_USE_259")
        self.DO_NOT_USE_259.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.DO_NOT_USE_256.addWidget(self.DO_NOT_USE_259, 1, 0, 1, 1)

        self.DO_NOT_USE_260 = QComboBox(self.DO_NOT_USE_255)
        self.DO_NOT_USE_260.setObjectName(u"DO_NOT_USE_260")
        self.DO_NOT_USE_260.setEditable(True)

        self.DO_NOT_USE_256.addWidget(self.DO_NOT_USE_260, 0, 1, 1, 1)

        self.DO_NOT_USE_256.setColumnStretch(0, 1)
        self.DO_NOT_USE_256.setColumnStretch(1, 2)

        self.verticalLayout_98.addLayout(self.DO_NOT_USE_256)

        self.DO_NOT_USE_248.addTab(self.DO_NOT_USE_255, "")

        self.gridLayout_100.addWidget(self.DO_NOT_USE_248, 0, 0, 1, 1)


        self.gridLayout_99.addWidget(self.frame_19, 1, 0, 1, 1)


        self.gridLayout_14.addWidget(self.report__g_serv_total_dep_with_worker__where_vdate__by_client_id_by_dep_has_worker_id, 1, 0, 1, 2)

        self.cbx_1_dep_has_worker__2 = myQComboBox(self.widget_5)
        self.cbx_1_dep_has_worker__2.setObjectName(u"cbx_1_dep_has_worker__2")
        sizePolicy6.setHeightForWidth(self.cbx_1_dep_has_worker__2.sizePolicy().hasHeightForWidth())
        self.cbx_1_dep_has_worker__2.setSizePolicy(sizePolicy6)
        self.cbx_1_dep_has_worker__2.setEditable(True)

        self.gridLayout_14.addWidget(self.cbx_1_dep_has_worker__2, 0, 1, 1, 1)

        self.label_63 = QLabel(self.widget_5)
        self.label_63.setObjectName(u"label_63")
        sizePolicy7.setHeightForWidth(self.label_63.sizePolicy().hasHeightForWidth())
        self.label_63.setSizePolicy(sizePolicy7)

        self.gridLayout_14.addWidget(self.label_63, 0, 0, 1, 1)


        self.gridLayout_101.addLayout(self.gridLayout_14, 0, 0, 1, 1)


        self.gridLayout_28.addWidget(self.widget_5, 0, 0, 1, 1)

        self.tabWidget_8.addTab(self.tab_44, "")
        self.tab_45 = myQWidget()
        self.tab_45.setObjectName(u"tab_45")
        self.gridLayout_33 = QGridLayout(self.tab_45)
        self.gridLayout_33.setObjectName(u"gridLayout_33")
        self.report__call_workers_total__where_period__by_worker_id = qcSelectReport(self.tab_45)
        self.report__call_workers_total__where_period__by_worker_id.setObjectName(u"report__call_workers_total__where_period__by_worker_id")
        self.gridLayout_55 = QGridLayout(self.report__call_workers_total__where_period__by_worker_id)
        self.gridLayout_55.setObjectName(u"gridLayout_55")
        self.label_65 = QLabel(self.report__call_workers_total__where_period__by_worker_id)
        self.label_65.setObjectName(u"label_65")

        self.gridLayout_55.addWidget(self.label_65, 2, 2, 1, 1)

        self.btn_serv_you_11 = QPushButton(self.report__call_workers_total__where_period__by_worker_id)
        self.btn_serv_you_11.setObjectName(u"btn_serv_you_11")

        self.gridLayout_55.addWidget(self.btn_serv_you_11, 2, 0, 1, 1)

        self.pushButton_25 = QPushButton(self.report__call_workers_total__where_period__by_worker_id)
        self.pushButton_25.setObjectName(u"pushButton_25")

        self.gridLayout_55.addWidget(self.pushButton_25, 2, 1, 1, 1)

        self.lineEdit_6 = QLineEdit(self.report__call_workers_total__where_period__by_worker_id)
        self.lineEdit_6.setObjectName(u"lineEdit_6")

        self.gridLayout_55.addWidget(self.lineEdit_6, 2, 3, 1, 1)

        self.treeView_5 = QTreeView(self.report__call_workers_total__where_period__by_worker_id)
        self.treeView_5.setObjectName(u"treeView_5")

        self.gridLayout_55.addWidget(self.treeView_5, 1, 1, 1, 3)

        self.t_main_for_dep_6 = QTableView(self.report__call_workers_total__where_period__by_worker_id)
        self.t_main_for_dep_6.setObjectName(u"t_main_for_dep_6")

        self.gridLayout_55.addWidget(self.t_main_for_dep_6, 3, 0, 1, 4)

        self.frame_9 = QFrame(self.report__call_workers_total__where_period__by_worker_id)
        self.frame_9.setObjectName(u"frame_9")
        self.frame_9.setFrameShape(QFrame.StyledPanel)
        self.frame_9.setFrameShadow(QFrame.Raised)
        self.gridLayout_56 = QGridLayout(self.frame_9)
        self.gridLayout_56.setObjectName(u"gridLayout_56")
        self.DO_NOT_USE_118 = myQTabWidget(self.frame_9)
        self.DO_NOT_USE_118.setObjectName(u"DO_NOT_USE_118")
        sizePolicy14.setHeightForWidth(self.DO_NOT_USE_118.sizePolicy().hasHeightForWidth())
        self.DO_NOT_USE_118.setSizePolicy(sizePolicy14)
        self.DO_NOT_USE_118.setMinimumSize(QSize(300, 0))
        self.DO_NOT_USE_119 = QWidget()
        self.DO_NOT_USE_119.setObjectName(u"DO_NOT_USE_119")
        self.verticalLayout_78 = QVBoxLayout(self.DO_NOT_USE_119)
        self.verticalLayout_78.setObjectName(u"verticalLayout_78")
        self.DO_NOT_USE_120 = QGridLayout()
        self.DO_NOT_USE_120.setObjectName(u"DO_NOT_USE_120")
        self.DO_NOT_USE_120.setHorizontalSpacing(0)
        self.DO_NOT_USE_121 = QDateEdit(self.DO_NOT_USE_119)
        self.DO_NOT_USE_121.setObjectName(u"DO_NOT_USE_121")

        self.DO_NOT_USE_120.addWidget(self.DO_NOT_USE_121, 1, 1, 1, 1)

        self.DO_NOT_USE_122 = QLabel(self.DO_NOT_USE_119)
        self.DO_NOT_USE_122.setObjectName(u"DO_NOT_USE_122")
        sizePolicy5.setHeightForWidth(self.DO_NOT_USE_122.sizePolicy().hasHeightForWidth())
        self.DO_NOT_USE_122.setSizePolicy(sizePolicy5)
        self.DO_NOT_USE_122.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.DO_NOT_USE_120.addWidget(self.DO_NOT_USE_122, 1, 0, 1, 1)

        self.DO_NOT_USE_124 = QDateEdit(self.DO_NOT_USE_119)
        self.DO_NOT_USE_124.setObjectName(u"DO_NOT_USE_124")

        self.DO_NOT_USE_120.addWidget(self.DO_NOT_USE_124, 0, 1, 1, 1)

        self.DO_NOT_USE_123 = QLabel(self.DO_NOT_USE_119)
        self.DO_NOT_USE_123.setObjectName(u"DO_NOT_USE_123")
        sizePolicy5.setHeightForWidth(self.DO_NOT_USE_123.sizePolicy().hasHeightForWidth())
        self.DO_NOT_USE_123.setSizePolicy(sizePolicy5)
        self.DO_NOT_USE_123.setLayoutDirection(Qt.LeftToRight)
        self.DO_NOT_USE_123.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.DO_NOT_USE_120.addWidget(self.DO_NOT_USE_123, 0, 0, 1, 1)

        self.verticalSpacer_10 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.DO_NOT_USE_120.addItem(self.verticalSpacer_10, 2, 1, 1, 1)

        self.DO_NOT_USE_120.setColumnStretch(0, 1)

        self.verticalLayout_78.addLayout(self.DO_NOT_USE_120)

        self.DO_NOT_USE_118.addTab(self.DO_NOT_USE_119, "")
        self.DO_NOT_USE_125 = QWidget()
        self.DO_NOT_USE_125.setObjectName(u"DO_NOT_USE_125")
        self.verticalLayout_79 = QVBoxLayout(self.DO_NOT_USE_125)
        self.verticalLayout_79.setObjectName(u"verticalLayout_79")
        self.DO_NOT_USE_126 = QGridLayout()
        self.DO_NOT_USE_126.setObjectName(u"DO_NOT_USE_126")
        self.DO_NOT_USE_127 = QLabel(self.DO_NOT_USE_125)
        self.DO_NOT_USE_127.setObjectName(u"DO_NOT_USE_127")
        self.DO_NOT_USE_127.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.DO_NOT_USE_126.addWidget(self.DO_NOT_USE_127, 0, 0, 1, 1)

        self.DO_NOT_USE_128 = QSpinBox(self.DO_NOT_USE_125)
        self.DO_NOT_USE_128.setObjectName(u"DO_NOT_USE_128")
        self.DO_NOT_USE_128.setMinimum(1950)
        self.DO_NOT_USE_128.setMaximum(2050)
        self.DO_NOT_USE_128.setValue(2019)

        self.DO_NOT_USE_126.addWidget(self.DO_NOT_USE_128, 1, 1, 1, 1)

        self.DO_NOT_USE_129 = QLabel(self.DO_NOT_USE_125)
        self.DO_NOT_USE_129.setObjectName(u"DO_NOT_USE_129")
        self.DO_NOT_USE_129.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.DO_NOT_USE_126.addWidget(self.DO_NOT_USE_129, 1, 0, 1, 1)

        self.DO_NOT_USE_130 = QComboBox(self.DO_NOT_USE_125)
        self.DO_NOT_USE_130.setObjectName(u"DO_NOT_USE_130")
        self.DO_NOT_USE_130.setEditable(True)

        self.DO_NOT_USE_126.addWidget(self.DO_NOT_USE_130, 0, 1, 1, 1)

        self.DO_NOT_USE_126.setColumnStretch(0, 1)
        self.DO_NOT_USE_126.setColumnStretch(1, 2)

        self.verticalLayout_79.addLayout(self.DO_NOT_USE_126)

        self.DO_NOT_USE_118.addTab(self.DO_NOT_USE_125, "")

        self.gridLayout_56.addWidget(self.DO_NOT_USE_118, 0, 0, 1, 1)


        self.gridLayout_55.addWidget(self.frame_9, 0, 0, 2, 1)


        self.gridLayout_33.addWidget(self.report__call_workers_total__where_period__by_worker_id, 0, 0, 1, 1)

        self.tabWidget_8.addTab(self.tab_45, "")

        self.verticalLayout_10.addWidget(self.tabWidget_8)

        self.tabs_total.addTab(self.tab_tot_group, "")
        self.tab_41 = myQWidget()
        self.tab_41.setObjectName(u"tab_41")
        self.gridLayout_89 = QGridLayout(self.tab_41)
        self.gridLayout_89.setObjectName(u"gridLayout_89")
        self.tabWidget_11 = myQTabWidget(self.tab_41)
        self.tabWidget_11.setObjectName(u"tabWidget_11")
        self.tab_tot_group_dep_2 = myQWidget()
        self.tab_tot_group_dep_2.setObjectName(u"tab_tot_group_dep_2")
        self.verticalLayout_29 = QVBoxLayout(self.tab_tot_group_dep_2)
        self.verticalLayout_29.setObjectName(u"verticalLayout_29")
        self.report__g_serv_list_for_dep_for_year__where_vdate__by_client_id = qcSelectReport(self.tab_tot_group_dep_2)
        self.report__g_serv_list_for_dep_for_year__where_vdate__by_client_id.setObjectName(u"report__g_serv_list_for_dep_for_year__where_vdate__by_client_id")
        self.gridLayout_78 = QGridLayout(self.report__g_serv_list_for_dep_for_year__where_vdate__by_client_id)
        self.gridLayout_78.setObjectName(u"gridLayout_78")
        self.label_72 = QLabel(self.report__g_serv_list_for_dep_for_year__where_vdate__by_client_id)
        self.label_72.setObjectName(u"label_72")

        self.gridLayout_78.addWidget(self.label_72, 2, 2, 1, 1)

        self.btn_serv_you_16 = QPushButton(self.report__g_serv_list_for_dep_for_year__where_vdate__by_client_id)
        self.btn_serv_you_16.setObjectName(u"btn_serv_you_16")

        self.gridLayout_78.addWidget(self.btn_serv_you_16, 2, 0, 1, 1)

        self.pushButton_30 = QPushButton(self.report__g_serv_list_for_dep_for_year__where_vdate__by_client_id)
        self.pushButton_30.setObjectName(u"pushButton_30")

        self.gridLayout_78.addWidget(self.pushButton_30, 2, 1, 1, 1)

        self.lineEdit_11 = QLineEdit(self.report__g_serv_list_for_dep_for_year__where_vdate__by_client_id)
        self.lineEdit_11.setObjectName(u"lineEdit_11")

        self.gridLayout_78.addWidget(self.lineEdit_11, 2, 3, 1, 1)

        self.treeView_9 = QTreeView(self.report__g_serv_list_for_dep_for_year__where_vdate__by_client_id)
        self.treeView_9.setObjectName(u"treeView_9")

        self.gridLayout_78.addWidget(self.treeView_9, 1, 1, 1, 3)

        self.t_main_for_dep_10 = QTableView(self.report__g_serv_list_for_dep_for_year__where_vdate__by_client_id)
        self.t_main_for_dep_10.setObjectName(u"t_main_for_dep_10")

        self.gridLayout_78.addWidget(self.t_main_for_dep_10, 3, 0, 1, 4)

        self.frame_15 = QFrame(self.report__g_serv_list_for_dep_for_year__where_vdate__by_client_id)
        self.frame_15.setObjectName(u"frame_15")
        self.frame_15.setFrameShape(QFrame.StyledPanel)
        self.frame_15.setFrameShadow(QFrame.Raised)
        self.gridLayout_79 = QGridLayout(self.frame_15)
        self.gridLayout_79.setObjectName(u"gridLayout_79")
        self.DO_NOT_USE_183 = myQTabWidget(self.frame_15)
        self.DO_NOT_USE_183.setObjectName(u"DO_NOT_USE_183")
        sizePolicy14.setHeightForWidth(self.DO_NOT_USE_183.sizePolicy().hasHeightForWidth())
        self.DO_NOT_USE_183.setSizePolicy(sizePolicy14)
        self.DO_NOT_USE_183.setMinimumSize(QSize(300, 0))
        self.DO_NOT_USE_184 = QWidget()
        self.DO_NOT_USE_184.setObjectName(u"DO_NOT_USE_184")
        self.verticalLayout_88 = QVBoxLayout(self.DO_NOT_USE_184)
        self.verticalLayout_88.setObjectName(u"verticalLayout_88")
        self.DO_NOT_USE_185 = QGridLayout()
        self.DO_NOT_USE_185.setObjectName(u"DO_NOT_USE_185")
        self.DO_NOT_USE_185.setHorizontalSpacing(0)
        self.DO_NOT_USE_186 = QDateEdit(self.DO_NOT_USE_184)
        self.DO_NOT_USE_186.setObjectName(u"DO_NOT_USE_186")

        self.DO_NOT_USE_185.addWidget(self.DO_NOT_USE_186, 1, 1, 1, 1)

        self.DO_NOT_USE_187 = QLabel(self.DO_NOT_USE_184)
        self.DO_NOT_USE_187.setObjectName(u"DO_NOT_USE_187")
        sizePolicy5.setHeightForWidth(self.DO_NOT_USE_187.sizePolicy().hasHeightForWidth())
        self.DO_NOT_USE_187.setSizePolicy(sizePolicy5)
        self.DO_NOT_USE_187.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.DO_NOT_USE_185.addWidget(self.DO_NOT_USE_187, 1, 0, 1, 1)

        self.DO_NOT_USE_188 = QLabel(self.DO_NOT_USE_184)
        self.DO_NOT_USE_188.setObjectName(u"DO_NOT_USE_188")
        sizePolicy5.setHeightForWidth(self.DO_NOT_USE_188.sizePolicy().hasHeightForWidth())
        self.DO_NOT_USE_188.setSizePolicy(sizePolicy5)
        self.DO_NOT_USE_188.setLayoutDirection(Qt.LeftToRight)
        self.DO_NOT_USE_188.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.DO_NOT_USE_185.addWidget(self.DO_NOT_USE_188, 0, 0, 1, 1)

        self.DO_NOT_USE_189 = QDateEdit(self.DO_NOT_USE_184)
        self.DO_NOT_USE_189.setObjectName(u"DO_NOT_USE_189")

        self.DO_NOT_USE_185.addWidget(self.DO_NOT_USE_189, 0, 1, 1, 1)

        self.verticalSpacer_14 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.DO_NOT_USE_185.addItem(self.verticalSpacer_14, 2, 1, 1, 1)

        self.DO_NOT_USE_185.setColumnStretch(0, 1)
        self.DO_NOT_USE_185.setColumnStretch(1, 2)

        self.verticalLayout_88.addLayout(self.DO_NOT_USE_185)

        self.DO_NOT_USE_183.addTab(self.DO_NOT_USE_184, "")
        self.DO_NOT_USE_190 = QWidget()
        self.DO_NOT_USE_190.setObjectName(u"DO_NOT_USE_190")
        self.verticalLayout_89 = QVBoxLayout(self.DO_NOT_USE_190)
        self.verticalLayout_89.setObjectName(u"verticalLayout_89")
        self.DO_NOT_USE_191 = QGridLayout()
        self.DO_NOT_USE_191.setObjectName(u"DO_NOT_USE_191")
        self.DO_NOT_USE_192 = QLabel(self.DO_NOT_USE_190)
        self.DO_NOT_USE_192.setObjectName(u"DO_NOT_USE_192")
        self.DO_NOT_USE_192.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.DO_NOT_USE_191.addWidget(self.DO_NOT_USE_192, 0, 0, 1, 1)

        self.DO_NOT_USE_193 = QSpinBox(self.DO_NOT_USE_190)
        self.DO_NOT_USE_193.setObjectName(u"DO_NOT_USE_193")
        self.DO_NOT_USE_193.setMinimum(1950)
        self.DO_NOT_USE_193.setMaximum(2050)
        self.DO_NOT_USE_193.setValue(2019)

        self.DO_NOT_USE_191.addWidget(self.DO_NOT_USE_193, 1, 1, 1, 1)

        self.DO_NOT_USE_194 = QLabel(self.DO_NOT_USE_190)
        self.DO_NOT_USE_194.setObjectName(u"DO_NOT_USE_194")
        self.DO_NOT_USE_194.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.DO_NOT_USE_191.addWidget(self.DO_NOT_USE_194, 1, 0, 1, 1)

        self.DO_NOT_USE_195 = QComboBox(self.DO_NOT_USE_190)
        self.DO_NOT_USE_195.setObjectName(u"DO_NOT_USE_195")
        self.DO_NOT_USE_195.setEditable(True)

        self.DO_NOT_USE_191.addWidget(self.DO_NOT_USE_195, 0, 1, 1, 1)

        self.DO_NOT_USE_191.setColumnStretch(0, 1)
        self.DO_NOT_USE_191.setColumnStretch(1, 2)

        self.verticalLayout_89.addLayout(self.DO_NOT_USE_191)

        self.DO_NOT_USE_183.addTab(self.DO_NOT_USE_190, "")

        self.gridLayout_79.addWidget(self.DO_NOT_USE_183, 0, 0, 1, 1)


        self.gridLayout_78.addWidget(self.frame_15, 0, 0, 2, 1)

        self.verticalSpacer_15 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout_78.addItem(self.verticalSpacer_15, 0, 2, 1, 1)


        self.verticalLayout_29.addWidget(self.report__g_serv_list_for_dep_for_year__where_vdate__by_client_id)

        self.tabWidget_11.addTab(self.tab_tot_group_dep_2, "")
        self.tab_50 = myQWidget()
        self.tab_50.setObjectName(u"tab_50")
        self.gridLayout_80 = QGridLayout(self.tab_50)
        self.gridLayout_80.setObjectName(u"gridLayout_80")
        self.report__g_serv_total_you__where_vdate__by_client_id_3 = qcSelectReport(self.tab_50)
        self.report__g_serv_total_you__where_vdate__by_client_id_3.setObjectName(u"report__g_serv_total_you__where_vdate__by_client_id_3")
        self.gridLayout_81 = QGridLayout(self.report__g_serv_total_you__where_vdate__by_client_id_3)
        self.gridLayout_81.setObjectName(u"gridLayout_81")
        self.label_73 = QLabel(self.report__g_serv_total_you__where_vdate__by_client_id_3)
        self.label_73.setObjectName(u"label_73")

        self.gridLayout_81.addWidget(self.label_73, 2, 2, 1, 1)

        self.btn_serv_you_17 = QPushButton(self.report__g_serv_total_you__where_vdate__by_client_id_3)
        self.btn_serv_you_17.setObjectName(u"btn_serv_you_17")

        self.gridLayout_81.addWidget(self.btn_serv_you_17, 2, 0, 1, 1)

        self.pushButton_31 = QPushButton(self.report__g_serv_total_you__where_vdate__by_client_id_3)
        self.pushButton_31.setObjectName(u"pushButton_31")

        self.gridLayout_81.addWidget(self.pushButton_31, 2, 1, 1, 1)

        self.lineEdit_12 = QLineEdit(self.report__g_serv_total_you__where_vdate__by_client_id_3)
        self.lineEdit_12.setObjectName(u"lineEdit_12")

        self.gridLayout_81.addWidget(self.lineEdit_12, 2, 3, 1, 1)

        self.treeView_10 = QTreeView(self.report__g_serv_total_you__where_vdate__by_client_id_3)
        self.treeView_10.setObjectName(u"treeView_10")

        self.gridLayout_81.addWidget(self.treeView_10, 1, 1, 1, 3)

        self.t_main_for_dep_11 = QTableView(self.report__g_serv_total_you__where_vdate__by_client_id_3)
        self.t_main_for_dep_11.setObjectName(u"t_main_for_dep_11")

        self.gridLayout_81.addWidget(self.t_main_for_dep_11, 3, 0, 1, 4)

        self.frame_16 = QFrame(self.report__g_serv_total_you__where_vdate__by_client_id_3)
        self.frame_16.setObjectName(u"frame_16")
        self.frame_16.setFrameShape(QFrame.StyledPanel)
        self.frame_16.setFrameShadow(QFrame.Raised)
        self.gridLayout_82 = QGridLayout(self.frame_16)
        self.gridLayout_82.setObjectName(u"gridLayout_82")
        self.DO_NOT_USE_196 = myQTabWidget(self.frame_16)
        self.DO_NOT_USE_196.setObjectName(u"DO_NOT_USE_196")
        sizePolicy14.setHeightForWidth(self.DO_NOT_USE_196.sizePolicy().hasHeightForWidth())
        self.DO_NOT_USE_196.setSizePolicy(sizePolicy14)
        self.DO_NOT_USE_196.setMinimumSize(QSize(300, 0))
        self.DO_NOT_USE_197 = QWidget()
        self.DO_NOT_USE_197.setObjectName(u"DO_NOT_USE_197")
        self.verticalLayout_90 = QVBoxLayout(self.DO_NOT_USE_197)
        self.verticalLayout_90.setObjectName(u"verticalLayout_90")
        self.DO_NOT_USE_198 = QGridLayout()
        self.DO_NOT_USE_198.setObjectName(u"DO_NOT_USE_198")
        self.DO_NOT_USE_198.setHorizontalSpacing(0)
        self.DO_NOT_USE_199 = QDateEdit(self.DO_NOT_USE_197)
        self.DO_NOT_USE_199.setObjectName(u"DO_NOT_USE_199")

        self.DO_NOT_USE_198.addWidget(self.DO_NOT_USE_199, 1, 1, 1, 1)

        self.DO_NOT_USE_200 = QLabel(self.DO_NOT_USE_197)
        self.DO_NOT_USE_200.setObjectName(u"DO_NOT_USE_200")
        sizePolicy5.setHeightForWidth(self.DO_NOT_USE_200.sizePolicy().hasHeightForWidth())
        self.DO_NOT_USE_200.setSizePolicy(sizePolicy5)
        self.DO_NOT_USE_200.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.DO_NOT_USE_198.addWidget(self.DO_NOT_USE_200, 1, 0, 1, 1)

        self.DO_NOT_USE_201 = QLabel(self.DO_NOT_USE_197)
        self.DO_NOT_USE_201.setObjectName(u"DO_NOT_USE_201")
        sizePolicy5.setHeightForWidth(self.DO_NOT_USE_201.sizePolicy().hasHeightForWidth())
        self.DO_NOT_USE_201.setSizePolicy(sizePolicy5)
        self.DO_NOT_USE_201.setLayoutDirection(Qt.LeftToRight)
        self.DO_NOT_USE_201.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.DO_NOT_USE_198.addWidget(self.DO_NOT_USE_201, 0, 0, 1, 1)

        self.DO_NOT_USE_202 = QDateEdit(self.DO_NOT_USE_197)
        self.DO_NOT_USE_202.setObjectName(u"DO_NOT_USE_202")

        self.DO_NOT_USE_198.addWidget(self.DO_NOT_USE_202, 0, 1, 1, 1)

        self.verticalSpacer_16 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.DO_NOT_USE_198.addItem(self.verticalSpacer_16, 2, 1, 1, 1)

        self.DO_NOT_USE_198.setColumnStretch(0, 1)
        self.DO_NOT_USE_198.setColumnStretch(1, 2)

        self.verticalLayout_90.addLayout(self.DO_NOT_USE_198)

        self.DO_NOT_USE_196.addTab(self.DO_NOT_USE_197, "")
        self.DO_NOT_USE_203 = QWidget()
        self.DO_NOT_USE_203.setObjectName(u"DO_NOT_USE_203")
        self.verticalLayout_91 = QVBoxLayout(self.DO_NOT_USE_203)
        self.verticalLayout_91.setObjectName(u"verticalLayout_91")
        self.DO_NOT_USE_204 = QGridLayout()
        self.DO_NOT_USE_204.setObjectName(u"DO_NOT_USE_204")
        self.DO_NOT_USE_205 = QLabel(self.DO_NOT_USE_203)
        self.DO_NOT_USE_205.setObjectName(u"DO_NOT_USE_205")
        self.DO_NOT_USE_205.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.DO_NOT_USE_204.addWidget(self.DO_NOT_USE_205, 0, 0, 1, 1)

        self.DO_NOT_USE_206 = QSpinBox(self.DO_NOT_USE_203)
        self.DO_NOT_USE_206.setObjectName(u"DO_NOT_USE_206")
        self.DO_NOT_USE_206.setMinimum(1950)
        self.DO_NOT_USE_206.setMaximum(2050)
        self.DO_NOT_USE_206.setValue(2019)

        self.DO_NOT_USE_204.addWidget(self.DO_NOT_USE_206, 1, 1, 1, 1)

        self.DO_NOT_USE_207 = QLabel(self.DO_NOT_USE_203)
        self.DO_NOT_USE_207.setObjectName(u"DO_NOT_USE_207")
        self.DO_NOT_USE_207.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.DO_NOT_USE_204.addWidget(self.DO_NOT_USE_207, 1, 0, 1, 1)

        self.DO_NOT_USE_208 = QComboBox(self.DO_NOT_USE_203)
        self.DO_NOT_USE_208.setObjectName(u"DO_NOT_USE_208")
        self.DO_NOT_USE_208.setEditable(True)

        self.DO_NOT_USE_204.addWidget(self.DO_NOT_USE_208, 0, 1, 1, 1)

        self.DO_NOT_USE_204.setColumnStretch(0, 1)
        self.DO_NOT_USE_204.setColumnStretch(1, 2)

        self.verticalLayout_91.addLayout(self.DO_NOT_USE_204)

        self.DO_NOT_USE_196.addTab(self.DO_NOT_USE_203, "")

        self.gridLayout_82.addWidget(self.DO_NOT_USE_196, 0, 0, 1, 1)


        self.gridLayout_81.addWidget(self.frame_16, 0, 0, 2, 1)

        self.verticalSpacer_17 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout_81.addItem(self.verticalSpacer_17, 0, 2, 1, 1)


        self.gridLayout_80.addWidget(self.report__g_serv_total_you__where_vdate__by_client_id_3, 0, 0, 1, 1)

        self.tabWidget_11.addTab(self.tab_50, "")
        self.tab_51 = myQWidget()
        self.tab_51.setObjectName(u"tab_51")
        self.gridLayout_84 = QGridLayout(self.tab_51)
        self.gridLayout_84.setObjectName(u"gridLayout_84")
        self.gridLayout_83 = QGridLayout()
        self.gridLayout_83.setObjectName(u"gridLayout_83")
        self.report__g_serv_total_dep_with_worker__where_vdate__by_client_id_by_dep_has_worker_id__2 = qcSelectReport(self.tab_51)
        self.report__g_serv_total_dep_with_worker__where_vdate__by_client_id_by_dep_has_worker_id__2.setObjectName(u"report__g_serv_total_dep_with_worker__where_vdate__by_client_id_by_dep_has_worker_id__2")
        self.gridLayout_102 = QGridLayout(self.report__g_serv_total_dep_with_worker__where_vdate__by_client_id_by_dep_has_worker_id__2)
        self.gridLayout_102.setObjectName(u"gridLayout_102")
        self.table__dep_has_main_9 = QTableView(self.report__g_serv_total_dep_with_worker__where_vdate__by_client_id_by_dep_has_worker_id__2)
        self.table__dep_has_main_9.setObjectName(u"table__dep_has_main_9")

        self.gridLayout_102.addWidget(self.table__dep_has_main_9, 3, 0, 1, 2)

        self.pushButton_35 = QPushButton(self.report__g_serv_total_dep_with_worker__where_vdate__by_client_id_by_dep_has_worker_id__2)
        self.pushButton_35.setObjectName(u"pushButton_35")

        self.gridLayout_102.addWidget(self.pushButton_35, 2, 1, 1, 1)

        self.btn_serv_you_21 = QPushButton(self.report__g_serv_total_dep_with_worker__where_vdate__by_client_id_by_dep_has_worker_id__2)
        self.btn_serv_you_21.setObjectName(u"btn_serv_you_21")

        self.gridLayout_102.addWidget(self.btn_serv_you_21, 2, 0, 1, 1)

        self.frame_20 = QFrame(self.report__g_serv_total_dep_with_worker__where_vdate__by_client_id_by_dep_has_worker_id__2)
        self.frame_20.setObjectName(u"frame_20")
        self.frame_20.setFrameShape(QFrame.StyledPanel)
        self.frame_20.setFrameShadow(QFrame.Raised)
        self.gridLayout_103 = QGridLayout(self.frame_20)
        self.gridLayout_103.setObjectName(u"gridLayout_103")
        self.DO_NOT_USE_261 = myQTabWidget(self.frame_20)
        self.DO_NOT_USE_261.setObjectName(u"DO_NOT_USE_261")
        sizePolicy14.setHeightForWidth(self.DO_NOT_USE_261.sizePolicy().hasHeightForWidth())
        self.DO_NOT_USE_261.setSizePolicy(sizePolicy14)
        self.DO_NOT_USE_261.setMinimumSize(QSize(300, 0))
        self.DO_NOT_USE_262 = QWidget()
        self.DO_NOT_USE_262.setObjectName(u"DO_NOT_USE_262")
        self.verticalLayout_99 = QVBoxLayout(self.DO_NOT_USE_262)
        self.verticalLayout_99.setObjectName(u"verticalLayout_99")
        self.DO_NOT_USE_263 = QGridLayout()
        self.DO_NOT_USE_263.setObjectName(u"DO_NOT_USE_263")
        self.DO_NOT_USE_263.setHorizontalSpacing(0)
        self.DO_NOT_USE_264 = QDateEdit(self.DO_NOT_USE_262)
        self.DO_NOT_USE_264.setObjectName(u"DO_NOT_USE_264")

        self.DO_NOT_USE_263.addWidget(self.DO_NOT_USE_264, 1, 1, 1, 1)

        self.DO_NOT_USE_265 = QLabel(self.DO_NOT_USE_262)
        self.DO_NOT_USE_265.setObjectName(u"DO_NOT_USE_265")
        sizePolicy5.setHeightForWidth(self.DO_NOT_USE_265.sizePolicy().hasHeightForWidth())
        self.DO_NOT_USE_265.setSizePolicy(sizePolicy5)
        self.DO_NOT_USE_265.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.DO_NOT_USE_263.addWidget(self.DO_NOT_USE_265, 1, 0, 1, 1)

        self.DO_NOT_USE_266 = QLabel(self.DO_NOT_USE_262)
        self.DO_NOT_USE_266.setObjectName(u"DO_NOT_USE_266")
        sizePolicy5.setHeightForWidth(self.DO_NOT_USE_266.sizePolicy().hasHeightForWidth())
        self.DO_NOT_USE_266.setSizePolicy(sizePolicy5)
        self.DO_NOT_USE_266.setLayoutDirection(Qt.LeftToRight)
        self.DO_NOT_USE_266.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.DO_NOT_USE_263.addWidget(self.DO_NOT_USE_266, 0, 0, 1, 1)

        self.DO_NOT_USE_267 = QDateEdit(self.DO_NOT_USE_262)
        self.DO_NOT_USE_267.setObjectName(u"DO_NOT_USE_267")

        self.DO_NOT_USE_263.addWidget(self.DO_NOT_USE_267, 0, 1, 1, 1)

        self.DO_NOT_USE_263.setColumnStretch(0, 1)
        self.DO_NOT_USE_263.setColumnStretch(1, 2)

        self.verticalLayout_99.addLayout(self.DO_NOT_USE_263)

        self.DO_NOT_USE_261.addTab(self.DO_NOT_USE_262, "")
        self.DO_NOT_USE_268 = QWidget()
        self.DO_NOT_USE_268.setObjectName(u"DO_NOT_USE_268")
        self.verticalLayout_100 = QVBoxLayout(self.DO_NOT_USE_268)
        self.verticalLayout_100.setObjectName(u"verticalLayout_100")
        self.DO_NOT_USE_269 = QGridLayout()
        self.DO_NOT_USE_269.setObjectName(u"DO_NOT_USE_269")
        self.DO_NOT_USE_270 = QLabel(self.DO_NOT_USE_268)
        self.DO_NOT_USE_270.setObjectName(u"DO_NOT_USE_270")
        self.DO_NOT_USE_270.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.DO_NOT_USE_269.addWidget(self.DO_NOT_USE_270, 0, 0, 1, 1)

        self.DO_NOT_USE_271 = QSpinBox(self.DO_NOT_USE_268)
        self.DO_NOT_USE_271.setObjectName(u"DO_NOT_USE_271")
        self.DO_NOT_USE_271.setMinimum(1950)
        self.DO_NOT_USE_271.setMaximum(2050)
        self.DO_NOT_USE_271.setValue(2019)

        self.DO_NOT_USE_269.addWidget(self.DO_NOT_USE_271, 1, 1, 1, 1)

        self.DO_NOT_USE_272 = QLabel(self.DO_NOT_USE_268)
        self.DO_NOT_USE_272.setObjectName(u"DO_NOT_USE_272")
        self.DO_NOT_USE_272.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.DO_NOT_USE_269.addWidget(self.DO_NOT_USE_272, 1, 0, 1, 1)

        self.DO_NOT_USE_273 = QComboBox(self.DO_NOT_USE_268)
        self.DO_NOT_USE_273.setObjectName(u"DO_NOT_USE_273")
        self.DO_NOT_USE_273.setEditable(True)

        self.DO_NOT_USE_269.addWidget(self.DO_NOT_USE_273, 0, 1, 1, 1)

        self.DO_NOT_USE_269.setColumnStretch(0, 1)
        self.DO_NOT_USE_269.setColumnStretch(1, 2)

        self.verticalLayout_100.addLayout(self.DO_NOT_USE_269)

        self.DO_NOT_USE_261.addTab(self.DO_NOT_USE_268, "")

        self.gridLayout_103.addWidget(self.DO_NOT_USE_261, 0, 0, 1, 1)


        self.gridLayout_102.addWidget(self.frame_20, 1, 0, 1, 1)


        self.gridLayout_83.addWidget(self.report__g_serv_total_dep_with_worker__where_vdate__by_client_id_by_dep_has_worker_id__2, 1, 0, 1, 2)

        self.cbx_1_dep_has_worker__3 = myQComboBox(self.tab_51)
        self.cbx_1_dep_has_worker__3.setObjectName(u"cbx_1_dep_has_worker__3")
        sizePolicy6.setHeightForWidth(self.cbx_1_dep_has_worker__3.sizePolicy().hasHeightForWidth())
        self.cbx_1_dep_has_worker__3.setSizePolicy(sizePolicy6)
        self.cbx_1_dep_has_worker__3.setEditable(True)

        self.gridLayout_83.addWidget(self.cbx_1_dep_has_worker__3, 0, 1, 1, 1)

        self.label_64 = QLabel(self.tab_51)
        self.label_64.setObjectName(u"label_64")
        sizePolicy7.setHeightForWidth(self.label_64.sizePolicy().hasHeightForWidth())
        self.label_64.setSizePolicy(sizePolicy7)

        self.gridLayout_83.addWidget(self.label_64, 0, 0, 1, 1)


        self.gridLayout_84.addLayout(self.gridLayout_83, 0, 0, 1, 1)

        self.tabWidget_11.addTab(self.tab_51, "")
        self.tab_52 = myQWidget()
        self.tab_52.setObjectName(u"tab_52")
        self.gridLayout_86 = QGridLayout(self.tab_52)
        self.gridLayout_86.setObjectName(u"gridLayout_86")
        self.report__call_workers_total__where_period__by_worker_id_2 = qcSelectReport(self.tab_52)
        self.report__call_workers_total__where_period__by_worker_id_2.setObjectName(u"report__call_workers_total__where_period__by_worker_id_2")
        self.gridLayout_87 = QGridLayout(self.report__call_workers_total__where_period__by_worker_id_2)
        self.gridLayout_87.setObjectName(u"gridLayout_87")
        self.label_76 = QLabel(self.report__call_workers_total__where_period__by_worker_id_2)
        self.label_76.setObjectName(u"label_76")

        self.gridLayout_87.addWidget(self.label_76, 2, 2, 1, 1)

        self.btn_serv_you_19 = QPushButton(self.report__call_workers_total__where_period__by_worker_id_2)
        self.btn_serv_you_19.setObjectName(u"btn_serv_you_19")

        self.gridLayout_87.addWidget(self.btn_serv_you_19, 2, 0, 1, 1)

        self.pushButton_33 = QPushButton(self.report__call_workers_total__where_period__by_worker_id_2)
        self.pushButton_33.setObjectName(u"pushButton_33")

        self.gridLayout_87.addWidget(self.pushButton_33, 2, 1, 1, 1)

        self.lineEdit_14 = QLineEdit(self.report__call_workers_total__where_period__by_worker_id_2)
        self.lineEdit_14.setObjectName(u"lineEdit_14")

        self.gridLayout_87.addWidget(self.lineEdit_14, 2, 3, 1, 1)

        self.treeView_12 = QTreeView(self.report__call_workers_total__where_period__by_worker_id_2)
        self.treeView_12.setObjectName(u"treeView_12")

        self.gridLayout_87.addWidget(self.treeView_12, 1, 1, 1, 3)

        self.t_main_for_dep_13 = QTableView(self.report__call_workers_total__where_period__by_worker_id_2)
        self.t_main_for_dep_13.setObjectName(u"t_main_for_dep_13")

        self.gridLayout_87.addWidget(self.t_main_for_dep_13, 3, 0, 1, 4)

        self.frame_18 = QFrame(self.report__call_workers_total__where_period__by_worker_id_2)
        self.frame_18.setObjectName(u"frame_18")
        self.frame_18.setFrameShape(QFrame.StyledPanel)
        self.frame_18.setFrameShadow(QFrame.Raised)
        self.gridLayout_88 = QGridLayout(self.frame_18)
        self.gridLayout_88.setObjectName(u"gridLayout_88")
        self.DO_NOT_USE_222 = myQTabWidget(self.frame_18)
        self.DO_NOT_USE_222.setObjectName(u"DO_NOT_USE_222")
        sizePolicy14.setHeightForWidth(self.DO_NOT_USE_222.sizePolicy().hasHeightForWidth())
        self.DO_NOT_USE_222.setSizePolicy(sizePolicy14)
        self.DO_NOT_USE_222.setMinimumSize(QSize(300, 0))
        self.DO_NOT_USE_223 = QWidget()
        self.DO_NOT_USE_223.setObjectName(u"DO_NOT_USE_223")
        self.verticalLayout_94 = QVBoxLayout(self.DO_NOT_USE_223)
        self.verticalLayout_94.setObjectName(u"verticalLayout_94")
        self.DO_NOT_USE_224 = QGridLayout()
        self.DO_NOT_USE_224.setObjectName(u"DO_NOT_USE_224")
        self.DO_NOT_USE_224.setHorizontalSpacing(0)
        self.DO_NOT_USE_225 = QDateEdit(self.DO_NOT_USE_223)
        self.DO_NOT_USE_225.setObjectName(u"DO_NOT_USE_225")

        self.DO_NOT_USE_224.addWidget(self.DO_NOT_USE_225, 1, 1, 1, 1)

        self.DO_NOT_USE_226 = QLabel(self.DO_NOT_USE_223)
        self.DO_NOT_USE_226.setObjectName(u"DO_NOT_USE_226")
        sizePolicy5.setHeightForWidth(self.DO_NOT_USE_226.sizePolicy().hasHeightForWidth())
        self.DO_NOT_USE_226.setSizePolicy(sizePolicy5)
        self.DO_NOT_USE_226.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.DO_NOT_USE_224.addWidget(self.DO_NOT_USE_226, 1, 0, 1, 1)

        self.DO_NOT_USE_227 = QDateEdit(self.DO_NOT_USE_223)
        self.DO_NOT_USE_227.setObjectName(u"DO_NOT_USE_227")

        self.DO_NOT_USE_224.addWidget(self.DO_NOT_USE_227, 0, 1, 1, 1)

        self.DO_NOT_USE_228 = QLabel(self.DO_NOT_USE_223)
        self.DO_NOT_USE_228.setObjectName(u"DO_NOT_USE_228")
        sizePolicy5.setHeightForWidth(self.DO_NOT_USE_228.sizePolicy().hasHeightForWidth())
        self.DO_NOT_USE_228.setSizePolicy(sizePolicy5)
        self.DO_NOT_USE_228.setLayoutDirection(Qt.LeftToRight)
        self.DO_NOT_USE_228.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.DO_NOT_USE_224.addWidget(self.DO_NOT_USE_228, 0, 0, 1, 1)

        self.verticalSpacer_20 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.DO_NOT_USE_224.addItem(self.verticalSpacer_20, 2, 1, 1, 1)

        self.DO_NOT_USE_224.setColumnStretch(0, 1)

        self.verticalLayout_94.addLayout(self.DO_NOT_USE_224)

        self.DO_NOT_USE_222.addTab(self.DO_NOT_USE_223, "")
        self.DO_NOT_USE_229 = QWidget()
        self.DO_NOT_USE_229.setObjectName(u"DO_NOT_USE_229")
        self.verticalLayout_95 = QVBoxLayout(self.DO_NOT_USE_229)
        self.verticalLayout_95.setObjectName(u"verticalLayout_95")
        self.DO_NOT_USE_230 = QGridLayout()
        self.DO_NOT_USE_230.setObjectName(u"DO_NOT_USE_230")
        self.DO_NOT_USE_231 = QLabel(self.DO_NOT_USE_229)
        self.DO_NOT_USE_231.setObjectName(u"DO_NOT_USE_231")
        self.DO_NOT_USE_231.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.DO_NOT_USE_230.addWidget(self.DO_NOT_USE_231, 0, 0, 1, 1)

        self.DO_NOT_USE_232 = QSpinBox(self.DO_NOT_USE_229)
        self.DO_NOT_USE_232.setObjectName(u"DO_NOT_USE_232")
        self.DO_NOT_USE_232.setMinimum(1950)
        self.DO_NOT_USE_232.setMaximum(2050)
        self.DO_NOT_USE_232.setValue(2019)

        self.DO_NOT_USE_230.addWidget(self.DO_NOT_USE_232, 1, 1, 1, 1)

        self.DO_NOT_USE_233 = QLabel(self.DO_NOT_USE_229)
        self.DO_NOT_USE_233.setObjectName(u"DO_NOT_USE_233")
        self.DO_NOT_USE_233.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.DO_NOT_USE_230.addWidget(self.DO_NOT_USE_233, 1, 0, 1, 1)

        self.DO_NOT_USE_234 = QComboBox(self.DO_NOT_USE_229)
        self.DO_NOT_USE_234.setObjectName(u"DO_NOT_USE_234")
        self.DO_NOT_USE_234.setEditable(True)

        self.DO_NOT_USE_230.addWidget(self.DO_NOT_USE_234, 0, 1, 1, 1)

        self.DO_NOT_USE_230.setColumnStretch(0, 1)
        self.DO_NOT_USE_230.setColumnStretch(1, 2)

        self.verticalLayout_95.addLayout(self.DO_NOT_USE_230)

        self.DO_NOT_USE_222.addTab(self.DO_NOT_USE_229, "")

        self.gridLayout_88.addWidget(self.DO_NOT_USE_222, 0, 0, 1, 1)


        self.gridLayout_87.addWidget(self.frame_18, 0, 0, 2, 1)


        self.gridLayout_86.addWidget(self.report__call_workers_total__where_period__by_worker_id_2, 0, 0, 1, 1)

        self.tabWidget_11.addTab(self.tab_52, "")

        self.gridLayout_89.addWidget(self.tabWidget_11, 0, 0, 1, 1)

        self.tabs_total.addTab(self.tab_41, "")
        self.tab_16 = myQWidget()
        self.tab_16.setObjectName(u"tab_16")
        self.gridLayout_30 = QGridLayout(self.tab_16)
        self.gridLayout_30.setObjectName(u"gridLayout_30")
        self.tabWidget_9 = myQTabWidget(self.tab_16)
        self.tabWidget_9.setObjectName(u"tabWidget_9")
        self.tab_46 = myQWidget()
        self.tab_46.setObjectName(u"tab_46")
        self.gridLayout_31 = QGridLayout(self.tab_46)
        self.gridLayout_31.setObjectName(u"gridLayout_31")
        self.report__g_categ_list_client__by_client_id = qcSelectReport(self.tab_46)
        self.report__g_categ_list_client__by_client_id.setObjectName(u"report__g_categ_list_client__by_client_id")
        self.gridLayout_62 = QGridLayout(self.report__g_categ_list_client__by_client_id)
        self.gridLayout_62.setObjectName(u"gridLayout_62")
        self.label_68 = QLabel(self.report__g_categ_list_client__by_client_id)
        self.label_68.setObjectName(u"label_68")

        self.gridLayout_62.addWidget(self.label_68, 2, 2, 1, 1)

        self.btn_serv_you_12 = QPushButton(self.report__g_categ_list_client__by_client_id)
        self.btn_serv_you_12.setObjectName(u"btn_serv_you_12")

        self.gridLayout_62.addWidget(self.btn_serv_you_12, 2, 0, 1, 1)

        self.pushButton_26 = QPushButton(self.report__g_categ_list_client__by_client_id)
        self.pushButton_26.setObjectName(u"pushButton_26")

        self.gridLayout_62.addWidget(self.pushButton_26, 2, 1, 1, 1)

        self.lineEdit_8 = QLineEdit(self.report__g_categ_list_client__by_client_id)
        self.lineEdit_8.setObjectName(u"lineEdit_8")

        self.gridLayout_62.addWidget(self.lineEdit_8, 2, 3, 1, 1)

        self.treeView_6 = QTreeView(self.report__g_categ_list_client__by_client_id)
        self.treeView_6.setObjectName(u"treeView_6")

        self.gridLayout_62.addWidget(self.treeView_6, 1, 1, 1, 3)

        self.t_main_for_dep_7 = QTableView(self.report__g_categ_list_client__by_client_id)
        self.t_main_for_dep_7.setObjectName(u"t_main_for_dep_7")

        self.gridLayout_62.addWidget(self.t_main_for_dep_7, 3, 0, 1, 4)

        self.frame_11 = QFrame(self.report__g_categ_list_client__by_client_id)
        self.frame_11.setObjectName(u"frame_11")
        self.frame_11.setFrameShape(QFrame.StyledPanel)
        self.frame_11.setFrameShadow(QFrame.Raised)
        self.gridLayout_63 = QGridLayout(self.frame_11)
        self.gridLayout_63.setObjectName(u"gridLayout_63")
        self.DO_NOT_USE_131 = myQTabWidget(self.frame_11)
        self.DO_NOT_USE_131.setObjectName(u"DO_NOT_USE_131")
        sizePolicy14.setHeightForWidth(self.DO_NOT_USE_131.sizePolicy().hasHeightForWidth())
        self.DO_NOT_USE_131.setSizePolicy(sizePolicy14)
        self.DO_NOT_USE_131.setMinimumSize(QSize(300, 0))
        self.DO_NOT_USE_132 = QWidget()
        self.DO_NOT_USE_132.setObjectName(u"DO_NOT_USE_132")
        self.verticalLayout_80 = QVBoxLayout(self.DO_NOT_USE_132)
        self.verticalLayout_80.setObjectName(u"verticalLayout_80")
        self.DO_NOT_USE_133 = QGridLayout()
        self.DO_NOT_USE_133.setObjectName(u"DO_NOT_USE_133")
        self.DO_NOT_USE_133.setHorizontalSpacing(0)
        self.DO_NOT_USE_134 = QDateEdit(self.DO_NOT_USE_132)
        self.DO_NOT_USE_134.setObjectName(u"DO_NOT_USE_134")

        self.DO_NOT_USE_133.addWidget(self.DO_NOT_USE_134, 1, 1, 1, 1)

        self.DO_NOT_USE_135 = QLabel(self.DO_NOT_USE_132)
        self.DO_NOT_USE_135.setObjectName(u"DO_NOT_USE_135")
        sizePolicy5.setHeightForWidth(self.DO_NOT_USE_135.sizePolicy().hasHeightForWidth())
        self.DO_NOT_USE_135.setSizePolicy(sizePolicy5)
        self.DO_NOT_USE_135.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.DO_NOT_USE_133.addWidget(self.DO_NOT_USE_135, 1, 0, 1, 1)

        self.DO_NOT_USE_136 = QDateEdit(self.DO_NOT_USE_132)
        self.DO_NOT_USE_136.setObjectName(u"DO_NOT_USE_136")

        self.DO_NOT_USE_133.addWidget(self.DO_NOT_USE_136, 0, 1, 1, 1)

        self.DO_NOT_USE_137 = QLabel(self.DO_NOT_USE_132)
        self.DO_NOT_USE_137.setObjectName(u"DO_NOT_USE_137")
        sizePolicy5.setHeightForWidth(self.DO_NOT_USE_137.sizePolicy().hasHeightForWidth())
        self.DO_NOT_USE_137.setSizePolicy(sizePolicy5)
        self.DO_NOT_USE_137.setLayoutDirection(Qt.LeftToRight)
        self.DO_NOT_USE_137.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.DO_NOT_USE_133.addWidget(self.DO_NOT_USE_137, 0, 0, 1, 1)

        self.verticalSpacer_11 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.DO_NOT_USE_133.addItem(self.verticalSpacer_11, 2, 1, 1, 1)

        self.DO_NOT_USE_133.setColumnStretch(0, 1)

        self.verticalLayout_80.addLayout(self.DO_NOT_USE_133)

        self.DO_NOT_USE_131.addTab(self.DO_NOT_USE_132, "")
        self.DO_NOT_USE_138 = QWidget()
        self.DO_NOT_USE_138.setObjectName(u"DO_NOT_USE_138")
        self.verticalLayout_81 = QVBoxLayout(self.DO_NOT_USE_138)
        self.verticalLayout_81.setObjectName(u"verticalLayout_81")
        self.DO_NOT_USE_139 = QGridLayout()
        self.DO_NOT_USE_139.setObjectName(u"DO_NOT_USE_139")
        self.DO_NOT_USE_140 = QLabel(self.DO_NOT_USE_138)
        self.DO_NOT_USE_140.setObjectName(u"DO_NOT_USE_140")
        self.DO_NOT_USE_140.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.DO_NOT_USE_139.addWidget(self.DO_NOT_USE_140, 0, 0, 1, 1)

        self.DO_NOT_USE_141 = QSpinBox(self.DO_NOT_USE_138)
        self.DO_NOT_USE_141.setObjectName(u"DO_NOT_USE_141")
        self.DO_NOT_USE_141.setMinimum(1950)
        self.DO_NOT_USE_141.setMaximum(2050)
        self.DO_NOT_USE_141.setValue(2019)

        self.DO_NOT_USE_139.addWidget(self.DO_NOT_USE_141, 1, 1, 1, 1)

        self.DO_NOT_USE_142 = QLabel(self.DO_NOT_USE_138)
        self.DO_NOT_USE_142.setObjectName(u"DO_NOT_USE_142")
        self.DO_NOT_USE_142.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.DO_NOT_USE_139.addWidget(self.DO_NOT_USE_142, 1, 0, 1, 1)

        self.DO_NOT_USE_143 = QComboBox(self.DO_NOT_USE_138)
        self.DO_NOT_USE_143.setObjectName(u"DO_NOT_USE_143")
        self.DO_NOT_USE_143.setEditable(True)

        self.DO_NOT_USE_139.addWidget(self.DO_NOT_USE_143, 0, 1, 1, 1)

        self.DO_NOT_USE_139.setColumnStretch(0, 1)
        self.DO_NOT_USE_139.setColumnStretch(1, 2)

        self.verticalLayout_81.addLayout(self.DO_NOT_USE_139)

        self.DO_NOT_USE_131.addTab(self.DO_NOT_USE_138, "")

        self.gridLayout_63.addWidget(self.DO_NOT_USE_131, 0, 0, 1, 1)


        self.gridLayout_62.addWidget(self.frame_11, 0, 0, 2, 1)


        self.gridLayout_31.addWidget(self.report__g_categ_list_client__by_client_id, 0, 0, 1, 1)

        self.tabWidget_9.addTab(self.tab_46, "")
        self.tab_47 = myQWidget()
        self.tab_47.setObjectName(u"tab_47")
        self.gridLayout_69 = QGridLayout(self.tab_47)
        self.gridLayout_69.setObjectName(u"gridLayout_69")
        self.report__call_categ_list_client_total__by_category_id = qcSelectReport(self.tab_47)
        self.report__call_categ_list_client_total__by_category_id.setObjectName(u"report__call_categ_list_client_total__by_category_id")
        self.gridLayout_67 = QGridLayout(self.report__call_categ_list_client_total__by_category_id)
        self.gridLayout_67.setObjectName(u"gridLayout_67")
        self.label_71 = QLabel(self.report__call_categ_list_client_total__by_category_id)
        self.label_71.setObjectName(u"label_71")

        self.gridLayout_67.addWidget(self.label_71, 2, 2, 1, 1)

        self.btn_serv_you_14 = QPushButton(self.report__call_categ_list_client_total__by_category_id)
        self.btn_serv_you_14.setObjectName(u"btn_serv_you_14")

        self.gridLayout_67.addWidget(self.btn_serv_you_14, 2, 0, 1, 1)

        self.pushButton_28 = QPushButton(self.report__call_categ_list_client_total__by_category_id)
        self.pushButton_28.setObjectName(u"pushButton_28")

        self.gridLayout_67.addWidget(self.pushButton_28, 2, 1, 1, 1)

        self.lineEdit_10 = QLineEdit(self.report__call_categ_list_client_total__by_category_id)
        self.lineEdit_10.setObjectName(u"lineEdit_10")

        self.gridLayout_67.addWidget(self.lineEdit_10, 2, 3, 1, 1)

        self.treeView_8 = QTreeView(self.report__call_categ_list_client_total__by_category_id)
        self.treeView_8.setObjectName(u"treeView_8")

        self.gridLayout_67.addWidget(self.treeView_8, 1, 1, 1, 3)

        self.t_main_for_dep_9 = QTableView(self.report__call_categ_list_client_total__by_category_id)
        self.t_main_for_dep_9.setObjectName(u"t_main_for_dep_9")

        self.gridLayout_67.addWidget(self.t_main_for_dep_9, 3, 0, 1, 4)

        self.frame_13 = QFrame(self.report__call_categ_list_client_total__by_category_id)
        self.frame_13.setObjectName(u"frame_13")
        self.frame_13.setFrameShape(QFrame.StyledPanel)
        self.frame_13.setFrameShadow(QFrame.Raised)
        self.gridLayout_68 = QGridLayout(self.frame_13)
        self.gridLayout_68.setObjectName(u"gridLayout_68")
        self.DO_NOT_USE_157 = myQTabWidget(self.frame_13)
        self.DO_NOT_USE_157.setObjectName(u"DO_NOT_USE_157")
        sizePolicy14.setHeightForWidth(self.DO_NOT_USE_157.sizePolicy().hasHeightForWidth())
        self.DO_NOT_USE_157.setSizePolicy(sizePolicy14)
        self.DO_NOT_USE_157.setMinimumSize(QSize(300, 0))
        self.DO_NOT_USE_158 = QWidget()
        self.DO_NOT_USE_158.setObjectName(u"DO_NOT_USE_158")
        self.verticalLayout_84 = QVBoxLayout(self.DO_NOT_USE_158)
        self.verticalLayout_84.setObjectName(u"verticalLayout_84")
        self.DO_NOT_USE_159 = QGridLayout()
        self.DO_NOT_USE_159.setObjectName(u"DO_NOT_USE_159")
        self.DO_NOT_USE_159.setHorizontalSpacing(0)
        self.DO_NOT_USE_160 = QDateEdit(self.DO_NOT_USE_158)
        self.DO_NOT_USE_160.setObjectName(u"DO_NOT_USE_160")

        self.DO_NOT_USE_159.addWidget(self.DO_NOT_USE_160, 1, 1, 1, 1)

        self.DO_NOT_USE_161 = QLabel(self.DO_NOT_USE_158)
        self.DO_NOT_USE_161.setObjectName(u"DO_NOT_USE_161")
        sizePolicy5.setHeightForWidth(self.DO_NOT_USE_161.sizePolicy().hasHeightForWidth())
        self.DO_NOT_USE_161.setSizePolicy(sizePolicy5)
        self.DO_NOT_USE_161.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.DO_NOT_USE_159.addWidget(self.DO_NOT_USE_161, 1, 0, 1, 1)

        self.DO_NOT_USE_162 = QDateEdit(self.DO_NOT_USE_158)
        self.DO_NOT_USE_162.setObjectName(u"DO_NOT_USE_162")

        self.DO_NOT_USE_159.addWidget(self.DO_NOT_USE_162, 0, 1, 1, 1)

        self.DO_NOT_USE_163 = QLabel(self.DO_NOT_USE_158)
        self.DO_NOT_USE_163.setObjectName(u"DO_NOT_USE_163")
        sizePolicy5.setHeightForWidth(self.DO_NOT_USE_163.sizePolicy().hasHeightForWidth())
        self.DO_NOT_USE_163.setSizePolicy(sizePolicy5)
        self.DO_NOT_USE_163.setLayoutDirection(Qt.LeftToRight)
        self.DO_NOT_USE_163.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.DO_NOT_USE_159.addWidget(self.DO_NOT_USE_163, 0, 0, 1, 1)

        self.verticalSpacer_13 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.DO_NOT_USE_159.addItem(self.verticalSpacer_13, 2, 1, 1, 1)

        self.DO_NOT_USE_159.setColumnStretch(0, 1)

        self.verticalLayout_84.addLayout(self.DO_NOT_USE_159)

        self.DO_NOT_USE_157.addTab(self.DO_NOT_USE_158, "")
        self.DO_NOT_USE_164 = QWidget()
        self.DO_NOT_USE_164.setObjectName(u"DO_NOT_USE_164")
        self.verticalLayout_85 = QVBoxLayout(self.DO_NOT_USE_164)
        self.verticalLayout_85.setObjectName(u"verticalLayout_85")
        self.DO_NOT_USE_165 = QGridLayout()
        self.DO_NOT_USE_165.setObjectName(u"DO_NOT_USE_165")
        self.DO_NOT_USE_166 = QLabel(self.DO_NOT_USE_164)
        self.DO_NOT_USE_166.setObjectName(u"DO_NOT_USE_166")
        self.DO_NOT_USE_166.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.DO_NOT_USE_165.addWidget(self.DO_NOT_USE_166, 0, 0, 1, 1)

        self.DO_NOT_USE_167 = QSpinBox(self.DO_NOT_USE_164)
        self.DO_NOT_USE_167.setObjectName(u"DO_NOT_USE_167")
        self.DO_NOT_USE_167.setMinimum(1950)
        self.DO_NOT_USE_167.setMaximum(2050)
        self.DO_NOT_USE_167.setValue(2019)

        self.DO_NOT_USE_165.addWidget(self.DO_NOT_USE_167, 1, 1, 1, 1)

        self.DO_NOT_USE_168 = QLabel(self.DO_NOT_USE_164)
        self.DO_NOT_USE_168.setObjectName(u"DO_NOT_USE_168")
        self.DO_NOT_USE_168.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.DO_NOT_USE_165.addWidget(self.DO_NOT_USE_168, 1, 0, 1, 1)

        self.DO_NOT_USE_169 = QComboBox(self.DO_NOT_USE_164)
        self.DO_NOT_USE_169.setObjectName(u"DO_NOT_USE_169")
        self.DO_NOT_USE_169.setEditable(True)

        self.DO_NOT_USE_165.addWidget(self.DO_NOT_USE_169, 0, 1, 1, 1)

        self.DO_NOT_USE_165.setColumnStretch(0, 1)
        self.DO_NOT_USE_165.setColumnStretch(1, 2)

        self.verticalLayout_85.addLayout(self.DO_NOT_USE_165)

        self.DO_NOT_USE_157.addTab(self.DO_NOT_USE_164, "")

        self.gridLayout_68.addWidget(self.DO_NOT_USE_157, 0, 0, 1, 1)


        self.gridLayout_67.addWidget(self.frame_13, 0, 0, 2, 1)


        self.gridLayout_69.addWidget(self.report__call_categ_list_client_total__by_category_id, 0, 0, 1, 1)

        self.tabWidget_9.addTab(self.tab_47, "")
        self.tab_10 = myQWidget()
        self.tab_10.setObjectName(u"tab_10")
        self.gridLayout_66 = QGridLayout(self.tab_10)
        self.gridLayout_66.setObjectName(u"gridLayout_66")
        self.report__g_category_total_new__by_client_id__2 = qcSelectReport(self.tab_10)
        self.report__g_category_total_new__by_client_id__2.setObjectName(u"report__g_category_total_new__by_client_id__2")
        self.gridLayout_64 = QGridLayout(self.report__g_category_total_new__by_client_id__2)
        self.gridLayout_64.setObjectName(u"gridLayout_64")
        self.label_69 = QLabel(self.report__g_category_total_new__by_client_id__2)
        self.label_69.setObjectName(u"label_69")

        self.gridLayout_64.addWidget(self.label_69, 2, 2, 1, 1)

        self.btn_serv_you_13 = QPushButton(self.report__g_category_total_new__by_client_id__2)
        self.btn_serv_you_13.setObjectName(u"btn_serv_you_13")

        self.gridLayout_64.addWidget(self.btn_serv_you_13, 2, 0, 1, 1)

        self.pushButton_27 = QPushButton(self.report__g_category_total_new__by_client_id__2)
        self.pushButton_27.setObjectName(u"pushButton_27")

        self.gridLayout_64.addWidget(self.pushButton_27, 2, 1, 1, 1)

        self.lineEdit_9 = QLineEdit(self.report__g_category_total_new__by_client_id__2)
        self.lineEdit_9.setObjectName(u"lineEdit_9")

        self.gridLayout_64.addWidget(self.lineEdit_9, 2, 3, 1, 1)

        self.treeView_7 = QTreeView(self.report__g_category_total_new__by_client_id__2)
        self.treeView_7.setObjectName(u"treeView_7")

        self.gridLayout_64.addWidget(self.treeView_7, 1, 1, 1, 3)

        self.t_main_for_dep_8 = QTableView(self.report__g_category_total_new__by_client_id__2)
        self.t_main_for_dep_8.setObjectName(u"t_main_for_dep_8")

        self.gridLayout_64.addWidget(self.t_main_for_dep_8, 3, 0, 1, 4)

        self.frame_12 = QFrame(self.report__g_category_total_new__by_client_id__2)
        self.frame_12.setObjectName(u"frame_12")
        self.frame_12.setFrameShape(QFrame.StyledPanel)
        self.frame_12.setFrameShadow(QFrame.Raised)
        self.gridLayout_65 = QGridLayout(self.frame_12)
        self.gridLayout_65.setObjectName(u"gridLayout_65")
        self.DO_NOT_USE_144 = myQTabWidget(self.frame_12)
        self.DO_NOT_USE_144.setObjectName(u"DO_NOT_USE_144")
        sizePolicy14.setHeightForWidth(self.DO_NOT_USE_144.sizePolicy().hasHeightForWidth())
        self.DO_NOT_USE_144.setSizePolicy(sizePolicy14)
        self.DO_NOT_USE_144.setMinimumSize(QSize(300, 0))
        self.DO_NOT_USE_145 = QWidget()
        self.DO_NOT_USE_145.setObjectName(u"DO_NOT_USE_145")
        self.verticalLayout_82 = QVBoxLayout(self.DO_NOT_USE_145)
        self.verticalLayout_82.setObjectName(u"verticalLayout_82")
        self.DO_NOT_USE_146 = QGridLayout()
        self.DO_NOT_USE_146.setObjectName(u"DO_NOT_USE_146")
        self.DO_NOT_USE_146.setHorizontalSpacing(0)
        self.DO_NOT_USE_147 = QDateEdit(self.DO_NOT_USE_145)
        self.DO_NOT_USE_147.setObjectName(u"DO_NOT_USE_147")

        self.DO_NOT_USE_146.addWidget(self.DO_NOT_USE_147, 1, 1, 1, 1)

        self.DO_NOT_USE_148 = QLabel(self.DO_NOT_USE_145)
        self.DO_NOT_USE_148.setObjectName(u"DO_NOT_USE_148")
        sizePolicy5.setHeightForWidth(self.DO_NOT_USE_148.sizePolicy().hasHeightForWidth())
        self.DO_NOT_USE_148.setSizePolicy(sizePolicy5)
        self.DO_NOT_USE_148.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.DO_NOT_USE_146.addWidget(self.DO_NOT_USE_148, 1, 0, 1, 1)

        self.DO_NOT_USE_149 = QDateEdit(self.DO_NOT_USE_145)
        self.DO_NOT_USE_149.setObjectName(u"DO_NOT_USE_149")

        self.DO_NOT_USE_146.addWidget(self.DO_NOT_USE_149, 0, 1, 1, 1)

        self.DO_NOT_USE_150 = QLabel(self.DO_NOT_USE_145)
        self.DO_NOT_USE_150.setObjectName(u"DO_NOT_USE_150")
        sizePolicy5.setHeightForWidth(self.DO_NOT_USE_150.sizePolicy().hasHeightForWidth())
        self.DO_NOT_USE_150.setSizePolicy(sizePolicy5)
        self.DO_NOT_USE_150.setLayoutDirection(Qt.LeftToRight)
        self.DO_NOT_USE_150.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.DO_NOT_USE_146.addWidget(self.DO_NOT_USE_150, 0, 0, 1, 1)

        self.verticalSpacer_12 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.DO_NOT_USE_146.addItem(self.verticalSpacer_12, 2, 1, 1, 1)

        self.DO_NOT_USE_146.setColumnStretch(0, 1)

        self.verticalLayout_82.addLayout(self.DO_NOT_USE_146)

        self.DO_NOT_USE_144.addTab(self.DO_NOT_USE_145, "")
        self.DO_NOT_USE_151 = QWidget()
        self.DO_NOT_USE_151.setObjectName(u"DO_NOT_USE_151")
        self.verticalLayout_83 = QVBoxLayout(self.DO_NOT_USE_151)
        self.verticalLayout_83.setObjectName(u"verticalLayout_83")
        self.DO_NOT_USE_152 = QGridLayout()
        self.DO_NOT_USE_152.setObjectName(u"DO_NOT_USE_152")
        self.DO_NOT_USE_153 = QLabel(self.DO_NOT_USE_151)
        self.DO_NOT_USE_153.setObjectName(u"DO_NOT_USE_153")
        self.DO_NOT_USE_153.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.DO_NOT_USE_152.addWidget(self.DO_NOT_USE_153, 0, 0, 1, 1)

        self.DO_NOT_USE_154 = QSpinBox(self.DO_NOT_USE_151)
        self.DO_NOT_USE_154.setObjectName(u"DO_NOT_USE_154")
        self.DO_NOT_USE_154.setMinimum(1950)
        self.DO_NOT_USE_154.setMaximum(2050)
        self.DO_NOT_USE_154.setValue(2019)

        self.DO_NOT_USE_152.addWidget(self.DO_NOT_USE_154, 1, 1, 1, 1)

        self.DO_NOT_USE_155 = QLabel(self.DO_NOT_USE_151)
        self.DO_NOT_USE_155.setObjectName(u"DO_NOT_USE_155")
        self.DO_NOT_USE_155.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.DO_NOT_USE_152.addWidget(self.DO_NOT_USE_155, 1, 0, 1, 1)

        self.DO_NOT_USE_156 = QComboBox(self.DO_NOT_USE_151)
        self.DO_NOT_USE_156.setObjectName(u"DO_NOT_USE_156")
        self.DO_NOT_USE_156.setEditable(True)

        self.DO_NOT_USE_152.addWidget(self.DO_NOT_USE_156, 0, 1, 1, 1)

        self.DO_NOT_USE_152.setColumnStretch(0, 1)
        self.DO_NOT_USE_152.setColumnStretch(1, 2)

        self.verticalLayout_83.addLayout(self.DO_NOT_USE_152)

        self.DO_NOT_USE_144.addTab(self.DO_NOT_USE_151, "")

        self.gridLayout_65.addWidget(self.DO_NOT_USE_144, 0, 0, 1, 1)


        self.gridLayout_64.addWidget(self.frame_12, 0, 0, 2, 1)


        self.gridLayout_66.addWidget(self.report__g_category_total_new__by_client_id__2, 0, 0, 1, 1)

        self.tabWidget_9.addTab(self.tab_10, "")

        self.gridLayout_30.addWidget(self.tabWidget_9, 0, 0, 1, 1)

        self.tabs_total.addTab(self.tab_16, "")
        self.tab_20 = myQWidget()
        self.tab_20.setObjectName(u"tab_20")
        self.verticalLayout_17 = QVBoxLayout(self.tab_20)
        self.verticalLayout_17.setObjectName(u"verticalLayout_17")
        self.tabWidget_10 = QTabWidget(self.tab_20)
        self.tabWidget_10.setObjectName(u"tabWidget_10")
        self.tab_48 = myQWidget()
        self.tab_48.setObjectName(u"tab_48")
        self.tabWidget_10.addTab(self.tab_48, "")
        self.tab_49 = myQWidget()
        self.tab_49.setObjectName(u"tab_49")
        self.tabWidget_10.addTab(self.tab_49, "")

        self.verticalLayout_17.addWidget(self.tabWidget_10)

        self.tabs_total.addTab(self.tab_20, "")
        self.tab_13 = myQWidget()
        self.tab_13.setObjectName(u"tab_13")
        self.tabs_total.addTab(self.tab_13, "")

        self.verticalLayout_6.addWidget(self.tabs_total)

        self.tabMain.addTab(self.tab_total, "")
        self.tab_admin = myQWidget()
        self.tab_admin.setObjectName(u"tab_admin")
        self.horizontalLayout = QHBoxLayout(self.tab_admin)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.tabs_admin = myQTabWidget(self.tab_admin)
        self.tabs_admin.setObjectName(u"tabs_admin")
        self.tabs_admin.setToolTipDuration(-1)
        self.tab_serv = myQWidget()
        self.tab_serv.setObjectName(u"tab_serv")
        self.horizontalLayout_2 = QHBoxLayout(self.tab_serv)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.gridLayout_23 = QGridLayout()
        self.gridLayout_23.setObjectName(u"gridLayout_23")
        self.label_serv_year = QLabel(self.tab_serv)
        self.label_serv_year.setObjectName(u"label_serv_year")
        sizePolicy24 = QSizePolicy(QSizePolicy.Maximum, QSizePolicy.Preferred)
        sizePolicy24.setHorizontalStretch(0)
        sizePolicy24.setVerticalStretch(0)
        sizePolicy24.setHeightForWidth(self.label_serv_year.sizePolicy().hasHeightForWidth())
        self.label_serv_year.setSizePolicy(sizePolicy24)

        self.gridLayout_23.addWidget(self.label_serv_year, 0, 0, 1, 1)

        self.btn_add_services_for_new_year = QPushButton(self.tab_serv)
        self.btn_add_services_for_new_year.setObjectName(u"btn_add_services_for_new_year")

        self.gridLayout_23.addWidget(self.btn_add_services_for_new_year, 0, 3, 1, 1)

        self.table_serv__by_year = myQTableView(self.tab_serv)
        self.table_serv__by_year.setObjectName(u"table_serv__by_year")
        self.table_serv__by_year.setAlternatingRowColors(True)
        self.table_serv__by_year.setSortingEnabled(True)

        self.gridLayout_23.addWidget(self.table_serv__by_year, 1, 0, 1, 4)

        self.horizontalSpacer_4 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_23.addItem(self.horizontalSpacer_4, 0, 2, 1, 1)

        self.cbx_4_serv__uniq_year = myQComboBox(self.tab_serv)
        self.cbx_4_serv__uniq_year.setObjectName(u"cbx_4_serv__uniq_year")

        self.gridLayout_23.addWidget(self.cbx_4_serv__uniq_year, 0, 1, 1, 1)


        self.horizontalLayout_2.addLayout(self.gridLayout_23)

        self.tabs_admin.addTab(self.tab_serv, "")
        self.tab_ripso = myQWidget()
        self.tab_ripso.setObjectName(u"tab_ripso")
        self.gridLayout_107 = QGridLayout(self.tab_ripso)
        self.gridLayout_107.setObjectName(u"gridLayout_107")
        self.splitter_2 = QSplitter(self.tab_ripso)
        self.splitter_2.setObjectName(u"splitter_2")
        self.splitter_2.setOrientation(Qt.Horizontal)
        self.widget_7 = QWidget(self.splitter_2)
        self.widget_7.setObjectName(u"widget_7")
        self.gridLayout_3 = QGridLayout(self.widget_7)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.label_10 = QLabel(self.widget_7)
        self.label_10.setObjectName(u"label_10")

        self.gridLayout_3.addWidget(self.label_10, 0, 0, 1, 1)

        self.table_ripso = wsQTableView(self.widget_7)
        self.table_ripso.setObjectName(u"table_ripso")

        self.gridLayout_3.addWidget(self.table_ripso, 1, 0, 1, 1)

        self.splitter_2.addWidget(self.widget_7)
        self.widget_8 = QWidget(self.splitter_2)
        self.widget_8.setObjectName(u"widget_8")
        self.gridLayout_95 = QGridLayout(self.widget_8)
        self.gridLayout_95.setObjectName(u"gridLayout_95")
        self.label_11 = QLabel(self.widget_8)
        self.label_11.setObjectName(u"label_11")

        self.gridLayout_95.addWidget(self.label_11, 0, 0, 1, 1)

        self.table_ripso_has_serv__by_ripso_id = myQTableView(self.widget_8)
        self.table_ripso_has_serv__by_ripso_id.setObjectName(u"table_ripso_has_serv__by_ripso_id")

        self.gridLayout_95.addWidget(self.table_ripso_has_serv__by_ripso_id, 1, 0, 1, 1)

        self.splitter_2.addWidget(self.widget_8)

        self.gridLayout_107.addWidget(self.splitter_2, 0, 0, 1, 1)

        self.tabs_admin.addTab(self.tab_ripso, "")
        self.tab_workers = myQWidget()
        self.tab_workers.setObjectName(u"tab_workers")
        self.gridLayout_108 = QGridLayout(self.tab_workers)
        self.gridLayout_108.setObjectName(u"gridLayout_108")
        self.widget_9 = myQWidget(self.tab_workers)
        self.widget_9.setObjectName(u"widget_9")
        self.gridLayout_110 = QGridLayout(self.widget_9)
        self.gridLayout_110.setObjectName(u"gridLayout_110")
        self.splitter_3 = QSplitter(self.widget_9)
        self.splitter_3.setObjectName(u"splitter_3")
        self.splitter_3.setOrientation(Qt.Horizontal)
        self.widget_10 = QWidget(self.splitter_3)
        self.widget_10.setObjectName(u"widget_10")
        self.gridLayout_109 = QGridLayout(self.widget_10)
        self.gridLayout_109.setObjectName(u"gridLayout_109")
        self.label_13 = QLabel(self.widget_10)
        self.label_13.setObjectName(u"label_13")

        self.gridLayout_109.addWidget(self.label_13, 0, 0, 1, 1)

        self.table_worker = wsQTableView(self.widget_10)
        self.table_worker.setObjectName(u"table_worker")
        self.table_worker.setTabletTracking(False)

        self.gridLayout_109.addWidget(self.table_worker, 1, 0, 1, 1)

        self.splitter_3.addWidget(self.widget_10)
        self.widget_11 = QWidget(self.splitter_3)
        self.widget_11.setObjectName(u"widget_11")
        self.gridLayout_4 = QGridLayout(self.widget_11)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.label_14 = QLabel(self.widget_11)
        self.label_14.setObjectName(u"label_14")

        self.gridLayout_4.addWidget(self.label_14, 0, 0, 1, 1)

        self.btn_show_qrcode = QPushButton(self.widget_11)
        self.btn_show_qrcode.setObjectName(u"btn_show_qrcode")

        self.gridLayout_4.addWidget(self.btn_show_qrcode, 0, 1, 1, 1)

        self.table_dep_has_worker__by_worker_id = myQTableView(self.widget_11)
        self.table_dep_has_worker__by_worker_id.setObjectName(u"table_dep_has_worker__by_worker_id")

        self.gridLayout_4.addWidget(self.table_dep_has_worker__by_worker_id, 1, 0, 1, 2)

        self.splitter_3.addWidget(self.widget_11)

        self.gridLayout_110.addWidget(self.splitter_3, 0, 0, 1, 1)


        self.gridLayout_108.addWidget(self.widget_9, 0, 0, 1, 1)

        self.tabs_admin.addTab(self.tab_workers, "")
        self.tab_password = myQWidget()
        self.tab_password.setObjectName(u"tab_password")
        self.horizontalLayout_3 = QHBoxLayout(self.tab_password)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.gridLayout_35 = QGridLayout()
        self.gridLayout_35.setObjectName(u"gridLayout_35")
        self.widget_3 = QWidget(self.tab_password)
        self.widget_3.setObjectName(u"widget_3")
        sizePolicy21.setHeightForWidth(self.widget_3.sizePolicy().hasHeightForWidth())
        self.widget_3.setSizePolicy(sizePolicy21)
        self.horizontalLayout_20 = QHBoxLayout(self.widget_3)
        self.horizontalLayout_20.setObjectName(u"horizontalLayout_20")
        self.table_dep_has_worker__by_worker_id__3 = myQTableView(self.widget_3)
        self.table_dep_has_worker__by_worker_id__3.setObjectName(u"table_dep_has_worker__by_worker_id__3")

        self.horizontalLayout_20.addWidget(self.table_dep_has_worker__by_worker_id__3)


        self.gridLayout_35.addWidget(self.widget_3, 6, 1, 1, 1)

        self.cbx_1_worker__pass = myQComboBox(self.tab_password)
        self.cbx_1_worker__pass.setObjectName(u"cbx_1_worker__pass")
        sizePolicy6.setHeightForWidth(self.cbx_1_worker__pass.sizePolicy().hasHeightForWidth())
        self.cbx_1_worker__pass.setSizePolicy(sizePolicy6)

        self.gridLayout_35.addWidget(self.cbx_1_worker__pass, 1, 1, 1, 1)

        self.widget = QWidget(self.tab_password)
        self.widget.setObjectName(u"widget")
        self.horizontalLayout_4 = QHBoxLayout(self.widget)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.btn_pw_gen = QPushButton(self.widget)
        self.btn_pw_gen.setObjectName(u"btn_pw_gen")

        self.horizontalLayout_4.addWidget(self.btn_pw_gen)

        self.btn_update_login_pass = QPushButton(self.widget)
        self.btn_update_login_pass.setObjectName(u"btn_update_login_pass")

        self.horizontalLayout_4.addWidget(self.btn_update_login_pass)

        self.btnClean = QPushButton(self.widget)
        self.btnClean.setObjectName(u"btnClean")

        self.horizontalLayout_4.addWidget(self.btnClean)


        self.gridLayout_35.addWidget(self.widget, 5, 1, 1, 1)

        self.label_6 = QLabel(self.tab_password)
        self.label_6.setObjectName(u"label_6")

        self.gridLayout_35.addWidget(self.label_6, 3, 0, 1, 1)

        self.label_5 = QLabel(self.tab_password)
        self.label_5.setObjectName(u"label_5")

        self.gridLayout_35.addWidget(self.label_5, 2, 0, 1, 1)

        self.label_31 = QLabel(self.tab_password)
        self.label_31.setObjectName(u"label_31")

        self.gridLayout_35.addWidget(self.label_31, 6, 0, 1, 1)

        self.horizontalLayout_23 = QHBoxLayout()
        self.horizontalLayout_23.setObjectName(u"horizontalLayout_23")
        self.lineEdit_pass = myQLineEdit(self.tab_password)
        self.lineEdit_pass.setObjectName(u"lineEdit_pass")
        self.lineEdit_pass.setEnabled(True)
        sizePolicy3.setHeightForWidth(self.lineEdit_pass.sizePolicy().hasHeightForWidth())
        self.lineEdit_pass.setSizePolicy(sizePolicy3)
        self.lineEdit_pass.setMinimumSize(QSize(300, 0))
        self.lineEdit_pass.setReadOnly(True)

        self.horizontalLayout_23.addWidget(self.lineEdit_pass)

        self.qle_fio_log_pass = QLineEdit(self.tab_password)
        self.qle_fio_log_pass.setObjectName(u"qle_fio_log_pass")

        self.horizontalLayout_23.addWidget(self.qle_fio_log_pass)


        self.gridLayout_35.addLayout(self.horizontalLayout_23, 3, 1, 1, 1)

        self.label_4 = QLabel(self.tab_password)
        self.label_4.setObjectName(u"label_4")

        self.gridLayout_35.addWidget(self.label_4, 1, 0, 1, 1)

        self.lineEdit_login = myQLineEdit(self.tab_password)
        self.lineEdit_login.setObjectName(u"lineEdit_login")
        self.lineEdit_login.setInputMethodHints(Qt.ImhLatinOnly|Qt.ImhLowercaseOnly)
        self.lineEdit_login.setMaxLength(32)
        self.lineEdit_login.setCursorPosition(0)

        self.gridLayout_35.addWidget(self.lineEdit_login, 2, 1, 1, 1)

        self.label_75 = QLabel(self.tab_password)
        self.label_75.setObjectName(u"label_75")
        font3 = QFont()
        font3.setPointSize(12)
        self.label_75.setFont(font3)
        self.label_75.setAlignment(Qt.AlignCenter)

        self.gridLayout_35.addWidget(self.label_75, 0, 1, 1, 1)


        self.horizontalLayout_3.addLayout(self.gridLayout_35)

        self.tabs_admin.addTab(self.tab_password, "")
        self.tab_dep = myQWidget()
        self.tab_dep.setObjectName(u"tab_dep")
        self.gridLayout_5 = QGridLayout(self.tab_dep)
        self.gridLayout_5.setObjectName(u"gridLayout_5")
        self.widget_12 = QWidget(self.tab_dep)
        self.widget_12.setObjectName(u"widget_12")
        self.gridLayout_118 = QGridLayout(self.widget_12)
        self.gridLayout_118.setObjectName(u"gridLayout_118")
        self.splitter_6 = QSplitter(self.widget_12)
        self.splitter_6.setObjectName(u"splitter_6")
        self.splitter_6.setOrientation(Qt.Horizontal)
        self.widget_15 = QWidget(self.splitter_6)
        self.widget_15.setObjectName(u"widget_15")
        sizePolicy25 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Preferred)
        sizePolicy25.setHorizontalStretch(1)
        sizePolicy25.setVerticalStretch(1)
        sizePolicy25.setHeightForWidth(self.widget_15.sizePolicy().hasHeightForWidth())
        self.widget_15.setSizePolicy(sizePolicy25)
        self.gridLayout_111 = QGridLayout(self.widget_15)
        self.gridLayout_111.setObjectName(u"gridLayout_111")
        self.label_15 = QLabel(self.widget_15)
        self.label_15.setObjectName(u"label_15")

        self.gridLayout_111.addWidget(self.label_15, 0, 0, 1, 1)

        self.table_dep = wsQTableView(self.widget_15)
        self.table_dep.setObjectName(u"table_dep")
        sizePolicy26 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy26.setHorizontalStretch(2)
        sizePolicy26.setVerticalStretch(0)
        sizePolicy26.setHeightForWidth(self.table_dep.sizePolicy().hasHeightForWidth())
        self.table_dep.setSizePolicy(sizePolicy26)

        self.gridLayout_111.addWidget(self.table_dep, 1, 0, 1, 1)

        self.splitter_6.addWidget(self.widget_15)
        self.widget_18 = QWidget(self.splitter_6)
        self.widget_18.setObjectName(u"widget_18")
        sizePolicy27 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Preferred)
        sizePolicy27.setHorizontalStretch(2)
        sizePolicy27.setVerticalStretch(2)
        sizePolicy27.setHeightForWidth(self.widget_18.sizePolicy().hasHeightForWidth())
        self.widget_18.setSizePolicy(sizePolicy27)
        self.gridLayout_117 = QGridLayout(self.widget_18)
        self.gridLayout_117.setObjectName(u"gridLayout_117")
        self.splitter_5 = QSplitter(self.widget_18)
        self.splitter_5.setObjectName(u"splitter_5")
        self.splitter_5.setOrientation(Qt.Vertical)
        self.widget_13 = QWidget(self.splitter_5)
        self.widget_13.setObjectName(u"widget_13")
        sizePolicy28 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Expanding)
        sizePolicy28.setHorizontalStretch(1)
        sizePolicy28.setVerticalStretch(1)
        sizePolicy28.setHeightForWidth(self.widget_13.sizePolicy().hasHeightForWidth())
        self.widget_13.setSizePolicy(sizePolicy28)
        self.gridLayout_115 = QGridLayout(self.widget_13)
        self.gridLayout_115.setObjectName(u"gridLayout_115")
        self.label_16 = QLabel(self.widget_13)
        self.label_16.setObjectName(u"label_16")

        self.gridLayout_115.addWidget(self.label_16, 0, 0, 1, 1)

        self.table_dep_has_ripso__by_dep_id = myQTableView(self.widget_13)
        self.table_dep_has_ripso__by_dep_id.setObjectName(u"table_dep_has_ripso__by_dep_id")
        sizePolicy29 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy29.setHorizontalStretch(1)
        sizePolicy29.setVerticalStretch(1)
        sizePolicy29.setHeightForWidth(self.table_dep_has_ripso__by_dep_id.sizePolicy().hasHeightForWidth())
        self.table_dep_has_ripso__by_dep_id.setSizePolicy(sizePolicy29)

        self.gridLayout_115.addWidget(self.table_dep_has_ripso__by_dep_id, 1, 0, 1, 1)

        self.splitter_5.addWidget(self.widget_13)
        self.widget_17 = QWidget(self.splitter_5)
        self.widget_17.setObjectName(u"widget_17")
        sizePolicy30 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Expanding)
        sizePolicy30.setHorizontalStretch(0)
        sizePolicy30.setVerticalStretch(2)
        sizePolicy30.setHeightForWidth(self.widget_17.sizePolicy().hasHeightForWidth())
        self.widget_17.setSizePolicy(sizePolicy30)
        self.gridLayout_116 = QGridLayout(self.widget_17)
        self.gridLayout_116.setObjectName(u"gridLayout_116")
        self.label_17 = QLabel(self.widget_17)
        self.label_17.setObjectName(u"label_17")

        self.gridLayout_116.addWidget(self.label_17, 0, 0, 1, 1)

        self.table_dep_has_worker__by_dep_id = myQTableView(self.widget_17)
        self.table_dep_has_worker__by_dep_id.setObjectName(u"table_dep_has_worker__by_dep_id")
        sizePolicy31 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy31.setHorizontalStretch(1)
        sizePolicy31.setVerticalStretch(4)
        sizePolicy31.setHeightForWidth(self.table_dep_has_worker__by_dep_id.sizePolicy().hasHeightForWidth())
        self.table_dep_has_worker__by_dep_id.setSizePolicy(sizePolicy31)

        self.gridLayout_116.addWidget(self.table_dep_has_worker__by_dep_id, 1, 0, 1, 1)

        self.splitter_5.addWidget(self.widget_17)

        self.gridLayout_117.addWidget(self.splitter_5, 0, 0, 1, 1)

        self.splitter_6.addWidget(self.widget_18)

        self.gridLayout_118.addWidget(self.splitter_6, 0, 0, 1, 1)


        self.gridLayout_5.addWidget(self.widget_12, 0, 0, 1, 1)

        self.tabs_admin.addTab(self.tab_dep, "")
        self.tab_roles = myQWidget()
        self.tab_roles.setObjectName(u"tab_roles")
        self.verticalLayout_16 = QVBoxLayout(self.tab_roles)
        self.verticalLayout_16.setObjectName(u"verticalLayout_16")
        self.gridLayout_11 = QGridLayout()
        self.gridLayout_11.setObjectName(u"gridLayout_11")
        self.table_worker__2 = wsQTableView(self.tab_roles)
        self.table_worker__2.setObjectName(u"table_worker__2")

        self.gridLayout_11.addWidget(self.table_worker__2, 2, 0, 1, 1)

        self.label_28 = QLabel(self.tab_roles)
        self.label_28.setObjectName(u"label_28")
        self.label_28.setWordWrap(True)

        self.gridLayout_11.addWidget(self.label_28, 1, 0, 1, 1)

        self.label_26 = QLabel(self.tab_roles)
        self.label_26.setObjectName(u"label_26")

        self.gridLayout_11.addWidget(self.label_26, 0, 0, 1, 1)

        self.table_dep_has_worker__by_worker_id__2 = myQTableView(self.tab_roles)
        self.table_dep_has_worker__by_worker_id__2.setObjectName(u"table_dep_has_worker__by_worker_id__2")

        self.gridLayout_11.addWidget(self.table_dep_has_worker__by_worker_id__2, 2, 1, 1, 1)

        self.label_29 = QLabel(self.tab_roles)
        self.label_29.setObjectName(u"label_29")

        self.gridLayout_11.addWidget(self.label_29, 1, 1, 1, 1)


        self.verticalLayout_16.addLayout(self.gridLayout_11)

        self.tabs_admin.addTab(self.tab_roles, "")
        self.tab_37 = myQWidget()
        self.tab_37.setObjectName(u"tab_37")
        self.gridLayout_77 = QGridLayout(self.tab_37)
        self.gridLayout_77.setObjectName(u"gridLayout_77")
        self.table_live_min = myQTableView(self.tab_37)
        self.table_live_min.setObjectName(u"table_live_min")

        self.gridLayout_77.addWidget(self.table_live_min, 0, 0, 1, 1)

        self.tabs_admin.addTab(self.tab_37, "")
        self.tab_settings = myQWidget()
        self.tab_settings.setObjectName(u"tab_settings")
        self.verticalLayout_7 = QVBoxLayout(self.tab_settings)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.label_30 = QLabel(self.tab_settings)
        self.label_30.setObjectName(u"label_30")

        self.verticalLayout_7.addWidget(self.label_30)

        self.table_setting = myQTableView(self.tab_settings)
        self.table_setting.setObjectName(u"table_setting")

        self.verticalLayout_7.addWidget(self.table_setting)

        self.tabs_admin.addTab(self.tab_settings, "")
        self.tab_notifies = myQWidget()
        self.tab_notifies.setObjectName(u"tab_notifies")
        self.verticalLayout_8 = QVBoxLayout(self.tab_notifies)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.label_12 = QLabel(self.tab_notifies)
        self.label_12.setObjectName(u"label_12")
        self.label_12.setAlignment(Qt.AlignCenter)
        self.label_12.setWordWrap(True)

        self.verticalLayout_8.addWidget(self.label_12)

        self.table_notifies = myQTableView(self.tab_notifies)
        self.table_notifies.setObjectName(u"table_notifies")

        self.verticalLayout_8.addWidget(self.table_notifies)

        self.tabs_admin.addTab(self.tab_notifies, "")
        self.tab_holiday = myQWidget()
        self.tab_holiday.setObjectName(u"tab_holiday")
        self.horizontalLayout_5 = QHBoxLayout(self.tab_holiday)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.table_holiday = myQTableView(self.tab_holiday)
        self.table_holiday.setObjectName(u"table_holiday")

        self.horizontalLayout_5.addWidget(self.table_holiday)

        self.tabs_admin.addTab(self.tab_holiday, "")
        self.tab_26 = myQWidget()
        self.tab_26.setObjectName(u"tab_26")
        self.table = QTableView(self.tab_26)
        self.table.setObjectName(u"table")
        self.table.setGeometry(QRect(60, 170, 871, 401))
        self.gridLayoutWidget = QWidget(self.tab_26)
        self.gridLayoutWidget.setObjectName(u"gridLayoutWidget")
        self.gridLayoutWidget.setGeometry(QRect(270, 60, 251, 80))
        self.gridLayout_16 = QGridLayout(self.gridLayoutWidget)
        self.gridLayout_16.setObjectName(u"gridLayout_16")
        self.pushButton_5 = QPushButton(self.gridLayoutWidget)
        self.pushButton_5.setObjectName(u"pushButton_5")

        self.gridLayout_16.addWidget(self.pushButton_5, 0, 0, 1, 1)

        self.pushButton_6 = QPushButton(self.gridLayoutWidget)
        self.pushButton_6.setObjectName(u"pushButton_6")

        self.gridLayout_16.addWidget(self.pushButton_6, 0, 1, 1, 1)

        self.tabs_admin.addTab(self.tab_26, "")
        self.tab_sql_check = myQWidget()
        self.tab_sql_check.setObjectName(u"tab_sql_check")
        self.gridLayout_26 = QGridLayout(self.tab_sql_check)
        self.gridLayout_26.setObjectName(u"gridLayout_26")
        self.txt_sql2 = QPlainTextEdit(self.tab_sql_check)
        self.txt_sql2.setObjectName(u"txt_sql2")

        self.gridLayout_26.addWidget(self.txt_sql2, 2, 0, 1, 1)

        self.btn_check_sql = QPushButton(self.tab_sql_check)
        self.btn_check_sql.setObjectName(u"btn_check_sql")

        self.gridLayout_26.addWidget(self.btn_check_sql, 0, 0, 1, 1)

        self.txt_sql = QPlainTextEdit(self.tab_sql_check)
        self.txt_sql.setObjectName(u"txt_sql")

        self.gridLayout_26.addWidget(self.txt_sql, 1, 0, 1, 2)

        self.test_tableView = stubQTableView(self.tab_sql_check)
        self.test_tableView.setObjectName(u"test_tableView")

        self.gridLayout_26.addWidget(self.test_tableView, 3, 0, 1, 1)

        self.tabs_admin.addTab(self.tab_sql_check, "")
        self.tab_3 = myQWidget()
        self.tab_3.setObjectName(u"tab_3")
        self.gridLayout_13 = QGridLayout(self.tab_3)
        self.gridLayout_13.setObjectName(u"gridLayout_13")
        self.label_18 = QLabel(self.tab_3)
        self.label_18.setObjectName(u"label_18")

        self.gridLayout_13.addWidget(self.label_18, 0, 1, 1, 1)

        self.table_complex_dep_has_dep__by_complex_dep = myQTableView(self.tab_3)
        self.table_complex_dep_has_dep__by_complex_dep.setObjectName(u"table_complex_dep_has_dep__by_complex_dep")

        self.gridLayout_13.addWidget(self.table_complex_dep_has_dep__by_complex_dep, 1, 1, 1, 1)

        self.label_9 = QLabel(self.tab_3)
        self.label_9.setObjectName(u"label_9")

        self.gridLayout_13.addWidget(self.label_9, 0, 0, 1, 1)

        self.table_complex_dep = wsQTableView(self.tab_3)
        self.table_complex_dep.setObjectName(u"table_complex_dep")

        self.gridLayout_13.addWidget(self.table_complex_dep, 1, 0, 1, 1)

        self.tabs_admin.addTab(self.tab_3, "")

        self.horizontalLayout.addWidget(self.tabs_admin)

        self.tabMain.addTab(self.tab_admin, "")
        self.tab_journal = myQWidgetUnblockable()
        self.tab_journal.setObjectName(u"tab_journal")
        self.gridLayout_12 = QGridLayout(self.tab_journal)
        self.gridLayout_12.setObjectName(u"gridLayout_12")
        self.pushButton_24 = QPushButton(self.tab_journal)
        self.pushButton_24.setObjectName(u"pushButton_24")

        self.gridLayout_12.addWidget(self.pushButton_24, 0, 2, 1, 1)

        self.pushButton_32 = QPushButton(self.tab_journal)
        self.pushButton_32.setObjectName(u"pushButton_32")

        self.gridLayout_12.addWidget(self.pushButton_32, 0, 1, 1, 1)

        self.pushButton_16 = QPushButton(self.tab_journal)
        self.pushButton_16.setObjectName(u"pushButton_16")

        self.gridLayout_12.addWidget(self.pushButton_16, 0, 0, 1, 1)

        self.journal_table = tsQTableViewYear(self.tab_journal)
        self.journal_table.setObjectName(u"journal_table")

        self.gridLayout_12.addWidget(self.journal_table, 1, 0, 1, 3)

        self.tabMain.addTab(self.tab_journal, "")
        self.tab_pyc = myQWidget()
        self.tab_pyc.setObjectName(u"tab_pyc")
        self.gridLayout_94 = QGridLayout(self.tab_pyc)
        self.gridLayout_94.setObjectName(u"gridLayout_94")
        self.tabMain.addTab(self.tab_pyc, "")
        self.tab_export = myQWidget()
        self.tab_export.setObjectName(u"tab_export")
        self.gridLayout_72 = QGridLayout(self.tab_export)
        self.gridLayout_72.setObjectName(u"gridLayout_72")
        self.report__call_export_dep__where_period__2 = qcSelectReport(self.tab_export)
        self.report__call_export_dep__where_period__2.setObjectName(u"report__call_export_dep__where_period__2")
        self.gridLayout_70 = QGridLayout(self.report__call_export_dep__where_period__2)
        self.gridLayout_70.setObjectName(u"gridLayout_70")
        self.table__dep_has_main_6 = QTableView(self.report__call_export_dep__where_period__2)
        self.table__dep_has_main_6.setObjectName(u"table__dep_has_main_6")

        self.gridLayout_70.addWidget(self.table__dep_has_main_6, 3, 0, 1, 2)

        self.pushButton_29 = QPushButton(self.report__call_export_dep__where_period__2)
        self.pushButton_29.setObjectName(u"pushButton_29")

        self.gridLayout_70.addWidget(self.pushButton_29, 2, 1, 1, 1)

        self.btn_serv_you_15 = QPushButton(self.report__call_export_dep__where_period__2)
        self.btn_serv_you_15.setObjectName(u"btn_serv_you_15")

        self.gridLayout_70.addWidget(self.btn_serv_you_15, 2, 0, 1, 1)

        self.frame_14 = QFrame(self.report__call_export_dep__where_period__2)
        self.frame_14.setObjectName(u"frame_14")
        self.frame_14.setFrameShape(QFrame.StyledPanel)
        self.frame_14.setFrameShadow(QFrame.Raised)
        self.gridLayout_71 = QGridLayout(self.frame_14)
        self.gridLayout_71.setObjectName(u"gridLayout_71")
        self.DO_NOT_USE_170 = myQTabWidget(self.frame_14)
        self.DO_NOT_USE_170.setObjectName(u"DO_NOT_USE_170")
        sizePolicy14.setHeightForWidth(self.DO_NOT_USE_170.sizePolicy().hasHeightForWidth())
        self.DO_NOT_USE_170.setSizePolicy(sizePolicy14)
        self.DO_NOT_USE_170.setMinimumSize(QSize(300, 0))
        self.DO_NOT_USE_171 = QWidget()
        self.DO_NOT_USE_171.setObjectName(u"DO_NOT_USE_171")
        self.verticalLayout_86 = QVBoxLayout(self.DO_NOT_USE_171)
        self.verticalLayout_86.setObjectName(u"verticalLayout_86")
        self.DO_NOT_USE_172 = QGridLayout()
        self.DO_NOT_USE_172.setObjectName(u"DO_NOT_USE_172")
        self.DO_NOT_USE_172.setHorizontalSpacing(0)
        self.DO_NOT_USE_173 = QDateEdit(self.DO_NOT_USE_171)
        self.DO_NOT_USE_173.setObjectName(u"DO_NOT_USE_173")

        self.DO_NOT_USE_172.addWidget(self.DO_NOT_USE_173, 1, 1, 1, 1)

        self.DO_NOT_USE_174 = QLabel(self.DO_NOT_USE_171)
        self.DO_NOT_USE_174.setObjectName(u"DO_NOT_USE_174")
        sizePolicy5.setHeightForWidth(self.DO_NOT_USE_174.sizePolicy().hasHeightForWidth())
        self.DO_NOT_USE_174.setSizePolicy(sizePolicy5)
        self.DO_NOT_USE_174.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.DO_NOT_USE_172.addWidget(self.DO_NOT_USE_174, 1, 0, 1, 1)

        self.DO_NOT_USE_175 = QLabel(self.DO_NOT_USE_171)
        self.DO_NOT_USE_175.setObjectName(u"DO_NOT_USE_175")
        sizePolicy5.setHeightForWidth(self.DO_NOT_USE_175.sizePolicy().hasHeightForWidth())
        self.DO_NOT_USE_175.setSizePolicy(sizePolicy5)
        self.DO_NOT_USE_175.setLayoutDirection(Qt.LeftToRight)
        self.DO_NOT_USE_175.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.DO_NOT_USE_172.addWidget(self.DO_NOT_USE_175, 0, 0, 1, 1)

        self.DO_NOT_USE_176 = QDateEdit(self.DO_NOT_USE_171)
        self.DO_NOT_USE_176.setObjectName(u"DO_NOT_USE_176")

        self.DO_NOT_USE_172.addWidget(self.DO_NOT_USE_176, 0, 1, 1, 1)

        self.DO_NOT_USE_172.setColumnStretch(0, 1)
        self.DO_NOT_USE_172.setColumnStretch(1, 2)

        self.verticalLayout_86.addLayout(self.DO_NOT_USE_172)

        self.DO_NOT_USE_170.addTab(self.DO_NOT_USE_171, "")
        self.DO_NOT_USE_177 = QWidget()
        self.DO_NOT_USE_177.setObjectName(u"DO_NOT_USE_177")
        self.verticalLayout_87 = QVBoxLayout(self.DO_NOT_USE_177)
        self.verticalLayout_87.setObjectName(u"verticalLayout_87")
        self.DO_NOT_USE_178 = QGridLayout()
        self.DO_NOT_USE_178.setObjectName(u"DO_NOT_USE_178")
        self.DO_NOT_USE_179 = QLabel(self.DO_NOT_USE_177)
        self.DO_NOT_USE_179.setObjectName(u"DO_NOT_USE_179")
        self.DO_NOT_USE_179.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.DO_NOT_USE_178.addWidget(self.DO_NOT_USE_179, 0, 0, 1, 1)

        self.DO_NOT_USE_180 = QSpinBox(self.DO_NOT_USE_177)
        self.DO_NOT_USE_180.setObjectName(u"DO_NOT_USE_180")
        self.DO_NOT_USE_180.setMinimum(1950)
        self.DO_NOT_USE_180.setMaximum(2050)
        self.DO_NOT_USE_180.setValue(2019)

        self.DO_NOT_USE_178.addWidget(self.DO_NOT_USE_180, 1, 1, 1, 1)

        self.DO_NOT_USE_181 = QLabel(self.DO_NOT_USE_177)
        self.DO_NOT_USE_181.setObjectName(u"DO_NOT_USE_181")
        self.DO_NOT_USE_181.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.DO_NOT_USE_178.addWidget(self.DO_NOT_USE_181, 1, 0, 1, 1)

        self.DO_NOT_USE_182 = QComboBox(self.DO_NOT_USE_177)
        self.DO_NOT_USE_182.setObjectName(u"DO_NOT_USE_182")
        self.DO_NOT_USE_182.setEditable(True)

        self.DO_NOT_USE_178.addWidget(self.DO_NOT_USE_182, 0, 1, 1, 1)

        self.DO_NOT_USE_178.setColumnStretch(0, 1)
        self.DO_NOT_USE_178.setColumnStretch(1, 2)

        self.verticalLayout_87.addLayout(self.DO_NOT_USE_178)

        self.DO_NOT_USE_170.addTab(self.DO_NOT_USE_177, "")

        self.gridLayout_71.addWidget(self.DO_NOT_USE_170, 0, 0, 1, 1)


        self.gridLayout_70.addWidget(self.frame_14, 1, 0, 1, 1)


        self.gridLayout_72.addWidget(self.report__call_export_dep__where_period__2, 0, 0, 1, 1)

        self.tabMain.addTab(self.tab_export, "")

        self.vl_centralwidget.addWidget(self.tabMain)


        self.horizontalLayout_26.addLayout(self.vl_centralwidget)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 1672, 21))
        self.menu = QMenu(self.menubar)
        self.menu.setObjectName(u"menu")
        self.menu_2 = QMenu(self.menubar)
        self.menu_2.setObjectName(u"menu_2")
        self.menu_3 = QMenu(self.menubar)
        self.menu_3.setObjectName(u"menu_3")
        self.menu_settings = QMenu(self.menubar)
        self.menu_settings.setObjectName(u"menu_settings")
        self.menu_5 = QMenu(self.menubar)
        self.menu_5.setObjectName(u"menu_5")
        self.menu_7 = QMenu(self.menubar)
        self.menu_7.setObjectName(u"menu_7")
        self.menu_4 = QMenu(self.menubar)
        self.menu_4.setObjectName(u"menu_4")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.toolBar = QToolBar(MainWindow)
        self.toolBar.setObjectName(u"toolBar")
        MainWindow.addToolBar(Qt.TopToolBarArea, self.toolBar)
        self.toolBar_2 = QToolBar(MainWindow)
        self.toolBar_2.setObjectName(u"toolBar_2")
        self.toolBar_2.setFont(font3)
        self.toolBar_2.setContextMenuPolicy(Qt.NoContextMenu)
        self.toolBar_2.setToolButtonStyle(Qt.ToolButtonTextBesideIcon)
        MainWindow.addToolBar(Qt.TopToolBarArea, self.toolBar_2)
        self.dock_people_info = infoQDockWidget(MainWindow)
        self.dock_people_info.setObjectName(u"dock_people_info")
        sizePolicy32 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy32.setHorizontalStretch(1)
        sizePolicy32.setVerticalStretch(1)
        sizePolicy32.setHeightForWidth(self.dock_people_info.sizePolicy().hasHeightForWidth())
        self.dock_people_info.setSizePolicy(sizePolicy32)
        self.dock_people_info.setBaseSize(QSize(300, 0))
        self.dockWidgetContents = QWidget()
        self.dockWidgetContents.setObjectName(u"dockWidgetContents")
        self.gridLayout_106 = QGridLayout(self.dockWidgetContents)
        self.gridLayout_106.setObjectName(u"gridLayout_106")
        self.gridLayout_85 = QGridLayout()
        self.gridLayout_85.setObjectName(u"gridLayout_85")
        self.label_79 = QLabel(self.dockWidgetContents)
        self.label_79.setObjectName(u"label_79")

        self.gridLayout_85.addWidget(self.label_79, 4, 0, 1, 2)

        self.label_82 = QLabel(self.dockWidgetContents)
        self.label_82.setObjectName(u"label_82")

        self.gridLayout_85.addWidget(self.label_82, 12, 0, 1, 1)

        self.qle_serv_total = QLineEdit(self.dockWidgetContents)
        self.qle_serv_total.setObjectName(u"qle_serv_total")
        sizePolicy4.setHeightForWidth(self.qle_serv_total.sizePolicy().hasHeightForWidth())
        self.qle_serv_total.setSizePolicy(sizePolicy4)

        self.gridLayout_85.addWidget(self.qle_serv_total, 11, 0, 1, 2)

        self.cbx_1_servform = myQComboBox(self.dockWidgetContents)
        self.cbx_1_servform.setObjectName(u"cbx_1_servform")

        self.gridLayout_85.addWidget(self.cbx_1_servform, 5, 0, 1, 2)

        self.label_80 = QLabel(self.dockWidgetContents)
        self.label_80.setObjectName(u"label_80")

        self.gridLayout_85.addWidget(self.label_80, 6, 0, 1, 2)

        self.horizontalLayout_27 = QHBoxLayout()
        self.horizontalLayout_27.setObjectName(u"horizontalLayout_27")
        self.pushButton_13 = QPushButton(self.dockWidgetContents)
        self.pushButton_13.setObjectName(u"pushButton_13")
        sizePolicy3.setHeightForWidth(self.pushButton_13.sizePolicy().hasHeightForWidth())
        self.pushButton_13.setSizePolicy(sizePolicy3)
        self.pushButton_13.setMaximumSize(QSize(20, 16777215))

        self.horizontalLayout_27.addWidget(self.pushButton_13)

        self.qle_month = QLineEdit(self.dockWidgetContents)
        self.qle_month.setObjectName(u"qle_month")
        sizePolicy6.setHeightForWidth(self.qle_month.sizePolicy().hasHeightForWidth())
        self.qle_month.setSizePolicy(sizePolicy6)

        self.horizontalLayout_27.addWidget(self.qle_month)

        self.pushButton_14 = QPushButton(self.dockWidgetContents)
        self.pushButton_14.setObjectName(u"pushButton_14")
        sizePolicy3.setHeightForWidth(self.pushButton_14.sizePolicy().hasHeightForWidth())
        self.pushButton_14.setSizePolicy(sizePolicy3)
        self.pushButton_14.setMaximumSize(QSize(20, 16777215))

        self.horizontalLayout_27.addWidget(self.pushButton_14)


        self.gridLayout_85.addLayout(self.horizontalLayout_27, 9, 0, 1, 2)

        self.qle_topay = QLineEdit(self.dockWidgetContents)
        self.qle_topay.setObjectName(u"qle_topay")
        sizePolicy4.setHeightForWidth(self.qle_topay.sizePolicy().hasHeightForWidth())
        self.qle_topay.setSizePolicy(sizePolicy4)

        self.gridLayout_85.addWidget(self.qle_topay, 13, 0, 1, 2)

        self.verticalSpacer_21 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout_85.addItem(self.verticalSpacer_21, 17, 1, 1, 1)

        self.label_78 = QLabel(self.dockWidgetContents)
        self.label_78.setObjectName(u"label_78")

        self.gridLayout_85.addWidget(self.label_78, 2, 0, 1, 1)

        self.qle_contract = QLineEdit(self.dockWidgetContents)
        self.qle_contract.setObjectName(u"qle_contract")
        sizePolicy4.setHeightForWidth(self.qle_contract.sizePolicy().hasHeightForWidth())
        self.qle_contract.setSizePolicy(sizePolicy4)

        self.gridLayout_85.addWidget(self.qle_contract, 3, 0, 1, 2)

        self.qle_last_fio = QLineEdit(self.dockWidgetContents)
        self.qle_last_fio.setObjectName(u"qle_last_fio")
        sizePolicy4.setHeightForWidth(self.qle_last_fio.sizePolicy().hasHeightForWidth())
        self.qle_last_fio.setSizePolicy(sizePolicy4)

        self.gridLayout_85.addWidget(self.qle_last_fio, 1, 0, 1, 2)

        self.label_77 = QLabel(self.dockWidgetContents)
        self.label_77.setObjectName(u"label_77")

        self.gridLayout_85.addWidget(self.label_77, 0, 0, 1, 1)

        self.label_81 = QLabel(self.dockWidgetContents)
        self.label_81.setObjectName(u"label_81")

        self.gridLayout_85.addWidget(self.label_81, 10, 0, 1, 1)

        self.label_89 = QLabel(self.dockWidgetContents)
        self.label_89.setObjectName(u"label_89")

        self.gridLayout_85.addWidget(self.label_89, 15, 0, 1, 1)

        self.qle_sdd = QLineEdit(self.dockWidgetContents)
        self.qle_sdd.setObjectName(u"qle_sdd")
        sizePolicy4.setHeightForWidth(self.qle_sdd.sizePolicy().hasHeightForWidth())
        self.qle_sdd.setSizePolicy(sizePolicy4)

        self.gridLayout_85.addWidget(self.qle_sdd, 15, 1, 1, 1)

        self.qle_dock_state = QLineEdit(self.dockWidgetContents)
        self.qle_dock_state.setObjectName(u"qle_dock_state")

        self.gridLayout_85.addWidget(self.qle_dock_state, 16, 0, 1, 2)


        self.gridLayout_106.addLayout(self.gridLayout_85, 0, 1, 1, 1)

        self.dock_people_info.setWidget(self.dockWidgetContents)
        MainWindow.addDockWidget(Qt.RightDockWidgetArea, self.dock_people_info)
#if QT_CONFIG(shortcut)
        self.label_client.setBuddy(self.qle_table_client_filter)
#endif // QT_CONFIG(shortcut)
        QWidget.setTabOrder(self.qle_date, self.cbx_1__dep_has_client__2)
        QWidget.setTabOrder(self.cbx_1__dep_has_client__2, self.cbx_1__dep_has_worker)
        QWidget.setTabOrder(self.cbx_1__dep_has_worker, self.cbx_1__serv_activ__dis_total)
        QWidget.setTabOrder(self.cbx_1__serv_activ__dis_total, self.qleNote)
        QWidget.setTabOrder(self.qleNote, self.btn_serv_bydayQ)
        QWidget.setTabOrder(self.btn_serv_bydayQ, self.btn_serv_bydayW)
        QWidget.setTabOrder(self.btn_serv_bydayW, self.btn_serv_bydayE)
        QWidget.setTabOrder(self.btn_serv_bydayE, self.btn_serv_bydayA)
        QWidget.setTabOrder(self.btn_serv_bydayA, self.chkLFio)
        QWidget.setTabOrder(self.chkLFio, self.chkLW)
        QWidget.setTabOrder(self.chkLW, self.chkLServ)
        QWidget.setTabOrder(self.chkLServ, self.btn_qle_date_1)
        QWidget.setTabOrder(self.btn_qle_date_1, self.btn_qle_date_p1)
        QWidget.setTabOrder(self.btn_qle_date_p1, self.tab__main_for_dep_by)
        QWidget.setTabOrder(self.tab__main_for_dep_by, self.table__dep_has_main__where_vdate__by_vdate)
        QWidget.setTabOrder(self.table__dep_has_main__where_vdate__by_vdate, self.table__dep_has_main__where_vdate__by_vdate_by_worker_id)
        QWidget.setTabOrder(self.table__dep_has_main__where_vdate__by_vdate_by_worker_id, self.table__dep_has_main__where_vdate__by_vdate_by_you)
        QWidget.setTabOrder(self.table__dep_has_main__where_vdate__by_vdate_by_you, self.table__dep_has_main__where_vdate__by_vdate_by_serv_id)
        QWidget.setTabOrder(self.table__dep_has_main__where_vdate__by_vdate_by_serv_id, self.table__client_has_valid_contracts__by_client)
        QWidget.setTabOrder(self.table__client_has_valid_contracts__by_client, self.tabs_client2)
        QWidget.setTabOrder(self.tabs_client2, self.btn_upd_fio_list)
        QWidget.setTabOrder(self.btn_upd_fio_list, self.pushButton_2)
        QWidget.setTabOrder(self.pushButton_2, self.table__dep_has_client_by_ripso__by_client)
        QWidget.setTabOrder(self.table__dep_has_client_by_ripso__by_client, self.qle_FIO)
        QWidget.setTabOrder(self.qle_FIO, self.table__client_has_add_info__where_client_id__by_client_id)
        QWidget.setTabOrder(self.table__client_has_add_info__where_client_id__by_client_id, self.table_ripso_has_serv__by_ripso_id)
        QWidget.setTabOrder(self.table_ripso_has_serv__by_ripso_id, self.table_ripso)
        QWidget.setTabOrder(self.table_ripso, self.table_dep_has_worker__by_worker_id)
        QWidget.setTabOrder(self.table_dep_has_worker__by_worker_id, self.btn_show_qrcode)
        QWidget.setTabOrder(self.btn_show_qrcode, self.table_worker)
        QWidget.setTabOrder(self.table_worker, self.cbx_1_worker__pass)
        QWidget.setTabOrder(self.cbx_1_worker__pass, self.lineEdit_login)
        QWidget.setTabOrder(self.lineEdit_login, self.btn_pw_gen)
        QWidget.setTabOrder(self.btn_pw_gen, self.btn_update_login_pass)
        QWidget.setTabOrder(self.btn_update_login_pass, self.btnClean)
        QWidget.setTabOrder(self.btnClean, self.table_worker__2)
        QWidget.setTabOrder(self.table_worker__2, self.table_dep_has_worker__by_worker_id__2)
        QWidget.setTabOrder(self.table_dep_has_worker__by_worker_id__2, self.table_dep_has_ripso__by_dep_id)
        QWidget.setTabOrder(self.table_dep_has_ripso__by_dep_id, self.table_dep_has_worker__by_dep_id)
        QWidget.setTabOrder(self.table_dep_has_worker__by_dep_id, self.table_dep)
        QWidget.setTabOrder(self.table_dep, self.table_setting)
        QWidget.setTabOrder(self.table_setting, self.table_notifies)
        QWidget.setTabOrder(self.table_notifies, self.table_holiday)
        QWidget.setTabOrder(self.table_holiday, self.table)
        QWidget.setTabOrder(self.table, self.pushButton_5)
        QWidget.setTabOrder(self.pushButton_5, self.pushButton_6)
        QWidget.setTabOrder(self.pushButton_6, self.btn_check_sql)
        QWidget.setTabOrder(self.btn_check_sql, self.txt_sql)
        QWidget.setTabOrder(self.txt_sql, self.txt_sql2)
        QWidget.setTabOrder(self.txt_sql2, self.pushButton_10)
        QWidget.setTabOrder(self.pushButton_10, self.lineEdit)
        QWidget.setTabOrder(self.lineEdit, self.tableView_2)
        QWidget.setTabOrder(self.tableView_2, self.qle_date_2)
        QWidget.setTabOrder(self.qle_date_2, self.comboServ_2)
        QWidget.setTabOrder(self.comboServ_2, self.comboW_2)
        QWidget.setTabOrder(self.comboW_2, self.qleAmount_2)
        QWidget.setTabOrder(self.qleAmount_2, self.qleNote_2)
        QWidget.setTabOrder(self.qleNote_2, self.pushButton_8)
        QWidget.setTabOrder(self.pushButton_8, self.tableView_5)
        QWidget.setTabOrder(self.tableView_5, self.pushButton_12)
        QWidget.setTabOrder(self.pushButton_12, self.btn_qle_date_2)
        QWidget.setTabOrder(self.btn_qle_date_2, self.pushButton_9)
        QWidget.setTabOrder(self.pushButton_9, self.plainTextEdit)
        QWidget.setTabOrder(self.plainTextEdit, self.pushButton_11)
        QWidget.setTabOrder(self.pushButton_11, self.btn_qle_date_p1_2)
        QWidget.setTabOrder(self.btn_qle_date_p1_2, self.chkLAmount)
        QWidget.setTabOrder(self.chkLAmount, self.qleAmount)
        QWidget.setTabOrder(self.qleAmount, self.qle_serv_left)
        QWidget.setTabOrder(self.qle_serv_left, self.cbx_1_ui_select_fiolist)
        QWidget.setTabOrder(self.cbx_1_ui_select_fiolist, self.btn_goto_client)
        QWidget.setTabOrder(self.btn_goto_client, self.btn_goto_worker)
        QWidget.setTabOrder(self.btn_goto_worker, self.table__dep_has_main__where_vdate__by_vdate_by_client_id)
        QWidget.setTabOrder(self.table__dep_has_main__where_vdate__by_vdate_by_client_id, self.cbx_1__dep_has_client__3)
        QWidget.setTabOrder(self.cbx_1__dep_has_client__3, self.cbx_1__dep_has_worker__2)
        QWidget.setTabOrder(self.cbx_1__dep_has_worker__2, self.cbx_1__serv_activ__dis_total__2)
        QWidget.setTabOrder(self.cbx_1__serv_activ__dis_total__2, self.chk_mouse_left)
        QWidget.setTabOrder(self.chk_mouse_left, self.chk_continue_input)
        QWidget.setTabOrder(self.chk_continue_input, self.pb_start_serv_add)
        QWidget.setTabOrder(self.pb_start_serv_add, self.chk_wheel)
        QWidget.setTabOrder(self.chk_wheel, self.qleAmount2)
        QWidget.setTabOrder(self.qleAmount2, self.chk_enter_input)
        QWidget.setTabOrder(self.chk_enter_input, self.clndr__dep_has_main_raw__where_calendar)
        QWidget.setTabOrder(self.clndr__dep_has_main_raw__where_calendar, self.qleNote2)
        QWidget.setTabOrder(self.qleNote2, self.cbx_1_ui_select_fiolist__3)
        QWidget.setTabOrder(self.cbx_1_ui_select_fiolist__3, self.tab_user_has_main)
        QWidget.setTabOrder(self.tab_user_has_main, self.table__user_has_main_today)
        QWidget.setTabOrder(self.table__user_has_main_today, self.table__user_has_main_limit30)
        QWidget.setTabOrder(self.table__user_has_main_limit30, self.table__dep_has_main__where_calendar__by_vdate__2)
        QWidget.setTabOrder(self.table__dep_has_main__where_calendar__by_vdate__2, self.lineEdit_15)
        QWidget.setTabOrder(self.lineEdit_15, self.table__dep_has_main__where_calendar__by_vdate_by_client_id__2)
        QWidget.setTabOrder(self.table__dep_has_main__where_calendar__by_vdate_by_client_id__2, self.table__dep_has_main__where_calendar__by_vdate_by_serv_id__2)
        QWidget.setTabOrder(self.table__dep_has_main__where_calendar__by_vdate_by_serv_id__2, self.table__dep_has_main__where_calendar__by_vdate_by_worker_id__3)
        QWidget.setTabOrder(self.table__dep_has_main__where_calendar__by_vdate_by_worker_id__3, self.table__dep_has_main__where_calendar__by_vdate_by_client_id_by_serv_id)
        QWidget.setTabOrder(self.table__dep_has_main__where_calendar__by_vdate_by_client_id_by_serv_id, self.textEdit_2)
        QWidget.setTabOrder(self.textEdit_2, self.tabs_fio_dep)
        QWidget.setTabOrder(self.tabs_fio_dep, self.btn_goto_client_from_list)
        QWidget.setTabOrder(self.btn_goto_client_from_list, self.btn_goto_serv_from_list)
        QWidget.setTabOrder(self.btn_goto_serv_from_list, self.table__dep_has_client__by_client)
        QWidget.setTabOrder(self.table__dep_has_client__by_client, self.table__dep_has_client_count_main_year__by_client)
        QWidget.setTabOrder(self.table__dep_has_client_count_main_year__by_client, self.table__dep_has_client_blocked_in_year__by_client_2)
        QWidget.setTabOrder(self.table__dep_has_client_blocked_in_year__by_client_2, self.table__dep_has_client_ending__by_client)
        QWidget.setTabOrder(self.table__dep_has_client_ending__by_client, self.table__dep_has_client_ended__by_client)
        QWidget.setTabOrder(self.table__dep_has_client_ended__by_client, self.table__dep_has_client_more__by_client)
        QWidget.setTabOrder(self.table__dep_has_client_more__by_client, self.table__dep_has_new_client__by_client_2)
        QWidget.setTabOrder(self.table__dep_has_new_client__by_client_2, self.qle_fio_filter)
        QWidget.setTabOrder(self.qle_fio_filter, self.qle_table_client_filter)
        QWidget.setTabOrder(self.qle_table_client_filter, self.table_client__by_client)
        QWidget.setTabOrder(self.table_client__by_client, self.pushButton_15)
        QWidget.setTabOrder(self.pushButton_15, self.table__client_has_invalid_contracts__by_client)
        QWidget.setTabOrder(self.table__client_has_invalid_contracts__by_client, self.btn_goto_serv_add)
        QWidget.setTabOrder(self.btn_goto_serv_add, self.btn_prev)
        QWidget.setTabOrder(self.btn_prev, self.cbx_1__dep_has_client)
        QWidget.setTabOrder(self.cbx_1__dep_has_client, self.btn_next)
        QWidget.setTabOrder(self.btn_next, self.cbx_1_ui_select_fiolist__2)
        QWidget.setTabOrder(self.cbx_1_ui_select_fiolist__2, self.tabs_client2)
        QWidget.setTabOrder(self.tabs_client2, self.dateEdit_death)
        QWidget.setTabOrder(self.dateEdit_death, self.lineEdit_phone)
        QWidget.setTabOrder(self.lineEdit_phone, self.dateEdit_birth)
        QWidget.setTabOrder(self.dateEdit_birth, self.qle_SNILS)
        QWidget.setTabOrder(self.qle_SNILS, self.sp_ESRN)
        QWidget.setTabOrder(self.sp_ESRN, self.pte_note)
        QWidget.setTabOrder(self.pte_note, self.table_client_has_category__by_client_id)
        QWidget.setTabOrder(self.table_client_has_category__by_client_id, self.sp_ippsuNum)
        QWidget.setTabOrder(self.sp_ippsuNum, self.cbx_0_worker_has_dep)
        QWidget.setTabOrder(self.cbx_0_worker_has_dep, self.cbx_0__dep_has_ripso)
        QWidget.setTabOrder(self.cbx_0__dep_has_ripso, self.de_startdate)
        QWidget.setTabOrder(self.de_startdate, self.de_enddate)
        QWidget.setTabOrder(self.de_enddate, self.chk_blocked)
        QWidget.setTabOrder(self.chk_blocked, self.tab_sub_client)
        QWidget.setTabOrder(self.tab_sub_client, self.table_main__where_client_id__by_contracts_id)
        QWidget.setTabOrder(self.table_main__where_client_id__by_contracts_id, self.table__client_has_add_info__where_client_id__by_contracts_id)
        QWidget.setTabOrder(self.table__client_has_add_info__where_client_id__by_contracts_id, self.btn_prev_2)
        QWidget.setTabOrder(self.btn_prev_2, self.cbx_1_contracts__by_client_id)
        QWidget.setTabOrder(self.cbx_1_contracts__by_client_id, self.btn_next_2)
        QWidget.setTabOrder(self.btn_next_2, self.pte_contracts_note)
        QWidget.setTabOrder(self.pte_contracts_note, self.table_main__where_client_id__by_dep_id)
        QWidget.setTabOrder(self.table_main__where_client_id__by_dep_id, self.tabs_total)
        QWidget.setTabOrder(self.tabs_total, self.tabs_tot_serv)
        QWidget.setTabOrder(self.tabs_tot_serv, self.btn_serv_you_3)
        QWidget.setTabOrder(self.btn_serv_you_3, self.pushButton_17)
        QWidget.setTabOrder(self.pushButton_17, self.lineEdit_2)
        QWidget.setTabOrder(self.lineEdit_2, self.treeView)
        QWidget.setTabOrder(self.treeView, self.t_main_for_dep)
        QWidget.setTabOrder(self.t_main_for_dep, self.DO_NOT_USE_14)
        QWidget.setTabOrder(self.DO_NOT_USE_14, self.DO_NOT_USE_17)
        QWidget.setTabOrder(self.DO_NOT_USE_17, self.DO_NOT_USE_20)
        QWidget.setTabOrder(self.DO_NOT_USE_20, self.DO_NOT_USE_24)
        QWidget.setTabOrder(self.DO_NOT_USE_24, self.DO_NOT_USE_26)
        QWidget.setTabOrder(self.DO_NOT_USE_26, self.btn_serv_you_5)
        QWidget.setTabOrder(self.btn_serv_you_5, self.pushButton_19)
        QWidget.setTabOrder(self.pushButton_19, self.DO_NOT_USE_53)
        QWidget.setTabOrder(self.DO_NOT_USE_53, self.DO_NOT_USE_69)
        QWidget.setTabOrder(self.DO_NOT_USE_69, self.DO_NOT_USE_72)
        QWidget.setTabOrder(self.DO_NOT_USE_72, self.DO_NOT_USE_76)
        QWidget.setTabOrder(self.DO_NOT_USE_76, self.DO_NOT_USE_78)
        QWidget.setTabOrder(self.DO_NOT_USE_78, self.t_main_for_dep_2)
        QWidget.setTabOrder(self.t_main_for_dep_2, self.btn_serv_you_6)
        QWidget.setTabOrder(self.btn_serv_you_6, self.pushButton_20)
        QWidget.setTabOrder(self.pushButton_20, self.DO_NOT_USE_79)
        QWidget.setTabOrder(self.DO_NOT_USE_79, self.DO_NOT_USE_82)
        QWidget.setTabOrder(self.DO_NOT_USE_82, self.DO_NOT_USE_85)
        QWidget.setTabOrder(self.DO_NOT_USE_85, self.DO_NOT_USE_89)
        QWidget.setTabOrder(self.DO_NOT_USE_89, self.DO_NOT_USE_91)
        QWidget.setTabOrder(self.DO_NOT_USE_91, self.table__dep_has_main_3)
        QWidget.setTabOrder(self.table__dep_has_main_3, self.cbx_1_dep_has_worker)
        QWidget.setTabOrder(self.cbx_1_dep_has_worker, self.table__dep_has_main_4)
        QWidget.setTabOrder(self.table__dep_has_main_4, self.pushButton_21)
        QWidget.setTabOrder(self.pushButton_21, self.btn_serv_you_7)
        QWidget.setTabOrder(self.btn_serv_you_7, self.DO_NOT_USE_92)
        QWidget.setTabOrder(self.DO_NOT_USE_92, self.DO_NOT_USE_95)
        QWidget.setTabOrder(self.DO_NOT_USE_95, self.DO_NOT_USE_98)
        QWidget.setTabOrder(self.DO_NOT_USE_98, self.DO_NOT_USE_102)
        QWidget.setTabOrder(self.DO_NOT_USE_102, self.DO_NOT_USE_104)
        QWidget.setTabOrder(self.DO_NOT_USE_104, self.table__dep_has_main_5)
        QWidget.setTabOrder(self.table__dep_has_main_5, self.pushButton_22)
        QWidget.setTabOrder(self.pushButton_22, self.btn_serv_you_8)
        QWidget.setTabOrder(self.btn_serv_you_8, self.DO_NOT_USE_105)
        QWidget.setTabOrder(self.DO_NOT_USE_105, self.DO_NOT_USE_108)
        QWidget.setTabOrder(self.DO_NOT_USE_108, self.DO_NOT_USE_111)
        QWidget.setTabOrder(self.DO_NOT_USE_111, self.DO_NOT_USE_115)
        QWidget.setTabOrder(self.DO_NOT_USE_115, self.DO_NOT_USE_117)
        QWidget.setTabOrder(self.DO_NOT_USE_117, self.tabWidget_8)
        QWidget.setTabOrder(self.tabWidget_8, self.btn_serv_you_4)
        QWidget.setTabOrder(self.btn_serv_you_4, self.pushButton_18)
        QWidget.setTabOrder(self.pushButton_18, self.lineEdit_3)
        QWidget.setTabOrder(self.lineEdit_3, self.treeView_2)
        QWidget.setTabOrder(self.treeView_2, self.t_main_for_dep_3)
        QWidget.setTabOrder(self.t_main_for_dep_3, self.DO_NOT_USE_27)
        QWidget.setTabOrder(self.DO_NOT_USE_27, self.DO_NOT_USE_30)
        QWidget.setTabOrder(self.DO_NOT_USE_30, self.DO_NOT_USE_33)
        QWidget.setTabOrder(self.DO_NOT_USE_33, self.DO_NOT_USE_37)
        QWidget.setTabOrder(self.DO_NOT_USE_37, self.DO_NOT_USE_39)
        QWidget.setTabOrder(self.DO_NOT_USE_39, self.btn_serv_you_9)
        QWidget.setTabOrder(self.btn_serv_you_9, self.pushButton_23)
        QWidget.setTabOrder(self.pushButton_23, self.lineEdit_4)
        QWidget.setTabOrder(self.lineEdit_4, self.treeView_3)
        QWidget.setTabOrder(self.treeView_3, self.t_main_for_dep_4)
        QWidget.setTabOrder(self.t_main_for_dep_4, self.DO_NOT_USE_40)
        QWidget.setTabOrder(self.DO_NOT_USE_40, self.DO_NOT_USE_43)
        QWidget.setTabOrder(self.DO_NOT_USE_43, self.DO_NOT_USE_46)
        QWidget.setTabOrder(self.DO_NOT_USE_46, self.DO_NOT_USE_50)
        QWidget.setTabOrder(self.DO_NOT_USE_50, self.DO_NOT_USE_52)
        QWidget.setTabOrder(self.DO_NOT_USE_52, self.btn_serv_you_11)
        QWidget.setTabOrder(self.btn_serv_you_11, self.pushButton_25)
        QWidget.setTabOrder(self.pushButton_25, self.lineEdit_6)
        QWidget.setTabOrder(self.lineEdit_6, self.treeView_5)
        QWidget.setTabOrder(self.treeView_5, self.t_main_for_dep_6)
        QWidget.setTabOrder(self.t_main_for_dep_6, self.DO_NOT_USE_118)
        QWidget.setTabOrder(self.DO_NOT_USE_118, self.DO_NOT_USE_121)
        QWidget.setTabOrder(self.DO_NOT_USE_121, self.DO_NOT_USE_124)
        QWidget.setTabOrder(self.DO_NOT_USE_124, self.DO_NOT_USE_128)
        QWidget.setTabOrder(self.DO_NOT_USE_128, self.DO_NOT_USE_130)
        QWidget.setTabOrder(self.DO_NOT_USE_130, self.tabWidget_11)
        QWidget.setTabOrder(self.tabWidget_11, self.btn_serv_you_16)
        QWidget.setTabOrder(self.btn_serv_you_16, self.pushButton_30)
        QWidget.setTabOrder(self.pushButton_30, self.lineEdit_11)
        QWidget.setTabOrder(self.lineEdit_11, self.treeView_9)
        QWidget.setTabOrder(self.treeView_9, self.t_main_for_dep_10)
        QWidget.setTabOrder(self.t_main_for_dep_10, self.DO_NOT_USE_183)
        QWidget.setTabOrder(self.DO_NOT_USE_183, self.DO_NOT_USE_186)
        QWidget.setTabOrder(self.DO_NOT_USE_186, self.DO_NOT_USE_189)
        QWidget.setTabOrder(self.DO_NOT_USE_189, self.DO_NOT_USE_193)
        QWidget.setTabOrder(self.DO_NOT_USE_193, self.DO_NOT_USE_195)
        QWidget.setTabOrder(self.DO_NOT_USE_195, self.btn_serv_you_17)
        QWidget.setTabOrder(self.btn_serv_you_17, self.pushButton_31)
        QWidget.setTabOrder(self.pushButton_31, self.lineEdit_12)
        QWidget.setTabOrder(self.lineEdit_12, self.treeView_10)
        QWidget.setTabOrder(self.treeView_10, self.t_main_for_dep_11)
        QWidget.setTabOrder(self.t_main_for_dep_11, self.DO_NOT_USE_196)
        QWidget.setTabOrder(self.DO_NOT_USE_196, self.DO_NOT_USE_199)
        QWidget.setTabOrder(self.DO_NOT_USE_199, self.DO_NOT_USE_202)
        QWidget.setTabOrder(self.DO_NOT_USE_202, self.DO_NOT_USE_206)
        QWidget.setTabOrder(self.DO_NOT_USE_206, self.DO_NOT_USE_208)
        QWidget.setTabOrder(self.DO_NOT_USE_208, self.btn_serv_you_19)
        QWidget.setTabOrder(self.btn_serv_you_19, self.pushButton_33)
        QWidget.setTabOrder(self.pushButton_33, self.lineEdit_14)
        QWidget.setTabOrder(self.lineEdit_14, self.treeView_12)
        QWidget.setTabOrder(self.treeView_12, self.t_main_for_dep_13)
        QWidget.setTabOrder(self.t_main_for_dep_13, self.DO_NOT_USE_222)
        QWidget.setTabOrder(self.DO_NOT_USE_222, self.DO_NOT_USE_225)
        QWidget.setTabOrder(self.DO_NOT_USE_225, self.DO_NOT_USE_227)
        QWidget.setTabOrder(self.DO_NOT_USE_227, self.DO_NOT_USE_232)
        QWidget.setTabOrder(self.DO_NOT_USE_232, self.DO_NOT_USE_234)
        QWidget.setTabOrder(self.DO_NOT_USE_234, self.tabWidget_9)
        QWidget.setTabOrder(self.tabWidget_9, self.btn_serv_you_12)
        QWidget.setTabOrder(self.btn_serv_you_12, self.pushButton_26)
        QWidget.setTabOrder(self.pushButton_26, self.lineEdit_8)
        QWidget.setTabOrder(self.lineEdit_8, self.treeView_6)
        QWidget.setTabOrder(self.treeView_6, self.t_main_for_dep_7)
        QWidget.setTabOrder(self.t_main_for_dep_7, self.DO_NOT_USE_131)
        QWidget.setTabOrder(self.DO_NOT_USE_131, self.DO_NOT_USE_134)
        QWidget.setTabOrder(self.DO_NOT_USE_134, self.DO_NOT_USE_136)
        QWidget.setTabOrder(self.DO_NOT_USE_136, self.DO_NOT_USE_141)
        QWidget.setTabOrder(self.DO_NOT_USE_141, self.DO_NOT_USE_143)
        QWidget.setTabOrder(self.DO_NOT_USE_143, self.btn_serv_you_14)
        QWidget.setTabOrder(self.btn_serv_you_14, self.pushButton_28)
        QWidget.setTabOrder(self.pushButton_28, self.lineEdit_10)
        QWidget.setTabOrder(self.lineEdit_10, self.treeView_8)
        QWidget.setTabOrder(self.treeView_8, self.t_main_for_dep_9)
        QWidget.setTabOrder(self.t_main_for_dep_9, self.DO_NOT_USE_157)
        QWidget.setTabOrder(self.DO_NOT_USE_157, self.DO_NOT_USE_160)
        QWidget.setTabOrder(self.DO_NOT_USE_160, self.DO_NOT_USE_162)
        QWidget.setTabOrder(self.DO_NOT_USE_162, self.DO_NOT_USE_167)
        QWidget.setTabOrder(self.DO_NOT_USE_167, self.DO_NOT_USE_169)
        QWidget.setTabOrder(self.DO_NOT_USE_169, self.btn_serv_you_13)
        QWidget.setTabOrder(self.btn_serv_you_13, self.pushButton_27)
        QWidget.setTabOrder(self.pushButton_27, self.lineEdit_9)
        QWidget.setTabOrder(self.lineEdit_9, self.treeView_7)
        QWidget.setTabOrder(self.treeView_7, self.t_main_for_dep_8)
        QWidget.setTabOrder(self.t_main_for_dep_8, self.DO_NOT_USE_144)
        QWidget.setTabOrder(self.DO_NOT_USE_144, self.DO_NOT_USE_147)
        QWidget.setTabOrder(self.DO_NOT_USE_147, self.DO_NOT_USE_149)
        QWidget.setTabOrder(self.DO_NOT_USE_149, self.DO_NOT_USE_154)
        QWidget.setTabOrder(self.DO_NOT_USE_154, self.DO_NOT_USE_156)
        QWidget.setTabOrder(self.DO_NOT_USE_156, self.tabWidget_10)
        QWidget.setTabOrder(self.tabWidget_10, self.table_serv__by_year)
        QWidget.setTabOrder(self.table_serv__by_year, self.table_dep_has_worker__by_worker_id__3)
        QWidget.setTabOrder(self.table_dep_has_worker__by_worker_id__3, self.lineEdit_pass)
        QWidget.setTabOrder(self.lineEdit_pass, self.qle_fio_log_pass)
        QWidget.setTabOrder(self.qle_fio_log_pass, self.table_live_min)
        QWidget.setTabOrder(self.table_live_min, self.test_tableView)
        QWidget.setTabOrder(self.test_tableView, self.table_complex_dep_has_dep__by_complex_dep)
        QWidget.setTabOrder(self.table_complex_dep_has_dep__by_complex_dep, self.table_complex_dep)
        QWidget.setTabOrder(self.table_complex_dep, self.table__dep_has_main_6)
        QWidget.setTabOrder(self.table__dep_has_main_6, self.pushButton_29)
        QWidget.setTabOrder(self.pushButton_29, self.btn_serv_you_15)
        QWidget.setTabOrder(self.btn_serv_you_15, self.DO_NOT_USE_170)
        QWidget.setTabOrder(self.DO_NOT_USE_170, self.DO_NOT_USE_173)
        QWidget.setTabOrder(self.DO_NOT_USE_173, self.DO_NOT_USE_176)
        QWidget.setTabOrder(self.DO_NOT_USE_176, self.DO_NOT_USE_180)
        QWidget.setTabOrder(self.DO_NOT_USE_180, self.DO_NOT_USE_182)
        QWidget.setTabOrder(self.DO_NOT_USE_182, self.qle_last_fio)
        QWidget.setTabOrder(self.qle_last_fio, self.qle_contract)
        QWidget.setTabOrder(self.qle_contract, self.cbx_1_servform)
        QWidget.setTabOrder(self.cbx_1_servform, self.qle_serv_total)
        QWidget.setTabOrder(self.qle_serv_total, self.qle_topay)
        QWidget.setTabOrder(self.qle_topay, self.chk_to_recheck)
        QWidget.setTabOrder(self.chk_to_recheck, self.dte_check_date)
        QWidget.setTabOrder(self.dte_check_date, self.qle_contracts2)
        QWidget.setTabOrder(self.qle_contracts2, self.tabMain)
        QWidget.setTabOrder(self.tabMain, self.tabs_add_serv)
        QWidget.setTabOrder(self.tabs_add_serv, self.chk_autosave)
        QWidget.setTabOrder(self.chk_autosave, self.pushButton_3)
        QWidget.setTabOrder(self.pushButton_3, self.pushButton_37)
        QWidget.setTabOrder(self.pushButton_37, self.cbx_1_contracts__by_client_id__2)
        QWidget.setTabOrder(self.cbx_1_contracts__by_client_id__2, self.chk_all_serv_ripso)
        QWidget.setTabOrder(self.chk_all_serv_ripso, self.btn_goto_client_2)
        QWidget.setTabOrder(self.btn_goto_client_2, self.de_contracts)
        QWidget.setTabOrder(self.de_contracts, self.cbx_1_ui_select_fiolist__4)
        QWidget.setTabOrder(self.cbx_1_ui_select_fiolist__4, self.cbx_1__dep_has_client__4)
        QWidget.setTabOrder(self.cbx_1__dep_has_client__4, self.pushButton_4)
        QWidget.setTabOrder(self.pushButton_4, self.tableViewYear)
        QWidget.setTabOrder(self.tableViewYear, self.pushButton_7)
        QWidget.setTabOrder(self.pushButton_7, self.qle_contracts)
        QWidget.setTabOrder(self.qle_contracts, self.table_main__where_client_id)
        QWidget.setTabOrder(self.table_main__where_client_id, self.table__dep_has_main_10)
        QWidget.setTabOrder(self.table__dep_has_main_10, self.pushButton_36)
        QWidget.setTabOrder(self.pushButton_36, self.btn_serv_you_22)
        QWidget.setTabOrder(self.btn_serv_you_22, self.DO_NOT_USE_274)
        QWidget.setTabOrder(self.DO_NOT_USE_274, self.DO_NOT_USE_277)
        QWidget.setTabOrder(self.DO_NOT_USE_277, self.DO_NOT_USE_280)
        QWidget.setTabOrder(self.DO_NOT_USE_280, self.DO_NOT_USE_284)
        QWidget.setTabOrder(self.DO_NOT_USE_284, self.DO_NOT_USE_286)
        QWidget.setTabOrder(self.DO_NOT_USE_286, self.cbx_1_category)
        QWidget.setTabOrder(self.cbx_1_category, self.table__dep_has_main_8)
        QWidget.setTabOrder(self.table__dep_has_main_8, self.pushButton_34)
        QWidget.setTabOrder(self.pushButton_34, self.btn_serv_you_20)
        QWidget.setTabOrder(self.btn_serv_you_20, self.DO_NOT_USE_248)
        QWidget.setTabOrder(self.DO_NOT_USE_248, self.DO_NOT_USE_251)
        QWidget.setTabOrder(self.DO_NOT_USE_251, self.DO_NOT_USE_254)
        QWidget.setTabOrder(self.DO_NOT_USE_254, self.DO_NOT_USE_258)
        QWidget.setTabOrder(self.DO_NOT_USE_258, self.DO_NOT_USE_260)
        QWidget.setTabOrder(self.DO_NOT_USE_260, self.cbx_1_dep_has_worker__2)
        QWidget.setTabOrder(self.cbx_1_dep_has_worker__2, self.table__dep_has_main_9)
        QWidget.setTabOrder(self.table__dep_has_main_9, self.pushButton_35)
        QWidget.setTabOrder(self.pushButton_35, self.btn_serv_you_21)
        QWidget.setTabOrder(self.btn_serv_you_21, self.DO_NOT_USE_261)
        QWidget.setTabOrder(self.DO_NOT_USE_261, self.DO_NOT_USE_264)
        QWidget.setTabOrder(self.DO_NOT_USE_264, self.DO_NOT_USE_267)
        QWidget.setTabOrder(self.DO_NOT_USE_267, self.DO_NOT_USE_271)
        QWidget.setTabOrder(self.DO_NOT_USE_271, self.DO_NOT_USE_273)
        QWidget.setTabOrder(self.DO_NOT_USE_273, self.cbx_1_dep_has_worker__3)
        QWidget.setTabOrder(self.cbx_1_dep_has_worker__3, self.tabs_admin)
        QWidget.setTabOrder(self.tabs_admin, self.pushButton_24)
        QWidget.setTabOrder(self.pushButton_24, self.pushButton_32)
        QWidget.setTabOrder(self.pushButton_32, self.pushButton_16)
        QWidget.setTabOrder(self.pushButton_16, self.journal_table)
        QWidget.setTabOrder(self.journal_table, self.pushButton_13)
        QWidget.setTabOrder(self.pushButton_13, self.qle_month)
        QWidget.setTabOrder(self.qle_month, self.pushButton_14)
        QWidget.setTabOrder(self.pushButton_14, self.qle_sdd)
        QWidget.setTabOrder(self.qle_sdd, self.qle_dock_state)

        self.menubar.addAction(self.menu.menuAction())
        self.menubar.addAction(self.menu_2.menuAction())
        self.menubar.addAction(self.menu_4.menuAction())
        self.menubar.addAction(self.menu_7.menuAction())
        self.menubar.addAction(self.menu_3.menuAction())
        self.menubar.addAction(self.menu_settings.menuAction())
        self.menubar.addAction(self.menu_5.menuAction())
        self.menu.addSeparator()
        self.menu.addAction(self.qa_load_all_models)
        self.menu.addAction(self.action_update_tables)
        self.menu.addAction(self.action_update_tables_on_tab)
        self.menu.addAction(self.action_year)
        self.menu.addAction(self.action_curDep)
        self.menu.addSeparator()
        self.menu.addAction(self.qaDBconnect)
        self.menu.addAction(self.qaDBReconnect)
        self.menu.addAction(self.qaDBDisconnect)
        self.menu.addAction(self.qa_close_app)
        self.menu.addSeparator()
        self.menu.addAction(self.qa_import_XLS)
        self.menu_2.addAction(self.qa_goto_back_tab)
        self.menu_2.addAction(self.qa_goto_forward_tab)
        self.menu_2.addSeparator()
        self.menu_2.addAction(self.qa_tab_add_serv_by_day)
        self.menu_2.addAction(self.qa_tab_people_of_dep)
        self.menu_2.addAction(self.qa_tab__dep_has_client_more)
        self.menu_2.addAction(self.qa_tab_journal)
        self.menu_2.addAction(self.qa_tab_workers)
        self.menu_2.addAction(self.qa_tab_serv_you)
        self.menu_2.addAction(self.qa_tab_dep)
        self.menu_2.addAction(self.action)
        self.menu_2.addAction(self.action_6)
        self.menu_2.addAction(self.action_7)
        self.menu_3.addSeparator()
        self.menu_3.addAction(self.action_9)
        self.menu_3.addSeparator()
        self.menu_3.addAction(self.qa_act)
        self.menu_3.addAction(self.qa_invoice)
        self.menu_3.addAction(self.qa_contract)
        self.menu_3.addAction(self.qa_predv_contract)
        self.menu_3.addAction(self.qa_request)
        self.menu_3.addAction(self.action_14)
        self.menu_3.addAction(self.action_25)
        self.menu_3.addAction(self.qa_menu_pd)
        self.menu_3.addSeparator()
        self.menu_3.addAction(self.action_15)
        self.menu_3.addSeparator()
        self.menu_3.addAction(self.action_16)
        self.menu_3.addAction(self.action_17)
        self.menu_3.addAction(self.action_18)
        self.menu_3.addAction(self.action_19)
        self.menu_3.addAction(self.action_20)
        self.menu_3.addAction(self.action_28)
        self.menu_settings.addAction(self.qa_style)
        self.menu_settings.addAction(self.action_26)
        self.menu_settings.addSeparator()
        self.menu_settings.addAction(self.qaFontSmaller)
        self.menu_settings.addAction(self.qaFontBigger)
        self.menu_settings.addSeparator()
        self.menu_settings.addAction(self.qa_drop_qsettings)
        self.menu_settings.addAction(self.action_2)
        self.menu_settings.addAction(self.action_23)
        self.menu_settings.addAction(self.qa_show_settings)
        self.menu_settings.addAction(self.qa_dock_people_info)
        self.menu_5.addAction(self.action_24)
        self.menu_5.addAction(self.action_27)
        self.menu_5.addAction(self.action_QT)
        self.menu_5.addAction(self.my_test_action)
        self.menu_5.addAction(self.qa_about)
        self.menu_7.addAction(self.action_undo)
        self.menu_7.addAction(self.action_redo)
        self.menu_7.addSeparator()
        self.menu_7.addAction(self.action_save)
        self.menu_7.addAction(self.action_discard)
        self.menu_7.addSeparator()
        self.menu_7.addAction(self.qa_dirty_tab_unblocked)
        self.menu_4.addAction(self.qa_new_people)
        self.menu_4.addAction(self.action_3)
        self.menu_4.addAction(self.action_4)
        self.menu_4.addAction(self.qa_goto_password)
        self.toolBar.addAction(self.action_save)
        self.toolBar.addAction(self.action_discard)
        self.toolBar.addSeparator()
        self.toolBar.addAction(self.action_undo)
        self.toolBar.addAction(self.action_redo)
        self.toolBar.addSeparator()
        self.toolBar.addAction(self.qa_dock_people_info)
        self.toolBar_2.addAction(self.action_year)
        self.toolBar_2.addSeparator()
        self.toolBar_2.addAction(self.action_curDep)
        self.toolBar_2.addSeparator()
        self.toolBar_2.addAction(self.action_connected_user)
        self.toolBar_2.addSeparator()

        self.retranslateUi(MainWindow)
        self.btnClean.clicked.connect(self.lineEdit_pass.clear)
        self.btnClean.clicked.connect(self.lineEdit_login.clear)
        self.btnClean.clicked.connect(self.cbx_1_worker__pass.clear)
        self.btn_upd_fio_list.clicked.connect(self.qa_upd_fio_list.trigger)
        self.btn_qle_date_2.clicked.connect(self.qle_date_2.stepDown)
        self.btn_qle_date_p1_2.clicked.connect(self.qle_date_2.stepUp)
        self.table_complex_dep.selectionChanged1.connect(self.table_complex_dep_has_dep__by_complex_dep.filter_by_selection_of)
        self.table_worker__2.selectionChanged1.connect(self.table_dep_has_worker__by_worker_id__2.filter_by_selection_of)
        self.table_ripso.selectionChanged1.connect(self.table_ripso_has_serv__by_ripso_id.filter_by_selection_of)
        self.table_worker.selectionChanged1.connect(self.table_dep_has_worker__by_worker_id.filter_by_selection_of)
        self.qle_table_client_filter.textChanged.connect(self.table__client_has_invalid_contracts__by_client.set_first_filter_str)
        self.qle_table_client_filter.textChanged.connect(self.table__dep_has_client_by_ripso__by_client.set_first_filter_str)
        self.qle_table_client_filter.textChanged.connect(self.table__client_has_valid_contracts__by_client.set_first_filter_str)
        self.qle_table_client_filter.textChanged.connect(self.table_client__by_client.set_first_filter_str)
        self.qle_fio_filter.textChanged.connect(self.table__dep_has_client__by_client.set_first_filter_str)
        self.qle_fio_filter.textChanged.connect(self.table__dep_has_client_ending__by_client.set_first_filter_str)
        self.qle_fio_filter.textChanged.connect(self.table__dep_has_client_ended__by_client.set_first_filter_str)
        self.qle_fio_filter.textChanged.connect(self.table__dep_has_client_more__by_client.set_first_filter_str)
        self.cbx_1_contracts__by_client_id.editTextChanged.connect(self.table_main__where_client_id__by_contracts_id.set_first_filter_exact)
        self.cbx_1_worker__pass.editTextChanged.connect(self.table_dep_has_worker__by_worker_id__3.set_first_filter_exact)
        self.lineEdit_pass.cursorPositionChanged.connect(self.lineEdit_pass.selectAll)
        self.qle_date.dateChanged.connect(self.table__dep_has_main__where_vdate__by_vdate.set_first_filter_date)
        self.qle_date.dateChanged.connect(self.table__dep_has_main__where_vdate__by_vdate_by_worker_id.set_first_filter_date)
        self.qle_date.dateChanged.connect(self.table__dep_has_main__where_vdate__by_vdate_by_you.set_first_filter_date)
        self.qle_date.dateChanged.connect(self.table__dep_has_main__where_vdate__by_vdate_by_serv_id.set_first_filter_date)
        self.cbx_1__serv_activ__dis_total.currentIndexChanged_model.connect(self.table__dep_has_main__where_vdate__by_vdate_by_serv_id.set_second_filter)
        self.cbx_1_contracts__by_client_id.currentIndexChanged_model.connect(self.table__contracts_has_serv__where_contracts_id__by_contracts_id.set_where)
        self.cbx_1__dep_has_client.currentIndexChanged_model.connect(self.table__client_has_add_info__where_client_id__by_client_id.set_where)
        self.cbx_1__dep_has_client.currentTextChanged.connect(self.table__client_has_add_info__where_client_id__by_client_id.set_first_filter_exact)
        self.cbx_1__dep_has_client.currentIndexChanged.connect(self.table_client_has_category__by_client_id.set_first_filter_exact)
        self.cbx_1__dep_has_client.currentIndexChanged_model.connect(self.table_main__where_client_id__by_dep_id.set_where)
        self.qle_date.dateChanged.connect(self.table__dep_has_main__where_vdate__by_vdate_by_client_id.set_first_filter_date)
        self.cbx_1__dep_has_client__2.currentIndexChanged_model.connect(self.table__dep_has_main__where_vdate__by_vdate_by_client_id.set_second_filter)
        self.btn_prev.clicked.connect(self.cbx_1__dep_has_client.toPrevious)
        self.btn_next.clicked.connect(self.cbx_1__dep_has_client.toNext)
        self.btn_prev_2.clicked.connect(self.cbx_1_contracts__by_client_id.toPrevious)
        self.btn_next_2.clicked.connect(self.cbx_1_contracts__by_client_id.toNext)
        self.clndr__dep_has_main_raw__where_calendar.inwork.connect(self.cbx_1__serv_activ__dis_total__2.disable_events)
        self.clndr__dep_has_main_raw__where_calendar.inwork.connect(self.cbx_1__dep_has_worker__2.disable_events)
        self.clndr__dep_has_main_raw__where_calendar.inwork.connect(self.cbx_1__dep_has_client__3.disable_events)
        self.qleNote2.textChanged.connect(self.clndr__dep_has_main_raw__where_calendar.set_note)
        self.cbx_1__serv_activ__dis_total__2.currentIndexChanged_model.connect(self.clndr__dep_has_main_raw__where_calendar.set_flt_serv_model)
        self.cbx_1__dep_has_worker__2.currentIndexChanged_model.connect(self.clndr__dep_has_main_raw__where_calendar.set_flt_worker_model)
        self.cbx_1__dep_has_client__3.currentIndexChanged_model.connect(self.clndr__dep_has_main_raw__where_calendar.set_flt_client)
        self.pb_start_serv_add.toggled.connect(self.clndr__dep_has_main_raw__where_calendar.set_input_state)
        self.chk_continue_input.stateChanged.connect(self.clndr__dep_has_main_raw__where_calendar.set_continue_input)
        self.qleAmount2.valueChanged.connect(self.clndr__dep_has_main_raw__where_calendar.set_increase)
        self.clndr__dep_has_main_raw__where_calendar.inwork_total.connect(self.lcd_serv_num.display)
        self.buttonBox.accepted.connect(self.clndr__dep_has_main_raw__where_calendar.save_changes)
        self.buttonBox.rejected.connect(self.clndr__dep_has_main_raw__where_calendar.discard_changes)
        self.cbx_1_contracts__by_client_id.editTextChanged.connect(self.table__contracts_has_serv__where_contracts_id__by_contracts_id.set_first_filter_exact)
        self.chk_mouse_left.stateChanged.connect(self.clndr__dep_has_main_raw__where_calendar.set_click_input)
        self.chk_wheel.stateChanged.connect(self.clndr__dep_has_main_raw__where_calendar.set_continue_input)
        self.cbx_1_ui_select_fiolist.currentIndexChanged_model.connect(self.cbx_1__dep_has_client__2.change_model)
        self.cbx_1_ui_select_fiolist__3.currentIndexChanged_model.connect(self.cbx_1__dep_has_client__3.change_model)
        self.cbx_1_ui_select_fiolist__2.currentIndexChanged_model.connect(self.cbx_1__dep_has_client.change_model)
        self.clndr__dep_has_main_raw__where_calendar.clicked.connect(self.table__dep_has_main__where_calendar__by_vdate__2.set_first_filter_date)
        self.chk_enter_input.stateChanged.connect(self.clndr__dep_has_main_raw__where_calendar.set_continue_input)
        self.clndr__dep_has_main_raw__where_calendar.can_start.connect(self.pb_start_serv_add.setChecked)
        self.clndr__dep_has_main_raw__where_calendar.clicked.connect(self.table__dep_has_main__where_calendar__by_vdate_by_client_id__2.set_first_filter_date)
        self.cbx_1__dep_has_client__3.currentIndexChanged_model.connect(self.table__dep_has_main__where_calendar__by_vdate_by_client_id__2.set_second_filter)
        self.clndr__dep_has_main_raw__where_calendar.clicked.connect(self.table__dep_has_main__where_calendar__by_vdate_by_serv_id__2.set_first_filter_date)
        self.cbx_1__serv_activ__dis_total__2.currentIndexChanged_model.connect(self.table__dep_has_main__where_calendar__by_vdate_by_serv_id__2.set_second_filter)
        self.clndr__dep_has_main_raw__where_calendar.clicked.connect(self.table__dep_has_main__where_calendar__by_vdate_by_worker_id__3.set_first_filter_date)
        self.cbx_1__dep_has_worker__2.currentIndexChanged_model.connect(self.table__dep_has_main__where_calendar__by_vdate_by_worker_id__3.set_second_filter)
        self.clndr__dep_has_main_raw__where_calendar.clicked.connect(self.table__dep_has_main__where_calendar__by_vdate_by_client_id_by_serv_id.set_first_filter_date)
        self.cbx_1__dep_has_client__3.currentIndexChanged_model.connect(self.table__dep_has_main__where_calendar__by_vdate_by_client_id_by_serv_id.set_second_filter)
        self.cbx_1__serv_activ__dis_total__2.currentIndexChanged_model.connect(self.table__dep_has_main__where_calendar__by_vdate_by_client_id_by_serv_id.set_third_filter_model)
        self.btn_qle_date_p1.clicked.connect(self.qle_date.plus_day)
        self.btn_qle_date_1.clicked.connect(self.qle_date.minus_day)
        self.qle_fio_filter.textChanged.connect(self.table__dep_has_client_count_main_year__by_client.set_first_filter_str)
        self.cbx_1__dep_has_client.currentIndexChanged.connect(self.cbx_1_contracts__by_client_id.set_first_filter_exact)
        self.clndr__dep_has_main_raw__where_calendar.signal_cur_client_left_serv.connect(self.lcdNumber.display)
        self.qle_fio_filter.textChanged.connect(self.table__dep_has_new_client__by_client_2.set_first_filter_str)
        self.cbx_1_worker__pass.currentTextChanged.connect(self.qle_fio_log_pass.clear)
        self.lineEdit_login.textEdited.connect(self.qle_fio_log_pass.clear)
        self.lineEdit_pass.textEdited.connect(self.qle_fio_log_pass.clear)
        self.cbx_1_contracts__by_client_id.editTextChanged.connect(self.table__client_has_add_info__where_client_id__by_contracts_id.set_first_filter_exact)
        self.btn_upd_fio_list.clicked.connect(self.table__dep_has_client__by_client.select_model_data)
        self.cbx_1__dep_has_client.currentIndexChanged_col_id.connect(self.cbx_1_contracts__by_client_id.add_new_rec_autofill)
        self.cbx_1__dep_has_client.currentIndexChanged_model.connect(self.table__client_has_add_info__where_client_id__by_contracts_id.set_curFIO)
        self.cbx_1_ui_select_fiolist__4.currentIndexChanged_model.connect(self.cbx_1__dep_has_client__4.change_model)
        self.cbx_1__dep_has_client__4.currentIndexChanged.connect(self.cbx_1_contracts__by_client_id__2.set_first_filter_exact)
        self.cbx_1_contracts__by_client_id__2.currentIndexChanged_col_id.connect(self.tableViewYear.set_contract_id)
        self.cbx_1_contracts__by_client_id__2.currentIndexChanged.connect(self.tableViewYear.visibleDataChangedEmit)
        self.cbx_1__dep_has_client.currentIndexChanged_model.connect(self.table_main__where_client_id.set_where)
        self.cbx_1_dep_has_worker__3.editTextChanged.connect(self.report__g_serv_total_dep_with_worker__where_vdate__by_client_id_by_dep_has_worker_id__2.set_second_filter_str)
        self.cbx_1_dep_has_worker__2.editTextChanged.connect(self.report__g_serv_total_dep_with_worker__where_vdate__by_client_id_by_dep_has_worker_id.set_second_filter_str)
        self.cbx_1_dep_has_worker.editTextChanged.connect(self.report__main_for_dep__where_vdate__by_client_id_by_dep_has_worker_id.set_second_filter_str)
        self.cbx_1__dep_has_client__2.currentIndexChanged_id.connect(self.dock_people_info.update_client_id)
        self.qle_date.dateChanged.connect(self.dock_people_info.update_vdate)
        self.cbx_1__dep_has_client__3.currentIndexChanged_id.connect(self.dock_people_info.update_client_id)
        self.clndr__dep_has_main_raw__where_calendar.clicked.connect(self.dock_people_info.update_vdate)
        self.cbx_1__dep_has_client.currentIndexChanged_id.connect(self.dock_people_info.update_client_id)
        self.pushButton_13.clicked.connect(self.dock_people_info.sub_month)
        self.pushButton_14.clicked.connect(self.dock_people_info.add_month)
        self.clndr__dep_has_main_raw__where_calendar.clicked.connect(self.table__dep_has_main__where_calendar__by_vdate__2.update_where)
        self.cbx_1__dep_has_client__4.currentIndexChanged_id.connect(self.dock_people_info.update_client_id)
        self.cbx_1__dep_has_worker.currentIndexChanged_model.connect(self.table__dep_has_main__where_vdate__by_vdate_by_worker_id.set_second_filter_exact)
        self.table_dep.selectionChanged1.connect(self.table_dep_has_ripso__by_dep_id.filter_by_selection_of)
        self.table_dep.selectionChanged1.connect(self.table_dep_has_worker__by_dep_id.filter_by_selection_of)
        self.cbx_4_serv__uniq_year.currentTextChanged.connect(self.table_serv__by_year.set_first_filter_exact)

        self.tabMain.setCurrentIndex(5)
        self.tabs_add_serv.setCurrentIndex(0)
        self.tab__main_for_dep_by.setCurrentIndex(1)
        self.pb_start_serv_add.setDefault(False)
        self.tab_user_has_main.setCurrentIndex(5)
        self.tabs_fio_dep.setCurrentIndex(1)
        self.tabs_client2.setCurrentIndex(0)
        self.tabs_client.setCurrentIndex(2)
        self.tab_sub_client.setCurrentIndex(0)
        self.tabs_total.setCurrentIndex(0)
        self.tabs_tot_serv.setCurrentIndex(0)
        self.DO_NOT_USE_14.setCurrentIndex(0)
        self.DO_NOT_USE_53.setCurrentIndex(0)
        self.DO_NOT_USE_79.setCurrentIndex(0)
        self.DO_NOT_USE_92.setCurrentIndex(0)
        self.DO_NOT_USE_274.setCurrentIndex(0)
        self.DO_NOT_USE_105.setCurrentIndex(0)
        self.tabWidget_8.setCurrentIndex(2)
        self.DO_NOT_USE_27.setCurrentIndex(0)
        self.DO_NOT_USE_40.setCurrentIndex(0)
        self.DO_NOT_USE_248.setCurrentIndex(0)
        self.DO_NOT_USE_118.setCurrentIndex(0)
        self.tabWidget_11.setCurrentIndex(3)
        self.DO_NOT_USE_183.setCurrentIndex(0)
        self.DO_NOT_USE_196.setCurrentIndex(0)
        self.DO_NOT_USE_261.setCurrentIndex(0)
        self.DO_NOT_USE_222.setCurrentIndex(0)
        self.tabWidget_9.setCurrentIndex(2)
        self.DO_NOT_USE_131.setCurrentIndex(0)
        self.DO_NOT_USE_157.setCurrentIndex(0)
        self.DO_NOT_USE_144.setCurrentIndex(0)
        self.tabWidget_10.setCurrentIndex(0)
        self.tabs_admin.setCurrentIndex(0)
        self.DO_NOT_USE_170.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"\u0410\u0418\u0421 \u0422\u0440\u0438\u0423\u0421\u041e\u041d", None))
        self.qaDBconnect.setText(QCoreApplication.translate("MainWindow", u"\u041f\u043e\u0434\u043a\u043b\u044e\u0447\u0438\u0442\u0441\u044f", None))
        self.qaDBDisconnect.setText(QCoreApplication.translate("MainWindow", u"\u041e\u0442\u043a\u043b\u044e\u0447\u0438\u0442\u0441\u044f", None))
        self.qa_close_app.setText(QCoreApplication.translate("MainWindow", u"\u0417\u0430\u043a\u0440\u044b\u0442\u044c \u043f\u0440\u0438\u043b\u043e\u0436\u0435\u043d\u0438\u0435", None))
        self.qa_tab_people_of_dep.setText(QCoreApplication.translate("MainWindow", u"\u0421\u043f\u0438\u0441\u043e\u043a \u043e\u0431\u0441\u043b\u0443\u0436\u0438\u0432\u0430\u0435\u043c\u044b\u0445", None))
        self.qa_tab__dep_has_client_more.setText(QCoreApplication.translate("MainWindow", u"\u0420\u0430\u0441\u0448\u0438\u0440\u0435\u043d\u043d\u044b\u0439 \u0441\u043f\u0438\u0441\u043e\u043a \u0424\u0418\u041e", None))
        self.qa_tab_journal.setText(QCoreApplication.translate("MainWindow", u"\u0416\u0443\u0440\u043d\u0430\u043b \u0440\u0430\u0431\u043e\u0442\u044b", None))
        self.qa_tab_workers.setText(QCoreApplication.translate("MainWindow", u"\u0421\u043f\u0438\u0441\u043e\u043a \u0440\u0430\u0431\u043e\u0442\u043d\u0438\u043a\u043e\u0432", None))
        self.qa_tab_serv_you.setText(QCoreApplication.translate("MainWindow", u"\u0421\u0442\u0430\u0442\u0438\u0441\u0442\u0438\u043a\u0430 (\u0418\u0442\u043e\u0433\u0438)", None))
        self.action_9.setText(QCoreApplication.translate("MainWindow", u"\u0423\u0434\u0430\u043b\u0438\u0442\u044c \u0438 \u0441\u043e\u0437\u0434\u0430\u0442\u044c \u043d\u043e\u0432\u044b\u0439:", None))
        self.qa_act.setText(QCoreApplication.translate("MainWindow", u"\u0410\u043a\u0442", None))
        self.qa_invoice.setText(QCoreApplication.translate("MainWindow", u"\u041a\u0432\u0438\u0442\u0430\u043d\u0446\u0438\u044e", None))
        self.qa_contract.setText(QCoreApplication.translate("MainWindow", u"\u0414\u043e\u0433\u043e\u0432\u043e\u0440", None))
        self.qa_request.setText(QCoreApplication.translate("MainWindow", u"\u0417\u0430\u044f\u0432\u043b\u0435\u043d\u0438\u0435", None))
        self.action_14.setText(QCoreApplication.translate("MainWindow", u"\u0414\u043e\u0433\u043e\u0432\u043e\u0440 \u0441 \u043f\u0440\u0435\u0434\u0441\u0442\u0430\u0432\u0438\u0442\u0435\u043b\u0435\u043c", None))
        self.action_15.setText(QCoreApplication.translate("MainWindow", u"\u041e\u0442\u043a\u0440\u044b\u0442\u044c \u0441\u0443\u0449\u0435\u0441\u0442\u0432\u0443\u044e\u0449\u0438\u0439:", None))
        self.action_16.setText(QCoreApplication.translate("MainWindow", u"\u0410\u043a\u0442", None))
        self.action_17.setText(QCoreApplication.translate("MainWindow", u"\u041a\u0432\u0438\u0442\u0430\u043d\u0446\u0438\u044e", None))
        self.action_18.setText(QCoreApplication.translate("MainWindow", u"\u0414\u043e\u0433\u043e\u0432\u043e\u0440", None))
        self.action_19.setText(QCoreApplication.translate("MainWindow", u"\u0417\u0430\u044f\u0432\u043b\u0435\u043d\u0438\u0435", None))
        self.action_20.setText(QCoreApplication.translate("MainWindow", u"\u0414\u043e\u0433\u043e\u0432\u043e\u0440 \u0441 \u043f\u0440\u0435\u0434\u0441\u0442\u0430\u0432\u0438\u0442\u0435\u043b\u0435\u043c", None))
        self.qa_style.setText(QCoreApplication.translate("MainWindow", u"\u0412\u043d\u0435\u0448\u043d\u0438\u0439 \u0432\u0438\u0434", None))
        self.action_26.setText(QCoreApplication.translate("MainWindow", u"\u041e\u0442\u043a\u0440\u044b\u0442\u044c \u043f\u0430\u043f\u043a\u0443 \u0441 \u0441\u043e\u0445\u0440\u0430\u043d\u0435\u043d\u043d\u044b\u043c\u0438 \u0434\u0430\u043d\u043d\u044b\u043c\u0438", None))
        self.qa_tab_dep.setText(QCoreApplication.translate("MainWindow", u"\u0410\u0434\u043c\u0438\u043d\u0438\u0441\u0442\u0440\u0438\u0440\u043e\u0432\u0430\u043d\u0438\u0435", None))
        self.action_22.setText(QCoreApplication.translate("MainWindow", u"\u0417\u0430\u043a\u0440\u044b\u0442\u044c \u0432\u0441\u0435 \u043e\u043a\u043d\u0430", None))
        self.action_year.setText(QCoreApplication.translate("MainWindow", u"\u0413\u043e\u0434: &2019", None))
#if QT_CONFIG(tooltip)
        self.action_year.setToolTip(QCoreApplication.translate("MainWindow", u"\u0414\u0430\u043d\u043d\u044b\u0435 \u043e\u0442\u043e\u0431\u0440\u0430\u0436\u0430\u044e\u0442\u0441\u044f \u043d\u0430 \u0432\u044b\u0431\u0440\u0430\u043d\u043d\u044b\u0439 \u0433\u043e\u0434, \u0449\u0435\u043b\u043a\u043d\u0438\u0442\u0435 \u0447\u0442\u043e\u0431\u044b \u0441\u043c\u0435\u043d\u0438\u0442\u044c \u0433\u043e\u0434", None))
#endif // QT_CONFIG(tooltip)
        self.action_curDep.setText(QCoreApplication.translate("MainWindow", u"\u041e\u0442\u0434\u0435\u043b\u0435\u043d\u0438\u0435: \u041d\u0435 \u0443\u043a\u0430\u0437\u0430\u043d\u043e", None))
#if QT_CONFIG(tooltip)
        self.action_curDep.setToolTip(QCoreApplication.translate("MainWindow", u"\u0412\u044b \u0440\u0430\u0431\u043e\u0442\u0430\u0435\u0442\u0435 \u0441 \u0434\u0430\u043d\u043d\u044b\u043c\u0438 \u044d\u0442\u043e\u0433\u043e \u043e\u0442\u0434\u0435\u043b\u0435\u043d\u0438\u044f, \u0449\u0435\u043b\u043a\u043d\u0438\u0442\u0435 \u0447\u0442\u043e\u0431\u044b \u0438\u0437\u043c\u0435\u043d\u0438\u0442\u044c", None))
#endif // QT_CONFIG(tooltip)
        self.qa_upd_fio_list.setText(QCoreApplication.translate("MainWindow", u"\u041e\u0431\u043d\u043e\u0432\u0438\u0442\u044c \u0441\u043f\u0438\u0441\u043e\u043a \u043b\u044e\u0434\u0435\u0439", None))
        self.qaFontSmaller.setText(QCoreApplication.translate("MainWindow", u"\u0423\u043c\u0435\u043d\u044c\u0448\u0438\u0442\u044c \u0440\u0430\u0437\u043c\u0435\u0440 \u0442\u0435\u043a\u0441\u0442\u0430", None))
        self.qaFontBigger.setText(QCoreApplication.translate("MainWindow", u"\u0423\u0432\u0435\u043b\u0438\u0447\u0438\u0442\u044c \u0440\u0430\u0437\u043c\u0435\u0440 \u0442\u0435\u043a\u0441\u0442\u0430", None))
        self.qaFontVBig.setText(QCoreApplication.translate("MainWindow", u"\u041e\u0433\u0440\u043e\u043c\u043d\u044b\u0439 \u0440\u0430\u0437\u043c\u0435\u0440 \u0442\u0435\u043a\u0441\u0442\u0430", None))
        self.action_connected_user.setText(QCoreApplication.translate("MainWindow", u"\u041f\u043e\u043b\u044c\u0437\u043e\u0432\u0430\u0442\u0435\u043b\u044c:", None))
#if QT_CONFIG(tooltip)
        self.action_connected_user.setToolTip(QCoreApplication.translate("MainWindow", u"\u0412\u044b \u0440\u0430\u0431\u043e\u0442\u0430\u0435\u0442\u0435 \u043f\u043e\u0434 \u044d\u0442\u043e\u0439 \u0443\u0447\u0435\u0442\u043d\u043e\u0439 \u0437\u0430\u043f\u0438\u0441\u044c\u044e", None))
#endif // QT_CONFIG(tooltip)
        self.qa_drop_qsettings.setText(QCoreApplication.translate("MainWindow", u"\u0423\u0441\u0442\u0430\u043d\u043e\u0432\u0438\u0442\u044c \u0432\u0441\u0435 \u043d\u0430\u0441\u0442\u0440\u043e\u0439\u043a\u0438 \u0432\u043d\u0435\u0448\u043d\u0435\u0433\u043e \u0432\u0438\u0434\u0430 \u043f\u043e \u0443\u043c\u043e\u043b\u0447\u0430\u043d\u0438\u044e", None))
        self.action_QT.setText(QCoreApplication.translate("MainWindow", u"\u0411\u0438\u0431\u043b\u0438\u043e\u0442\u0435\u043a\u0430 &QT", None))
        self.action_save.setText(QCoreApplication.translate("MainWindow", u"\u0421\u043e\u0445\u0440\u0430\u043d\u0438\u0442\u044c \u0438\u0437\u043c\u0435\u043d\u0435\u043d\u0438\u044f", None))
        self.action_discard.setText(QCoreApplication.translate("MainWindow", u"\u041e\u0442\u043c\u0435\u043d\u0438\u0442\u044c \u0438\u0437\u043c\u0435\u043d\u0435\u043d\u0438\u044f", None))
        self.action_undo.setText(QCoreApplication.translate("MainWindow", u"\u041e\u0442\u043c\u0435\u043d\u0430", None))
#if QT_CONFIG(shortcut)
        self.action_undo.setShortcut(QCoreApplication.translate("MainWindow", u"Ctrl+Z", None))
#endif // QT_CONFIG(shortcut)
        self.action_redo.setText(QCoreApplication.translate("MainWindow", u"\u041f\u043e\u0432\u0442\u043e\u0440", None))
#if QT_CONFIG(shortcut)
        self.action_redo.setShortcut(QCoreApplication.translate("MainWindow", u"Ctrl+Shift+Z", None))
#endif // QT_CONFIG(shortcut)
        self.action_2.setText(QCoreApplication.translate("MainWindow", u"\u0417\u0430\u0433\u0440\u0443\u0436\u0430\u0442\u044c \u0432\u0441\u0435 \u0442\u0430\u0431\u043b\u0438\u0446\u044b \u043f\u0440\u0438 \u0441\u0442\u0430\u0440\u0442\u0435 \u043f\u0440\u043e\u0433\u0440\u0430\u043c\u043c\u044b", None))
        self.action_23.setText(QCoreApplication.translate("MainWindow", u"\u041f\u043e\u043a\u0430\u0437\u044b\u0432\u0430\u0442\u044c \u0441\u0442\u043e\u043b\u0431\u0446\u044b \u043d\u0435 \u0434\u043e\u0441\u0442\u0443\u043f\u043d\u044b\u0435 \u0434\u043b\u044f \u0440\u0435\u0434\u0430\u043a\u0442\u0438\u0440\u043e\u0432\u0430\u043d\u0438\u044f", None))
        self.action_update_tables.setText(QCoreApplication.translate("MainWindow", u"\u041e\u0431\u043d\u043e\u0432\u0438\u0442\u044c \u0432\u0441\u0435 \u0442\u0430\u0431\u043b\u0438\u0446\u044b", None))
        self.action_24.setText(QCoreApplication.translate("MainWindow", u"\u0420\u0443\u043a\u043e\u0432\u043e\u0434\u0441\u0442\u0432\u043e \u043f\u043e\u043b\u044c\u0437\u043e\u0432\u0430\u0442\u0435\u043b\u044f", None))
        self.action_27.setText(QCoreApplication.translate("MainWindow", u"\u0420\u0443\u043a\u043e\u0432\u043e\u0434\u0441\u0442\u0432\u043e \u0430\u0434\u043c\u0438\u043d\u0438\u0441\u0442\u0440\u0430\u0442\u043e\u0440\u0430", None))
        self.action_25.setText(QCoreApplication.translate("MainWindow", u"\u041e\u0442\u0447\u0435\u0442 \u043e\u0442\u0434\u0435\u043b\u0435\u043d\u0438\u044f", None))
        self.action_28.setText(QCoreApplication.translate("MainWindow", u"\u041e\u0442\u0447\u0435\u0442 \u043e\u0442\u0434\u0435\u043b\u0435\u043d\u0438\u044f", None))
        self.action_update_tables_on_tab.setText(QCoreApplication.translate("MainWindow", u"\u041e\u0431\u043d\u043e\u0432\u0438\u0442\u044c \u0430\u043a\u0442\u0438\u0432\u043d\u0443\u044e \u0432\u043a\u043b\u0430\u0434\u043a\u0443", None))
        self.qa_new_people.setText(QCoreApplication.translate("MainWindow", u"\u041b\u0438\u0447\u043d\u043e\u0435 \u0434\u0435\u043b\u043e \u0447\u0435\u043b\u043e\u0432\u0435\u043a\u0430", None))
        self.action_3.setText(QCoreApplication.translate("MainWindow", u"\u0414\u043e\u0433\u043e\u0432\u043e\u0440 \u0434\u043b\u044f...", None))
        self.action_4.setText(QCoreApplication.translate("MainWindow", u"\u0423\u0441\u043b\u0443\u0433\u0443", None))
        self.qa_goto_password.setText(QCoreApplication.translate("MainWindow", u"\u041b\u043e\u0433\u0438\u043d \u0438 \u043f\u0430\u0440\u043e\u043b\u044c \u0434\u043b\u044f \u0440\u0430\u0431\u043e\u0442\u043d\u0438\u043a\u0430", None))
        self.qaDBReconnect.setText(QCoreApplication.translate("MainWindow", u"\u041f\u0435\u0440\u0435\u043f\u043e\u0434\u043a\u043b\u044e\u0447\u0438\u0442\u0441\u044f", None))
        self.my_test_action.setText(QCoreApplication.translate("MainWindow", u"\u041d\u0415 \u041d\u0410\u0416\u0418\u041c\u0410\u0422\u042c!", None))
        self.qa_load_all_models.setText(QCoreApplication.translate("MainWindow", u"\u0417\u0430\u0433\u0440\u0443\u0437\u0438\u0442\u044c \u0432\u0441\u0435 \u0442\u0430\u0431\u043b\u0438\u0446\u044b", None))
        self.qa_show_settings.setText(QCoreApplication.translate("MainWindow", u"\u041f\u043e\u043a\u0430\u0437\u0430\u0442\u044c \u043d\u0430\u0441\u0442\u0440\u043e\u0439\u043a\u0438", None))
        self.qa_menu_pd.setText(QCoreApplication.translate("MainWindow", u"\u0421\u043e\u0433\u043b\u0430\u0441\u0438\u0435 \u043d\u0430 \u043e\u0431\u0440\u0430\u0431\u043e\u0442\u043a\u0443 \u041f\u0414", None))
        self.qa_about.setText(QCoreApplication.translate("MainWindow", u"\u041e \u043f\u0440\u043e\u0433\u0440\u0430\u043c\u043c\u0435 \u0410\u0418\u0421 \u0422\u0440\u0438\u0423\u0421\u041e\u041d", None))
        self.qa_tab_add_serv_by_day.setText(QCoreApplication.translate("MainWindow", u"\u0412\u0432\u043e\u0434 \u0443\u0441\u043b\u0443\u0433", None))
        self.qa_goto_back_tab.setText(QCoreApplication.translate("MainWindow", u"\u041d\u0430\u0437\u0430\u0434(\u043f\u0440\u0435\u0434\u044b\u0434\u0443\u0449\u0430\u044f \u0432\u043a\u043b\u0430\u0434\u043a\u0430)", None))
        self.qa_predv_contract.setText(QCoreApplication.translate("MainWindow", u"\u041f\u0440\u0435\u0434\u0432\u0430\u0440\u0438\u0442\u0435\u043b\u044c\u043d\u044b\u0439 \u0440\u0430\u0441\u0447\u0435\u0442 \u043e\u043f\u043b\u0430\u0442\u044b", None))
        self.action.setText(QCoreApplication.translate("MainWindow", u"\u0418\u0442\u043e\u0433\u0438 \u043f\u043e \u0447\u0435\u043b\u043e\u0432\u0435\u043a\u0443", None))
        self.action_6.setText(QCoreApplication.translate("MainWindow", u"\u0420\u0435\u0434\u0430\u043a\u0442\u0438\u0440\u043e\u0432\u0430\u0442\u044c \u043b\u044e\u0434\u0435\u0439 \u0441\u043f\u0438\u0441\u043a\u043e\u043c", None))
        self.action_7.setText(QCoreApplication.translate("MainWindow", u"\u0420\u0435\u0434\u0430\u043a\u0442\u0438\u0440\u043e\u0432\u0430\u0442\u044c \u0434\u043e\u0433\u043e\u0432\u043e\u0440\u0430 \u0441\u043f\u0438\u0441\u043a\u043e\u043c", None))
        self.qa_dock_people_info.setText(QCoreApplication.translate("MainWindow", u"\u041f\u043e\u043a\u0430\u0437\u0430\u0442\u044c \u043f\u0430\u043d\u0435\u043b\u044c &\u0438\u0442\u043e\u0433\u043e\u0432 \u043f\u043e \u0447\u0435\u043b\u043e\u0432\u0435\u043a\u0443", None))
        self.qa_goto_forward_tab.setText(QCoreApplication.translate("MainWindow", u"\u0412\u043f\u0435\u0440\u0435\u0434(\u0441\u043b\u0435\u0434\u0443\u044e\u0449\u0430\u044f \u0432\u043a\u043b\u0430\u0434\u043a\u0430)", None))
        self.qa_dirty_tab_unblocked.setText(QCoreApplication.translate("MainWindow", u"\u0420\u0430\u0437\u0440\u0435\u0448\u0438\u0442\u044c \u043f\u0435\u0440\u0435\u0445\u043e\u0434 \u0441 \u043d\u0435\u0441\u043e\u0445\u0440\u0430\u043d\u0435\u043d\u043d\u044b\u0445 \u0432\u043a\u043b\u0430\u0434\u043e\u043a", None))
        self.qa_import_XLS.setText(QCoreApplication.translate("MainWindow", u"\u0418\u043c\u043f\u043e\u0440\u0442 \u043e\u0442\u0434\u0435\u043b\u0435\u043d\u0438\u044f \u0438\u0437 XLS \u0444\u0430\u0439\u043b\u0430", None))
        self.btn_goto_worker.setText(QCoreApplication.translate("MainWindow", u"...", None))
        self.btn_qle_date_1.setText(QCoreApplication.translate("MainWindow", u"\u043c\u0438\u043d\u0443\u0441 \u0434\u0435\u043d\u044c", None))
        self.btn_qle_date_p1.setText(QCoreApplication.translate("MainWindow", u"\u043f\u043b\u044e\u0441 \u0434\u0435\u043d\u044c", None))
#if QT_CONFIG(tooltip)
        self.chkLAmount.setToolTip(QCoreApplication.translate("MainWindow", u"\u0417\u0430\u043f\u043e\u043c\u043d\u0438\u0442\u044c \u043a\u043e\u043b\u0438\u0447\u0435\u0441\u0442\u0432\u043e \u0443\u0441\u043b\u0443\u0433", None))
#endif // QT_CONFIG(tooltip)
        self.chkLAmount.setText(QCoreApplication.translate("MainWindow", u"\u0417\u0430\u043f\u043e\u043c\u043d\u0438\u0442\u044c", None))
#if QT_CONFIG(tooltip)
        self.cbx_1_ui_select_fiolist.setToolTip(QCoreApplication.translate("MainWindow", u"\u0421\u043f\u0438\u0441\u043a\u0438 \u043b\u044e\u0434\u0435\u0439", None))
#endif // QT_CONFIG(tooltip)
        self.cbx_1_ui_select_fiolist.setCurrentText("")
#if QT_CONFIG(tooltip)
        self.chkLFio.setToolTip(QCoreApplication.translate("MainWindow", u"\u0417\u0430\u043f\u043e\u043c\u043d\u0438\u0442\u044c \u0432\u044b\u0431\u0440\u0430\u043d\u043d\u043e \u0447\u0435\u043b\u043e\u0432\u0435\u043a\u0430", None))
#endif // QT_CONFIG(tooltip)
        self.chkLFio.setText(QCoreApplication.translate("MainWindow", u"\u0417\u0430\u043f\u043e\u043c\u043d\u0438\u0442\u044c", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"\u0412\u0432\u043e\u0434\u0438\u0442\u044c \u0442\u043e\u043b\u044c\u043a\u043e:", None))
#if QT_CONFIG(tooltip)
        self.chkLServ.setToolTip(QCoreApplication.translate("MainWindow", u"\u0417\u0430\u043f\u043e\u043c\u043d\u0438\u0442\u044c \u0432\u044b\u0431\u0440\u0430\u043d\u043d\u0443\u044e \u0443\u0441\u043b\u0443\u0433\u0443", None))
#endif // QT_CONFIG(tooltip)
        self.chkLServ.setText(QCoreApplication.translate("MainWindow", u"\u0417\u0430\u043f\u043e\u043c\u043d\u0438\u0442\u044c", None))
        self.label_34.setText(QCoreApplication.translate("MainWindow", u"\u041a\u043e\u043b\u0438\u0447\u0435\u0441\u0442\u0432\u043e \u0443\u0441\u043b\u0443\u0433: Alt+A", None))
#if QT_CONFIG(tooltip)
        self.cbx_1__serv_activ__dis_total.setToolTip(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>\u0411\u0443\u0434\u0435\u0442 \u0432\u0432\u0435\u0434\u0435\u043d\u0430 \u0443\u0441\u043b\u0443\u0433\u0430, \u0430 \u0437\u0430\u0442\u0435\u043c \u0444\u043e\u043a\u0443\u0441 \u0432\u0432\u043e\u0434\u0430 \u0432\u0435\u0440\u043d\u0435\u0442\u0441\u044f \u043a \u0432\u044b\u0431\u043e\u0440\u0443 \u043a\u043e\u043b\u0438\u0447\u0435\u0441\u0442\u0432\u0430 \u0443\u0441\u043b\u0443\u0433</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(tooltip)
        self.qleNote.setToolTip(QCoreApplication.translate("MainWindow", u"\u0417\u0434\u0435\u0441\u044c \u043c\u043e\u0436\u043d\u043e \u0434\u043e\u0431\u0430\u0432\u0438\u0442\u044c \u043f\u0440\u0438\u043c\u0435\u0447\u0430\u043d\u0438\u0435 \u043a \u0443\u0441\u043b\u0443\u0433\u0435", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(tooltip)
        self.btn_serv_bydayQ.setToolTip(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>\u0411\u0443\u0434\u0435\u0442 \u0432\u0432\u0435\u0434\u0435\u043d\u0430 \u0443\u0441\u043b\u0443\u0433\u0430, \u0430 \u0437\u0430\u0442\u0435\u043c \u0444\u043e\u043a\u0443\u0441 \u0432\u0432\u043e\u0434\u0430 \u0432\u0435\u0440\u043d\u0435\u0442\u0441\u044f \u043a \u0432\u044b\u0431\u043e\u0440\u0443 \u043f\u043e\u043b\u0443\u0447\u0430\u0442\u0435\u043b\u044f \u0421\u0423</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.btn_serv_bydayQ.setText(QCoreApplication.translate("MainWindow", u"\u0412\u0432\u0435\u0441\u0442\u0438 Alt+Q", None))
#if QT_CONFIG(tooltip)
        self.btn_serv_bydayW.setToolTip(QCoreApplication.translate("MainWindow", u"\u0411\u0443\u0434\u0435\u0442 \u0432\u0432\u0435\u0434\u0435\u043d\u0430 \u0443\u0441\u043b\u0443\u0433\u0430, \u0430 \u0437\u0430\u0442\u0435\u043c \u0444\u043e\u043a\u0443\u0441 \u0432\u0432\u043e\u0434\u0430 \u0432\u0435\u0440\u043d\u0435\u0442\u0441\u044f \u043a \u0432\u044b\u0431\u043e\u0440\u0443 \u0440\u0430\u0431\u043e\u0442\u043d\u0438\u043a\u0430", None))
#endif // QT_CONFIG(tooltip)
        self.btn_serv_bydayW.setText(QCoreApplication.translate("MainWindow", u"\u0412\u0432\u0435\u0441\u0442\u0438 Alt+W", None))
#if QT_CONFIG(tooltip)
        self.btn_serv_bydayE.setToolTip(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>\u0411\u0443\u0434\u0435\u0442 \u0432\u0432\u0435\u0434\u0435\u043d\u0430 \u0443\u0441\u043b\u0443\u0433\u0430, \u0430 \u0437\u0430\u0442\u0435\u043c \u0444\u043e\u043a\u0443\u0441 \u0432\u0432\u043e\u0434\u0430 \u0432\u0435\u0440\u043d\u0435\u0442\u0441\u044f \u043a \u0432\u044b\u0431\u043e\u0440\u0443 \u0443\u0441\u043b\u0443\u0433\u0438</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.btn_serv_bydayE.setText(QCoreApplication.translate("MainWindow", u"\u0412\u0432\u0435\u0441\u0442\u0438 Alt+E", None))
#if QT_CONFIG(tooltip)
        self.btn_serv_bydayA.setToolTip(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>\u0411\u0443\u0434\u0435\u0442 \u0432\u0432\u0435\u0434\u0435\u043d\u0430 \u0443\u0441\u043b\u0443\u0433\u0430, \u0430 \u0437\u0430\u0442\u0435\u043c \u0444\u043e\u043a\u0443\u0441 \u0432\u0432\u043e\u0434\u0430 \u0432\u0435\u0440\u043d\u0435\u0442\u0441\u044f \u043a \u0432\u044b\u0431\u043e\u0440\u0443 \u043a\u043e\u043b\u0438\u0447\u0435\u0441\u0442\u0432\u0430 \u0443\u0441\u043b\u0443\u0433</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.btn_serv_bydayA.setText(QCoreApplication.translate("MainWindow", u"\u0412\u0432\u0435\u0441\u0442\u0438 Alt+A", None))
        self.label_36.setText(QCoreApplication.translate("MainWindow", u"\u0412\u0432\u0435\u0441\u0442\u0438 \u0443\u0441\u043b\u0443\u0433\u0443 \u0438 \u043f\u0435\u0440\u0435\u0439\u0442\u0438 \u043a:", None))
        self.label_53.setText(QCoreApplication.translate("MainWindow", u"\u043e\u0441\u0442\u0430\u043b\u043e\u0441\u044c:", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"\u0423\u0441\u043b\u0443\u0433\u0430: Alt+E", None))
#if QT_CONFIG(tooltip)
        self.chkLW.setToolTip(QCoreApplication.translate("MainWindow", u"\u0417\u0430\u043f\u043e\u043c\u043d\u0438\u0442\u044c \u0432\u044b\u0431\u0440\u0430\u043d\u043d\u043e \u0440\u0430\u0431\u043e\u0442\u043d\u0438\u043a\u0430", None))
#endif // QT_CONFIG(tooltip)
        self.chkLW.setText(QCoreApplication.translate("MainWindow", u"\u0417\u0430\u043f\u043e\u043c\u043d\u0438\u0442\u044c", None))
        self.label_32.setText(QCoreApplication.translate("MainWindow", u"\u0414\u0430\u0442\u0430:", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"\u0424\u0418\u041e \u043e\u0431\u0441\u043b\u0443\u0436\u0438\u0432\u0430\u0435\u043c\u043e\u0433\u043e: Alt+Q", None))
        self.label_33.setText(QCoreApplication.translate("MainWindow", u"\u041f\u0440\u0438\u043c\u0435\u0447\u0430\u043d\u0438\u0435", None))
        self.label_35.setText(QCoreApplication.translate("MainWindow", u"\u0420\u0430\u0431\u043e\u0442\u043d\u0438\u043a: Alt+W", None))
        self.btn_goto_client.setText(QCoreApplication.translate("MainWindow", u"...", None))
        self.chk_autosave.setText(QCoreApplication.translate("MainWindow", u"\u0421\u0440\u0430\u0437\u0443 \u0441\u043e\u0445\u0440\u0430\u043d\u044f\u0442\u044c", None))
        self.tab__main_for_dep_by.setTabText(self.tab__main_for_dep_by.indexOf(self.tab_all_by_day), QCoreApplication.translate("MainWindow", u"\u0412\u0441\u0435 \u0443\u0441\u043b\u0443\u0433\u0438 \u043e\u0442\u0434\u0435\u043b\u0430 \u0432 \u044d\u0442\u043e\u0442 \u0434\u0435\u043d\u044c", None))
        self.tab__main_for_dep_by.setTabText(self.tab__main_for_dep_by.indexOf(self.tab_24), QCoreApplication.translate("MainWindow", u"... \u043d\u0430 \u0432\u044b\u0431\u0440\u0430\u043d\u043d\u043e\u0433\u043e \u0440\u0430\u0431\u043e\u0442\u043d\u0438\u043a\u0430", None))
        self.tab__main_for_dep_by.setTabText(self.tab__main_for_dep_by.indexOf(self.tab_7), QCoreApplication.translate("MainWindow", u"... \u043d\u0430 \u0432\u044b\u0431\u0440\u0430\u043d\u043d\u043e\u0433\u043e \u0447\u0435\u043b\u043e\u0432\u0435\u043a\u0430", None))
        self.tab__main_for_dep_by.setTabText(self.tab__main_for_dep_by.indexOf(self.tab_23), QCoreApplication.translate("MainWindow", u"... \u0432\u0432\u0435\u0434\u0435\u043d\u044b \u0432\u0430\u043c\u0438", None))
        self.tab__main_for_dep_by.setTabText(self.tab__main_for_dep_by.indexOf(self.tab_25), QCoreApplication.translate("MainWindow", u".. \u0432\u044b\u0431\u0440\u0430\u043d\u043d\u0430\u044f \u0443\u0441\u043b\u0443\u0433\u0430", None))
        self.tabs_add_serv.setTabText(self.tabs_add_serv.indexOf(self.tab_add_serv_by_day), QCoreApplication.translate("MainWindow", u"\u041f\u043e \u0434\u043d\u044f\u043c", None))
        self.label_43.setText(QCoreApplication.translate("MainWindow", u"\u0420\u0430\u0431\u043e\u0442\u043d\u0438\u043a:", None))
        self.label_37.setText(QCoreApplication.translate("MainWindow", u"\u041a\u043e\u043b\u0438\u0447\u0435\u0441\u0442\u0432\u043e \u0443\u0441\u043b\u0443\u0433:", None))
        self.lbl_input_serv.setText(QCoreApplication.translate("MainWindow", u"\u0411\u0443\u0434\u0435\u0442 \u0432\u0432\u0435\u0434\u0435\u043d\u043e:", None))
        self.chk_mouse_left.setText(QCoreApplication.translate("MainWindow", u"\u0412\u0432\u043e\u0434 \u043d\u0430\u0436\u0430\u0442\u0438\u0435\u043c \u041b\u041a\u041c", None))
        self.chk_continue_input.setText(QCoreApplication.translate("MainWindow", u"\u0412\u0432\u043e\u0434 \u043f\u0440\u043e\u0442\u044f\u0433\u0438\u0432\u0430\u043d\u0438\u0435\u043c", None))
        self.pb_start_serv_add.setText(QCoreApplication.translate("MainWindow", u"\u041d\u0410\u0427\u0410\u0422\u042c \u0412\u0412\u041e\u0414 \u0423\u0421\u041b\u0423\u0413", None))
        self.chk_wheel.setText(QCoreApplication.translate("MainWindow", u"\u0412\u0432\u043e\u0434 \u043a\u043e\u043b\u0435\u0441\u0438\u043a\u043e\u043c \u043c\u044b\u0448\u0438", None))
        self.label_66.setText(QCoreApplication.translate("MainWindow", u"\u041e\u0441\u0442\u0430\u043b\u043e\u0441\u044c:", None))
        self.chk_enter_input.setText(QCoreApplication.translate("MainWindow", u"\u0412\u0432\u043e\u0434 \u043a\u043b\u0430\u0432\u0438\u0448\u0430\u043c\u0438 Enter/+/-", None))
        self.clndr__dep_has_main_raw__where_calendar.setProperty("my_test", QCoreApplication.translate("MainWindow", u"123456789", None))
        self.label_40.setText(QCoreApplication.translate("MainWindow", u"\u0424\u0418\u041e \u043e\u0431\u0441\u043b\u0443\u0436\u0438\u0432\u0430\u0435\u043c\u043e\u0433\u043e:", None))
        self.label_70.setText(QCoreApplication.translate("MainWindow", u"\u0412\u0432\u043e\u0434\u0438\u0442\u044c \u0442\u043e\u043b\u044c\u043a\u043e:", None))
        self.label_67.setText(QCoreApplication.translate("MainWindow", u"\u041f\u0440\u0438\u043c.:", None))
        self.label_41.setText(QCoreApplication.translate("MainWindow", u"\u0423\u0441\u043b\u0443\u0433\u0430:", None))
        self.tab_user_has_main.setTabText(self.tab_user_has_main.indexOf(self.tab_28), QCoreApplication.translate("MainWindow", u"\u0412\u0441\u0435 \u0443\u0441\u043b\u0443\u0433\u0438 \u0432\u0432\u0435\u0434\u0435\u043d\u043d\u044b\u0435 \u0432\u0430\u043c\u0438 \u0441\u0435\u0433\u043e\u0434\u043d\u044f:", None))
        self.tab_user_has_main.setTabText(self.tab_user_has_main.indexOf(self.tab_29), QCoreApplication.translate("MainWindow", u"\u041f\u043e\u0441\u043b\u0435\u0434\u043d\u0438\u0435 30 \u0432\u0432\u0435\u0434\u0435\u043d\u043d\u044b\u0445 \u0443\u0441\u043b\u0443\u0433", None))
        self.tab_user_has_main.setTabText(self.tab_user_has_main.indexOf(self.tab_am_serv_in_day), QCoreApplication.translate("MainWindow", u"\u0423\u0441\u043b\u0443\u0433\u0438 \u0432 \u0432\u044b\u0431\u0440\u0430\u043d\u043d\u044b\u0439 \u0434\u0435\u043d\u044c", None))
        self.label_serv_in.setText(QCoreApplication.translate("MainWindow", u"\u0423\u0441\u043b\u0443\u0433 \u0432 :", None))
        self.tab_user_has_main.setTabText(self.tab_user_has_main.indexOf(self.tab_17), QCoreApplication.translate("MainWindow", u"... \u043f\u043e \u0447\u0435\u043b\u043e\u0432\u0435\u043a\u0443", None))
        self.tab_user_has_main.setTabText(self.tab_user_has_main.indexOf(self.tab_18), QCoreApplication.translate("MainWindow", u"... \u043f\u043e \u0443\u0441\u043b\u0443\u0433\u0435", None))
        self.tab_user_has_main.setTabText(self.tab_user_has_main.indexOf(self.tab_21), QCoreApplication.translate("MainWindow", u"... \u043f\u043e \u0440\u0430\u0431\u043e\u0442\u043d\u0438\u043a\u0443", None))
        self.tab_user_has_main.setTabText(self.tab_user_has_main.indexOf(self.tab_27), QCoreApplication.translate("MainWindow", u"... \u043f\u043e \u0447\u0435\u043b\u043e\u0432\u0435\u043a\u0443 \u0438 \u0443\u0441\u043b\u0443\u0433\u0435", None))
        self.textEdit_2.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'MS Shell Dlg 2'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">                          </p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">                           </p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">                           </p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">                           </p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-"
                        "left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">                           </p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">                           </p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">                           </p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">                           </p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">                           </p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">                           </p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">                "
                        "           </p>\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Noto Sans'; font-size:11pt; font-weight:600;\">\u0412\u043a\u043b\u0430\u0434\u043a\u0430: \u0412\u0432\u043e\u0434                          \u0443\u0441\u043b\u0443\u0433 \u041d\u0430 \u0432\u0435\u0441\u044c \u043c\u0435\u0441\u044f\u0446</span>                           </p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">\u0414\u0430\u043d\u043d\u0430\u044f \u0432\u043a\u043b\u0430\u0434\u043a\u0430 <span style=\" font-family:'Noto Sans'; font-size:11pt;\">\u043f\u043e\u0437\u0432\u043e\u043b\u044f\u0435\u0442 \u0431\u044b\u0441\u0442\u0440\u043e \u0432\u0432\u043e\u0434\u0438\u0442\u044c \u0443\u0441\u043b\u0443\u0433\u0438 \u043d\u0430 \u043c\u0435\u0441\u044f\u0446 \u0441                          \u043f\u043e\u043c\u043e\u0449\u044c\u044e \u043c"
                        "\u044b\u0448\u0438.</span>                           </p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">                           </p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">\u0414\u043e\u0441\u0442\u0443\u043f\u043d\u044b \u0442\u0440\u0438 \u0441\u043f\u043e\u0441\u043e\u0431\u0430 \u0432\u0432\u043e\u0434\u0430 \u0443\u0441\u043b\u0443\u0433:<span style=\" font-family:'Noto Sans'; font-size:11pt;\"> \u0449\u0435\u043b\u0447\u043a\u043e\u043c \u041b\u041a\u041c (\u043b\u0435\u0432\u043e\u0439 \u043a\u043d\u043e\u043f\u043a\u0438 \u043c\u044b\u0448\u0438) \u043f\u043e \u0434\u0430\u0442\u0435,                          \u043f\u0440\u043e\u0442\u044f\u0433\u0438\u0432\u0430\u043d\u0438\u0435\u043c \u043d\u0430\u0436\u0430\u0442\u043e\u0439 \u043c\u044b\u0448\u0438 \u043f\u043e \u043d\u0443\u0436\u043d\u044b\u043c \u0434\u0430\u0442\u0430\u043c, \u0438"
                        " \u0441 \u043f\u043e\u043c\u043e\u0449\u044c\u044e \u043a\u043e\u043b\u0435\u0441\u0438\u043a\u0430 \u043c\u044b\u0448\u0438. </span>                           </p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">                           </p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">\u0412\u044b\u0431\u0435\u0440\u0438\u0442\u0435 \u0424\u0418\u041e \u043f\u043e\u043b\u0443\u0447\u0430\u0442\u0435\u043b\u044f \u0421\u0423, \u0440\u0430\u0431\u043e\u0442\u043d\u0438\u043a\u0430, \u0443\u0441\u043b\u0443\u0433\u0443 \u0438                          \u043a\u043e\u043b\u043b\u0438\u0447\u0435\u0441\u0442\u0432\u043e \u0443\u0441\u043b\u0443\u0433 \u043a\u043e\u0442\u043e\u0440\u044b\u0435 \u0431\u0443\u0434\u0443\u0442 \u0432\u0432\u0435\u0434\u0435\u043d\u044b \u0437\u0430 \u043e\u0434\u043d\u043e \u043d\u0430\u0436\u0430\u0442\u0438\u0435/\u043f\u0440\u043e"
                        "\u0442\u044f\u0433\u0438\u0432\u0430\u043d\u0438\u0435. \u041a\u043e\u043b\u0435\u0441\u0438\u043a\u043e \u043c\u044b\u0448\u0438 \u0432\u0441\u0435\u0433\u0434\u0430                          \u043f\u0440\u0438\u0431\u0430\u0432\u043b\u044f\u0435\u0442/\u043e\u0442\u043d\u0438\u043c\u0430\u0435\u0442 \u043f\u043e 1 \u0443\u0441\u043b\u0443\u0433\u0435.                           </p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">                           </p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">\u041d\u0415 \u0417\u0410\u0411\u0423\u0414\u042c\u0422\u0415 \u0421\u041e\u0425\u0420\u0410\u041d\u0418\u0422\u042c \u0423\u0421\u041b\u0423\u0413\u0418!                           </p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Noto Sans'; font-s"
                        "ize:11pt;\"> </span>                          </p></body></html>", None))
        self.tab_user_has_main.setTabText(self.tab_user_has_main.indexOf(self.tab_8), QCoreApplication.translate("MainWindow", u"\u0421\u043f\u0440\u0430\u0432\u043a\u0430", None))
        self.tabs_add_serv.setTabText(self.tabs_add_serv.indexOf(self.tab_add_serv_by_month), QCoreApplication.translate("MainWindow", u"\u041d\u0430 \u0432\u0435\u0441\u044c \u043c\u0435\u0441\u044f\u0446", None))
        self.groupBox_5.setTitle(QCoreApplication.translate("MainWindow", u"1) \u0412\u044b\u0431\u0438\u0440\u0438\u0442\u0435 \u0438\u043b\u0438 \u0441\u043e\u0437\u0434\u0430\u0439\u0442\u0435 \u0433\u0440\u0443\u043f\u043f\u0443 \u043b\u044e\u0434\u0435\u0439", None))
        self.pushButton_10.setText(QCoreApplication.translate("MainWindow", u"\u0441\u043e\u0437\u0434\u0430\u0442\u044c \u043a\u043e\u043f\u0438\u044e \u0433\u0440\u0443\u043f\u043f\u044b", None))
        self.label_8.setText(QCoreApplication.translate("MainWindow", u"\u0413\u0440\u0443\u043f\u043f\u044b \u043b\u044e\u0434\u0435\u0439:", None))
        self.label_47.setText(QCoreApplication.translate("MainWindow", u"\u0411\u044b\u0441\u0442\u0440\u044b\u0439 \u043f\u043e\u0438\u0441\u043a:", None))
        self.groupBox_6.setTitle(QCoreApplication.translate("MainWindow", u"3) \u0412\u044b\u0434\u0435\u043b\u0438\u0442\u0435 \u043b\u044e\u0434\u0435\u0439 \u043a\u043e\u0442\u043e\u0440\u044b\u043c \u0432\u044b \u0445\u043e\u0442\u0438\u0442\u0435 \u0434\u043e\u0431\u0430\u0432\u0438\u0442\u044c \u0443\u0441\u043b\u0443\u0433\u0438", None))
        self.pushButton_11.setText(QCoreApplication.translate("MainWindow", u"\u041d\u043e\u0432\u044b\u0439 \u0441\u043f\u0438\u0441\u043e\u043a \u0438\u0437 \u0432\u044b\u0434\u0435\u043b\u0435\u043d\u043d\u044b\u0445", None))
        self.pushButton_8.setText(QCoreApplication.translate("MainWindow", u"\u0412\u044b\u0434\u0435\u043b\u0438\u0442\u044c \u0432\u0441\u0435\u0445", None))
        self.pushButton_9.setText(QCoreApplication.translate("MainWindow", u"\u0421\u043d\u044f\u0442\u044c \u0432\u044b\u0434\u0435\u043b\u0435\u043d\u0438\u0435", None))
        self.label_38.setText(QCoreApplication.translate("MainWindow", u"\u041b\u044e\u0434\u0438 \u0432\u0445\u043e\u0434\u044f\u0449\u0438\u0435 \u0432 \u0433\u0440\u0443\u043f\u043f\u0443:", None))
        self.groupBox_4.setTitle(QCoreApplication.translate("MainWindow", u"2) \u0423\u0441\u0442\u0430\u043d\u043e\u0432\u0438\u0442\u0435 \u0434\u0430\u0442\u0443 \u0432\u0432\u043e\u0434\u0430, \u0440\u0430\u0431\u043e\u0442\u043d\u0438\u043a\u0430, \u0430 \u0442\u0430\u043a\u0436\u0435 \u0443\u0441\u043b\u0443\u0433\u0443 \u0438\u043b\u0438 _\u043a\u0440\u0443\u0436\u043e\u043a:\n"
"                                           ", None))
        self.label_42.setText(QCoreApplication.translate("MainWindow", u"\u041a\u043e\u043b\u0438\u0447\u0435\u0441\u0442\u0432\u043e \u0443\u0441\u043b\u0443\u0433:", None))
        self.label_39.setText(QCoreApplication.translate("MainWindow", u"\u0423\u0441\u043b\u0443\u0433\u0430:", None))
        self.label_45.setText(QCoreApplication.translate("MainWindow", u"\u041f\u0440\u0438\u043c./_\u043a\u0440\u0443\u0436\u043e\u043a:", None))
        self.label_44.setText(QCoreApplication.translate("MainWindow", u"\u0420\u0430\u0431\u043e\u0442\u043d\u0438\u043a:", None))
        self.label_46.setText(QCoreApplication.translate("MainWindow", u"\u0414\u0430\u0442\u0430:", None))
        self.btn_qle_date_2.setText(QCoreApplication.translate("MainWindow", u"\u043c\u0438\u043d\u0443\u0441 \u0434\u0435\u043d\u044c", None))
        self.btn_qle_date_p1_2.setText(QCoreApplication.translate("MainWindow", u"\u043f\u043b\u044e\u0441 \u0434\u0435\u043d\u044c", None))
        self.label_48.setText(QCoreApplication.translate("MainWindow", u"\u041f\u043e\u0441\u043b\u0435\u0434\u043d\u0438\u0435 \u0434\u0435\u0439\u0441\u0442\u0432\u0438\u044f:", None))
        self.pushButton_12.setText(QCoreApplication.translate("MainWindow", u"4) \u0412\u0432\u0435\u0441\u0442\u0438 N \u0443\u0441\u043b\u0443\u0433 \u043d\u0430 M \u043b\u044e\u0434\u0435\u0439", None))
        self.tabs_add_serv.setTabText(self.tabs_add_serv.indexOf(self.tab_add_group_services), QCoreApplication.translate("MainWindow", u"\u0412\u0432\u043e\u0434 \u0433\u0440\u0443\u043f\u043f\u043e\u0432\u044b\u0445 \u0443\u0441\u043b\u0443\u0433", None))
        self.pushButton_3.setText(QCoreApplication.translate("MainWindow", u"PushButton", None))
        self.tabs_add_serv.setTabText(self.tabs_add_serv.indexOf(self.tab_show_group_services), QCoreApplication.translate("MainWindow", u"\u041f\u0440\u043e\u0441\u043c\u043e\u0442\u0440 \u0432\u0432\u0435\u0434\u0435\u043d\u043d\u044b\u0445 \u0433\u0440\u0443\u043f\u043e\u0432\u044b\u0445 \u0443\u0441\u043b\u0443\u0433", None))
        self.pushButton_37.setText(QCoreApplication.translate("MainWindow", u"PushButton", None))
        self.tabs_add_serv.setTabText(self.tabs_add_serv.indexOf(self.tab_add_club_services), QCoreApplication.translate("MainWindow", u"\u0412\u0432\u043e\u0434 \u043a\u0440\u0443\u0436\u043a\u043e\u0432/\u043a\u043b\u0443\u0431\u043e\u0432", None))
        self.label_87.setText(QCoreApplication.translate("MainWindow", u"\u0424\u0418\u041e:", None))
        self.label_86.setText(QCoreApplication.translate("MainWindow", u"\u0424\u0438\u043b\u044c\u0442\u0440:", None))
        self.chk_all_serv_ripso.setText(QCoreApplication.translate("MainWindow", u"\u041f\u043e\u043a\u0430\u0437\u0430\u0442\u044c \u0432\u0441\u0435 \u0443\u0441\u043b\u0443\u0433\u0438 \u043f\u043e \u0440\u0438\u043f\u0441\u043e", None))
        self.label_85.setText(QCoreApplication.translate("MainWindow", u"\u0414\u043e\u0433\u043e\u0432\u043e\u0440:", None))
        self.btn_goto_client_2.setText(QCoreApplication.translate("MainWindow", u"\u041b\u0438\u0447\u043d\u043e\u0435 \u0434\u0435\u043b\u043e", None))
        self.label_88.setText(QCoreApplication.translate("MainWindow", u"\u041f\u043b\u0430\u043d \u043f\u0440\u043e\u0432\u0435\u0440\u0435\u043d:", None))
#if QT_CONFIG(tooltip)
        self.cbx_1_ui_select_fiolist__4.setToolTip(QCoreApplication.translate("MainWindow", u"\u0421\u043f\u0438\u0441\u043a\u0438 \u043b\u044e\u0434\u0435\u0439", None))
#endif // QT_CONFIG(tooltip)
        self.cbx_1_ui_select_fiolist__4.setCurrentText("")
        self.pushButton_4.setText(QCoreApplication.translate("MainWindow", u"\u041e\u0431\u043d\u043e\u0432\u0438\u0442\u044c", None))
        self.tabs_add_serv.setTabText(self.tabs_add_serv.indexOf(self.tab_table_serv), QCoreApplication.translate("MainWindow", u"\u0423\u0441\u043b\u0443\u0433\u0438 \u0432 \u0432\u0438\u0434\u0435 \u0442\u0430\u0431\u043b\u0438\u0446\u044b", None))
        self.tabMain.setTabText(self.tabMain.indexOf(self.tab_add_serv), QCoreApplication.translate("MainWindow", u"\u0412\u0432\u043e\u0434 \u0443\u0441\u043b\u0443\u0433", None))
#if QT_CONFIG(accessibility)
        self.tab_fio_dep.setAccessibleName("")
#endif // QT_CONFIG(accessibility)
        self.btn_upd_fio_list.setText(QCoreApplication.translate("MainWindow", u"\u041e\u0431\u043d\u043e\u0432\u0438\u0442\u044c \u0441\u043f\u0438\u0441\u043e\u043a", None))
        self.pushButton_2.setText(QCoreApplication.translate("MainWindow", u"\u041f\u0440\u0438\u043c\u0435\u043d\u0438\u0442\u044c \u0441\u043b\u043e\u0436\u043d\u044b\u0439 \u0444\u0438\u043b\u044c\u0442\u0440", None))
        self.btn_goto_serv_from_list.setText(QCoreApplication.translate("MainWindow", u"\u0412\u0432\u0435\u0441\u0442\u0438 \u0443\u0441\u043b\u0443\u0433\u0438", None))
        self.btn_goto_client_from_list.setText(QCoreApplication.translate("MainWindow", u"\u041b\u0438\u0447\u043d\u043e\u0435 \u0434\u0435\u043b\u043e", None))
        self.tabs_fio_dep.setTabText(self.tabs_fio_dep.indexOf(self.tab_people_of_dep), QCoreApplication.translate("MainWindow", u"\u0421\u043f\u0438\u0441\u043e\u043a \u043e\u0431\u0441\u043b\u0443\u0436\u0438\u0432\u0430\u0435\u043c\u044b\u0445 \u043d\u0430 \u043e\u0442\u0434\u0435\u043b\u0435\u043d\u0438\u0438", None))
        self.tabs_fio_dep.setTabText(self.tabs_fio_dep.indexOf(self.tab_33), QCoreApplication.translate("MainWindow", u"...\u0435\u0449\u0435 \u0431\u0435\u0437 \u0434\u043e\u0433\u043e\u0432\u043e\u0440\u0430", None))
        self.tabs_fio_dep.setTabText(self.tabs_fio_dep.indexOf(self.tab_53), QCoreApplication.translate("MainWindow", u"\u041f\u043e\u043b\u0443\u0447\u0430\u043b\u0438 \u0443\u0441\u043b\u0443\u0433\u0438 \u0432 \u044d\u0442\u043e\u043c \u0433\u043e\u0434\u0443", None))
        self.tabs_fio_dep.setTabText(self.tabs_fio_dep.indexOf(self.tab_55), QCoreApplication.translate("MainWindow", u"\u0421\u043d\u044f\u0442\u044b \u0441 \u043e\u0431\u0441\u043b\u0443\u0436\u0438\u0432\u0430\u043d\u0438\u044f \u0432 \u044d\u0442\u043e\u043c \u0433\u043e\u0434\u0443", None))
        self.tabs_fio_dep.setTabText(self.tabs_fio_dep.indexOf(self.tab_40), QCoreApplication.translate("MainWindow", u"\u0417\u0430\u043a\u0430\u043d\u0447\u0438\u0432\u0430\u0435\u0442\u0441\u044f \u0434\u043e\u0433\u043e\u0432\u043e\u0440", None))
        self.tabs_fio_dep.setTabText(self.tabs_fio_dep.indexOf(self.tab_39), QCoreApplication.translate("MainWindow", u"\u041e\u0431\u0441\u043b\u0443\u0436\u0438\u0432\u0430\u043b\u0438\u0441\u044c \u0440\u0430\u043d\u0435\u0435", None))
        self.tabs_fio_dep.setTabText(self.tabs_fio_dep.indexOf(self.tab__dep_has_client_more), QCoreApplication.translate("MainWindow", u"\u0420\u0430\u0441\u0448\u0438\u0440\u0435\u043d\u043d\u044b\u0439 \u0441\u043f\u0438\u0441\u043e\u043a", None))
        self.label_fio_filter.setText(QCoreApplication.translate("MainWindow", u"\u0411\u044b\u0441\u0442\u0440\u044b\u0439 \u0444\u0438\u043b\u044c\u0442\u0440", None))
        self.tabMain.setTabText(self.tabMain.indexOf(self.tab_fio_dep), QCoreApplication.translate("MainWindow", u"\u0421\u043f\u0438\u0441\u043e\u043a \u043e\u0431\u0441\u043b\u0443\u0436\u0438\u0432\u0430\u0435\u043c\u044b\u0445 \u043d\u0430 \u043e\u0442\u0434\u0435\u043b\u0435\u043d\u0438\u0438", None))
        self.label_client.setText(QCoreApplication.translate("MainWindow", u"\u0411\u044b\u0441\u0442\u0440\u044b\u0439 &\u0444\u0438\u043b\u044c\u0442\u0440:", None))
        self.pushButton_7.setText(QCoreApplication.translate("MainWindow", u"\u041f\u0435\u0440\u0435\u0439\u0442\u0438 \u043a \u043a\u0430\u0440\u0442\u043e\u0447\u043a\u0435", None))
        self.pushButton_15.setText(QCoreApplication.translate("MainWindow", u"\u0421\u043e\u0437\u0434\u0430\u0442\u044c \u043d\u043e\u0432\u044b\u0439 \u0434\u043e\u0433\u043e\u0432\u043e\u0440 \u0434\u043b\u044f \u0432\u044b\u0431\u0440\u0430\u043d\u043d\u043e\u0433\u043e \u0447\u0435\u043b\u043e\u0432\u0435\u043a\u0430", None))
        self.tabs_client2.setTabText(self.tabs_client2.indexOf(self.tab_35), QCoreApplication.translate("MainWindow", u"\u0412\u0441\u0435 \u043e\u0431\u0440\u0430\u0449\u0430\u0432\u0448\u0438\u0435\u0441\u044f", None))
        self.tabs_client2.setTabText(self.tabs_client2.indexOf(self.tab_15), QCoreApplication.translate("MainWindow", u"\u0412\u0441\u0435 \u043e\u0431\u0441\u043b\u0443\u0436\u0438\u0432\u0430\u0435\u043c\u044b\u0435", None))
        self.tabs_client2.setTabText(self.tabs_client2.indexOf(self.tab), QCoreApplication.translate("MainWindow", u"\u041f\u043e\u0434\u0445\u043e\u0434\u044f\u0442 \u043f\u043e \u0420\u0418\u041f\u0421\u041e", None))
        self.tabs_client2.setTabText(self.tabs_client2.indexOf(self.tab_36), QCoreApplication.translate("MainWindow", u"\u0417\u0430\u043a\u043e\u043d\u0447\u0438\u043b\u0441\u044f \u0434\u043e\u0433\u043e\u0432\u043e\u0440", None))
        self.tabMain.setTabText(self.tabMain.indexOf(self.tab_clients), QCoreApplication.translate("MainWindow", u"\u0412\u0441\u0435 \u043b\u044e\u0434\u0438 \u0432 \u043e\u0440\u0433\u0430\u043d\u0438\u0437\u0430\u0446\u0438\u0438", None))
#if QT_CONFIG(tooltip)
        self.btn_goto_serv_add.setToolTip(QCoreApplication.translate("MainWindow", u"\u0412\u0432\u0435\u0441\u0442\u0438 \u0443\u0441\u043b\u0443\u0433\u0438 \u043d\u0430 \u044d\u0442\u043e\u0433\u043e \u0447\u0435\u043b\u043e\u0432\u0435\u043a\u0430", None))
#endif // QT_CONFIG(tooltip)
        self.btn_goto_serv_add.setText(QCoreApplication.translate("MainWindow", u"...", None))
        self.label_21.setText(QCoreApplication.translate("MainWindow", u"\u041f\u0435\u0440\u0435\u0445\u043e\u0434 \u043a \u0424\u0418\u041e:", None))
        self.btn_prev.setText(QCoreApplication.translate("MainWindow", u"<<\u043f\u0440\u0435\u0434", None))
        self.btn_next.setText(QCoreApplication.translate("MainWindow", u"\u0441\u043b\u0435\u0434>>", None))
        self.label_23.setText(QCoreApplication.translate("MainWindow", u"\u0424\u0438\u043b\u044c\u0442\u0440:", None))
        self.groupBox.setTitle("")
        self.groupBox_2.setTitle(QCoreApplication.translate("MainWindow", u"\u0414\u0430\u043d\u043d\u044b\u0435 \u0434\u043b\u044f \u0434\u043e\u0433\u043e\u0432\u043e\u0440\u043e\u0432:", None))
        self.groupBox_3.setTitle("")
        self.label_22.setText(QCoreApplication.translate("MainWindow", u"\u0424\u0418\u041e:", None))
        self.label_27.setText(QCoreApplication.translate("MainWindow", u"\u0414\u0430\u0442\u0430 \u0441\u043c\u0435\u0440\u0442\u0438:", None))
        self.label_49.setText(QCoreApplication.translate("MainWindow", u"\u0422\u0435\u043b\u0435\u0444\u043e\u043d:", None))
        self.label_24.setText(QCoreApplication.translate("MainWindow", u"\u042d\u0421\u0420\u041d:", None))
        self.label_25.setText(QCoreApplication.translate("MainWindow", u"\u0414\u0430\u0442\u0430 \u0440\u043e\u0436\u0434\u0435\u043d\u0438\u044f:", None))
        self.label_50.setText(QCoreApplication.translate("MainWindow", u"\u0421\u041d\u0418\u041b\u0421:", None))
        self.qle_SNILS.setText("")
        self.label_52.setText(QCoreApplication.translate("MainWindow", u"\u041f\u0440\u0438\u043c\u0435\u0447\u0430\u043d\u0438\u0435:", None))
        self.tabs_client.setTabText(self.tabs_client.indexOf(self.tab_people_main), QCoreApplication.translate("MainWindow", u"\u041a\u0430\u0440\u0442\u043e\u0447\u043a\u0430 \u043f\u043e\u043b\u0443\u0447\u0430\u0442\u0435\u043b\u044f \u0421\u0423", None))
        self.label_54.setText(QCoreApplication.translate("MainWindow", u"\u0414\u043e\u0431\u0430\u0432\u0438\u0442\u044c \u043a\u0430\u0442\u0435\u0433\u043e\u0440\u0438\u044e:", None))
        self.label_83.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>\u0437\u0434\u0435\u0441\u044c \u0431\u0443\u0434\u0443\u0442 \u0444\u043b\u0430\u0436\u043a\u0438</p><p> \u0441\n"
"                    \u043a\u0430\u0442\u0435\u0433\u043e\u0440\u0438\u044f\u043c\u0438</p></body></html>\n"
"                   ", None))
        self.tabs_client.setTabText(self.tabs_client.indexOf(self.tab_pcat), QCoreApplication.translate("MainWindow", u"\u041b\u044c\u0433\u043e\u0442\u043d\u044b\u0435 \u043a\u0430\u0442\u0435\u0433\u043e\u0440\u0438\u0438", None))
        self.label_60.setText(QCoreApplication.translate("MainWindow", u"\u041d\u043e\u043c\u0435\u0440 \u0418\u041f\u041f\u0421\u0423:", None))
        self.label_59.setText(QCoreApplication.translate("MainWindow", u"\u0420\u0418\u041f\u0421\u041e:", None))
        self.chk_to_recheck.setText(QCoreApplication.translate("MainWindow", u"\u0412\u0437\u044f\u0442\u044c \u043f\u043e\u043b\u043e\u0436\u0435\u043d\u043e \u0443\u0441\u043b\u0443\u0433 \u0438\u0437 \u0418\u041f\u041f\u0421\u0423", None))
        self.label_55.setText(QCoreApplication.translate("MainWindow", u"\u041d\u043e\u043c\u0435\u0440 \u0434\u043e\u0433\u043e\u0432\u043e\u0440\u0430:", None))
        self.groupBox_7.setTitle("")
        self.label_62.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>\u0412\u044b\u0431\u0435\u0440\u0438\u0442\u0435<br>\u0434\u043e\u0433\u043e\u0432\u043e\u0440:</p></body></html>", None))
        self.btn_prev_2.setText(QCoreApplication.translate("MainWindow", u"<<\u043f\u0440\u0435\u0434", None))
        self.btn_next_2.setText(QCoreApplication.translate("MainWindow", u"\u0441\u043b\u0435\u0434>>", None))
        self.label_56.setText(QCoreApplication.translate("MainWindow", u"\u0414\u0435\u0439\u0441\u0442\u0432\u0443\u0435\u0442 c:", None))
        self.label_61.setText(QCoreApplication.translate("MainWindow", u"\u041f\u0440\u0438\u043c\u0435\u0447\u0430\u043d\u0438\u0435:", None))
        self.btn_paste_planned.setText(QCoreApplication.translate("MainWindow", u"\u0412\u0441\u0442\u0430\u0432\u0438\u0442\u044c \u043f\u043b\u0430\u043d \u0443\u0441\u043b\u0443\u0433...", None))
        self.pushButton.setText(QCoreApplication.translate("MainWindow", u"\u041f\u043e\u0434\u0441\u043a\u0430\u0437\u043a\u0430 ", None))
        self.tab_sub_client.setTabText(self.tab_sub_client.indexOf(self.tab_contract_planned), QCoreApplication.translate("MainWindow", u"\u041f\u043e\u043b\u043e\u0436\u0435\u043d\u043e \u0443\u0441\u043b\u0443\u0433", None))
        self.tab_sub_client.setTabText(self.tab_sub_client.indexOf(self.tab_43), QCoreApplication.translate("MainWindow", u"\u041f\u043e\u043b\u0443\u0447\u0435\u043d\u043d\u044b\u0435 \u0443\u0441\u043b\u0443\u0433\u0438 \u043f\u043e \u0438\u043f\u043f\u0441\u0443(\u0434\u043e\u0433\u043e\u0432\u043e\u0440\u0443)", None))
        self.tab_sub_client.setTabText(self.tab_sub_client.indexOf(self.tab_54), QCoreApplication.translate("MainWindow", u"\u0414\u0430\u043d\u043d\u044b\u0435 \u0434\u043b\u044f \u0434\u043e\u0433\u043e\u0432\u043e\u0440\u043e\u0432:", None))
        self.label_57.setText(QCoreApplication.translate("MainWindow", u"\u043f\u043e:", None))
        self.chk_blocked.setText(QCoreApplication.translate("MainWindow", u"\u0417\u0430\u0431\u043b\u043e\u043a\u0438\u0440\u043e\u0432\u0430\u043d", None))
        self.label_58.setText(QCoreApplication.translate("MainWindow", u"\u041e\u0442\u0434\u0435\u043b\u0435\u043d\u0438\u0435:", None))
        self.label_84.setText(QCoreApplication.translate("MainWindow", u"\u043d\u043e\u0432\u044b\u0439:", None))
#if QT_CONFIG(tooltip)
        self.qle_contracts2.setToolTip(QCoreApplication.translate("MainWindow", u"\u0434\u043e\u0433\u043e\u0432\u043e\u0440 \u0432 \u044d\u0442\u043e\u043c \u0433\u043e\u0434\u0443, \u043c\u043e\u0436\u043d\u043e \u043d\u0435 \u0437\u0430\u043f\u043e\u043b\u043d\u044f\u0442\u044c", None))
#endif // QT_CONFIG(tooltip)
        self.tabs_client.setTabText(self.tabs_client.indexOf(self.tab_client_contr), QCoreApplication.translate("MainWindow", u"\u0414\u043e\u0433\u043e\u0432\u043e\u0440\u0430", None))
        self.tabs_client.setTabText(self.tabs_client.indexOf(self.tab_2), QCoreApplication.translate("MainWindow", u"\u041f\u043e\u043b\u0443\u0447\u0435\u043d\u043d\u044b\u0435 \u0443\u0441\u043b\u0443\u0433\u0438 \u043d\u0430 \u043e\u0442\u0434\u0435\u043b\u0435\u043d\u0438\u0438", None))
        self.tabs_client.setTabText(self.tabs_client.indexOf(self.tab_5), QCoreApplication.translate("MainWindow", u"\u0412\u0441\u0435 \u043f\u043e\u043b\u0443\u0447\u0435\u043d\u043d\u044b\u0435 \u0443\u0441\u043b\u0443\u0433\u0438", None))
        self.tabMain.setTabText(self.tabMain.indexOf(self.tab_client), QCoreApplication.translate("MainWindow", u"\u041b\u0438\u0447\u043d\u043e\u0435 \u0434\u0435\u043b\u043e \u0447\u0435\u043b\u043e\u0432\u0435\u043a\u0430", None))
        self.label_19.setText(QCoreApplication.translate("MainWindow", u"\u0424\u0438\u043b\u044c\u0442\u0440:", None))
        self.btn_serv_you_3.setText(QCoreApplication.translate("MainWindow", u"\u041f\u043e\u0441\u0447\u0438\u0442\u0430\u0442\u044c", None))
        self.pushButton_17.setText(QCoreApplication.translate("MainWindow", u"\u0414\u043e\u0431\u0430\u0432\u0438\u0442\u044c \u0443\u0441\u043b\u043e\u0432\u0438\u044f", None))
        self.DO_NOT_USE_18.setText(QCoreApplication.translate("MainWindow", u"\u041e\u043a\u043e\u043d\u0447\u0430\u043d\u0438\u0435:", None))
        self.DO_NOT_USE_19.setText(QCoreApplication.translate("MainWindow", u"\u041d\u0430\u0447\u0430\u043b\u043e:", None))
        self.DO_NOT_USE_14.setTabText(self.DO_NOT_USE_14.indexOf(self.DO_NOT_USE_15), QCoreApplication.translate("MainWindow", u"\u041f\u0440\u043e\u0438\u0437\u0432\u043e\u043b\u044c\u043d\u044b\u0439 \u043f\u0435\u0440\u0438\u043e\u0434", None))
        self.DO_NOT_USE_23.setText(QCoreApplication.translate("MainWindow", u"\u041c\u0435\u0441\u044f\u0446:", None))
        self.DO_NOT_USE_25.setText(QCoreApplication.translate("MainWindow", u"\u0413\u043e\u0434:", None))
        self.DO_NOT_USE_14.setTabText(self.DO_NOT_USE_14.indexOf(self.DO_NOT_USE_21), QCoreApplication.translate("MainWindow", u"\u041f\u0435\u0440\u0438\u043e\u0434 \u0438\u0437 \u0441\u043f\u0438\u0441\u043a\u0430", None))
        self.tabs_tot_serv.setTabText(self.tabs_tot_serv.indexOf(self.tab_12), QCoreApplication.translate("MainWindow", u"\u0423\u0441\u043b\u0443\u0433\u0438 \u043e\u0442\u0434\u0435\u043b\u0435\u043d\u0438\u044f", None))
        self.btn_serv_you_5.setText(QCoreApplication.translate("MainWindow", u"\u041f\u043e\u0441\u0447\u0438\u0442\u0430\u0442\u044c", None))
        self.pushButton_19.setText(QCoreApplication.translate("MainWindow", u"\u0414\u043e\u0431\u0430\u0432\u0438\u0442\u044c \u0443\u0441\u043b\u043e\u0432\u0438\u044f", None))
        self.DO_NOT_USE_70.setText(QCoreApplication.translate("MainWindow", u"\u041e\u043a\u043e\u043d\u0447\u0430\u043d\u0438\u0435:", None))
        self.DO_NOT_USE_71.setText(QCoreApplication.translate("MainWindow", u"\u041d\u0430\u0447\u0430\u043b\u043e:", None))
        self.DO_NOT_USE_53.setTabText(self.DO_NOT_USE_53.indexOf(self.DO_NOT_USE_67), QCoreApplication.translate("MainWindow", u"\u041f\u0440\u043e\u0438\u0437\u0432\u043e\u043b\u044c\u043d\u044b\u0439 \u043f\u0435\u0440\u0438\u043e\u0434", None))
        self.DO_NOT_USE_75.setText(QCoreApplication.translate("MainWindow", u"\u041c\u0435\u0441\u044f\u0446:", None))
        self.DO_NOT_USE_77.setText(QCoreApplication.translate("MainWindow", u"\u0413\u043e\u0434:", None))
        self.DO_NOT_USE_53.setTabText(self.DO_NOT_USE_53.indexOf(self.DO_NOT_USE_73), QCoreApplication.translate("MainWindow", u"\u041f\u0435\u0440\u0438\u043e\u0434 \u0438\u0437 \u0441\u043f\u0438\u0441\u043a\u0430", None))
        self.tabs_tot_serv.setTabText(self.tabs_tot_serv.indexOf(self.tab_serv_you), QCoreApplication.translate("MainWindow", u"\u041e\u043a\u0430\u0437\u0430\u043d\u043d\u044b\u0435 \u0432\u0430\u043c\u0438", None))
        self.btn_serv_you_6.setText(QCoreApplication.translate("MainWindow", u"\u041f\u043e\u0441\u0447\u0438\u0442\u0430\u0442\u044c", None))
        self.pushButton_20.setText(QCoreApplication.translate("MainWindow", u"\u0414\u043e\u0431\u0430\u0432\u0438\u0442\u044c \u0443\u0441\u043b\u043e\u0432\u0438\u044f", None))
        self.DO_NOT_USE_83.setText(QCoreApplication.translate("MainWindow", u"\u041e\u043a\u043e\u043d\u0447\u0430\u043d\u0438\u0435:", None))
        self.DO_NOT_USE_84.setText(QCoreApplication.translate("MainWindow", u"\u041d\u0430\u0447\u0430\u043b\u043e:", None))
        self.DO_NOT_USE_79.setTabText(self.DO_NOT_USE_79.indexOf(self.DO_NOT_USE_80), QCoreApplication.translate("MainWindow", u"\u041f\u0440\u043e\u0438\u0437\u0432\u043e\u043b\u044c\u043d\u044b\u0439 \u043f\u0435\u0440\u0438\u043e\u0434", None))
        self.DO_NOT_USE_88.setText(QCoreApplication.translate("MainWindow", u"\u041c\u0435\u0441\u044f\u0446:", None))
        self.DO_NOT_USE_90.setText(QCoreApplication.translate("MainWindow", u"\u0413\u043e\u0434:", None))
        self.DO_NOT_USE_79.setTabText(self.DO_NOT_USE_79.indexOf(self.DO_NOT_USE_86), QCoreApplication.translate("MainWindow", u"\u041f\u0435\u0440\u0438\u043e\u0434 \u0438\u0437 \u0441\u043f\u0438\u0441\u043a\u0430", None))
        self.tabs_tot_serv.setTabText(self.tabs_tot_serv.indexOf(self.tab_9), QCoreApplication.translate("MainWindow", u"\u0412\u0432\u0435\u0434\u0435\u043d\u043d\u044b\u0435 \u0432\u0430\u043c\u0438", None))
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"\u0412\u044b\u0431\u0435\u0440\u0438\u0442\u0435 \u0440\u0430\u0431\u043e\u0442\u043d\u0438\u043a\u0430:", None))
        self.pushButton_21.setText(QCoreApplication.translate("MainWindow", u"\u0414\u043e\u0431\u0430\u0432\u0438\u0442\u044c \u0443\u0441\u043b\u043e\u0432\u0438\u044f", None))
        self.btn_serv_you_7.setText(QCoreApplication.translate("MainWindow", u"\u041f\u043e\u0441\u0447\u0438\u0442\u0430\u0442\u044c", None))
        self.DO_NOT_USE_96.setText(QCoreApplication.translate("MainWindow", u"\u041e\u043a\u043e\u043d\u0447\u0430\u043d\u0438\u0435:", None))
        self.DO_NOT_USE_97.setText(QCoreApplication.translate("MainWindow", u"\u041d\u0430\u0447\u0430\u043b\u043e:", None))
        self.DO_NOT_USE_92.setTabText(self.DO_NOT_USE_92.indexOf(self.DO_NOT_USE_93), QCoreApplication.translate("MainWindow", u"\u041f\u0440\u043e\u0438\u0437\u0432\u043e\u043b\u044c\u043d\u044b\u0439 \u043f\u0435\u0440\u0438\u043e\u0434", None))
        self.DO_NOT_USE_101.setText(QCoreApplication.translate("MainWindow", u"\u041c\u0435\u0441\u044f\u0446:", None))
        self.DO_NOT_USE_103.setText(QCoreApplication.translate("MainWindow", u"\u0413\u043e\u0434:", None))
        self.DO_NOT_USE_92.setTabText(self.DO_NOT_USE_92.indexOf(self.DO_NOT_USE_99), QCoreApplication.translate("MainWindow", u"\u041f\u0435\u0440\u0438\u043e\u0434 \u0438\u0437 \u0441\u043f\u0438\u0441\u043a\u0430", None))
        self.tabs_tot_serv.setTabText(self.tabs_tot_serv.indexOf(self.tab_19), QCoreApplication.translate("MainWindow", u"\u0423\u0441\u043b\u0443\u0433\u0438 \u043f\u043e \u0440\u0430\u0431\u043e\u0442\u043d\u0438\u043a\u0430\u043c", None))
        self.pushButton_36.setText(QCoreApplication.translate("MainWindow", u"\u0414\u043e\u0431\u0430\u0432\u0438\u0442\u044c \u0443\u0441\u043b\u043e\u0432\u0438\u044f", None))
        self.btn_serv_you_22.setText(QCoreApplication.translate("MainWindow", u"\u041f\u043e\u0441\u0447\u0438\u0442\u0430\u0442\u044c", None))
        self.DO_NOT_USE_278.setText(QCoreApplication.translate("MainWindow", u"\u041e\u043a\u043e\u043d\u0447\u0430\u043d\u0438\u0435:", None))
        self.DO_NOT_USE_279.setText(QCoreApplication.translate("MainWindow", u"\u041d\u0430\u0447\u0430\u043b\u043e:", None))
        self.DO_NOT_USE_274.setTabText(self.DO_NOT_USE_274.indexOf(self.DO_NOT_USE_275), QCoreApplication.translate("MainWindow", u"\u041f\u0440\u043e\u0438\u0437\u0432\u043e\u043b\u044c\u043d\u044b\u0439 \u043f\u0435\u0440\u0438\u043e\u0434", None))
        self.DO_NOT_USE_283.setText(QCoreApplication.translate("MainWindow", u"\u041c\u0435\u0441\u044f\u0446:", None))
        self.DO_NOT_USE_285.setText(QCoreApplication.translate("MainWindow", u"\u0413\u043e\u0434:", None))
        self.DO_NOT_USE_274.setTabText(self.DO_NOT_USE_274.indexOf(self.DO_NOT_USE_281), QCoreApplication.translate("MainWindow", u"\u041f\u0435\u0440\u0438\u043e\u0434 \u0438\u0437 \u0441\u043f\u0438\u0441\u043a\u0430", None))
        self.label_74.setText(QCoreApplication.translate("MainWindow", u"\u0412\u044b\u0431\u0435\u0440\u0438\u0442\u0435 \u043a\u0430\u0442\u0435\u0433\u043e\u0440\u0438\u044e:", None))
        self.tabs_tot_serv.setTabText(self.tabs_tot_serv.indexOf(self.tab_4), QCoreApplication.translate("MainWindow", u"\u0421\u0442\u0440\u0430\u043d\u0438\u0446\u0430", None))
        self.pushButton_22.setText(QCoreApplication.translate("MainWindow", u"\u0414\u043e\u0431\u0430\u0432\u0438\u0442\u044c \u0443\u0441\u043b\u043e\u0432\u0438\u044f", None))
        self.btn_serv_you_8.setText(QCoreApplication.translate("MainWindow", u"\u041f\u043e\u0441\u0447\u0438\u0442\u0430\u0442\u044c", None))
        self.DO_NOT_USE_109.setText(QCoreApplication.translate("MainWindow", u"\u041e\u043a\u043e\u043d\u0447\u0430\u043d\u0438\u0435:", None))
        self.DO_NOT_USE_110.setText(QCoreApplication.translate("MainWindow", u"\u041d\u0430\u0447\u0430\u043b\u043e:", None))
        self.DO_NOT_USE_105.setTabText(self.DO_NOT_USE_105.indexOf(self.DO_NOT_USE_106), QCoreApplication.translate("MainWindow", u"\u041f\u0440\u043e\u0438\u0437\u0432\u043e\u043b\u044c\u043d\u044b\u0439 \u043f\u0435\u0440\u0438\u043e\u0434", None))
        self.DO_NOT_USE_114.setText(QCoreApplication.translate("MainWindow", u"\u041c\u0435\u0441\u044f\u0446:", None))
        self.DO_NOT_USE_116.setText(QCoreApplication.translate("MainWindow", u"\u0413\u043e\u0434:", None))
        self.DO_NOT_USE_105.setTabText(self.DO_NOT_USE_105.indexOf(self.DO_NOT_USE_112), QCoreApplication.translate("MainWindow", u"\u041f\u0435\u0440\u0438\u043e\u0434 \u0438\u0437 \u0441\u043f\u0438\u0441\u043a\u0430", None))
        self.tabs_tot_serv.setTabText(self.tabs_tot_serv.indexOf(self.tab_6), QCoreApplication.translate("MainWindow", u"\u0414\u043b\u044f \u044d\u043a\u0441\u043f\u043e\u0440\u0442\u0430", None))
        self.tabs_total.setTabText(self.tabs_total.indexOf(self.tab_tot_serv), QCoreApplication.translate("MainWindow", u"\u0421\u043f\u0438\u0441\u043a\u0438 \u0443\u0441\u043b\u0443\u0433", None))
        self.label_20.setText(QCoreApplication.translate("MainWindow", u"\u0424\u0438\u043b\u044c\u0442\u0440:", None))
        self.btn_serv_you_4.setText(QCoreApplication.translate("MainWindow", u"\u041f\u043e\u0441\u0447\u0438\u0442\u0430\u0442\u044c", None))
        self.pushButton_18.setText(QCoreApplication.translate("MainWindow", u"\u0414\u043e\u0431\u0430\u0432\u0438\u0442\u044c \u0443\u0441\u043b\u043e\u0432\u0438\u044f", None))
        self.DO_NOT_USE_31.setText(QCoreApplication.translate("MainWindow", u"\u041e\u043a\u043e\u043d\u0447\u0430\u043d\u0438\u0435:", None))
        self.DO_NOT_USE_32.setText(QCoreApplication.translate("MainWindow", u"\u041d\u0430\u0447\u0430\u043b\u043e:", None))
        self.DO_NOT_USE_27.setTabText(self.DO_NOT_USE_27.indexOf(self.DO_NOT_USE_28), QCoreApplication.translate("MainWindow", u"\u041f\u0440\u043e\u0438\u0437\u0432\u043e\u043b\u044c\u043d\u044b\u0439 \u043f\u0435\u0440\u0438\u043e\u0434", None))
        self.DO_NOT_USE_36.setText(QCoreApplication.translate("MainWindow", u"\u041c\u0435\u0441\u044f\u0446:", None))
        self.DO_NOT_USE_38.setText(QCoreApplication.translate("MainWindow", u"\u0413\u043e\u0434:", None))
        self.DO_NOT_USE_27.setTabText(self.DO_NOT_USE_27.indexOf(self.DO_NOT_USE_34), QCoreApplication.translate("MainWindow", u"\u041f\u0435\u0440\u0438\u043e\u0434 \u0438\u0437 \u0441\u043f\u0438\u0441\u043a\u0430", None))
        self.tabWidget_8.setTabText(self.tabWidget_8.indexOf(self.tab_tot_group_dep), QCoreApplication.translate("MainWindow", u"\u0418\u0442\u043e\u0433\u0438 \u043f\u043e \u043e\u0442\u0434\u0435\u043b\u0435\u043d\u0438\u044e", None))
        self.label_51.setText(QCoreApplication.translate("MainWindow", u"\u0424\u0438\u043b\u044c\u0442\u0440:", None))
        self.btn_serv_you_9.setText(QCoreApplication.translate("MainWindow", u"\u041f\u043e\u0441\u0447\u0438\u0442\u0430\u0442\u044c", None))
        self.pushButton_23.setText(QCoreApplication.translate("MainWindow", u"\u0414\u043e\u0431\u0430\u0432\u0438\u0442\u044c \u0443\u0441\u043b\u043e\u0432\u0438\u044f", None))
        self.DO_NOT_USE_44.setText(QCoreApplication.translate("MainWindow", u"\u041e\u043a\u043e\u043d\u0447\u0430\u043d\u0438\u0435:", None))
        self.DO_NOT_USE_45.setText(QCoreApplication.translate("MainWindow", u"\u041d\u0430\u0447\u0430\u043b\u043e:", None))
        self.DO_NOT_USE_40.setTabText(self.DO_NOT_USE_40.indexOf(self.DO_NOT_USE_41), QCoreApplication.translate("MainWindow", u"\u041f\u0440\u043e\u0438\u0437\u0432\u043e\u043b\u044c\u043d\u044b\u0439 \u043f\u0435\u0440\u0438\u043e\u0434", None))
        self.DO_NOT_USE_49.setText(QCoreApplication.translate("MainWindow", u"\u041c\u0435\u0441\u044f\u0446:", None))
        self.DO_NOT_USE_51.setText(QCoreApplication.translate("MainWindow", u"\u0413\u043e\u0434:", None))
        self.DO_NOT_USE_40.setTabText(self.DO_NOT_USE_40.indexOf(self.DO_NOT_USE_47), QCoreApplication.translate("MainWindow", u"\u041f\u0435\u0440\u0438\u043e\u0434 \u0438\u0437 \u0441\u043f\u0438\u0441\u043a\u0430", None))
        self.tabWidget_8.setTabText(self.tabWidget_8.indexOf(self.tab_38), QCoreApplication.translate("MainWindow", u"\u0412\u0430\u0448\u0438 \u0438\u0442\u043e\u0433\u0438", None))
        self.pushButton_34.setText(QCoreApplication.translate("MainWindow", u"\u0414\u043e\u0431\u0430\u0432\u0438\u0442\u044c \u0443\u0441\u043b\u043e\u0432\u0438\u044f", None))
        self.btn_serv_you_20.setText(QCoreApplication.translate("MainWindow", u"\u041f\u043e\u0441\u0447\u0438\u0442\u0430\u0442\u044c", None))
        self.DO_NOT_USE_252.setText(QCoreApplication.translate("MainWindow", u"\u041e\u043a\u043e\u043d\u0447\u0430\u043d\u0438\u0435:", None))
        self.DO_NOT_USE_253.setText(QCoreApplication.translate("MainWindow", u"\u041d\u0430\u0447\u0430\u043b\u043e:", None))
        self.DO_NOT_USE_248.setTabText(self.DO_NOT_USE_248.indexOf(self.DO_NOT_USE_249), QCoreApplication.translate("MainWindow", u"\u041f\u0440\u043e\u0438\u0437\u0432\u043e\u043b\u044c\u043d\u044b\u0439 \u043f\u0435\u0440\u0438\u043e\u0434", None))
        self.DO_NOT_USE_257.setText(QCoreApplication.translate("MainWindow", u"\u041c\u0435\u0441\u044f\u0446:", None))
        self.DO_NOT_USE_259.setText(QCoreApplication.translate("MainWindow", u"\u0413\u043e\u0434:", None))
        self.DO_NOT_USE_248.setTabText(self.DO_NOT_USE_248.indexOf(self.DO_NOT_USE_255), QCoreApplication.translate("MainWindow", u"\u041f\u0435\u0440\u0438\u043e\u0434 \u0438\u0437 \u0441\u043f\u0438\u0441\u043a\u0430", None))
        self.label_63.setText(QCoreApplication.translate("MainWindow", u"\u0412\u044b\u0431\u0435\u0440\u0438\u0442\u0435 \u0440\u0430\u0431\u043e\u0442\u043d\u0438\u043a\u0430:", None))
        self.tabWidget_8.setTabText(self.tabWidget_8.indexOf(self.tab_44), QCoreApplication.translate("MainWindow", u"\u0418\u0442\u043e\u0433\u0438 \u043f\u043e \u0440\u0430\u0431\u043e\u0442\u043d\u0438\u043a\u0443", None))
        self.label_65.setText(QCoreApplication.translate("MainWindow", u"\u0424\u0438\u043b\u044c\u0442\u0440:", None))
        self.btn_serv_you_11.setText(QCoreApplication.translate("MainWindow", u"\u041f\u043e\u0441\u0447\u0438\u0442\u0430\u0442\u044c", None))
        self.pushButton_25.setText(QCoreApplication.translate("MainWindow", u"\u0414\u043e\u0431\u0430\u0432\u0438\u0442\u044c \u0443\u0441\u043b\u043e\u0432\u0438\u044f", None))
        self.DO_NOT_USE_122.setText(QCoreApplication.translate("MainWindow", u"\u041e\u043a\u043e\u043d\u0447\u0430\u043d\u0438\u0435:", None))
        self.DO_NOT_USE_123.setText(QCoreApplication.translate("MainWindow", u"\u041d\u0430\u0447\u0430\u043b\u043e:", None))
        self.DO_NOT_USE_118.setTabText(self.DO_NOT_USE_118.indexOf(self.DO_NOT_USE_119), QCoreApplication.translate("MainWindow", u"\u041f\u0440\u043e\u0438\u0437\u0432\u043e\u043b\u044c\u043d\u044b\u0439 \u043f\u0435\u0440\u0438\u043e\u0434", None))
        self.DO_NOT_USE_127.setText(QCoreApplication.translate("MainWindow", u"\u041c\u0435\u0441\u044f\u0446:", None))
        self.DO_NOT_USE_129.setText(QCoreApplication.translate("MainWindow", u"\u0413\u043e\u0434:", None))
        self.DO_NOT_USE_118.setTabText(self.DO_NOT_USE_118.indexOf(self.DO_NOT_USE_125), QCoreApplication.translate("MainWindow", u"\u041f\u0435\u0440\u0438\u043e\u0434 \u0438\u0437 \u0441\u043f\u0438\u0441\u043a\u0430", None))
        self.tabWidget_8.setTabText(self.tabWidget_8.indexOf(self.tab_45), QCoreApplication.translate("MainWindow", u"\u041e\u0431\u0449\u0438\u0435 \u0438\u0442\u043e\u0433\u0438 \u043f\u043e \u0440\u0430\u0431\u043e\u0442\u043d\u0438\u043a\u0430\u043c", None))
        self.tabs_total.setTabText(self.tabs_total.indexOf(self.tab_tot_group), QCoreApplication.translate("MainWindow", u"\u0418\u0442\u043e\u0433\u043e \u0443\u0441\u043b\u0443\u0433 \u0443 \u043b\u044e\u0434\u0435\u0439", None))
        self.label_72.setText(QCoreApplication.translate("MainWindow", u"\u0424\u0438\u043b\u044c\u0442\u0440:", None))
        self.btn_serv_you_16.setText(QCoreApplication.translate("MainWindow", u"\u041f\u043e\u0441\u0447\u0438\u0442\u0430\u0442\u044c", None))
        self.pushButton_30.setText(QCoreApplication.translate("MainWindow", u"\u0414\u043e\u0431\u0430\u0432\u0438\u0442\u044c \u0443\u0441\u043b\u043e\u0432\u0438\u044f", None))
        self.DO_NOT_USE_187.setText(QCoreApplication.translate("MainWindow", u"\u041e\u043a\u043e\u043d\u0447\u0430\u043d\u0438\u0435:", None))
        self.DO_NOT_USE_188.setText(QCoreApplication.translate("MainWindow", u"\u041d\u0430\u0447\u0430\u043b\u043e:", None))
        self.DO_NOT_USE_183.setTabText(self.DO_NOT_USE_183.indexOf(self.DO_NOT_USE_184), QCoreApplication.translate("MainWindow", u"\u041f\u0440\u043e\u0438\u0437\u0432\u043e\u043b\u044c\u043d\u044b\u0439 \u043f\u0435\u0440\u0438\u043e\u0434", None))
        self.DO_NOT_USE_192.setText(QCoreApplication.translate("MainWindow", u"\u041c\u0435\u0441\u044f\u0446:", None))
        self.DO_NOT_USE_194.setText(QCoreApplication.translate("MainWindow", u"\u0413\u043e\u0434:", None))
        self.DO_NOT_USE_183.setTabText(self.DO_NOT_USE_183.indexOf(self.DO_NOT_USE_190), QCoreApplication.translate("MainWindow", u"\u041f\u0435\u0440\u0438\u043e\u0434 \u0438\u0437 \u0441\u043f\u0438\u0441\u043a\u0430", None))
        self.tabWidget_11.setTabText(self.tabWidget_11.indexOf(self.tab_tot_group_dep_2), QCoreApplication.translate("MainWindow", u"\u0418\u0442\u043e\u0433\u0438 \u043f\u043e \u043e\u0442\u0434\u0435\u043b\u0435\u043d\u0438\u044e", None))
        self.label_73.setText(QCoreApplication.translate("MainWindow", u"\u0424\u0438\u043b\u044c\u0442\u0440:", None))
        self.btn_serv_you_17.setText(QCoreApplication.translate("MainWindow", u"\u041f\u043e\u0441\u0447\u0438\u0442\u0430\u0442\u044c", None))
        self.pushButton_31.setText(QCoreApplication.translate("MainWindow", u"\u0414\u043e\u0431\u0430\u0432\u0438\u0442\u044c \u0443\u0441\u043b\u043e\u0432\u0438\u044f", None))
        self.DO_NOT_USE_200.setText(QCoreApplication.translate("MainWindow", u"\u041e\u043a\u043e\u043d\u0447\u0430\u043d\u0438\u0435:", None))
        self.DO_NOT_USE_201.setText(QCoreApplication.translate("MainWindow", u"\u041d\u0430\u0447\u0430\u043b\u043e:", None))
        self.DO_NOT_USE_196.setTabText(self.DO_NOT_USE_196.indexOf(self.DO_NOT_USE_197), QCoreApplication.translate("MainWindow", u"\u041f\u0440\u043e\u0438\u0437\u0432\u043e\u043b\u044c\u043d\u044b\u0439 \u043f\u0435\u0440\u0438\u043e\u0434", None))
        self.DO_NOT_USE_205.setText(QCoreApplication.translate("MainWindow", u"\u041c\u0435\u0441\u044f\u0446:", None))
        self.DO_NOT_USE_207.setText(QCoreApplication.translate("MainWindow", u"\u0413\u043e\u0434:", None))
        self.DO_NOT_USE_196.setTabText(self.DO_NOT_USE_196.indexOf(self.DO_NOT_USE_203), QCoreApplication.translate("MainWindow", u"\u041f\u0435\u0440\u0438\u043e\u0434 \u0438\u0437 \u0441\u043f\u0438\u0441\u043a\u0430", None))
        self.tabWidget_11.setTabText(self.tabWidget_11.indexOf(self.tab_50), QCoreApplication.translate("MainWindow", u"\u0412\u0430\u0448\u0438 \u0438\u0442\u043e\u0433\u0438", None))
        self.pushButton_35.setText(QCoreApplication.translate("MainWindow", u"\u0414\u043e\u0431\u0430\u0432\u0438\u0442\u044c \u0443\u0441\u043b\u043e\u0432\u0438\u044f", None))
        self.btn_serv_you_21.setText(QCoreApplication.translate("MainWindow", u"\u041f\u043e\u0441\u0447\u0438\u0442\u0430\u0442\u044c", None))
        self.DO_NOT_USE_265.setText(QCoreApplication.translate("MainWindow", u"\u041e\u043a\u043e\u043d\u0447\u0430\u043d\u0438\u0435:", None))
        self.DO_NOT_USE_266.setText(QCoreApplication.translate("MainWindow", u"\u041d\u0430\u0447\u0430\u043b\u043e:", None))
        self.DO_NOT_USE_261.setTabText(self.DO_NOT_USE_261.indexOf(self.DO_NOT_USE_262), QCoreApplication.translate("MainWindow", u"\u041f\u0440\u043e\u0438\u0437\u0432\u043e\u043b\u044c\u043d\u044b\u0439 \u043f\u0435\u0440\u0438\u043e\u0434", None))
        self.DO_NOT_USE_270.setText(QCoreApplication.translate("MainWindow", u"\u041c\u0435\u0441\u044f\u0446:", None))
        self.DO_NOT_USE_272.setText(QCoreApplication.translate("MainWindow", u"\u0413\u043e\u0434:", None))
        self.DO_NOT_USE_261.setTabText(self.DO_NOT_USE_261.indexOf(self.DO_NOT_USE_268), QCoreApplication.translate("MainWindow", u"\u041f\u0435\u0440\u0438\u043e\u0434 \u0438\u0437 \u0441\u043f\u0438\u0441\u043a\u0430", None))
        self.label_64.setText(QCoreApplication.translate("MainWindow", u"\u0412\u044b\u0431\u0435\u0440\u0438\u0442\u0435 \u0440\u0430\u0431\u043e\u0442\u043d\u0438\u043a\u0430:", None))
        self.tabWidget_11.setTabText(self.tabWidget_11.indexOf(self.tab_51), QCoreApplication.translate("MainWindow", u"\u0418\u0442\u043e\u0433\u0438 \u043f\u043e \u0440\u0430\u0431\u043e\u0442\u043d\u0438\u043a\u0443", None))
        self.label_76.setText(QCoreApplication.translate("MainWindow", u"\u0424\u0438\u043b\u044c\u0442\u0440:", None))
        self.btn_serv_you_19.setText(QCoreApplication.translate("MainWindow", u"\u041f\u043e\u0441\u0447\u0438\u0442\u0430\u0442\u044c", None))
        self.pushButton_33.setText(QCoreApplication.translate("MainWindow", u"\u0414\u043e\u0431\u0430\u0432\u0438\u0442\u044c \u0443\u0441\u043b\u043e\u0432\u0438\u044f", None))
        self.DO_NOT_USE_226.setText(QCoreApplication.translate("MainWindow", u"\u041e\u043a\u043e\u043d\u0447\u0430\u043d\u0438\u0435:", None))
        self.DO_NOT_USE_228.setText(QCoreApplication.translate("MainWindow", u"\u041d\u0430\u0447\u0430\u043b\u043e:", None))
        self.DO_NOT_USE_222.setTabText(self.DO_NOT_USE_222.indexOf(self.DO_NOT_USE_223), QCoreApplication.translate("MainWindow", u"\u041f\u0440\u043e\u0438\u0437\u0432\u043e\u043b\u044c\u043d\u044b\u0439 \u043f\u0435\u0440\u0438\u043e\u0434", None))
        self.DO_NOT_USE_231.setText(QCoreApplication.translate("MainWindow", u"\u041c\u0435\u0441\u044f\u0446:", None))
        self.DO_NOT_USE_233.setText(QCoreApplication.translate("MainWindow", u"\u0413\u043e\u0434:", None))
        self.DO_NOT_USE_222.setTabText(self.DO_NOT_USE_222.indexOf(self.DO_NOT_USE_229), QCoreApplication.translate("MainWindow", u"\u041f\u0435\u0440\u0438\u043e\u0434 \u0438\u0437 \u0441\u043f\u0438\u0441\u043a\u0430", None))
        self.tabWidget_11.setTabText(self.tabWidget_11.indexOf(self.tab_52), QCoreApplication.translate("MainWindow", u"\u041e\u0431\u0449\u0438\u0435 \u0438\u0442\u043e\u0433\u0438 \u043f\u043e \u0440\u0430\u0431\u043e\u0442\u043d\u0438\u043a\u0430\u043c", None))
        self.tabs_total.setTabText(self.tabs_total.indexOf(self.tab_41), QCoreApplication.translate("MainWindow", u"\u0418\u0442\u043e\u0433\u043e \u0443\u0441\u043b\u0443\u0433/\u043b\u044e\u0434\u0435\u0439", None))
        self.label_68.setText(QCoreApplication.translate("MainWindow", u"\u0424\u0438\u043b\u044c\u0442\u0440:", None))
        self.btn_serv_you_12.setText(QCoreApplication.translate("MainWindow", u"\u041f\u043e\u0441\u0447\u0438\u0442\u0430\u0442\u044c", None))
        self.pushButton_26.setText(QCoreApplication.translate("MainWindow", u"\u0414\u043e\u0431\u0430\u0432\u0438\u0442\u044c \u0443\u0441\u043b\u043e\u0432\u0438\u044f", None))
        self.DO_NOT_USE_135.setText(QCoreApplication.translate("MainWindow", u"\u041e\u043a\u043e\u043d\u0447\u0430\u043d\u0438\u0435:", None))
        self.DO_NOT_USE_137.setText(QCoreApplication.translate("MainWindow", u"\u041d\u0430\u0447\u0430\u043b\u043e:", None))
        self.DO_NOT_USE_131.setTabText(self.DO_NOT_USE_131.indexOf(self.DO_NOT_USE_132), QCoreApplication.translate("MainWindow", u"\u041f\u0440\u043e\u0438\u0437\u0432\u043e\u043b\u044c\u043d\u044b\u0439 \u043f\u0435\u0440\u0438\u043e\u0434", None))
        self.DO_NOT_USE_140.setText(QCoreApplication.translate("MainWindow", u"\u041c\u0435\u0441\u044f\u0446:", None))
        self.DO_NOT_USE_142.setText(QCoreApplication.translate("MainWindow", u"\u0413\u043e\u0434:", None))
        self.DO_NOT_USE_131.setTabText(self.DO_NOT_USE_131.indexOf(self.DO_NOT_USE_138), QCoreApplication.translate("MainWindow", u"\u041f\u0435\u0440\u0438\u043e\u0434 \u0438\u0437 \u0441\u043f\u0438\u0441\u043a\u0430", None))
        self.tabWidget_9.setTabText(self.tabWidget_9.indexOf(self.tab_46), QCoreApplication.translate("MainWindow", u"\u0421\u043f\u0438\u0441\u043a\u0438 \u043b\u044e\u0434\u0435\u0439 \u0441 \u043a\u0430\u0442\u0435\u0433\u043e\u0440\u0438\u044f\u043c\u0438", None))
        self.label_71.setText(QCoreApplication.translate("MainWindow", u"\u0424\u0438\u043b\u044c\u0442\u0440:", None))
        self.btn_serv_you_14.setText(QCoreApplication.translate("MainWindow", u"\u041f\u043e\u0441\u0447\u0438\u0442\u0430\u0442\u044c", None))
        self.pushButton_28.setText(QCoreApplication.translate("MainWindow", u"\u0414\u043e\u0431\u0430\u0432\u0438\u0442\u044c \u0443\u0441\u043b\u043e\u0432\u0438\u044f", None))
        self.DO_NOT_USE_161.setText(QCoreApplication.translate("MainWindow", u"\u041e\u043a\u043e\u043d\u0447\u0430\u043d\u0438\u0435:", None))
        self.DO_NOT_USE_163.setText(QCoreApplication.translate("MainWindow", u"\u041d\u0430\u0447\u0430\u043b\u043e:", None))
        self.DO_NOT_USE_157.setTabText(self.DO_NOT_USE_157.indexOf(self.DO_NOT_USE_158), QCoreApplication.translate("MainWindow", u"\u041f\u0440\u043e\u0438\u0437\u0432\u043e\u043b\u044c\u043d\u044b\u0439 \u043f\u0435\u0440\u0438\u043e\u0434", None))
        self.DO_NOT_USE_166.setText(QCoreApplication.translate("MainWindow", u"\u041c\u0435\u0441\u044f\u0446:", None))
        self.DO_NOT_USE_168.setText(QCoreApplication.translate("MainWindow", u"\u0413\u043e\u0434:", None))
        self.DO_NOT_USE_157.setTabText(self.DO_NOT_USE_157.indexOf(self.DO_NOT_USE_164), QCoreApplication.translate("MainWindow", u"\u041f\u0435\u0440\u0438\u043e\u0434 \u0438\u0437 \u0441\u043f\u0438\u0441\u043a\u0430", None))
        self.tabWidget_9.setTabText(self.tabWidget_9.indexOf(self.tab_47), QCoreApplication.translate("MainWindow", u"\u0418\u0442\u043e\u0433\u0438 \u0443\u0441\u043b\u0443\u0433 \u043f\u043e \u043a\u0430\u0442\u0435\u0433\u043e\u0440\u0438\u044f\u043c", None))
        self.label_69.setText(QCoreApplication.translate("MainWindow", u"\u0424\u0438\u043b\u044c\u0442\u0440:", None))
        self.btn_serv_you_13.setText(QCoreApplication.translate("MainWindow", u"\u041f\u043e\u0441\u0447\u0438\u0442\u0430\u0442\u044c", None))
        self.pushButton_27.setText(QCoreApplication.translate("MainWindow", u"\u0414\u043e\u0431\u0430\u0432\u0438\u0442\u044c \u0443\u0441\u043b\u043e\u0432\u0438\u044f", None))
        self.DO_NOT_USE_148.setText(QCoreApplication.translate("MainWindow", u"\u041e\u043a\u043e\u043d\u0447\u0430\u043d\u0438\u0435:", None))
        self.DO_NOT_USE_150.setText(QCoreApplication.translate("MainWindow", u"\u041d\u0430\u0447\u0430\u043b\u043e:", None))
        self.DO_NOT_USE_144.setTabText(self.DO_NOT_USE_144.indexOf(self.DO_NOT_USE_145), QCoreApplication.translate("MainWindow", u"\u041f\u0440\u043e\u0438\u0437\u0432\u043e\u043b\u044c\u043d\u044b\u0439 \u043f\u0435\u0440\u0438\u043e\u0434", None))
        self.DO_NOT_USE_153.setText(QCoreApplication.translate("MainWindow", u"\u041c\u0435\u0441\u044f\u0446:", None))
        self.DO_NOT_USE_155.setText(QCoreApplication.translate("MainWindow", u"\u0413\u043e\u0434:", None))
        self.DO_NOT_USE_144.setTabText(self.DO_NOT_USE_144.indexOf(self.DO_NOT_USE_151), QCoreApplication.translate("MainWindow", u"\u041f\u0435\u0440\u0438\u043e\u0434 \u0438\u0437 \u0441\u043f\u0438\u0441\u043a\u0430", None))
        self.tabWidget_9.setTabText(self.tabWidget_9.indexOf(self.tab_10), QCoreApplication.translate("MainWindow", u"\u0412\u043f\u0435\u0440\u0432\u044b\u0435 \u0432 \u0433\u043e\u0434\u0443 \u0432 \u043f\u0435\u0440\u0438\u043e\u0434", None))
        self.tabs_total.setTabText(self.tabs_total.indexOf(self.tab_16), QCoreApplication.translate("MainWindow", u"\u041f\u043e \u043a\u0430\u0442\u0435\u0433\u043e\u0440\u0438\u044f\u043c \u043b\u044e\u0434\u0435\u0439", None))
        self.tabWidget_10.setTabText(self.tabWidget_10.indexOf(self.tab_48), QCoreApplication.translate("MainWindow", u"\u041a\u0430\u0442\u0435\u0433\u043e\u0440\u0438\u0438 ", None))
        self.tabWidget_10.setTabText(self.tabWidget_10.indexOf(self.tab_49), QCoreApplication.translate("MainWindow", u"Tab 2", None))
        self.tabs_total.setTabText(self.tabs_total.indexOf(self.tab_20), QCoreApplication.translate("MainWindow", u"\u041a\u0430\u0442\u0435\u0433\u043e\u0440\u0438\u0438 \u0443\u0441\u043b\u0443\u0433 \u043e\u0442\u0434\u0435\u043b\u0435\u043d\u0438\u044f", None))
        self.tabs_total.setTabText(self.tabs_total.indexOf(self.tab_13), QCoreApplication.translate("MainWindow", u"\u0421\u0432\u043e\u0434\u043d\u044b\u0435 \u043e\u0442\u0447\u0435\u0442\u044b", None))
        self.tabMain.setTabText(self.tabMain.indexOf(self.tab_total), QCoreApplication.translate("MainWindow", u"\u0418\u0442\u043e\u0433\u0438", None))
        self.label_serv_year.setText(QCoreApplication.translate("MainWindow", u"\u041f\u043e\u043a\u0430\u0437\u0430\u043d\u044b \u0443\u0441\u043b\u0443\u0433\u0438 \u0432 \u0433\u043e\u0434\u0443:", None))
#if QT_CONFIG(tooltip)
        self.btn_add_services_for_new_year.setToolTip(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-weight:600;\">\u0414\u043e\u0431\u0430\u0432\u0438\u0442\u044c \u0441\u043f\u0438\u0441\u043e\u043a \u0443\u0441\u043b\u0443\u0433:</span></p><p><br/></p><p>\u0418\u0441\u043f\u043e\u043b\u044c\u0437\u0443\u0439\u0442\u0435 \u043a\u0430\u0436\u0434\u044b\u0439 \u0440\u0430\u0437 \u043a\u043e\u0433\u0434\u0430 \u0432\u044b\u0445\u043e\u0434\u0438\u0442 \u043d\u043e\u0432\u044b\u0439(\u043e\u0431\u043d\u043e\u0432\u043b\u044f\u0435\u0442\u0441\u044f) \u043f\u0435\u0440\u0435\u0447\u0435\u043d\u044c \u0443\u0441\u043b\u0443\u0433.</p><p>\u0414\u0430\u043d\u043d\u0430\u044f \u043a\u043d\u043e\u043f\u043a\u0430 \u0441\u043e\u0437\u0434\u0430\u0435\u0442 \u043f\u0435\u0440\u0435\u0447\u0435\u043d\u044c \u0443\u0441\u043b\u0443\u0433 \u043d\u0430 \u0433\u043e\u0434 \u0438\u0437 \u043f\u0435\u0440\u0435\u0447\u043d\u044f \u043f\u043e\u0441\u043b\u0435\u0434\u043d\u0435\u0433\u043e \u0433\u043e\u0434\u0430,</p><p>\u043f\u0440\u0438 \u044d\u0442\u043e\u043c, \u043f\u0440\u0435\u0434"
                        "\u044b\u0434\u0443\u044e\u0449\u0438\u0439 \u043f\u0435\u0440\u0435\u0447\u0435\u043d\u044c \u0430\u0440\u0445\u0438\u0432\u0438\u0440\u0443\u0435\u0442\u0441\u044f(\u043f\u043e\u043b\u044c\u0437\u043e\u0432\u0430\u0442\u0435\u043b\u0438 \u043d\u0435 \u0441\u043c\u043e\u0433\u0443\u0442 \u0432\u0432\u0435\u0441\u0442\u0438 \u0443\u0441\u043b\u0443\u0433\u0438 \u043f\u0440\u0435\u0434\u044b\u0434\u0443\u0449\u0435\u0433\u043e \u043f\u0435\u0440\u0435\u0447\u043d\u044f). </p><p><span style=\" font-weight:600;\">\u0412\u043d\u0438\u043c\u0430\u043d\u0438\u0435!</span> \u0421\u043f\u0438\u0441\u043a\u0438 \u0443\u0441\u043b\u0443\u0433 \u0432 \u0440\u0438\u043f\u0441\u043e \u0438 \u0441\u043f\u0438\u0441\u043a\u0438 \u0443\u0441\u043b\u0443\u0433 \u043f\u043e\u043b\u043e\u0436\u0435\u043d\u043d\u044b\u0445 \u043f\u043e \u0434\u043e\u0433\u043e\u0432\u043e\u0440\u0443 \u0431\u0443\u0434\u0443\u0442 \u043e\u0431\u043d\u043e\u0432\u043b\u0435\u043d\u044b! \u041d\u043e \u0443\u0436\u0435 \u0432\u0432\u0435\u0434\u0435"
                        "\u043d\u043d\u044b\u0435 \u0443\u0441\u043b\u0443\u0433\u0438 \u043e\u0431\u043d\u043e\u0432\u043b\u0435\u043d\u044b \u041d\u0415 \u0431\u0443\u0434\u0443\u0442. </p><p><br/></p><p>\u041f\u0440\u0438\u043c\u0435\u0447\u0430\u043d\u0438\u0435: \u0435\u0441\u043b\u0438 \u0432\u044b \u043c\u0435\u043d\u044f\u0435\u0442\u0435 \u0441\u043f\u0438\u0441\u043e\u043a \u0432 \u0441\u0435\u0440\u0435\u0434\u0438\u043d\u0435 \u0433\u043e\u0434\u0430(\u043d\u0430\u043f\u0440\u0438\u043c\u0435\u0440 \u0438\u0437\u043c\u0435\u043d\u0438\u043b\u0430\u0441\u044c \u0441\u0442\u043e\u0438\u043c\u043e\u0441\u0442\u044c), \u0442\u043e \u0432 \u043e\u0442\u0447\u0435\u0442\u0430\u0445 \u0434\u0430\u043d\u043d\u044b\u0435 \u0443\u0441\u043b\u0443\u0433\u0438 \u0431\u0443\u0434\u0443\u0442 \u043f\u0435\u0440\u0435\u0447\u0438\u0441\u043b\u0435\u043d\u044b \u0434\u0432\u0430\u0436\u0434\u044b. </p><p><br/></p><p><br/></p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.btn_add_services_for_new_year.setText(QCoreApplication.translate("MainWindow", u"\u0414\u043e\u0431\u0430\u0432\u0438\u0442 \u0443\u0441\u043b\u0443\u0433\u0438 \u0434\u043b\u044f \u0441\u043b\u0435\u0434\u0443\u044e\u0449\u0435\u0433\u043e \u0433\u043e\u0434\u0430", None))
        self.tabs_admin.setTabText(self.tabs_admin.indexOf(self.tab_serv), QCoreApplication.translate("MainWindow", u"\u041f\u0435\u0440\u0435\u0447\u0435\u043d\u044c \u0443\u0441\u043b\u0443\u0433 \u0438 \u0438\u0445 \u0441\u0442\u043e\u0438\u043c\u043e\u0441\u0442\u044c", None))
        self.label_10.setText(QCoreApplication.translate("MainWindow", u"\u0421\u043f\u0438\u0441\u043e\u043a \u0420\u0418\u041f\u0421\u041e \u0443\u0447\u0440\u0435\u0436\u0434\u0435\u043d\u0438\u044f", None))
        self.label_11.setText(QCoreApplication.translate("MainWindow", u"\u0421\u043f\u0438\u0441\u043e\u043a \u0443\u0441\u043b\u0443\u0433 \u0432\u044b\u0431\u0440\u0430\u043d\u043d\u043e\u0433\u043e \u0420\u0418\u041f\u0421\u041e", None))
        self.tabs_admin.setTabText(self.tabs_admin.indexOf(self.tab_ripso), QCoreApplication.translate("MainWindow", u"\u041f\u0435\u0440\u0435\u0447\u0435\u043d\u044c \u0420\u0418\u041f\u0421\u041e", None))
        self.label_13.setText(QCoreApplication.translate("MainWindow", u"\u0421\u043f\u0438\u0441\u043e\u043a \u0440\u0430\u0431\u043e\u0442\u043d\u0438\u043a\u043e\u0432:", None))
        self.label_14.setText(QCoreApplication.translate("MainWindow", u"\u0414\u043e\u043b\u0436\u043d\u043e\u0441\u0442\u0438 \u0440\u0430\u0431\u043e\u0442\u043d\u0438\u043a\u0430 \u043d\u0430 \u043e\u0442\u0434\u0435\u043b\u0435\u043d\u0438\u0438:", None))
        self.btn_show_qrcode.setText(QCoreApplication.translate("MainWindow", u"QR \u043a\u043e\u0434 \u0440\u0430\u0431\u043e\u0442\u043d\u0438\u043a\u0430 \u043e\u0442\u0434\u0435\u043b\u0435\u043d\u0438\u044f", None))
        self.tabs_admin.setTabText(self.tabs_admin.indexOf(self.tab_workers), QCoreApplication.translate("MainWindow", u"\u0420\u0430\u0431\u043e\u0442\u043d\u0438\u043a\u0438", None))
        self.btn_pw_gen.setText(QCoreApplication.translate("MainWindow", u"\u0421\u0433\u0435\u043d\u0435\u0440\u0438\u0440\u043e\u0432\u0430\u0442\u044c \u043f\u0430\u0440\u043e\u043b\u044c", None))
        self.btn_update_login_pass.setText(QCoreApplication.translate("MainWindow", u"\u041e\u0431\u043d\u043e\u0432\u0438\u0442\u044c \u043b\u043e\u0433\u0438\u043d \u0438 \u043f\u0430\u0440\u043e\u043b\u044c \u0441\u043e\u0442\u0440\u0443\u0434\u043d\u0438\u043a\u0430", None))
        self.btnClean.setText(QCoreApplication.translate("MainWindow", u"\u041e\u0447\u0438\u0441\u0442\u0438\u0442\u044c", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"\u041f\u0430\u0440\u043e\u043b\u044c:", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"\u041b\u043e\u0433\u0438\u043d:", None))
        self.label_31.setText(QCoreApplication.translate("MainWindow", u"\u041f\u0440\u0430\u0432\u0430 \u0434\u043e\u0441\u0442\u0443\u043f\u0430:", None))
        self.lineEdit_pass.setText("")
        self.lineEdit_pass.setPlaceholderText(QCoreApplication.translate("MainWindow", u"\u0421\u043e\u0437\u0434\u0430\u0439\u0442\u0435 \u043d\u043e\u0432\u044b\u0439 \u043f\u0430\u0440\u043e\u043b\u044c \u043d\u0430\u0436\u0430\u0432 \u043d\u0430 \u043a\u043d\u043e\u043f\u043a\u0443 \u0421\u0433\u0435\u043d\u0435\u0440\u0438\u0440\u043e\u0432\u0430\u0442\u044c \u043f\u0430\u0440\u043e\u043b\u044c", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"\u0420\u0430\u0431\u043e\u0442\u043d\u0438\u043a:", None))
        self.lineEdit_login.setInputMask("")
        self.lineEdit_login.setText("")
        self.lineEdit_login.setPlaceholderText(QCoreApplication.translate("MainWindow", u"\u0412\u0432\u0435\u0434\u0438\u0442\u0435 \u043b\u043e\u0433\u0438\u043d - \u0442\u043e\u043b\u044c\u043a\u043e \u043b\u0430\u0442\u0438\u043d\u0441\u043a\u0438\u0435 \u0431\u0443\u043a\u0432\u044b", None))
        self.label_75.setText(QCoreApplication.translate("MainWindow", u"\u0412\u044b\u0434\u0430\u0447\u0430 \u043f\u0430\u0440\u043e\u043b\u044f \u0434\u043b\u044f \u043f\u043e\u043b\u044c\u0437\u043e\u0432\u0430\u0442\u0435\u043b\u0435\u0439 \u043f\u043e\u043b\u043d\u043e\u0439(\u043d\u0435 \u043c\u043e\u0431\u0438\u043b\u044c\u043d\u043e\u0439) \u0432\u0435\u0440\u0441\u0438\u0438 \u043f\u0440\u043e\u0433\u0440\u0430\u043c\u043c\u044b:", None))
        self.tabs_admin.setTabText(self.tabs_admin.indexOf(self.tab_password), QCoreApplication.translate("MainWindow", u"\u0412\u044b\u0434\u0430\u0447\u0430 \u043f\u0430\u0440\u043e\u043b\u044f", None))
        self.label_15.setText(QCoreApplication.translate("MainWindow", u"\u0421\u043f\u0438\u0441\u043e\u043a \u043e\u0442\u0434\u0435\u043b\u0435\u043d\u0438\u0439:", None))
        self.label_16.setText(QCoreApplication.translate("MainWindow", u"\u0420\u0438\u043f\u0441\u043e \u043e\u0442\u0434\u0435\u043b\u0435\u043d\u0438\u044f:", None))
        self.label_17.setText(QCoreApplication.translate("MainWindow", u"\u0420\u0430\u0431\u043e\u0442\u043d\u0438\u043a\u0438 \u043e\u0442\u0434\u0435\u043b\u0435\u043d\u0438\u044f:", None))
        self.tabs_admin.setTabText(self.tabs_admin.indexOf(self.tab_dep), QCoreApplication.translate("MainWindow", u"\u041e\u0442\u0434\u0435\u043b\u0435\u043d\u0438\u044f", None))
        self.label_28.setText(QCoreApplication.translate("MainWindow", u"\u0415\u0441\u043b\u0438 \u0440\u0430\u0431\u043e\u0442\u043d\u0438\u043a\u0430 \u043d\u0435\u0442 \u0432 \u0441\u043f\u0438\u0441\u043a\u0435, \u0437\u043d\u0430\u0447\u0438\u0442 \u0443 \u043d\u0435\u0433\u043e \u043d\u0435\u0442 \u043b\u043e\u0433\u0438\u043d\u0430/\u043f\u0430\u0440\u043e\u043b\u044f", None))
        self.label_26.setText(QCoreApplication.translate("MainWindow", u"\u0421\u043f\u0438\u0441\u043e\u043a \u0440\u0430\u0431\u043e\u0442\u043d\u0438\u043a\u043e\u0432 \u0441 \u043f\u0430\u0440\u043e\u043b\u044f\u043c\u0438", None))
        self.label_29.setText(QCoreApplication.translate("MainWindow", u"\u0414\u043e\u043b\u0436\u043d\u043e\u0441\u0442\u044c \u0438 \u0440\u043e\u043b\u044c \u043d\u0430 \u043e\u0442\u0434\u0435\u043b\u0435\u043d\u0438\u0438:", None))
        self.tabs_admin.setTabText(self.tabs_admin.indexOf(self.tab_roles), QCoreApplication.translate("MainWindow", u"\u041f\u0440\u0430\u0432\u0430 \u0434\u043e\u0441\u0442\u0443\u043f\u0430", None))
        self.tabs_admin.setTabText(self.tabs_admin.indexOf(self.tab_37), QCoreApplication.translate("MainWindow", u"\u041f\u0440\u043e\u0436\u0438\u0442\u043e\u0447\u043d\u044b\u0439 \u043c\u0438\u043d\u0438\u043c\u0443\u043c", None))
        self.label_30.setText(QCoreApplication.translate("MainWindow", u"\u041e\u0431\u0449\u0438\u0435 \u043d\u0430\u0441\u0442\u0440\u043e\u0439\u043a\u0438 \u0434\u043b\u044f \u0432\u0441\u0435\u0439 \u0411\u0430\u0437\u044b \u0414\u0430\u043d\u043d\u044b\u0445", None))
        self.tabs_admin.setTabText(self.tabs_admin.indexOf(self.tab_settings), QCoreApplication.translate("MainWindow", u"\u041d\u0430\u0441\u0442\u0440\u043e\u0439\u043a\u0438 \u0411\u0414", None))
        self.label_12.setText(QCoreApplication.translate("MainWindow", u"\u0421\u043f\u0438\u0441\u043e\u043a \u0441\u043e\u043e\u0431\u0449\u0435\u043d\u0438\u0439 \u043f\u043e\u043a\u0430\u0437\u044b\u0432\u0430\u0435\u043c\u044b\u0445 \u043f\u0440\u0438 \u043e\u0442\u043a\u0440\u044b\u0442\u0438\u0438 \u044d\u0442\u043e\u0439 \u043f\u0440\u043e\u0433\u0440\u0430\u043c\u043c\u044b: \u0431\u0443\u0434\u0443\u0442 \u043f\u043e\u043a\u0430\u0437\u0430\u043d\u044b\n"
"                                       \u0442\u043e\u043b\u044c\u043a\u043e \u0430\u043a\u0442\u0438\u0432\u043d\u044b\u0435, \u043e\u0441\u0442\u0430\u043b\u044c\u043d\u044b\u0435 - \u0430\u0440\u0445\u0438\u0432\n"
"                                   ", None))
        self.tabs_admin.setTabText(self.tabs_admin.indexOf(self.tab_notifies), QCoreApplication.translate("MainWindow", u"\u0421\u043e\u043e\u0431\u0449\u0435\u043d\u0438\u044f", None))
        self.tabs_admin.setTabText(self.tabs_admin.indexOf(self.tab_holiday), QCoreApplication.translate("MainWindow", u"\u0412\u044b\u0445\u043e\u0434\u043d\u044b\u0435 \u0434\u043d\u0438", None))
        self.pushButton_5.setText(QCoreApplication.translate("MainWindow", u"\u0438\u043c\u043f\u043e\u0440\u0442 \u0438\u0437 \u0444\u0430\u0439\u043b\u0430", None))
        self.pushButton_6.setText(QCoreApplication.translate("MainWindow", u"\u0424\u0438\u043b\u044c\u0442\u0440", None))
        self.tabs_admin.setTabText(self.tabs_admin.indexOf(self.tab_26), QCoreApplication.translate("MainWindow", u"\u0412\u0432\u043e\u0434 \u0434\u0430\u043d\u043d\u044b\u0445 \u043e\u0431 \u043e\u043f\u043b\u0430\u0442\u0435", None))
        self.btn_check_sql.setText(QCoreApplication.translate("MainWindow", u"\u0412\u044b\u043f\u043e\u043b\u043d\u0438\u0442\u044c", None))
        self.tabs_admin.setTabText(self.tabs_admin.indexOf(self.tab_sql_check), QCoreApplication.translate("MainWindow", u"SQL \u043f\u0440\u043e\u0432\u0435\u0440\u043a\u0430", None))
        self.label_18.setText(QCoreApplication.translate("MainWindow", u"\u041e\u0442\u0434\u0435\u043b\u0435\u043d\u0438\u044f:", None))
        self.label_9.setText(QCoreApplication.translate("MainWindow", u"\u0413\u0440\u0443\u043f\u043f\u044b \u043e\u0442\u0434\u0435\u043b\u0435\u043d\u0438\u0439:", None))
        self.tabs_admin.setTabText(self.tabs_admin.indexOf(self.tab_3), QCoreApplication.translate("MainWindow", u"\u0413\u0440\u0443\u043f\u043f\u044b \u043e\u0442\u0434\u0435\u043b\u0435\u043d\u0438\u0439", None))
        self.tabMain.setTabText(self.tabMain.indexOf(self.tab_admin), QCoreApplication.translate("MainWindow", u"\u0410\u0434\u043c\u0438\u043d\u0438\u0441\u0442\u0440\u0438\u0440\u043e\u0432\u0430\u043d\u0438\u0435", None))
        self.pushButton_24.setText(QCoreApplication.translate("MainWindow", u"PushButton", None))
        self.pushButton_32.setText(QCoreApplication.translate("MainWindow", u"\u041e\u0442\u043c\u0435\u043d\u0438\u0442\u044c \u0432\u044b\u0431\u0440\u0430\u043d\u043d\u043e\u0435", None))
        self.pushButton_16.setText(QCoreApplication.translate("MainWindow", u"\u0421\u043e\u0445\u0440\u0430\u043d\u0438\u0442\u044c \u0432\u044b\u0431\u0440\u0430\u043d\u043d\u044b\u0435", None))
        self.tabMain.setTabText(self.tabMain.indexOf(self.tab_journal), QCoreApplication.translate("MainWindow", u"\u0416\u0443\u0440\u043d\u0430\u043b \u0440\u0430\u0431\u043e\u0442\u044b", None))
        self.tabMain.setTabText(self.tabMain.indexOf(self.tab_pyc), QCoreApplication.translate("MainWindow", u"\u041f\u0423\u041a\u0414\u0421\u0421\u041e", None))
        self.pushButton_29.setText(QCoreApplication.translate("MainWindow", u"\u0414\u043e\u0431\u0430\u0432\u0438\u0442\u044c \u0443\u0441\u043b\u043e\u0432\u0438\u044f", None))
        self.btn_serv_you_15.setText(QCoreApplication.translate("MainWindow", u"\u041f\u043e\u0441\u0447\u0438\u0442\u0430\u0442\u044c", None))
        self.DO_NOT_USE_174.setText(QCoreApplication.translate("MainWindow", u"\u041e\u043a\u043e\u043d\u0447\u0430\u043d\u0438\u0435:", None))
        self.DO_NOT_USE_175.setText(QCoreApplication.translate("MainWindow", u"\u041d\u0430\u0447\u0430\u043b\u043e:", None))
        self.DO_NOT_USE_170.setTabText(self.DO_NOT_USE_170.indexOf(self.DO_NOT_USE_171), QCoreApplication.translate("MainWindow", u"\u041f\u0440\u043e\u0438\u0437\u0432\u043e\u043b\u044c\u043d\u044b\u0439 \u043f\u0435\u0440\u0438\u043e\u0434", None))
        self.DO_NOT_USE_179.setText(QCoreApplication.translate("MainWindow", u"\u041c\u0435\u0441\u044f\u0446:", None))
        self.DO_NOT_USE_181.setText(QCoreApplication.translate("MainWindow", u"\u0413\u043e\u0434:", None))
        self.DO_NOT_USE_170.setTabText(self.DO_NOT_USE_170.indexOf(self.DO_NOT_USE_177), QCoreApplication.translate("MainWindow", u"\u041f\u0435\u0440\u0438\u043e\u0434 \u0438\u0437 \u0441\u043f\u0438\u0441\u043a\u0430", None))
        self.tabMain.setTabText(self.tabMain.indexOf(self.tab_export), QCoreApplication.translate("MainWindow", u"\u042d\u043a\u0441\u043f\u043e\u0440\u0442 \u0443\u0441\u043b\u0443\u0433", None))
        self.menu.setTitle(QCoreApplication.translate("MainWindow", u"\u0411\u0430\u0437\u0430 \u0434\u0430\u043d\u043d\u044b\u0445", None))
        self.menu_2.setTitle(QCoreApplication.translate("MainWindow", u"\u041f\u0435\u0440\u0435\u0439\u0442\u0438 \u043a", None))
        self.menu_3.setTitle(QCoreApplication.translate("MainWindow", u"\u041f\u0435\u0447\u0430\u0442\u044c \u0434\u043e\u043a\u0443\u043c\u0435\u043d\u0442\u043e\u0432", None))
        self.menu_settings.setTitle(QCoreApplication.translate("MainWindow", u"&\u041d\u0430\u0441\u0442\u0440\u043e\u0439\u043a\u0438", None))
        self.menu_5.setTitle(QCoreApplication.translate("MainWindow", u"\u0421\u043f\u0440\u0430\u0432\u043a\u0430", None))
        self.menu_7.setTitle(QCoreApplication.translate("MainWindow", u"\u041f\u0440\u0430\u0432\u043a\u0430", None))
        self.menu_4.setTitle(QCoreApplication.translate("MainWindow", u"\u0421\u043e\u0437\u0434\u0430\u0442\u044c", None))
        self.toolBar.setWindowTitle(QCoreApplication.translate("MainWindow", u"toolBar", None))
        self.toolBar_2.setWindowTitle(QCoreApplication.translate("MainWindow", u"toolBar_2", None))
        self.dock_people_info.setWindowTitle(QCoreApplication.translate("MainWindow", u"\u0418\u043d\u0444\u043e\u0440\u043c\u0430\u0446\u0438\u044f:", None))
        self.label_79.setText(QCoreApplication.translate("MainWindow", u"\u0424\u043e\u0440\u043c\u0430 \u0441\u043e\u0446. \u043e\u0431\u0441\u043b\u0436\u0438\u0432\u0430\u043d\u0438\u044f:", None))
        self.label_82.setText(QCoreApplication.translate("MainWindow", u"\u041a \u043e\u043f\u043b\u0430\u0442\u0435:", None))
        self.label_80.setText(QCoreApplication.translate("MainWindow", u"\u041c\u0435\u0441\u044f\u0446, \u043f\u0440\u043e\u0446\u0435\u043d\u0442\u044b:", None))
        self.pushButton_13.setText(QCoreApplication.translate("MainWindow", u"-", None))
        self.pushButton_14.setText(QCoreApplication.translate("MainWindow", u"+", None))
        self.label_78.setText(QCoreApplication.translate("MainWindow", u"\u0414\u043e\u0433\u043e\u0432\u043e\u0440(\u044b):", None))
        self.label_77.setText(QCoreApplication.translate("MainWindow", u"\u0424\u0418\u041e:", None))
        self.label_81.setText(QCoreApplication.translate("MainWindow", u"\u041e\u043a\u0430\u0437\u0430\u043d\u043e \u0443\u0441\u043b\u0443\u0433:", None))
        self.label_89.setText(QCoreApplication.translate("MainWindow", u"\u0421\u0414\u0414:", None))
    # retranslateUi

