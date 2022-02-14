#!/usr/bin/python3
# -------------------------------------------------------------------------------
# -*- coding: utf-8 -*-
# Name:        AIS 3USON web worker
# Purpose:     Middleware to connect SQL DBMS to mobile clients,
#                   this file should have minimal amount of dependency,
#                   and should be able to run on any system
#
# Author:      Savin Alexander Viktorovich aka alexqwesa
# Created:     2021-2022
# Copyright:   Savin Alexander Viktorovich aka alexqwesa
# Licence:     LGPL 3
# This software is licensed under the "LGPLv3" License as described in the "LICENSE" file,
# which should be included with this package. The terms are also available at
# http://www.gnu.org/licenses/lgpl-3.0.html
# -------------------------------------------------------------------------------
import os
import ssl
import sys
import json
import threading
from http.server import BaseHTTPRequestHandler
from os import R_OK

DEBUG_MODE = True
#############################
# add support python pre 3.6
# ---------------------------
try:
    _ = ModuleNotFoundError
except Exception:  # for Python 3.6 and before.
    class ModuleNotFoundError(Exception):
        pass

try:
    from http.server import ThreadingHTTPServer
except (ModuleNotFoundError, ImportError):
    # python 3.6 and before.
    import socketserver
    from http.server import HTTPServer


    class ThreadingHTTPServer(socketserver.ThreadingMixIn, HTTPServer):
        pass

# import ssl
#############################
# import mysql connector with check
# ---------------------------

README_linux = """
# To setup this service:

useradd -r -s /bin/false ais3uson
# or prohibit login to exist user with:  passwd -l 
# I strongly recommend:
# to use only key authentication: PasswordAuthentication no  (in file /etc/ssh/sshd_conf) 

# save script on server to /usr/local/bin
mkdir -p /usr/local/bin
cp -a %s /usr/local/bin/

# create file for storing password and secure it
mkdir /etc/ais3uson/
touch /etc/ais3uson/mysql.key
chown ais3uson:ais3uson /etc/ais3uson/ -R
chmod 0700 /etc/ais3uson/ -R
chmod 0600 /etc/ais3uson/mysql.key
# WRITE PASSWORD FOR USER web_info INTO THIS FILE


# create systemd service
cat < EOF >> /etc/systemd/system/ais3uson_www.service
[Unit]
Description=Web worker for AIS3USON

[Service]
Type=simple
User=ais3uson
Group=nogroup
Restart=on-failure
Environment=PYTHONUNBUFFERED=1
ExecStart=/usr/bin/python  /usr/local/bin/ais3uson_www.py 
StartLimitInterval = 60
StartLimitBurst = 10

[Install]
WantedBy=multi-user.target

EOF

# check it works
chmod a+x /usr/local/bin/ais3uson_www.py
/usr/local/bin/ais3uson_www.py     # check it works , and then kill it

# enable service 
systemctl enable ais3uson_www
systemctl start  ais3uson_www
systemctl status ais3uson_www


""" % __file__


def this_help():
    print(README_linux)
    exit()


try:
    import mysql
    from mysql.connector import connect
except:
    print("=============================")
    print("Install mysql connector")
    print("pip install mysql-connector-python")
    print("=============================")
    this_help()

hostName = "0.0.0.0"  # "localhost"  if this script used with ssh -NR
serverPort = 48080
PASSWORD = "nopassword"
MYSQLPORT = 3306
try:
    with open(r"/etc/ais3uson/mysql.key", mode="r") as f:
        PASSWORD = f.readline().replace("\n", "")
except (FileNotFoundError, PermissionError):
    print("Can't load password!!!")
    pass


