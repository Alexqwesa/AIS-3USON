# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'qcSelectPeriod.ui'
#
# Created by: PyQt5 UI code generator 5.14.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(336, 148)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Form.sizePolicy().hasHeightForWidth())
        Form.setSizePolicy(sizePolicy)
        self.gridLayout = QtWidgets.QGridLayout(Form)
        self.gridLayout.setObjectName("gridLayout")
        self.qcFrame = QtWidgets.QFrame(Form)
        self.qcFrame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.qcFrame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.qcFrame.setObjectName("qcFrame")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.qcFrame)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.tabs = myQTabWidget(self.qcFrame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tabs.sizePolicy().hasHeightForWidth())
        self.tabs.setSizePolicy(sizePolicy)
        self.tabs.setMinimumSize(QtCore.QSize(300, 0))
        self.tabs.setObjectName("tabs")
        self.tab_period = QtWidgets.QWidget()
        self.tab_period.setObjectName("tab_period")
        self.verticalLayout_43 = QtWidgets.QVBoxLayout(self.tab_period)
        self.verticalLayout_43.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_43.setObjectName("verticalLayout_43")
        self.gridLayout_14 = QtWidgets.QGridLayout()
        self.gridLayout_14.setHorizontalSpacing(0)
        self.gridLayout_14.setObjectName("gridLayout_14")
        self.de_start = QtWidgets.QDateEdit(self.tab_period)
        self.de_start.setObjectName("de_start")
        self.gridLayout_14.addWidget(self.de_start, 0, 1, 1, 1)
        self.label_63 = QtWidgets.QLabel(self.tab_period)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_63.sizePolicy().hasHeightForWidth())
        self.label_63.setSizePolicy(sizePolicy)
        self.label_63.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_63.setObjectName("label_63")
        self.gridLayout_14.addWidget(self.label_63, 1, 0, 1, 1)
        self.de_stop = QtWidgets.QDateEdit(self.tab_period)
        self.de_stop.setObjectName("de_stop")
        self.gridLayout_14.addWidget(self.de_stop, 1, 1, 1, 1)
        self.label_51 = QtWidgets.QLabel(self.tab_period)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_51.sizePolicy().hasHeightForWidth())
        self.label_51.setSizePolicy(sizePolicy)
        self.label_51.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label_51.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_51.setObjectName("label_51")
        self.gridLayout_14.addWidget(self.label_51, 0, 0, 1, 1)
        self.gridLayout_14.setColumnStretch(0, 1)
        self.gridLayout_14.setColumnStretch(1, 2)
        self.verticalLayout_43.addLayout(self.gridLayout_14)
        self.tabs.addTab(self.tab_period, "")
        self.tab_month = QtWidgets.QWidget()
        self.tab_month.setObjectName("tab_month")
        self.verticalLayout_44 = QtWidgets.QVBoxLayout(self.tab_month)
        self.verticalLayout_44.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_44.setObjectName("verticalLayout_44")
        self.gridLayout_35 = QtWidgets.QGridLayout()
        self.gridLayout_35.setObjectName("gridLayout_35")
        self.label_64 = QtWidgets.QLabel(self.tab_month)
        self.label_64.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_64.setObjectName("label_64")
        self.gridLayout_35.addWidget(self.label_64, 0, 0, 1, 1)
        self.sp_year = QtWidgets.QSpinBox(self.tab_month)
        self.sp_year.setMinimum(1950)
        self.sp_year.setMaximum(2050)
        self.sp_year.setProperty("value", 2019)
        self.sp_year.setObjectName("sp_year")
        self.gridLayout_35.addWidget(self.sp_year, 1, 1, 1, 1)
        self.label_65 = QtWidgets.QLabel(self.tab_month)
        self.label_65.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_65.setObjectName("label_65")
        self.gridLayout_35.addWidget(self.label_65, 1, 0, 1, 1)
        self.cbx_month = QtWidgets.QComboBox(self.tab_month)
        self.cbx_month.setEditable(True)
        self.cbx_month.setObjectName("cbx_month")
        self.gridLayout_35.addWidget(self.cbx_month, 0, 1, 1, 1)
        self.gridLayout_35.setColumnStretch(0, 1)
        self.gridLayout_35.setColumnStretch(1, 2)
        self.verticalLayout_44.addLayout(self.gridLayout_35)
        self.tabs.addTab(self.tab_month, "")
        self.gridLayout_2.addWidget(self.tabs, 0, 0, 1, 1)
        self.gridLayout.addWidget(self.qcFrame, 0, 0, 1, 1)

        self.retranslateUi(Form)
        self.tabs.setCurrentIndex(1)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.label_63.setText(_translate("Form", "Окончание:"))
        self.label_51.setText(_translate("Form", "Начало:"))
        self.tabs.setTabText(self.tabs.indexOf(self.tab_period), _translate("Form", "Произвольный период"))
        self.label_64.setText(_translate("Form", "Месяц:"))
        self.label_65.setText(_translate("Form", "Год:"))
        self.tabs.setTabText(self.tabs.indexOf(self.tab_month), _translate("Form", "Период из списка"))
from widgets.custumQWidgets import myQTabWidget


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
