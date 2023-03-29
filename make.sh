#!/bin/bash


cd tools || exit
./uic.sh
cd ..

source ./venv/bin/activate
env QT_API=PySide6 python3 -m PyInstaller  --name AIS-3USON   --onedir  --noupx  \
--add-data "src:src" --add-data "LICENSE:." --add-data "tools/connect_and_run.bat:."  \
--add-data "thirdparty:thirdparty" --add-data "widgets_ui:widgets_ui" --add-data "templates:templates"   \
 run_app.py --noconfirm --hidden-import PySide6.QtXml --hidden-import  sqlalchemy.ext.baked --paths src

