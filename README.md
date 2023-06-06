# AIS 3USON ( "АИС ТриУСОН" )

<img align="right" src="src/images/ais-3uson-logo-128.png" alt="logo">

An AIS-3USON project contain both Backend(SQL) and desktop Frontend(python+Qt), it supports Linux and Windows OS.

Проект "АИС ТриУСОН" предназначен для автоматизации работы в учреждениях социальной сферы. В данном репозитории ПО
размещены сервер и клиент АИС, которые могут работать в операционных системах семейств Windows и Linux.

Полное название: информационная система "АИС ТриУСОН" ("Автоматизированная Информационная Система Учета Услуг Учреждений
Социального Обслуживания Населения").

## Содержание

- [Установка](#установка)
- [Сборка клиентского приложения](#сборка-клиентского-приложения)
- [Использование](#использование)
- [Для Разработчиков](#для-разработчиков)
- [TODO](#todo)
- [Разработчики](#разработчики)
- [Лицензия](#лицензия)

## Установка

Для запуска серверных компонент в Docker подготовлен пакет helm (пакет конфигурационных файлов
Kubernetes) [инструкция по установке](docker/helm/README.md),
также есть файл [docker-compose.yml](docker/docker-compose.yml)(устаревший).

Локальная установка:

- Установить SQL СУБД - приложение протестировано на СУБД MySQL 8 _(для других СУБД не забудьте установить другие
  коннекторы и изменить настройки по умолчанию в файле 3uson.conf)_
- Импортировать в БД из директории sql/mysql следующие файлы(для **mariaDB** используйте файлы директории sql/mariadb):
    - 01_schema.sql
    - 02_data.sql
    - 03_test_data.sql (для тестов: 05_extended_test_data.sql и 06_extended_test_data_2.sql )
    - 04_security.sql
    - 05_activate_admin_and_test_user.sql
- В файле `05_activate_admin_and_test_user.sql` перед импортом необходимо сменить пароль пользователя-администратора admin2 (SQL роль admin),
  который будет администрировать базу данных из настольного
  приложения(подробнее см. раздел [Использование](#использование))

## Сборка клиентского приложения

Windows версия **pySide6** на момент разработки поддерживала только 64 битную архитектуру, поэтому сборки для
Windows должны использовать 64 битные утилиты(Python 64bit, MSVC Redistributable 64bit, SQL Connector)

Windows версия **pySide2** на момент разработки поддерживала только 32 битную архитектуру, поэтому сборки для Windows
должны использовать 32 битные утилиты(Python 32bit, MSVC Redistributable 32bit, SQL Connector)

Подготовьте среду python c необходимыми пакетами:
```bash
git clone https://github.com/Alexqwesa/AIS-3USON
cd AIS-3USON
virtualenv -p python3 venv
source venv/bin/activate
pip3 install -r requirements.txt
```
- отредактируйте в файле 3uson.conf ip-адрес вашего сервера (и др. настройки по умолчанию);
- отредактируйте в файле `make.bat`(`make.sh`) путь к вашему профилю Python (и используемую библиотеку qt, по умолчанию используется pyside6)); 
- запустите `make.bat` (для Windows) или `make.sh` (для Linux);
- полученные дистрибутивы удобно распространять через общую директорию по локальной сети (см. tools)

Запуск приложения возможен без установки, однако:

- на **клиентских Windows компьютерах** должны быть установлены:
    - MSVC Redistributable [vcredist_x86.exe](https://www.microsoft.com/en-US/download/details.aspx?id=48145)
    - MySQL Connector/ODBC 8  [mysql-connector-odbc.msi](https://dev.mysql.com/downloads/connector/odbc/)
- на **клиентских Linux компьютерах** нужно установить и указать:
    - MySQL Connector/ODBC 8  [mysql-connector-odbc.tar.gz](https://dev.mysql.com/downloads/connector/odbc/)
    - unixODBC
    - добавить в /etc/unixODBC/odbcinst.ini следующие строки:

```
[MySQL ODBC 8.0 Unicode Driver]
Driver=/путь/куда/вы/установили/libmyodbc8w.so
UsageCount=1
```

## Использование

Пользователь-администратор через клиентское приложение создает:

- отделения
- заведующих отделений, специалистов, работников (назначает роли, выдает пароли);
- вводит изменившийся прожиточный минимум;
- вводит изменившиеся тарифы на услуги;
- и др.

Заведующие:

- вводят людей и их ПД
- создают/закрывают договора
- контролируют работу специалистов и работников
- печатают акты, квитанции, отчеты из АИС ТриУСОН

Специалисты:

- вводят оказанные услуги

Работники:

- вводят оказанные услуги

Бухгалтер

- вводит информацию о пришедших платежах (функционал в разработке)

## Для Разработчиков

Для запуска приложения без сборки - запустите файл run_app.py (в корневой директории проекта)

Приложение-клиент написано с использованием инструмента Qt Designer, и логика GUI прописана в .ui файлах (какая кнопка
на какой виджет влияет).

Сами классы виджетов содержат лишь обработчики сигналов/слотов. От этого правила я немного отошел при написании классов
вкладок(QTabWidget - файл tab_classes.py), просто потому, что в Qt Designer это было бы сделать сложно, и не всегда
возможно.

TODO:

### Безопасность

Созданные пользователи, имеют доступ лишь к использованию (**USE**) схемы бд и выполнению в ней процедур(**Execute**),
при подключении клиентское ПО выполняет команды `call GET_PRIVILEGES` и `SET ROLE all` которые назначают
пользователю роли и активируют их.
Процедура GET_PRIVILEGES назначает роль в зависимости от записей в таблице dep_has_worker.
Так же введены дополнительные ограничения: пользователь может вводить услуги только в свое отделение (для некоторых
пользователей ограничен и просмотр услуг по отделению) и другие правила - см. файл Безопасность.

Если пользователю нужно работать сразу с несколькими отделениями - этого можно добиться:

1. Завести в таблице dep_has_worker вторую запись на работника из таблицы worker (в этой таблице у работника должна -
   быть только одна запись - TODO)
2. Создать над объединенное отделение в из нескольких отделений в таблице complex_dep (ВНИМАНИЕ: данная функция
   сделана для получения отчетов сразу по нескольким отделениям, а не для ввода услуг!)

## Разработчики

[@Alexqwesa](https://github.com/Alexqwesa).

## Лицензия

[LGPLv3](LICENSE) © Savin Aleksander Viktorovich (Савин Александр Викторович)
