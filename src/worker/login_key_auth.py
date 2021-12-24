#!/usr/bin/python3
# -------------------------------------------------------------------------------
# -*- coding: utf-8 -*-
# Name:        AIS 3USON login api key creation
# Purpose:
#
# Author:      Savin Alexander Viktorovich aka alexqwesa
# Created:     2021
# Copyright:   Savin Alexander Viktorovich aka alexqwesa
# Licence:     LGPL 3
# This software is licensed under the "LGPLv3" License as described in the "LICENSE" file,
# which should be included with this package. The terms are also available at
# http://www.gnu.org/licenses/lgpl-3.0.html
# -------------------------------------------------------------------------------
import json
import qrcode
from PIL.ImageQt import ImageQt
from qtpy.QtCore import Qt

from logic.data_worker import WD
from safe_shared_data import SD


def api_key(worker_dep_id: int, dep: str, name: str = "test", password=None, db="kcson", host=None, port="48080"):
    """ Create api key for login via qr-code

    Args:

    Return:
           (password, qr_code)
    Tests:
        >>> password, key, qim = api_key(1, "otd test", password="123" )
        >>> print(key)  # doctest:+ELLIPSIS
        # {'app': 'AIS3USON web', 'name': 'test', 'api_key': '123', 'dep_id': 1, 'dep': 'otd test', 'db': 'kcson', 'host': 'None', 'port': '48080'}
        >>> print(qim)  # doctest:+ELLIPSIS
        # <PIL.ImageQt.ImageQt(QSize(570, 570),format=QImage::Format_Mono,depth=1,devicePixelRatio=1,bytesPerLine=72,sizeInBytes=41040)...
    """
    if not host:
        if "setting" in WD.inited_models:
            host = WD.get_rows_from_model_name(model_name="setting", id_field="setting",
                                               id0="mobile_server")[0].siblingAtColumn(
                WD.inited_models["setting"].index_of_col("setting")).data(Qt.EditRole)
        else:
            host = SD.line_query("select value from setting where setting='mobile_server'")

    # TODO: use real key or encrypted string,
    #############################
    # create api key
    # ---------------------------
    key = {
        "app": "AIS3USON web",
        "name": name,
        "api_key": password,
        "worker_dep_id": worker_dep_id, "dep": dep, "db": db,
        "host": host, "port": port
    }
    #############################
    # make Qr image
    # ---------------------------
    qim = ImageQt(
        qrcode.make(
            json.dumps(key)
        )
    )
    # QtGui.QPixmap.fromImage(qim)
    return password, key, qim


if __name__ == '__main__':
    import doctest

    doctest.testmod(optionflags=doctest.NORMALIZE_WHITESPACE)
