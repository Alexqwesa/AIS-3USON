#!/usr/bin/python3
# -*- coding: utf-8 -*-
""" Web worker for AIS-3USON """
# -------------------------------------------------------------------------------
# Name:        AIS 3USON web worker
# Purpose:     Middleware to connect SQL DBMS to mobile clients,
#                   this file should have minimal amount of dependency,
#                   and should be able to run on any system
#
# Author:      Savin Alexander Viktorovich aka alexqwesa
# Created:     2021-2023
# Copyright:   Savin Alexander Viktorovich aka alexqwesa
# Licence:     LGPL 3
# This software is licensed under the "LGPLv3" License as described in the "LICENSE" file,
# which should be included with this package. The terms are also available at
# http://www.gnu.org/licenses/lgpl-3.0.html
# -------------------------------------------------------------------------------
import argparse
import json
import os
import socket
import sys
from subprocess import Popen
from typing import Annotated, Tuple, Union

import mysql
import uvicorn
from fastapi import FastAPI, Header, Body
from mysql.connector import connect
from pydantic import BaseModel
from starlette.middleware.cors import CORSMiddleware
from starlette.responses import HTMLResponse
from starlette.testclient import TestClient

VERSION = 13

BIND_HOST = os.getenv("HOST_NAME", "0.0.0.0")
BIND_PORT = int(os.getenv("SERVER_PORT", 48080))
MYSQL_PORT = int(os.getenv("MYSQL_PORT", 3306))
MYSQL_HOST = os.getenv("MYSQL_HOST", "127.0.0.1")
PASSWORD = os.getenv("PASSWORD", "nopassword")
CONFDIR = os.getenv("CONFDIR", "/etc/ais3uson")
CORS_LIST = json.loads(os.getenv('CORS_LIST', """
{
    "1":"https://127.0.0.1",
    "2":"https://localhost", 
    "3":"http://127.0.0.1",
    "4":"http://localhost"
}
""".replace("\n", "")))
# "5":"https://alexqwesa.github.io", # will be put at deployment time
# "6":"*"  # useful for testing


app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=CORS_LIST.values(),
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


def ping_server(server: str = MYSQL_HOST, port: str = MYSQL_PORT, timeout=3):
    """ping server"""
    try:
        socket.setdefaulttimeout(timeout)
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect((server, port))
    except OSError as error:
        return f"error: {error}"
    finally:
        s.close()
    return "ok"


# @lru_cache(maxsize=1000)
def api_key_check(api_key: str):
    if api_key:
        head, res = get_sql_data(f"select api_key from _apikey_exist where api_key = '{api_key}';")
        if res and api_key in res[0]:
            return True
    return False


@app.get("/")
async def root():
    return {"ais_3uson": VERSION}


@app.get("/stat", response_class=HTMLResponse)
async def stat(api_key: Annotated[str, Header()] = ""):
    """Statistics of web worker"""
    print("stat requested")
    responses = await stat_json(api_key)
    return f"""
    <html><head><title>Statistic for WEB-sevrer AIS-3USON</title></head>
    <body>
    <p>Statistic for WEB-sevrer AIS-3USON</p> 
    <p>Web worker version: {VERSION}</p> 
    <p>DB version: {responses["DB version"]}</p> 
    <p>MySQL ping status: {responses["MySQL ping status"]}</p> 
    <p>MySQL api_key correct:  {responses["MySQL api_key correct"]}</p> 
    </body></html>
    """


@app.get("/stat_json")
async def stat_json(api_key: Annotated[str, Header()] = ""):
    """Statistics of web worker"""
    print("stat requested")
    return {"Web worker version": VERSION,
            "DB version": get_sql_data("select * from _version;"),
            "MySQL ping status": ping_server(),
            "MySQL api_key correct": api_key_check(api_key)
            }


@app.get("/clients")
async def read_clients(api_key: Annotated[str, Header()] = ""):
    """Get list of clients"""
    if api_key:
        header, message = get_sql_data(sql_query=f"""
            select  contract_id, dep_id, client_id, contract, client, dhw_id
            from    _apikey_has_contracts 
            where api_key = '{api_key}';
        """)  # TODO: add ,contract_duration, comment, percent, max_pay
        return to_list_of_dict(header, message, default=str)
    return {}


