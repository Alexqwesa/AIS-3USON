#!/usr/bin/python3
# -------------------------------------------------------------------------------
# -*- coding: utf-8 -*-
# Name:        AIS 3USON QCalendarView Widgets
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
from qtpy.QtGui import QPainter
from qtpy.QtCore import QRect, QSemaphore, QThread, QPoint
from qtpy.QtGui import QKeySequence, QPen, QShowEvent
from qtpy.QtWidgets import QAction, QCalendarWidget

from widgets.widget_metaclasses import *


class _myQCalendar(QCalendarWidget, tsFilteredModel):
    __metaclass__ = QCalendarWidget


class QCalendarView(_myQCalendar):
    invalidation_needed: Signal = Signal()
    period_changed: Signal = Signal(QDate)

    def __init__(self, parent=None):
        """Constructor for QCalendar_view"""
        super().__init__(parent)
        self.last_filter_str = ""
        self.ts__init__("clndr_")
        #############################
        # current state
        # ---------------------------
        self.cur_ufio_id = 0
        self.cur_serv_id = 0
        self.cur_dep_has_worker_id = 0
        self.cur_worker_id = 0
        self.cur_serv_id_list = 0
        self._data_center = QDate()
        self._cur_filter_full = "__none__"
        self.cached = {}
        self.cache_inited = False
        self.cache = {}
        self.cache_start = False
        self.lock: QMutex = QRecursiveMutex()
        self.cache_lock: QMutex = QRecursiveMutex()
        self.uslnum_col = 0
        #############################
        # inner state setup
        # ---------------------------
        self.table: QTableView = self.findChild(QTableView)
        self.table.viewport().installEventFilter(self)
        self.vp: QWidget = self.table.viewport()
        self.setGridVisible(True)
        #############################
        # collect data in separate loop
        # ---------------------------
        self.cached_table = TableByRowsWHeader()
        self.invalidation_needed.connect(self.invalidate_cache)
        self.inited = False
        self.__class_prefix = "clndr_"

    def return_first_last_dates(self) -> Tuple[QDate, QDate]:
        # first row(0) and col(0) - headers, so we use second(1,1)
        first_date = self.date_by_index(
            self.table.model().index(1, 1))
        last_date = self.date_by_index(
            self.table.model().index(6, 7))
        return first_date, last_date

    def model(self):
        return self.filter_model()

    @Slot(QShowEvent)
    def showEvent(self, ev):
        self.init_model()
        if self.model():
            self.apply_delayed_filters()
            self.super_model().update_data()
        return super().showEvent(ev)

    def date_by_index(self, index: QModelIndex) -> Union[QDate, None]:
        """ Return QDate by index of model of QTableView """
        date: QDate = self.selectedDate()
        try:
            day = int(index.data())
        except (TypeError, ValueError):
            return None
        mnth = date.month()  # current month always the same as current date
        year = date.year()  # current month always the same as current date
        if day > 15 and index.row() < 3:  # qcalendar always display 6 rows( and 0 - is header)
            mnth = date.addMonths(-1).month()
            year = date.addMonths(-1).year()
        if day < 15 and index.row() > 4:
            mnth = date.addMonths(1).month()
            year = date.addMonths(1).year()
        return QDate(year, mnth, day)

    def setModel(self, model: tsSqlTableModel):
        pass

    @Slot()
    def invalidate_cache(self):
        # TODO: only clear dirty cache
        with QMutexLocker(self.cache_lock):
            self.cache = {}
        self.updateCells()

    def event(self, e: QEvent):
        if e.type() == QEvent.KeyPress:
            if e.key() == Qt.Key_F5:
                self.model().super_model().select()
                self.invalidate_cache()
            else:
                self.debug_event_handler(e)
        return super().event(e)

    def init_model(self):
        with QMutexLocker(self.locks("init_model")):
            if not self.inited:
                with QMutexLocker(self.lock):
                    #############################
                    # main model init and connect
                    # ---------------------------
                    self.inited = True
                    from logic.data_worker import WD
                    self.__class_prefix = "clndr_"
                    model_name = self.objectName().replace(self.__class_prefix, "private")
                    mdl = QSqlRelTableModelExtWithMetaData(
                        model_name,
                        self,
                        SD.get_new_dbconnect(model_name),
                        False)
                    mdl.setTable("_dep_has_main", FALSE_STR)
                    # mdl.setFilter()
                    # mdl: tsSqlTableModel = WD.model_by_name(self.objectName(), self.__class_prefix, False)
                    self.set_model(mdl)
                    self.setModel(mdl)
                    # with QMutexLocker(self.locks("init_model_filter")):
                    #     self._inited = True
                    # self.init_model_filter()
                    WD.inited_models[model_name] = mdl
                    self.uslnum_col = self.super_model().index_of_col("uslnum")
                    self.super_model().selected.connect(self.invalidate_cache)
                    self.super_model().fetch_all()
                    #############################
                    # sub model init and connect
                    # ---------------------------
                    # sub_model: tsSqlTableModel = WD.models("_dep_has_main")
                    # sub_model: tsSqlTableModel = WD.models("_dep_has_main__where_calendar")
                    # self.period_changed.connect(sub_model.update_where)
            return True

    def after_filters_updated(self):
        _ = self.current_full_filter  # just update
        return self.updateCells()

    @Slot(int, str)
    def set_flt_serv_model(self, val, get_val_from_model_name):
        with QMutexLocker(self.lock):
            # if self.set_third_filter_model(val, get_val_from_model_name):
            from logic.data_worker import WD
            self.cur_serv_id = WD.get_data_from_model_name(get_val_from_model_name, "serv_id_list", val)
            self.cur_serv_id_list = set()  # WD.get_data_from_model_name(get_val_from_model_name, "serv_id_list", val)
            if isinstance(val, str):
                if "," in val:
                    self.cur_serv_id_list = {int(x) for x in val.split(",")}
                else:
                    self.cur_serv_id_list.add(int(val))
            else:
                self.cur_serv_id_list.add(int(val))
            _ = self.current_full_filter  # just update
        self.updateCells()

    @Slot(int, str)
    def set_flt_worker_model(self, val, get_val_from_model_name):
        with QMutexLocker(self.lock):
            # if self.set_second_filter_model(val, get_val_from_model_name):
            from logic.data_worker import WD
            self.cur_dep_has_worker_id = WD.get_data_from_model_name(get_val_from_model_name, "id", val)
            model_raw, _, _ = get_val_from_model_name.partition("__")
            model_raw = (model_raw + "_raw").replace("_raw_raw", "_raw")
            self.cur_worker_id = WD.get_data_from_model_name(model_raw, "worker_id", val)
            # self.cur_worker_id.add(val)
            _ = self.current_full_filter  # just update
        self.updateCells()

    @Slot(int, str)
    def set_flt_ufio(self, val, get_val_from_model_name):
        with QMutexLocker(self.lock):
            # if self.set_first_filter_model(val, get_val_from_model_name):
            self.cur_ufio_id = val  # WD.get_data_from_model_name(get_val_from_model_name, "id", val)
            _ = self.current_full_filter  # just update
        self.updateCells()
        # if self.init_model():
        #     flt = self.get_filter_by("ufio_id")
        #     if flt_str != flt.currentFilterRegularExpression():
        #         flt.setFilterFixedString(flt_str)
        #         debug("flt_ufio_id - %s", flt_str)
        #         self.updateCells()

    def paintCell(self, painter: QPainter, rect: QRect, date: QDate):
        # ret = super().paintCell(painter, rect, date)
        if rect.isValid():
            #############################
            # get services in cell - serv_in_cell
            # ---------------------------
            serv_in_cell = self.get_serv_in_cell(date)
            #############################
            # paint cell
            # ---------------------------
            painter.save()
            #############################
            # draw date day
            # ---------------------------
            pstr = " " + str(date.day())
            font = QApplication.instance().font()
            font.setPointSize(font.pointSize() - 2)
            painter.setFont(font)
            painter.drawText(rect, 8 | Qt.AlignLeft | Qt.AlignTop, pstr)
            # debug(mdl)
            # pen = QPen()
            # pen.setWidth(1)
            # painter.setPen(pen)
            #############################
            # adjust rect rectangle
            # ---------------------------
            rect.setWidth(rect.width() - 2)
            rect.setHeight(rect.height() - 2)
            #############################
            # show total in day
            # ---------------------------
            if serv_in_cell:
                font.setPointSize(font.pointSize() + 6)
                painter.setFont(font)
                painter.setPen(Qt.red)
                # rect2 = QRect(rect)
                # rect2.setLeft(QFontMetrics(painter.font()).size(Qt.TextSingleLine, pstr).width())
                # debug(rect2)
                painter.drawText(rect, 8 | Qt.AlignCenter, str(serv_in_cell))
                painter.drawRect(rect)
                # fm = painter.fontMetrics()
                # rect2.setLeft(rect2.x() + fm.width(" " + str(serv_in_cell))*2)
                # painter.restore()
            painter.restore()

    @property
    def date_center(self):
        return self._data_center

    @date_center.setter
    def date_center(self, value):
        if self._data_center != value:
            self._data_center = value
            self.period_changed.emit(value)

    @property
    def current_full_filter(self):
        """
        Get current fulters as string except date
            example: empty_filters == "__none__{}{}{}"
        """
        if self.init_model():
            with QMutexLocker(self.locks("current_full_filter")):
                # model = self.super_model()  # all except real model and last filter
                cff = "__none__"
                cff += "{}|{}|{}".format(self.cur_ufio_id, self.cur_worker_id, self.cur_serv_id)
                # debug("current_full_filter = %s", cff)
                self._cur_filter_full = cff
                return cff

    def get_serv_in_cell(self, date):
        """ check(update) model and return sum(services) in cell """
        # snum = None
        if self.inited:
            #############################
            # look for cached service count
            # ---------------------------
            with QMutexLocker(self.cache_lock):
                cff = self.current_full_filter
                if cff and cff in self.cache:
                    if isinstance(self.cache[cff], dict):
                        if date in self.cache[cff]:
                            # QMutexLocker(self.lock)
                            snum = self.cache[cff][date]
                            return snum
                    else:
                        self.cache[cff] = {}
            self.recount_serv_in_cell(cff, date)  # don't return value because it can be in other thread
            return

    def update_data_center(self, date):
        #############################
        # check query in range (date_center+-43)
        # ---------------------------
        with QMutexLocker(self.lock):
            date_center: QDate = self.date_center
        if not date_center or \
                date > date_center.addDays(CACHE_DAYS) or \
                date < date_center.addDays(-CACHE_DAYS):
            #############################
            # if not prepare requery
            # ---------------------------
            date_center = date
            with QMutexLocker(self.lock):
                self.date_center = date_center
                self.cache_start = False
                self.last_filter_str = "vdate between '{}' and '{}'".format(
                    date_center.addDays(-CACHE_DAYS).toString(SQL_DATE_FORMAT),
                    date_center.addDays(CACHE_DAYS).toString(SQL_DATE_FORMAT))
            #############################
            # set where for raw model - TODO: use one model
            # ---------------------------
            # with QMutexLocker(self.cache_lock):
            self.super_model().setFilter(self.last_filter_str)  # 43
            self.invalidation_needed.emit()  # TODO: only invalidate if first cache entry is old > 5 min
            header = "ufio_id,worker_id,serv_id,uslnum,vdate".split(",")
            if self.super_model().filter() != FALSE_STR:
                with QMutexLocker(self.locks("current_full_filter")):
                    # cff = self._cur_filter_full
                    self.cached[self.date_center.toString(SQL_DATE_FORMAT)] = self.super_model().read_into_2darray(
                        header)
                    if not self.cache_inited:
                        ct = self.cached[self.date_center.toString(SQL_DATE_FORMAT)]
                        self.ct_uslnum = ct.header.index("uslnum")
                        self.ct_ufio_id = ct.header.index("ufio_id")
                        self.ct_worker_id = ct.header.index("worker_id")
                        self.ct_serv_id = ct.header.index("serv_id")
                        self.ct_vdate = ct.header.index("vdate")
                        self.cache_inited = True
                    # self.cached_table = self.super_model().read_into_2darray(header)
                    self.cache_start = True

    def recount_serv_in_cell(self, cff, date):
        """ trigger recount services then no cache found """
        self.update_data_center(date)
        self.count_serv_in_cell_runner(cff, date)
        self.updateCell(date)

    def count_serv_in_cell_runner(self, cff, date):
        """ count service in cell and write into cache """
        # QApplication.processEvents()
        with QMutexLocker(self.lock):
            if not self.cache_start:
                return
            cur_ufio_id = self.cur_ufio_id
            cur_worker_id = self.cur_worker_id
            cur_serv_id = self.cur_serv_id
            cur_serv_id_list = self.cur_serv_id_list
            if cff != self.current_full_filter:
                return
        #############################
        # count services TODO: read lock?
        # ---------------------------
        # snum = 0
        with QMutexLocker(self.locks("current_full_filter")):
            # self.cached[cff+self.date_center]=self.super_model().read_into_2darray(header)
            try:
                ct: TableByRowsWHeader = self.cached[self.date_center.toString(SQL_DATE_FORMAT)]  # check date here
            except KeyError:
                return
            all_ufio = not cur_ufio_id
            all_wrkr = not cur_worker_id
            all_serv = not cur_serv_id
            if self.cache_inited:
                uslnum, ufio_id, worker_id, serv_id, vdate = self.ct_uslnum, self.ct_ufio_id, \
                                                             self.ct_worker_id, self.ct_serv_id, self.ct_vdate
            else:
                uslnum = ct.header.index("uslnum")
                ufio_id = ct.header.index("ufio_id")
                worker_id = ct.header.index("worker_id")
                serv_id = ct.header.index("serv_id")
                vdate = ct.header.index("vdate")
            snum = sum([
                x[uslnum]
                for x in ct
                if
                (x[vdate] == date) and
                (all_ufio or x[ufio_id] == cur_ufio_id) and
                (all_wrkr or x[worker_id] == cur_worker_id) and
                (all_serv or x[serv_id] in cur_serv_id_list)
            ])
        # #############################
        # # if filter changed  we probably count wrong - TODO: interrupt count on filter change?
        # # ---------------------------
        # if cff != self.current_full_filter:
        #     # dismiss result
        #     return
        #############################
        # cache result
        # ---------------------------
        with QMutexLocker(self.cache_lock):
            # with QMutexLocker(self.lock):
            if cff not in self.cache:
                self.cache[cff] = {}
            self.cache[cff][date] = snum
        # debug("self.cache[%s][%s] = %s", cff, date, self.cache[cff][date])
        # TODO: self.update_cells


