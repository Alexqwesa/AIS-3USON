#!/usr/bin/python3
# -------------------------------------------------------------------------------
# -*- coding: utf-8 -*-
# Name:        AIS 3USON thread safe shared data
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
import configparser
import threading
import time
from contextlib import contextmanager

import sqlalchemy
from qtpy.QtCore import QRecursiveMutex
from sqlalchemy import create_engine
from sqlalchemy.exc import OperationalError, ProgrammingError
from sqlalchemy.orm import sessionmaker

from journal import *

from qtpy.QtCore import QObject, Signal, Slot, QMutex, QSettings, QCoreApplication, QDate
from qtpy.QtWidgets import QApplication, QMessageBox, QTableView, QCheckBox
from qtpy.QtSql import QSqlDatabase, QSql, QSqlQuery


def _SD_fill_dict():
    debug("_SD_fill_dict start")
    from logic.data_worker import WD
    # while not SD.key_lock.acquire(False):
    #     time.sleep(0.3)
    # QApplication.instance().processEvents()
    with SD.key_lock:
        for mname in ["dep", "ufio", "worker", "contracts", "_serv_activ"]:
            model = WD.models(mname)
            col_name = mname + "_id"
            for i in range(model.rowCount()):
                ind = model.index(i, 0)
                id = ind.data(Qt.EditRole)
                if id:
                    val = ind.siblingAtColumn(1).data(Qt.EditRole)
                    SD.key_id[col_name][id] = val
                    SD.key_val[col_name][val] = id
    debug("_SD_fill_dict finished")
    with suppress(AttributeError):
        QApplication.processEvents()
    return