@app.get("/services")
async def read_services(api_key: Annotated[str, Header()] = ""):
    """Get list of clients"""
    if api_key_check(api_key):
        header, message = get_sql_data(sql_query="""
                select id, tnum, serv_text, total, image, serv_id_list, sub_serv, short_text, price 
                from _api_key_services;
        """)
        return to_list_of_dict(header, message, default=str)
    return {}


@app.get("/planned")
async def read_planned(api_key: Annotated[Union[str, None], Header()] = None):
    """Get list of clients"""
    if api_key:
        header, message = get_sql_data(sql_query="""
                    select contract_id,serv_id,planned,filled 
                    from _api_key_planned 
                    where api_key = '{api_key}';
        """)
        return to_list_of_dict(header, message, default=str)
    return {}


class ClientService(BaseModel):
    contracts_id: int
    serv_id: int
    dep_has_worker_id: int
    vdate: str
    uuid: str

    def one_service_entry(self):
        return (f"{self.contracts_id}, {self.serv_id}, {self.dep_has_worker_id}, "
                f"'{self.vdate}', 1, '{self.uuid}'")


class ClientServiceDelete(BaseModel):
    dep_has_worker_id: int
    contracts_id: int
    serv_id: int
    uuid: str


@app.get("/add")
async def add_service(api_key: Annotated[str, Header()] = "",
                      body: Annotated[ClientService, Body(embed=True)] = None):
    """Add new service to client"""
    if api_key:
        return put_sql_data(sql_query=f"""
                    INSERT INTO kcson.api_key_insert_main
                    (contracts_id, serv_id, dep_has_worker_id, vdate, quantity, uuid, check_api_key )
                    VALUES({body.one_service_entry()}, '{api_key})'; 
                """)
    return {'id': 0, 'error': "Wrong api_key"}


@app.get("/delete")
async def delete_service(api_key: Annotated[str, Header()] = "",
                         body: Annotated[ClientServiceDelete, Body(embed=True)] = None):
    """Delete service of client"""
    if api_key:
        return put_sql_data(sql_query=f"""
                UPDATE kcson.api_key_insert_main
                    SET quantity = 0, 
                        check_api_key = '{api_key}', 
                        dep_has_worker_id =  {body.dep_has_worker_id}
                    WHERE uuid = '{body.uuid}'
                """)
    return {'id': 0, 'error': "Wrong api_key"}


@app.get("/healthcheck")
def healthcheck():
    return 'Health - OK'


def put_sql_data(sql_query: str, host: str = MYSQL_HOST, port: int = MYSQL_PORT, user: str = 'web_info',
                 password: str = PASSWORD,
                 database: str = 'kcson'):
    cursor = None
    try:
        database = connect(host=host, port=port, user=user, password=password, database=database)
        cursor = database.cursor()
        cursor.execute(sql_query)
        database.commit()
        ret = cursor.lastrowid
        ret_structure = {"id": ret}
        cursor.close()
        database.close()
    except mysql.connector.errors.IntegrityError:
        ret_structure = {"id": 0, "error": "duplicate"}
        print(ret_structure)
    finally:
        if cursor:
            cursor.close()
        database.close()
    return ret_structure


def get_sql_data(sql_query: str,
                 host: str = MYSQL_HOST,
                 port: int = MYSQL_PORT,
                 user: str = 'web_info',
                 password: str = PASSWORD,
                 database: str = 'kcson') -> Tuple[Tuple[str], Tuple[str]]:
    database = connect(host=host, port=port, user=user, password=password, database=database)
    cursor = database.cursor()
    cursor.execute(sql_query)
    ret = cursor.fetchall()
    cursor.close()
    database.close()
    return cursor.column_names, ret


def this_help():
    print("Read README.md near this file")
    sys.exit(0)


def to_list_of_dict(header, message, default=str):
    """
    Skip None and empty string in message,
    return: json.dumps(message)
    """
    message = [dict(zip(header, data)) for data in message if len(data) > 0]
    return message


