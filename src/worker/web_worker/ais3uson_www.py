#!/usr/bin/python3
# -------------------------------------------------------------------------------
# -*- coding: utf-8 -*-
# Name:        AIS 3USON web worker
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
import json
import os

from mysql.connector import connect
import threading

from http.server import BaseHTTPRequestHandler

DEBUG_MODE = None
if os.environ["DEBUG_MODE"].lower() == "on":
    DEBUG_MODE = True
#############################
# add support python 3.5
# ---------------------------
try:
    _ = ModuleNotFoundError
except Exception:  # Python 3.6 and before.
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

README_linux = """
# To setup this service:

useradd -r -s /bin/false ais3uson
# or prohibit login to exist user with  passwd -l 
# consider to use only key authentication: PasswordAuthentication no  (/etc/ssh/sshd_conf) 

# save script on server to /usr/local/bin
mkdir -p /usr/local/bin


# create file for password and secure it
touch /etc/ais3uson.key
chown ais3uson:ais3uson /etc/ais3uson.key
chmod 0600 /etc/ais3uson.key
# write password to this file

# 
# 

cat < EOF >> /etc/systemd/system/ais3uson_www
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

#enable service 
systemctl enable ais3uson_www
systemctl start  ais3uson_www
systemctl status ais3uson_www


"""

hostName = "localhost"
serverPort = 48080
PASSWORD = "nopassword"
try:
    with open(r"/etc/ais3uson.key", mode="r") as f:
        PASSWORD = f.readline()
except (FileNotFoundError, PermissionError):
    print("Can't load password!!!")
    pass


class MyServer(BaseHTTPRequestHandler):
    # def __init__(self):
    #     super().__init__()
    def do_OPTIONS(self):
        self.send_response(204)
        # self.send_header('Access-Control-Allow-Origin', '*')
        self.send_header('Access-Control-Allow-Methods', 'GET, POST, OPTIONS')
        self.send_header("Access-Control-Allow-Headers", "X-Requested-With")
        self.send_header("Access-Control-Allow-Headers", "Content-Type")
        self.end_headers()
        # self.process_request()

    def do_GET(self):
        if self.path == "/stat":
            self.stat()
        elif self.path.startswith("/get"):
            self.get()
        else:
            pass
            # TODO: about + link to app here
        # elif self.path.startswith("/post"):
        #     self.post()

    def json_header(self):
        self.send_response(200)
        # self.send_header("Access-Control-Allow-Origin", "*")
        self.send_header("Content-type", "application/json")
        self.end_headers()

    def end_headers(self):
        if DEBUG_MODE:
            self.send_header('Access-Control-Allow-Origin', '*')
        super().end_headers()

    def write(self, msg):
        self.wfile.write(bytes(msg, "utf-8"))

    def do_POST(self):
        # refuse to receive non-json content
        if self.headers.get_content_type() != 'application/json':
            self.send_response(400)
            self.end_headers()
            return

        if self.path == "/fio":
            _, api_key = self.get_auth()
            if api_key:
                message = self.get_sql_data(sql_query="""
                    select * from _apikey_has_contracts where api_key = '%s'
                """ % self.api_key)
                # send the message back
                self.json_header()
                # message=message+message # test
                self.write(json.dumps(message, default=str))
        elif self.path == "/planned":
            _, api_key = self.get_auth()
            if api_key:
                message = self.get_sql_data(sql_query="""
                        select contract_id,serv_id,planned,filled from _api_key_planned where api_key = '%s'
                    """ % self.api_key)
                # send the message back
                self.json_header()
                self.write(json.dumps(message, default=str))
        elif self.path == "/services":
            _, api_key = self.get_auth()
            if api_key:
                message = self.get_sql_data(sql_query="""
                        select id, tnum, serv_text, total, image, serv_id_list, sub_serv, short_text from _api_key_services 
                    """)
                # send the message back
                self.json_header()
                self.write(json.dumps(message, default=str))
        elif self.path == "/add":
            data, api_key = self.get_auth()
            if api_key:
                message = self.get_sql_data(sql_query="""
                        INSERT INTO kcson.api_key_insert_main
(contracts_id, serv_id, dep_has_worker_id, vdate, uslnum, uuid)
VALUES(%(contracts_id)s , %(serv_id)s, %(dep_has_worker_id)s, '%(vdate)s', 1, '%(uuid)s' ); 
                    """ % data)
                # send the message back
                self.json_header()
                self.write(json.dumps(message, default=str))
        elif self.path == "/test":
            # read the message and convert it into a python dictionary
            message, api_key = self.get_auth()
            if api_key:
                # add a property to the object
                self.api_key = "123"
                message['received'] = self.get_sql_data()
                # send the message back
                self.json_header()
                self.write(json.dumps(message, default=str))

    def get_auth(self):
        content_len = int(self.headers.get('Content-Length'))
        message = json.loads(self.rfile.read(content_len))
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
        return message, self.api_key

    def get(self):
        pass

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

    def get_sql_data(self, host='localhost', port=3306, user='web_info', password=PASSWORD,
                     database='kcson', sql_query="select * from holiday"):
        if self.api_key:
            database = connect(host=host, port=port, user=user, password=password, database=database)
            cursor = database.cursor()
            cursor.execute(sql_query)
            if "INSERT INTO" in sql_query:
                database.commit()
                ret = cursor.lastrowid
                cursor.close()
                ret_structure = [{"id": ret}]
            else:
                ret = cursor.fetchall()
                cursor.close()
                ret_structure = [{key: val for key, val in zip(cursor.column_names, lst)} for lst in ret]
            # database.commit()
            database.close()
            return ret_structure
        return "Wrong authorization key"


#
# class mysql_json:
#     def __init__(self, host='localhost', port="3366", user='web_info', password=PASSWORD,
#                  database='kcson'):
#         pass


if __name__ == "__main__":
    webServer = ThreadingHTTPServer((hostName, serverPort), MyServer)
    # webServer.socket = ssl.wrap_socket(webServer.socket, keyfile='./privkey.pem',certfile='./certificate.pem',
    #                   server_side=True)
    # print("Server started http://%s:%s" % (hostName, serverPort))

    try:
        webServer.serve_forever()
    except KeyboardInterrupt:
        pass

    webServer.server_close()
    print("Server stopped.")
