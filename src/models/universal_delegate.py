from threading import Lock

from qtpy.QtCore import QTime
from qtpy.QtSql import QSqlRelationalDelegate
from qtpy.QtWidgets import QLineEdit, QSpinBox, QDoubleSpinBox, \
    QDateTimeEdit, QDateEdit, QPlainTextEdit, QStyledItemDelegate
from qtpy.QtWidgets import QStyleOptionViewItem

from models.ts_models_plus import *


class tsPureItemDelegate(QSqlRelationalDelegate):
    def __init__(self, parent):
        """Constructor for chkItemDelegate FOR CHECKBOX ONLY"""
        super().__init__(parent)
        self.pcindex = None
        self.cindex = None
        self.ctype = None
        self.cname = None
        self.cmodel = None

    def createEditor(self, parent: QWidget, option, index: QModelIndex):
        #############################
        # parse info
        # ---------------------------
        mdl = index.model()
        self.pcindex = index
        while isinstance(mdl, tsQsfpModel):
            index = mdl.mapToSource(index)
            mdl = index.model()
        if len(mdl.tsFieldNames) == 0:
            mdl.setMetaInfo()
        try:
            ctyp: str = mdl.tsFieldTypes[index.column()].lower()
            cnam: str = mdl.tsFieldNames[index.column()].lower()
        except IndexError:
            editor = QLineEdit(parent)
            return editor
        #############################
        # store last info
        # ---------------------------
        self.cindex = index
        self.ctype = ctyp
        self.cname = cnam
        self.cmodel = mdl
        #############################
        # create editor
        # ---------------------------
        if "tinyint" in ctyp:  # TODO: don't call for tableView !!!
            if isinstance(self.parent(), QTableView):
                return
            cbox = QCheckBox(parent)
            return cbox
        elif "varchar" in ctyp:
            editor = QLineEdit(parent)
            return editor
        elif "year" in ctyp:
            editor = QSpinBox(parent)
            editor.setMaximum(2100)
            editor.setMinimum(1901)
            return editor
        elif cnam[-3:] == "_id":
            if "_raw" == index.model().objectName()[-4:]:
                editor = QSpinBox(parent)
                editor.setMaximum(sys.maxsize)
                editor.setMinimum(0)
            else:
                editor = super().createEditor(parent, option, index)  # WTF?
                # editor = QComboBox(self.parent())
                if not isinstance(editor, QComboBox):
                    error("createEditor unexpected widget!")
                    return editor
                try:
                    # print_model_data(editor.model())
                    while editor.model().canFetchMore():
                        editor.model().fetchMore()
                except (AttributeError, TypeError):
                    debug("Delegate: no model")
                    return editor
                if isinstance(editor.model(), QSqlTableModel):
                    emdl = editor.model()
                    ename = editor.model().objectName()
                    #############################
                    # TODO: use fitered model
                    # ---------------------------
                    if not ename:
                        _, _, ename = editor.model().selectStatement().rpartition(" FROM ")
                        ename = "rel_" + ename
                        editor.model().setObjectName(ename)
                    try:
                        from logic.data_worker import WD
                        if WD.model_last_update(ename[4:]) > emdl.last_update:
                            editor.model().select()
                            emdl.last_update = QDateTime.currentDateTime()
                    except AttributeError:
                        editor.model().select()
                        emdl.last_update = QDateTime.currentDateTime()
                # ret = QSqlRelationalDelegate(parent).createEditor()
            return editor
        elif "int" in ctyp:
            editor = QSpinBox(parent)
            editor.setMaximum(99999)
            editor.setMinimum(0)
            return editor
        elif "float" in ctyp or "decimal" in ctyp or "double" in ctyp:
            editor = QDoubleSpinBox(parent)
            editor.setMaximum(999999)
            editor.setMinimum(0)
            editor.setDecimals(2)
            return editor
        elif "timestamp" in ctyp or "datetime" in ctyp:
            editor = QDateTimeEdit(parent)
            return editor
        elif "date" in ctyp:
            editor = QDateEdit(parent)
            return editor
        else:
            editor = QLineEdit(parent)
            return editor

    def setEditorData(self, editor, index: QModelIndex):
        # TODO: check data valid
        # if index.isValid():
        # TODO: Always directly check journal data
        #############################
        # set color
        # ---------------------------
        bg_color: QColor = index.data(Qt.BackgroundRole)
        if bg_color:
            editor.setStyleSheet("background-color: {};".format(bg_color.name()))
        else:
            editor.setStyleSheet("")
        # #############################
        # # get latest data
        # # ---------------------------
        # model: tsSqlTableModel = index.model().super_model()
        # try:
        #     if model.pending_edit[0] == index.model().mapToSuper(index):
        #         dat = model.pending_edit[1]
        #     else:
        #         raise TypeError
        # except TypeError:  # no latest data
        #     dat = index.data(Qt.EditRole)
        dat = index.data(Qt.EditRole)
        #############################
        # set data
        # ---------------------------
        if isinstance(editor, QDateEdit):
            try:
                dat = QDate(dat)
            except TypeError:
                dat = 0
            if dat:
                editor.setDate(dat)
            else:
                editor.setDate(QDate(1900, 1, 1))  # TODO: maybe use different date?
        elif isinstance(editor, QDateTimeEdit):
            dat = QDateTime(dat)
            if dat:
                editor.setDateTime(dat)
            else:
                editor.setDateTime(QDateTime(QDate(1900, 1, 1), QTime(0, 0, 0)))
        elif isinstance(editor, QCheckBox):  # not called in tableView - only QDataMapper
            if dat:
                editor.setCheckState(Qt.Checked)
            else:
                editor.setCheckState(Qt.Unchecked)
            # debug(val)
        elif isinstance(editor, QSpinBox):
            try:
                dat = int(dat)
            except (TypeError, ValueError):
                dat = 0
            editor.setValue(dat)
        elif isinstance(editor, QDoubleSpinBox):
            dat = float(dat)
            editor.setValue(dat)
        elif isinstance(editor, QLineEdit):
            editor.setText(
                str(dat))
        elif isinstance(editor, QComboBox):
            # while isinstance(index.model(), tsQsfpModel):
            #     proxy = index.model()
            #     index = proxy.mapToSource(index)
            super().setEditorData(editor, index)
            rel = index.model().super_model().relation(index.column())
            rel_mdl = editor.model()
            rel_col_name = rel.displayColumn()
            rcol = 1
            if rel_mdl.headerData(rcol, Qt.Horizontal, Qt.DisplayRole) != rel_col_name:
                return
            # rcol =  rel_mdl.fieldIndex(rel_col_name)
            # value = self.record(row).value(col)
            value = index.data(Qt.DisplayRole)
            # if value:
            try:
                rel_ind = rel_mdl.match(rel_mdl.index(0, rcol), Qt.EditRole,
                                        value, flags=Qt.MatchExactly)[0]
                editor.setCurrentIndex(rel_ind.row())
            except:  # in case relation set wrong
                try:
                    rel_ind = rel_mdl.match(rel_mdl.index(0, 0), Qt.EditRole,
                                            value, flags=Qt.MatchExactly)[0]
                    editor.setCurrentIndex(rel_ind.row())
                except:
                    error("rel_model no index found")
            # editor.setCurrentIndex(index.model().ind_of_related(dat).column())
        elif isinstance(editor, QPlainTextEdit):
            editor.setPlainText(str(dat))
        elif isinstance(editor, QWidget):
            pass
        else:
            return QStyledItemDelegate.setEditorData(
                editor, index)

    def setModelData(self, editor, model: QSortFilterProxyModel, index: QModelIndex):
        if index.isValid():
            val = None
            # old_value = index.data(Qt.EditRole)
            #############################
            # create pending journal entry
            # ---------------------------
            view = self.parent()
            smodel: tsSqlTableModel = view.model().super_model()
            SD.unsaved_view = view  # TODO: make obsolete
            sindex = index
            while sindex.model() != smodel:
                sindex = sindex.model().mapToSource(sindex)
            row_id = smodel.row_id(sindex.row())
            try:
                col_name = smodel.tsFieldNames[index.column()]
            except IndexError:
                error("unknown field -%s in view - %s ", index.column(), view)
                col_name = index.column()
            SD.start_edit(view, smodel, row_id, col_name)  # , old_value, val)
            #############################
            # set model data
            # ---------------------------
            if isinstance(editor, QPlainTextEdit):
                val = editor.toPlainText()
                ret = model.setData(index, val, Qt.EditRole)
            elif isinstance(editor, QLineEdit):
                val = editor.text()
                ret = model.setData(index, val, Qt.EditRole)
            elif isinstance(editor, QCheckBox):
                val = 0
                if editor.checkState() == Qt.Checked:
                    val = 1
                ret = model.setData(index, val, Qt.CheckStateRole)
            elif isinstance(editor, QSpinBox):
                val = editor.value()
                ret = model.setData(index, val, Qt.EditRole)
            elif isinstance(editor, QComboBox):
                ind = editor.currentIndex()
                ret = False
                if ind != -1:
                    val = editor.model().data(editor.model().index(ind, 0), Qt.EditRole)
                    model.setData(index, val, Qt.EditRole)
                    ret = True
                    # by default, related tables fetch only first 255 records... should be fixed...?
                elif isinstance(editor, QDateTimeEdit):
                    val = editor.dateTime()
                    ret = model.setData(index, val, Qt.EditRole)
            elif isinstance(editor, QDateEdit):
                val = editor.date()
                ret = model.setData(index, val, Qt.EditRole)
            else:
                ret = super(QSqlRelationalDelegate, self).setModelData(
                    editor, model, index)
        else:
            ret = super(QSqlRelationalDelegate, self).setModelData(
                editor, model, index)
        return ret

    def updateEditorGeometry(self, editor: QCheckBox, option: QStyleOptionViewItem, index: QModelIndex):
        editor.setGeometry(option.rect)


