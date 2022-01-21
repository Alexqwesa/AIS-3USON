USE `kcson`;


INSERT INTO `kcson`.`dep` (`id`, `dep`, `dep_full_name`, `note`) VALUES (DEFAULT, 'Не указано', 'Не указано', NULL);


INSERT INTO kcson.worker (id, worker, `user`, prim, role_id, dep_id, archive) VALUES(1, 'Не указан(Работник)', 'newuser', NULL, 1, 1, 0);
INSERT INTO kcson.worker (id, worker, `user`, prim, role_id, dep_id, archive) VALUES(2, 'Не указан(Админ)', 'root', NULL, 1, 1, 0);


INSERT INTO kcson.client (id, client, client_short, clientDeath, clientbirth, ESRN, prim, phone, snils, curator, `create`, ts, cr_by, upd_by, cr_dep_id) VALUES(1, 'Тестовый человек', 'Тx ', '1900-01-01', '1976-01-01', 123461111, '1323', NULL, NULL, NULL, NULL, '2020-06-26 15:26:39', NULL, 1, 0);
INSERT INTO kcson.client (id, client, client_short, clientDeath, clientbirth, ESRN, prim, phone, snils, curator, `create`, ts, cr_by, upd_by, cr_dep_id) VALUES(2, 'Тестовый чел2', NULL, NULL, '1987-01-01', 543, NULL, NULL, NULL, NULL, NULL, '2020-01-21 15:04:59', NULL, 1, 0);


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


INSERT INTO kcson.client_has_category (client_id, category_id, get_date, archive, prim, `create`, ts, cr_by, upd_by, stop_date) VALUES(1, 1, NULL, NULL, '4113', NULL, NULL, 2, 2, '9999-01-01');
INSERT INTO kcson.client_has_category (client_id, category_id, get_date, archive, prim, `create`, ts, cr_by, upd_by, stop_date) VALUES(1, 2, NULL, NULL, '1245', NULL, '2020-06-26 15:50:21', 2, 1, '9999-01-01');
INSERT INTO kcson.client_has_category (client_id, category_id, get_date, archive, prim, `create`, ts, cr_by, upd_by, stop_date) VALUES(1, 3, '2018-01-01', 0, NULL, '2020-08-05 15:12:31', '2020-08-05 15:12:31', 1, 1, '9999-01-01');
INSERT INTO kcson.client_has_category (client_id, category_id, get_date, archive, prim, `create`, ts, cr_by, upd_by, stop_date) VALUES(1, 14, NULL, NULL, '1444', NULL, '2020-08-07 18:41:13', 2, 1, '9999-01-01');
INSERT INTO kcson.client_has_category (client_id, category_id, get_date, archive, prim, `create`, ts, cr_by, upd_by, stop_date) VALUES(2, 1, NULL, NULL, '22222', NULL, '2020-06-26 15:44:32', 2, 1, '9999-01-01');
INSERT INTO kcson.client_has_category (client_id, category_id, get_date, archive, prim, `create`, ts, cr_by, upd_by, stop_date) VALUES(2, 6, NULL, NULL, '33311', NULL, '2020-06-26 15:44:41', 2, 1, '9999-01-01');
INSERT INTO kcson.client_has_category (client_id, category_id, get_date, archive, prim, `create`, ts, cr_by, upd_by, stop_date) VALUES(2, 7, '2018-01-01', 0, NULL, '2020-08-05 15:11:00', '2020-08-05 15:11:00', 1, 1, '9999-01-01');
INSERT INTO kcson.client_has_category (client_id, category_id, get_date, archive, prim, `create`, ts, cr_by, upd_by, stop_date) VALUES(2, 10, '2018-01-01', 0, NULL, '2020-08-07 18:42:42', '2020-08-07 18:42:42', 1, 1, '9999-01-01');


