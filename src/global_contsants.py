#!/usr/bin/python3
# -------------------------------------------------------------------------------
# -*- coding: utf-8 -*-
# Name:        AIS 3USON global constants
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
import os
from itertools import count

from qtpy.QtGui import QColor
from qtpy.QtCore import Qt
from dataclasses import make_dataclass

#############################
# to silent syntax highlighter
# ---------------------------
if False:
    class Signal(Signal):
        def emit(self, *arg, **kwargs):
            return super().emit(*arg, **kwargs)

        def connect(self, *arg, **kwargs):
            return super().connect(*arg, **kwargs)


    class QAbstractTableModel(QAbstractTableModel):
        def tr(self, *arg, **kwargs):
            return super().tr(*arg, **kwargs)


    class QObject(QObject):
        def tr(self, *arg, **kwargs):
            return super().tr(*arg, **kwargs)


    class QMainWindow(QMainWindow):
        def tr(self, *arg, **kwargs):
            return super().tr(*arg, **kwargs)


    class Slot(Slot):
        def __call__(self, *args, **kwargs):
            return super().__call__(*args, **kwargs)
#############################
# date formats
# ---------------------------
SQL_DATE_FORMAT = "yyyy-MM-dd"
DEF_DATE_FORMAT = "dd.MM.yyyy"
TRUE_STR = " True "
FALSE_STR = " False "
ID_COL_IN_SQL_TABLE = 0
#############################
# journal
# for every edit object there is several states:
#     pending - in process    of    creation
#     committed - added    to    history
#     shadowed - edit marked as not needed for save because more recent change added
#     submitted - submit    to    DB
#     saved - status    of    submit    ok, and row_id    updated
#     confirmed - reselected    from DB
#     failed - failed    to    submit or reselect
# ---------------------------
bin_count = (2 ** i for i in range(31))
CE_PENDING = next(bin_count)
CE_COMMITTED = next(bin_count)
CE_SHADOWED = next(bin_count)
CE_SUBMITTED = next(bin_count)
CE_SAVED = next(bin_count)
CE_CONFIRMED = next(bin_count)
CE_SUB_FAILED = next(bin_count)
CE_SEL_FAILED = next(bin_count)
CE_CON_FAILED = next(bin_count)
CE_NEWEST = next(bin_count)  # this edit come from DB after trying to commit
CE_DISCARD = next(bin_count)
CE_STOP = next(bin_count)

# top limit of state
CE_PENDING_ = CE_COMMITTED - 1
CE_COMMITTED_ = CE_SHADOWED - 1
CE_SHADOWED_ = CE_SUBMITTED - 1
CE_SUBMITTED_ = CE_SAVED - 1
CE_SAVED_ = CE_CONFIRMED - 1
CE_CONFIRMED_ = CE_SUB_FAILED - 1
CE_SUB_FAILED_ = CE_SEL_FAILED - 1
CE_SEL_FAILED_ = CE_CON_FAILED - 1
CE_CON_FAILED_ = CE_NEWEST - 1
CE_NEWEST_ = CE_DISCARD - 1  # this edit come from DB after trying to commit
CE_DISCARD_ = CE_STOP - 1
CE_STOP_ = next(bin_count) - 1

#############################
# Qt.UserRoles
# ---------------------------
qt_user_role_iter = count(Qt.UserRole + 1)
prevData = next(qt_user_role_iter)
totalServ = next(qt_user_role_iter)
plannedServ = next(qt_user_role_iter)
filledServ = next(qt_user_role_iter)
leftServ = next(qt_user_role_iter)
priceServ = next(qt_user_role_iter)
nameServ = next(qt_user_role_iter)
subServ = next(qt_user_role_iter)
numNameServ = next(qt_user_role_iter)
idListServ = next(qt_user_role_iter)
roleMonth0 = next(qt_user_role_iter)
roleMonth1 = next(qt_user_role_iter)
roleMonth2 = next(qt_user_role_iter)
roleMonth3 = next(qt_user_role_iter)
roleMonth4 = next(qt_user_role_iter)
roleMonth5 = next(qt_user_role_iter)
roleMonth6 = next(qt_user_role_iter)
roleMonth7 = next(qt_user_role_iter)
roleMonth8 = next(qt_user_role_iter)
roleMonth9 = next(qt_user_role_iter)
roleMonth10 = next(qt_user_role_iter)
roleMonth11 = next(qt_user_role_iter)
roleMonth12 = next(qt_user_role_iter)
roleMonthYear = next(qt_user_role_iter)
roleMoneyMonth0 = next(qt_user_role_iter)
roleMoneyMonth1 = next(qt_user_role_iter)
roleMoneyMonth2 = next(qt_user_role_iter)
roleMoneyMonth3 = next(qt_user_role_iter)
roleMoneyMonth4 = next(qt_user_role_iter)
roleMoneyMonth5 = next(qt_user_role_iter)
roleMoneyMonth6 = next(qt_user_role_iter)
roleMoneyMonth7 = next(qt_user_role_iter)
roleMoneyMonth8 = next(qt_user_role_iter)
roleMoneyMonth9 = next(qt_user_role_iter)
roleMoneyMonth10 = next(qt_user_role_iter)
roleMoneyMonth11 = next(qt_user_role_iter)
roleMoneyMonth12 = next(qt_user_role_iter)
roleMoneyMonthYear = next(qt_user_role_iter)
roleSQL = next(qt_user_role_iter)
#############################
#
# ---------------------------
CACHE_DAYS = 43
POPUPMaxVisibleItems: int = 30
#############################
# colors
# ---------------------------
NEW_COLOR = QColor(240, 230, 255)
NEW_ROW_COLOR = QColor(240, 240, 255)
NEW_FAILED_COLOR = QColor(255, 200, 200)
NEW_FAIL_NEWEST_COLOR = QColor(245, 245, 200)
NEW_UNSAVED_COLOR = QColor(245, 245, 220)
NEW_UNSAVED_ROW_COLOR = QColor(255, 255, 240)
NEW_SAVED_COLOR = QColor(230, 255, 230)
NEW_SAVED_ROW_COLOR = QColor(240, 255, 240)
NEW_SUBMITTED_COLOR = QColor(220, 245, 220)
TOTAL_ROW_COLOR = QColor(200, 200, 210)
TOTAL_COL_COLOR = QColor(210, 210, 220)
ERROR_COLOR = QColor(230, 50, 50)
WARNING_COLOR = QColor(230, 200, 100)
#############################
# for orm
# ---------------------------
C_SDD = 0
C_PERC = 1
C_MPAY = 2
C_PERC_RIGHT = 3
C_IS_LAST = 4
#############################
# 
# ---------------------------

Dimensions = make_dataclass("Dimensions", ["up", "down", "left", "right"])

#
# @dataclass()
# class Dimensions:
#     up = 0
#     down = 0
#     left = 0
#     right = 0


#############################
# app settigns
# ---------------------------
try:
    if os.environ["FAST_LOG"].lower() == "true":
        FAST_LOG = True
    elif os.environ["FAST_LOG"].lower() == "false":
        FAST_LOG = False
except KeyError:
    FAST_LOG = True
