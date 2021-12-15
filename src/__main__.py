#!/usr/bin/python3
# -------------------------------------------------------------------------------
# -*- coding: utf-8 -*-
# Name:        AIS 3USON
# Purpose:
#
# Author:      Savin Alexander Viktorovich aka alexqwesa
# Created:     2021
# Copyright:   Savin Alexander Viktorovich aka alexqwesa
# Licence:     LGPL 3
# This software is licensed under the "LGPLv3" License as described in the "LICENSE" file,
# which should be included with this package. The terms are also available at
# http://www.gnu.org/licenses/lgpl-3.0.html
# -------------------------------------------------------------------------------

#############################
# check init vars
# ---------------------------
import os

start = "main_pyqt_frontend"
try:
    if os.environ['TUSON'] == "console_frontend":
        start = "console_frontend"
    elif os.environ['TUSON'] == "main_pyqt_frontend":
        start = "main_pyqt_frontend"
    elif os.environ['TUSON'] == "fill_templates":
        start = "fill_templates"
    elif os.environ['TUSON'] == "helper_func":
        start = "helper_func"
except KeyError:
    start = "main_pyqt_frontend"

#############################
# default QT binding
# ---------------------------
if not os.environ['QT_API']:
    os.environ['QT_API'] = "pyside6"
# os.environ['QT_API'] = "pyqt5"

#############################
# start app
# ---------------------------
if start == "main_pyqt_frontend":
    from main_pyqt_frontend import *
    main()
elif start == "fill_templates":
    from logic.fill_templates import *
    main()
elif start == "helper_func":
    from helper_func import *
    main()
