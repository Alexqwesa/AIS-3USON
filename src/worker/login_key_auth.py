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
import string
import random

import qrcode
from PIL.ImageQt import ImageQt


def pw_gen(size=6, chars=string.ascii_letters + string.digits + "+*!@%=?") -> str:
    # + string.punctuation
    chars = [c for c in chars]
    return ''.join(random.choice(chars) for _ in range(size))


def api_key(otd_id: int, otd: str, name: str = "test", password=None, db="kcson", host="192.168.0.102", port="48080"):
    """ Create api key for login via qr-code

    Args:

    Return:
           (password, qr_code)
    Tests:
        >>> password, key, qim = api_key(1, "otd test", password="123" )
        >>> print(key)  # doctest:+ELLIPSIS
        {'app': 'AIS3USON web', 'name': 'test', 'api_key': '123', 'otd_id': 1, 'otd': 'otd test', 'db': 'kcson', 'host': '192.168.0.102', 'port': '48080'}
        >>> print(qim)  # doctest:+ELLIPSIS
        <PIL.ImageQt.ImageQt(QSize(570, 570),format=QImage::Format_Mono,depth=1,devicePixelRatio=1,bytesPerLine=72,sizeInBytes=41040)...
    """
    if not password:
        password = pw_gen(32)  # TODO: use other generator
    # TODO: use real key or encrypted string,
    #############################
    # create api key
    # ---------------------------
    key = {
        "app": "AIS3USON web",
        "name": name,
        "api_key": password,
        "otd_id": otd_id, "otd": otd, "db": db,
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
