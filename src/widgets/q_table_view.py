#!/usr/bin/python3
# -------------------------------------------------------------------------------
# -*- coding: utf-8 -*-
# Name:        AIS 3USON QTableView child classes
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
from qtpy.QtGui import QPaintEvent
from qtpy.QtCore import QItemSelectionModel, QMimeData, QItemSelection
from qtpy.QtWidgets import QAbstractItemView
from qtpy.QtGui import QMouseEvent, QFontMetrics

from models.universal_delegate import tsItemDelegate
from widgets.q_calendar_view import *


class tsQTableViewDockInfo(QTableView):
    def mousePressEvent(self, ev: QMouseEvent):
        ret = super().mousePressEvent(ev)
        if ev.button() == Qt.LeftButton:
            #############################
            # check selection
            # ---------------------------
            col = None
            if hasattr(self, "super_model"):
                if self.super_model():
                    if "ufio_id" in self.super_model().tsFieldNames:
                        col = self.super_model().tsFieldNames.index("ufio_id")
                    if "ufio" in self.super_model().tsFieldNames and "snils" in self.super_model().tsFieldNames:
                        col = self.super_model().tsFieldNames.index("id")
                    if col is not None:
                        selection: QItemSelectionModel = self.selectionModel()
                        indexes: [QModelIndex] = selection.selectedIndexes()
                        if len(indexes) == 1:
                            ind: QModelIndex = indexes[0]
                            uid = ind.siblingAtColumn(col).data(Qt.EditRole)
                            if uid:
                                UI.dock_pinfo_uid = uid
        return ret


