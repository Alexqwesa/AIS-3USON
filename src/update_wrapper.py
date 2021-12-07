#!/usr/bin/python3
# -------------------------------------------------------------------------------
# -*- coding: utf-8 -*-
# Name:        AIS 3USON Updater
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
import subprocess
import sys


def main():
    pass
    binpath = os.path.join(os.getcwd(), "..", "thirdparty", "vcredist_x86.exe").replace("src\\..\\", "")
    subprocess.run(binpath + " /q:a /c:\"msiexec /i vcredist.msi /qn\"", shell=True, stdin=None, stdout=None,
                   stderr=None, close_fds=True)
    exit(0)


if __name__ == "__main__":
    main()
