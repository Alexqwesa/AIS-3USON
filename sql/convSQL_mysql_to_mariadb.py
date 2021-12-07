#!/usr/bin/python
# -------------------------------------------------------------------------------
# -*- coding: utf-8 -*-
# Name:        convert SQL create Script from MySQL to mariadb
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

import sys
import datetime

list_of_wrong = [
    """
COLLATE utf8mb4_0900_ai_ci 
""", """
COLLATE = utf8mb4_0900_ai_ci
""", """
VISIBLE
""", ["""
utf8mb4 COLLATE utf8mb4_0900_ai_ci
""",
      "utf8"], """


""", """

""", """

"""

]


def main(*arg):
    fin = "kcson.sql"
    fout = "kcson_mariadb.sql"
    if arg:
        try:
            print(arg)
            fin = arg[1]
            fout = arg[2]
        except:
            pass
    data = ""
    with open(fin, "r") as fp:
        line = "" + datetime.date.today().strftime("# Converted %d.%m.%y'")
        ln = 1
        while line:
            ln = +1
            line = fp.readline()
            data = data + replacer(line)
    print(data)
    with open(fout, "w") as fo:
        fo.write(data)

def replacer(line: str) -> str:
    for exp in list_of_wrong:
        repl = ""
        if isinstance(exp, list):
            exp = exp[0]
            repl = exp[1]
        exp = exp.strip().replace("\n", "")
        repl = repl.strip().replace("\n", "")

        line = line.replace(exp, repl)
    return line

if __name__ == "__main__":
    main(sys.argv)
