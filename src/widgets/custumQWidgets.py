#!/usr/bin/python3
# -------------------------------------------------------------------------------
# -*- coding: utf-8 -*-
# Name:        AIS 3USON Custum QT Widgets
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
from typing import Optional

#############################
# QT Libraries
# ---------------------------
from qtpy import QtWidgets
from qtpy.QtWidgets import QTabBar

from widgets.q_dock_info import *


class myQLineEdit(QtWidgets.QLineEdit):
    def __init__(self, *a, **kw):
        super().__init__(*a, **kw)
        self.setClearButtonEnabled(True)


class myQTabBar(QTabBar):
    def __init__(self, *a, **kw):
        super().__init__(*a, **kw)
        self.setStyleSheet("""QTabBar::tab:selected {                                    
                                    background-color: rgb(235, 245, 255);
                                    
                            }""")
        # color:  # 000000;
        # font - weight: 600; font: bold;
        # border: 50 px;
        # background - color: rgb(240, 240, 255);

    # def tabRect(self, index: int) -> QRect:
    #     rect: QRect = super().tabRect(index)
    #     rect.setX(rect.x() + 100)
    #     return rect
    #
    # def geometry(self) -> QRect:
    #     rect: QRect = super().geometry()
    #     rect.setX(rect.x() + 100)
    #     return rect


class myQTabWidget(QtWidgets.QTabWidget):
    widgetVisibilityChanged: Signal = Signal(bool)
    tabActivated: Signal = Signal(int, QWidget)

    def __init__(self, *a, **kw):
        super().__init__(*a, **kw)
        self._dirty = False
        self._list_of_widgets = []
        self.setTabBar(myQTabBar())
        self.setDocumentMode(True)

    def isDirty(self):
        return self._dirty

    def setDirty(self, dirty=True):
        if self._dirty != dirty:
            self._dirty = dirty
            ind = self.currentIndex()
            for i in range(0, self.count()):
                if i != ind:
                    if not isinstance(self.widget(i), myQWidgetUnblockable):
                        self.setTabEnabled(i, not dirty)

    def setCurrentWidget(self, widget):
        if not self._dirty:
            return super().setCurrentWidget(widget)

    def showEvent(self, ev):
        ret = super().showEvent(ev)
        self.widgetVisibilityChanged.emit(True)
        self.tabActivated.emit(self.currentIndex(), self.currentWidget())
        return ret

    def isTabVisibleFor(self, qwidget):
        # par = self.parent()
        # while not isinstance(par, QTabWidget)  and par:
        #     par = par.parent()
        # if (not par) or par.isTabVisibleFor(self):  # is needed ?
        if not self.isVisible():
            return False
        wname = qwidget.objectName()
        for tabw in self.list_of_widgets:
            if tabw.findChild(type(qwidget), wname):
                if tabw is self.currentWidget():
                    return True
                else:
                    return False
        return False

    @property
    def list_of_widgets(self) -> [QWidget]:
        # TODO: don't recount every time
        self._list_of_widgets = []
        for i in range(self.count()):
            self._list_of_widgets.append(self.widget(i))
        return self._list_of_widgets

    # def mousePressEvent(self, event:QMouseEvent):
    #     self.widgetVisibilityChanged.emit(True)
    #     return super().mousePressEvent(event)

    def set_active_tab_by_name(self, name: str) -> Optional[QWidget]:
        tab: QWidget = self.findChild(QWidget, name)
        try:
            ind = self.indexOf(tab)
            if ind == -1:
                error("tab - %s not found", name)
                return None
            self.setCurrentIndex(ind)
            QApplication.instance().processEvents()  # let init widgets in tab
            return tab
        except:
            return None


class myQWidget(QtWidgets.QWidget):
    widgetVisibilityChanged: Signal = Signal(bool)

    def __init__(self, *a, **kw):
        super().__init__(*a, **kw)
        self._dirty = False

    def isDirty(self):
        return self._dirty

    def setDirty(self, dirty=True):
        if self._dirty != dirty:
            self._dirty = dirty

    def showEvent(self, ev):
        UI.last_tab = self
        ret = super().showEvent(ev)
        self.widgetVisibilityChanged.emit(True)
        return ret

    def activate(self):
        """ Activate all parents tab from top """
        parents = list(reversed(self.parents()))
        parents.append(self)
        for par, _, widg in zip(parents, parents[1:], parents[2:]):
            # second is stackWidget
            if isinstance(par, myQTabWidget):
                par.set_active_tab_by_name(widg.objectName())

    def parents(self) -> [QObject]:
        par: QObject = self.parent()
        pars = []
        while par:
            pars.append(par)
            par = par.parent()
        return pars


class myQWidgetUnblockable(myQWidget):
    pass


class myQDateEdit(QDateEdit):
    @Slot()
    def plus_day(self):
        self.setDate(self.date().addDays(1))

    @Slot()
    def minus_day(self):
        self.setDate(self.date().addDays(-1))


class myQStackedWidget(QStackedWidget):
    @Slot()
    def next_tab(self):
        next_tab = self.currentIndex() + 1
        if next_tab >= self.count():
            next_tab = 0
        self.setCurrentIndex(next_tab)


# # TODO: lru_cache
# # @staticmethod


if __name__ == "__main__":
    pass
