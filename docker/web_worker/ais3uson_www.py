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
import argparse
import json
import os
import ssl
import sys
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
groupadd ais3uson
# or prohibit login to exist user with:  passwd -l 
# I strongly recommend:
# to use only key authentication: PasswordAuthentication no  (in file /etc/ssh/sshd_conf) 

# save script on server to /usr/local/bin
mkdir -p /usr/local/bin
cp -a %s /usr/local/bin/

# create file for storing password and secure it
mkdir /etc/ais3uson/
touch /etc/ais3uson/mysql-web-worker-password
chown ais3uson:ais3uson /etc/ais3uson/ -R
chmod 0700 /etc/ais3uson/
chmod 0600 /etc/ais3uson/*
# WRITE PASSWORD FOR USER web_info INTO THIS FILE


# create systemd service
cat < EOF >> /etc/systemd/system/ais3uson_www.service
[Unit]
Description=Web worker for AIS3USON

[Service]
Type=simple
User=ais3uson
Group=ais3uson
Restart=on-failure
Environment=PYTHONUNBUFFERED=1
ExecStart=/usr/bin/python3  /usr/local/bin/ais3uson_www.py 
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
    sys.exit(0)


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
SERVERPORT = 48080
PASSWORD = "nopassword"
MYSQLPORT = 3306
MYSQLHOST = "127.0.0.1"
CONFDIR = "/etc/ais3uson"
try:
    with open(CONFDIR + r"/mysql-web-worker-password", mode="r") as f:
        PASSWORD = f.readline().replace("\n", "")
except (FileNotFoundError, PermissionError):
    print("Can't load password from file!!!")


def json_dumps(message, default=str):
    for m in message:
        s = set()
        for k, v in m.items():
            if v in ("", "None"):
                s.add(k)
        for k in s:
            m.pop(k, None)
    return json.dumps(message, default=default)


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
        if self.path.startswith("/clients"):
            _, api_key = self.get_auth()
            if api_key:
                message = self.get_sql_data(sql_query="""
                    select  contract_id, dep_id, client_id, contract, client, dhw_id, 
                        comment, percent, max_pay 
                    from    _apikey_has_contracts 
                    where api_key = '%s'
                """ % self.api_key)
                # send the message back
                json_message = json_dumps(message, default=str)
                self.send_json_header(json_message)
                self.write(json_message)
        elif self.path == "/services":
            _, api_key = self.get_auth()
            if api_key:
                message = self.get_sql_data(sql_query="""
                        select id, tnum, serv_text, total, image, serv_id_list, sub_serv, short_text
                        , price 
                        from _api_key_services;
                    """)
                # send the message back
                json_message = json_dumps(message, default=str)
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
                json_message = json_dumps(message, default=str)
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
        if self.path == "/add":
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
        self.send_header("Content-Length", str(len(content)))
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
        self.write("<html><head><title>Statistic for WEB-sevrer AIS-3USON</title></head>")
        self.write("<body>")
        self.write("<p>Statistic for WEB-sevrer AIS-3USON</p>")
        self.write("<p>Request: %s</p>" % self.path)
        self.write("<p>Thread: %s</p>" % threading.current_thread().name)
        self.write("<p>Thread Count: %s</p>" % threading.active_count())
        self.write("</body></html>")

    def put_sql_data(self, host=MYSQLHOST, port=MYSQLPORT, user='web_info', password=PASSWORD,
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

    def get_sql_data(self, host=MYSQLHOST, port=MYSQLPORT, user='web_info', password=PASSWORD,
                     database='kcson', sql_query="select * from holiday"):
        if self.api_key:
            database = connect(host=host, port=port, user=user, password=password, database=database)
            cursor = database.cursor()
            cursor.execute(sql_query)
            ret = cursor.fetchall()
            cursor.close()
            ret_structure = dict(zip(cursor.column_names, ret))
            # database.commit()
            database.close()
            return ret_structure
        return "Wrong authorization key"


def ssl_wrap_socket(sock, keyfile=None, certfile=None,
                    server_hostname=None,
                    server_side=None):
    context = ssl.create_default_context(ssl.Purpose.CLIENT_AUTH)
    context.load_cert_chain(certfile, keyfile)
    if ssl.HAS_SNI:  # Platform-specific: OpenSSL with enabled SNI
        return context.wrap_socket(sock, server_hostname=server_hostname, server_side=server_side)
    return context.wrap_socket(sock, server_side=server_side)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        prog="AIS-3USON web-server for supporting mobile clients",
        description="A middleware between SQL DBMS and clients")
    parser.add_argument("--usage", action="count", help="how to use this script")
    parser.add_argument("--secret", "--password", action="store", help="password for SQL authentication")
    parser.add_argument("--mysql_host", action="store", help="Name of host with MySQL database, default: 'localhost'")
    parser.add_argument("--port", action="store", default=48080, help="Use port, default: 48080")
    parser.add_argument("--debug-port", action="count",
                        help="Only for https: start http server(second server) on port 48081")
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
        MYSQLHOST = args.mysql_host
        print("Using MySQL host: %s" % MYSQLHOST)

    if args.conf_dir:
        CONFDIR = args.conf_dir
        print("Using config directory: %s" % CONFDIR)

    webServer = ThreadingHTTPServer((hostName, SERVERPORT), MyServer)
    if os.path.isfile(CONFDIR + "/privkey.pem"):
        if os.access(CONFDIR + "/privkey.pem", R_OK):
            webServer.socket = ssl_wrap_socket(webServer.socket, keyfile=CONFDIR + "/privkey.pem",
                                               certfile=CONFDIR + "/cert.pem",
                                               server_side=True)
            print("Server started https://%s:%s" % (hostName, SERVERPORT))
            if args.debug_port:
                webServer2 = ThreadingHTTPServer((hostName, 48081), MyServer)
                thread = threading.Thread(target=webServer2.serve_forever)
                thread.start()
        else:
            print("Can't read SSL certificate")
    else:
        print("Server started http://%s:%s" % (hostName, SERVERPORT))

    try:
        webServer.serve_forever()
    except KeyboardInterrupt:
        pass

    webServer.server_close()
    print("Server stopped.")
