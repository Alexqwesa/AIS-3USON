#!/bin/bash


cd tools
./uic.sh
cd ..

#os.environ['QT_API'] = PySide2
source ./venvqt38-32/bin/activate
env QT_API=PySide2 python3 -m PyInstaller  --name AIS-3USON   --onedir  --noupx  \
--add-data "src:src" --add-data "LICENSE:." --add-data "tools/connect_and_run.bat:."  \
--add-data "thirdparty:thirdparty" --add-data "widgets_ui:widgets_ui" --add-data "templates:templates"   \
 run_app.py --noconfirm --hidden-import PySide2.QtXml --hidden-import  sqlalchemy.ext.baked --paths src

#  --specpath "build"
# --add-data "../src/3uson.conf:src"  \
#--add-data "../src/MainWindow.ui:src" --add-data "../src/login_dialog.ui:src"
#--add-data "../src/templates:src/templates"
