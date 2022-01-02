USE `kcson`;


INSERT INTO `kcson`.`dep` (`id`, `dep`, `dep_full_name`, `note`) VALUES (DEFAULT, 'Не указано', 'Не указано', NULL);

INSERT INTO kcson.worker (id, worker, `user`, prim, role_id, dep_id, archive) VALUES(1, 'Не указан(Работник)', 'newuser', NULL, 1, 1, 0);
INSERT INTO kcson.worker (id, worker, `user`, prim, role_id, dep_id, archive) VALUES(2, 'Не указан(Админ)', 'root', NULL, 1, 1, 0);


INSERT INTO kcson.ufio (id, ufio, ufio_short, ufioDeath, ufiobirth, ESRN, prim, phone, snils, curator, `create`, ts, cr_by, upd_by, cr_dep_id) VALUES(1, 'Тестовый человек', 'Тx ', '1900-01-01', '1976-01-01', 123461111, '1323', NULL, NULL, NULL, NULL, '2020-06-26 15:26:39', NULL, 1, 0);
INSERT INTO kcson.ufio (id, ufio, ufio_short, ufioDeath, ufiobirth, ESRN, prim, phone, snils, curator, `create`, ts, cr_by, upd_by, cr_dep_id) VALUES(2, 'Тестовый чел2', NULL, NULL, '1987-01-01', 543, NULL, NULL, NULL, NULL, NULL, '2020-01-21 15:04:59', NULL, 1, 0);


INSERT INTO kcson.category (id, category, archive, prim, total, subof) VALUES(1, 'УВОВр', 0, 'Участник Отечественной Войны(ЖБЛ,ТБЛ,ТТ,узники, вдовы)', NULL, NULL);
INSERT INTO kcson.category (id, category, archive, prim, total, subof) VALUES(2, 'УВОВ', 0, 'Участник Отечественной Войны(ЖБЛ,ТБЛ,ТТ)', NULL, 1);
INSERT INTO kcson.category (id, category, archive, prim, total, subof) VALUES(3, 'ВТ', NULL, 'Ветеран труда', NULL, NULL);
INSERT INTO kcson.category (id, category, archive, prim, total, subof) VALUES(4, 'ПМИНОБ', NULL, 'Пенсионер мин. обороны', NULL, NULL);
INSERT INTO kcson.category (id, category, archive, prim, total, subof) VALUES(5, 'ИВОВ', NULL, 'Инвалид ВОВ', NULL, 2);
INSERT INTO kcson.category (id, category, archive, prim, total, subof) VALUES(6, 'УВ', NULL, NULL, NULL, 2);
INSERT INTO kcson.category (id, category, archive, prim, total, subof) VALUES(7, 'ЖБЛ', NULL, NULL, NULL, 2);
INSERT INTO kcson.category (id, category, archive, prim, total, subof) VALUES(8, 'ТБЛ', NULL, NULL, NULL, 2);
INSERT INTO kcson.category (id, category, archive, prim, total, subof) VALUES(9, 'ТТ', NULL, NULL, NULL, 2);
INSERT INTO kcson.category (id, category, archive, prim, total, subof) VALUES(10, 'УТТ', NULL, NULL, NULL, 2);
INSERT INTO kcson.category (id, category, archive, prim, total, subof) VALUES(11, 'Узники конц.л.', NULL, NULL, NULL, 1);
INSERT INTO kcson.category (id, category, archive, prim, total, subof) VALUES(12, 'Вдовы ВОВ', NULL, NULL, NULL, 1);
INSERT INTO kcson.category (id, category, archive, prim, total, subof) VALUES(13, 'Инвалид', 0, NULL, 0, NULL);
INSERT INTO kcson.category (id, category, archive, prim, total, subof) VALUES(14, 'ИПР', NULL, NULL, 0, 13);
INSERT INTO kcson.category (id, category, archive, prim, total, subof) VALUES(15, 'Социо-культ. ИПР', NULL, NULL, NULL, 14);
INSERT INTO kcson.category (id, category, archive, prim, total, subof) VALUES(16, 'Социо-псих. ИПР', NULL, NULL, NULL, 14);



