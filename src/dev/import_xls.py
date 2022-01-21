#!/usr/bin/python3
# -------------------------------------------------------------------------------
# -*- coding: utf-8 -*-
# Name:        AIS 3USON module to read xls files
# Purpose:
#
# Author:      Savin Alexander Viktorovich aka alexqwesa
# Created:     2019-2020
# Copyright:   Savin Alexander Viktorovich aka alexqwesa
# Licence:     LGPL 3
# This software is licensed under the "LGPLv3" License as described in the "LICENSE" file,
# which should be included with this package. The terms are also available at
# http://www.gnu.org/licenses/lgpl-3.0.html
# -------------------------------------------------------------------------------
import calendar
from datetime import date
from typing import Union

import pandas as pd
import sqlalchemy
from qtpy.QtWidgets import QFileDialog
from sqlalchemy import and_, select, between
from sqlalchemy.exc import OperationalError, ProgrammingError
from sqlalchemy.orm.exc import NoResultFound, MultipleResultsFound

from dev.logger_setup import debug, error, critical
from safe_shared_data import UI, SD
from models.orm import Updatable_contracts as Contracts, Updatable_client as Client, Updatable_add_info as Add_info, \
    Ripso, Client_has_category, Serv, main, updatable_main, Worker
import os
from thirdparty.levenshtein import levenshtein

pd.options.mode.use_inf_as_na = True


def select_xls_file():
    file_name = QFileDialog.getOpenFileName(UI.main_window,
                                            UI.tr("Открыть файл Excel"), "",
                                            UI.tr("Excel Files (*xlsx *.xls *.xlsm *.xlsb)"))
    return file_name


def read_xls(file):
    """

    :param file: full file path
    :return: DataFrames: dfio, dcontracts, duhc, dainfo, dmain, dmetainfo

    >>> read_xls( os.path.join(os.getcwd() , "tests","export_for_3uson.xlsx"))[0]
         ippsuNum client  ... phone           snils
    0  3333333333       ...        333-123-333-85
    1  2222222222       ...        233-123-124-85
    2  1111111111       ...        133-123-123-85
    <BLANKLINE>
    [3 rows x 10 columns]
    >>> read_xls( os.path.join(os.getcwd() , "tests","export_for_3uson.xlsx"))[1]
                      contracts_id  contracts  ...  startdate    enddate
    0  Батестова бария Бавтестовна  123456783  ... 2020-01-09 2021-03-09
    1     Атестова ария Автестовна  123456782  ... 2020-01-09 2021-01-09
    2         Тестов тевт Тертович  123456781  ... 2020-01-09 2021-01-09
    <BLANKLINE>
    [3 rows x 9 columns]
    """
    dmetainfo = pd.read_excel(file, sheet_name="metainfo").fillna('')
    dfio = pd.read_excel(file, sheet_name="client").fillna('')  # , inplace=True
    # dfio.insert(9, 'curator', dmetainfo["dep"][0])
    dfio.insert(5, 'client_id', "")
    dcontracts = pd.read_excel(file, sheet_name="contracts").fillna('')
    duhc = pd.read_excel(file, sheet_name="client_has_category", dtype=object).fillna('')
    dainfo = pd.read_excel(file, sheet_name="add_info").fillna('')
    dmain = pd.read_excel(file, sheet_name="main").fillna('')
    return dfio, dcontracts, duhc, dainfo, dmain, dmetainfo