class QCalendarParalled(QCalendarView):

    def __init__(self, parent=None):
        """Constructor for QCalendar_view"""
        super().__init__(parent)
        #############################
        # init and start 2nd thread
        # ---------------------------
        self.thread_cntr: Controller = self.Controller(self, self.count_serv_in_cell_runner, self.cache)
        self.thread_cntr.pool_emptied.connect(self.updateCells)
        self.thread_cntr.start()

    @Slot()
    def updateCells(self):
        return super().updateCells()

    # def get_serv_in_cell(self, date):
    #     ret = super().get_serv_in_cell(date)
    #
    #     return ret

    def recount_serv_in_cell(self, cff, date, second_call=False):
        """ trigger recount services then no cache found """
        #############################
        # run in thread
        # ---------------------------
        # if not second_call:
        #     self.thread_cntr.call_from_thread.emit([self.recount_serv_in_cell, cff, date, True])
        #     return
        #############################
        # reselect model if needed
        # ---------------------------
        self.update_data_center(date)
        #############################
        # recount in pool
        # ---------------------------
        # snum = 0
        thd_name = str(date) + str(cff)
        self.thread_cntr.add_date_with_kick(thd_name, [QMutex(), cff, date])

    def paintCell(self, painter: QPainter, rect: QRect, date: QDate):
        ret = super().paintCell(painter, rect, date)
        if str(date) + str(self.current_full_filter) in self.thread_cntr.todo_pool:
            # painter.setPen(Qt.Yellow)
            br = QBrush(QColor(190, 190, 100), Qt.Dense7Pattern)
            painter.fillRect(rect, br)
        return ret

    class Controller(QObject):
        """Control thread for counting filtered date"""
        operate: Signal = Signal(str, list)
        pool_emptied: Signal = Signal()
        call_from_thread = Signal(list)

        class Worker(QObject):
            """ Work in thread"""
            resultReady: Signal = Signal(str, list)

            def __init__(self, parent=None, run_func=None):
                super().__init__(parent)
                self.run_func = run_func

            def call_from_thread(self, args):
                # debug("thread called")
                args[0](*args[1:])

            def do_work(self, key, args):
                # debug("thread called")
                # get one arg - list, and convert it into list or args for run_func # TODO: support of **kwargs
                try:
                    self.resultReady.emit(
                        key,
                        self.run_func(*args)
                    )
                except:
                    pass
                # finally:
                #     QSemaphoreReleaser(self.todo_pool_sem)

        def __init__(self, parent, run_func, cache):
            """ Constructor for controller """
            super().__init__(parent)
            #############################
            # init pool
            # ---------------------------
            self.todo_pool = {}
            self.todo_pool_lock: QMutex = QRecursiveMutex()
            self.todo_pool_sem = QSemaphore(os.cpu_count())
            #############################
            # init thread
            # ---------------------------
            self.worker_thread = QThread()
            UI.qthreads.append(self.worker_thread)
            self.worker: Worker = self.Worker(None, run_func)
            self.move_to_thread(self.worker)
            self.worker.todo_pool_sem = self.todo_pool_sem
            #############################
            # dynamic vars
            # ---------------------------
            self.cache = cache
            self.cache_lock = self.parent().cache_lock  # TODO: pass as parameter
            self.runners_id = []
            self.dispatch_called = 0
            self.qtimer_dispatch = False
            self.dispatch_lock: QMutex = QRecursiveMutex()
            #############################
            # connect
            # ---------------------------
            self.worker.resultReady.connect(self.handleResults)
            self.operate.connect(self.worker.do_work)
            # self.call_from_thread.connect(self.worker.call_from_thread)
            self.call_from_thread.connect(self.call_from_thread1)

        def move_to_thread(self, obj: QObject):
            obj.moveToThread(self.worker_thread)
            obj.setParent(self.worker)
            # try:
            #     if obj.db:
            #         obj.db.moveToThread(self.worker_thread)
            #         obj.db.setParent(self.worker)
            # except AttributeError:
            #     pass

        def add_date_with_kick(self, key, args):
            with QMutexLocker(self.todo_pool_lock):
                if key not in self.todo_pool:
                    self.todo_pool[key] = args
                    # debug("scheduled - %s ", thd_name)
                #############################
                # check if dispatcher running
                # ---------------------------
                # Qtimer_runner(self.dispatch) TODO: don't use main thread?
            with QMutexLocker(self.dispatch_lock):
                if not self.qtimer_dispatch:
                    self.qtimer_dispatch = QTimer(self)
                    self.qtimer_dispatch.setSingleShot(False)
                    self.qtimer_dispatch.setInterval(200)
                    self.qtimer_dispatch.timeout.connect(self.dispatch)
                    self.qtimer_dispatch.start(0)
                if not self.qtimer_dispatch.isActive():
                    self.qtimer_dispatch.start(0)

        @Slot(str, list)
        def handleResults(self, key, ret_args):
            pass

        def call_from_thread1(self, args):
            # debug("thread called")
            args[0](*args[1:])

        def start(self):
            # connect( & worker_thread, & QThread::finished, worker, & QObject::deleteLater);
            self.worker_thread.start()

        def __del__(self):
            self.worker_thread.quit()
            self.worker_thread.wait()
            s = super()
            if hasattr(s, "__del__"):
                s.__del__(self)

        def dispatch(self):
            """
            look for self.todo_pool entries and start them
            :return:
            """
            dcall = self.dispatch_called
            while True:
                #############################
                # check todo_pool: get item / exit loop
                # ---------------------------
                with QMutexLocker(self.todo_pool_lock):
                    if not self.todo_pool:
                        if self.dispatch_called != dcall:
                            self.dispatch_called = dcall
                            self.pool_emptied.emit()
                        with QMutexLocker(self.dispatch_lock):
                            self.qtimer_dispatch.stop()
                        return
                    thd_name, val = self.todo_pool.popitem()
                    lock, args = val[0], val[1:]
                #############################
                # check element: run if not cached
                # ---------------------------
                # with QMutexLocker(lock):  # if not self.todo_pool_sem.available()
                try:
                    with QMutexLocker(self.cache_lock):
                        test = []
                        for i, a in enumerate(args):
                            if i == 0:
                                test.append(self.cache[a])
                            else:
                                test.append(test[-1][a])
                except KeyError:
                    dcall += 1
                    # self.todo_pool_sem.acquire()
                    self.operate.emit(thd_name, args)
                except:
                    critical("dispatch error")
                # thd.start()
                # thd.join()
                # try:
                #     debug("cached - %s - %s ", key, self.cache[cff][date])
                # except KeyError:
                #     debug("caching - %s  ", date)


