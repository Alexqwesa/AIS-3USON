# Setup docker-compose.yml

For real deployment better use, helm chart in helm folder.

### In file docker-compose.yml edit the following line:

MYSQL_ROOT_PASSWORD: example

### Create directory secrets

```bash
mkdir -p secrets # full path AIS-3USON/docker/secrets
```

and put into it files

- cert.pem
- privkey.pem
- mysql-web-worker-password
- mysql-root-password

```bash
chmod 0600 secrets/*  # don't forget to set them private
```

### Run

(docker should be already set up on your host)

```bash
docker compose up
```

### Fill sql database

```bash
cd sql/
export MYSQL_ROOT_PASSWORD=`eval cat ../docker/secrets/mysql-root-password`
docker exec -i aismysql sh -c 'exec mysql -uroot -p"$MYSQL_ROOT_PASSWORD"' < 01_schema.sql
docker exec -i aismysql sh -c 'exec mysql -uroot -p"$MYSQL_ROOT_PASSWORD"' < 02_data.sql
docker exec -i aismysql sh -c 'exec mysql -uroot -p"$MYSQL_ROOT_PASSWORD"' < 03_test_data.sql
docker exec -i aismysql sh -c 'exec mysql -uroot -p"$MYSQL_ROOT_PASSWORD"' < 04_security.sql
OPTIONAL:
docker exec -i aismysql sh -c 'exec mysql -uroot -p"$MYSQL_ROOT_PASSWORD"' < 05_extended_test_data.sql
docker exec -i aismysql sh -c 'exec mysql -uroot -p"$MYSQL_ROOT_PASSWORD"' < extended_test_data_2.sql
```