def parse_data_frame(data_frame: pd.DataFrame, cls, with_save=True):
    """


    :param data_frame:
    :param cls: parse data frame as data class cls
    :param with_save:
    :return:

    >>> dfio, dcontracts, *_ = read_xls(os.path.join(os.getcwd(), "tests", "export_for_3uson.xlsx"))
    >>> SD.engine.echo = False
    >>> clients = parse_data_frame(dfio, ClientCheck, False)
    status - updated, for - Батестова бария Бавтестовна
    status - updated, for - Атестова ария Автестовна
    status - updated, for - Тестов тевт Тертович
    >>> dcontracts.insert(8, "year", 2020)
    >>> _ = parse_data_frame(dcontracts, ContractCheck, False)
    status - failed - different client_id, for - 123456783/2020 at 2020-01-09
    status - failed - different client_id, for - 123456782/2020 at 2020-01-09
    status - failed - different client_id, for - 123456781/2020 at 2020-01-09
    >>> for i in range(len(clients)):
    ...     dcontracts.loc[i, "client_id"] = clients.loc[i, "id"]
    >>> _ = parse_data_frame(dcontracts, ContractCheck, False)
    status - updated, for - 123456783/2020 at 2020-01-09
    status - updated, for - 123456782/2020 at 2020-01-09
    status - updated, for - 123456781/2020 at 2020-01-09
    """
    # status - new, for - 123456783/2020 at 2020-01-09
    # status - new, for - 123456782/2020 at 2020-01-09
    # status - new, for - 123456781/2020 at 2020-01-09

    data_frame = cls.data_frame_precheck(data_frame)
    # record_ids = []
    for i, drow in data_frame.iterrows():
        #############################
        # prepare
        # ---------------------------
        drow = cls.drow_precheck(drow)
        status, record = cls.new_with_dup_check(drow)
        #############################
        # save
        # ---------------------------
        if with_save:
            ret, record = cls.save(status, record, drow)
            if ret is False:
                return False
        else:
            SD.session.rollback()
        #############################
        # return
        # ---------------------------
        if status in ["new", "updated", "exist"]:
            try:
                id = record.id
                drow.at["id"] = id
                # if "id" not in data_frame.keys():
                #     data_frame.insert(len(data_frame.keys()), "id", 0)
                data_frame.loc[i, "id"] = id
                data_frame.loc[i, "client"] = record.client
            except AttributeError:
                pass
        data_frame.update(drow, )
        cls.status_print(status, record)
    return data_frame


class Rec:
    pass


class Check:
    @classmethod
    def save(cls, status, record, drow):
        try:
            if status == "new":
                SD.session.add(record)
            elif status == "updated":
                cls.update_rec(record, drow)
            SD.session.commit()
        except sqlalchemy.exc.ProgrammingError:
            debug("rollback : %s", cls.__name__)
            SD.session.rollback()
            return False, record
        return True, record

    @staticmethod
    def drow_precheck(drow: pd.Series):
        return drow

    @staticmethod
    def data_frame_precheck(df: pd.DataFrame):
        return df

    @staticmethod
    def transpose(drow: pd.Series):
        return []

    @staticmethod
    def status_print(status, record):
        pass

    @staticmethod
    def new_with_dup_check(drow):
        pass

    @staticmethod
    def same_additional_checks(drow, rec):
        return "updated", rec

    @staticmethod
    def update_rec(rec, drow, only_this_fields: Union[bool, list] = False):
        pass


