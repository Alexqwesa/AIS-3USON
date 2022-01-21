#!/usr/bin/python3
# -------------------------------------------------------------------------------
# -*- coding: utf-8 -*-
# Name:        AIS 3USON helpers to get contract data
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
from functools import lru_cache
import logging
from qtpy.QtCore import Qt, QDate, QObject, Slot, QModelIndex


# @lru_cache(None)
def calc_perc_for_contract(contract_id, pddate):
    """

    :param contract_id:
    :return:

    >>> calc_perc_for_contract(1, QDate(2019,1,1))
    -1
    >>> calc_perc_for_contract(1, QDate(2020,1,1))
    0.15
    >>> calc_perc_for_contract(1, QDate(2020,7,1))
    0.1
    >>> calc_perc_for_contract(1, QDate(2020,8,1))
    0.1
    >>> calc_perc_for_contract(1, QDate(2020,3,1))
    0.2
    >>> calc_perc_for_contract(1, QDate(2020,4,1))
    0.2
    """
    #############################
    # check init
    # ---------------------------
    try:
        WD = calc_perc_for_contract.WD
    except AttributeError:
        from logic.data_worker import WD
        calc_perc_for_contract.WD = WD
        WD = calc_perc_for_contract.WD
    #############################
    # get data
    # ---------------------------
    # from models.ts_models import tsSqlTableModel
    contracts_model = WD.models("contracts")
    client_id = contracts_model.data_by_id(
        contract_id,
        contracts_model.tsFieldNames.index("client_id")
    )
    ripso_id = contracts_model.data_by_id(
        contract_id,
        contracts_model.tsFieldNames.index("ripso_id")
    )
    # ivov = WD.get_rows_from_model_name("client_has_category", client_id, id_field="client_id")
    uhc = WD.models("client_has_category")
    ivov = uhc.data_by_id(
        client_id,
        contracts_model.tsFieldNames.index("ripso_id"),
        id_field="client_id",
        id1=5,
        id_field1="category_id"
    )
    # cat_col = uhc.tsFieldNames.index("category_id")
    # ivov = [x for x in ivov if x.siblingAtColumn(cat_col).data(
    #     Qt.EditRole) == 5]  # TODO: check date and archive
    servform_id = WD.get_data_from_model_name("ripso", "servform_id", ripso_id)
    #############################
    # do calc
    # ---------------------------
    if ivov:
        return calc_proc(ivov, servform_id)
    else:
        self, row = add_info_before(pddate, contract_id)
        index = self.index(row, 0)
        sdd = index.siblingAtColumn(self.tsFieldNames.index("sdd")).data(Qt.EditRole)
        if not sdd:
            return -1
        pddate = index.siblingAtColumn(self.tsFieldNames.index("pddate")).data(Qt.EditRole)
        work_livemin = index.siblingAtColumn(self.tsFieldNames.index("work_livemin")).data(Qt.EditRole)
        return calc_proc(ivov, servform_id, pddate, sdd, work_livemin)


# @lru_cache(None)
def perc_for(index: QModelIndex):
    """
    return percents for SDD in rows (or -1 if fail)
    :param index:
    :return:
    """
    #############################
    # check init
    # ---------------------------
    try:
        WD = perc_for.WD
    except AttributeError:
        from logic.data_worker import WD
        perc_for.WD = WD
        WD = perc_for.WD
    #############################
    # get contract_id
    # ---------------------------
    self = index.model()
    contract_id = index.siblingAtColumn(self.tsFieldNames.index("contracts_id")).data(Qt.EditRole)
    #############################
    # get data
    # ---------------------------
    # from models.ts_models import tsSqlTableModel
    contracts_model = WD.models("contracts")
    client_id = contracts_model.data_by_id(
        contract_id,
        contracts_model.tsFieldNames.index("client_id")
    )
    ripso_id = contracts_model.data_by_id(
        contract_id,
        contracts_model.tsFieldNames.index("ripso_id")
    )
    # ivov = WD.get_rows_from_model_name("client_has_category", client_id, id_field0="client_id")
    uhc = WD.models("client_has_category")
    ivov = uhc.data_by_id(
        client_id,
        contracts_model.tsFieldNames.index("ripso_id"),
        id_field="client_id",
        id1=5,
        id_field1="category_id"
    )
    # cat_col = uhc.tsFieldNames.index("category_id")
    # ivov = [x for x in ivov if x.siblingAtColumn(cat_col).data(
    #     Qt.EditRole) == 5]  # TODO: check date and archive
    servform_id = WD.get_data_from_model_name("ripso", "servform_id", ripso_id)
    #############################
    # do calc
    # ---------------------------
    if ivov:
        return calc_proc(ivov, servform_id)
    else:
        sdd = index.siblingAtColumn(self.tsFieldNames.index("sdd")).data(Qt.EditRole)
        if not sdd:
            return -1
        pddate = index.siblingAtColumn(self.tsFieldNames.index("pddate")).data(Qt.EditRole)
        work_livemin = index.siblingAtColumn(self.tsFieldNames.index("work_livemin")).data(Qt.EditRole)
        return calc_proc(ivov, servform_id, pddate, sdd, work_livemin)


