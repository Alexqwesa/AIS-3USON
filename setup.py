#!/usr/bin/python3
# -------------------------------------------------------------------------------
# -*- coding: utf-8 -*-
# Name:        AIS 3USON runner
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

setup(
    name="AIS-3USON",
    version="1.0.0",
    description="Information System for social service organisation in Russia",
    long_description="README.md",
    long_description_content_type="",
    url="https://github.com/Alexqwesa/AIS-3USON",
    author="Savin Alexander Viktorovich  aka alexqwesa",
    author_email="alexo.veto@gmail.com",
    license="LGPL 3",
    classifiers=[
        "License :: OSI Approved :: LGPL 3"
    ],
    packages=["src", "thirdparty"],
    include_package_data=True,
    install_requires=[
        "qtpy", "python-docx", "pyside2", "pyqt5", 'docx', 'pypyodbc', "qtawesome", "concurrent-log-handler"
    ],
    entry_points={'console_scripts': ["ais3uson=run_app:main"]},
)
