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
import re
import sys
import datetime

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
""","utf8"], """


""", """
/*!50003 SET collation_connection  = utf8mb4_0900_ai_ci */ ;
""", """
/*!50001 SET collation_connection      = utf8mb4_0900_ai_ci */;
""", """

""", """

""", """

"""
# ,["""INSERT INTO kcson.serv (id, serv, serv_text, tnum, `year`, sub_serv, sub_serv_str, """,
#       "INSERT INTO kcson.serv (id, serv_text, tnum, `year`, sub_serv, sub_serv_str, "]

]

#############################
# mariadb import disallow import generated columns
# replace it
# ---------------------------
regexp=[
" id,\ serv,\ serv_text,\ tnum,\ `year`,\ sub_serv,\ sub_serv_str,\ price,\ price2,\ price3,\ archive,\ total,\ acronym,\ workload,\ content,\ `create`,\ ts,\ cr_by,\ upd_by\)\ VALUES([^,]*,)\ '([^']*)',\ ",
" id, serv_text, tnum, `year`, sub_serv, sub_serv_str, price, price2, price3,  archive, total, acronym, workload, content, `create`, ts, cr_by, upd_by) VALUES\\1 ",
]

def main(fin, fout):
    data = ""
    p = re.compile(regexp[0], re.VERBOSE)
    with open(fin, "r") as fp:
        line = "" + datetime.date.today().strftime("# Converted %d.%m.%y'")
        ln = 1
        while line:
            ln = +1
            line = fp.readline()
            line=line.replace("`columns`", "`COLUMNS`")
            if r"INSERT INTO kcson.serv (id, serv, serv_text, tnum, `year`, sub_serv, sub_serv_str, price, price2, price3, archive, total, acronym, workload," in line:
                line= p.sub(regexp[1], line)
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
    if len(sys.argv) > 2:
        main(sys.arg[1], sys.arg[2])
    else:
        main("schema.sql","maria_schema.sql")
        main("security.sql","maria_security.sql")
        main("data.sql","maria_data.sql")
        main("test_data.sql","maria_test_data.sql")
