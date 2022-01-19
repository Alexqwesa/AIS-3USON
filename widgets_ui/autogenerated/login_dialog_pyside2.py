# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'login_dialog.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *

from widgets.customQWidgets import myQLineEdit
from widgets.customQWidgets import myQStackedWidget


class Ui_loginDialog(object):
    def setupUi(self, loginDialog):
        if not loginDialog.objectName():
            loginDialog.setObjectName(u"loginDialog")
        loginDialog.resize(699, 464)
        font = QFont()
        font.setFamily(u"Droid Sans")
        font.setPointSize(18)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        loginDialog.setFont(font)
        loginDialog.setLayoutDirection(Qt.LeftToRight)
        self.verticalLayout = QVBoxLayout(loginDialog)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.label = QLabel(loginDialog)
        self.label.setObjectName(u"label")
        font1 = QFont()
        font1.setPointSize(22)
        font1.setBold(True)
        font1.setItalic(True)
        font1.setWeight(75)
        self.label.setFont(font1)
        self.label.setAlignment(Qt.AlignCenter)
        self.label.setWordWrap(True)

        self.verticalLayout.addWidget(self.label)

        self.formLayout = QFormLayout()
        self.formLayout.setObjectName(u"formLayout")
        self.formLayout.setLabelAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.formLayout.setFormAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignTop)
        self.label_4 = QLabel(loginDialog)
        self.label_4.setObjectName(u"label_4")

        self.formLayout.setWidget(0, QFormLayout.LabelRole, self.label_4)

        self.user = myQLineEdit(loginDialog)
        self.user.setObjectName(u"user")
        self.user.setInputMethodHints(Qt.ImhLatinOnly)
        self.user.setMaxLength(32)
        self.user.setClearButtonEnabled(True)

        self.formLayout.setWidget(0, QFormLayout.FieldRole, self.user)

        self.label_3 = QLabel(loginDialog)
        self.label_3.setObjectName(u"label_3")

        self.formLayout.setWidget(1, QFormLayout.LabelRole, self.label_3)

        self.password = myQLineEdit(loginDialog)
        self.password.setObjectName(u"password")
        self.password.setStyleSheet(u"* { lineedit-password-mask-delay: 800 }")
        self.password.setEchoMode(QLineEdit.Password)
        self.password.setClearButtonEnabled(True)

        self.formLayout.setWidget(1, QFormLayout.FieldRole, self.password)

        self.stackedWidget = myQStackedWidget(loginDialog)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.page_5 = QWidget()
        self.page_5.setObjectName(u"page_5")
        self.verticalLayout_2 = QVBoxLayout(self.page_5)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.label_2 = QLabel(self.page_5)
        self.label_2.setObjectName(u"label_2")

        self.verticalLayout_2.addWidget(self.label_2)

        self.status = QPlainTextEdit(self.page_5)
        self.status.setObjectName(u"status")
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(1)
        sizePolicy.setHeightForWidth(self.status.sizePolicy().hasHeightForWidth())
        self.status.setSizePolicy(sizePolicy)
        self.status.setUndoRedoEnabled(False)
        self.status.setReadOnly(True)

        self.verticalLayout_2.addWidget(self.status)

        self.stackedWidget.addWidget(self.page_5)
        self.page_6 = QWidget()
        self.page_6.setObjectName(u"page_6")
        self.verticalLayout_3 = QVBoxLayout(self.page_6)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.label_5 = QLabel(self.page_6)
        self.label_5.setObjectName(u"label_5")

        self.verticalLayout_3.addWidget(self.label_5)

        self.pt_driver = QPlainTextEdit(self.page_6)
        self.pt_driver.setObjectName(u"pt_driver")

        self.verticalLayout_3.addWidget(self.pt_driver)

        self.widget = QWidget(self.page_6)
        self.widget.setObjectName(u"widget")
        self.horizontalLayout = QHBoxLayout(self.widget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.label_6 = QLabel(self.widget)
        self.label_6.setObjectName(u"label_6")
        sizePolicy1 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.label_6.sizePolicy().hasHeightForWidth())
        self.label_6.setSizePolicy(sizePolicy1)

        self.horizontalLayout.addWidget(self.label_6)

        self.sp_port = QSpinBox(self.widget)
        self.sp_port.setObjectName(u"sp_port")
        self.sp_port.setMinimum(1024)
        self.sp_port.setMaximum(65500)
        self.sp_port.setValue(3306)

        self.horizontalLayout.addWidget(self.sp_port)

        self.label_8 = QLabel(self.widget)
        self.label_8.setObjectName(u"label_8")

        self.horizontalLayout.addWidget(self.label_8)

        self.server = QLineEdit(self.widget)
        self.server.setObjectName(u"server")

        self.horizontalLayout.addWidget(self.server)


        self.verticalLayout_3.addWidget(self.widget)

        self.stackedWidget.addWidget(self.page_6)
        self.page_7 = QWidget()
        self.page_7.setObjectName(u"page_7")
        self.gridLayout = QGridLayout(self.page_7)
        self.gridLayout.setObjectName(u"gridLayout")
        self.label_7 = QLabel(self.page_7)
        self.label_7.setObjectName(u"label_7")
        sizePolicy1.setHeightForWidth(self.label_7.sizePolicy().hasHeightForWidth())
        self.label_7.setSizePolicy(sizePolicy1)

        self.gridLayout.addWidget(self.label_7, 0, 0, 1, 1)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout.addItem(self.verticalSpacer, 2, 1, 1, 1)

        self.sp_dep = QSpinBox(self.page_7)
        self.sp_dep.setObjectName(u"sp_dep")

        self.gridLayout.addWidget(self.sp_dep, 0, 1, 1, 1)

        self.stackedWidget.addWidget(self.page_7)

        self.formLayout.setWidget(3, QFormLayout.SpanningRole, self.stackedWidget)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer)

        self.btnEnter = QDialogButtonBox(loginDialog)
        self.btnEnter.setObjectName(u"btnEnter")
        sizePolicy2 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.btnEnter.sizePolicy().hasHeightForWidth())
        self.btnEnter.setSizePolicy(sizePolicy2)
        font2 = QFont()
        font2.setPointSize(16)
        self.btnEnter.setFont(font2)
        self.btnEnter.setOrientation(Qt.Vertical)
        self.btnEnter.setStandardButtons(QDialogButtonBox.Cancel|QDialogButtonBox.Ok)
        self.btnEnter.setCenterButtons(False)

        self.horizontalLayout_2.addWidget(self.btnEnter)


        self.formLayout.setLayout(4, QFormLayout.FieldRole, self.horizontalLayout_2)

        self.pushButton = QPushButton(loginDialog)
        self.pushButton.setObjectName(u"pushButton")
        sizePolicy3 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.MinimumExpanding)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.pushButton.sizePolicy().hasHeightForWidth())
        self.pushButton.setSizePolicy(sizePolicy3)
        font3 = QFont()
        font3.setPointSize(12)
        font3.setBold(False)
        font3.setItalic(False)
        font3.setWeight(50)
        self.pushButton.setFont(font3)

        self.formLayout.setWidget(4, QFormLayout.LabelRole, self.pushButton)


        self.verticalLayout.addLayout(self.formLayout)