class tsQTableView(tsQTableViewDockInfo):
    call_activate: Signal = Signal(str)

    def __init__(self, *a, **kw):
        super().__init__(*a, **kw)
        self._dirty_connected = False
        self._dirty = False
        self.qa_save = QAction()
        self.qa_copy_shift = QAction()
        self.filters = {}
        self.inited = False
        #############################
        # setup
        # ---------------------------
        self.horizontalHeader().setDefaultAlignment(Qt.AlignLeft)
        self.setTextElideMode(Qt.ElideRight)
        # self.sortByColumn(0, Qt.AscendingOrder)
        self.setAlternatingRowColors(True)
        # self.SelectionBehavior(QAbstractItemView.SelectItems)
        self.setSelectionMode(QAbstractItemView.ExtendedSelection)
        self.col_adjusted = False
        #############################
        # add QActions with binding
        # ---------------------------
        self.qa_save.setShortcut(QKeySequence(self.tr("Ctrl+S", "Save")))
        self.qa_save.triggered.connect(self.save)
        self.addAction(self.qa_save)
        self.call_activate.connect(self.activate)

    def col_adjust(self):
        if not self.col_adjusted:
            self.col_adjusted = True
            for col in range(self.model().columnCount()):
                self.setColumnWidth(col,
                                    QFontMetrics(QApplication.font()).size(
                                        Qt.TextSingleLine, self.model().headerData(col, Qt.Horizontal)).width() + 10
                                    )
                # self.horizontalHeader().setSectionResizeMode(QHeaderView.ResizeToContents)
                # self.update()
                # self.horizontalHeader().setSectionResizeMode(QHeaderView.Interactive)

    @Slot()
    @Slot(str)
    def activate(self, col_name=""):
        #############################
        # activate tab with widget
        # ---------------------------
        p = self.parent()
        from widgets.custumQWidgets import myQWidget
        while p and not isinstance(p, myQWidget):
            p = p.parent()
        p.activate()
        #############################
        # update
        # ---------------------------
        self.setFocus()
        # self.update(self.selectedIndexes()[0])

    def init_model(self, val=True):
        self.inited = val
        #############################
        # TODO: resize but set limit by field name
        # ---------------------------
        # self.horizontalHeader().resizeSections(QHeaderView.ResizeToContents)

    @property
    def selection_in_progress(self):
        if self.model():
            try:
                return self.model().super_model().selection_in_progress
            except AttributeError:
                pass
        return False

    @Slot()
    def save(self):
        self.model().super_model().submitAll()

    def setModel(self, model):
        if not self._dirty_connected:
            try:
                model.super_model().setDirty.connect(self.setDirty)
            except AttributeError:
                warning("model - %s didn't have super_model", model.objectName())
            # try:
            # model.super_model().selection_in_progress.connect(self.set_selection_in_progress)
            # # model.super_model().try_select()
            # except AttributeError:
            #     debug("no selection_in_progress in model - ")  # %s", self.model().objectName())
            self._dirty_connected = True
        ret = super().setModel(model)
        return ret

    # def showEvent(self, ev):
    #     return super().showEvent(ev)

    def isDirty(self):
        return self._dirty

    def event(self, e: QEvent) -> bool:
        if e.type() == QEvent.FocusIn:
            SD.last_table = self
            self.init_model()
        return super().event(e)

    def keyPressEvent(self, ev: QKeyEvent):
        self.debug_event_handler(ev)
        # if ev.matches(self.topLevelWidget().qa_copy_shift):
        #     self.copy(Qt.EditRole)
        # el
        modifiers = ev.modifiers()
        if modifiers & Qt.ShiftModifier and modifiers & Qt.ControlModifier and ev.key() == Qt.Key_C:
            # if event.key() == Qt.Key_C and (event.modifiers() & Qt.ControlModifier):
            # if modifiers & Qt.ControlModifier:
            # if ev.matches(QKeySequence.Copy):
            self.copy_edit()
        elif ev.matches(QKeySequence.Copy):
            self.copy()
        # elif ev.matches(self.copy_edit_keys):
        # elif self.copy_edit_keys.matches(ev.key()):
        #     self.copy_edit()
        elif ev.matches(QKeySequence.Paste):
            self.paste()
        else:
            super().keyPressEvent(ev)

    @try_wrapper
    def mousePressEvent(self, ev: QMouseEvent):
        ret = super().mousePressEvent(ev)
        try:
            if ev.button() == Qt.LeftButton:
                mdl = self.model()
                debug("=====clicked on table %s =====", self.objectName())
                # index=self.selectionModel().selectedIndexes()[0]
                index = self.indexAt(ev.pos())
                if index.isValid():
                    debug("row - %s, col - %s", index.row(), index.column())
                while mdl:
                    if isinstance(mdl, tsQsfpModel):
                        debug("filter %s = %s", mdl.objectName(), mdl.currentFilterRegularExpression())
                        debug("dynfilt %s ", mdl.dynamicSortFilter())
                        debug("column %s ", mdl.filterKeyColumn())
                        mdl = mdl.sourceModel()
                    else:
                        debug("model %s, filter - %s ", mdl.objectName(), mdl.super_model().filter())
                        debug("model %s, statement - %s ", mdl.objectName(), mdl.super_model().selectStatement())
                        mdl = False
        except AttributeError:
            pass
        return ret

    @try_wrapper
    def copy(self, role=Qt.DisplayRole):
        #############################
        # check selection
        # ---------------------------
        selection: QItemSelectionModel = self.selectionModel()
        indexes: [QModelIndex] = selection.selectedIndexes()
        if len(indexes) < 1:
            return
        elif len(indexes) == 1:
            md = QMimeData()
            md.setText(str(indexes[0].data(role)))
            QApplication.instance().clipboard().setMimeData(md)
        #############################
        # get table with data
        # ---------------------------
        table_indexes = DynamicList(DynamicList(""))
        for ind in indexes:
            if self.super_model().tsFieldTypes[ind.column()] == "date":
                table_indexes[ind.row()][ind.column()] = ind.data(Qt.EditRole).toString("dd.MM.yyyy")
            else:
                table_indexes[ind.row()][ind.column()] = ind.data(role)
        table_indexes.shrink_2dtable()
        #############################
        # prepare strings
        # ---------------------------
        selected_as_html = "<html><style>br{mso-data-placement:same-cell;}</style><table>"  # body?
        selected_as_txt = ""
        # TODO: use custum string conversion method
        for row in table_indexes:
            selected_as_html += "<tr>" + "".join(["<td>" + str(el) + "</td>" for el in row]) + "</tr>"
            selected_as_txt += "".join([str(el) + "\t" for el in row]) + "\n"
        selected_as_html += "</table></html>"
        #############################
        # return QMimeData
        # ---------------------------
        md = QMimeData()
        md.setText(selected_as_txt)
        md.setHtml(selected_as_html)
        QApplication.instance().clipboard().setMimeData(md)

    def paste(self):
        if self.inited:
            clipboard = QApplication.clipboard().text()
            selection: QItemSelectionModel = self.selectionModel()
            indexes: [QModelIndex] = selection.selectedIndexes()
            return paste_to_model(indexes, None, self)

    # def super_model(self) -> tsSqlTableModel:
    #     # this is just a stub
    #     return self.model()

    @Slot(QShowEvent)
    def showEvent(self, ev):
        # ret=super().showEvent(ev)
        if self.model():
            self.col_adjust()
        return super().showEvent(ev)

    @Slot(bool)
    def copy_edit(self, b=True):
        self.copy(Qt.EditRole)

    @Slot(bool)
    def setDirty(self, dirty=True):
        """set dirty for self and all parent"""
        if self._dirty == dirty:
            return
        info("Set dirty myQTableView %s", self.objectName())
        #############################
        # set parent dirty
        # ---------------------------
        self._dirty = dirty
        par: QObject = self.parent()
        while par:
            try:
                par.setDirty(dirty)
            except:
                pass
                # debug("no _dirty property in %s", par.objectName())
            par = par.parent()
        #############################
        # set filters
        # ---------------------------
        for key, flt in self.filters.items():
            flt.setDynamicSortFilter(not dirty)

    @Slot()
    def visibleDataChangedEmit(self):
        self.dataChanged(self.indexAt(QPoint(0, 0)),
                         self.indexAt(QPoint(
                             self.viewport().size().width(), self.viewport().size().height()
                         )), [Qt.DisplayRole])

    def paintEvent(self, e: QPaintEvent):
        if not self.model() or not self.inited:
            self.init_model()
            painter = QPainter(self.viewport())
            painter.save()
            rect = e.rect()
            pstr = self.tr("Нет данных")
            font = QApplication.instance().font()
            br = QBrush(QColor(190, 190, 100), Qt.Dense7Pattern)
            painter.fillRect(rect, br)
            font.setPointSize(font.pointSize() + 6)
            painter.setFont(font)
            painter.drawText(rect, 8 | Qt.AlignCenter, pstr)
            painter.restore()
        elif self.selection_in_progress:
            if self.model():
                if not self.model().super_model().tsFieldNames:
                    painter = QPainter(self.viewport())
                    painter.save()
                    rect = e.rect()
                    pstr = self.tr("Нет доступа")
                    font = QApplication.instance().font()
                    br = QBrush(QColor(190, 190, 100), Qt.Dense7Pattern)
                    painter.fillRect(rect, br)
                    font.setPointSize(font.pointSize() + 6)
                    painter.setFont(font)
                    painter.drawText(rect, 8 | Qt.AlignCenter, pstr)
                    painter.restore()
                else:
                    painter = QPainter(self.viewport())
                    painter.save()
                    rect = e.rect()
                    pstr = self.tr("Идет запрос данных")
                    font = QApplication.instance().font()
                    br = QBrush(QColor(190, 190, 100), Qt.Dense7Pattern)
                    painter.fillRect(rect, br)
                    font.setPointSize(font.pointSize() + 6)
                    painter.setFont(font)
                    painter.drawText(rect, 8 | Qt.AlignCenter, pstr)
                    painter.restore()
        else:
            return super().paintEvent(e)