class ContractCheck(Check):
    """
    TODO: maybe add second contract for first half of year?

    """

    @staticmethod
    def drow_precheck(drow: pd.Series):
        """
        Fix row imported from xls file
        :param drow: pd.Series
        :return: drow: pd.Series

        >>> SD.engine.echo = False
        >>> ContractCheck.drow_precheck( pd.Series({"client_id": 1, "dep_id" : 1 , "year": 2020, "contracts": 1232132, \
             "ripso_id": "1|Старое рипсо 2019 года|", "startdate":pd.Timestamp('2020-01-01') , "enddate": ""}))
        client_id                 1
        dep_id                  1
        year                 2020
        contracts    1232132/2020
        ripso_id               13
        startdate      2020-01-01
        enddate        1900-01-01
        dtype: object

        """
        #############################
        # precheck - data fix
        # ---------------------------
        try:
            drow.at["startdate"] = drow.at["startdate"].to_pydatetime().date()
        except AttributeError:
            drow.at["startdate"] = date(1900, 1, 1)
        try:
            drow.at["enddate"] = drow.at["enddate"].to_pydatetime().date()
        except AttributeError:
            drow.at["enddate"] = date(1900, 1, 1)
        #############################
        # precheck contract name
        # ---------------------------
        if not drow.at["contracts"]:
            drow.at["contracts"] = str(drow.at["client_id"]) + "_" + str(drow.at["client_id"]) + "_" + str(
                drow.at["client_id"])
        if ((isinstance(drow.at["contracts"], str) and "/" not in drow.at["contracts"] and "\\" not in drow.at[
            "contracts"])
                or (isinstance(drow.at["contracts"], int))):
            if drow.at["startdate"]:
                drow.at["contracts"] = str(drow.at["contracts"]) + "/" + str(drow.at["startdate"].year)
            else:
                drow.at["contracts"] = str(drow.at["contracts"]) + "/" + str(drow.at["year"])
        #############################
        # detect ripso_id
        # ---------------------------
        try:
            rec = SD.session.query(Ripso).filter_by(ripso_short=drow.at["ripso_id"], year=drow.at["year"]).one()
            drow.at["ripso_id"] = rec.id
            # return "updated", rec
        except MultipleResultsFound:
            critical("ripso_id MultipleResultsFound")
        except NoResultFound:
            raise Exception(f"Can't detect ripso {drow.at['ripso_id']}")
        return drow

    @staticmethod
    def status_print(status, record):
        try:
            id = record.id
        except AttributeError:
            id = -1
        debug("status - %s, for - %s", status, id)
        print("status - %s, for - %s at %s" % (status, record.contracts, record.startdate))

    @staticmethod
    def new_with_dup_check(drow):
        """
        check if drow exist in DB
        :param drow: row of DataFrame for insert
        :return:
        """
        #############################
        # check exist in DB by ippsuNum
        # ---------------------------
        try:
            rec = SD.session.query(Contracts).filter_by(ippsuNum=drow.at["ippsuNum"]).one()
            #############################
            # additional checks if exist
            # ---------------------------
            if drow.at["client_id"] != rec.client_id:
                return "failed - different client_id", rec
            elif drow.at["startdate"] != rec.startdate:
                error("startdate is different for - %s / %s != %s", rec.contracts, rec.startdate, drow.at["startdate"])
            drow.at["id"] = rec.id
            return "updated", rec
        except MultipleResultsFound:
            critical("ippsuNum MultipleResultsFound")
        except NoResultFound:
            pass
        #############################
        # check by startdate and client_id - try twice
        # ---------------------------
        try:
            try:
                rec = SD.session.query(Contracts).filter_by(startdate=drow.at["startdate"],
                                                            client_id=int(drow.at["client_id"])).one()
            except (OperationalError, ProgrammingError):
                debug("rollback query %s ", drow.at["client"])
                SD.session.rollback()
                # SD.session.execute("CALL GET_PRIVILEGES")
                # SD.session.execute("SET ROLE ALL")
                rec = SD.session.query(Contracts).filter_by(startdate=drow.at["startdate"],
                                                            client_id=int(drow.at["client_id"])).one()
            #############################
            # additional checks if exist
            # ---------------------------
            return ContractCheck.same_additional_checks(drow, rec)
        except MultipleResultsFound:
            critical("Contracts startdate MultipleResultsFound")
        except NoResultFound:
            #############################
            # create new record
            # ---------------------------
            rec = Contracts()
            rec.contracts = drow.at["contracts"]
            rec.startdate = drow.at["startdate"]
            rec.enddate = drow.at["enddate"]
            rec.ripso_id = int(drow.at["ripso_id"])
            rec.client_id = int(drow.at["client_id"])
            rec.dep_id = int(drow.at["dep_id"])
            rec.ippsuNum = int(drow.at["ippsuNum"])
            return "new", rec

    @staticmethod
    def same_additional_checks(drow, rec):
        #############################
        # check same record
        # ---------------------------
        if rec.contracts == drow.at["contracts"]:
            pass
        elif rec.contracts in drow.at["contracts"]:
            pass
        elif drow.at["contracts"] in rec.contracts:
            pass
        else:
            #############################
            # not same
            # ---------------------------
            contract_cut = drow.at["contracts"].split("/")[0].split("\\")[0]
            if contract_cut not in rec.contracts:
                return ContractCheck.new_with_dup_check(drow)
        #############################
        # the same
        # ---------------------------
        drow.at["id"] = rec.id
        return "updated", rec

    @staticmethod
    def update_rec(rec, drow, only_this_fields: Union[bool, list] = False):
        if only_this_fields:
            for field in only_this_fields:
                setattr(rec, field, drow.at[field])
        else:
            rec.ippsuNum = drow.at["ippsuNum"]
            rec.phone = drow.at["enddate"]