INSERT INTO kcson.dep (id, dep, dep_full_name, dep_puname, note, archive, complex_dep_id) VALUES(0, 'Не указано', 'Не указано', NULL, NULL, 0, 0);
INSERT INTO kcson.dep (id, dep, dep_full_name, dep_puname, note, archive, complex_dep_id) VALUES(1, 'Не указано1', 'Не указано отделение', NULL, NULL, 0, 0);
INSERT INTO kcson.dep (id, dep, dep_full_name, dep_puname, note, archive, complex_dep_id) VALUES(2, 'Не указано2', 'Не указано отделение2', NULL, NULL, 0, 0);
INSERT INTO kcson.dep (id, dep, dep_full_name, dep_puname, note, archive, complex_dep_id) VALUES(3, 'Все отделения организации', 'Все отделения организации', NULL, NULL, 0, 1);
INSERT INTO kcson.dep (id, dep, dep_full_name, dep_puname, note, archive, complex_dep_id) VALUES(4, 'СОСМОДЫ', 'СОСМОДЫ', NULL, NULL, 0, 2);
INSERT INTO kcson.dep (id, dep, dep_full_name, dep_puname, note, archive, complex_dep_id) VALUES(5, 'Полустационарные отделения', 'Полустационарные отделения', NULL, NULL, 0, 3);
INSERT INTO kcson.dep (id, dep, dep_full_name, dep_puname, note, archive, complex_dep_id) VALUES(6, 'Стационарные отделения', 'Стационарные отделения', NULL, NULL, 0, 4);
INSERT INTO kcson.dep (id, dep, dep_full_name, dep_puname, note, archive, complex_dep_id) VALUES(7, 'Отделения на дому', 'Отделения на дому', NULL, NULL, 0, 5);
INSERT INTO kcson.dep (id, dep, dep_full_name, dep_puname, note, archive, complex_dep_id) VALUES(8, 'Срочные отделения', 'Срочные отделения', NULL, NULL, 0, 6);
INSERT INTO kcson.dep (id, dep, dep_full_name, dep_puname, note, archive, complex_dep_id) VALUES(9, 'Аппарат', 'Аппарат', 'Аппарат', NULL, 1, 0);


INSERT INTO kcson.dep_has_worker (id, dep_has_worker, worker_id, dep_id, job_id, prim, archive, `from`, till, role_id, api_key) VALUES(1, 'тестовый работник', 1, 1, 1, NULL, 0, '2000-01-01', '2050-01-01', 6, '123');
INSERT INTO kcson.dep_has_worker (id, dep_has_worker, worker_id, dep_id, job_id, prim, archive, `from`, till, role_id, api_key) VALUES(2, 'тестовый работник2', 1, 2, 1, NULL, 0, '2000-01-01', '2050-01-01', 6, '7.362514797935743e174ac3be74-4b21-11ec-b2a6-04d9f5c97b0c');


INSERT INTO kcson.dep_has_ripso (dep_id, ripso_id) VALUES(1, 1);
INSERT INTO kcson.dep_has_ripso (dep_id, ripso_id) VALUES(1, 13);
INSERT INTO kcson.dep_has_ripso (dep_id, ripso_id) VALUES(1, 14);
INSERT INTO kcson.dep_has_ripso (dep_id, ripso_id) VALUES(1, 18);
INSERT INTO kcson.dep_has_ripso (dep_id, ripso_id) VALUES(1, 22);
INSERT INTO kcson.dep_has_ripso (dep_id, ripso_id) VALUES(2, 2);
INSERT INTO kcson.dep_has_ripso (dep_id, ripso_id) VALUES(2, 1);