INSERT INTO kcson.ufio_has_category (ufio_id, category_id, get_date, archive, prim, `create`, ts, cr_by, upd_by, stop_date) VALUES(1, 1, NULL, NULL, '4113', NULL, NULL, 2, 2, '9999-01-01');
INSERT INTO kcson.ufio_has_category (ufio_id, category_id, get_date, archive, prim, `create`, ts, cr_by, upd_by, stop_date) VALUES(1, 2, NULL, NULL, '1245', NULL, '2020-06-26 15:50:21', 2, 1, '9999-01-01');
INSERT INTO kcson.ufio_has_category (ufio_id, category_id, get_date, archive, prim, `create`, ts, cr_by, upd_by, stop_date) VALUES(1, 3, '2018-01-01', 0, NULL, '2020-08-05 15:12:31', '2020-08-05 15:12:31', 1, 1, '9999-01-01');
INSERT INTO kcson.ufio_has_category (ufio_id, category_id, get_date, archive, prim, `create`, ts, cr_by, upd_by, stop_date) VALUES(1, 14, NULL, NULL, '1444', NULL, '2020-08-07 18:41:13', 2, 1, '9999-01-01');
INSERT INTO kcson.ufio_has_category (ufio_id, category_id, get_date, archive, prim, `create`, ts, cr_by, upd_by, stop_date) VALUES(2, 1, NULL, NULL, '22222', NULL, '2020-06-26 15:44:32', 2, 1, '9999-01-01');
INSERT INTO kcson.ufio_has_category (ufio_id, category_id, get_date, archive, prim, `create`, ts, cr_by, upd_by, stop_date) VALUES(2, 6, NULL, NULL, '33311', NULL, '2020-06-26 15:44:41', 2, 1, '9999-01-01');
INSERT INTO kcson.ufio_has_category (ufio_id, category_id, get_date, archive, prim, `create`, ts, cr_by, upd_by, stop_date) VALUES(2, 7, '2018-01-01', 0, NULL, '2020-08-05 15:11:00', '2020-08-05 15:11:00', 1, 1, '9999-01-01');
INSERT INTO kcson.ufio_has_category (ufio_id, category_id, get_date, archive, prim, `create`, ts, cr_by, upd_by, stop_date) VALUES(2, 10, '2018-01-01', 0, NULL, '2020-08-07 18:42:42', '2020-08-07 18:42:42', 1, 1, '9999-01-01');



INSERT INTO kcson.dep (id, dep, dep_full_name, dep_puname, note, archive, complex_dep_id) VALUES(1, 'Не указано1', 'Не указано отделение', NULL, NULL, NULL, 0);
INSERT INTO kcson.dep (id, dep, dep_full_name, dep_puname, note, archive, complex_dep_id) VALUES(2, 'Не указано2', 'Не указано отделение2', NULL, NULL, NULL, 0);
INSERT INTO kcson.dep (id, dep, dep_full_name, dep_puname, note, archive, complex_dep_id) VALUES(3, 'Все отделения организации', NULL, NULL, NULL, NULL, 1);
INSERT INTO kcson.dep (id, dep, dep_full_name, dep_puname, note, archive, complex_dep_id) VALUES(4, 'СОСМОДЫ', NULL, NULL, NULL, NULL, 2);
INSERT INTO kcson.dep (id, dep, dep_full_name, dep_puname, note, archive, complex_dep_id) VALUES(5, 'Полустационарные отделения', NULL, NULL, NULL, NULL, 3);
INSERT INTO kcson.dep (id, dep, dep_full_name, dep_puname, note, archive, complex_dep_id) VALUES(6, 'Стационарные отделения', NULL, NULL, NULL, NULL, 4);
INSERT INTO kcson.dep (id, dep, dep_full_name, dep_puname, note, archive, complex_dep_id) VALUES(7, 'Отделения на дому', NULL, NULL, NULL, NULL, 5);
INSERT INTO kcson.dep (id, dep, dep_full_name, dep_puname, note, archive, complex_dep_id) VALUES(8, 'Срочные отделения', NULL, NULL, NULL, NULL, 6);
INSERT INTO kcson.dep (id, dep, dep_full_name, dep_puname, note, archive, complex_dep_id) VALUES(9, 'Аппарат', 'Аппарат', 'Аппарат', NULL, 1, 0);


