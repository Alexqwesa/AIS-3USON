from qtpy.QtSql import QSqlDatabase, QSqlQuery


def main():
    db = QSqlDatabase.addDatabase('QMYSQL')
##    if not SD.server:
##        SD.set_server("127.0.0.1")
##    if not SD.port:
##        SD.set_port("3306")
##        bdstr = "Driver=%s;" \
##                "SERVER=%s;DATABASE=kcson;UID=%s;PORT=%s;" % \
##                (SD.driver, SD.server, SD.user, SD.port)
    # bdstr = "Driver={MariaDB ODBC 3.0 Driver};" \
    #         "SERVER=%s;DATABASE=kcson;UID=%s;PORT=%s" % \
    #         (self.server, user, self.port)
    #db.setDatabaseName(bdstr)
    db.setUserName("newuser")  # didn't work?
    db.setPassword("mysql local work")  # PWD=<password>"
    db.setHostName("localhost")
    db.setDatabaseName("kcson")
    # db.setServer("127.0.0.1")
    # db.setPort(3306)
    print("DB  isValid() - %s" % db.isValid())
    res = db.open()
    if res:
        print("DB version %s " % line_query("call GET_VER()", 0, db))
    else:
        print(db.lastError().text())

def line_query(qry_str, val=0, db=None):
    qry = QSqlQuery(db)
    qry.exec_(qry_str)
    qry.next()
    return qry.value(val)

main()
