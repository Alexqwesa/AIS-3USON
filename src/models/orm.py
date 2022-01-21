#!/usr/bin/python3
# -------------------------------------------------------------------------------
# -*- coding: utf-8 -*-
# Name:        AIS 3USON ORM
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
import cProfile
import contextlib
import datetime
import io
import pstats
from decimal import Decimal
from operator import attrgetter
from datetime import datetime as dt

from safe_shared_data import *
from sqlalchemy import ForeignKey, Date, Float, BigInteger, MetaData, Table
from sqlalchemy.ext.declarative import declarative_base, declared_attr
from sqlalchemy import Column, Integer, String, DECIMAL, Boolean
from sqlalchemy.orm import sessionmaker, relationship

# import pymysql

# pymysql.install_as_MySQLdb()
Base = declarative_base()

metadata = MetaData()
session = None

#
# def init_sqlalchemy(session=None):
#     if not session:
#         Session = sessionmaker(bind=SD.engine)
#         session = Session()
#         session.execute("CALL GET_PRIVILEGES")
#         session.execute("SET ROLE ALL")
#         return session


class def_table_name:
    @declared_attr
    def __tablename__(cls):
        return cls.__name__.lower()


class basePK(def_table_name):
    id = Column(Integer, primary_key=True)


def RefernceCol(tablename, nullable=False, **kwargs):
    return Column(Integer, ForeignKey("{}.id".format(tablename).lower()), nullable=nullable, **kwargs)


class Serv(basePK, Base):
    serv = Column(String, unique=True)
    serv_text = Column(String)
    tnum = Column(String, unique=True)
    year = Column(Integer)


class Worker(basePK, Base):
    worker = Column(String, unique=True)


main = Table("main", metadata,
             Column("id", Integer, primary_key=True),
             Column("client_id", Integer),
             Column("contracts_id", Integer),
             Column("dep_id", Integer),
             Column("worker_id", Integer),
             Column("serv_id", Integer),
             Column("quantity", Integer),
             Column("vdate", Date),
             Column("note", String))

updatable_main = Table("updatable_main", metadata,
                       Column("id", Integer, primary_key=True),
                       Column("client_id", Integer),
                       Column("contracts_id", Integer),
                       Column("dep_id", Integer),
                       Column("worker_id", Integer),
                       Column("serv_id", Integer),
                       Column("quantity", Integer),
                       Column("vdate", Date),
                       Column("note", String))


#
# class NamePK(basePK):
#     id = Column(Integer, primary_key=True)


class Client(basePK, Base):
    client = Column(String, unique=True)
    contracts = relationship("Contracts", backref="client")
    uhc = relationship("Client_has_category", backref="client")  # also Client_has_category.client
    clientbirth = Column(Date)
    clientDeath = Column(Date)
    ESRN = Column(BigInteger)
    snils = Column(String)
    prim = Column(String)

    def in_month_meta_pay(self, month, year):
        pass

    def ivov_at(self, month, year=None):
        ivov = [cat for cat in self.uhc if
                "ИВОВ" in cat.cat.category and
                (
                        cat.get_date is None or
                        (cat.get_date.month >= month and cat.get_date.year >= year) or
                        cat.get_date.year > year)
                ]
        if ivov:
            return True
        else:
            return False


class Updatable_client(basePK, Base):
    client = Column(String, unique=True)
    # contracts = relationship("Contracts", backref="client")
    # uhc = relationship("Client_has_category", backref="client")  # also Client_has_category.client
    clientbirth = Column(Date)
    clientDeath = Column(Date)
    ESRN = Column(BigInteger)
    snils = Column(String)
    prim = Column(String)


class Client_has_category(def_table_name, Base):
    client_id = RefernceCol("Client", primary_key=True)
    category_id = RefernceCol("Category", primary_key=True)
    # cat= relationship("Category", back_populates="Client_has_category")
    get_date = Column(Date, default=datetime.date(dt.now().year, 1, 1))


class Category(basePK, Base):
    category = Column(String, unique=True)
    uhc = relationship("Client_has_category", backref="cat")


class Ripso(basePK, Base):
    ripso = Column(String, unique=True)
    ripso_short = Column(String)
    year = Column(Integer)


class Dep(basePK, Base):
    dep = Column(String, unique=True)