class _safe_share_data(QObject):
    """Share data across thread"""
    # lock = threading.RLock() # replace to mutex in case of parallel processes (not threads)
    lock = QRecursiveMutex()
    lock__db_connections = QRecursiveMutex()
    # TODO: use several locks
    last_ufio_changed: Signal = Signal(int)
    last_contr_changed: Signal = Signal(int)
    last_dep_changed: Signal = Signal(int)
    last_tab_changed: Signal = Signal(str)
    last_ufio_filter_changed: Signal = Signal(int)
    server_changed: Signal = Signal(str)
    # port_changed: Signal = Signal(int)
    user_changed: Signal = Signal(str)
    password_changed: Signal = Signal(str)
    sql_sc_version_changed: Signal = Signal(str)
    # unsaved_changed: Signal = Signal()
    # saved_changed: Signal = Signal()
    dbconnect: Signal = Signal(bool)
    last_year_changed: Signal = Signal(int)
    setDirty_changed: Signal = Signal(bool)
    __instance = None

    # call_set_saved: Signal = Signal(QObject)

    def __new__(cls):
        if _safe_share_data.__instance is None:
            _safe_share_data.__instance = QObject.__new__(cls)
        return _safe_share_data.__instance

    def __init__(self, parent=None):
        """Constructor for SafeShared"""
        super().__init__(parent)
        self.setObjectName("main_data")
        self.db_name = "kcson"
        self._engine = None
        self._sess = None
        self._connnecion = None
        #############################
        # QSettings config
        # ---------------------------
        self.__driver_type = "QODBC"  # QODBC3  # before pyside6 QSqlDatabase QODBC3
        self.__driver = "{MySQL ODBC 8.0 Unicode Driver}"
        self.__user = ""
        self.__password = ""
        self.__server = "127.0.0.1"
        self.__port = 3306
        self.__sql_sc_version = 1
        self._config = None
        #############################
        # default QSettings
        # ---------------------------
        # QSettings - custum location not supported(
        # QSettings.setPath(QSettings.IniFormat, QSettings.SystemScope, ".")
        # self._qset = QSettings(QSettings.SystemScope,
        #                        "AIS 3USON", "main_qsettings"
        #                         )
        # QSettings.set
        # self._qset.setPath(QSettings.IniFormat, QSettings.SystemScope, ".")
        # self._qset = QSettings("main_qsettings.conf", QSettings.IniFormat)
        # self.__qset = QSettings(QSettings.IniFormat, QSettings.SystemScope, "3USON", "main_qsettings")
        #############################
        # sql config
        # ---------------------------
        self._dbconnected = False
        self.__last_ufio = None
        self.__last_contr = None
        self.__last_dep = 0
        self.__last_ufio_filter = None
        self.__last_year = QDate.currentDate().year()
        self.__last_tab = None
        self.__activate_signals = False
        self.QSqlAllTables = None
        self.preinited_models = False
        #############################
        # working state
        # ---------------------------
        self.journal = editStorage(self)
        self.__db_connections = {}
        self.__unsaved = False
        self.__unsaved_model = []
        self.__unsaved_view = []
        self._recently_saved_model = set()
        self.last_table: Union[QTableView, None] = None
        self.read_config(True)
        self.statusbar = self.tr("Загрузка приложения")  # update StatusBar by QTimer
        self.last_statusbar = ""
        # self.call_set_saved.connect(self.set_saved)
        #############################
        # relation data
        # ---------------------------
        self.key_id = defaultdict(lambda: dict())
        self.key_val = defaultdict(lambda: dict())
        self.key_lock = RLock()
        #############################
        # generete methods in loop
        # ---------------------------
        # for svar in ["__user"]:
        #     v=svar[2:]
        #     setv="set_" + v
        #     exec("self." + svar + " = None")
        #
        #     def sfunc(self, var):
        #         with QMutexLocker(self.lock):
        #             exec("self." + svar + " = var")
        #             # self.lock.release()
        #             exec("self." + svar + "_changed.emit(var)")
        #
        #     @property
        #     def func(self):
        #         return eval("self." + svar)
        #
        #     setattr(self, setv, sfunc)
        #     setattr(self, v, func)

    def preinit_models(self):
        if not self.preinited_models:
            self.preinited_models = True
            from logic.data_worker import WD
            for mname in ["dep", "ufio", "contracts", "worker", "_serv_activ"]:
                _ = WD.models(mname)
            # return _SD_fill_dict()
            self.thread = threading.Thread(None, _SD_fill_dict, "init_thread")
            # with SD.key_lock:
            if QApplication.instance():
                self.thread.start()
                QApplication.instance().processEvents()
                # Qtimer_runner(self.thread.join, 1000, "preinit_models", 1000)
                # self.thread.join()
            else:
                _SD_fill_dict()

    @property
    def db_connections(self):
        return self.__db_connections

    @db_connections.setter
    def db_connections(self, val):
        self.__db_connections = val

    def read_config(self, and_import=True):
        try:
            config = configparser.ConfigParser()
            conf_path = os.path.join(home_dir, "3uson.conf")
            if not os.path.exists(conf_path):
                conf_path = "3uson.conf"
            config.read(conf_path)
            debug(config.sections())
            if and_import:
                self._config = config
                try:
                    self.set_user(config['DEFAULT']['last_user'])
                except KeyError:
                    pass
                try:
                    self.set_server(config['DEFAULT']['server'])
                except KeyError:
                    pass
                try:
                    self.set_port(config['DEFAULT']['port'])
                except KeyError:
                    pass
                try:
                    self.set_driver(config['DEFAULT']['driver'])
                except KeyError:
                    pass
                try:
                    self.set_driver_type(config['DEFAULT']['driver_type'])
                except KeyError:
                    pass
                try:
                    self.set_password(config['DEFAULT']['DIRTY_HACK_FOR_DEBUG_SPW'])
                except KeyError:
                    pass
                try:
                    self.__last_year = int(config['DEFAULT']['DIRTY_HACK_FOR_DEBUG_YEAR'])
                except KeyError:
                    pass
                try:
                    self.__last_dep = int(config['DEFAULT']['last_dep'])
                except KeyError:
                    pass
                # self.set_last_dep(config['DEFAULT']['last_dep'])
                return config
        except:
            error("config read error")
            return None

    def save_conf(self):
        """Save config file
        """
        debug("save_conf")
        config = self._config
        config['DEFAULT']['last_user'] = self.user
        config['DEFAULT']['last_dep'] = str(self.last_dep)
        config['DEFAULT']['driver'] = str(self.driver)
        config['DEFAULT']['server'] = str(self.server)
        config['DEFAULT']['port'] = str(self.port)
        config['DEFAULT']['driver_type'] = str(self.driver_type)
        config['DEFAULT']['app_3uson_installed'] = str(1)
        config['DEFAULT']['mysql_connector'] = str(8020)  # TODO: update on mysql_connector change
        conf_path = os.path.join(home_dir, "3uson.conf")
        try:
            with open(conf_path, 'w', encoding='utf-8') as conf_file:
                config.write(conf_file)
        except:
            warning("config not saved")

    @Slot(bool)
    def setDirty(self, dirty):
        if dirty and not UI.dirty_is_blocked:
            for model in self.__unsaved_model:
                model.setDirty.emit(False)  # TODO: move check into model signal
        self.setDirty_changed.emit(dirty)

    def dump_configs(self):
        text = ""
        for var in dir(self):
            try:
                if var == "__password":
                    var = None
                if isinstance(var, list):
                    text = text + var + " = " + str(getattr(self, var))
                if isinstance(var, str):
                    text = text + var + " = " + str(getattr(self, var))
                if isinstance(var, int):
                    text = text + var + " = " + str(getattr(self, var))
                if isinstance(var, dict):
                    text = text + var + " = " + str(getattr(self, var))
                text = text + "\n"
            except:
                debug(var)
        return text

    #############################
    # set/get unsaved
    # ---------------------------
    @Slot(QObject)
    def set_unsaved(self, model):  # , view=None
        with QMutexLocker(self.lock):
            self.__unsaved = True
            self.__unsaved_model.append(model)
            #############################
            # find and set view
            # ---------------------------
            # try:
            #     view = QApplication.focusWidget()
            #     if hasattr(view, "model"):
            #         if view.model() is model:
            #             self.__unsaved_view = view
            #     elif hasattr(view.parent(), "model"):
            #         view = view.parent()
            #         if view.model() is model:
            #             self.__unsaved_view = view
            # except:
            #     debug("SD.__unsaved_view not found")
            #############################
            # send signal
            # ---------------------------
            # self.unsaved_changed.emit()
            self.setDirty(True)
            try:
                model.setDirty.emit(True)
            except:
                pass

    @Slot(QObject)
    def set_saved(self, mdl: QObject):
        with QMutexLocker(self.lock):
            if mdl in self.__unsaved_model:
                #############################
                # unlist views
                # ---------------------------
                for view in self.__unsaved_view:
                    if view.super_model() is mdl:
                        self.__unsaved_view.remove(view)
                #############################
                # unlist model, prep select list
                # ---------------------------
                self._recently_saved_model.add(mdl)
                self.__unsaved_model.remove(mdl)
                #############################
                # clean state
                # ---------------------------
                mdl.setDirty.emit(False)
                if not self.__unsaved_model:
                    self.__unsaved = False
                    # self.saved_changed.emit()
                    self.setDirty(False)
            else:
                error("trying to save unchanged model - %s", mdl.objectName())

    def reselect_saved_models(self):
        if not self.__unsaved_model:
            for mdl in self._recently_saved_model:
                mdl.select()
            self._recently_saved_model.clear()

    @property
    def unsaved(self):
        with QMutexLocker(self.lock):
            return self.__unsaved

    @property
    def unsaved_model(self):
        with QMutexLocker(self.lock):
            return self.__unsaved_model

    @property
    def unsaved_view(self):
        with QMutexLocker(self.lock):
            return self.__unsaved_view

    @unsaved_view.setter
    def unsaved_view(self, obj):
        with QMutexLocker(self.lock):
            if obj not in self.__unsaved_view:
                self.__unsaved_view.append(obj)

    #############################
    # set/get user
    # ---------------------------
    def set_user(self, var):
        with QMutexLocker(self.lock):
            self.__user = var
            # # self.lock.release()
            self.user_changed.emit(var)

    @property
    def user(self):
        return self.__user

    #############################
    # set/get last_ufio
    # ---------------------------
    def set_last_ufio(self, var):
        if var is None:
            var = -1
        with QMutexLocker(self.lock):
            self.__last_ufio = var
            # self.lock.release()
            ret = SD.line_query("select set_last_ufio(%s) " % var)
        self.last_ufio_changed.emit(var)
        return ret

    @property
    def last_ufio(self):
        return self.__last_ufio

    #############################
    # set/get last_dep
    # ---------------------------
    def set_last_dep(self, var=None):
        if var is None:
            var = self.__last_dep
        # prev = self.line_query("select GET_DEP(GET_wID())", 0 , self.get_new_dbconnect("set_last_dep"))
        # self.lock.release()
        #############################
        # select department in database - required for _active_dep_static !
        # ---------------------------
        if not self.get_db:
            return False
        ret = SD.line_query("call SET_DEP_(%s) " % var)
        if ret is None:
            ret = SD.line_query("select GET_DEP(GET_wID()) ")
        if ret == var:
            if ret != self.__last_dep:
                with QMutexLocker(self.lock):
                    SD.line_query("call GET_PRIVILEGES")
                    SD.line_query("SET ROLE all")
                    self.__last_dep = ret
                UI.threads_quit()
                QApplication.instance().exit(UI.main_window.EXIT_CODE_REBOOT)
                return
            with QMutexLocker(self.lock):
                SD.line_query("call GET_PRIVILEGES")
                SD.line_query("SET ROLE all")
                self.__last_dep = ret
            # for db_name, db in self.db_connections.items():
            #     if not db.isOpen():
            #         db.close()
            #         db.removeDatabase(db_name)
            #         db = self.get_new_dbconnect(db_name)
            #         if self.db_connections[db_name] != db:
            #             self.db_connections[db_name] = db
            #     SD.line_query("call GET_PRIVILEGES", 0, db)
            #     SD.line_query("SET ROLE all", 0, db)
            # self.last_dep_changed.emit(ret)
            return True
        else:
            error("Error can't set department - %s", var)
            return False

    @property
    def last_dep(self):
        return self.__last_dep

    #############################
    # set/get user
    # ---------------------------
    def set_last_tab(self, var):
        if var is None:
            var = ""
        with QMutexLocker(self.lock):
            self.__last_tab = var
            # self.lock.release()
            self.last_tab_changed.emit(var)

    @property
    def last_tab(self):
        return self.__last_tab

    #############################
    # set/get last_ufio_filter
    # ---------------------------
    def set_last_ufio_filter(self, var):
        if var is None:
            var = 0
        with QMutexLocker(self.lock):
            self.__last_ufio_filter = var
            # self.lock.release()
            self.last_ufio_filter_changed.emit(var)

    @property
    def last_ufio_filter(self):
        return self.__last_ufio_filter

    #############################
    # set/get last_contr
    # ---------------------------
    def set_last_contr(self, var):
        if var is None:
            var = 0
        with QMutexLocker(self.lock):
            ret = SD.line_query("select set_last_contr(%s) " % var)
            if ret:
                self.__last_contr = var
                self.last_contr_changed.emit(var)
            else:
                error("Error can't set contract - %s", var)
                return

    @property
    def last_contr(self):
        return self.__last_contr

    #############################
    # set/get last_year
    # ---------------------------
    def set_last_year(self, var):
        if var is None:
            var = 0
        with QMutexLocker(self.lock):
            self.__last_year = var
            ret = self.line_query("select SET_YEAR(%s) " % var)
            # self.lock.release()
            self.last_year_changed.emit(var)
            return ret

    @property
    def last_year(self):
        return self.__last_year

    #############################
    # set/get server
    # ---------------------------
    def set_server(self, var: str):
        with QMutexLocker(self.lock):
            self.__server = var
            # self.lock.release()
            self.server_changed.emit(var)

    @property
    def server(self):
        return self.__server

    #############################
    # set/get driver
    # ---------------------------
    def set_driver(self, var: str):
        with QMutexLocker(self.lock):
            self.__driver = var
            # self.lock.release()
            # self.driver_changed.emit(var)
            self.server_changed.emit(self.__server)  # driver?

    @property
    def driver(self):
        return self.__driver

    #############################
    # set/get driver_type
    # ---------------------------
    def set_driver_type(self, var: str):
        with QMutexLocker(self.lock):
            self.__driver_type = var
            # self.lock.release()
            # self.driver_type_changed.emit(var)
            self.server_changed.emit(self.__server)  # driver_type?

    @property
    def driver_type(self):
        return self.__driver_type

    #############################
    # set/get port
    # ---------------------------
    def set_port(self, var):
        with QMutexLocker(self.lock):
            self.__port = var
            # self.lock.release()
            # self.port_changed.emit(int(var))

    @property
    def port(self):
        return self.__port

    #############################
    # set/get password
    # ---------------------------
    def set_password(self, var):
        with QMutexLocker(self.lock):
            self.__password = var
            # self.lock.release()
            self.password_changed.emit(var)

    @property
    def password(self):
        return self.__password

    #############################
    # set/get sql_sc_version
    # ---------------------------
    def set_sql_sc_version(self, var):
        with QMutexLocker(self.lock):
            self.__sql_sc_version = var
            # self.lock.release()
            self.sql_sc_version_changed.emit(var)

    @property
    def sql_sc_version(self):
        return self.__sql_sc_version

    #############################
    # set/get session and engine
    # ---------------------------
    @property
    def session(self):
        if not self._sess:
            try:
                self._sess = self.new_session
            except (OperationalError, ProgrammingError):
                error("can't init sqlalchemy ")
        return self._sess

    @property
    def connection(self):
        if not self._connnecion:
            self._connnecion = self.engine.connect()
            self._connnecion.execute("CALL GET_PRIVILEGES")
            self._connnecion.execute("SET ROLE ALL")
        return self._connnecion

    @property
    def new_session(self):
        try:
            try:
                session = self._Session()
            except AttributeError:
                self._Session = sessionmaker(bind=self.engine, expire_on_commit=False)
                session = self._Session()
            session.execute("CALL GET_PRIVILEGES")
            session.execute("SET ROLE ALL")
            #############################
            # auth after rollback
            # ---------------------------
            orig_rollback = session.rollback

            def rollback(*a, **kw):
                res = orig_rollback()
                session.execute("CALL GET_PRIVILEGES")
                session.execute("SET ROLE ALL")
                return res

            session.rollback = rollback
            #############################
            # auth after commit
            # ---------------------------
            orig_commit = session.commit

            def commit(*a, **kw):
                res = orig_commit()
                session.execute("CALL GET_PRIVILEGES")
                session.execute("SET ROLE ALL")
                return res

            session.commit = commit
            # with self._engine
        except (OperationalError, ProgrammingError):
            error("can't init sqlalchemy ")
        finally:
            return session

    @contextmanager
    def session_scope(self):
        """Provide a transactional scope around a series of operations.
        Usage:
        with session_scope() as session:
            # use session here
        """
        session = self.session
        try:
            # with self._engine.connect() as connection:
            #     with connection.begin():
            #         connection.execute("CALL GET_PRIVILEGES();")
            #         connection.execute("SET ROLE ALL")
            yield session
            session.commit()
        except:
            session.rollback()
            raise
        finally:
            session.close()

    @property
    def engine(self):
        if not self._engine:
            if not SD._config:
                SD.read_config(True)
            try:
                # engine = create_engine('sqlite:///:memory:', echo=True)
                connect_str = "mysql+mysqlconnector://{0}:{1}@{2}:{3}/{4}".format(SD.user, SD.password, SD.server,
                                                                                  SD.port,
                                                                                  SD.db_name)
                # connect_str = "mysql+mysqldb://{0}:{1}@{2}:{3}/{4}".format(SD.user, SD.password, SD.server, SD.port,
                #                                                            SD.db_name)
                self._engine = create_engine(connect_str, echo=True, pool_recycle=3600)  # , multi=True
            except (OperationalError, ProgrammingError):
                error("can't init sqlalchemy ")
        return self._engine

    #############################
    # return QSettings
    # ---------------------------
    @property
    def qsettings(self) -> QSettings:
        # TODO: store 1 object per thread
        return QSettings("3USON", "main_qsettings")

    #############################
    # return new DB connection
    # ---------------------------
    @property
    def get_db(self):  # connect_name
        db_name = str(threading.get_ident())
        while is_locked(self.lock__db_connections):
            time.sleep(1)
        with QMutexLocker(self.lock__db_connections):
            #############################
            # check exist
            # ---------------------------
            if db_name in self.__db_connections:
                if self.__db_connections[db_name].isOpen():
                    return self.__db_connections[db_name]
            return self.get_new_dbconnect(db_name)

    def get_new_dbconnect(self, db_name):
        # with QMutexLocker(self.lock__db_connections):
        #############################
        # pre check db parameters
        # ---------------------------
        if not SD.server:
            SD.set_server("127.0.0.1")
        if not SD.port:
            SD.set_port("3306")
        #############################
        # set db parameters
        # ---------------------------
        db = QSqlDatabase.addDatabase(self.driver_type, db_name)
        if self.driver_type in ["QODBC", "QODBC3"]:
            db.setDatabaseName("Driver=%s;" \
                               "SERVER=%s;DATABASE=%s;UID=%s;PORT=%s;" % \
                               (SD.driver, SD.server, SD.db_name, SD.user, SD.port))
        elif self.driver_type == "QMYSQL":
            db.setDatabaseName(SD.db_name)
        else:
            error("Driver %s is not supported ", self.driver_type)
            return False
        db.setHostName(SD.server)
        db.setPort(SD.port)
        db.setUserName(SD.user)  # didn't work?
        db.setPassword(SD.password)  # PWD=<password>"
        #############################
        # open db
        # ---------------------------
        debug("DB %s isValid() - %s", db_name, db.isValid())
        res = db.open()
        if res:
            SD.line_query("call GET_PRIVILEGES", 0, db)
            SD.line_query("SET ROLE all", 0, db)
            # db.setNumericalPrecisionPolicy()
            with QMutexLocker(self.lock__db_connections):
                self.__db_connections[db_name] = db
                self.__first_init_var_ondbconnect(db)
            #############################
            # preinit models
            # ---------------------------
            self.preinit_models()
            #############################
            # return DB
            # ---------------------------
            return db
        elif not SD.password:
            return False
        else:
            #############################
            # error msg
            # ---------------------------
            # if "Access denied" in db.lastError().text():
            app = QCoreApplication.instance()
            msg = self.tr("Не удалось установить соединение с сервером"
                          " - свяжитесь в администратором")
            critical(msg)
            if isinstance(app, QApplication):
                # TODO: check pc avialable
                QMessageBox.critical(QApplication.topLevelWidgets()[0], self.tr("Отказано"),
                                     msg)  # TODO: rework this UI.main_window?
            # self.install_app()
            return False

    def install_app(self):
        pass
        # msgBox = QMessageBox()
        # msgBox.setText(
        #     self.tr("""Отказано( если не установлен драйвер - нажмите ДА,
        #     чтобы установить драйвер базы данных)"""))
        # msgBox.setInformativeText(msg)
        # msgBox.setStandardButtons(QMessageBox.Yes | QMessageBox.No)
        # msgBox.setDefaultButton(QMessageBox.No)
        # ret = msgBox.exec()
        # if ret:
        #     try:
        #         binpath = os.path.join(os.getcwd(), "..", "thirdparty", "vcredist_x86.exe").replace(
        #         "src\\..\\",      "")
        #         info("installing vcredist.exe")
        #         subprocess.run(
        #             binpath + " /q:a /c:\"msiexec /i vcredist.msi /qn\"",
        #             shell=True, stdin=None, stdout=True, stderr=True, close_fds=True)
        #         info("installing mysql-connector-odbc")
        #         subprocess.run(
        #             """ msiexec /i  ../thirdparty/mysql-connector-odbc-8.0.msi /quiet /qn /norestart """,
        #             shell=True, stdin=None, stdout=True, stderr=True, close_fds=True)
        #     except:
        #         error("installation failed")

    #############################
    # get SQL configs on first db connect
    # ---------------------------
    def __first_init_var_ondbconnect(self, db):
        if not self._dbconnected:
            # self.set_last_dep()
            # self.line_query("call GET_PRIVILEGES()", 0, db)
            self.QSqlAllTables = db.tables(QSql.AllTables)
            self.set_last_ufio(self.line_query("select get_last_ufio() ", 0, db))
            # self.set_last_ufio_filter(self.line_query("select get_last_ufio_filter() ", 0, db))
            sc = str(self.line_query("call GET_VER()", 0, db))
            if sc is None:
                sc = "0"
            self.set_sql_sc_version(sc)
            self.set_last_year(self.__last_year)
            #############################
            # send signal
            # ---------------------------
            self._dbconnected = True
            self.dbconnect.emit(True)

    # @staticmethod
    def line_query(self, qry_str, val=0, db=None):
        try:
            db.isOpen()
        except AttributeError:
            db = self.get_db
        qry = QSqlQuery(db)
        qry.exec_(qry_str)
        qry.next()
        return qry.value(val)

    #############################
    # disconnect DB's
    # ---------------------------
    def disconnect(self):
        # TODO: stop all QTimer
        self._dbconnected = False
        for name, db in self.__db_connections.items():
            db.close()
        self.__db_connections = {}

    #############################
    # reconnect DB's
    # ---------------------------
    def reconnect(self):
        # TODO: stop all QTimer
        for name, db in self.__db_connections.items():
            try:
                db.close()
            except AttributeError:
                pass
            db.open()

    # def replModel(self, modelName: str = None,
    #               sql: str = None, sqlTable: str = None,
    #               where: str = None) -> QSqlTableModel:
    #     #############################
    #     # add model to dict
    #     # ---------------------------
    #     if not modelName: modelName = sqlTable
    #     if not modelName: return False
    #     try:
    #         self.models.pop(modelName)
    #     except KeyError:
    #         pass
    #     return self.addModel(modelName, sql, sqlTable, where)

    def start_edit(self, view, model, row_id, col_name, prev=None, new=None):
        return self.journal.start_edit(view, model, row_id, col_name, prev, new)

    def commit_edit(self, model, prev, new, added_values=None):
        # self.unsaved.emit(self)
        self.set_unsaved(model)
        return self.journal.commit_edit(model, prev, new, added_values)

    @property
    def QSqlAllUpdatableTables(self):
        ret = []
        for t in self.QSqlAllTables:
            if "updatable_" in t:
                ret.append(t)
        return ret