class MainCheck(Check):
    """
    TODO: maybe add second contract for first half of year?

    """

    @staticmethod
    def status_print(status, record):
        try:
            debug("status - %s, for - %s %s", status, record.id, record.client_id)
            print("status - %s, for - %s %s" % (status, record.id, record.client_id))
        except AttributeError:
            debug("record error")

    @staticmethod
    def new_with_dup_check(drow):
        """

        :param drow: row of DataFrame for insert
        :return:
        """
        #############################
        # check exist in DB
        # ---------------------------
        dat = drow.at["vdate"]
        fday, endday = calendar.monthrange(dat.year, dat.month)
        start = date(dat.year, dat.month, 1)
        end = date(dat.year, dat.month, endday)
        s = select([main]).where(and_(main.c.client_id == drow.at["client_id"],
                                      main.c.contracts_id == drow.at["contracts_id"],
                                      main.c.serv_id == drow.at["serv_id"],
                                      main.c.worker_id == drow.at["worker_id"],
                                      main.c.quantity == drow.at["quantity"],
                                      main.c.dep_id == drow.at["dep_id"],
                                      between(main.c.vdate, start, end)

                                      ))
        rec = Rec()
        for row in SD.connection.execute(s):
            print(row)
            rec.id = row.id
            rec.client_id = drow.at["client_id"]
            return "exist", rec
        else:
            return "new", rec

    @classmethod
    def save(cls, status, record, drow):
        if status != "exist":
            dat = drow.at["vdate"]
            pydat = date(dat.year, dat.month, dat.day)
            ins = updatable_main.insert().values(client_id=drow.at["client_id"],
                                                 contracts_id=drow.at["contracts_id"],
                                                 serv_id=drow.at["serv_id"],
                                                 worker_id=drow.at["worker_id"],
                                                 quantity=drow.at["quantity"],
                                                 dep_id=drow.at["dep_id"],
                                                 vdate=pydat)
            result = SD.connection.execute(ins)  # .returning(updatable_main.c.id)
            if result:
                # if "COMMIT" in result:
                # rec = Rec()
                record.id = result.inserted_primary_key
                record.client_id = drow.at["client_id"]
                return True, record
            return False, record
        else:
            return True, record

    # try:
    #     rec = SD.session.query(Add_info).filter_by(pddate=drow.at["pddate"],
    #                                                contracts_id=int(drow.at["contracts_id"])).one()
    #     return "exist", rec
    #     # return UhcCheck.same_additional_checks(drow, rec)
    # except MultipleResultsFound:
    #     critical("Add_info MultipleResultsFound")
    # except NoResultFound:
    #     # SD.session.rollback()
    #     #############################
    #     # create new record
    #     # ---------------------------
    #     rec = Add_info()
    #     for attr in drow.keys():
    #         setattr(rec, attr, drow.at[attr])
    # return "new", rec

    @staticmethod
    def drow_precheck(drow: pd.Series):
        """
        Fix row imported from xls file
        :param drow: pd.Series
        :return: drow: pd.Series

        >>> SD.engine.echo = False
        >>> ContractCheck.drow_precheck( pd.Series({"client_id": 1, "dep_id" : 1 , "year": 2020, "contracts": 1232132, \
             "ripso_id": "1|Старое рипсо 2019 года|", "startdate":pd.Timestamp('2020-01-01') , "enddate": ""}))
        client_id                 1
        dep_id                  1
        year                 2020
        contracts    1232132/2020
        ripso_id               13
        startdate      2020-01-01
        enddate        1900-01-01
        dtype: object

        """
        #############################
        # precheck - data fix
        # ---------------------------
        if isinstance(drow.at["vdate"], str):
            drow.at["vdate"] = pd.Timestamp("-".join(reversed(drow.at["vdate"].split("."))))
        else:
            drow.at["vdate"] = drow.at["vdate"].to_pydatetime().date()
        #############################
        # detect serv_id
        # ---------------------------
        # try:
        #     rec = SD.session.query(Serv).filter_by(ripso_short=drow.at["ripso_id"], year=drow.at["year"]).one()
        #     drow.at["ripso_id"] = rec.id
        #     return "updated", rec
        # except MultipleResultsFound:
        #     critical("ripso_id MultipleResultsFound")
        # except NoResultFound:
        #     raise Exception(f"Can't detect ripso {drow.at['ripso_id']}")
        return drow


