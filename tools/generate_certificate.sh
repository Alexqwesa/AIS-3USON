#!/bin/bash
echo ""
echo "----------------------------------"
echo "JUST USE certbot to create your certificate"
echo "then move files privkey.pem and cert.pem to /etc/asi3uson/ of your web server"
echo "=================================="
echo "or use OUTDATED method"

echo "
# OUTDATED
#
##  GENERATE CUSTOM SELFSIGNED CERTIFICATE

openssl req -x509 -newkey rsa:4096 -sha256 -days 3650 -nodes \
   -keyout privkey.pem -out certificate.pem -subj "/CN=example.com" \
   -addext "subjectAltName=IP:your_ip,IP:127.0.0.1"
"
echo "move files privkey.pem and cert.pem to /etc/asi3uson/ of your web server"
echo "use text below as certBase64 of WorkerKey"
echo "cat certificate.pem | base64 -w 0"
