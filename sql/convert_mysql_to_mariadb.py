#!/usr/bin/python
# -------------------------------------------------------------------------------
# -*- coding: utf-8 -*-
# Name:        convert SQL create Scripts from MySQL to mariaDB
# Purpose:
#
# Author:      Savin Alexander Viktorovich aka alexqwesa
# Created:     2019-2022
# Copyright:   Savin Alexander Viktorovich aka alexqwesa
# Licence:     LGPL 3
# This software is licensed under the "LGPLv3" License as described in the "LICENSE" file,
# which should be included with this package. The terms are also available at
# http://www.gnu.org/licenses/lgpl-3.0.html
# -------------------------------------------------------------------------------
import datetime
import os
import re
import sys

list_of_wrong = [
    """
COLLATE utf8mb4_0900_ai_ci 
""", """
COLLATE = utf8mb4_0900_ai_ci
""", """
COLLATE=utf8mb4_0900_ai_ci
""", """
VISIBLE
""", ["""
utf8mb4 COLLATE utf8mb4_0900_ai_ci
""", "utf8"], """

""", """
/*!50003 SET collation_connection  = utf8mb4_0900_ai_ci */ ;
""", """
/*!50001 SET collation_connection      = utf8mb4_0900_ai_ci */;
""", """

""", """

""", """

"""

]

#############################
# mariadb import disallow import generated columns
# replace it
# ---------------------------
regexp = [
    # [
    #     "id,\ serv,\ serv_text,\ tnum,\ `year`,\ sub_serv,\ sub_serv_str,\ price,\ price2,\ price3,\ archive,\ replacedby,\ total,\ acronym,\ workload,\ content,\ `create`,\ ts,\ cr_by,\ upd_by\)\ VALUES([^,]*,)\ '([^']*)',\ ",
    #     "id, serv_text, tnum, `year`, sub_serv, sub_serv_str, price, price2, price3, archive, replacedby, total, acronym, workload, content, `create`, ts, cr_by, upd_by) VALUES\\1 ",
    # ]
]


def main(fin, fout):
    data = ""
    with open(fin, "r", encoding='utf-8') as fp:
        line = "" + datetime.date.today().strftime("# Converted %d.%m.%y'")
        ln = 1
        while line:
            ln += 1
            line = fp.readline()
            line = line.replace("`columns`", "`COLUMNS`")
            for reg in regexp:
                p = re.compile(reg[0], re.VERBOSE)
                if reg[1][10:150] in line:
                    line = p.sub(reg[1], line)
            data = data + replacer(line)
    print(data)
    with open(fout, "w", encoding='utf-8') as fo:
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
    if len(sys.argv) > 2:
        main(sys.argv[1], sys.argv[2])
    else:
        for file in list(os.walk("mysql"))[0][2]:
            main(os.path.join("mysql", file), os.path.join("mariadb", "generated_"+file))