class ClientCheck(Check):

    @staticmethod
    def data_frame_precheck(data_frame: pd.DataFrame):
        if "id" not in data_frame.keys():
            data_frame.insert(len(data_frame.keys()), "id", 0)
            # data_frame.insert(len(data_frame.keys()), "client_orig", 0)
            data_frame["client_orig"] = data_frame["client_full"]
        return data_frame

    @staticmethod
    def drow_precheck(drow: pd.Series):
        """
        Fix row imported from xls file
        :param drow: pd.Series
        :return: drow: pd.Series

        >>> ClientCheck.drow_precheck( pd.Series({"client": "Тестовы тест твич", "snils" : "112-123-123-22", \
             "ESRN": 1121321311, "clientbirth":pd.Timestamp('1953-01-01') , "clientDeath": ""}))
        client         Тестовы тест твич
        snils           112-123-123-22
        ESRN                1121321311
        clientbirth           1953-01-01
        clientDeath           1900-01-01
        dtype: object
        """
        #############################
        # precheck
        # ---------------------------
        try:
            drow.at["clientbirth"] = drow.at["clientbirth"].to_pydatetime().date()
        except AttributeError:
            drow.at["clientbirth"] = date(1900, 1, 1)
        try:
            drow.at["clientDeath"] = drow.at["clientDeath"].to_pydatetime().date()
        except AttributeError:
            drow.at["clientDeath"] = date(1900, 1, 1)
        if not drow.at["client"]:
            drow.at["client"] = drow.at["client_full"]
        return drow

    @staticmethod
    def status_print(status, record):
        debug("status - %s, for - %s", status, record.id)
        print("status - %s, for - %s" % (status, record.client))

    @staticmethod
    def new_with_dup_check(drow):
        """

        :param drow: row of DataFrame for insert
        :return:
        """
        #############################
        # check exist in DB by ippsuNum
        # ---------------------------
        try:
            rec = SD.session.query(Contracts).filter_by(ippsuNum=drow.at["ippsuNum"]).one()
            client = SD.session.query(Client).filter_by(client=rec.client_id).one()
            if levenshtein(client.client, drow.at["client"]) < 4 or levenshtein(client.client, drow.at["client_full"]) < 4:
                return ClientCheck.same_additional_checks(drow, client)
            else:
                return "failed - different fio", rec
        except MultipleResultsFound:
            critical("ippsuNum MultipleResultsFound")
        except NoResultFound:
            pass
        #############################
        # check exist in DB by client
        # ---------------------------
        try:
            rec = SD.session.query(Client).filter_by(client=drow.at["client"]).one()
            return ClientCheck.same_additional_checks(drow, rec)
        except MultipleResultsFound:
            critical("client MultipleResultsFound")
        except NoResultFound:
            # SD.session.rollback()
            #############################
            # create new record
            # ---------------------------
            rec = Client()
            rec.client = drow.at["client"]
            rec.clientbirth = drow.at["clientbirth"]
            rec.clientDeath = drow.at["clientDeath"]
            rec.ESRN = drow.at["ESRN"]
            rec.prim = drow.at["prim"]
            rec.phone = drow.at["phone"]
            rec.snils = drow.at["snils"]
            return "new", rec

    @staticmethod
    def same_additional_checks(drow, rec):
        #############################
        # check same record
        # ---------------------------
        if rec.clientbirth == drow.at["clientbirth"]:
            rec.ESRN = drow.at["ESRN"]
        elif rec.ESRN == drow.at["ESRN"]:
            rec.clientbirth = drow.at["clientbirth"]
        else:
            #############################
            # not same
            # ---------------------------
            if drow.at["clientbirth"] and drow.at["clientbirth"].strftime("dd.MM.yyy") not in drow.at["client"]:
                drow.at["client"] += "(" + drow.at["clientbirth"].strftime("dd.MM.yyy") + ")"
            else:
                return "false - can't add client", drow
            return ClientCheck.new_with_dup_check(drow)
        #############################
        # the same
        # ---------------------------
        drow.at["id"] = rec.id
        return "updated", rec

    @staticmethod
    def update_rec(rec, drow, only_this_fields: Union[bool, list] = False):
        if only_this_fields:
            for field in only_this_fields:
                setattr(rec, field, drow.at[field])
        else:
            rec.clientDeath = drow.at["clientDeath"]
            rec.phone = drow.at["phone"]
            rec.snils = drow.at["snils"]
            new_note = rec.prim + drow.at["prim"]
            if len(new_note) < 255:
                rec.prim = new_note
                # rec.prim = ""