INSERT INTO kcson.dep_has_worker (id, dep_has_worker, worker_id, dep_id, job_id, prim, archive, `from`, till, role_id, api_key) VALUES(1, 'тестовый работник', 1, 1, 1, NULL, 0, '2000-01-01', '2050-01-01', 6, '123');
INSERT INTO kcson.dep_has_worker (id, dep_has_worker, worker_id, dep_id, job_id, prim, archive, `from`, till, role_id, api_key) VALUES(2, 'тестовый работник2', 1, 2, 1, NULL, 0, '2000-01-01', '2050-01-01', 7, '7.362514797935743e174ac3be74-4b21-11ec-b2a6-04d9f5c97b0c');


INSERT INTO kcson.dep_has_ripso (dep_id, ripso_id) VALUES(1, 1);
INSERT INTO kcson.dep_has_ripso (dep_id, ripso_id) VALUES(1, 13);
INSERT INTO kcson.dep_has_ripso (dep_id, ripso_id) VALUES(1, 14);
INSERT INTO kcson.dep_has_ripso (dep_id, ripso_id) VALUES(1, 18);
INSERT INTO kcson.dep_has_ripso (dep_id, ripso_id) VALUES(1, 22);
INSERT INTO kcson.dep_has_ripso (dep_id, ripso_id) VALUES(2, 2);
INSERT INTO kcson.dep_has_ripso (dep_id, ripso_id) VALUES(2, 1);






