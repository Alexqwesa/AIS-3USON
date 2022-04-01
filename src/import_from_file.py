import json
from itertools import count
from logging import debug, error
from os import path

from qtpy.QtCore import QUrl
from qtpy.QtWidgets import QFileDialog
from qtpy.QtCore import Qt
from qtpy.QtCore import QAbstractTableModel

from helper_func import Qtimer_runner
from logic.data_worker import WD
from models.ts_models import tsSqlTableModel
from safe_shared_data import UI


class ImportJsonModel(QAbstractTableModel):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.json_import = []
        # self.json_import.json_import_changed.connect(self.update_view)
        self.rc = 1
        self.__col_count = count()
        self.IN = next(self.__col_count)
        self.state = next(self.__col_count)
        self.UID = next(self.__col_count)
        self.serv_id = next(self.__col_count)
        self.worker_id = next(self.__col_count)
        self.contract_id = next(self.__col_count)
        self.client_id = next(self.__col_count)
        self.vdate = next(self.__col_count)
        self.file_name = next(self.__col_count)
        self.error = next(self.__col_count)

    def headerData(self, section: int, orientation: Qt.Orientation, role: int = Qt.DisplayRole):
        if orientation == Qt.Horizontal and role in (Qt.DisplayRole, Qt.ToolTipRole):
            if section == self.IN:
                return self.tr("Внесено")
            elif section == self.state:
                return self.tr("Статус")
            elif section == self.UID:
                return self.tr("uid")
            elif section == self.serv_id:
                return self.tr("Услуга")
            elif section == self.worker_id:
                return self.tr("Работник")
            elif section == self.contract_id:
                return self.tr("№ контракта")
            elif section == self.client_id:
                return self.tr("Получатель СУ")
            elif section == self.vdate:
                return self.tr("Дата")
            elif section == self.file_name:
                return self.tr("Имя файла")
            elif section == self.error:
                return self.tr("Сообщение")
        return super().headerData(section, orientation, role)

    def update_view(self):
        Qtimer_runner(self._update_view, 1000, "ImportJsonModel")

    def _update_view(self):
        debug(f"inserted {self.rowCount() - self.rc} at {self.rc}")
        # self.beginInsertRows(QModelIndex(), self.rc, self.rowCount())
        # self.rc = self.rowCount()
        # self.endInsertRows()
        self.layoutChanged.emit()
        # self.resetInternalData()

    def rowCount(self, parent=None):
        # return self.rc
        return len(self.json_import)

    def columnCount(self, parent=None):
        return self.error

    def data(self, index, role=Qt.DisplayRole):
        contracts_model = WD.models("contracts")
        col = index.column()
        row = self.json_import[index.row()]
        if role in [Qt.DisplayRole, Qt.ToolTipRole]:
            if col == self.IN:
                return row["IN"]
            if col == self.state:
                return row["state"]
            elif col == self.UID:
                return row["uid"]
            elif col == self.serv_id:
                return WD.models("client").data_by_id(row["servId"], 1)
            elif col == self.worker_id:
                return WD.models("dep_has_worker").data_by_id(row["workerId"], 1)
            elif col == self.contract_id:
                return WD.models("contracts").data_by_id(row["contractId"], 1)
            elif col == self.client_id:
                return WD.models("client").data_by_id(
                    contracts_model.data_by_id(row["contractId"], contracts_model.index_of_col("client_id")), 1)
            elif col == self.vdate:
                return row["provDate"]
            elif col == self.file_name:
                return row["file_name"]
            elif col == self.error:
                return row["error"]

    def import_services_from_file(self, file: QUrl):
        try:
            with open(file.toLocalFile(), "r") as f:
                json_list = json.load(f)
            if isinstance(json_list, list):
                dhw: tsSqlTableModel = WD.models("dep_has_worker")
                imain: tsSqlTableModel = WD.models("api_key_insert_main")
                api_key = json_list[0]["api_key"]
                json_list = json_list[1:]
                api_key_from_db = dhw.get_index_by_id(api_key, dhw.index_of_col("api_key")).data(Qt.EditRole)
                for el in json_list:
                    el["workerId"] = dhw.get_index_by_id(api_key, dhw.index_of_col("api_key")).siblingAtColumn(
                        dhw.index_of_col("dep_has_worker_id")).data(Qt.EditRole)
                    el["file_name"] = path.basename(file.toLocalFile())
                    if api_key_from_db != api_key:
                        el["IN"] = "Worker not found"
                    try:
                        imain.get_index_by_id(el["uid"], imain.index_of_col("uuid")).data(Qt.EditRole)
                        el["IN"] = "Exist"
                    except IndexError:
                        el["IN"] = "New"
                self.json_import += json_list

        except IndexError:
            error("Can't find api_key")
        except:
            error("Import Error")

    def import_services_from_files(self):
        files = QFileDialog.getOpenFileUrls(caption=UI.tr("Выберите файлы полученные от работников"),
                                            selectedFilter="*.aisjson",
                                            )
        for file in files:
            self.import_services_from_file(file[0])
