# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'qcSelectReport.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *

from widgets.custumQWidgets import myQTabWidget
from widgets.custumQWidgets import qcSelectPeriod
from widgets.custumQWidgets import stubQTableView


class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(842, 485)
        self.gridLayout = QGridLayout(Form)
        self.gridLayout.setObjectName(u"gridLayout")
        self.qcFrame = QFrame(Form)
        self.qcFrame.setObjectName(u"qcFrame")
        self.qcFrame.setFrameShape(QFrame.StyledPanel)
        self.qcFrame.setFrameShadow(QFrame.Raised)
        self.gridLayout_2 = QGridLayout(self.qcFrame)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.gridLayout_42 = QGridLayout()
        self.gridLayout_42.setObjectName(u"gridLayout_42")
        self.label = QLabel(self.qcFrame)
        self.label.setObjectName(u"label")

        self.gridLayout_42.addWidget(self.label, 1, 2, 1, 1)

        self.table = stubQTableView(self.qcFrame)
        self.table.setObjectName(u"table")
        self.table.setAlternatingRowColors(True)

        self.gridLayout_42.addWidget(self.table, 2, 0, 1, 4)

        self.period = qcSelectPeriod(self.qcFrame)
        self.period.setObjectName(u"period")
        self.verticalLayout_28 = QVBoxLayout(self.period)
        self.verticalLayout_28.setObjectName(u"verticalLayout_28")
        self.DO_NOT_USE_14 = myQTabWidget(self.period)
        self.DO_NOT_USE_14.setObjectName(u"DO_NOT_USE_14")
        sizePolicy = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.DO_NOT_USE_14.sizePolicy().hasHeightForWidth())
        self.DO_NOT_USE_14.setSizePolicy(sizePolicy)
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
        sizePolicy1 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.DO_NOT_USE_18.sizePolicy().hasHeightForWidth())
        self.DO_NOT_USE_18.setSizePolicy(sizePolicy1)
        self.DO_NOT_USE_18.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.DO_NOT_USE_16.addWidget(self.DO_NOT_USE_18, 1, 0, 1, 1)

        self.DO_NOT_USE_19 = QLabel(self.DO_NOT_USE_15)
        self.DO_NOT_USE_19.setObjectName(u"DO_NOT_USE_19")
        sizePolicy1.setHeightForWidth(self.DO_NOT_USE_19.sizePolicy().hasHeightForWidth())
        self.DO_NOT_USE_19.setSizePolicy(sizePolicy1)
        self.DO_NOT_USE_19.setLayoutDirection(Qt.LeftToRight)
        self.DO_NOT_USE_19.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.DO_NOT_USE_16.addWidget(self.DO_NOT_USE_19, 0, 0, 1, 1)

        self.DO_NOT_USE_20 = QDateEdit(self.DO_NOT_USE_15)
        self.DO_NOT_USE_20.setObjectName(u"DO_NOT_USE_20")

        self.DO_NOT_USE_16.addWidget(self.DO_NOT_USE_20, 0, 1, 1, 1)

        self.DO_NOT_USE_16.setColumnStretch(0, 1)
        self.DO_NOT_USE_16.setColumnStretch(1, 2)

        self.verticalLayout_62.addLayout(self.DO_NOT_USE_16)

        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_62.addItem(self.verticalSpacer_2)

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

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_63.addItem(self.verticalSpacer)

        self.DO_NOT_USE_14.addTab(self.DO_NOT_USE_21, "")

        self.verticalLayout_28.addWidget(self.DO_NOT_USE_14)


        self.gridLayout_42.addWidget(self.period, 0, 0, 1, 1)

        self.lineEdit = QLineEdit(self.qcFrame)
        self.lineEdit.setObjectName(u"lineEdit")

        self.gridLayout_42.addWidget(self.lineEdit, 1, 3, 1, 1)

        self.btn_add_filter = QPushButton(self.qcFrame)
        self.btn_add_filter.setObjectName(u"btn_add_filter")

        self.gridLayout_42.addWidget(self.btn_add_filter, 1, 1, 1, 1)

        self.btn_count = QPushButton(self.qcFrame)
        self.btn_count.setObjectName(u"btn_count")

        self.gridLayout_42.addWidget(self.btn_count, 1, 0, 1, 1)

        self.tabWidget = myQTabWidget(self.qcFrame)
        self.tabWidget.setObjectName(u"tabWidget")
        self.tab_data = QWidget()
        self.tab_data.setObjectName(u"tab_data")
        self.tabWidget.addTab(self.tab_data, "")
        self.tab_where = QWidget()
        self.tab_where.setObjectName(u"tab_where")
        self.tabWidget.addTab(self.tab_where, "")
        self.tab_filter = QWidget()
        self.tab_filter.setObjectName(u"tab_filter")
        self.tabWidget.addTab(self.tab_filter, "")

        self.gridLayout_42.addWidget(self.tabWidget, 0, 1, 1, 3)

        self.gridLayout_42.setRowStretch(0, 1)
        self.gridLayout_42.setRowStretch(2, 5)

        self.gridLayout_2.addLayout(self.gridLayout_42, 0, 0, 1, 1)


        self.gridLayout.addWidget(self.qcFrame, 0, 0, 1, 1)


        self.retranslateUi(Form)
        self.lineEdit.textChanged.connect(self.table.set_first_filter_str)

        self.DO_NOT_USE_14.setCurrentIndex(0)
        self.tabWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.label.setText(QCoreApplication.translate("Form", u"\u0424\u0438\u043b\u044c\u0442\u0440:", None))
        self.DO_NOT_USE_18.setText(QCoreApplication.translate("Form", u"\u041e\u043a\u043e\u043d\u0447\u0430\u043d\u0438\u0435:", None))
        self.DO_NOT_USE_19.setText(QCoreApplication.translate("Form", u"\u041d\u0430\u0447\u0430\u043b\u043e:", None))
        self.DO_NOT_USE_14.setTabText(self.DO_NOT_USE_14.indexOf(self.DO_NOT_USE_15), QCoreApplication.translate("Form", u"\u041f\u0440\u043e\u0438\u0437\u0432\u043e\u043b\u044c\u043d\u044b\u0439 \u043f\u0435\u0440\u0438\u043e\u0434", None))
        self.DO_NOT_USE_23.setText(QCoreApplication.translate("Form", u"\u041c\u0435\u0441\u044f\u0446:", None))
        self.DO_NOT_USE_25.setText(QCoreApplication.translate("Form", u"\u0413\u043e\u0434:", None))
        self.DO_NOT_USE_14.setTabText(self.DO_NOT_USE_14.indexOf(self.DO_NOT_USE_21), QCoreApplication.translate("Form", u"\u041f\u0435\u0440\u0438\u043e\u0434 \u0438\u0437 \u0441\u043f\u0438\u0441\u043a\u0430", None))
        self.btn_add_filter.setText(QCoreApplication.translate("Form", u"\u0414\u043e\u0431\u0430\u0432\u0438\u0442\u044c \u0443\u0441\u043b\u043e\u0432\u0438\u044f", None))
        self.btn_count.setText(QCoreApplication.translate("Form", u"\u041f\u043e\u0441\u0447\u0438\u0442\u0430\u0442\u044c", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_data), QCoreApplication.translate("Form", u"\u0421\u043e\u0431\u0438\u0440\u0430\u0435\u043c\u044b\u0435 \u0434\u0430\u043d\u043d\u044b\u0435", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_where), QCoreApplication.translate("Form", u"\u0421\u043f\u0438\u0441\u043e\u043a \u043e\u0433\u0440\u0430\u043d\u0438\u0447\u0435\u043d\u0438\u0439", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_filter), QCoreApplication.translate("Form", u"\u0424\u0438\u043b\u044c\u0442\u0440\u044b \u043f\u043e \u0441\u043e\u0431\u0440\u0430\u043d\u043d\u044b\u043c \u0434\u0430\u043d\u043d\u044b\u043c", None))
    # retranslateUi