client = TestClient(app)


def test_read_main():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"ais_3uson": VERSION}


def main():
    # globals()[""]
    global CONFDIR
    global PASSWORD
    global BIND_HOST
    global BIND_PORT
    global MYSQL_PORT
    global MYSQL_HOST
    global CORS_LIST
    global CONFDIR
    try:
        with open(CONFDIR + r"/mysql-web-worker-password", mode="r", encoding="utf-8") as f:
            PASSWORD = f.readline().replace("\n", "")
    except (FileNotFoundError, PermissionError):
        print("Can't load password from file!!!")

    parser = argparse.ArgumentParser(
        prog="AIS-3USON web-server for supporting mobile clients",
        description="A middleware between SQL DBMS and clients")
    parser.add_argument("--usage", action="count", help="how to use this script")
    parser.add_argument("--secret", "--password", action="store", help="password for SQL authentication")
    parser.add_argument("--mysql-host", action="store", help="Name of host with MySQL database, default: 'localhost'")
    parser.add_argument("--mysql-port", action="store", help="MySQL database port, default: 3306")
    parser.add_argument("--port", action="store", default=48080, help="Which port to use, default: 48080")
    parser.add_argument("--no-ssl", action="count", help="Disable SSL, default port will be PORT+1")
    parser.add_argument("--allow-cors-for", action="append", help="Allow CORS requests from website ")
    parser.add_argument("--debug-port", action="count",
                        help="Only for https: start http server(second server) on port PORT+1")
    parser.add_argument("--conf-dir", action="store", default="/etc/ais3uson",
                        help="Directory with configuration files, default: '/etc/ais3uson'")

    args = parser.parse_args()

    if args.usage:
        this_help()
        sys.exit(0)

    if args.secret:
        PASSWORD = args.secret
        print("Using password from commandline")

    if args.mysql_host:
        MYSQL_HOST = args.mysql_host
        print(f"Using MySQL host: {MYSQL_HOST}")

    if args.mysql_port:
        MYSQL_PORT = args.mysql_port
        print(f"Using MySQL port: {MYSQL_PORT}")

    if args.conf_dir:
        CONFDIR = args.conf_dir
        print(f"Using config directory: {CONFDIR}")

    if args.port:
        BIND_PORT = int(args.port)

    if args.no_ssl:
        BIND_PORT = int(BIND_PORT) + 1

    if args.allow_cors_for:
        for a in args.allow_cors_for:
            CORS_LIST[a] = a
        print(f"Allowed CORS: {CORS_LIST.values()}")

    os.environ["BIND_HOST"] = str(BIND_HOST)
    os.environ["BIND_PORT"] = str(BIND_PORT)
    os.environ["MYSQL_PORT"] = str(MYSQL_PORT)
    os.environ["MYSQL_HOST"] = str(MYSQL_HOST)
    os.environ["PASSWORD"] = str(PASSWORD)
    os.environ["CONFDIR"] = str(CONFDIR)
    os.environ["CORS_LIST"] = json.dumps(CORS_LIST)

    if not args.no_ssl and os.path.isfile(CONFDIR + "/privkey.pem"):
        #############################
        # start with ssl certificate
        # ---------------------------
        if args.debug_port:
            Popen(['python3', '-m', 'ais3uson_www', *sys.argv[1:], "--no-ssl"])
        if os.access(CONFDIR + "/privkey.pem", os.R_OK):
            print(f"Server started https://{BIND_HOST}:{BIND_PORT}")
            uvicorn.run(
                'ais3uson_www:app', port=BIND_PORT, host=BIND_HOST,
                ssl_keyfile=f"{CONFDIR}/privkey.pem",
                ssl_certfile=f"{CONFDIR}/cert.pem")
        else:
            print("Can't read SSL certificate")
    else:
        #############################
        # start without ssl
        # ---------------------------
        print(f"Server started http://{BIND_HOST}:{BIND_PORT}")
        uvicorn.run(
            'ais3uson_www:app', port=BIND_PORT, host=BIND_HOST)

    print("Server stopped.")


if __name__ == "__main__":
    main()