class MyServer(BaseHTTPRequestHandler):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.api_key = None

    def do_OPTIONS(self):
        self.send_response(200, "ok")
        # self.send_header('Access-Control-Allow-Origin', '*') # already done if DEBUG=True, don't send twice!
        self.send_header("Access-Control-Allow-Credentials", 'true')
        self.send_header('Access-Control-Allow-Methods', 'GET, POST, DELETE, OPTIONS')
        self.send_header("Access-Control-Allow-Headers", "X-Requested-With, Content-Type, api_key")
        self.end_headers()
        # self.process_request()

    def do_GET(self):
        if self.path == "/stat":
            self.stat()
            print("stat requested")
        #############################
        # refuse to receive non-json content
        # ---------------------------
        if self.headers.get_content_type() != 'application/json':
            self.send_response(400)
            self.end_headers()
            return
        elif self.path.startswith("/clients"):
            _, api_key = self.get_auth()
            if api_key:
                message = self.get_sql_data(sql_query="""
                    select  contract_id, dep_id, client_id, contract, client, dhw_id 
                    from    _apikey_has_contracts 
                    where api_key = '%s'
                """ % self.api_key)
                # send the message back
                json_message = json.dumps(message, default=str)
                self.send_json_header(json_message)
                self.write(json_message)
        elif self.path == "/services":
            _, api_key = self.get_auth()
            if api_key:
                message = self.get_sql_data(sql_query="""
                        select id, tnum, serv_text, total, image, serv_id_list, sub_serv, short_text 
                        from _api_key_services;
                    """)
                # send the message back
                json_message = json.dumps(message, default=str)
                self.send_json_header(json_message)
                self.write(json_message)
        elif self.path == "/planned":
            _, api_key = self.get_auth()
            if api_key:
                message = self.get_sql_data(sql_query="""
                        select contract_id,serv_id,planned,filled 
                        from _api_key_planned 
                        where api_key = '%s'
                    """ % self.api_key)
                # send the message back
                json_message = json.dumps(message, default=str)
                self.send_json_header(json_message)
                self.write(json_message)
        else:
            pass
            # TODO: about + link to app here
        # elif self.path.startswith("/post"):
        #     self.post()

    def do_POST(self):
        # refuse to receive non-json content
        if self.headers.get_content_type() != 'application/json':
            self.send_response(400)
            self.end_headers()
            return
        elif self.path == "/add":
            data, api_key = self.get_auth()
            if api_key:
                message = self.put_sql_data(sql_query="""
                        INSERT INTO kcson.api_key_insert_main
                        (contracts_id, serv_id, dep_has_worker_id, vdate, quantity, uuid, check_api_key )
                        VALUES(%(contracts_id)s , %(serv_id)s, %(dep_has_worker_id)s, '%(vdate)s', 1,
                         '%(uuid)s', '%(check_api_key)s' ); 
                    """ % data)
                # send the message back
                json_message = json.dumps(message, default=str)
                # json_message = '{"id": 0}'
                self.send_json_header(json_message)
                self.write(json_message)

    def do_DELETE(self):
        # refuse to receive non-json content
        if self.headers.get_content_type() != 'application/json':
            self.send_response(400)
            self.end_headers()
            return
        if self.path == "/delete":
            data, api_key = self.get_auth()
            if api_key:
                message = self.put_sql_data(sql_query="""
                    UPDATE kcson.api_key_insert_main
                        SET quantity = 0, 
                            check_api_key = '%(check_api_key)s', 
                            dep_has_worker_id =  %(dep_has_worker_id)s
                        WHERE uuid = '%(uuid)s' 
                    """ % data)
                # send the message back
                json_message = json.dumps(message, default=str)
                self.send_json_header(json_message)
                self.write(json_message)

    def send_json_header(self, content=""):
        self.send_response(200, "ok")
        self.send_header("Content-type", "application/json")
        self.send_header("Content-Length", len(content))
        self.end_headers()

    def end_headers(self):
        if DEBUG_MODE:
            self.send_header('Access-Control-Allow-Origin', '*')
        super().end_headers()

    def write(self, msg):
        self.wfile.write(bytes(msg, "utf-8"))

    def get_auth(self):
        self.api_key = None
        message = None
        try:
            content_len = int(self.headers.get('Content-Length'))
            message = json.loads(self.rfile.read(content_len))
        except TypeError:
            pass
        try:
            self.api_key = self.headers.get("api_key")
        except KeyError:
            self.api_key = message["api_key"]
        #############################
        # api_key will be passed to mysql - TODO: make more checks
        # ---------------------------
        if not self.api_key:
            self.api_key = None
        if isinstance(self.api_key, str):
            for c in ["'", '"']:
                if c in self.api_key:
                    self.api_key = None
        if message:
            message['check_api_key'] = self.api_key
        return message, self.api_key

    def stat(self):
        self.send_response(200)
        self.send_header("Content-type", "text/html; charset=utf-8")
        self.end_headers()
        self.write("<html><head><title>Статистика WEB-сервера АИС ТриУСОН</title></head>")
        self.write("<body>")
        self.write("<p>Статистика WEB-сервера АИС ТриУСОН</p>")
        self.write("<p>Request: %s</p>" % self.path)
        self.write("<p>Thread: %s</p>" % threading.currentThread().getName())
        self.write("<p>Thread Count: %s</p>" % threading.active_count())
        self.write("</body></html>")

    def put_sql_data(self, host='localhost', port=MYSQLPORT, user='web_info', password=PASSWORD,
                     database='kcson', sql_query="select * from holiday"):
        if self.api_key:
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
        return "Wrong authorization key"

    def get_sql_data(self, host='localhost', port=MYSQLPORT, user='web_info', password=PASSWORD,
                     database='kcson', sql_query="select * from holiday"):
        if self.api_key:
            database = connect(host=host, port=port, user=user, password=password, database=database)
            cursor = database.cursor()
            cursor.execute(sql_query)
            ret = cursor.fetchall()
            cursor.close()
            ret_structure = [{key: val for key, val in zip(cursor.column_names, lst)} for lst in ret]
            # database.commit()
            database.close()
            return ret_structure
        return "Wrong authorization key"


if __name__ == "__main__":
    if len(sys.argv) > 1:
        if sys.argv[1] in ["-h", "--help", "/h", "/help"]:
            this_help()

    webServer = ThreadingHTTPServer((hostName, serverPort), MyServer)
    if os.path.isfile("/etc/ais3uson/privkey.pem") and os.access("/etc/ais3uson/privkey.pem", R_OK):
        webServer.socket = ssl.wrap_socket(webServer.socket, keyfile='/etc/ais3uson/privkey.pem',
                                           certfile='/etc/ais3uson/certificate.pem',
                                           server_side=True)
        print("Server started https://%s:%s" % (hostName, serverPort))
    else:
        print("Server started http://%s:%s" % (hostName, serverPort))


    try:
        webServer.serve_forever()
    except KeyboardInterrupt:
        pass

    webServer.server_close()
    print("Server stopped.")
