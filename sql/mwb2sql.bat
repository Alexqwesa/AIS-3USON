@echo off
REM generate sql from mwb
REM usage: mwb2sql.bat {.mwb file} {output file}

SET WORKBENCH="C:\Program Files\MySQL\MySQL Workbench 8.0 CE\MySQLWorkbench.exe"
SET OUTPUT=kcson.sql
%WORKBENCH% ^
  -open kcson.mwb ^
  -run-python "import os;import grt;from grt.modules import DbMySQLFE as fe;c = grt.root.wb.doc.physicalModels[0].catalog;fe.generateSQLCreateStatements(c, c.version, {});fe.createScriptForCatalogObjects(os.getenv('OUTPUT'), c, {})" ^
  -quit-when-done