class tsQTableViewYear(tsQTableView):
    _selectionChanged: Signal = Signal(QItemSelection, QItemSelection)

    def __init__(self, *a, **kw):
        super().__init__(*a, **kw)
        self.inited = False
        # TODO: resize by header width
        # self.resizeColumnToContents(0)
        # self.resizeColumnToContents(2)
        # self.resizeColumnToContents(3)
        # self.resizeColumnToContents(4)
        # self.setSortingEnabled(False)
        self.last_sel_model = None

    @Slot()
    def focusInEvent(self, ev):
        if self.last_sel_model != self.selectionModel():
            self.last_sel_model = self.selectionModel()
            ret = super().focusInEvent(ev)
            self.last_sel_model.selectionChanged.connect(self.on_sel_activated)
            return ret
        super().focusInEvent(ev)
        self.last_sel_model.selectionChanged.connect(self.on_sel_activated)

    @Slot(QItemSelection, QItemSelection)
    def on_sel_activated(self, inds: QItemSelection, inds_old: QItemSelection):
        self._selectionChanged.emit(inds, inds_old)

    # @try_wrapper
    def debug_event_handler(self, e: QKeyEvent):
        pass
        # return tsFilteredModel.debug_event_handler(self, e)

    # @Slot("QShowEvent")
    # def showEvent(self, ev):
    #     return super().showEvent(ev)

    def init_model(self, val=True):
        # QMutexLocker(self.locks("init_model"))
        if not self.inited:
            # self.init_model_filter()
            # self.model().init_model_filter()
            super().init_model(True)
        if self.inited and not isinstance(self.itemDelegate(), tsItemDelegate):
            #############################
            # set Delegate
            # ---------------------------
            self.setItemDelegate(tsItemDelegate(self))
        return True

    # def init_model_filter(self):
    #     return self.model().init_model_filter()

    def super_model(self):
        if hasattr(self.model(), "gmdata"):
            return self.model().gmdata  # TODO: fix this ugly hack
        else:
            error("no gmdata")

    @Slot(str, int)
    def set_contract_id(self, col_name, id0):
        if self.model().contract_id != id0:
            self.init_model()
            self.model().contract_id = id0