@lru_cache(None)
def calc_proc(ivov, servform_id, pddate=None, sdd=0, work_livemin=False):
    """

    :param ivov:
    :param servform_id:
    :param pddate:
    :param sdd:
    :param work_livemin:
    :return:

    >>> calc_proc(1, 1)
    0.05
    >>> calc_proc(None, 1, QDate(2018,1,1),13000)
    0.1
    """
    if ivov:
        if servform_id == 4:
            return 0.1
        else:
            return 0.05
    try:
        if work_livemin:
            prmin = lm_before(pddate, "live_min_w")
        else:
            prmin = lm_before(pddate, "live_min_p")
    except TypeError:
        return -1
    if servform_id == 4:
        return 0.35
    elif servform_id in [1, 2, 3]:
        if sdd - prmin * 4 > 0:
            return 0.4
        elif sdd - prmin * 3 > 0:
            return 0.3
        elif sdd - prmin * 2.5 > 0:
            return 0.2
        elif sdd - prmin * 2 > 0:
            return 0.15
        elif sdd - prmin * 1.5 > 0:
            return 0.1
        else:
            return 0
    # error("Unknown servform_id")
    return -1


# @lru_cache(None)
def add_info_before(pddate: QDate, contract_id):
    """
    Return live minimum before date for category of people ptype

    :param pddate: one of live_min_p|live_min_w|live_min_c
    :param contract_id:
    :return:

    >>> logging.getLogger().setLevel(logging.INFO)

    """
    #############################
    # check inited
    # ---------------------------
    ai_filter = f"contracts_id = {contract_id}"  # and pddate < {pddate}
    model_found = False
    try:
        WD = add_info_before.WD
        model = add_info_before.add_info
        #############################
        # check ai model right
        # ---------------------------
        if ai_filter in model.filter() and " and " not in model.filter() and "or" not in model.filter():
            if model.rowCount0() > 0:
                model_found = True
                add_info_before.add_info = model
    except AttributeError:
        from logic.data_worker import WD
        add_info_before.WD = WD
        WD = add_info_before.WD
    #############################
    # find inited model
    # ---------------------------
    if not model_found:
        for name, model in WD.inited_models.items():
            if "add_info" in name:
                if ai_filter in model.filter() and " and " not in model.filter() and "or" not in model.filter():
                    if model.rowCount0() > 0:
                        model_found = True
                        add_info_before.add_info = model
                        break
    try:
        #############################
        # get prev ai
        # ---------------------------
        add_info = add_info_before.add_info
        if not model_found:
            add_info.setFilter(ai_filter)
    except AttributeError:
        from logic.data_worker import WD
        add_info = WD.models("add_info_raw__where_contracts_id_for_before",
                             "add_info",
                             ai_filter, False)
        if add_info.rowCount0() == 0:
            return False, -1
        add_info_before.add_info = add_info
    #############################
    # init cols
    # ---------------------------
    coldat = add_info.tsFieldNames.index("pddate")
    # col = add_info.tsFieldNames.index(contract_id)
    ai = add_info
    #############################
    # find and return last row before pddate
    # ---------------------------
    row = -1
    first_date = QDate(1900, 1, 1)
    for r in reversed(range(ai.rowCount())):
        if r != ai.special_row:
            date = ai.index(r, coldat).data(Qt.EditRole)
            if first_date < date <= pddate:
                first_date = date
                row = r
                # pddate = date
                # result = ai.index(r, col).data(Qt.EditRole)
    return ai, row


@lru_cache(None)
def lm_before(pddate: QDate, ptype="live_min_p"):
    """
    Return live minimum before date for category of people ptype

    :param ptype: one of live_min_p|live_min_w|live_min_c
    :param pddate:
    :return:

    >>> logging.getLogger().setLevel(logging.INFO)
    >>> lm_before(QDate(2020,1,1))
    9303.8
    >>> lm_before(QDate(2019,2,1))
    8954.1
    >>> lm_before(QDate(2019,7,1), "live_min_w")
    12472.1
    >>> lm_before(QDate(2017,7,1), "live_min_w")
    11658.9
    """
    #############################
    # init model
    # ---------------------------
    try:
        lm = lm_before.live_min_model
    except AttributeError:
        from logic.data_worker import WD
        live_min_model = WD.models("live_min")
        lm_before.live_min_model = live_min_model
        live_min_model.saved.connect(lm_before_cache_clear)
        live_min_model.selected.connect(lm_before_cache_clear)
        lm = lm_before.live_min_model
    #############################
    # init cols
    # ---------------------------
    coldat = lm.tsFieldNames.index("lmdate")
    col = lm.tsFieldNames.index(ptype)
    #############################
    # find and return last live_min before pddate
    # ---------------------------
    result = 0
    first_date = QDate(1900, 1, 1)
    for r in reversed(range(lm.rowCount())):
        if r != lm.special_row:
            date = lm.index(r, coldat).data(Qt.EditRole)
            if first_date < date <= pddate:
                first_date = date
                # pddate = date
                result = lm.index(r, col).data(Qt.EditRole)
    return result


@Slot()  # other signals
@Slot(QObject)
def lm_before_cache_clear(obj=None):
    return lm_before.cache_clear()


if __name__ == '__main__':
    import doctest

    doctest.testmod()