INSERT INTO kcson.contracts (id, contracts, contracts2, ufio_id, dep_id, ripso_id, blocked, startdate, enddate, ippsuNum, note, `create`, ts, cr_by, upd_by, to_recheck, check_date, pyc_prim) VALUES(1, '12312313/2001', NULL, 1, 1, 1, 0, '2001-01-01', '2020-12-31', NULL, NULL, NULL, '2020-01-21 18:45:29', NULL, 2, 0, NULL, NULL);
INSERT INTO kcson.contracts (id, contracts, contracts2, ufio_id, dep_id, ripso_id, blocked, startdate, enddate, ippsuNum, note, `create`, ts, cr_by, upd_by, to_recheck, check_date, pyc_prim) VALUES(2, '123441/2020', '0', 1, 1, 1, 0, '2020-01-21', '2020-01-21', NULL, 'test note1', '2020-01-21 19:22:28', '2021-12-15 16:08:49', 2, 2, 0, NULL, NULL);
INSERT INTO kcson.contracts (id, contracts, contracts2, ufio_id, dep_id, ripso_id, blocked, startdate, enddate, ippsuNum, note, `create`, ts, cr_by, upd_by, to_recheck, check_date, pyc_prim) VALUES(3, '43434/2001', NULL, 2, 1, 1, 0, '2011-01-01', '2019-12-31', NULL, '', NULL, '2020-02-07 16:18:31', NULL, 1, 1, NULL, NULL);
INSERT INTO kcson.contracts (id, contracts, contracts2, ufio_id, dep_id, ripso_id, blocked, startdate, enddate, ippsuNum, note, `create`, ts, cr_by, upd_by, to_recheck, check_date, pyc_prim) VALUES(4, '11111111111111/2020', NULL, 2, 1, 13, 1, '2017-01-17', '2020-01-17', 0, '', '2020-01-17 12:09:57', '2021-12-15 16:08:20', 1, 2, 0, NULL, NULL);
INSERT INTO kcson.contracts (id, contracts, contracts2, ufio_id, dep_id, ripso_id, blocked, startdate, enddate, ippsuNum, note, `create`, ts, cr_by, upd_by, to_recheck, check_date, pyc_prim) VALUES(5, '4546546/2020', NULL, 2, 1, 1, 1, '2020-01-17', '2020-01-17', 1231231, '', '2020-01-17 12:24:40', '2020-01-21 18:45:29', 1, 2, 0, NULL, NULL);
INSERT INTO kcson.contracts (id, contracts, contracts2, ufio_id, dep_id, ripso_id, blocked, startdate, enddate, ippsuNum, note, `create`, ts, cr_by, upd_by, to_recheck, check_date, pyc_prim) VALUES(6, '1212/2017', '', 2, 1, 13, 2, '2017-01-17', '2018-04-20', 0, '', '2020-01-20 16:26:39', '2020-03-03 11:19:55', 1, 1, 2, NULL, '');
INSERT INTO kcson.contracts (id, contracts, contracts2, ufio_id, dep_id, ripso_id, blocked, startdate, enddate, ippsuNum, note, `create`, ts, cr_by, upd_by, to_recheck, check_date, pyc_prim) VALUES(7, '9999/2020', '', 2, 1, 14, 0, '2020-01-20', '2021-01-20', 0, 'test note2', '2020-01-20 19:32:59', '2021-12-15 16:08:49', 1, 2, 0, NULL, '');
INSERT INTO kcson.contracts (id, contracts, contracts2, ufio_id, dep_id, ripso_id, blocked, startdate, enddate, ippsuNum, note, `create`, ts, cr_by, upd_by, to_recheck, check_date, pyc_prim) VALUES(8, '1111/2019', '', 2, 1, 13, 0, '2018-01-17', '2020-01-21', 0, '', '2020-01-21 08:24:48', '2020-07-24 11:58:36', 1, 1, 0, NULL, '');
INSERT INTO kcson.contracts (id, contracts, contracts2, ufio_id, dep_id, ripso_id, blocked, startdate, enddate, ippsuNum, note, `create`, ts, cr_by, upd_by, to_recheck, check_date, pyc_prim) VALUES(9, '11110/2020', '11110', 2, 1, 1, 2, '2006-01-17', '2020-01-17', 0, NULL, '2020-01-21 08:46:15', '2020-06-18 16:21:12', 1, 1, 0, NULL, NULL);
INSERT INTO kcson.contracts (id, contracts, contracts2, ufio_id, dep_id, ripso_id, blocked, startdate, enddate, ippsuNum, note, `create`, ts, cr_by, upd_by, to_recheck, check_date, pyc_prim) VALUES(10, '13213213/2021', '', 2, 1, 2, 0, '1999-01-01', '1999-12-01', 0, '', '2020-01-21 09:07:18', '2021-12-15 16:09:27', 1, 2, 0, NULL, '');


INSERT INTO kcson.complex_dep (id, complex_dep, note) VALUES(1, 'Все отделения организации', NULL);
INSERT INTO kcson.complex_dep (id, complex_dep, note) VALUES(2, 'СОСМОДЫ', NULL);
INSERT INTO kcson.complex_dep (id, complex_dep, note) VALUES(3, 'Полустационарные отделения', NULL);
INSERT INTO kcson.complex_dep (id, complex_dep, note) VALUES(4, 'Стационарные отделения', NULL);
INSERT INTO kcson.complex_dep (id, complex_dep, note) VALUES(5, 'Отделения на дому', NULL);
INSERT INTO kcson.complex_dep (id, complex_dep, note) VALUES(6, 'Срочные отделения', NULL);



--INSERT INTO kcson.complex_dep_has_dep (complex_dep_id, dep_id) VALUES(1, 1);
--INSERT INTO kcson.complex_dep_has_dep (complex_dep_id, dep_id) VALUES(1, 2);
--INSERT INTO kcson.complex_dep_has_dep (complex_dep_id, dep_id) VALUES(1, 3);
--INSERT INTO kcson.complex_dep_has_dep (complex_dep_id, dep_id) VALUES(1, 4);
--INSERT INTO kcson.complex_dep_has_dep (complex_dep_id, dep_id) VALUES(1, 5);
--INSERT INTO kcson.complex_dep_has_dep (complex_dep_id, dep_id) VALUES(1, 6);
--INSERT INTO kcson.complex_dep_has_dep (complex_dep_id, dep_id) VALUES(1, 7);
--INSERT INTO kcson.complex_dep_has_dep (complex_dep_id, dep_id) VALUES(1, 8);
--INSERT INTO kcson.complex_dep_has_dep (complex_dep_id, dep_id) VALUES(1, 9);
--INSERT INTO kcson.complex_dep_has_dep (complex_dep_id, dep_id) VALUES(1, 10);



