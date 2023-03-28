#!/bin/bash

mkdir -p mysql_gz || true
for f in mysql/*;
 do
cat  "$f" | gzip > "${f/mysql/mysql_gz/}.gz"
done

mkdir -p mariadb_gz || true
for f in mariadb/*;
 do
cat  "$f" | gzip > "${f/mariadb/mariadb_gz/}.gz"
done