class Contracts(basePK, Base):
    contracts = Column(String, unique=True)
    client_id = RefernceCol("Client")
    dep_id = RefernceCol("Dep")
    ripso_id = RefernceCol("Ripso")
    # client = relationship("Client", back_populates="Contracts")
    add_info = relationship("Add_info", backref="contracts")
    max_last_pay = relationship("Max_pay_in_month", backref="contracts")
    ippsuNum = Column(Integer)
    startdate = Column(Date)
    enddate = Column(Date)

    def in_month_meta_pay(self, month, year):
        """ :returns sdd, perc, max_pay, is_correct, new_at"""
        mpays = [mpay for mpay in self.max_last_pay if
                 year > mpay.pddate.year or
                 year == mpay.pddate.year and month >= mpay.pddate.month]
        if not mpays:
            return None, None, None, None, None
        max_pay = max(mpays, key=attrgetter("pddate"))  # lambda e: e.pddate)
        #############################
        # check is new_at newer
        # ---------------------------
        new_at = max_pay.new_at
        if new_at:
            if new_at.year == year and new_at.month <= month:
                pass
            elif new_at.year < year:
                pass
            else:  # if not
                new_at = False
        return max_pay.sdd, max_pay.perc, max_pay.max_pay, max_pay.perc == max_pay.counted_perc(), new_at


class Updatable_contracts(basePK, Base):
    contracts = Column(String, unique=True)
    client_id = RefernceCol("Client")
    dep_id = RefernceCol("Dep")
    ripso_id = RefernceCol("Ripso")
    # client = relationship("Client", back_populates="Contracts")
    # add_info = relationship("Add_info", backref="contracts")
    # max_last_pay = relationship("Max_pay_in_month", backref="contracts")
    ippsuNum = Column(Integer)
    startdate = Column(Date)
    enddate = Column(Date)


class Max_pay_in_month(def_table_name, Base):
    contracts_id = RefernceCol("Contracts", primary_key=True)
    pddate = Column(Date, primary_key=True)
    # contracts = relationship("Contracts", back_populates="max_pay_in_month")
    servform_id = Column(DECIMAL)
    sdd = Column(DECIMAL)
    perc = Column(DECIMAL)
    max_pay = Column(DECIMAL)
    lm = Column(DECIMAL)  # prmin
    # work_livemin = Column(Boolean)
    new_at = Column(Date)

    def counted_perc(self):
        servform_id = self.servform_id
        ivov = self.contracts.client.ivov_at(self.pddate.month, self.pddate.year)
        if ivov:
            if servform_id == 4:
                return 0.1
            else:
                return 0.05
        else:
            sdd = self.sdd
            # pddate = self.pddate
            # work_livemin = self.work_livemin
            try:
                prmin = self.lm  # if work_livemin:
                #     prmin = self.lm_before(pddate)[2]
                if servform_id == 4:
                    return 0.35
                elif servform_id in [1, 2, 3]:
                    if sdd - prmin * 4 > 0:
                        return 0.4
                    elif sdd - prmin * 3 > 0:
                        return 0.3
                    elif sdd - prmin * Decimal(2.5) > 0:
                        return 0.2
                    elif sdd - prmin * 2 > 0:
                        return 0.15
                    elif sdd - prmin * Decimal(1.5) > 0:
                        return 0.1
                    else:
                        return 0
                else:
                    error("Unknown servform_id")
                    return -1
            except TypeError:
                error("error maybe unknown prmin")
                return -1


class Updatable_add_info(def_table_name, Base):
    pddate = Column(Date, primary_key=True)
    contracts_id = RefernceCol("Contracts", primary_key=True)
    # contracts = relationship("Contracts", back_populates="add_info")
    sdd = Column(DECIMAL)
    perc = Column(Float)
    curFIO = Column(String(255))
    psp = Column(String(255))
    address = Column(String(255))
    repr_FIO = Column(String(255))
    repr_psp = Column(String(255))
    repr_addr = Column(String(255))
    work_livemin = Column(Boolean, default=0)


class Add_info(def_table_name, Base):
    pddate = Column(Date, primary_key=True)
    contracts_id = RefernceCol("Contracts", primary_key=True)
    # contracts = relationship("Contracts", back_populates="add_info")
    sdd = Column(DECIMAL)
    perc = Column(Float)
    curFIO = Column(String(255))
    psp = Column(String(255))
    address = Column(String(255))
    repr_FIO = Column(String(255))
    repr_psp = Column(String(255))
    repr_addr = Column(String(255))
    work_livemin = Column(Boolean, default=0)

    def in_month(self, month, year=None):
        """ :returns sdd, perc, is_correct, is_last"""
        if not year:
            year = SD.last_year
        return


@contextlib.contextmanager
def profiled():
    pr = cProfile.Profile()
    pr.enable()
    yield
    pr.disable()
    s = io.StringIO()
    ps = pstats.Stats(pr, stream=s).sort_stats('cumulative')
    ps.print_stats()
    # uncomment this to see who's calling what
    # ps.print_callers()
    print(s.getvalue())


if __name__ == "__main__":
    # for instance in session.query(Client).order_by(Client.id):
    #     print(instance.client, instance.id)
    with profiled():
        if not session:
            session = SD.sess
        for instance in session.query(Contracts).order_by(Contracts.client_id):
            print(instance.client.client, instance.client_id, instance.id, instance.in_month_meta_pay(1, 2020))