INSERT INTO kcson.add_info (pddate, contracts_id, predv_money, curFIO, psp, address, sdd, sdd_date, perc, not_standart_contract, not_standart_act, prim, `create`, ts, cr_by, upd_by, repr_FIO, repr_addr, repr_psp, work_livemin) VALUES('2020-01-01', 1, 0.00, 'Тестовый человек', '6', '1', 22000.00, '2020-01-01', 20.0, 0, 0, '', '2020-04-27 15:29:54', '2020-09-14 00:11:26', 1, 1, '', '', '', 0);
INSERT INTO kcson.add_info (pddate, contracts_id, predv_money, curFIO, psp, address, sdd, sdd_date, perc, not_standart_contract, not_standart_act, prim, `create`, ts, cr_by, upd_by, repr_FIO, repr_addr, repr_psp, work_livemin) VALUES('2020-07-01', 1, NULL, 'Тестовый человек', '6', '1', 18000.00, '2020-07-01', 15.0, NULL, NULL, NULL, '2020-07-21 18:56:07', '2020-09-14 00:11:25', 1, 1, NULL, NULL, NULL, 0);
INSERT INTO kcson.add_info (pddate, contracts_id, predv_money, curFIO, psp, address, sdd, sdd_date, perc, not_standart_contract, not_standart_act, prim, `create`, ts, cr_by, upd_by, repr_FIO, repr_addr, repr_psp, work_livemin) VALUES('2020-03-01', 1, 5284.43, '1212', '6', '1', 24000.00, '2002-01-01', 0.2, NULL, NULL, NULL, NULL, '2020-09-14 00:35:02', 2, 1, NULL, NULL, NULL, 0);
INSERT INTO kcson.add_info (pddate, contracts_id, predv_money, curFIO, psp, address, sdd, sdd_date, perc, not_standart_contract, not_standart_act, prim, `create`, ts, cr_by, upd_by, repr_FIO, repr_addr, repr_psp, work_livemin) VALUES('2020-01-01', 2, 0.00, 'Тестовый чел2', '1', '1', 0.00, '2020-01-01', 0.1, 0, 0, '', '2020-01-21 15:06:23', '2020-01-21 15:06:23', 1, 1, '', '', '', 0);
INSERT INTO kcson.add_info (pddate, contracts_id, predv_money, curFIO, psp, address, sdd, sdd_date, perc, not_standart_contract, not_standart_act, prim, `create`, ts, cr_by, upd_by, repr_FIO, repr_addr, repr_psp, work_livemin) VALUES('2001-02-01', 2, 0.00, NULL, '5555', '111', 13000.00, NULL, 0.2, NULL, NULL, NULL, NULL, '2020-09-14 10:22:21', 2, 1, NULL, NULL, NULL, 0);
INSERT INTO kcson.add_info (pddate, contracts_id, predv_money, curFIO, psp, address, sdd, sdd_date, perc, not_standart_contract, not_standart_act, prim, `create`, ts, cr_by, upd_by, repr_FIO, repr_addr, repr_psp, work_livemin) VALUES('2001-06-01', 2, 0.00, 'Тестовый человек2', '43434', '2', 17000.00, NULL, 0.1, NULL, NULL, NULL, NULL, '2020-09-14 10:22:21', 2, 1, NULL, NULL, NULL, 0);




INSERT INTO kcson.dhw_has_ufio (dhw_id, ufio_id, prim) VALUES(1, 1, NULL);
INSERT INTO kcson.dhw_has_ufio (dhw_id, ufio_id, prim) VALUES(1, 2, NULL);
