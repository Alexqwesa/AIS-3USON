# The helm chart for ais3uson

## Installation

Create initial configuration for mysql:

```bash
# git clone https://github.com/Alexqwesa/AIS-3USON
# cd AIS-3USON/sql
# bash ./gzip_sql_files.sh  # will create mysql_gz folder
kubectl create configmap aismysql-init-data --from-file=mysql_gz
```

Select node for storing mysql data and assign it label: `ais-mysql-role=data`:

```bash
kubectl get nodes --show-labels
kubectl label nodes minikube ais-mysql-role=data  # there minikube is the node you selected
```

Create folder for mysql database(on system with node label ais-mysql-role=data):

```bash
mkdir -p /var/ais-mysql-data  # you can change this path in pv-aismysql-volume.yaml
```

Create a secret with ssl certificate for web worker(and web worker password):

```bash
kubectl create secret generic ais3uson-https-cert --from-file=cert.pem=cert.pem \
                                                  --from-file=privkey.pem=privkey.pem \
                                                  --from-file=mysql-web-worker-password=mysql-web-worker-password

# optionally add test data:
#
```

Create secret with mysql root password:

```bash
kubectl create secret generic mysql-root-password --from-file=mysql-root-password=mysql-root-password 
```

After the first start of aismysql container update web_info password:

```bash
# cd docker/secrets/
kubectl get pods | grep aismysql  # to see exact pod name
kubectl exec -it aismysql -- mysql  -uroot  -p$(cat mysql-root-password) \
        "SET PASSWORD FOR 'web_info'@'%' = '$(cat mysql-web-worker-password)';"
```

Create user admin2 with admin role:
```bash
# cd AIS-3USON/sql
# edit password in 05_admin_and_test_user.sql
kubectl get pods | grep aismysql  # to see exact pod name
kubectl exec -it aismysql -- mysql  -uroot  -p$(cat ../docker/secrets/mysql-root-password)) < 05_admin_and_test_user.sql
```