INSERT INTO kcson.contracts (id, contracts, contracts2, client_id, dep_id, ripso_id, blocked, startdate, enddate, ippsuNum, note, `create`, ts, cr_by, upd_by, to_recheck, check_date, pyc_prim) VALUES(1, '661/2021/t/2001', NULL, 1, 1, 1, 0, '2001-01-01', '2030-12-31', NULL, NULL, NULL, '2022-01-14 10:18:02', 2, 2, 0, NULL, NULL);
INSERT INTO kcson.contracts (id, contracts, contracts2, client_id, dep_id, ripso_id, blocked, startdate, enddate, ippsuNum, note, `create`, ts, cr_by, upd_by, to_recheck, check_date, pyc_prim) VALUES(2, '1/2022/t/2020', '0', 1, 1, 1, 0, '2020-01-21', '2031-01-01', NULL, 'test note1', '2020-01-21 19:22:28', '2022-01-14 10:18:02', 2, 2, 0, NULL, NULL);
INSERT INTO kcson.contracts (id, contracts, contracts2, client_id, dep_id, ripso_id, blocked, startdate, enddate, ippsuNum, note, `create`, ts, cr_by, upd_by, to_recheck, check_date, pyc_prim) VALUES(3, '2/2022/t/2011', NULL, 2, 1, 1, 0, '2011-01-01', '2021-01-02', NULL, '', NULL, '2022-01-14 10:18:02', 2, 2, 1, NULL, NULL);
INSERT INTO kcson.contracts (id, contracts, contracts2, client_id, dep_id, ripso_id, blocked, startdate, enddate, ippsuNum, note, `create`, ts, cr_by, upd_by, to_recheck, check_date, pyc_prim) VALUES(4, '701/2021/t/2017', NULL, 2, 1, 13, 1, '2017-01-17', '2031-01-03', 0, '', '2020-01-17 12:09:57', '2022-01-14 10:18:02', 2, 2, 0, NULL, NULL);
INSERT INTO kcson.contracts (id, contracts, contracts2, client_id, dep_id, ripso_id, blocked, startdate, enddate, ippsuNum, note, `create`, ts, cr_by, upd_by, to_recheck, check_date, pyc_prim) VALUES(5, '702/2021/t/2020', NULL, 2, 1, 1, 1, '2020-01-17', '2031-01-04', 1231231, '', '2020-01-17 12:24:40', '2022-01-14 10:18:02', 2, 2, 0, NULL, NULL);
INSERT INTO kcson.contracts (id, contracts, contracts2, client_id, dep_id, ripso_id, blocked, startdate, enddate, ippsuNum, note, `create`, ts, cr_by, upd_by, to_recheck, check_date, pyc_prim) VALUES(6, '703/2021/t/2017', '', 2, 1, 13, 2, '2017-01-17', '2031-01-05', 0, '', '2020-01-20 16:26:39', '2022-01-14 10:18:02', 2, 2, 2, NULL, '');
INSERT INTO kcson.contracts (id, contracts, contracts2, client_id, dep_id, ripso_id, blocked, startdate, enddate, ippsuNum, note, `create`, ts, cr_by, upd_by, to_recheck, check_date, pyc_prim) VALUES(7, '704/2021/t/2020', '', 2, 1, 14, 0, '2020-01-20', '2031-01-06', 0, 'test note2', '2020-01-20 19:32:59', '2022-01-14 10:18:02', 2, 2, 0, NULL, '');
INSERT INTO kcson.contracts (id, contracts, contracts2, client_id, dep_id, ripso_id, blocked, startdate, enddate, ippsuNum, note, `create`, ts, cr_by, upd_by, to_recheck, check_date, pyc_prim) VALUES(8, '7/2022/t/2018', '', 2, 1, 13, 0, '2018-01-17', '2031-01-07', 0, '', '2020-01-21 08:24:48', '2022-01-14 10:18:02', 2, 2, 0, NULL, '');
INSERT INTO kcson.contracts (id, contracts, contracts2, client_id, dep_id, ripso_id, blocked, startdate, enddate, ippsuNum, note, `create`, ts, cr_by, upd_by, to_recheck, check_date, pyc_prim) VALUES(9, '8/2022/t/2006', '11110', 2, 1, 1, 2, '2006-01-17', '2020-01-08', 0, NULL, '2020-01-21 08:46:15', '2022-01-14 10:18:02', 2, 2, 0, NULL, NULL);
INSERT INTO kcson.contracts (id, contracts, contracts2, client_id, dep_id, ripso_id, blocked, startdate, enddate, ippsuNum, note, `create`, ts, cr_by, upd_by, to_recheck, check_date, pyc_prim) VALUES(10, '9/2022/t/1999', '', 2, 1, 2, 0, '1999-01-01', '2031-01-09', 0, '', '2020-01-21 09:07:18', '2022-01-14 10:18:02', 2, 2, 0, NULL, '');


INSERT INTO kcson.complex_dep (id, complex_dep, note) VALUES(1, 'Все отделения организации', NULL);
INSERT INTO kcson.complex_dep (id, complex_dep, note) VALUES(2, 'СОСМОДЫ', NULL);
INSERT INTO kcson.complex_dep (id, complex_dep, note) VALUES(3, 'Полустационарные отделения', NULL);
INSERT INTO kcson.complex_dep (id, complex_dep, note) VALUES(4, 'Стационарные отделения', NULL);
INSERT INTO kcson.complex_dep (id, complex_dep, note) VALUES(5, 'Отделения на дому', NULL);
INSERT INTO kcson.complex_dep (id, complex_dep, note) VALUES(6, 'Срочные отделения', NULL);