class _myQTableView(tsQTableView, tsFilteredModel):
    __metaclass__ = tsQTableView


class myQTableView(_myQTableView):  # _myQTableView , tsFilteredModel
    # TODO: add indicator for used filters
    # __metaclass__ = QTableView
    def __init__(self, *a, **kw):
        super().__init__(*a, **kw)
        self.ts__init__()
        #############################
        # Setup
        # ---------------------------
        self.setSortingEnabled(True)
        #############################
        # vars
        # ---------------------------
        # self.shown = False

    @Slot()
    def select_model_data(self):
        if self.inited:
            self.super_model().select()

    @Slot(QShowEvent)
    def showEvent(self, ev):
        self.init_model()
        if self.model():
            self.apply_delayed_filters()
            self.super_model().update_data()
        return super().showEvent(ev)

    def init_model(self, val=None):
        with QMutexLocker(self.locks("init_model")):
            if not self.inited:
                self.init_model_filter()
                super().init_model(True)
            if self.inited and type(self.itemDelegate()) != tsItemDelegate:
                #############################
                # set Delegate
                # ---------------------------
                self.setItemDelegate(tsItemDelegate(self))
            return True

    @Slot(bool)
    def disable_filters(self, disabled=False):
        if disabled:
            self.setBackgroundRole(Qt.gray)
        else:
            self.setBackgroundRole(self.parent().backgroundRole())
        super().disable_filters(disabled)

    def model(self) -> tsSqlTableModel:
        return super().model()


class DepQTableView(tsDependable, myQTableView):  # _myQTableView , tsFilteredModel
    pass
    # @Slot("QShowEvent")
    # def showEvent(self, ev):
    #     super(QTableView, self).showEvent(ev)


class add_info_QTableView(myQTableView):
    @Slot(int, str)
    def set_curFIO(self, id0, model_name):
        if self.model():
            if id0:
                from logic.data_worker import WD
                val = WD.get_data_from_model_name("ufio", "ufio", id0)
                dic = {"curFIO": val}
                qry_str = """
                    SELECT psp, address
                    from 
                    add_info ai
                    join  contracts c on ai.contracts_id = c.id
                    where c.ufio_id = {}
                    order by pddate desc
                    limit 1
                    """.format(id0)
                qry = tsQuery()
                qry.exec_(qry_str)
                qry.next()
                dic["psp"] = qry.value(0)
                dic["address"] = qry.value(1)
                self.super_model().set_new_rec_autofill(**dic)


class wsQTableView(myQTableView):
    selectionChanged0: Signal = Signal(str, int)
    selectionChanged1: Signal = Signal(str, int)

    def __init__(self, *a, **kw):
        super().__init__(*a, **kw)
        self.last_sel_model = None

    @Slot()
    def focusInEvent(self, ev):
        if self.last_sel_model != self.selectionModel():
            self.last_sel_model = self.selectionModel()
            self.last_sel_model.selectionChanged.connect(self.on_sel_activated)
            debug("wsQTableView inited")
        super().focusInEvent(ev)

    @Slot(QItemSelection, QItemSelection)
    def on_sel_activated(self, inds: QItemSelection, inds_old: QItemSelection):
        self.selectionChanged0.emit(self.objectName(), 0)
        self.selectionChanged1.emit(self.objectName(), 1)