#if QT_CONFIG(shortcut)
        self.label_4.setBuddy(self.user)
        self.label_3.setBuddy(self.password)
#endif // QT_CONFIG(shortcut)

        self.retranslateUi(loginDialog)
        self.btnEnter.accepted.connect(loginDialog.accept)
        self.btnEnter.rejected.connect(loginDialog.reject)
        self.pushButton.clicked.connect(self.stackedWidget.next_tab)

        self.stackedWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(loginDialog)
    # setupUi

    def retranslateUi(self, loginDialog):
        loginDialog.setWindowTitle(QCoreApplication.translate("loginDialog", u"\u0410\u0418\u0421 \u0422\u0440\u0438\u0423\u0421\u041e\u041d", None))
        self.label.setText(QCoreApplication.translate("loginDialog", u"\u0412\u0432\u0435\u0434\u0438\u0442\u0435 \u0432\u0430\u0448\u0438 \u043b\u043e\u0433\u0438\u043d \u043f\u0430\u0440\u043e\u043b\u044c \u0434\u043b\u044f \u0432\u0445\u043e\u0434\u0430 \u0432 \u0441\u0438\u0441\u0442\u0435\u043c\u0443 \u0410\u0418\u0421 \u0422\u0440\u0438\u0423\u0421\u041e\u041d:", None))
        self.label_4.setText(QCoreApplication.translate("loginDialog", u"\u041b\u043e\u0433\u0438\u043d:", None))
        self.label_3.setText(QCoreApplication.translate("loginDialog", u"\u041f\u0430\u0440\u043e\u043b\u044c:", None))
        self.label_2.setText(QCoreApplication.translate("loginDialog", u"\u0421\u0442\u0430\u0442\u0443\u0441:", None))
        self.label_5.setText(QCoreApplication.translate("loginDialog", u"\u0414\u0440\u0430\u0439\u0432\u0435\u0440", None))
        self.label_6.setText(QCoreApplication.translate("loginDialog", u"\u041f\u043e\u0440\u0442", None))
        self.label_8.setText(QCoreApplication.translate("loginDialog", u"\u0421\u0435\u0440\u0432\u0435\u0440:", None))
        self.label_7.setText(QCoreApplication.translate("loginDialog", u"\u2116 \u043e\u0442\u0434\u0435\u043b\u0435\u043d\u0438\u044f", None))
        self.pushButton.setText(QCoreApplication.translate("loginDialog", u"info", None))
    # retranslateUi

