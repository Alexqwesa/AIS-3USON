set PYTHONOPTIMIZE=1

rem ./venv/bin/activate.bat
set QT_API=PySide2
set PY_QT=PySide2
rmdir  dist\AIS-3USON -R

cd tools
call uic.bat
cd ..

venvqt38-32\Scripts\pyinstaller.exe --clean --name AIS-3USON   --onedir  --noupx   ^
--add-data "src;src" --add-data "LICENSE;." --add-data "tools/connect_and_run.bat;."  ^
--add-data "thirdparty;thirdparty" --add-data "widgets_ui;widgets_ui" --add-data "templates;templates"   ^
 run_app.py --noconfirm --hidden-import PySide2.QtXml --hidden-import  sqlalchemy.ext.baked  --paths src
 rem  --hidden-import src