-- INSERT INTO kcson.complex_dep_has_dep (complex_dep_id, dep_id) VALUES(1, 1);
-- INSERT INTO kcson.complex_dep_has_dep (complex_dep_id, dep_id) VALUES(1, 2);
-- INSERT INTO kcson.complex_dep_has_dep (complex_dep_id, dep_id) VALUES(1, 3);
-- INSERT INTO kcson.complex_dep_has_dep (complex_dep_id, dep_id) VALUES(1, 4);
-- INSERT INTO kcson.complex_dep_has_dep (complex_dep_id, dep_id) VALUES(1, 5);
-- INSERT INTO kcson.complex_dep_has_dep (complex_dep_id, dep_id) VALUES(1, 6);
-- INSERT INTO kcson.complex_dep_has_dep (complex_dep_id, dep_id) VALUES(1, 7);
-- INSERT INTO kcson.complex_dep_has_dep (complex_dep_id, dep_id) VALUES(1, 8);
-- INSERT INTO kcson.complex_dep_has_dep (complex_dep_id, dep_id) VALUES(1, 9);
-- INSERT INTO kcson.complex_dep_has_dep (complex_dep_id, dep_id) VALUES(1, 10);


INSERT INTO kcson.add_info (pddate, contracts_id, predv_money, curFIO, psp, address, sdd, sdd_date, perc, not_standart_contract, not_standart_act, prim, `create`, ts, cr_by, upd_by, repr_FIO, repr_addr, repr_psp, work_livemin) VALUES('2022-02-01', 2, 0.00, NULL, '5555', '111', 13000.00, '2022-02-01', 0.2, NULL, NULL, NULL, NULL, '2022-01-14 10:47:54', 2, 2, NULL, NULL, NULL, 0);
INSERT INTO kcson.add_info (pddate, contracts_id, predv_money, curFIO, psp, address, sdd, sdd_date, perc, not_standart_contract, not_standart_act, prim, `create`, ts, cr_by, upd_by, repr_FIO, repr_addr, repr_psp, work_livemin) VALUES('2022-06-01', 2, 0.00, 'Тестовый человек2', '43434', '2', 17000.00, '2022-06-01', 0.1, NULL, NULL, NULL, NULL, '2022-01-14 10:47:54', 2, 2, NULL, NULL, NULL, 0);
INSERT INTO kcson.add_info (pddate, contracts_id, predv_money, curFIO, psp, address, sdd, sdd_date, perc, not_standart_contract, not_standart_act, prim, `create`, ts, cr_by, upd_by, repr_FIO, repr_addr, repr_psp, work_livemin) VALUES('2022-01-01', 1, 0.00, 'Тестовый человек', '6', '1', 22000.00, '2022-01-01', 20.0, 0, 0, '', '2020-04-27 15:29:54', '2022-01-14 10:47:54', 2, 2, '', '', '', 0);
INSERT INTO kcson.add_info (pddate, contracts_id, predv_money, curFIO, psp, address, sdd, sdd_date, perc, not_standart_contract, not_standart_act, prim, `create`, ts, cr_by, upd_by, repr_FIO, repr_addr, repr_psp, work_livemin) VALUES('2022-01-01', 2, 0.00, 'Тестовый чел2', '1', '1', 0.00, '2022-01-01', 0.1, 0, 0, '', '2020-01-21 15:06:23', '2022-01-14 10:47:54', 2, 2, '', '', '', 0);
INSERT INTO kcson.add_info (pddate, contracts_id, predv_money, curFIO, psp, address, sdd, sdd_date, perc, not_standart_contract, not_standart_act, prim, `create`, ts, cr_by, upd_by, repr_FIO, repr_addr, repr_psp, work_livemin) VALUES('2022-03-01', 1, 5284.43, 'Тестовый чел2', '6', '1', 24000.00, '2022-03-01', 0.2, NULL, NULL, NULL, NULL, '2022-01-14 10:47:54', 2, 2, NULL, NULL, NULL, 0);
INSERT INTO kcson.add_info (pddate, contracts_id, predv_money, curFIO, psp, address, sdd, sdd_date, perc, not_standart_contract, not_standart_act, prim, `create`, ts, cr_by, upd_by, repr_FIO, repr_addr, repr_psp, work_livemin) VALUES('2022-07-01', 1, NULL, 'Тестовый человек', '6', '1', 18000.00, '2022-07-01', 15.0, NULL, NULL, NULL, '2020-07-21 18:56:07', '2022-01-14 10:47:54', 2, 2, NULL, NULL, NULL, 0);


INSERT INTO kcson.dhw_has_client (dhw_id, client_id, prim) VALUES(1, 1, NULL);
INSERT INTO kcson.dhw_has_client (dhw_id, client_id, prim) VALUES(1, 2, NULL);