class _QMessageBox:
    """ Just wrapper for unit testing"""

    def __init__(self, parent):
        self.parent = parent

    def information(self, parent, title, text, buttons=QMessageBox.Ok, defaultButton=QMessageBox.NoButton):
        if self.parent.main_window:
            QMessageBox.information(self.parent.main_window, title, text, buttons, defaultButton)
        else:
            msg = title + ": " + text
            info(msg)
            print(msg)

    def warning(self, parent, title, text, buttons=QMessageBox.Ok, defaultButton=QMessageBox.NoButton):
        if self.parent.main_window:
            QMessageBox.information(self.parent.main_window, title, text, buttons, defaultButton)
        else:
            msg = title + ": " + text
            warning(msg)
            print(msg)

    def critical(self, parent, title, text, buttons=QMessageBox.Ok, defaultButton=QMessageBox.NoButton):
        if self.parent.main_window:
            QMessageBox.information(self.parent.main_window, title, text, buttons, defaultButton)
        else:
            msg = title + ": " + text
            critical(msg)
            print(msg)


class _ui_data(QObject):
    """Share data across thread"""
    # lock = threading.RLock() # replace to mutex in case of parallel processes (not threads)
    lock = QRecursiveMutex()
    __instance = None

    def __new__(cls):
        if _ui_data.__instance is None:
            _ui_data.__instance = QObject.__new__(cls)
        return _ui_data.__instance

    def __init__(self, parent=None):
        """Constructor for SafeShared"""
        super().__init__(parent)
        self.setObjectName("ui_data")
        self._main_window: QWidget = Union[None, QWidget]
        self._history_of_tabs = []
        self.back_tab_index = 0
        self.last_view = None
        self.QMessageBox = _QMessageBox(self)
        self.qthreads = []

    def tr(self, *a, **kw):
        pass

    @property
    def main_window(self):
        return self._main_window

    @main_window.setter
    def main_window(self, value):
        self._main_window = value
        self.tr = self._main_window.tr

    @property
    def dirty_is_blocked(self):
        ui = self.main_window.ui
        chk: QCheckBox = ui.qa_dirty_tab_unblocked
        return not chk.isChecked()

    def go_back_to_tab(self, how_far=-1):
        """ go through self._history_of_tabs """
        tmp = self.back_tab_index
        if how_far:
            try:
                len1 = len(self._history_of_tabs)
                while len(self._history_of_tabs) and len1 == len(self._history_of_tabs):
                    tmp += how_far
                    self._history_of_tabs[tmp].activate()
                self.back_tab_index = tmp
            except IndexError:
                return

    @property
    def last_tab(self):
        return self._history_of_tabs[-1]

    @last_tab.setter
    def last_tab(self, val):
        with QMutexLocker(self.lock):
            self._history_of_tabs.append(val)
            self.back_tab_index = len(self._history_of_tabs) - 1

    @property
    def dock_pinfo_uid(self):
        if self.main_window:
            return self.main_window.ui.dock_people_info.ufio_id
        return 0

    @dock_pinfo_uid.setter
    def dock_pinfo_uid(self, uid):
        if self.main_window:
            self.main_window.ui.dock_people_info.update_ufio_id(uid)

    def threads_quit(self):
        for thd in self.qthreads:
            thd.quit()
        for thd in self.qthreads:
            thd.wait()
            self.qthreads.remove(thd)


#############################
# make only one instance
# ---------------------------
SD = _safe_share_data()
UI = _ui_data()
