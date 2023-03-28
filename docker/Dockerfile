# BUILD web-server
# eval $(minikube docker-env)  # for minikube only
# docker build . --tag=ais3uson:latest

FROM alpine:latest
RUN apk add --update --no-cache py3-pip python3
RUN pip install mysql-connector-python
RUN apk del py3-pip
ADD ./web_worker/ais3uson_www.py .
EXPOSE 48080
EXPOSE 48081
ENTRYPOINT ["/usr/bin/python", "./ais3uson_www.py"]

# DEPLOY
# eval $(minikube docker-env)  # for minikube only
# docker run -d -p 48080:48080 --name ais3uson ais3uson
# docker ps  # get hash of ais3uson
# docker commit #hast# ais3uson:v1
# kubectl create deployment ais3uson --image=ais3uson:v1
# kubectl expose deployment ais3uson --type=NodePort --port=48080
# minikube service ais3uson

# CREATE DEPLOYMENT WITH SECRET KEY
# kubectl create secret generic ais3uson-https-cert --from-file=cert.pem=/pathto/ais3uson/cert.pem  --from-file=privkey.pem=/pathto/ais3uson/privkey.pem  --from-file=mysql-web-worker-password=/pathto/ais3uson/mysql-web-worker-password
# kubectl apply -f docker/deploy-ais3uson-certified.yaml
# kubectl expose deployment ais3uson-certified --type=NodePort --port=48080


# FOR QUICK TEST
# docker run -d -p 48080:48080 --name ais3uson ais3uson --mount type=bind,source="/etc/ais3uson,target=/etc/ais3uson,readonly
#
# /etc/ais3uson/ should contain:
# certificate.pem
# privkey.pem
# mysql-web-worker-password