class UhcCheck(Check):
    """
    TODO: maybe add second contract for first half of year?

    """

    @staticmethod
    def data_frame_precheck(df: pd.DataFrame):
        data = []
        for i, drow in df.iterrows():
            data = data + UhcCheck.transpose(drow)
        if data:
            df = pd.DataFrame(data, columns=("client_id", "category_id"), dtype=int)
        return df

    @staticmethod
    def transpose(drow: pd.Series):
        """
        Fix row imported from xls file
        :param drow: pd.Series
        :return: drow: pd.Series

        >>> SD.engine.echo = False
        >>> UhcCheck.transpose( pd.Series({"client_id": 1, "category_id" : 1 , "1": 0, "2": 1, \
             "3": 0, "4":1 , "5":1} ,dtype=int) )
        [[1, 2], [1, 4], [1, 5]]
        """
        #############################
        # precheck - transpose table
        # ---------------------------
        uid = 0
        i = 0
        data = []
        for col, val in drow.to_dict().items():
            if col == "client_id":
                uid = val
            elif col == "category_id":
                pass
            elif isinstance(col, int) and val > 0:
                data.append([uid, col])
                # drow.loc[i, "client_id"] = uid
                # drow.loc[i, "category_id"] = col
                i += 1
            elif isinstance(col, str) and val > 0:
                col = int(col.replace("_1", ""))
                data.append([uid, col])
                # drow.loc[i, "client_id"] = uid
                # drow.loc[i, "category_id"] = col
                i += 1
        return data
        # ret = pd.DataFrame(data, columns=("client_id", "category_id"))
        # return ret

    @staticmethod
    def status_print(status, record):
        try:
            debug("status - %s, for - %s %s", status, record.client_id, record.category_id)
            print("status - %s, for - %s %s" % (status, record.client_id, record.category_id))
        except AttributeError:
            debug("record error")

    @staticmethod
    def new_with_dup_check(drow):
        """

        :param drow: row of DataFrame for insert
        :return:
        """
        #############################
        # check exist in DB
        # ---------------------------
        # recs = []
        try:
            rec = SD.session.query(Client_has_category).filter_by(client_id=int(drow.at["client_id"]),
                                                                category_id=int(drow.at["category_id"])).one()
            return "exist", rec
            # return UhcCheck.same_additional_checks(drow, rec)
        except MultipleResultsFound:
            critical("Uhc MultipleResultsFound")
        except NoResultFound:
            # SD.session.rollback()
            #############################
            # create new record
            # ---------------------------
            rec = Client_has_category()
            rec.client_id = int(drow.at["client_id"])
            rec.category_id = int(drow.at["category_id"])
            # recs.append(rec)
            return "new", rec


class AddInfoCheck(Check):
    """
    TODO: maybe add second contract for first half of year?

    """

    @staticmethod
    def data_frame_precheck(df: pd.DataFrame):
        data = []
        for i, drow in df.iterrows():
            data = data + AddInfoCheck.transpose(drow)
        if data:
            df = pd.DataFrame(data, columns=("pddate", "contracts_id", "psp", "address", \
                                             "work_livemin", "curfio", "sdd", "perc"))
        return df

    @staticmethod
    def transpose(drow: pd.Series):
        """
        Fix row imported from xls file
        :param drow: pd.Series
        :return: drow: pd.Series

        >>> SD.engine.echo = False
        >>> AddInfoCheck.transpose( pd.Series({"pddate": "", "contracts_id" : 1444 , "psp": 0, \
        "year": 2020, "address": 1, "work_livemin": "нет", "curfio":"" ,\
        "sdd1":11000, "perc1":0.1, "sdd2":11000, "perc2":0.1, "sdd3":11000, "perc3":0.1} ) )
        [[datetime.date(2020, 1, 1), 1444, 0, 1, 0, '', 11000, 0.1]]
        """
        #############################
        # precheck - transpose table
        # ---------------------------
        contracts_id = 0
        psp = ""
        address = ""
        work_livemin = 0
        curfio = ""
        year = 0
        i = 0
        data = []
        #  pddate	contracts_id	psp	address	work_livemin	curfio	sdd1
        for col, val in drow.to_dict().items():
            if col == "contracts_id":
                contracts_id = val
            if col == "psp":
                psp = val
            if col == "address":
                address = val
            if col == "work_livemin":
                work_livemin = 1 if val.lower() == "да" else 0
            if col == "curfio":
                curfio = val
            elif col == "year":
                year = val
            elif col == "pddate":
                pass
            elif "sdd" in col:
                month = col.replace("sdd", "")
                pddate = date(year, int(month), 1)
                if isinstance(val, str):
                    val = val.replace("$", "")
                    val = val.replace(" ", "")
                    if len(val) > 3 and val[-3] == ".":
                        val = val.replace(",", "")
                sdd = val
                if sdd == "":
                    sdd = 0
                perc = drow.loc["perc" + month]
                data.append([
                    pddate,
                    contracts_id,
                    psp,
                    address,
                    work_livemin,
                    curfio,
                    sdd,
                    perc
                ])
            elif "perc" in col:
                pass
        for i in reversed(range(len(data) - 1)):
            if data[i][1:] == data[i + 1][1:]:
                del data[i + 1]
        return data
        # ret = pd.DataFrame(data, columns=("client_id", "category_id"))
        # return ret

    @staticmethod
    def status_print(status, record):
        try:
            debug("status - %s, for - %s %s", status, record.pddate, record.contracts_id)
            print("status - %s, for - %s %s" % (status, record.pddate, record.contracts_id))
        except AttributeError:
            debug("record error")

    @staticmethod
    def new_with_dup_check(drow):
        """

        :param drow: row of DataFrame for insert
        :return:
        >>> df = pd.DataFrame([[date(2020, 1, 1), 1444, 0, 1, 0, '', 11000, 0.1]], \
                                columns=("pddate", "contracts_id", "psp", "address", \
                                         "work_livemin", "curfio", "sdd", "perc"))
        >>> SD.engine.echo = False
        >>> state, orm = AddInfoCheck.new_with_dup_check(df.loc[0])
        >>> state, repr(orm)[:37]
        ('new', '<models.orm.Updatable_add_info object')
        """
        #############################
        # check exist in DB
        # ---------------------------
        # recs = []
        try:
            rec = SD.session.query(Add_info).filter_by(pddate=drow.at["pddate"],
                                                       contracts_id=int(drow.at["contracts_id"])).one()
            return "exist", rec
            # return UhcCheck.same_additional_checks(drow, rec)
        except MultipleResultsFound:
            critical("Add_info MultipleResultsFound")
        except NoResultFound:
            # SD.session.rollback()
            #############################
            # create new record
            # ---------------------------
            rec = Add_info()
            for attr in drow.keys():
                setattr(rec, attr, drow.at[attr])
            return "new", rec


