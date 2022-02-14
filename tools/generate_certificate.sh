#!/bin/bash
openssl req -x509 -newkey rsa:4096 -sha256 -days 3650 -nodes \
   -keyout privkey.pem -out certificate.pem -subj "/CN=example.com" \
   -addext "subjectAltName=IP:80.87.196.11,IP:127.0.0.1,IP:192.168.0.102,IP:192.168.20.2"

echo "move files privkey.pem and certificate.pem to /etc/asi3uson/ of your web server"
echo "use text below as certBase64 of WorkerKey"
cat certificate.pem | base64 -w 0