class myQCalendar(QCalendarView):  # QCalendarParalled
    """custom QCalendarWidget"""
    add: Signal = Signal(QDate)
    inwork: Signal = Signal(bool)
    inwork_total: Signal = Signal(int)
    signal_cur_ufio_left_serv: Signal = Signal(int)
    inwork_status: Signal = Signal(str)
    can_start: Signal = Signal(bool)

    # TODO: don't switch month on input

    def __init__(self, parent):
        """Constructor for myQCalendarWidget"""
        super().__init__(parent)
        #############################
        # input state vars
        # ---------------------------
        self.__input_state = False
        self.__iscontinue = True
        self.__isclick = True
        self.__iswheel = True
        self.__isenter = True
        # self.def_min_date = self.minimumDate()
        # self.def_max_date = self.maximumDate()
        self.clicked.connect(self.on_click)
        #############################
        # current state
        # ---------------------------
        self.rec_added_dates: [QDate] = []
        self.rec_added_dates_serv_num: [int] = []
        self.clicked_dates_failed: [QDate] = []
        self.last_index = None
        self._inwork = OrderedDict()
        self.cur_increase = 0
        self.cur_note = ""
        self.cache_wheel = self.CacheWheel(self)
        self.cache_wheel_installed = False
        #############################
        # add QActions with binded QKeySequence
        # ---------------------------
        self.qa_undo_inwork = QAction()
        self.qa_undo_inwork.setShortcut(QKeySequence(self.tr("Ctrl+Z", "Undo selected for add of services")))
        self.qa_undo_inwork.triggered.connect(self.undo_inwork)
        self.addAction(self.qa_undo_inwork)
        self.qa_save_inwork = QAction()
        self.qa_save_inwork.setShortcut(QKeySequence(self.tr("Ctrl+S", "Save selected for add of services")))
        self.qa_save_inwork.triggered.connect(self.save_changes)
        self.addAction(self.qa_save_inwork)
        self._cur_ufio_left_serv = 0
        self._first_date = -1
        self._first_status = [0, ""]
        self._last_status = [0, ""]

    def paintCell(self, painter: QPainter, rect: QRect, date: QDate):
        """
        Also paint recently added services and services in work
        """
        if rect.isValid():
            super().paintCell(painter, rect, date)
            painter.save()
            #############################
            # recently added
            # ---------------------------
            if date in self.rec_added_dates:
                # old_pen = painter.pen()
                # old_br = painter.brush()
                pen = QPen()
                pen.setWidth(3)
                painter.setPen(pen)
                # painter.setBackgroundMode(Qt.OpaqueMode)
                # painter.setBackground(QBrush()
                # gr = QRadialGradient()
                br = QBrush(QColor(200, 225, 200), Qt.Dense6Pattern)
                painter.setBrush(br)
                painter.fillRect(rect, br)
            #############################
            # not yet saved
            # ---------------------------
            if date in self._inwork:
                painter.setPen(Qt.red)
                br = QBrush(QColor(190, 255, 190), Qt.Dense3Pattern)
                painter.setBrush(br)
                painter.fillRect(rect, br)
                font = painter.font()
                font.setPointSize(font.pointSize() + 5)
                painter.setFont(font)
                painter.drawText(rect, 8 | Qt.AlignRight, "+" + str(self._inwork[date][0]))
            painter.restore()

    def undo_inwork(self):
        if self._inwork:
            # key= [self._inwork.keys()][-1]
            self._inwork.popitem()
            self.updateCells()
            self.emit_inwork_total()
            if self._inwork:
                self.inwork.emit(True)
            else:
                self.inwork.emit(False)

    class CacheWheel(QObject):
        """ class for catching wheel events and adding cells to self._inwork"""

        def __init__(self, parent):
            super().__init__(parent)
            self.table: QTableView = parent.table
            self.vp = parent.vp
            self.add_inwork = parent.add_inwork
            self.date_by_index = parent.date_by_index

        def eventFilter(self, watched: QObject, event: QEvent) -> bool:
            # if self.parent.input_state and self.parent.iswheel:  # double check just for sure
            if event.type() == QEvent.Wheel:
                # event.accept()  # here?
                # if UI.qt = "PySide2" or UI.qt = "Qt5" :
                #     index = self.table.indexAt(
                #         self.vp.mapFromGlobal(
                #             self.parent().window().mapToGlobal(
                #                 event.pos()    # PySide2
                #             )))
                index = self.table.indexAt(
                    self.vp.mapFromGlobal(
                        self.parent().window().mapToGlobal(
                            event.position()  # PySide6
                        )).toPoint())
                if index.isValid():
                    numDegrees: QPoint = event.angleDelta() / 8
                    if numDegrees.y() > 0:
                        self.add_inwork(self.date_by_index(index), 1)
                    if numDegrees.y() < 0:
                        self.add_inwork(self.date_by_index(index), -1)
                return True
            # if self.__isenter:
            # if watched is self.vp:
            if event.type() == QEvent.KeyPress:
                if event.key() in (Qt.Key_Plus, Qt.Key_Enter):  # Qt.Key_Enter) ?
                    index = self.table.selectedIndexes()[0]
                    # indexAt(event.pos())
                    if index.row() > 0 and index.column() > 0:
                        # self.last_index = index
                        self.add_inwork(self.date_by_index(index), self.parent().cur_increase)
                        return True
                elif event.key() == Qt.Key_Minus:
                    index = self.table.selectedIndexes()[0]
                    # index = self.table.indexAt(event.pos())
                    if index.row() > 0 and index.column() > 0:
                        # self.last_index = index
                        self.add_inwork(self.date_by_index(index), - self.parent().cur_increase)
                        return True
            return False

    @Slot(int)
    def set_increase(self, i):
        self.cur_increase = i

    @property
    def input_state(self):
        return self.__input_state

    @property
    def iswheel(self):
        return self.__iswheel

        # class ctable_ev(QObject):

    def showEvent(self, ev):
        ret = super().showEvent(ev)
        self.apply_delayed_filters()
        return ret

    @try_wrapper
    def eventFilter(self, qobj, event: QEvent):
        # ui = self.parent.ui
        if self.__input_state:
            vp = self.vp
            #############################
            # catch wheel events
            # ---------------------------
            if event.type() == QEvent.Enter and self.__iswheel:
                if not self.cache_wheel_installed:
                    QCoreApplication.instance().installEventFilter(self.cache_wheel)
                    self.cache_wheel_installed = True
                    debug("self.cache_wheel_installed - %s", self.cache_wheel_installed)
                # self.setAttribute()
            if event.type() == QEvent.Leave and self.cache_wheel_installed:
                QCoreApplication.instance().removeEventFilter(self.cache_wheel)
                self.cache_wheel_installed = False
            #############################
            # add services by selection
            # ---------------------------
            if self.__iscontinue:
                #############################
                # select by dragging
                # ---------------------------
                if qobj is vp:
                    if event.type() == QEvent.MouseButtonPress:
                        vp.setMouseTracking(True)
                        debug("setMouseTracking(True)")
                        event.ignore()
                        return False

                    if event.type() == QEvent.MouseMove:
                        index = self.table.indexAt(event.pos())
                        if index.row() > 0 and index.column() > 0:
                            if not self.last_index:
                                self.last_index = index
                                self.add_inwork(self.date_by_index(index), None, self.cur_increase)
                            elif self.last_index != index:
                                self.last_index = index
                                self.add_inwork(self.date_by_index(index), None, self.cur_increase)
                            # debug('row: %s, column: %s, text: %s qdate: %s',
                            #       index.row(), index.column(), index.data(),
                            #       self.date_by_index(index).toString(SQL_DATE_FORMAT)
                            #      )
                            event.ignore()
                            return False

                    if event.type() == QEvent.MouseButtonRelease:
                        self.last_index = None
                        vp.setMouseTracking(False)
                        event.ignore()
                        return False
            return super().eventFilter(qobj, event)
        return super().eventFilter(qobj, event)

    # def showMonth(self, year, month):
    #     if not self.inwork:
    #         super().showMonth(year, month)
    #
    # def setCurrentPage(self, year, month):
    #     if not self.inwork:
    #         return super().setCurrentPage(year, month)
    #
    # def event(self, event: QEvent) -> bool:
    #     if event.type() == QEvent.Wheel:
    #         return event.accept()
    #         pass
    #     return super().event(event)
    #
    # def wheelEvent(self, event: QWheelEvent):
    #     index = self.table.indexAt(event.pos())
    #     numDegrees: QPoint = event.angleDelta() / 8
    #     if numDegrees.y() > 0:
    #         self.add_inwork(self.date_by_index(index), 1)
    #     if numDegrees.y() < 0:
    #         self.add_inwork(self.date_by_index(index), -1)
    #     return event.accept()

    def add_inwork(self, date, increase=None, amount=None):
        """

        :param date:
        :param increase:
        :param amount:
        :return:
        """
        if not date:
            return False
        #############################
        # new key(date) if not exist
        # ---------------------------
        if date not in self._inwork.keys() and (increase or amount):
            self._inwork[date] = []
            self._inwork[date].append(0)
            self._inwork[date].append("")
        #############################
        # inc or set services value
        # ---------------------------
        if increase:
            if increase < 0 and self._inwork[date][0] <= (-increase):
                self._inwork.pop(date)
                # return True
            else:
                self._inwork[date][0] = self._inwork[date][0] + increase
                self._inwork[date][1] = self.cur_note
        elif amount:
            self._inwork[date][0] = amount
            self._inwork[date][1] = self.cur_note
        #############################
        # emit signals
        # ---------------------------
        # self.inwork_total =
        self.inwork.emit(True)
        self.emit_inwork_total()
        self.updateCells()
        # start, end = self.return_first_last_dates()
        # self.setMinimumDate(start)
        # self.setMaximumDate(end)
        # return self._inwork[date][0]

    def emit_inwork_total(self):
        Qtimer_runner(self.emit_inwork_total_worker, 100, "emit_inwork_total")

    def emit_inwork_total_worker(self):
        #############################
        # emit inwork_total
        # ---------------------------
        total = sum([v[0] for d, v in self._inwork.items()])
        self.inwork_total.emit(total)
        #############################
        # TODO: check cached status and update cache
        # ---------------------------
        first_date = self.date_by_index(
            self.table.model().index(1, 1))  # first row and col - is a headers
        last_date = self.date_by_index(
            self.table.model().index(6, 7))
        # if (self.cur_ufio_id, self.cur_serv_id, first_date) != (self.last_ufio_id, self.last_serv_id, self._first_date):
        #     self.last_ufio_id= self.cur_serv_id
        #     self.last_serv_id= self.cur_serv_id
        #     self._first_date = first_date
        from logic.data_worker import WD
        self._first_status = WD.get_status_for(self.cur_ufio_id, self.cur_serv_id, first_date)
        self._last_status = WD.get_status_for(self.cur_ufio_id, self.cur_serv_id, last_date)
        sleft_1, ret_status = self._first_status
        sleft_2, ret_status2 = self._last_status
        #############################
        # emit status
        # ---------------------------
        if ret_status == ret_status2:
            self.signal_cur_ufio_left_serv.emit(sleft_1 - total)
            self.inwork_status.emit(ret_status)
        else:
            self.inwork_status.emit(ret_status + " | " + ret_status2)
            sleft_, ret_status = WD.get_status_for(self.cur_ufio_id, self.cur_serv_id, self.selectedDate())
            self.signal_cur_ufio_left_serv.emit(sleft_ - total)

    @Slot(int, str)
    def set_flt_serv_model(self, val, get_val_from_model_name):
        super().set_flt_serv_model(val, get_val_from_model_name)
        self.emit_inwork_total()

    @Slot(int, str)
    def set_flt_ufio(self, val, get_val_from_model_name):
        super().set_flt_ufio(val, get_val_from_model_name)
        self.emit_inwork_total()

    @Slot(int, str)
    def set_flt_worker_model(self, val, get_val_from_model_name):
        super().set_flt_worker_model(val, get_val_from_model_name)
        self.emit_inwork_total()

    @Slot()
    def save_changes(self):
        for d in self._inwork:
            # self.add.emit(d)
            self.add_new_date(d, self._inwork[d][0], self._inwork[d][1])
        self.cleanup()

    def cleanup(self):
        self._inwork = OrderedDict()
        self.inwork.emit(False)
        self.emit_inwork_total()
        # self.setMinimumDate(self.def_min_date)
        # self.setMaximumDate(self.def_max_date)
        self.updateCells()

    @Slot()
    def discard_changes(self):
        self.cleanup()
        self.can_start.emit(False)
        self.__input_state = False

    # def hideEvent(self, event:QHideEvent):
    #     pass

    # @Slot(int, int, str)
    # def set_flt_serv(self, ind, id0, flt_str):
    #     if self.init_model():
    #         # self.set_filter_data(self.get_filter_by("serv_id"),id0,True,flt_str)
    #         self.get_filter_by("serv_id").set_filter_by_id(id0,
    #                                           self.super_model().index_of_col("serv_id"))
    #         debug("flt_serv_id3 - %s", flt_str)
    #         self.updateCells()

    # def updateCells(self):
    #     model = self.filter_model().sourceModel()
    #     self.cur_filter_full = "__none__"
    #     while hasattr(model, 'sourceModel'):
    #         self.cur_filter_full += model.currentFilterRegularExpression()  # all except real model and last filter
    #         model = model.sourceModel()
    #     return super().updateCells()

    def add_new_date(self, date, serv, note):
        from logic.data_worker import WD
        vdate = date
        dep = SD.last_dep
        qry_data = [
            0,
            dep,
            self.cur_ufio_id,
            self.cur_serv_id,
            vdate,
            serv,
            self.cur_dep_has_worker_id,
            note
            # ,
            # get_cbox_data(ui.cbx_1__dep_has_worker__2)
        ]
        ret, msg = WD.ins_main(qry_data)
        #############################
        # update models
        # ---------------------------
        if ret:
            self.rec_added_dates.append(date)
            self.rec_added_dates_serv_num.append(serv)
            # move to save_changes ?
            Qtimer_runner(self.super_model().select, 1500, "myQCalendar_select")
            Qtimer_runner(self.invalidate_cache, 2000, "myQCalendar_invalidate_cache")
            Qtimer_runner(self.updateCells, 2500, "myQCalendar_updateCells")

    @Slot(str)
    def set_note(self, note: str):
        self.cur_note = note

    @Slot(int)
    def set_continue_input(self, state):
        if state:
            self.__iscontinue = True
        else:
            self.__iscontinue = False

    @Slot(int)
    def set_click_input(self, state):
        if state:
            self.__isclick = True
        else:
            self.__isclick = False

    @Slot(int)
    def set_wheel_input(self, state):
        if state:
            self.__iswheel = True
        else:
            self.__iswheel = False

    @Slot(int)
    def set_enter_input(self, state):
        if state:
            self.__isenter = True
        else:
            self.__isenter = False

    @Slot(bool)
    def set_input_state(self, state):
        """ check: can input state be changed and send signal if yes"""
        if state:
            if self.cur_ufio_id and self.cur_dep_has_worker_id and self.cur_serv_id \
                    and "," not in self.cur_serv_id:
                self.__input_state = True
            else:
                self.can_start.emit(False)
        else:  # TODO: msg box if not empty inwork
            self.__input_state = False
            self.discard_changes()

    @Slot(QDate)
    def on_click(self, date: QDate):
        if self.__input_state and self.__isclick:
            # self.add.emit(date)
            if date not in self._inwork:
                self.add_inwork(date, None, self.cur_increase)
        else:
            try:
                with QMutexLocker(self.cache_lock):
                    del self.cache[self.current_full_filter][date]
                self.updateCell(date)
            except KeyError:
                pass

    # def mouseMoveEvent(self, ev):
    #     pass