@try_wrapper
@reloader
def paste_to_model(indexes, model: tsSqlTableModel = None, view=None):
    """
    Paste text table(clipboard), into model starting from indexes[0]
    :param indexes:
    :param model:
    :param view:
    :return:
    """
    #############################
    # checks parameters
    # ---------------------------
    if len(indexes) == 0:
        UI.QMessageBox.information(UI, UI.tr("Ошибка"),
                                   UI.tr(""" Укажите куда вставлять!"""))
        return
    if not model:
        model = indexes[0].model()
        if hasattr(model, "super_model"):
            model = model.super_model()
    #############################
    # clipboard text to table and get borders
    # ---------------------------
    clipboard = QApplication.clipboard().text()
    if clipboard == "":
        return
    src_table = []
    src_border = Dimensions(0, 0, 0, 0)
    # src_table = DynamicList(DynamicList(""))
    #
    # src_table.shrink_2dtable()
    if clipboard[-1] in ("\t", "\n"):
        clipboard = clipboard[:-1]
    if clipboard[-1] in ("\t", "\n"):
        clipboard = clipboard[:-1]
    for crow in clipboard.split("\n"):
        if crow and crow != "\t":  # other checks
            ins_row = []
            if crow[-1] == "\t":
                crow = crow[:-1]
            for value in crow.split("\t"):
                ins_row.append(value)
            if ins_row:
                src_table.append(ins_row)
                if not src_border.right:
                    src_border.right = len(ins_row)
    src_border.down = len(src_table)
    #############################
    # organize indexes to rows and get borders
    # ---------------------------
    dst_rows = defaultdict(lambda: list())
    dst_border = Dimensions(-1, -1, -1, -1)
    for ind in indexes:
        dst_rows[ind.row()].append(ind)
        if ind.row() < dst_border.up:
            dst_border.up = ind.row()
        if ind.row() + 1 > dst_border.down:
            dst_border.down = ind.row() + 1
            if dst_border.up < 0:
                dst_border.up = ind.row()
        if ind.column() < dst_border.left:
            dst_border.left = ind.column()
        if ind.column() + 1 > dst_border.right:
            dst_border.right = ind.column() + 1
            if dst_border.left < 0:
                dst_border.left = ind.column()
    for row in dst_rows.values():
        row.sort(key=lambda x: x.column())
    #############################
    # check continues indexes
    # ---------------------------
    no_holes_dst_table = True
    first_row = next(iter(dst_rows.values()))
    first_key = next(iter(dst_rows.keys()))
    # rows continues and all rows has same length
    for k, r in enumerate(dst_rows.keys()):
        if k + first_key != r:
            no_holes_dst_table = False
            break
        if len(dst_rows[r]) != len(first_row):
            no_holes_dst_table = False
            break  # #
    # all elements aligned by columns
    for i, index in enumerate(first_row):
        for r, row in enumerate(dst_rows.values()):
            if row[i].column() != index.column():
                no_holes_dst_table = False
                break
    if not no_holes_dst_table:
        UI.QMessageBox.information(UI, UI.tr("Ошибка"),
                                   UI.tr("""Выделите непрерывный диапазон ячеек"""))
        return
    #############################
    # backup default values
    # ---------------------------
    if src_table:
        SD.unsaved_view = view  # TODO: make obsolete
    old_defaults = model.default_values
    #############################
    # edit rows
    # ---------------------------
    # new_rows_flag = False
    if model.special_row == dst_border.down:
        dst_border.down = dst_border.up + len(src_table)
        # new_rows_flag = True
    # new_row=model.special_row
    for dr, sr in zip(range(dst_border.up, dst_border.down), range(src_border.up, src_border.down)):
        for dc, sc in zip(range(dst_border.right - dst_border.left), range(src_border.left, src_border.right)):
            #############################
            # last check
            # ---------------------------
            ind = dst_rows[dr][dc]
            # if ind.column() != dc or ind.row() != dr:
            #     error("index != dr/dc")
            #############################
            # get source index and update it
            # ---------------------------
            index = mapToSuper(ind)
            try:
                SD.start_edit(view, model, model.row_id(index.row()),
                              model.tsFieldNames[index.column()])
                value = src_table[sr][sc]
                #############################
                # set with type check
                # ---------------------------
                if index.column() in model.relColumns and model._relations_used:
                    #############################
                    # for relational value - get id
                    # ---------------------------
                    if isinstance(value, int):
                        pass
                    elif isinstance(value, str):
                        try:
                            value = int(value)
                        except ValueError:
                            pass
                    else:
                        debug("wrong value for column %s - value %s", ind.column(), value)
                    if isinstance(value, str):
                        value = model.id_of_related_by_value(value, index.column())
                    model.setData(index, value, Qt.EditRole)
                elif "int" in model.tsFieldTypes[index.column()]:
                    #############################
                    # set int
                    # ---------------------------
                    try:
                        value = int(value)
                        model.setData(index, value, Qt.EditRole)
                    except ValueError:
                        pass
                elif "float" in model.tsFieldTypes[index.column()]:
                    #############################
                    # set float
                    # ---------------------------
                    try:
                        value = float(value.replace(",", "."))
                        model.setData(index, value, Qt.EditRole)
                    except ValueError:
                        pass
                elif model.tsFieldTypes[index.column()] == "date":
                    #############################
                    # set date
                    # ---------------------------
                    try:
                        try:
                            value = QDate().fromString(value, Qt.DefaultLocaleShortDate)
                        except ValueError:
                            value = QDate().fromString(value, Qt.DefaultLocaleShortDate)
                    except ValueError:
                        debug("wrong date for column %s - value %s", ind.column(), value)
                    model.setData(index, value, Qt.EditRole)
                # #############################
                # # set data
                # # ---------------------------
                # model.setData(index, value, Qt.EditRole)
            except ValueError:
                debug("paste data value error for col - %s, value - %s", ind.column(), value)
                pass
            # SD.commit_edit(model, index.data(Qt.EditRole), ins_table[sr][sc])
    model.default_values = old_defaults
    return True