class tsItemDelegate(tsPureItemDelegate):
    """
    Fine tuning for project models
    """

    def __init__(self, parent=None):
        super().__init__(parent)
        self.add_info_contracts = None
        self.lock = Lock()
        self.last_widget: QWidget = None

    def createEditor(self, parent: QWidget, option, index: QModelIndex):
        #############################
        # check prev editor still active
        # ---------------------------
        with self.lock:
            if self.last_widget:
                if self.last_widget.isVisible():
                    return None
        #############################
        # get editor
        # ---------------------------
        editor = super().createEditor(parent, option, index)
        #############################
        # data aware checks
        # ---------------------------
        if self.pcindex:
            if self.pcindex is index:
                if self.cmodel and self.cmodel.info:
                    if self.cmodel.info.cut_name == "main":
                        #############################
                        # don't allow change some fields after save
                        # ---------------------------
                        if self.cmodel.row_id(self.pcindex.row())[:3] != "new_":
                            if self.cname in ["serv_id", "dep_id", "contracts_id", "ufio_id"]:
                                return
                        #############################
                        # only show workers from department
                        # ---------------------------
                        if self.cname == "worker_id":
                            from logic.data_worker import WD
                            editor.setModel(WD.models("_dep_has_workers"))
                    if self.cmodel.info.cut_name == "add_info":
                        if self.cname == "contracts_id":
                            #############################
                            # show only contracts with same ufio
                            # ---------------------------
                            if "_by_ufio_id" in self.parent().objectName() or "_where_ufio_id" in self.parent().objectName():
                                if not self.add_info_contracts:
                                    self.add_info_contracts = tsQsfpModel_no_new(self, "private_contracts", "_contracts")
                                # editor.setModelColumn(self.add_info_contracts.super_model().tsFieldNames.index("contracts"))
                                self.add_info_contracts.setFilterKeyColumn(
                                    self.add_info_contracts.super_model().tsFieldNames.index("ufio_id"))
                                self.add_info_contracts.setFilterRegularExpression(
                                    "^" + str(self.parent().super_model().default_values["ufio_id"]) + "$")
                                editor.setModel(self.add_info_contracts)
        return editor
