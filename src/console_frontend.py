#!/usr/bin/python
# -------------------------------------------------------------------------------
# -*- coding: utf-8 -*-
# Name:        AIS 3USON console QT Frontend for quick tests
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

VERSION = 1
# import datetime
from datetime import datetime as dt
from datetime import timedelta

SQL_DATE_FORMAT = "yyyy-MM-dd"

from main_pyqt_frontend import *


class cons3uson(QObject):
    """Console AIS 3USON App"""

    def __init__(self, parent=None):
        """Constructor for cons3uson"""
        super().__init__()
        self.data = TsonData(self)
        self.qsettings = QSettings()
        debug("cons3uson init finished")

    def login(self):
        # debug("login %s ", (SD.user, SD.password))
        tr = self.tr
        if not SD.user:
            SD.set_user(input(tr("Введите имя пользователя:")))
        if not SD.password:
            SD.set_password(input(tr("Введите имя пользователя:")))
        ret = SD.get_db
        print(ret)

    def relogin(self):
        debug("relogin ")
        self.data.closeDBConnection()
        self.login()

    def show_tableView(self, wm, tname):
        #############################
        # test view
        # ---------------------------
        # try:
        #     debug(wm.qry_text)
        #     print(wm.selectStatement())
        # except:
        #     pass
        tv = myQTableView()
        tv.setObjectName(tname)
        # tv.data=self.data
        # tv.setModel(wm)
        tv.setGeometry(100, 100, 700, 700)
        tv.setWindowTitle("asdf")
        tv.show()
        tv.setItemDelegate(tsItemDelegate(tv))
        # tv.setItemDelegate(QSqlRelationalDelegate(tv))
        debug("show_tableView")

    def filter_table_model(self, dbModel):
        QSPmodel = tsQsfpModel()
        # TODO: qry one day only
        # self.data.addModel("dep_has_main_by_day",qryd)
        # dbModel.select()
        while dbModel.canFetchMore():
            dbModel.fetchMore()
        QSPmodel.setSourceModel(dbModel)
        # QSPmodel.setDynamicSortFilter(True)
        # QSPmodel.setSortingEnabled(True)
        # ui.table_dep_has_main.setModel(QSPmodel)
        # filter = "cast(lfnf as datetime)between cast('{}' as datetime) and cast('{}' as datetime)".format(
        #     combodate_1, combodate_2)
        # self.model.setFilter(filter)
        vdate = QDate(2001, 5, 27).toString("yyyy-MM-dd")
        debug(vdate)
        print_model_data(QSPmodel, 10, 10)
        QSPmodel.setFilterFixedString(vdate)
        QSPmodel.setFilterKeyColumn(6)  # TODO
        print_model_data(QSPmodel, 10, 10)

    def check_routines(self):
        print("=======GET_DEP=========")
        print(SD.line_query("select GET_DEP(GET_wID()) as res", 0))
        print(SD.last_dep)
        print("=======GET_wID=========")
        print(SD.line_query("select GET_wID() as res", 0))
        print("=======d.get_contract(1, vdate, 1)=========")
        vdate = QDate(2001, 5, 27).toString("yyyy-MM-dd")
        print(get_contract(1, vdate, 1))


def print_table(model, r=None, c=None):
    wm = model
    if isinstance(model, str):
        wm: tsSqlTableModel = SD.addModel(model)
    print_model_data(wm, r, c)


def main():
    info("3uson starting")
    debug("3uson debug on")
    #############################
    # start app
    # ---------------------------
    # app = QCoreApplication(sys.argv)
    # app.setQuitOnLastWindowClosed(False)
    app = QtWidgets.QApplication(sys.argv)
    cs = cons3uson()
    cs.login()
    debug("===========")
    d = cs.data
    #
    # mdl = d.addModel('dep_has_main_by_day', "select * from main_NZ where vdate between '01.05.01' and '28.05.01'")
    # print_model_data(mdl, 2, 2)

    # mdl: tsSqlTableModel = d.addModel("dep_has_worker")

    today = dt.now()
    dbeg = today - timedelta(days=32)
    dend = today + timedelta(days=32)
    debug("start setup table__dep_has_ufio__by_ufio")
    where = " vdate between '%s' and '%s' "
    where = where % (dbeg.strftime("%Y-%m-%d"), dend.strftime("%Y-%m-%d"))
    debug(where)
    # mdl: tsSqlTableModel = d.addModel("dep_has_main_by_day", "", "main_nz", where)
    # mdl2: tsSqlTableModel = d.addModel("dep_has_worker",)
    # mdl.setRelation(2, QtSql.QSqlRelation("dep", "id", "dep"))
    # mdl.setRelation(1, QtSql.QSqlRelation("worker", "id", "worker"))
    # mdl: tsSqlTableModel = WD.models("add_info")
    cs.show_tableView(None, "table_add_info")
    # debug("===== %s", mdl.data(mdl.index(0, 3), Qt.DisplayRole))
    # debug("===== %s", mdl.data(mdl.index(0, 3), Qt.EditRole))
    # mdl.setData(mdl.index(0, 3), 255, Qt.EditRole)
    # debug("===== %s", mdl.data(mdl.index(0, 3), Qt.DisplayRole))
    # mdl.setData(mdl.index(0, 3), 257, Qt.EditRole)
    # debug("===== %s", mdl.data(mdl.index(0, 3), Qt.DisplayRole))
    # # mdl.submitAll()
    #
    # rmdl = QSqlRelationalTableModel()
    # rmdl = QSqlRelTableModelExtView("main", app)
    # rmdl.setTable("main")
    #
    # rmdl.setRelation(3, QSqlRelation("ufio", "id", "ufio")
    #                  )
    # rmdl.setEditStrategy(QSqlTableModel.OnManualSubmit)
    # rmdl.select()
    # debug("===== %s", rmdl.data(mdl.index(0, 3), Qt.DisplayRole))
    # rmdl.setData(rmdl.index(0, 3), 250, Qt.EditRole)
    # debug("===== %s", rmdl.data(mdl.index(0, 3), Qt.DisplayRole))
    # rmdl.setData(rmdl.index(0, 3), 257, Qt.EditRole)
    # debug("===== %s", rmdl.data(mdl.index(0, 3), Qt.DisplayRole))
    # print_model_data(rmdl, 10)

    # print(d.line_query("select GET_DEP(GET_wID()) as res",1))
    # cs.relogin()
    # sys.exit(cs.exec())
    sys.exit(app.exec_())


if __name__ == "__main__":
    main()