@try_wrapper
@reloader
def paste_planned(view: tsQTableView):
    """
    Paste text table(clipboard), into model
    """
    # TODO: maybe replace if exists?
    #############################
    # checks model inited
    # ---------------------------
    COLLS = 8
    CHECKBOXUNSET = "  "
    from logic.data_worker import WD
    model: tsSqlTableModel = view.super_model()
    if not model.default_values["contracts_id"]:
        QMessageBox.critical(UI.main_window, UI.main_window.tr("Не выбран договор!"),
                             UI.main_window.tr("Выберите договор и повторите попытку!"))
        return
    contracts_id = model.default_values["contracts_id"]
    #############################
    # get clipboard text, TODO: use html,
    # right now we use dirty hack - there is two space if checkbox is not set
    # ---------------------------
    clipboard = QApplication.clipboard().text()
    if clipboard == "":
        return
    #############################
    # cut malformed lines
    # ---------------------------
    if clipboard[0] == "\n":
        clipboard = clipboard[1:]
    if clipboard[-1] == "\n":
        clipboard = clipboard[:-1]
    crows = clipboard.split("\n")
    if len(crows[0].split("\t")) < COLLS:
        crows = crows[1:]
    if len(crows[0].split("\t")) < COLLS:  # cut twice
        crows = crows[1:]
    if len(crows[-1].split("\t")) < COLLS:
        crows = crows[:-1]
    if len(crows[-1].split("\t")) < COLLS:
        crows = crows[:-1]
    if crows[0].split("\t")[1] == "Номер услуги":
        crows = crows[1:]
    #############################
    # parse
    # ---------------------------
    services = []
    skipped = 0
    for crow in crows:
        cells = crow.split("\t")
        if len(cells) < COLLS:
            return
        if cells[3] == CHECKBOXUNSET or cells[4] == CHECKBOXUNSET:
            skipped += 1
            continue
        #############################
        # parse cell values
        # ---------------------------
        planned = 0
        try:
            planned = int(cells[5].strip())
        except:
            skipped += 1
            continue
        filled = 0
        try:
            filled = int(cells[7].strip())
        except ValueError:
            pass
        #############################
        # add to list
        # ---------------------------
        services.append(
            {
                "planned": planned,
                "filled": filled,
                "serv_id": cells[2].strip(),
                "contracts_id": contracts_id
            }
        )
    for s in services:
        try:
            serv_id = WD.models("_serv_activ").index_by_id(s["serv_id"], "serv_text")[0].siblingAtColumn(0).data(
                Qt.EditRole)
            s["serv_id"] = serv_id
        except:
            s["prim"] = s["serv_id"]
            s["serv_id"] = ""
    #############################
    # backup default values
    # ---------------------------
    old_defaults = model.default_values
    #############################
    # add rows
    # ---------------------------
    col = model.index_of_col("contracts_id")  # just any column
    for s in services:
        model.default_values = s
        contracts_id = model.default_values["contracts_id"]
        model.default_values["contracts_id"] = 0
        index = model.index(model.special_row, col)
        SD.start_edit(view, model, model.row_id(index.row()), "contracts_id")
        # ce = model.insert_row(s)  # use this for speed + manual commitAll()
        model.setData(index, contracts_id, Qt.EditRole)
    #############################
    # restore default_values
    # ---------------------------
    model.default_values = old_defaults
    return True