def import_dep_from_xls(file, dep, year):
    """


    >>> SD.engine.echo = False
    >>> _ = import_dep_from_xls(os.path.join(os.getcwd(), "tests", "export_for_3uson.xlsx"), SD.last_dep, 2020)
    SD.last_year != 2020
    status - updated, for - Батестова бария Бавтестовна
    status - updated, for - Атестова ария Автестовна
    status - updated, for - Тестов тевт Тертович
    status - updated, for - 123456783/2020 at 2020-01-09
    status - updated, for - 123456782/2020 at 2020-01-09
    status - updated, for - 123456781/2020 at 2020-01-09
    status - exist, for - 1444 3
    status - exist, for - 1444 6
    status - exist, for - 1444 7
    status - exist, for - 1446 4
    status - exist, for - 1446 9
    status - exist, for - 1446 14
    status - exist, for - 1446 14
    status - exist, for - 2020-01-01 1507
    status - exist, for - 2020-02-01 1507
    status - exist, for - 2020-03-01 1507
    status - exist, for - 2020-04-01 1507
    status - exist, for - 2020-01-01 1508
    status - exist, for - 2020-01-01 1509
       worker_id  serv_id  dep_id  contracts_id  client_id      vdate
    0          1      406       1        1507.0     1444  21.1.2020
    1          1      391       1        1507.0     1444  14.2.2020
    2          1      387       1        1507.0     1444  17.3.2020
    3        156      386       1        1507.0     1444   8.4.2020
    4        156      293       1        1508.0     1445   9.6.2020
    5        156      295       1        1509.0     1446  20.2.2020
    6        156      310       1        1509.0     1446   3.3.2020
    7        156      309       1        1509.0     1446  20.4.2020
    8        156      293       1        1509.0     1446  23.6.2020
    (175257, 1444, 1507, 1, 1, 406, 11, datetime.date(2020, 1, 21), None)
    status - exist, for - 175257 1444
    (175258, 1444, 1507, 1, 1, 391, 12, datetime.date(2020, 2, 14), None)
    status - exist, for - 175258 1444
    (175259, 1444, 1507, 1, 1, 387, 13, datetime.date(2020, 3, 17), None)
    status - exist, for - 175259 1444
    (175260, 1444, 1507, 1, 156, 386, 14, datetime.date(2020, 4, 8), None)
    status - exist, for - 175260 1444
    (175261, 1445, 1508, 1, 156, 293, 10, datetime.date(2020, 6, 9), None)
    status - exist, for - 175261 1445
    (175262, 1446, 1509, 1, 156, 295, 10, datetime.date(2020, 2, 20), None)
    status - exist, for - 175262 1446
    (175263, 1446, 1509, 1, 156, 310, 12, datetime.date(2020, 3, 3), None)
    status - exist, for - 175263 1446
    (175264, 1446, 1509, 1, 156, 309, 14, datetime.date(2020, 4, 20), None)
    status - exist, for - 175264 1446
    (175265, 1446, 1509, 1, 156, 293, 10, datetime.date(2020, 6, 23), None)
    status - exist, for - 175265 1446
    done
    """
    if dep != SD.last_dep:
        print(f"SD.last_dep != {dep}")
    if year != SD.last_year:
        print(f"SD.last_year != {year}")
    #############################
    # read xls file
    # ---------------------------
    # file = select_xls_file()
    dfio, dcontracts, duhc, dainfo, dmain, dmeta = read_xls(file)
    #############################
    # import dfio
    # ---------------------------
    dfio = parse_data_frame(dfio, ClientCheck)
    #############################
    # import dcontracts
    # ---------------------------
    for i in range(len(dfio)):
        dcontracts.loc[i, "client_id"] = dfio.loc[i, "id"]
        duhc.loc[i, "client_id"] = dfio.loc[i, "id"]
        dainfo.loc[i, "curfio"] = dfio.loc[i, "client"]
    dcontracts["dep_id"] = dep
    dcontracts.insert(8, "year", year)
    dcontracts = parse_data_frame(dcontracts, ContractCheck)
    #############################
    # import client_has_category
    # ---------------------------
    duhc = parse_data_frame(duhc, UhcCheck)
    #############################
    # import add_info
    # ---------------------------
    dainfo.insert(2, "year", year)
    for i in range(len(dcontracts)):
        dainfo.loc[i, "contracts_id"] = int(dcontracts.loc[i, "id"])
    dainfo = parse_data_frame(dainfo, AddInfoCheck)
    #############################
    # import main
    # ---------------------------

    # dmain.insert(0, "year", year)
    dmain.insert(0, "client_id", 0)
    dmain.insert(0, "contracts_id", 0)
    dmain.insert(0, "dep_id", dep)
    dmain.insert(0, "serv_id", 0)
    dmain.insert(0, "worker_id", 0)
    # fio_contr = pd.DataFrame()
    # fio_contr["client"] = dfio["client"]
    # fio_contr["client_id"] = dfio["client_id"]
    # fio_contr["contracts_id"] = dcontracts["contracts_id"]
    # fio_contr["ESRN"] = dfio["ESRN"]
    # fio_contr["client_orig"] = dfio["client_orig"]
    for i in range(len(dmain)):
        uid = dcontracts.loc[dcontracts["contracts_id"] == dmain.loc[i, "client"], "client_id"].values[0]
        cid = dcontracts.loc[dcontracts["contracts_id"] == dmain.loc[i, "client"], "id"].values[0]
        dmain.loc[i, "client_id"] = uid
        dmain.loc[i, "contracts_id"] = cid
        # serv_text=dmain.loc[i, "serv_text"])
        sid = SD.session.query(Serv).filter(and_(
            Serv.serv_text.ilike("%" + dmain.at[i, "serv_text"] + "%"),
            Serv.tnum.ilike("%" + dmain.at[i, "tnum"] + "%"),
            Serv.year == year)).one()
        dmain.loc[i, "serv_id"] = sid.id
        worker = dmain.at[i, "worker"].split(" ")[:3]  # TODO: check before cutting
        worker = " ".join(worker)
        try:
            wid = SD.session.query(Worker).filter(Worker.worker.ilike("%" + worker + "%")).one()
            dmain.loc[i, "worker_id"] = wid.id
        except (NoResultFound, MultipleResultsFound):
            dmain.loc[i, "worker_id"] = 1
        # index = fio_contr.loc[fio_contr["client"] == dmain.loc[i, "client"]].index
        # if index.empty or index < 0:
        #     index = fio_contr.loc[fio_contr["client"] == dmain.loc[i, "client_orig"]].index
        # dmain.loc[i, "client_id"] = fio_contr.loc[index, "client_id"]
        # dmain.loc[i, "contracts_id"] = fio_contr.loc[index, "contracts_id"]
    print(dmain[["worker_id", "serv_id", "dep_id", "contracts_id", "client_id", "vdate"]])
    dmain = parse_data_frame(dmain, MainCheck)
    print("done")
    # if not contract_ids:
    #     return False


if __name__ == '__main__':
    import doctest

    doctest.testmod(optionflags=doctest.NORMALIZE_WHITESPACE)
