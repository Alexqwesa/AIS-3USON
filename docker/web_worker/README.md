# Installation on linux without docker (outdated)

The [ais3uson_www.py](ais3uson_www.py) script is part of helm package, there is also a docker-compose.yaml to run it,
and for debugging you can just run it(or `uvicorn ais3uson_www:app --reload`), so this method is outdated:

```bash
pip3 install mysql-connector-python

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


```