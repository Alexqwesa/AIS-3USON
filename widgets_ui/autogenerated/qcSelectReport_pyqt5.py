# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'qcSelectReport.ui'
#
# Created by: PyQt5 UI code generator 5.14.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(842, 485)
        self.gridLayout = QtWidgets.QGridLayout(Form)
        self.gridLayout.setObjectName("gridLayout")
        self.qcFrame = QtWidgets.QFrame(Form)
        self.qcFrame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.qcFrame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.qcFrame.setObjectName("qcFrame")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.qcFrame)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.gridLayout_42 = QtWidgets.QGridLayout()
        self.gridLayout_42.setObjectName("gridLayout_42")
        self.label = QtWidgets.QLabel(self.qcFrame)
        self.label.setObjectName("label")
        self.gridLayout_42.addWidget(self.label, 1, 2, 1, 1)
        self.table = stubQTableView(self.qcFrame)
        self.table.setAlternatingRowColors(True)
        self.table.setObjectName("table")
        self.gridLayout_42.addWidget(self.table, 2, 0, 1, 4)
        self.period = qcSelectPeriod(self.qcFrame)
        self.period.setObjectName("period")
        self.verticalLayout_28 = QtWidgets.QVBoxLayout(self.period)
        self.verticalLayout_28.setObjectName("verticalLayout_28")
        self.DO_NOT_USE_14 = myQTabWidget(self.period)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.DO_NOT_USE_14.sizePolicy().hasHeightForWidth())
        self.DO_NOT_USE_14.setSizePolicy(sizePolicy)
        self.DO_NOT_USE_14.setMinimumSize(QtCore.QSize(300, 0))
        self.DO_NOT_USE_14.setObjectName("DO_NOT_USE_14")
        self.DO_NOT_USE_15 = QtWidgets.QWidget()
        self.DO_NOT_USE_15.setObjectName("DO_NOT_USE_15")
        self.verticalLayout_62 = QtWidgets.QVBoxLayout(self.DO_NOT_USE_15)
        self.verticalLayout_62.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_62.setObjectName("verticalLayout_62")
        self.DO_NOT_USE_16 = QtWidgets.QGridLayout()
        self.DO_NOT_USE_16.setHorizontalSpacing(0)
        self.DO_NOT_USE_16.setObjectName("DO_NOT_USE_16")
        self.DO_NOT_USE_17 = QtWidgets.QDateEdit(self.DO_NOT_USE_15)
        self.DO_NOT_USE_17.setObjectName("DO_NOT_USE_17")
        self.DO_NOT_USE_16.addWidget(self.DO_NOT_USE_17, 1, 1, 1, 1)
        self.DO_NOT_USE_18 = QtWidgets.QLabel(self.DO_NOT_USE_15)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.DO_NOT_USE_18.sizePolicy().hasHeightForWidth())
        self.DO_NOT_USE_18.setSizePolicy(sizePolicy)
        self.DO_NOT_USE_18.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.DO_NOT_USE_18.setObjectName("DO_NOT_USE_18")
        self.DO_NOT_USE_16.addWidget(self.DO_NOT_USE_18, 1, 0, 1, 1)
        self.DO_NOT_USE_19 = QtWidgets.QLabel(self.DO_NOT_USE_15)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.DO_NOT_USE_19.sizePolicy().hasHeightForWidth())
        self.DO_NOT_USE_19.setSizePolicy(sizePolicy)
        self.DO_NOT_USE_19.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.DO_NOT_USE_19.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.DO_NOT_USE_19.setObjectName("DO_NOT_USE_19")
        self.DO_NOT_USE_16.addWidget(self.DO_NOT_USE_19, 0, 0, 1, 1)
        self.DO_NOT_USE_20 = QtWidgets.QDateEdit(self.DO_NOT_USE_15)
        self.DO_NOT_USE_20.setObjectName("DO_NOT_USE_20")
        self.DO_NOT_USE_16.addWidget(self.DO_NOT_USE_20, 0, 1, 1, 1)
        self.DO_NOT_USE_16.setColumnStretch(0, 1)
        self.DO_NOT_USE_16.setColumnStretch(1, 2)
        self.verticalLayout_62.addLayout(self.DO_NOT_USE_16)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_62.addItem(spacerItem)
        self.DO_NOT_USE_14.addTab(self.DO_NOT_USE_15, "")
        self.DO_NOT_USE_21 = QtWidgets.QWidget()
        self.DO_NOT_USE_21.setObjectName("DO_NOT_USE_21")
        self.verticalLayout_63 = QtWidgets.QVBoxLayout(self.DO_NOT_USE_21)
        self.verticalLayout_63.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_63.setObjectName("verticalLayout_63")
        self.DO_NOT_USE_22 = QtWidgets.QGridLayout()
        self.DO_NOT_USE_22.setObjectName("DO_NOT_USE_22")
        self.DO_NOT_USE_23 = QtWidgets.QLabel(self.DO_NOT_USE_21)
        self.DO_NOT_USE_23.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.DO_NOT_USE_23.setObjectName("DO_NOT_USE_23")
        self.DO_NOT_USE_22.addWidget(self.DO_NOT_USE_23, 0, 0, 1, 1)
        self.DO_NOT_USE_24 = QtWidgets.QSpinBox(self.DO_NOT_USE_21)
        self.DO_NOT_USE_24.setMinimum(1950)
        self.DO_NOT_USE_24.setMaximum(2050)
        self.DO_NOT_USE_24.setProperty("value", 2019)
        self.DO_NOT_USE_24.setObjectName("DO_NOT_USE_24")
        self.DO_NOT_USE_22.addWidget(self.DO_NOT_USE_24, 1, 1, 1, 1)
        self.DO_NOT_USE_25 = QtWidgets.QLabel(self.DO_NOT_USE_21)
        self.DO_NOT_USE_25.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.DO_NOT_USE_25.setObjectName("DO_NOT_USE_25")
        self.DO_NOT_USE_22.addWidget(self.DO_NOT_USE_25, 1, 0, 1, 1)
        self.DO_NOT_USE_26 = QtWidgets.QComboBox(self.DO_NOT_USE_21)
        self.DO_NOT_USE_26.setEditable(True)
        self.DO_NOT_USE_26.setObjectName("DO_NOT_USE_26")
        self.DO_NOT_USE_22.addWidget(self.DO_NOT_USE_26, 0, 1, 1, 1)
        self.DO_NOT_USE_22.setColumnStretch(0, 1)
        self.DO_NOT_USE_22.setColumnStretch(1, 2)
        self.verticalLayout_63.addLayout(self.DO_NOT_USE_22)
        spacerItem1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_63.addItem(spacerItem1)
        self.DO_NOT_USE_14.addTab(self.DO_NOT_USE_21, "")
        self.verticalLayout_28.addWidget(self.DO_NOT_USE_14)
        self.gridLayout_42.addWidget(self.period, 0, 0, 1, 1)
        self.lineEdit = QtWidgets.QLineEdit(self.qcFrame)
        self.lineEdit.setObjectName("lineEdit")
        self.gridLayout_42.addWidget(self.lineEdit, 1, 3, 1, 1)
        self.btn_add_filter = QtWidgets.QPushButton(self.qcFrame)
        self.btn_add_filter.setObjectName("btn_add_filter")
        self.gridLayout_42.addWidget(self.btn_add_filter, 1, 1, 1, 1)
        self.btn_count = QtWidgets.QPushButton(self.qcFrame)
        self.btn_count.setObjectName("btn_count")
        self.gridLayout_42.addWidget(self.btn_count, 1, 0, 1, 1)
        self.tabWidget = myQTabWidget(self.qcFrame)
        self.tabWidget.setObjectName("tabWidget")
        self.tab_data = QtWidgets.QWidget()
        self.tab_data.setObjectName("tab_data")
        self.tabWidget.addTab(self.tab_data, "")
        self.tab_where = QtWidgets.QWidget()
        self.tab_where.setObjectName("tab_where")
        self.tabWidget.addTab(self.tab_where, "")
        self.tab_filter = QtWidgets.QWidget()
        self.tab_filter.setObjectName("tab_filter")
        self.tabWidget.addTab(self.tab_filter, "")
        self.gridLayout_42.addWidget(self.tabWidget, 0, 1, 1, 3)
        self.gridLayout_42.setRowStretch(0, 1)
        self.gridLayout_42.setRowStretch(2, 5)
        self.gridLayout_2.addLayout(self.gridLayout_42, 0, 0, 1, 1)
        self.gridLayout.addWidget(self.qcFrame, 0, 0, 1, 1)

        self.retranslateUi(Form)
        self.DO_NOT_USE_14.setCurrentIndex(0)
        self.tabWidget.setCurrentIndex(0)
        self.lineEdit.textChanged['QString'].connect(self.table.set_first_filter_str)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.label.setText(_translate("Form", "????????????:"))
        self.DO_NOT_USE_18.setText(_translate("Form", "??????????????????:"))
        self.DO_NOT_USE_19.setText(_translate("Form", "????????????:"))
        self.DO_NOT_USE_14.setTabText(self.DO_NOT_USE_14.indexOf(self.DO_NOT_USE_15), _translate("Form", "???????????????????????? ????????????"))
        self.DO_NOT_USE_23.setText(_translate("Form", "??????????:"))
        self.DO_NOT_USE_25.setText(_translate("Form", "??????:"))
        self.DO_NOT_USE_14.setTabText(self.DO_NOT_USE_14.indexOf(self.DO_NOT_USE_21), _translate("Form", "???????????? ???? ????????????"))
        self.btn_add_filter.setText(_translate("Form", "???????????????? ??????????????"))
        self.btn_count.setText(_translate("Form", "??????????????????"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_data), _translate("Form", "???????????????????? ????????????"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_where), _translate("Form", "???????????? ??????????????????????"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_filter), _translate("Form", "?????????????? ???? ?????????????????? ????????????"))
from widgets.customQWidgets import myQTabWidget, qcSelectPeriod, stubQTableView


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
