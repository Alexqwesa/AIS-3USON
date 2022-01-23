# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'qcSelectPeriod.ui'
##
## Created by: Qt User Interface Compiler version 6.2.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QComboBox, QDateEdit, QFrame,
    QGridLayout, QLabel, QSizePolicy, QSpinBox,
    QVBoxLayout, QWidget)

from widgets.customQWidgets import myQTabWidget

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(336, 148)
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Form.sizePolicy().hasHeightForWidth())
        Form.setSizePolicy(sizePolicy)
        self.gridLayout = QGridLayout(Form)
        self.gridLayout.setObjectName(u"gridLayout")
        self.qcFrame = QFrame(Form)
        self.qcFrame.setObjectName(u"qcFrame")
        self.qcFrame.setFrameShape(QFrame.StyledPanel)
        self.qcFrame.setFrameShadow(QFrame.Raised)
        self.gridLayout_2 = QGridLayout(self.qcFrame)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.tabs = myQTabWidget(self.qcFrame)
        self.tabs.setObjectName(u"tabs")
        sizePolicy1 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.tabs.sizePolicy().hasHeightForWidth())
        self.tabs.setSizePolicy(sizePolicy1)
        self.tabs.setMinimumSize(QSize(300, 0))
        self.tab_period = QWidget()
        self.tab_period.setObjectName(u"tab_period")
        self.verticalLayout_43 = QVBoxLayout(self.tab_period)
        self.verticalLayout_43.setObjectName(u"verticalLayout_43")
        self.gridLayout_14 = QGridLayout()
        self.gridLayout_14.setObjectName(u"gridLayout_14")
        self.gridLayout_14.setHorizontalSpacing(0)
        self.de_start = QDateEdit(self.tab_period)
        self.de_start.setObjectName(u"de_start")

        self.gridLayout_14.addWidget(self.de_start, 0, 1, 1, 1)

        self.label_63 = QLabel(self.tab_period)
        self.label_63.setObjectName(u"label_63")
        sizePolicy2 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Preferred)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.label_63.sizePolicy().hasHeightForWidth())
        self.label_63.setSizePolicy(sizePolicy2)
        self.label_63.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_14.addWidget(self.label_63, 1, 0, 1, 1)

        self.de_stop = QDateEdit(self.tab_period)
        self.de_stop.setObjectName(u"de_stop")

        self.gridLayout_14.addWidget(self.de_stop, 1, 1, 1, 1)

        self.label_51 = QLabel(self.tab_period)
        self.label_51.setObjectName(u"label_51")
        sizePolicy2.setHeightForWidth(self.label_51.sizePolicy().hasHeightForWidth())
        self.label_51.setSizePolicy(sizePolicy2)
        self.label_51.setLayoutDirection(Qt.LeftToRight)
        self.label_51.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_14.addWidget(self.label_51, 0, 0, 1, 1)

        self.gridLayout_14.setColumnStretch(0, 1)
        self.gridLayout_14.setColumnStretch(1, 2)

        self.verticalLayout_43.addLayout(self.gridLayout_14)

        self.tabs.addTab(self.tab_period, "")
        self.tab_month = QWidget()
        self.tab_month.setObjectName(u"tab_month")
        self.verticalLayout_44 = QVBoxLayout(self.tab_month)
        self.verticalLayout_44.setObjectName(u"verticalLayout_44")
        self.gridLayout_35 = QGridLayout()
        self.gridLayout_35.setObjectName(u"gridLayout_35")
        self.label_64 = QLabel(self.tab_month)
        self.label_64.setObjectName(u"label_64")
        self.label_64.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_35.addWidget(self.label_64, 0, 0, 1, 1)

        self.sp_year = QSpinBox(self.tab_month)
        self.sp_year.setObjectName(u"sp_year")
        self.sp_year.setMinimum(1950)
        self.sp_year.setMaximum(2050)
        self.sp_year.setValue(2019)

        self.gridLayout_35.addWidget(self.sp_year, 1, 1, 1, 1)

        self.label_65 = QLabel(self.tab_month)
        self.label_65.setObjectName(u"label_65")
        self.label_65.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_35.addWidget(self.label_65, 1, 0, 1, 1)

        self.cbx_month = QComboBox(self.tab_month)
        self.cbx_month.setObjectName(u"cbx_month")
        self.cbx_month.setEditable(True)

        self.gridLayout_35.addWidget(self.cbx_month, 0, 1, 1, 1)

        self.gridLayout_35.setColumnStretch(0, 1)
        self.gridLayout_35.setColumnStretch(1, 2)

        self.verticalLayout_44.addLayout(self.gridLayout_35)

        self.tabs.addTab(self.tab_month, "")

        self.gridLayout_2.addWidget(self.tabs, 0, 0, 1, 1)


        self.gridLayout.addWidget(self.qcFrame, 0, 0, 1, 1)


        self.retranslateUi(Form)

        self.tabs.setCurrentIndex(1)


        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.label_63.setText(QCoreApplication.translate("Form", u"\u041e\u043a\u043e\u043d\u0447\u0430\u043d\u0438\u0435:", None))
        self.label_51.setText(QCoreApplication.translate("Form", u"\u041d\u0430\u0447\u0430\u043b\u043e:", None))
        self.tabs.setTabText(self.tabs.indexOf(self.tab_period), QCoreApplication.translate("Form", u"\u041f\u0440\u043e\u0438\u0437\u0432\u043e\u043b\u044c\u043d\u044b\u0439 \u043f\u0435\u0440\u0438\u043e\u0434", None))
        self.label_64.setText(QCoreApplication.translate("Form", u"\u041c\u0435\u0441\u044f\u0446:", None))
        self.label_65.setText(QCoreApplication.translate("Form", u"\u0413\u043e\u0434:", None))
        self.tabs.setTabText(self.tabs.indexOf(self.tab_month), QCoreApplication.translate("Form", u"\u041f\u0435\u0440\u0438\u043e\u0434 \u0438\u0437 \u0441\u043f\u0438\u0441\u043a\u0430", None))
    # retranslateUi

