-- MySQL dump 10.13  Distrib 8.0.27, for Linux (x86_64)
--
-- Host: 127.0.0.1    Database: kcson
-- ------------------------------------------------------
-- Server version	8.0.20

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!50503 SET NAMES utf8mb4 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Temporary view structure for view `_active_dep`
--

DROP TABLE IF EXISTS `_active_dep`;
/*!50001 DROP VIEW IF EXISTS `_active_dep`*/;
SET @saved_cs_client     = @@character_set_client;
/*!50503 SET character_set_client = utf8mb4 */;
/*!50001 CREATE VIEW `_active_dep` AS SELECT 
 1 AS `id`,
 1 AS `dep`,
 1 AS `dep_full_name`,
 1 AS `dep_puname`,
 1 AS `note`,
 1 AS `archive`,
 1 AS `complex_dep_id`*/;
SET character_set_client = @saved_cs_client;

--
-- Temporary view structure for view `_active_dep_static`
--

DROP TABLE IF EXISTS `_active_dep_static`;
/*!50001 DROP VIEW IF EXISTS `_active_dep_static`*/;
SET @saved_cs_client     = @@character_set_client;
/*!50503 SET character_set_client = utf8mb4 */;
/*!50001 CREATE VIEW `_active_dep_static` AS SELECT 
 1 AS `id`,
 1 AS `dep`,
 1 AS `dep_full_name`,
 1 AS `dep_puname`,
 1 AS `note`,
 1 AS `archive`,
 1 AS `complex_dep_id`*/;
SET character_set_client = @saved_cs_client;

--
-- Temporary view structure for view `_api_key_planned`
--

DROP TABLE IF EXISTS `_api_key_planned`;
/*!50001 DROP VIEW IF EXISTS `_api_key_planned`*/;
SET @saved_cs_client     = @@character_set_client;
/*!50503 SET character_set_client = utf8mb4 */;
/*!50001 CREATE VIEW `_api_key_planned` AS SELECT 
 1 AS `contract_id`,
 1 AS `serv_id`,
 1 AS `planned`,
 1 AS `filled`,
 1 AS `api_key`*/;
SET character_set_client = @saved_cs_client;

--
-- Temporary view structure for view `_api_key_services`
--

DROP TABLE IF EXISTS `_api_key_services`;
/*!50001 DROP VIEW IF EXISTS `_api_key_services`*/;
SET @saved_cs_client     = @@character_set_client;
/*!50503 SET character_set_client = utf8mb4 */;
/*!50001 CREATE VIEW `_api_key_services` AS SELECT 
 1 AS `id`,
 1 AS `serv`,
 1 AS `serv_text`,
 1 AS `tnum`,
 1 AS `price`,
 1 AS `total`,
 1 AS `sub_serv`,
 1 AS `serv_id_list`,
 1 AS `image`,
 1 AS `expr`,
 1 AS `short_text`*/;
SET character_set_client = @saved_cs_client;

--
-- Temporary view structure for view `_apikey_has_contracts`
--

DROP TABLE IF EXISTS `_apikey_has_contracts`;
/*!50001 DROP VIEW IF EXISTS `_apikey_has_contracts`*/;
SET @saved_cs_client     = @@character_set_client;
/*!50503 SET character_set_client = utf8mb4 */;
/*!50001 CREATE VIEW `_apikey_has_contracts` AS SELECT 
 1 AS `api_key`,
 1 AS `contract_id`,
 1 AS `dep_id`,
 1 AS `client_id`,
 1 AS `contract`,
 1 AS `client`,
 1 AS `dhw_id`*/;
SET character_set_client = @saved_cs_client;

--
-- Temporary view structure for view `_bm_dep_has_client`
--

DROP TABLE IF EXISTS `_bm_dep_has_client`;
/*!50001 DROP VIEW IF EXISTS `_bm_dep_has_client`*/;
SET @saved_cs_client     = @@character_set_client;
/*!50503 SET character_set_client = utf8mb4 */;
/*!50001 CREATE VIEW `_bm_dep_has_client` AS SELECT 
 1 AS `id`,
 1 AS `client`,
 1 AS `client_short`,
 1 AS `clientDeath`,
 1 AS `clientbirth`,
 1 AS `ESRN`,
 1 AS `note`,
 1 AS `phone`,
 1 AS `snils`,
 1 AS `curator`,
 1 AS `create`,
 1 AS `ts`,
 1 AS `cr_by`,
 1 AS `upd_by`,
 1 AS `cr_dep_id`*/;
SET character_set_client = @saved_cs_client;

--
-- Temporary view structure for view `_bm_dep_has_client_other_year`
--

DROP TABLE IF EXISTS `_bm_dep_has_client_other_year`;
/*!50001 DROP VIEW IF EXISTS `_bm_dep_has_client_other_year`*/;
SET @saved_cs_client     = @@character_set_client;
/*!50503 SET character_set_client = utf8mb4 */;
/*!50001 CREATE VIEW `_bm_dep_has_client_other_year` AS SELECT 
 1 AS `id`,
 1 AS `client`,
 1 AS `client_short`,
 1 AS `clientDeath`,
 1 AS `clientbirth`,
 1 AS `ESRN`,
 1 AS `note`,
 1 AS `phone`,
 1 AS `snils`,
 1 AS `curator`,
 1 AS `create`,
 1 AS `ts`,
 1 AS `cr_by`,
 1 AS `upd_by`,
 1 AS `cr_dep_id`*/;
SET character_set_client = @saved_cs_client;

--
-- Temporary view structure for view `_bm_dep_has_client_year`
--

DROP TABLE IF EXISTS `_bm_dep_has_client_year`;
/*!50001 DROP VIEW IF EXISTS `_bm_dep_has_client_year`*/;
SET @saved_cs_client     = @@character_set_client;
/*!50503 SET character_set_client = utf8mb4 */;
/*!50001 CREATE VIEW `_bm_dep_has_client_year` AS SELECT 
 1 AS `id`,
 1 AS `client`,
 1 AS `client_short`,
 1 AS `clientDeath`,
 1 AS `clientbirth`,
 1 AS `ESRN`,
 1 AS `note`,
 1 AS `phone`,
 1 AS `snils`,
 1 AS `curator`,
 1 AS `create`,
 1 AS `ts`,
 1 AS `cr_by`,
 1 AS `upd_by`,
 1 AS `cr_dep_id`*/;
SET character_set_client = @saved_cs_client;

--
-- Temporary view structure for view `_categ_list_client`
--

DROP TABLE IF EXISTS `_categ_list_client`;
/*!50001 DROP VIEW IF EXISTS `_categ_list_client`*/;
SET @saved_cs_client     = @@character_set_client;
/*!50503 SET character_set_client = utf8mb4 */;
/*!50001 CREATE VIEW `_categ_list_client` AS SELECT 
 1 AS `category_id`,
 1 AS `client_id`,
 1 AS `quantity`,
 1 AS `vdate`,
 1 AS `serv`*/;
SET character_set_client = @saved_cs_client;

--
-- Temporary view structure for view `_client`
--

DROP TABLE IF EXISTS `_client`;
/*!50001 DROP VIEW IF EXISTS `_client`*/;
SET @saved_cs_client     = @@character_set_client;
/*!50503 SET character_set_client = utf8mb4 */;
/*!50001 CREATE VIEW `_client` AS SELECT 
 1 AS `id`,
 1 AS `client`,
 1 AS `client_short`,
 1 AS `clientDeath`,
 1 AS `clientbirth`,
 1 AS `ESRN`,
 1 AS `note`,
 1 AS `phone`,
 1 AS `snils`,
 1 AS `curator`,
 1 AS `create`,
 1 AS `ts`,
 1 AS `cr_by`,
 1 AS `upd_by`,
 1 AS `cr_dep_id`*/;
SET character_set_client = @saved_cs_client;

--
-- Temporary view structure for view `_client_has_add_info`
--

DROP TABLE IF EXISTS `_client_has_add_info`;
/*!50001 DROP VIEW IF EXISTS `_client_has_add_info`*/;
SET @saved_cs_client     = @@character_set_client;
/*!50503 SET character_set_client = utf8mb4 */;
/*!50001 CREATE VIEW `_client_has_add_info` AS SELECT 
 1 AS `client_id`,
 1 AS `pddate`,
 1 AS `contracts_id`,
 1 AS `predv_money`,
 1 AS `curFIO`,
 1 AS `psp`,
 1 AS `address`,
 1 AS `sdd`,
 1 AS `sdd_date`,
 1 AS `perc`,
 1 AS `not_standart_contract`,
 1 AS `not_standart_act`,
 1 AS `note`,
 1 AS `create`,
 1 AS `ts`,
 1 AS `cr_by`,
 1 AS `upd_by`,
 1 AS `repr_FIO`,
 1 AS `repr_addr`,
 1 AS `repr_psp`,
 1 AS `work_livemin`*/;
SET character_set_client = @saved_cs_client;

--
-- Temporary view structure for view `_client_has_category_for_last_client`
--

DROP TABLE IF EXISTS `_client_has_category_for_last_client`;
/*!50001 DROP VIEW IF EXISTS `_client_has_category_for_last_client`*/;
SET @saved_cs_client     = @@character_set_client;
/*!50503 SET character_set_client = utf8mb4 */;
/*!50001 CREATE VIEW `_client_has_category_for_last_client` AS SELECT 
 1 AS `client_id`,
 1 AS `category_id`,
 1 AS `get_date`,
 1 AS `archive`,
 1 AS `note`,
 1 AS `create`,
 1 AS `ts`,
 1 AS `cr_by`,
 1 AS `upd_by`*/;
SET character_set_client = @saved_cs_client;

--
-- Temporary view structure for view `_client_has_contracts`
--

DROP TABLE IF EXISTS `_client_has_contracts`;
/*!50001 DROP VIEW IF EXISTS `_client_has_contracts`*/;
SET @saved_cs_client     = @@character_set_client;
/*!50503 SET character_set_client = utf8mb4 */;
/*!50001 CREATE VIEW `_client_has_contracts` AS SELECT 
 1 AS `id`,
 1 AS `contracts`,
 1 AS `contracts2`,
 1 AS `client_id`,
 1 AS `dep_id`,
 1 AS `ripso_id`,
 1 AS `blocked`,
 1 AS `startdate`,
 1 AS `enddate`,
 1 AS `ippsuNum`,
 1 AS `note`,
 1 AS `create`,
 1 AS `ts`,
 1 AS `cr_by`,
 1 AS `upd_by`,
 1 AS `to_recheck`,
 1 AS `check_date`,
 1 AS `pyc_prim`*/;
SET character_set_client = @saved_cs_client;

--
-- Temporary view structure for view `_client_has_invalid_contracts`
--

DROP TABLE IF EXISTS `_client_has_invalid_contracts`;
/*!50001 DROP VIEW IF EXISTS `_client_has_invalid_contracts`*/;
SET @saved_cs_client     = @@character_set_client;
/*!50503 SET character_set_client = utf8mb4 */;
/*!50001 CREATE VIEW `_client_has_invalid_contracts` AS SELECT 
 1 AS `client`,
 1 AS `id`,
 1 AS `contracts`,
 1 AS `client_id`,
 1 AS `dep_id`,
 1 AS `ripso_id`,
 1 AS `blocked`,
 1 AS `startdate`,
 1 AS `enddate`,
 1 AS `ippsuNum`,
 1 AS `note`,
 1 AS `create`,
 1 AS `ts`,
 1 AS `cr_by`,
 1 AS `upd_by`,
 1 AS `to_recheck`,
 1 AS `check_date`*/;
SET character_set_client = @saved_cs_client;

--
-- Temporary view structure for view `_client_has_main`
--

DROP TABLE IF EXISTS `_client_has_main`;
/*!50001 DROP VIEW IF EXISTS `_client_has_main`*/;
SET @saved_cs_client     = @@character_set_client;
/*!50503 SET character_set_client = utf8mb4 */;
/*!50001 CREATE VIEW `_client_has_main` AS SELECT 
 1 AS `id`,
 1 AS `contracts_id`,
 1 AS `dep_id`,
 1 AS `client_id`,
 1 AS `serv_id`,
 1 AS `dep_has_worker_id`,
 1 AS `worker_id`,
 1 AS `vdate`,
 1 AS `quantity`,
 1 AS `note`,
 1 AS `create`,
 1 AS `ts`,
 1 AS `cr_by`,
 1 AS `upd_by`,
 1 AS `reported`,
 1 AS `wdate`,
 1 AS `overdid`,
 1 AS `prev_quantity`*/;
SET character_set_client = @saved_cs_client;

--
-- Temporary view structure for view `_client_has_valid_contracts`
--

DROP TABLE IF EXISTS `_client_has_valid_contracts`;
/*!50001 DROP VIEW IF EXISTS `_client_has_valid_contracts`*/;
SET @saved_cs_client     = @@character_set_client;
/*!50503 SET character_set_client = utf8mb4 */;
/*!50001 CREATE VIEW `_client_has_valid_contracts` AS SELECT 
 1 AS `client`,
 1 AS `id`,
 1 AS `contracts`,
 1 AS `client_id`,
 1 AS `dep_id`,
 1 AS `ripso_id`,
 1 AS `blocked`,
 1 AS `startdate`,
 1 AS `enddate`,
 1 AS `ippsuNum`,
 1 AS `note`,
 1 AS `create`,
 1 AS `ts`,
 1 AS `cr_by`,
 1 AS `upd_by`,
 1 AS `to_recheck`,
 1 AS `check_date`*/;
SET character_set_client = @saved_cs_client;

--
-- Temporary view structure for view `_contr_has_add_info`
--

DROP TABLE IF EXISTS `_contr_has_add_info`;
/*!50001 DROP VIEW IF EXISTS `_contr_has_add_info`*/;
SET @saved_cs_client     = @@character_set_client;
/*!50503 SET character_set_client = utf8mb4 */;
/*!50001 CREATE VIEW `_contr_has_add_info` AS SELECT 
 1 AS `pddate`,
 1 AS `contracts_id`,
 1 AS `predv_money`,
 1 AS `curFIO`,
 1 AS `psp`,
 1 AS `address`,
 1 AS `sdd`,
 1 AS `sdd_date`,
 1 AS `perc`,
 1 AS `not_standart_contract`,
 1 AS `not_standart_act`,
 1 AS `note`,
 1 AS `create`,
 1 AS `ts`,
 1 AS `cr_by`,
 1 AS `upd_by`,
 1 AS `repr_FIO`,
 1 AS `repr_addr`,
 1 AS `repr_psp`,
 1 AS `work_livemin`*/;
SET character_set_client = @saved_cs_client;

--
-- Temporary view structure for view `_contr_has_main`
--

DROP TABLE IF EXISTS `_contr_has_main`;
/*!50001 DROP VIEW IF EXISTS `_contr_has_main`*/;
SET @saved_cs_client     = @@character_set_client;
/*!50503 SET character_set_client = utf8mb4 */;
/*!50001 CREATE VIEW `_contr_has_main` AS SELECT 
 1 AS `id`,
 1 AS `contracts_id`,
 1 AS `dep_id`,
 1 AS `client_id`,
 1 AS `serv_id`,
 1 AS `dep_has_worker_id`,
 1 AS `worker_id`,
 1 AS `vdate`,
 1 AS `quantity`,
 1 AS `note`,
 1 AS `create`,
 1 AS `ts`,
 1 AS `cr_by`,
 1 AS `upd_by`,
 1 AS `reported`,
 1 AS `wdate`,
 1 AS `overdid`,
 1 AS `prev_quantity`*/;
SET character_set_client = @saved_cs_client;

--
-- Temporary view structure for view `_contr_has_serv_predv`
--

DROP TABLE IF EXISTS `_contr_has_serv_predv`;
/*!50001 DROP VIEW IF EXISTS `_contr_has_serv_predv`*/;
SET @saved_cs_client     = @@character_set_client;
/*!50503 SET character_set_client = utf8mb4 */;
/*!50001 CREATE VIEW `_contr_has_serv_predv` AS SELECT 
 1 AS `contracts_id`,
 1 AS `full_price`,
 1 AS `tnum`,
 1 AS `serv`,
 1 AS `serv_text`,
 1 AS `quantity`,
 1 AS `price`,
 1 AS `to_pay`,
 1 AS `servform_id`,
 1 AS `serv_id`,
 1 AS `sub_serv`,
 1 AS `vdate`,
 1 AS `dep_id`,
 1 AS `perc`,
 1 AS `year`*/;
SET character_set_client = @saved_cs_client;

--
-- Temporary view structure for view `_contracts`
--

DROP TABLE IF EXISTS `_contracts`;
/*!50001 DROP VIEW IF EXISTS `_contracts`*/;
SET @saved_cs_client     = @@character_set_client;
/*!50503 SET character_set_client = utf8mb4 */;
/*!50001 CREATE VIEW `_contracts` AS SELECT 
 1 AS `id`,
 1 AS `contracts`,
 1 AS `client_id`,
 1 AS `dep_id`,
 1 AS `ripso_id`,
 1 AS `blocked`,
 1 AS `startdate`,
 1 AS `enddate`,
 1 AS `ippsuNum`,
 1 AS `note`,
 1 AS `create`,
 1 AS `ts`,
 1 AS `cr_by`,
 1 AS `upd_by`,
 1 AS `to_recheck`,
 1 AS `check_date`,
 1 AS `servform_id`*/;
SET character_set_client = @saved_cs_client;

--
-- Temporary view structure for view `_contracts_has_serv`
--

DROP TABLE IF EXISTS `_contracts_has_serv`;
/*!50001 DROP VIEW IF EXISTS `_contracts_has_serv`*/;
SET @saved_cs_client     = @@character_set_client;
/*!50503 SET character_set_client = utf8mb4 */;
/*!50001 CREATE VIEW `_contracts_has_serv` AS SELECT 
 1 AS `serv_id`,
 1 AS `contracts_id`,
 1 AS `planned`,
 1 AS `filled`,
 1 AS `note`,
 1 AS `archive`,
 1 AS `create`,
 1 AS `ts`,
 1 AS `cr_by`,
 1 AS `upd_by`,
 1 AS `to_recheck`,
 1 AS `check_date`,
 1 AS `filled_old`,
 1 AS `tnum`*/;
SET character_set_client = @saved_cs_client;

--
-- Temporary view structure for view `_dep_has_add_info`
--

DROP TABLE IF EXISTS `_dep_has_add_info`;
/*!50001 DROP VIEW IF EXISTS `_dep_has_add_info`*/;
SET @saved_cs_client     = @@character_set_client;
/*!50503 SET character_set_client = utf8mb4 */;
/*!50001 CREATE VIEW `_dep_has_add_info` AS SELECT 
 1 AS `pddate`,
 1 AS `contracts_id`,
 1 AS `predv_money`,
 1 AS `curFIO`,
 1 AS `psp`,
 1 AS `address`,
 1 AS `sdd`,
 1 AS `sdd_date`,
 1 AS `perc`,
 1 AS `not_standart_contract`,
 1 AS `not_standart_act`,
 1 AS `note`,
 1 AS `create`,
 1 AS `ts`,
 1 AS `cr_by`,
 1 AS `upd_by`,
 1 AS `repr_FIO`,
 1 AS `repr_addr`,
 1 AS `repr_psp`,
 1 AS `work_livemin`*/;
SET character_set_client = @saved_cs_client;

--
-- Temporary view structure for view `_dep_has_client`
--

DROP TABLE IF EXISTS `_dep_has_client`;
/*!50001 DROP VIEW IF EXISTS `_dep_has_client`*/;
SET @saved_cs_client     = @@character_set_client;
/*!50503 SET character_set_client = utf8mb4 */;
/*!50001 CREATE VIEW `_dep_has_client` AS SELECT 
 1 AS `id`,
 1 AS `client`,
 1 AS `client_short`,
 1 AS `clientDeath`,
 1 AS `clientbirth`,
 1 AS `ESRN`,
 1 AS `note`,
 1 AS `phone`,
 1 AS `snils`,
 1 AS `curator`,
 1 AS `create`,
 1 AS `ts`,
 1 AS `cr_by`,
 1 AS `upd_by`,
 1 AS `cr_dep_id`*/;
SET character_set_client = @saved_cs_client;

--
-- Temporary view structure for view `_dep_has_client_blocked_in_year`
--

DROP TABLE IF EXISTS `_dep_has_client_blocked_in_year`;
/*!50001 DROP VIEW IF EXISTS `_dep_has_client_blocked_in_year`*/;
SET @saved_cs_client     = @@character_set_client;
/*!50503 SET character_set_client = utf8mb4 */;
/*!50001 CREATE VIEW `_dep_has_client_blocked_in_year` AS SELECT 
 1 AS `id`,
 1 AS `client`,
 1 AS `client_short`,
 1 AS `clientDeath`,
 1 AS `clientbirth`,
 1 AS `ESRN`,
 1 AS `note`,
 1 AS `phone`,
 1 AS `snils`,
 1 AS `curator`,
 1 AS `create`,
 1 AS `ts`,
 1 AS `cr_by`,
 1 AS `upd_by`,
 1 AS `cr_dep_id`*/;
SET character_set_client = @saved_cs_client;

--
-- Temporary view structure for view `_dep_has_client_by_ripso`
--

DROP TABLE IF EXISTS `_dep_has_client_by_ripso`;
/*!50001 DROP VIEW IF EXISTS `_dep_has_client_by_ripso`*/;
SET @saved_cs_client     = @@character_set_client;
/*!50503 SET character_set_client = utf8mb4 */;
/*!50001 CREATE VIEW `_dep_has_client_by_ripso` AS SELECT 
 1 AS `id`,
 1 AS `client`,
 1 AS `client_short`,
 1 AS `clientDeath`,
 1 AS `clientbirth`,
 1 AS `ESRN`,
 1 AS `note`,
 1 AS `phone`,
 1 AS `snils`,
 1 AS `curator`,
 1 AS `create`,
 1 AS `ts`,
 1 AS `cr_by`,
 1 AS `upd_by`*/;
SET character_set_client = @saved_cs_client;

--
-- Temporary view structure for view `_dep_has_client_contracts`
--

DROP TABLE IF EXISTS `_dep_has_client_contracts`;
/*!50001 DROP VIEW IF EXISTS `_dep_has_client_contracts`*/;
SET @saved_cs_client     = @@character_set_client;
/*!50503 SET character_set_client = utf8mb4 */;
/*!50001 CREATE VIEW `_dep_has_client_contracts` AS SELECT 
 1 AS `id`,
 1 AS `client`,
 1 AS `client_short`,
 1 AS `clientDeath`,
 1 AS `clientbirth`,
 1 AS `ESRN`,
 1 AS `note`,
 1 AS `phone`,
 1 AS `snils`,
 1 AS `curator`,
 1 AS `create`,
 1 AS `ts`,
 1 AS `cr_by`,
 1 AS `upd_by`,
 1 AS `cr_dep_id`*/;
SET character_set_client = @saved_cs_client;

--
-- Temporary view structure for view `_dep_has_client_count_2month`
--

DROP TABLE IF EXISTS `_dep_has_client_count_2month`;
/*!50001 DROP VIEW IF EXISTS `_dep_has_client_count_2month`*/;
SET @saved_cs_client     = @@character_set_client;
/*!50503 SET character_set_client = utf8mb4 */;
/*!50001 CREATE VIEW `_dep_has_client_count_2month` AS SELECT 
 1 AS `quantity`,
 1 AS `id`,
 1 AS `client`,
 1 AS `client_short`,
 1 AS `clientDeath`,
 1 AS `clientbirth`,
 1 AS `ESRN`,
 1 AS `note`,
 1 AS `phone`,
 1 AS `snils`,
 1 AS `curator`,
 1 AS `create`,
 1 AS `ts`,
 1 AS `cr_by`,
 1 AS `upd_by`,
 1 AS `cr_dep_id`*/;
SET character_set_client = @saved_cs_client;

--
-- Temporary view structure for view `_dep_has_client_count_main_year`
--

DROP TABLE IF EXISTS `_dep_has_client_count_main_year`;
/*!50001 DROP VIEW IF EXISTS `_dep_has_client_count_main_year`*/;
SET @saved_cs_client     = @@character_set_client;
/*!50503 SET character_set_client = utf8mb4 */;
/*!50001 CREATE VIEW `_dep_has_client_count_main_year` AS SELECT 
 1 AS `quantity`,
 1 AS `id`,
 1 AS `client`,
 1 AS `client_short`,
 1 AS `clientDeath`,
 1 AS `clientbirth`,
 1 AS `ESRN`,
 1 AS `note`,
 1 AS `phone`,
 1 AS `snils`,
 1 AS `curator`,
 1 AS `create`,
 1 AS `ts`,
 1 AS `cr_by`,
 1 AS `upd_by`,
 1 AS `cr_dep_id`*/;
SET character_set_client = @saved_cs_client;

--
-- Temporary view structure for view `_dep_has_client_count_month`
--

DROP TABLE IF EXISTS `_dep_has_client_count_month`;
/*!50001 DROP VIEW IF EXISTS `_dep_has_client_count_month`*/;
SET @saved_cs_client     = @@character_set_client;
/*!50503 SET character_set_client = utf8mb4 */;
/*!50001 CREATE VIEW `_dep_has_client_count_month` AS SELECT 
 1 AS `quantity`,
 1 AS `id`,
 1 AS `client`,
 1 AS `client_short`,
 1 AS `clientDeath`,
 1 AS `clientbirth`,
 1 AS `ESRN`,
 1 AS `note`,
 1 AS `phone`,
 1 AS `snils`,
 1 AS `curator`,
 1 AS `create`,
 1 AS `ts`,
 1 AS `cr_by`,
 1 AS `upd_by`,
 1 AS `cr_dep_id`*/;
SET character_set_client = @saved_cs_client;

--
-- Temporary view structure for view `_dep_has_client_ended`
--

DROP TABLE IF EXISTS `_dep_has_client_ended`;
/*!50001 DROP VIEW IF EXISTS `_dep_has_client_ended`*/;
SET @saved_cs_client     = @@character_set_client;
/*!50503 SET character_set_client = utf8mb4 */;
/*!50001 CREATE VIEW `_dep_has_client_ended` AS SELECT 
 1 AS `client`,
 1 AS `id`,
 1 AS `contracts`,
 1 AS `client_id`,
 1 AS `dep_id`,
 1 AS `ripso_id`,
 1 AS `blocked`,
 1 AS `startdate`,
 1 AS `enddate`,
 1 AS `ippsuNum`,
 1 AS `note`,
 1 AS `create`,
 1 AS `ts`,
 1 AS `cr_by`,
 1 AS `upd_by`,
 1 AS `to_recheck`,
 1 AS `check_date`*/;
SET character_set_client = @saved_cs_client;

--
-- Temporary view structure for view `_dep_has_client_ending`
--

DROP TABLE IF EXISTS `_dep_has_client_ending`;
/*!50001 DROP VIEW IF EXISTS `_dep_has_client_ending`*/;
SET @saved_cs_client     = @@character_set_client;
/*!50503 SET character_set_client = utf8mb4 */;
/*!50001 CREATE VIEW `_dep_has_client_ending` AS SELECT 
 1 AS `client`,
 1 AS `id`,
 1 AS `contracts`,
 1 AS `client_id`,
 1 AS `dep_id`,
 1 AS `ripso_id`,
 1 AS `blocked`,
 1 AS `startdate`,
 1 AS `enddate`,
 1 AS `ippsuNum`,
 1 AS `note`,
 1 AS `create`,
 1 AS `ts`,
 1 AS `cr_by`,
 1 AS `upd_by`,
 1 AS `to_recheck`,
 1 AS `check_date`*/;
SET character_set_client = @saved_cs_client;

--
-- Temporary view structure for view `_dep_has_client_more`
--

DROP TABLE IF EXISTS `_dep_has_client_more`;
/*!50001 DROP VIEW IF EXISTS `_dep_has_client_more`*/;
SET @saved_cs_client     = @@character_set_client;
/*!50503 SET character_set_client = utf8mb4 */;
/*!50001 CREATE VIEW `_dep_has_client_more` AS SELECT 
 1 AS `id`,
 1 AS `client`,
 1 AS `client_short`,
 1 AS `clientDeath`,
 1 AS `clientbirth`,
 1 AS `ESRN`,
 1 AS `prim_fio`,
 1 AS `phone`,
 1 AS `snils`,
 1 AS `curator_fio`,
 1 AS `create_fio`,
 1 AS `ts_fio`,
 1 AS `cr_by_fio`,
 1 AS `upd_by_fio`,
 1 AS `client_id`,
 1 AS `pddate`,
 1 AS `contracts_id`,
 1 AS `predv_money`,
 1 AS `curFIO`,
 1 AS `psp`,
 1 AS `address`,
 1 AS `sdd`,
 1 AS `sdd_date`,
 1 AS `perc`,
 1 AS `not_standart_contract`,
 1 AS `not_standart_act`,
 1 AS `note`,
 1 AS `create`,
 1 AS `ts`,
 1 AS `cr_by`,
 1 AS `upd_by`,
 1 AS `repr_FIO`,
 1 AS `repr_addr`,
 1 AS `repr_psp`,
 1 AS `work_livemin`*/;
SET character_set_client = @saved_cs_client;

--
-- Temporary view structure for view `_dep_has_client_ripso`
--

DROP TABLE IF EXISTS `_dep_has_client_ripso`;
/*!50001 DROP VIEW IF EXISTS `_dep_has_client_ripso`*/;
SET @saved_cs_client     = @@character_set_client;
/*!50503 SET character_set_client = utf8mb4 */;
/*!50001 CREATE VIEW `_dep_has_client_ripso` AS SELECT 
 1 AS `id`,
 1 AS `client`,
 1 AS `client_short`,
 1 AS `clientDeath`,
 1 AS `clientbirth`,
 1 AS `ESRN`,
 1 AS `note`,
 1 AS `phone`,
 1 AS `snils`,
 1 AS `curator`,
 1 AS `create`,
 1 AS `ts`,
 1 AS `cr_by`,
 1 AS `upd_by`,
 1 AS `cr_dep_id`*/;
SET character_set_client = @saved_cs_client;

--
-- Temporary view structure for view `_dep_has_client_ripso_or_contracts`
--

DROP TABLE IF EXISTS `_dep_has_client_ripso_or_contracts`;
/*!50001 DROP VIEW IF EXISTS `_dep_has_client_ripso_or_contracts`*/;
SET @saved_cs_client     = @@character_set_client;
/*!50503 SET character_set_client = utf8mb4 */;
/*!50001 CREATE VIEW `_dep_has_client_ripso_or_contracts` AS SELECT 
 1 AS `id`,
 1 AS `client`,
 1 AS `client_short`,
 1 AS `clientDeath`,
 1 AS `clientbirth`,
 1 AS `ESRN`,
 1 AS `note`,
 1 AS `phone`,
 1 AS `snils`,
 1 AS `curator`,
 1 AS `create`,
 1 AS `ts`,
 1 AS `cr_by`,
 1 AS `upd_by`,
 1 AS `cr_dep_id`*/;
SET character_set_client = @saved_cs_client;

--
-- Temporary view structure for view `_dep_has_client_year`
--

DROP TABLE IF EXISTS `_dep_has_client_year`;
/*!50001 DROP VIEW IF EXISTS `_dep_has_client_year`*/;
SET @saved_cs_client     = @@character_set_client;
/*!50503 SET character_set_client = utf8mb4 */;
/*!50001 CREATE VIEW `_dep_has_client_year` AS SELECT 
 1 AS `id`,
 1 AS `client`,
 1 AS `client_short`,
 1 AS `clientDeath`,
 1 AS `clientbirth`,
 1 AS `ESRN`,
 1 AS `note`,
 1 AS `phone`,
 1 AS `snils`,
 1 AS `curator`,
 1 AS `create`,
 1 AS `ts`,
 1 AS `cr_by`,
 1 AS `upd_by`,
 1 AS `cr_dep_id`*/;
SET character_set_client = @saved_cs_client;

--
-- Temporary view structure for view `_dep_has_contracts`
--

DROP TABLE IF EXISTS `_dep_has_contracts`;
/*!50001 DROP VIEW IF EXISTS `_dep_has_contracts`*/;
SET @saved_cs_client     = @@character_set_client;
/*!50503 SET character_set_client = utf8mb4 */;
/*!50001 CREATE VIEW `_dep_has_contracts` AS SELECT 
 1 AS `client`,
 1 AS `id`,
 1 AS `contracts`,
 1 AS `contracts2`,
 1 AS `client_id`,
 1 AS `dep_id`,
 1 AS `ripso_id`,
 1 AS `blocked`,
 1 AS `startdate`,
 1 AS `enddate`,
 1 AS `ippsuNum`,
 1 AS `note`,
 1 AS `create`,
 1 AS `ts`,
 1 AS `cr_by`,
 1 AS `upd_by`,
 1 AS `to_recheck`,
 1 AS `check_date`,
 1 AS `pyc_prim`*/;
SET character_set_client = @saved_cs_client;

--
-- Temporary view structure for view `_dep_has_main`
--

DROP TABLE IF EXISTS `_dep_has_main`;
/*!50001 DROP VIEW IF EXISTS `_dep_has_main`*/;
SET @saved_cs_client     = @@character_set_client;
/*!50503 SET character_set_client = utf8mb4 */;
/*!50001 CREATE VIEW `_dep_has_main` AS SELECT 
 1 AS `id`,
 1 AS `contracts_id`,
 1 AS `dep_id`,
 1 AS `client_id`,
 1 AS `serv_id`,
 1 AS `dep_has_worker_id`,
 1 AS `worker_id`,
 1 AS `vdate`,
 1 AS `quantity`,
 1 AS `note`,
 1 AS `create`,
 1 AS `ts`,
 1 AS `cr_by`,
 1 AS `upd_by`,
 1 AS `reported`,
 1 AS `wdate`,
 1 AS `overdid`,
 1 AS `prev_quantity`*/;
SET character_set_client = @saved_cs_client;

--
-- Temporary view structure for view `_dep_has_new_client`
--

DROP TABLE IF EXISTS `_dep_has_new_client`;
/*!50001 DROP VIEW IF EXISTS `_dep_has_new_client`*/;
SET @saved_cs_client     = @@character_set_client;
/*!50503 SET character_set_client = utf8mb4 */;
/*!50001 CREATE VIEW `_dep_has_new_client` AS SELECT 
 1 AS `id`,
 1 AS `client`,
 1 AS `client_short`,
 1 AS `clientDeath`,
 1 AS `clientbirth`,
 1 AS `ESRN`,
 1 AS `note`,
 1 AS `phone`,
 1 AS `snils`,
 1 AS `curator`,
 1 AS `create`,
 1 AS `ts`,
 1 AS `cr_by`,
 1 AS `upd_by`,
 1 AS `cr_dep_id`*/;
SET character_set_client = @saved_cs_client;

--
-- Temporary view structure for view `_dep_has_ripso`
--

DROP TABLE IF EXISTS `_dep_has_ripso`;
/*!50001 DROP VIEW IF EXISTS `_dep_has_ripso`*/;
SET @saved_cs_client     = @@character_set_client;
/*!50503 SET character_set_client = utf8mb4 */;
/*!50001 CREATE VIEW `_dep_has_ripso` AS SELECT 
 1 AS `ripso_id`,
 1 AS `ripso`*/;
SET character_set_client = @saved_cs_client;

--
-- Temporary view structure for view `_dep_has_worker`
--

DROP TABLE IF EXISTS `_dep_has_worker`;
/*!50001 DROP VIEW IF EXISTS `_dep_has_worker`*/;
SET @saved_cs_client     = @@character_set_client;
/*!50503 SET character_set_client = utf8mb4 */;
/*!50001 CREATE VIEW `_dep_has_worker` AS SELECT 
 1 AS `id`,
 1 AS `dep_has_worker`,
 1 AS `worker_id`,
 1 AS `dep_id`,
 1 AS `job_id`,
 1 AS `note`,
 1 AS `archive`,
 1 AS `from`,
 1 AS `till`,
 1 AS `role_id`,
 1 AS `api_key`*/;
SET character_set_client = @saved_cs_client;

--
-- Temporary view structure for view `_dep_has_workers`
--

DROP TABLE IF EXISTS `_dep_has_workers`;
/*!50001 DROP VIEW IF EXISTS `_dep_has_workers`*/;
SET @saved_cs_client     = @@character_set_client;
/*!50503 SET character_set_client = utf8mb4 */;
/*!50001 CREATE VIEW `_dep_has_workers` AS SELECT 
 1 AS `id`,
 1 AS `worker`,
 1 AS `user`,
 1 AS `note`,
 1 AS `role_id`,
 1 AS `dep_id`,
 1 AS `archive`*/;
SET character_set_client = @saved_cs_client;

--
-- Temporary view structure for view `_dhw_has_client`
--

DROP TABLE IF EXISTS `_dhw_has_client`;
/*!50001 DROP VIEW IF EXISTS `_dhw_has_client`*/;
SET @saved_cs_client     = @@character_set_client;
/*!50503 SET character_set_client = utf8mb4 */;
/*!50001 CREATE VIEW `_dhw_has_client` AS SELECT 
 1 AS `dhw_id`,
 1 AS `client_id`,
 1 AS `note`*/;
SET character_set_client = @saved_cs_client;

--
-- Temporary view structure for view `_g_categ_list_client_for_dep_for_year`
--

DROP TABLE IF EXISTS `_g_categ_list_client_for_dep_for_year`;
/*!50001 DROP VIEW IF EXISTS `_g_categ_list_client_for_dep_for_year`*/;
SET @saved_cs_client     = @@character_set_client;
/*!50503 SET character_set_client = utf8mb4 */;
/*!50001 CREATE VIEW `_g_categ_list_client_for_dep_for_year` AS SELECT 
 1 AS `category_id`,
 1 AS `client_id`,
 1 AS `SUM(quantity)`*/;
SET character_set_client = @saved_cs_client;

--
-- Temporary view structure for view `_g_serv_list_for_dep_for_year`
--

DROP TABLE IF EXISTS `_g_serv_list_for_dep_for_year`;
/*!50001 DROP VIEW IF EXISTS `_g_serv_list_for_dep_for_year`*/;
SET @saved_cs_client     = @@character_set_client;
/*!50503 SET character_set_client = utf8mb4 */;
/*!50001 CREATE VIEW `_g_serv_list_for_dep_for_year` AS SELECT 
 1 AS `category_id`,
 1 AS `count(client_id)`,
 1 AS `SUM(quantity)`*/;
SET character_set_client = @saved_cs_client;

--
-- Temporary view structure for view `_g_serv_total_you`
--

DROP TABLE IF EXISTS `_g_serv_total_you`;
/*!50001 DROP VIEW IF EXISTS `_g_serv_total_you`*/;
SET @saved_cs_client     = @@character_set_client;
/*!50503 SET character_set_client = utf8mb4 */;
/*!50001 CREATE VIEW `_g_serv_total_you` AS SELECT 
 1 AS `serv_id`,
 1 AS `quantity`,
 1 AS `client_id_count`,
 1 AS `client_id`,
 1 AS `records`*/;
SET character_set_client = @saved_cs_client;

--
-- Temporary view structure for view `_information_schema_columns`
--

DROP TABLE IF EXISTS `_information_schema_columns`;
/*!50001 DROP VIEW IF EXISTS `_information_schema_columns`*/;
SET @saved_cs_client     = @@character_set_client;
/*!50503 SET character_set_client = utf8mb4 */;
/*!50001 CREATE VIEW `_information_schema_columns` AS SELECT 
 1 AS `TABLE_NAME`,
 1 AS `ORDINAL_POSITION`,
 1 AS `COLUMN_NAME`,
 1 AS `IS_NULLABLE`,
 1 AS `COLUMN_DEFAULT`,
 1 AS `DATA_TYPE`,
 1 AS `NUMERIC_PRECISION`,
 1 AS `COLUMN_TYPE`,
 1 AS `CHARACTER_MAXIMUM_LENGTH`*/;
SET character_set_client = @saved_cs_client;

--
-- Temporary view structure for view `_main__months`
--

DROP TABLE IF EXISTS `_main__months`;
/*!50001 DROP VIEW IF EXISTS `_main__months`*/;
SET @saved_cs_client     = @@character_set_client;
/*!50503 SET character_set_client = utf8mb4 */;
/*!50001 CREATE VIEW `_main__months` AS SELECT 
 1 AS `serv_id`,
 1 AS `dep_id`,
 1 AS `contracts_id`,
 1 AS `year1`,
 1 AS `dep_has_worker_id`,
 1 AS `month1`,
 1 AS `month2`,
 1 AS `month3`,
 1 AS `month4`,
 1 AS `month5`,
 1 AS `month6`,
 1 AS `month7`,
 1 AS `month8`,
 1 AS `month9`,
 1 AS `month10`,
 1 AS `month11`,
 1 AS `month12`*/;
SET character_set_client = @saved_cs_client;

--
-- Temporary view structure for view `_main_cprice`
--

DROP TABLE IF EXISTS `_main_cprice`;
/*!50001 DROP VIEW IF EXISTS `_main_cprice`*/;
SET @saved_cs_client     = @@character_set_client;
/*!50503 SET character_set_client = utf8mb4 */;
/*!50001 CREATE VIEW `_main_cprice` AS SELECT 
 1 AS `id`,
 1 AS `contracts_id`,
 1 AS `dep_id`,
 1 AS `client_id`,
 1 AS `serv_id`,
 1 AS `dep_has_worker_id`,
 1 AS `worker_id`,
 1 AS `vdate`,
 1 AS `quantity`,
 1 AS `note`,
 1 AS `create`,
 1 AS `ts`,
 1 AS `cr_by`,
 1 AS `upd_by`,
 1 AS `reported`,
 1 AS `wdate`,
 1 AS `overdid`,
 1 AS `prev_quantity`,
 1 AS `perc`,
 1 AS `price`,
 1 AS `price2`,
 1 AS `price3`,
 1 AS `servform_id`,
 1 AS `tnum`,
 1 AS `serv`,
 1 AS `serv_text`,
 1 AS `sub_serv`,
 1 AS `to_pay`,
 1 AS `to_pay2`*/;
SET character_set_client = @saved_cs_client;

--
-- Temporary view structure for view `_main_cprice_for_contracts`
--

DROP TABLE IF EXISTS `_main_cprice_for_contracts`;
/*!50001 DROP VIEW IF EXISTS `_main_cprice_for_contracts`*/;
SET @saved_cs_client     = @@character_set_client;
/*!50503 SET character_set_client = utf8mb4 */;
/*!50001 CREATE VIEW `_main_cprice_for_contracts` AS SELECT 
 1 AS `id`,
 1 AS `contracts_id`,
 1 AS `dep_id`,
 1 AS `client_id`,
 1 AS `serv_id`,
 1 AS `dep_has_worker_id`,
 1 AS `worker_id`,
 1 AS `vdate`,
 1 AS `quantity`,
 1 AS `note`,
 1 AS `create`,
 1 AS `ts`,
 1 AS `cr_by`,
 1 AS `upd_by`,
 1 AS `reported`,
 1 AS `wdate`,
 1 AS `overdid`,
 1 AS `prev_quantity`,
 1 AS `perc`,
 1 AS `price`,
 1 AS `price2`,
 1 AS `price3`,
 1 AS `servform_id`,
 1 AS `to_pay`,
 1 AS `to_pay2`*/;
SET character_set_client = @saved_cs_client;

--
-- Temporary view structure for view `_main_for_dep`
--

DROP TABLE IF EXISTS `_main_for_dep`;
/*!50001 DROP VIEW IF EXISTS `_main_for_dep`*/;
SET @saved_cs_client     = @@character_set_client;
/*!50503 SET character_set_client = utf8mb4 */;
/*!50001 CREATE VIEW `_main_for_dep` AS SELECT 
 1 AS `id`,
 1 AS `contracts_id`,
 1 AS `dep_id`,
 1 AS `client_id`,
 1 AS `serv_id`,
 1 AS `dep_has_worker_id`,
 1 AS `worker_id`,
 1 AS `vdate`,
 1 AS `quantity`,
 1 AS `note`,
 1 AS `create`,
 1 AS `ts`,
 1 AS `cr_by`,
 1 AS `upd_by`,
 1 AS `reported`,
 1 AS `wdate`,
 1 AS `overdid`,
 1 AS `prev_quantity`*/;
SET character_set_client = @saved_cs_client;

--
-- Temporary view structure for view `_main_for_you`
--

DROP TABLE IF EXISTS `_main_for_you`;
/*!50001 DROP VIEW IF EXISTS `_main_for_you`*/;
SET @saved_cs_client     = @@character_set_client;
/*!50503 SET character_set_client = utf8mb4 */;
/*!50001 CREATE VIEW `_main_for_you` AS SELECT 
 1 AS `id`,
 1 AS `contracts_id`,
 1 AS `dep_id`,
 1 AS `client_id`,
 1 AS `serv_id`,
 1 AS `dep_has_worker_id`,
 1 AS `worker_id`,
 1 AS `vdate`,
 1 AS `quantity`,
 1 AS `note`,
 1 AS `create`,
 1 AS `ts`,
 1 AS `cr_by`,
 1 AS `upd_by`,
 1 AS `reported`,
 1 AS `wdate`,
 1 AS `overdid`,
 1 AS `prev_quantity`*/;
SET character_set_client = @saved_cs_client;

--
-- Temporary view structure for view `_main_months`
--

DROP TABLE IF EXISTS `_main_months`;
/*!50001 DROP VIEW IF EXISTS `_main_months`*/;
SET @saved_cs_client     = @@character_set_client;
/*!50503 SET character_set_client = utf8mb4 */;
/*!50001 CREATE VIEW `_main_months` AS SELECT 
 1 AS `serv_id`,
 1 AS `dep_id`,
 1 AS `contracts_id`,
 1 AS `year1`,
 1 AS `dep_has_worker_id`,
 1 AS `month1`,
 1 AS `month2`,
 1 AS `month3`,
 1 AS `month4`,
 1 AS `month5`,
 1 AS `month6`,
 1 AS `month7`,
 1 AS `month8`,
 1 AS `month9`,
 1 AS `month10`,
 1 AS `month11`,
 1 AS `month12`*/;
SET character_set_client = @saved_cs_client;

--
-- Temporary view structure for view `_main_serv_name`
--

DROP TABLE IF EXISTS `_main_serv_name`;
/*!50001 DROP VIEW IF EXISTS `_main_serv_name`*/;
SET @saved_cs_client     = @@character_set_client;
/*!50503 SET character_set_client = utf8mb4 */;
/*!50001 CREATE VIEW `_main_serv_name` AS SELECT 
 1 AS `serv`,
 1 AS `id`,
 1 AS `contracts_id`,
 1 AS `dep_id`,
 1 AS `client_id`,
 1 AS `serv_id`,
 1 AS `dep_has_worker_id`,
 1 AS `worker_id`,
 1 AS `vdate`,
 1 AS `quantity`,
 1 AS `note`,
 1 AS `create`,
 1 AS `ts`,
 1 AS `cr_by`,
 1 AS `upd_by`,
 1 AS `reported`,
 1 AS `wdate`,
 1 AS `overdid`,
 1 AS `prev_quantity`*/;
SET character_set_client = @saved_cs_client;

--
-- Temporary view structure for view `_main_serv_name_ripso`
--

DROP TABLE IF EXISTS `_main_serv_name_ripso`;
/*!50001 DROP VIEW IF EXISTS `_main_serv_name_ripso`*/;
SET @saved_cs_client     = @@character_set_client;
/*!50503 SET character_set_client = utf8mb4 */;
/*!50001 CREATE VIEW `_main_serv_name_ripso` AS SELECT 
 1 AS `serv`,
 1 AS `ripso_id`,
 1 AS `id`,
 1 AS `contracts_id`,
 1 AS `dep_id`,
 1 AS `client_id`,
 1 AS `serv_id`,
 1 AS `dep_has_worker_id`,
 1 AS `worker_id`,
 1 AS `vdate`,
 1 AS `quantity`,
 1 AS `note`,
 1 AS `create`,
 1 AS `ts`,
 1 AS `cr_by`,
 1 AS `upd_by`,
 1 AS `reported`,
 1 AS `wdate`,
 1 AS `overdid`,
 1 AS `prev_quantity`*/;
SET character_set_client = @saved_cs_client;

--
-- Temporary view structure for view `_main_serv_name_ripso_static`
--

DROP TABLE IF EXISTS `_main_serv_name_ripso_static`;
/*!50001 DROP VIEW IF EXISTS `_main_serv_name_ripso_static`*/;
SET @saved_cs_client     = @@character_set_client;
/*!50503 SET character_set_client = utf8mb4 */;
/*!50001 CREATE VIEW `_main_serv_name_ripso_static` AS SELECT 
 1 AS `serv`,
 1 AS `ripso_id`,
 1 AS `id`,
 1 AS `contracts_id`,
 1 AS `dep_id`,
 1 AS `client_id`,
 1 AS `serv_id`,
 1 AS `dep_has_worker_id`,
 1 AS `worker_id`,
 1 AS `vdate`,
 1 AS `quantity`,
 1 AS `note`,
 1 AS `create`,
 1 AS `ts`,
 1 AS `cr_by`,
 1 AS `upd_by`,
 1 AS `reported`,
 1 AS `wdate`,
 1 AS `overdid`,
 1 AS `prev_quantity`*/;
SET character_set_client = @saved_cs_client;

--
-- Temporary view structure for view `_main_serv_name_static`
--

DROP TABLE IF EXISTS `_main_serv_name_static`;
/*!50001 DROP VIEW IF EXISTS `_main_serv_name_static`*/;
SET @saved_cs_client     = @@character_set_client;
/*!50503 SET character_set_client = utf8mb4 */;
/*!50001 CREATE VIEW `_main_serv_name_static` AS SELECT 
 1 AS `serv`,
 1 AS `id`,
 1 AS `contracts_id`,
 1 AS `dep_id`,
 1 AS `client_id`,
 1 AS `serv_id`,
 1 AS `dep_has_worker_id`,
 1 AS `worker_id`,
 1 AS `vdate`,
 1 AS `quantity`,
 1 AS `note`,
 1 AS `create`,
 1 AS `ts`,
 1 AS `cr_by`,
 1 AS `upd_by`,
 1 AS `reported`,
 1 AS `wdate`,
 1 AS `overdid`,
 1 AS `prev_quantity`*/;
SET character_set_client = @saved_cs_client;

--
-- Temporary view structure for view `_serv_activ`
--

DROP TABLE IF EXISTS `_serv_activ`;
/*!50001 DROP VIEW IF EXISTS `_serv_activ`*/;
SET @saved_cs_client     = @@character_set_client;
/*!50503 SET character_set_client = utf8mb4 */;
/*!50001 CREATE VIEW `_serv_activ` AS SELECT 
 1 AS `id`,
 1 AS `serv`,
 1 AS `serv_text`,
 1 AS `tnum`,
 1 AS `price`,
 1 AS `total`,
 1 AS `sub_serv`,
 1 AS `serv_id_list`*/;
SET character_set_client = @saved_cs_client;

--
-- Temporary view structure for view `_serv_total`
--

DROP TABLE IF EXISTS `_serv_total`;
/*!50001 DROP VIEW IF EXISTS `_serv_total`*/;
SET @saved_cs_client     = @@character_set_client;
/*!50503 SET character_set_client = utf8mb4 */;
/*!50001 CREATE VIEW `_serv_total` AS SELECT 
 1 AS `id`,
 1 AS `serv`,
 1 AS `serv_text`,
 1 AS `tnum`,
 1 AS `year`,
 1 AS `sub_serv`,
 1 AS `sub_serv_str`,
 1 AS `price`,
 1 AS `price2`,
 1 AS `price3`,
 1 AS `archive`,
 1 AS `total`,
 1 AS `acronym`,
 1 AS `workload`,
 1 AS `content`,
 1 AS `create`,
 1 AS `ts`,
 1 AS `cr_by`,
 1 AS `upd_by`*/;
SET character_set_client = @saved_cs_client;

--
-- Temporary view structure for view `_user_has_main`
--

DROP TABLE IF EXISTS `_user_has_main`;
/*!50001 DROP VIEW IF EXISTS `_user_has_main`*/;
SET @saved_cs_client     = @@character_set_client;
/*!50503 SET character_set_client = utf8mb4 */;
/*!50001 CREATE VIEW `_user_has_main` AS SELECT 
 1 AS `id`,
 1 AS `contracts_id`,
 1 AS `dep_id`,
 1 AS `client_id`,
 1 AS `serv_id`,
 1 AS `dep_has_worker_id`,
 1 AS `worker_id`,
 1 AS `vdate`,
 1 AS `quantity`,
 1 AS `note`,
 1 AS `create`,
 1 AS `ts`,
 1 AS `cr_by`,
 1 AS `upd_by`,
 1 AS `reported`,
 1 AS `wdate`,
 1 AS `overdid`,
 1 AS `prev_quantity`*/;
SET character_set_client = @saved_cs_client;

--
-- Temporary view structure for view `_user_has_main_limit30`
--

DROP TABLE IF EXISTS `_user_has_main_limit30`;
/*!50001 DROP VIEW IF EXISTS `_user_has_main_limit30`*/;
SET @saved_cs_client     = @@character_set_client;
/*!50503 SET character_set_client = utf8mb4 */;
/*!50001 CREATE VIEW `_user_has_main_limit30` AS SELECT 
 1 AS `id`,
 1 AS `contracts_id`,
 1 AS `dep_id`,
 1 AS `client_id`,
 1 AS `serv_id`,
 1 AS `dep_has_worker_id`,
 1 AS `worker_id`,
 1 AS `vdate`,
 1 AS `quantity`,
 1 AS `note`,
 1 AS `create`,
 1 AS `ts`,
 1 AS `cr_by`,
 1 AS `upd_by`,
 1 AS `reported`,
 1 AS `wdate`,
 1 AS `overdid`,
 1 AS `prev_quantity`*/;
SET character_set_client = @saved_cs_client;

--
-- Temporary view structure for view `_user_has_main_today`
--

DROP TABLE IF EXISTS `_user_has_main_today`;
/*!50001 DROP VIEW IF EXISTS `_user_has_main_today`*/;
SET @saved_cs_client     = @@character_set_client;
/*!50503 SET character_set_client = utf8mb4 */;
/*!50001 CREATE VIEW `_user_has_main_today` AS SELECT 
 1 AS `id`,
 1 AS `contracts_id`,
 1 AS `dep_id`,
 1 AS `client_id`,
 1 AS `serv_id`,
 1 AS `dep_has_worker_id`,
 1 AS `worker_id`,
 1 AS `vdate`,
 1 AS `quantity`,
 1 AS `note`,
 1 AS `create`,
 1 AS `ts`,
 1 AS `cr_by`,
 1 AS `upd_by`,
 1 AS `reported`,
 1 AS `wdate`,
 1 AS `overdid`,
 1 AS `prev_quantity`*/;
SET character_set_client = @saved_cs_client;

--
-- Temporary view structure for view `_worker_has_dep`
--

DROP TABLE IF EXISTS `_worker_has_dep`;
/*!50001 DROP VIEW IF EXISTS `_worker_has_dep`*/;
SET @saved_cs_client     = @@character_set_client;
/*!50503 SET character_set_client = utf8mb4 */;
/*!50001 CREATE VIEW `_worker_has_dep` AS SELECT 
 1 AS `id`,
 1 AS `dep`*/;
SET character_set_client = @saved_cs_client;

--
-- Temporary view structure for view `_worker_has_main`
--

DROP TABLE IF EXISTS `_worker_has_main`;
/*!50001 DROP VIEW IF EXISTS `_worker_has_main`*/;
SET @saved_cs_client     = @@character_set_client;
/*!50503 SET character_set_client = utf8mb4 */;
/*!50001 CREATE VIEW `_worker_has_main` AS SELECT 
 1 AS `id`,
 1 AS `contracts_id`,
 1 AS `dep_id`,
 1 AS `client_id`,
 1 AS `serv_id`,
 1 AS `dep_has_worker_id`,
 1 AS `worker_id`,
 1 AS `vdate`,
 1 AS `quantity`,
 1 AS `note`,
 1 AS `create`,
 1 AS `ts`,
 1 AS `cr_by`,
 1 AS `upd_by`,
 1 AS `reported`,
 1 AS `wdate`,
 1 AS `overdid`,
 1 AS `prev_quantity`*/;
SET character_set_client = @saved_cs_client;

--
-- Temporary view structure for view `_worker_settings`
--

DROP TABLE IF EXISTS `_worker_settings`;
/*!50001 DROP VIEW IF EXISTS `_worker_settings`*/;
SET @saved_cs_client     = @@character_set_client;
/*!50503 SET character_set_client = utf8mb4 */;
/*!50001 CREATE VIEW `_worker_settings` AS SELECT 
 1 AS `id`,
 1 AS `last_tab`,
 1 AS `last_dep`,
 1 AS `last_client`,
 1 AS `last_contr`,
 1 AS `last_client_filter`,
 1 AS `last_year`*/;
SET character_set_client = @saved_cs_client;

--
-- Table structure for table `add_info`
--

DROP TABLE IF EXISTS `add_info`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `add_info` (
  `pddate` date NOT NULL,
  `contracts_id` int unsigned NOT NULL,
  `predv_money` decimal(10,2) DEFAULT NULL,
  `curFIO` varchar(255) DEFAULT NULL,
  `psp` varchar(255) DEFAULT NULL,
  `address` varchar(255) DEFAULT NULL,
  `sdd` decimal(10,2) DEFAULT NULL,
  `sdd_date` date DEFAULT NULL COMMENT 'Дата первое число месяца в котором проверяли СДД (будут взяты 12 предшествующих этой дате месяцев)',
  `perc` double DEFAULT NULL,
  `not_standart_contract` tinyint DEFAULT NULL,
  `not_standart_act` tinyint DEFAULT NULL,
  `note` varchar(255) DEFAULT NULL,
  `create` datetime DEFAULT CURRENT_TIMESTAMP,
  `ts` datetime DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  `cr_by` int DEFAULT NULL,
  `upd_by` int DEFAULT NULL,
  `repr_FIO` varchar(255) DEFAULT NULL,
  `repr_addr` varchar(255) DEFAULT NULL,
  `repr_psp` varchar(255) DEFAULT NULL,
  `work_livemin` tinyint DEFAULT '0',
  PRIMARY KEY (`pddate`,`contracts_id`),
  KEY `fk_add_info_contracts1_idx` (`contracts_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;
/*!50003 SET @saved_cs_client      = @@character_set_client */ ;
/*!50003 SET @saved_cs_results     = @@character_set_results */ ;
/*!50003 SET @saved_col_connection = @@collation_connection */ ;
/*!50003 SET character_set_client  = utf8mb4 */ ;
/*!50003 SET character_set_results = utf8mb4 */ ;
/*!50003 SET collation_connection  = utf8mb4_0900_ai_ci */ ;
/*!50003 SET @saved_sql_mode       = @@sql_mode */ ;
/*!50003 SET sql_mode              = 'ONLY_FULL_GROUP_BY,STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_ENGINE_SUBSTITUTION' */ ;
DELIMITER @@
/*!50003 CREATE*/ /*!50017 DEFINER=`root`@`localhost`*/ /*!50003 TRIGGER `add_info_BEFORE_INSERT` BEFORE INSERT ON `add_info` FOR EACH ROW BEGIN

	SET  NEW.cr_by = get_wID();
	SET  NEW.upd_by = get_wID();
END */@@
DELIMITER ;
/*!50003 SET sql_mode              = @saved_sql_mode */ ;
/*!50003 SET character_set_client  = @saved_cs_client */ ;
/*!50003 SET character_set_results = @saved_cs_results */ ;
/*!50003 SET collation_connection  = @saved_col_connection */ ;
/*!50003 SET @saved_cs_client      = @@character_set_client */ ;
/*!50003 SET @saved_cs_results     = @@character_set_results */ ;
/*!50003 SET @saved_col_connection = @@collation_connection */ ;
/*!50003 SET character_set_client  = utf8mb4 */ ;
/*!50003 SET character_set_results = utf8mb4 */ ;
/*!50003 SET collation_connection  = utf8mb4_0900_ai_ci */ ;
/*!50003 SET @saved_sql_mode       = @@sql_mode */ ;
/*!50003 SET sql_mode              = 'ONLY_FULL_GROUP_BY,STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_ENGINE_SUBSTITUTION' */ ;
DELIMITER @@
/*!50003 CREATE*/ /*!50017 DEFINER=`root`@`localhost`*/ /*!50003 TRIGGER `add_info_AFTER_INSERT` AFTER INSERT ON `add_info` FOR EACH ROW BEGIN
	declare ripso int default 0;
    DECLARE CONTINUE HANDLER FOR SQLEXCEPTION set ripso =0 ;
    set ripso = (select ripso_id from contracts where id=new.contracts_id);
    if ripso > 0 then
		insert into contracts_has_serv (serv_id, contracts_id, planned, archive)
			select serv_id, new.contracts_id, planned,0 from ripso_has_serv where ripso_id=ripso;
		# By default ippsu had all services of ripso - worker can change it later
    end if;
END */@@
DELIMITER ;
/*!50003 SET sql_mode              = @saved_sql_mode */ ;
/*!50003 SET character_set_client  = @saved_cs_client */ ;
/*!50003 SET character_set_results = @saved_cs_results */ ;
/*!50003 SET collation_connection  = @saved_col_connection */ ;
/*!50003 SET @saved_cs_client      = @@character_set_client */ ;
/*!50003 SET @saved_cs_results     = @@character_set_results */ ;
/*!50003 SET @saved_col_connection = @@collation_connection */ ;
/*!50003 SET character_set_client  = utf8mb4 */ ;
/*!50003 SET character_set_results = utf8mb4 */ ;
/*!50003 SET collation_connection  = utf8mb4_0900_ai_ci */ ;
/*!50003 SET @saved_sql_mode       = @@sql_mode */ ;
/*!50003 SET sql_mode              = 'ONLY_FULL_GROUP_BY,STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_ENGINE_SUBSTITUTION' */ ;
DELIMITER @@
/*!50003 CREATE*/ /*!50017 DEFINER=`root`@`localhost`*/ /*!50003 TRIGGER `add_info_BEFORE_UPDATE` BEFORE UPDATE ON `add_info` FOR EACH ROW BEGIN

SET  NEW.upd_by = get_wID();
END */@@
DELIMITER ;
/*!50003 SET sql_mode              = @saved_sql_mode */ ;
/*!50003 SET character_set_client  = @saved_cs_client */ ;
/*!50003 SET character_set_results = @saved_cs_results */ ;
/*!50003 SET collation_connection  = @saved_col_connection */ ;

--
-- Temporary view structure for view `add_info_for_client`
--

DROP TABLE IF EXISTS `add_info_for_client`;
/*!50001 DROP VIEW IF EXISTS `add_info_for_client`*/;
SET @saved_cs_client     = @@character_set_client;
/*!50503 SET character_set_client = utf8mb4 */;
/*!50001 CREATE VIEW `add_info_for_client` AS SELECT 
 1 AS `client_id`,
 1 AS `pddate`,
 1 AS `contracts_id`,
 1 AS `predv_money`,
 1 AS `curFIO`,
 1 AS `psp`,
 1 AS `address`,
 1 AS `sdd`,
 1 AS `sdd_date`,
 1 AS `perc`,
 1 AS `not_standart_contract`,
 1 AS `not_standart_act`,
 1 AS `note`,
 1 AS `create`,
 1 AS `ts`,
 1 AS `cr_by`,
 1 AS `upd_by`,
 1 AS `repr_FIO`,
 1 AS `repr_addr`,
 1 AS `repr_psp`,
 1 AS `work_livemin`*/;
SET character_set_client = @saved_cs_client;

--
-- Table structure for table `api_key_insert_main`
--

DROP TABLE IF EXISTS `api_key_insert_main`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `api_key_insert_main` (
  `id` bigint unsigned NOT NULL AUTO_INCREMENT,
  `contracts_id` int unsigned NOT NULL,
  `dep_id` int unsigned NOT NULL,
  `client_id` int unsigned NOT NULL,
  `serv_id` int unsigned NOT NULL,
  `dep_has_worker_id` int unsigned NOT NULL DEFAULT '0',
  `vdate` date NOT NULL COMMENT 'дата оказания услуги',
  `quantity` int DEFAULT '0' COMMENT 'Количество услуг',
  `note` varchar(255) DEFAULT NULL,
  `create` datetime DEFAULT CURRENT_TIMESTAMP,
  `uuid` varchar(36) NOT NULL,
  `check_api_key` varchar(100) DEFAULT NULL COMMENT 'If new.check_api_key incorrect - error',
  PRIMARY KEY (`id`),
  UNIQUE KEY `api_key_insert_main_UN` (`uuid`),
  UNIQUE KEY `api_key_insert_main_id_IDX` (`id`) USING BTREE,
  KEY `api_key_insert_main_uuid_IDX` (`uuid`) USING BTREE
) ENGINE=InnoDB AUTO_INCREMENT=248 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci COMMENT='inserts table web_info (special user)';
/*!40101 SET character_set_client = @saved_cs_client */;
/*!50003 SET @saved_cs_client      = @@character_set_client */ ;
/*!50003 SET @saved_cs_results     = @@character_set_results */ ;
/*!50003 SET @saved_col_connection = @@collation_connection */ ;
/*!50003 SET character_set_client  = utf8mb4 */ ;
/*!50003 SET character_set_results = utf8mb4 */ ;
/*!50003 SET collation_connection  = utf8mb4_0900_ai_ci */ ;
/*!50003 SET @saved_sql_mode       = @@sql_mode */ ;
/*!50003 SET sql_mode              = 'STRICT_TRANS_TABLES,NO_ENGINE_SUBSTITUTION' */ ;
DELIMITER @@
/*!50003 CREATE*/ /*!50017 DEFINER=`root`@`localhost`*/ /*!50003 TRIGGER `api_key_insert_main_on_insert` BEFORE INSERT ON `api_key_insert_main` FOR EACH ROW BEGIN

	SET  NEW.dep_id = (SELECT dep_id from dep_has_worker dhw where dhw.id = new.dep_has_worker_id);

	SET  NEW.client_id = (SELECT client_id from contracts c where c.id = new.contracts_id);

	if ( new.check_api_key =  (SELECT api_key from dep_has_worker dhw where dhw.id = new.dep_has_worker_id)) then 
		set new.check_api_key=new.dep_has_worker_id;
	else
		set new.check_api_key='error: wrong dep_has_worker_id';
		set new.quantity = 0;
	end if;

	END */@@
DELIMITER ;
/*!50003 SET sql_mode              = @saved_sql_mode */ ;
/*!50003 SET character_set_client  = @saved_cs_client */ ;
/*!50003 SET character_set_results = @saved_cs_results */ ;
/*!50003 SET collation_connection  = @saved_col_connection */ ;
/*!50003 SET @saved_cs_client      = @@character_set_client */ ;
/*!50003 SET @saved_cs_results     = @@character_set_results */ ;
/*!50003 SET @saved_col_connection = @@collation_connection */ ;
/*!50003 SET character_set_client  = utf8mb4 */ ;
/*!50003 SET character_set_results = utf8mb4 */ ;
/*!50003 SET collation_connection  = utf8mb4_0900_ai_ci */ ;
/*!50003 SET @saved_sql_mode       = @@sql_mode */ ;
/*!50003 SET sql_mode              = 'STRICT_TRANS_TABLES,NO_ENGINE_SUBSTITUTION' */ ;
DELIMITER @@
/*!50003 CREATE*/ /*!50017 DEFINER=`root`@`localhost`*/ /*!50003 TRIGGER `api_key_insert_main_after_insert` AFTER INSERT ON `api_key_insert_main` FOR EACH ROW begin
	
	insert into main (contracts_id, dep_id, client_id, serv_id, dep_has_worker_id, vdate, quantity, note)
	values( new.contracts_id ,new.dep_id, new.client_id, new.serv_id, new.dep_has_worker_id, new.vdate, new.quantity, new.uuid);


END */@@
DELIMITER ;
/*!50003 SET sql_mode              = @saved_sql_mode */ ;
/*!50003 SET character_set_client  = @saved_cs_client */ ;
/*!50003 SET character_set_results = @saved_cs_results */ ;
/*!50003 SET collation_connection  = @saved_col_connection */ ;
/*!50003 SET @saved_cs_client      = @@character_set_client */ ;
/*!50003 SET @saved_cs_results     = @@character_set_results */ ;
/*!50003 SET @saved_col_connection = @@collation_connection */ ;
/*!50003 SET character_set_client  = utf8mb4 */ ;
/*!50003 SET character_set_results = utf8mb4 */ ;
/*!50003 SET collation_connection  = utf8mb4_0900_ai_ci */ ;
/*!50003 SET @saved_sql_mode       = @@sql_mode */ ;
/*!50003 SET sql_mode              = 'STRICT_TRANS_TABLES,NO_ENGINE_SUBSTITUTION' */ ;
DELIMITER @@
/*!50003 CREATE*/ /*!50017 DEFINER=`root`@`localhost`*/ /*!50003 TRIGGER `api_key_before_update_main_` BEFORE UPDATE ON `api_key_insert_main` FOR EACH ROW begin 
	
	if ( new.check_api_key =  (SELECT api_key from dep_has_worker dhw where dhw.id = old.dep_has_worker_id)) then 
		set new.check_api_key=new.dep_has_worker_id;
		set new.dep_has_worker_id=old.dep_has_worker_id;
	else
		SIGNAL SQLSTATE '45000' 
		SET MESSAGE_TEXT = "error: wrong api_key";
	end if;
	
end */@@
DELIMITER ;
/*!50003 SET sql_mode              = @saved_sql_mode */ ;
/*!50003 SET character_set_client  = @saved_cs_client */ ;
/*!50003 SET character_set_results = @saved_cs_results */ ;
/*!50003 SET collation_connection  = @saved_col_connection */ ;
/*!50003 SET @saved_cs_client      = @@character_set_client */ ;
/*!50003 SET @saved_cs_results     = @@character_set_results */ ;
/*!50003 SET @saved_col_connection = @@collation_connection */ ;
/*!50003 SET character_set_client  = utf8mb4 */ ;
/*!50003 SET character_set_results = utf8mb4 */ ;
/*!50003 SET collation_connection  = utf8mb4_0900_ai_ci */ ;
/*!50003 SET @saved_sql_mode       = @@sql_mode */ ;
/*!50003 SET sql_mode              = 'STRICT_TRANS_TABLES,NO_ENGINE_SUBSTITUTION' */ ;
DELIMITER @@
/*!50003 CREATE*/ /*!50017 DEFINER=`root`@`localhost`*/ /*!50003 TRIGGER `api_key_insert_main_after_update` AFTER UPDATE ON `api_key_insert_main` FOR EACH ROW begin
	
	update main
		set quantity = new.quantity
		where note = new.uuid;


END */@@
DELIMITER ;
/*!50003 SET sql_mode              = @saved_sql_mode */ ;
/*!50003 SET character_set_client  = @saved_cs_client */ ;
/*!50003 SET character_set_results = @saved_cs_results */ ;
/*!50003 SET collation_connection  = @saved_col_connection */ ;

--
-- Table structure for table `audit`
--

DROP TABLE IF EXISTS `audit`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `audit` (
  `id` int NOT NULL,
  `date` datetime NOT NULL DEFAULT CURRENT_TIMESTAMP,
  `action` varchar(45) DEFAULT NULL,
  `user` varchar(32) DEFAULT NULL,
  `host` varchar(45) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `category`
--

DROP TABLE IF EXISTS `category`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `category` (
  `id` int unsigned NOT NULL AUTO_INCREMENT,
  `category` varchar(45) NOT NULL,
  `archive` tinyint DEFAULT '0',
  `note` varchar(255) DEFAULT NULL,
  `total` tinyint DEFAULT '0',
  `subof` int DEFAULT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `category_UNIQUE` (`category`)
) ENGINE=InnoDB AUTO_INCREMENT=17 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `client`
--

DROP TABLE IF EXISTS `client`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `client` (
  `id` int unsigned NOT NULL AUTO_INCREMENT,
  `client` varchar(255) NOT NULL,
  `client_short` varchar(150) DEFAULT NULL,
  `clientDeath` date DEFAULT NULL,
  `clientbirth` date DEFAULT NULL,
  `ESRN` bigint DEFAULT NULL,
  `note` varchar(255) DEFAULT NULL,
  `phone` varchar(45) DEFAULT NULL,
  `snils` varchar(14) DEFAULT NULL,
  `curator` varchar(45) DEFAULT NULL,
  `create` datetime DEFAULT CURRENT_TIMESTAMP,
  `ts` datetime DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  `cr_by` int DEFAULT NULL,
  `upd_by` int DEFAULT NULL,
  `cr_dep_id` int unsigned DEFAULT '0',
  PRIMARY KEY (`id`),
  UNIQUE KEY `client_UNIQUE` (`client`)
) ENGINE=InnoDB AUTO_INCREMENT=1447 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;
/*!50003 SET @saved_cs_client      = @@character_set_client */ ;
/*!50003 SET @saved_cs_results     = @@character_set_results */ ;
/*!50003 SET @saved_col_connection = @@collation_connection */ ;
/*!50003 SET character_set_client  = utf8mb4 */ ;
/*!50003 SET character_set_results = utf8mb4 */ ;
/*!50003 SET collation_connection  = utf8mb4_0900_ai_ci */ ;
/*!50003 SET @saved_sql_mode       = @@sql_mode */ ;
/*!50003 SET sql_mode              = 'ONLY_FULL_GROUP_BY,STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_ENGINE_SUBSTITUTION' */ ;
DELIMITER @@
/*!50003 CREATE*/ /*!50017 DEFINER=`root`@`localhost`*/ /*!50003 TRIGGER `client_BEFORE_INSERT` BEFORE INSERT ON `client` FOR EACH ROW BEGIN

    set new.client=trim(new.client);
	SET  NEW.cr_by = get_wID();
	SET  NEW.upd_by = get_wID();
    SET  NEW.cr_dep_id = GET_DEP(GET_wID());
END */@@
DELIMITER ;
/*!50003 SET sql_mode              = @saved_sql_mode */ ;
/*!50003 SET character_set_client  = @saved_cs_client */ ;
/*!50003 SET character_set_results = @saved_cs_results */ ;
/*!50003 SET collation_connection  = @saved_col_connection */ ;
/*!50003 SET @saved_cs_client      = @@character_set_client */ ;
/*!50003 SET @saved_cs_results     = @@character_set_results */ ;
/*!50003 SET @saved_col_connection = @@collation_connection */ ;
/*!50003 SET character_set_client  = utf8mb4 */ ;
/*!50003 SET character_set_results = utf8mb4 */ ;
/*!50003 SET collation_connection  = utf8mb4_0900_ai_ci */ ;
/*!50003 SET @saved_sql_mode       = @@sql_mode */ ;
/*!50003 SET sql_mode              = 'ONLY_FULL_GROUP_BY,STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_ENGINE_SUBSTITUTION' */ ;
DELIMITER @@
/*!50003 CREATE*/ /*!50017 DEFINER=`root`@`localhost`*/ /*!50003 TRIGGER `client_AFTER_INSERT` AFTER INSERT ON `client` FOR EACH ROW BEGIN

	
	
	
	
    
END */@@
DELIMITER ;
/*!50003 SET sql_mode              = @saved_sql_mode */ ;
/*!50003 SET character_set_client  = @saved_cs_client */ ;
/*!50003 SET character_set_results = @saved_cs_results */ ;
/*!50003 SET collation_connection  = @saved_col_connection */ ;
/*!50003 SET @saved_cs_client      = @@character_set_client */ ;
/*!50003 SET @saved_cs_results     = @@character_set_results */ ;
/*!50003 SET @saved_col_connection = @@collation_connection */ ;
/*!50003 SET character_set_client  = utf8mb4 */ ;
/*!50003 SET character_set_results = utf8mb4 */ ;
/*!50003 SET collation_connection  = utf8mb4_0900_ai_ci */ ;
/*!50003 SET @saved_sql_mode       = @@sql_mode */ ;
/*!50003 SET sql_mode              = 'ONLY_FULL_GROUP_BY,STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_ENGINE_SUBSTITUTION' */ ;
DELIMITER @@
/*!50003 CREATE*/ /*!50017 DEFINER=`root`@`localhost`*/ /*!50003 TRIGGER `client_BEFORE_UPDATE` BEFORE UPDATE ON `client` FOR EACH ROW BEGIN
    set new.client=trim(new.client);
	SET  NEW.upd_by = get_wID();
END */@@
DELIMITER ;
/*!50003 SET sql_mode              = @saved_sql_mode */ ;
/*!50003 SET character_set_client  = @saved_cs_client */ ;
/*!50003 SET character_set_results = @saved_cs_results */ ;
/*!50003 SET collation_connection  = @saved_col_connection */ ;

--
-- Table structure for table `client_has_category`
--

DROP TABLE IF EXISTS `client_has_category`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `client_has_category` (
  `client_id` int unsigned NOT NULL,
  `category_id` int unsigned NOT NULL,
  `get_date` date DEFAULT '2018-01-01',
  `archive` tinyint DEFAULT '0',
  `note` varchar(255) DEFAULT NULL,
  `create` datetime DEFAULT CURRENT_TIMESTAMP,
  `ts` datetime DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  `cr_by` int DEFAULT NULL,
  `upd_by` int DEFAULT NULL,
  `stop_date` date DEFAULT '9999-01-01',
  PRIMARY KEY (`client_id`,`category_id`),
  KEY `fk_client_has_category_category1_idx` (`category_id`),
  KEY `fk_client_has_category_client1_idx` (`client_id`),
  CONSTRAINT `fk_client_has_category_client1` FOREIGN KEY (`client_id`) REFERENCES `client` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;
/*!50003 SET @saved_cs_client      = @@character_set_client */ ;
/*!50003 SET @saved_cs_results     = @@character_set_results */ ;
/*!50003 SET @saved_col_connection = @@collation_connection */ ;
/*!50003 SET character_set_client  = utf8mb4 */ ;
/*!50003 SET character_set_results = utf8mb4 */ ;
/*!50003 SET collation_connection  = utf8mb4_0900_ai_ci */ ;
/*!50003 SET @saved_sql_mode       = @@sql_mode */ ;
/*!50003 SET sql_mode              = 'ONLY_FULL_GROUP_BY,STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_ENGINE_SUBSTITUTION' */ ;
DELIMITER @@
/*!50003 CREATE*/ /*!50017 DEFINER=`root`@`localhost`*/ /*!50003 TRIGGER `client_has_category_BEFORE_INSERT` BEFORE INSERT ON `client_has_category` FOR EACH ROW BEGIN
	SET  NEW.upd_by = get_wID();
	SET  NEW.cr_by = get_wID();
END */@@
DELIMITER ;
/*!50003 SET sql_mode              = @saved_sql_mode */ ;
/*!50003 SET character_set_client  = @saved_cs_client */ ;
/*!50003 SET character_set_results = @saved_cs_results */ ;
/*!50003 SET collation_connection  = @saved_col_connection */ ;
/*!50003 SET @saved_cs_client      = @@character_set_client */ ;
/*!50003 SET @saved_cs_results     = @@character_set_results */ ;
/*!50003 SET @saved_col_connection = @@collation_connection */ ;
/*!50003 SET character_set_client  = utf8mb4 */ ;
/*!50003 SET character_set_results = utf8mb4 */ ;
/*!50003 SET collation_connection  = utf8mb4_0900_ai_ci */ ;
/*!50003 SET @saved_sql_mode       = @@sql_mode */ ;
/*!50003 SET sql_mode              = 'ONLY_FULL_GROUP_BY,STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_ENGINE_SUBSTITUTION' */ ;
DELIMITER @@
/*!50003 CREATE*/ /*!50017 DEFINER=`root`@`localhost`*/ /*!50003 TRIGGER `client_has_category_BEFORE_UPDATE` BEFORE UPDATE ON `client_has_category` FOR EACH ROW BEGIN

	SET  NEW.upd_by = get_wID();
END */@@
DELIMITER ;
/*!50003 SET sql_mode              = @saved_sql_mode */ ;
/*!50003 SET character_set_client  = @saved_cs_client */ ;
/*!50003 SET character_set_results = @saved_cs_results */ ;
/*!50003 SET collation_connection  = @saved_col_connection */ ;

--
-- Table structure for table `complex_dep`
--

DROP TABLE IF EXISTS `complex_dep`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `complex_dep` (
  `id` int unsigned NOT NULL,
  `complex_dep` varchar(255) DEFAULT NULL,
  `note` varchar(255) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `complex_dep_has_dep`
--

DROP TABLE IF EXISTS `complex_dep_has_dep`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `complex_dep_has_dep` (
  `complex_dep_id` int unsigned NOT NULL,
  `dep_id` int unsigned NOT NULL,
  PRIMARY KEY (`complex_dep_id`,`dep_id`),
  KEY `fk_complex_dep_has_dep_dep1_idx` (`dep_id`),
  KEY `fk_complex_dep_has_dep_complex_dep1_idx` (`complex_dep_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `contracts`
--

DROP TABLE IF EXISTS `contracts`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `contracts` (
  `id` int unsigned NOT NULL AUTO_INCREMENT,
  `contracts` varchar(45) NOT NULL,
  `contracts2` varchar(45) DEFAULT NULL,
  `client_id` int NOT NULL,
  `dep_id` int unsigned NOT NULL,
  `ripso_id` int unsigned NOT NULL,
  `blocked` tinyint NOT NULL DEFAULT '0',
  `startdate` date NOT NULL COMMENT 'дата оказания услуги',
  `enddate` date NOT NULL,
  `ippsuNum` int DEFAULT NULL,
  `note` varchar(255) DEFAULT NULL,
  `create` datetime DEFAULT CURRENT_TIMESTAMP,
  `ts` datetime DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  `cr_by` int DEFAULT NULL,
  `upd_by` int DEFAULT NULL,
  `to_recheck` tinyint NOT NULL DEFAULT '0',
  `check_date` datetime DEFAULT NULL,
  `pyc_prim` varchar(255) DEFAULT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `contracts_UNIQUE` (`contracts`),
  KEY `fk_contract_client1_idx` (`client_id`),
  KEY `fk_contracts_ripso1_idx` (`ripso_id`),
  KEY `fk_contracts_dep1_idx` (`dep_id`)
) ENGINE=InnoDB AUTO_INCREMENT=2735 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;
/*!50003 SET @saved_cs_client      = @@character_set_client */ ;
/*!50003 SET @saved_cs_results     = @@character_set_results */ ;
/*!50003 SET @saved_col_connection = @@collation_connection */ ;
/*!50003 SET character_set_client  = utf8mb4 */ ;
/*!50003 SET character_set_results = utf8mb4 */ ;
/*!50003 SET collation_connection  = utf8mb4_0900_ai_ci */ ;
/*!50003 SET @saved_sql_mode       = @@sql_mode */ ;
/*!50003 SET sql_mode              = 'STRICT_TRANS_TABLES,NO_ENGINE_SUBSTITUTION' */ ;
DELIMITER @@
/*!50003 CREATE*/ /*!50017 DEFINER=`root`@`localhost`*/ /*!50003 TRIGGER `contracts_BEFORE_INSERT` BEFORE INSERT ON `contracts` FOR EACH ROW BEGIN

	SET  NEW.cr_by = get_wID();
	SET  NEW.upd_by = get_wID();
    
	IF (NEW.startdate IS NULL) THEN 
        SET NEW.startdate = now();
    END IF;
    
	IF (NEW.enddate IS NULL) THEN 
        SET NEW.enddate = now();
    END IF;
    
	IF not (NEW.contracts REGEXP "/[[:alnum:]][[:alnum:]][[:alnum:]][[:alnum:]]$") THEN 
        SET NEW.contracts = concat( NEW.contracts ,"/",year(NEW.startdate));
    END IF;
END */@@
DELIMITER ;
/*!50003 SET sql_mode              = @saved_sql_mode */ ;
/*!50003 SET character_set_client  = @saved_cs_client */ ;
/*!50003 SET character_set_results = @saved_cs_results */ ;
/*!50003 SET collation_connection  = @saved_col_connection */ ;
/*!50003 SET @saved_cs_client      = @@character_set_client */ ;
/*!50003 SET @saved_cs_results     = @@character_set_results */ ;
/*!50003 SET @saved_col_connection = @@collation_connection */ ;
/*!50003 SET character_set_client  = utf8mb4 */ ;
/*!50003 SET character_set_results = utf8mb4 */ ;
/*!50003 SET collation_connection  = utf8mb4_0900_ai_ci */ ;
/*!50003 SET @saved_sql_mode       = @@sql_mode */ ;
/*!50003 SET sql_mode              = 'STRICT_TRANS_TABLES,NO_ENGINE_SUBSTITUTION' */ ;
DELIMITER @@
/*!50003 CREATE*/ /*!50017 DEFINER=`root`@`localhost`*/ /*!50003 TRIGGER `contracts_AFTER_INSERT` AFTER INSERT ON `contracts` FOR EACH ROW BEGIN


	insert into contracts_has_serv (serv_id, contracts_id, planned ) 
		select serv_id, NEW.id, planned 
        from ripso_has_serv
		where ripso_id = NEW.ripso_id;
	
    update client set cr_dep_id = 0
		where client.id = NEW.client_id
    ;
    
END */@@
DELIMITER ;
/*!50003 SET sql_mode              = @saved_sql_mode */ ;
/*!50003 SET character_set_client  = @saved_cs_client */ ;
/*!50003 SET character_set_results = @saved_cs_results */ ;
/*!50003 SET collation_connection  = @saved_col_connection */ ;
/*!50003 SET @saved_cs_client      = @@character_set_client */ ;
/*!50003 SET @saved_cs_results     = @@character_set_results */ ;
/*!50003 SET @saved_col_connection = @@collation_connection */ ;
/*!50003 SET character_set_client  = utf8mb4 */ ;
/*!50003 SET character_set_results = utf8mb4 */ ;
/*!50003 SET collation_connection  = utf8mb4_0900_ai_ci */ ;
/*!50003 SET @saved_sql_mode       = @@sql_mode */ ;
/*!50003 SET sql_mode              = 'STRICT_TRANS_TABLES,NO_ENGINE_SUBSTITUTION' */ ;
DELIMITER @@
/*!50003 CREATE*/ /*!50017 DEFINER=`root`@`localhost`*/ /*!50003 TRIGGER `contracts_BEFORE_UPDATE` BEFORE UPDATE ON `contracts` FOR EACH ROW BEGIN

SET  NEW.upd_by = get_wID();
    
	IF (NEW.startdate IS NULL) THEN 
        SET NEW.startdate = now();
    END IF;
    
	IF (NEW.enddate IS NULL) THEN 
        SET NEW.enddate = now();
    END IF;
    
	IF (NEW.contracts REGEXP "/20[[:digit:]][[:digit:]]$") THEN 
		SET NEW.contracts = NEW.contracts;
	else
        SET NEW.contracts = concat( NEW.contracts ,"/",year(NEW.startdate));
    END IF;
END */@@
DELIMITER ;
/*!50003 SET sql_mode              = @saved_sql_mode */ ;
/*!50003 SET character_set_client  = @saved_cs_client */ ;
/*!50003 SET character_set_results = @saved_cs_results */ ;
/*!50003 SET collation_connection  = @saved_col_connection */ ;

--
-- Table structure for table `contracts_has_serv`
--

DROP TABLE IF EXISTS `contracts_has_serv`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `contracts_has_serv` (
  `serv_id` int unsigned NOT NULL,
  `contracts_id` int unsigned NOT NULL,
  `planned` int DEFAULT '0',
  `filled` int DEFAULT '0',
  `note` varchar(255) DEFAULT NULL,
  `archive` tinyint DEFAULT '0',
  `create` datetime DEFAULT CURRENT_TIMESTAMP,
  `ts` datetime DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  `cr_by` int DEFAULT NULL,
  `upd_by` int DEFAULT NULL,
  `to_recheck` tinyint NOT NULL DEFAULT '0',
  `check_date` datetime DEFAULT CURRENT_TIMESTAMP,
  `filled_old` int DEFAULT '0',
  PRIMARY KEY (`serv_id`,`contracts_id`),
  KEY `fk_contracts_has_serv_contracts1_idx` (`contracts_id`),
  CONSTRAINT `fk_contracts_has_serv_serv1` FOREIGN KEY (`serv_id`) REFERENCES `serv` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;
/*!50003 SET @saved_cs_client      = @@character_set_client */ ;
/*!50003 SET @saved_cs_results     = @@character_set_results */ ;
/*!50003 SET @saved_col_connection = @@collation_connection */ ;
/*!50003 SET character_set_client  = utf8mb4 */ ;
/*!50003 SET character_set_results = utf8mb4 */ ;
/*!50003 SET collation_connection  = utf8mb4_0900_ai_ci */ ;
/*!50003 SET @saved_sql_mode       = @@sql_mode */ ;
/*!50003 SET sql_mode              = 'ONLY_FULL_GROUP_BY,STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_ENGINE_SUBSTITUTION' */ ;
DELIMITER @@
/*!50003 CREATE*/ /*!50017 DEFINER=`root`@`localhost`*/ /*!50003 TRIGGER `contracts_has_serv_BEFORE_INSERT` BEFORE INSERT ON `contracts_has_serv` FOR EACH ROW BEGIN
	SET  NEW.cr_by = get_wID();
	SET  NEW.upd_by = get_wID();
END */@@
DELIMITER ;
/*!50003 SET sql_mode              = @saved_sql_mode */ ;
/*!50003 SET character_set_client  = @saved_cs_client */ ;
/*!50003 SET character_set_results = @saved_cs_results */ ;
/*!50003 SET collation_connection  = @saved_col_connection */ ;
/*!50003 SET @saved_cs_client      = @@character_set_client */ ;
/*!50003 SET @saved_cs_results     = @@character_set_results */ ;
/*!50003 SET @saved_col_connection = @@collation_connection */ ;
/*!50003 SET character_set_client  = utf8mb4 */ ;
/*!50003 SET character_set_results = utf8mb4 */ ;
/*!50003 SET collation_connection  = utf8mb4_0900_ai_ci */ ;
/*!50003 SET @saved_sql_mode       = @@sql_mode */ ;
/*!50003 SET sql_mode              = 'ONLY_FULL_GROUP_BY,STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_ENGINE_SUBSTITUTION' */ ;
DELIMITER @@
/*!50003 CREATE*/ /*!50017 DEFINER=`root`@`localhost`*/ /*!50003 TRIGGER `contracts_has_serv_BEFORE_UPDATE` BEFORE UPDATE ON `contracts_has_serv` FOR EACH ROW BEGIN
	SET  NEW.upd_by = get_wID();
END */@@
DELIMITER ;
/*!50003 SET sql_mode              = @saved_sql_mode */ ;
/*!50003 SET character_set_client  = @saved_cs_client */ ;
/*!50003 SET character_set_results = @saved_cs_results */ ;
/*!50003 SET collation_connection  = @saved_col_connection */ ;

--
-- Temporary view structure for view `cr_by`
--

DROP TABLE IF EXISTS `cr_by`;
/*!50001 DROP VIEW IF EXISTS `cr_by`*/;
SET @saved_cs_client     = @@character_set_client;
/*!50503 SET character_set_client = utf8mb4 */;
/*!50001 CREATE VIEW `cr_by` AS SELECT 
 1 AS `id`,
 1 AS `cr_by`,
 1 AS `user`,
 1 AS `note`,
 1 AS `role_id`,
 1 AS `dep_id`,
 1 AS `archive`*/;
SET character_set_client = @saved_cs_client;

--
-- Temporary view structure for view `cr_dep`
--

DROP TABLE IF EXISTS `cr_dep`;
/*!50001 DROP VIEW IF EXISTS `cr_dep`*/;
SET @saved_cs_client     = @@character_set_client;
/*!50503 SET character_set_client = utf8mb4 */;
/*!50001 CREATE VIEW `cr_dep` AS SELECT 
 1 AS `id`,
 1 AS `cr_dep`*/;
SET character_set_client = @saved_cs_client;

--
-- Temporary view structure for view `cr_dep_id`
--

DROP TABLE IF EXISTS `cr_dep_id`;
/*!50001 DROP VIEW IF EXISTS `cr_dep_id`*/;
SET @saved_cs_client     = @@character_set_client;
/*!50503 SET character_set_client = utf8mb4 */;
/*!50001 CREATE VIEW `cr_dep_id` AS SELECT 
 1 AS `id`,
 1 AS `dep`,
 1 AS `dep_full_name`,
 1 AS `dep_puname`,
 1 AS `note`,
 1 AS `archive`,
 1 AS `complex_dep_id`*/;
SET character_set_client = @saved_cs_client;

--
-- Table structure for table `data_log`
--

DROP TABLE IF EXISTS `data_log`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `data_log` (
  `id` int NOT NULL,
  `message` varchar(255) DEFAULT NULL,
  `date` datetime NOT NULL,
  `note` varchar(255) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `dep`
--

DROP TABLE IF EXISTS `dep`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `dep` (
  `id` int unsigned NOT NULL AUTO_INCREMENT,
  `dep` varchar(145) NOT NULL,
  `dep_full_name` varchar(255) DEFAULT NULL,
  `dep_puname` varchar(255) DEFAULT NULL,
  `note` varchar(255) DEFAULT NULL,
  `archive` tinyint DEFAULT '0',
  `complex_dep_id` int unsigned DEFAULT '0',
  PRIMARY KEY (`id`),
  UNIQUE KEY `dep_UNIQUE` (`dep`)
) ENGINE=InnoDB AUTO_INCREMENT=49 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci COMMENT='Departments';
/*!40101 SET character_set_client = @saved_cs_client */;
/*!50003 SET @saved_cs_client      = @@character_set_client */ ;
/*!50003 SET @saved_cs_results     = @@character_set_results */ ;
/*!50003 SET @saved_col_connection = @@collation_connection */ ;
/*!50003 SET character_set_client  = utf8mb4 */ ;
/*!50003 SET character_set_results = utf8mb4 */ ;
/*!50003 SET collation_connection  = utf8mb4_0900_ai_ci */ ;
/*!50003 SET @saved_sql_mode       = @@sql_mode */ ;
/*!50003 SET sql_mode              = 'ONLY_FULL_GROUP_BY,STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_ENGINE_SUBSTITUTION' */ ;
DELIMITER @@
/*!50003 CREATE*/ /*!50017 DEFINER=`root`@`localhost`*/ /*!50003 TRIGGER `dep_AFTER_INSERT` AFTER INSERT ON `dep` FOR EACH ROW BEGIN
	 insert into complex_dep_has_dep (complex_dep_id, dep_id)
     values(1 , NEW.id);
END */@@
DELIMITER ;
/*!50003 SET sql_mode              = @saved_sql_mode */ ;
/*!50003 SET character_set_client  = @saved_cs_client */ ;
/*!50003 SET character_set_results = @saved_cs_results */ ;
/*!50003 SET collation_connection  = @saved_col_connection */ ;

--
-- Temporary view structure for view `dep_has_client_by_contr`
--

DROP TABLE IF EXISTS `dep_has_client_by_contr`;
/*!50001 DROP VIEW IF EXISTS `dep_has_client_by_contr`*/;
SET @saved_cs_client     = @@character_set_client;
/*!50503 SET character_set_client = utf8mb4 */;
/*!50001 CREATE VIEW `dep_has_client_by_contr` AS SELECT 
 1 AS `id`,
 1 AS `client`,
 1 AS `client_short`,
 1 AS `clientDeath`,
 1 AS `clientbirth`,
 1 AS `ESRN`,
 1 AS `note`,
 1 AS `phone`,
 1 AS `snils`,
 1 AS `curator`,
 1 AS `create`,
 1 AS `ts`,
 1 AS `cr_by`,
 1 AS `upd_by`,
 1 AS `cr_dep_id`*/;
SET character_set_client = @saved_cs_client;

--
-- Temporary view structure for view `dep_has_client_by_ripso`
--

DROP TABLE IF EXISTS `dep_has_client_by_ripso`;
/*!50001 DROP VIEW IF EXISTS `dep_has_client_by_ripso`*/;
SET @saved_cs_client     = @@character_set_client;
/*!50503 SET character_set_client = utf8mb4 */;
/*!50001 CREATE VIEW `dep_has_client_by_ripso` AS SELECT 
 1 AS `id`,
 1 AS `client`,
 1 AS `client_short`,
 1 AS `clientDeath`,
 1 AS `clientbirth`,
 1 AS `ESRN`,
 1 AS `note`,
 1 AS `phone`,
 1 AS `snils`,
 1 AS `curator`,
 1 AS `create`,
 1 AS `ts`,
 1 AS `cr_by`,
 1 AS `upd_by`,
 1 AS `cr_dep_id`*/;
SET character_set_client = @saved_cs_client;

--
-- Temporary view structure for view `dep_has_main`
--

DROP TABLE IF EXISTS `dep_has_main`;
/*!50001 DROP VIEW IF EXISTS `dep_has_main`*/;
SET @saved_cs_client     = @@character_set_client;
/*!50503 SET character_set_client = utf8mb4 */;
/*!50001 CREATE VIEW `dep_has_main` AS SELECT 
 1 AS `id`,
 1 AS `contracts_id`,
 1 AS `dep_id`,
 1 AS `client_id`,
 1 AS `serv_id`,
 1 AS `dep_has_worker_id`,
 1 AS `worker_id`,
 1 AS `vdate`,
 1 AS `quantity`,
 1 AS `note`,
 1 AS `create`,
 1 AS `ts`,
 1 AS `cr_by`,
 1 AS `upd_by`,
 1 AS `reported`,
 1 AS `wdate`,
 1 AS `overdid`,
 1 AS `prev_quantity`*/;
SET character_set_client = @saved_cs_client;

--
-- Table structure for table `dep_has_ripso`
--

DROP TABLE IF EXISTS `dep_has_ripso`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `dep_has_ripso` (
  `dep_id` int unsigned NOT NULL,
  `ripso_id` int unsigned NOT NULL,
  PRIMARY KEY (`dep_id`,`ripso_id`),
  KEY `fk_dep_has_ripso_ripso1_idx` (`ripso_id`),
  KEY `fk_dep_has_ripso_dep1_idx` (`dep_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Temporary view structure for view `dep_has_serv`
--

DROP TABLE IF EXISTS `dep_has_serv`;
/*!50001 DROP VIEW IF EXISTS `dep_has_serv`*/;
SET @saved_cs_client     = @@character_set_client;
/*!50503 SET character_set_client = utf8mb4 */;
/*!50001 CREATE VIEW `dep_has_serv` AS SELECT 
 1 AS `id`,
 1 AS `tnum`,
 1 AS `serv`,
 1 AS `year`,
 1 AS `sub_serv`,
 1 AS `sub_serv_str`,
 1 AS `price`,
 1 AS `price2`,
 1 AS `price3`,
 1 AS `archive`,
 1 AS `total`,
 1 AS `acronym`,
 1 AS `workload`,
 1 AS `content`*/;
SET character_set_client = @saved_cs_client;

--
-- Table structure for table `dep_has_worker`
--

DROP TABLE IF EXISTS `dep_has_worker`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `dep_has_worker` (
  `id` int unsigned NOT NULL AUTO_INCREMENT,
  `dep_has_worker` varchar(255) NOT NULL,
  `worker_id` int unsigned NOT NULL,
  `dep_id` int unsigned NOT NULL,
  `job_id` int unsigned NOT NULL,
  `note` varchar(145) DEFAULT NULL,
  `archive` tinyint DEFAULT '0',
  `from` date DEFAULT '2000-01-01',
  `till` date DEFAULT '2050-01-01',
  `role_id` int unsigned NOT NULL DEFAULT '1',
  `api_key` varchar(64) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci DEFAULT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `wid_UNIQUE` (`id`),
  UNIQUE KEY `dep_has_worker_UNIQUE` (`dep_has_worker`),
  KEY `fk_dep_has_worker_dep1_idx` (`dep_id`),
  KEY `fk_dep_has_worker_job1_idx` (`job_id`),
  KEY `fk_dep_has_worker_role1_idx` (`role_id`),
  KEY `fk_dep_has_worker_worker1` (`worker_id`),
  CONSTRAINT `fk_dep_has_worker_worker1` FOREIGN KEY (`worker_id`) REFERENCES `worker` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=228 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;
/*!50003 SET @saved_cs_client      = @@character_set_client */ ;
/*!50003 SET @saved_cs_results     = @@character_set_results */ ;
/*!50003 SET @saved_col_connection = @@collation_connection */ ;
/*!50003 SET character_set_client  = utf8mb4 */ ;
/*!50003 SET character_set_results = utf8mb4 */ ;
/*!50003 SET collation_connection  = utf8mb4_0900_ai_ci */ ;
/*!50003 SET @saved_sql_mode       = @@sql_mode */ ;
/*!50003 SET sql_mode              = 'STRICT_TRANS_TABLES,NO_ENGINE_SUBSTITUTION' */ ;
DELIMITER @@
/*!50003 CREATE*/ /*!50017 DEFINER=`root`@`localhost`*/ /*!50003 TRIGGER `dep_has_worker_BEFORE_INSERT` BEFORE INSERT ON `dep_has_worker` FOR EACH ROW begin
	
    DECLARE cuser CHAR(32);
    DECLARE crole int;
   
	if length( coalesce( new.dep_has_worker, "") ) = 0 then
		set new.dep_has_worker = (select concat( worker, " " , job, " ", dep)  
				from worker w join  job j join  dep d 
				where w.id = NEW.worker_id and j.id = NEW.job_id and  d.id = NEW.dep_id);
	end if;
	 
	set NEW.api_key=concat( floor(RAND()*(1000000000000000000-100000000000000000)+100000000000000000), uuid());
	
	SET cuser := SUBSTRING_INDEX(current_user(),'@',1);
	set crole := (select dhw.role_id  from dep_has_worker dhw inner join  worker w  on 
		w.id = dhw.worker_id 
		where w.`user` = cuser
		order by dhw.role_id desc 
		limit 1);
	
		
    if  cuser = 'root' then
        set crole = crole;
    elseif  crole is null then
		set new.role_id = 1;
		-- throw error?
	elseif ( crole = 7 or crole = 8 ) then
	    -- admin and part admin
		set crole = crole;
	elseif (new.role_id > crole) then
		set new.role_id = crole - 1;
	end if;
END */@@
DELIMITER ;
/*!50003 SET sql_mode              = @saved_sql_mode */ ;
/*!50003 SET character_set_client  = @saved_cs_client */ ;
/*!50003 SET character_set_results = @saved_cs_results */ ;
/*!50003 SET collation_connection  = @saved_col_connection */ ;
/*!50003 SET @saved_cs_client      = @@character_set_client */ ;
/*!50003 SET @saved_cs_results     = @@character_set_results */ ;
/*!50003 SET @saved_col_connection = @@collation_connection */ ;
/*!50003 SET character_set_client  = utf8mb4 */ ;
/*!50003 SET character_set_results = utf8mb4 */ ;
/*!50003 SET collation_connection  = utf8mb4_0900_ai_ci */ ;
/*!50003 SET @saved_sql_mode       = @@sql_mode */ ;
/*!50003 SET sql_mode              = 'STRICT_TRANS_TABLES,NO_ENGINE_SUBSTITUTION' */ ;
DELIMITER @@
/*!50003 CREATE*/ /*!50017 DEFINER=`root`@`localhost`*/ /*!50003 TRIGGER `dep_has_worker_BEFORE_UPDATE` BEFORE UPDATE ON `dep_has_worker` FOR EACH ROW BEGIN	
    DECLARE cuser CHAR(32);
    DECLARE crole int;
	   
	if length( coalesce( new.dep_has_worker, "") ) = 0 then
		set new.dep_has_worker = (select concat( worker, " " , job, " ", dep)  
							from worker w join  job j join  dep d 
							where w.id = NEW.worker_id and j.id = NEW.job_id and  d.id = NEW.dep_id);
	end if;

 
	 if new.role_id != old.role_id then
	 	SET cuser := SUBSTRING_INDEX(current_user(),'@',1);
		set crole := (select dhw.role_id  from dep_has_worker dhw inner join  worker w  on 
			w.id = dhw.worker_id 
			where w.`user` = cuser
			order by dhw.role_id desc 
			limit 1);
		
		if  cuser = 'root' then
			set crole = crole;
		elseif  crole is null then
			set new.role_id = 1;
			-- throw error?
		elseif ( crole = 7 or crole = 8 ) then
		    -- admin and part admin
			set crole = crole;
		elseif (new.role_id > crole) then
			set new.role_id = crole - 1;
		end if;
	 end if;
 
END */@@
DELIMITER ;
/*!50003 SET sql_mode              = @saved_sql_mode */ ;
/*!50003 SET character_set_client  = @saved_cs_client */ ;
/*!50003 SET character_set_results = @saved_cs_results */ ;
/*!50003 SET collation_connection  = @saved_col_connection */ ;

--
-- Temporary view structure for view `dep_total_serv`
--

DROP TABLE IF EXISTS `dep_total_serv`;
/*!50001 DROP VIEW IF EXISTS `dep_total_serv`*/;
SET @saved_cs_client     = @@character_set_client;
/*!50503 SET character_set_client = utf8mb4 */;
/*!50001 CREATE VIEW `dep_total_serv` AS SELECT 
 1 AS `contracts_id`,
 1 AS `dep_id`,
 1 AS `serv_id`,
 1 AS `worker_id`,
 1 AS `SUM(quantity)`,
 1 AS `MONTH(vdate)`,
 1 AS `YEAR(vdate)`*/;
SET character_set_client = @saved_cs_client;

--
-- Temporary view structure for view `dep_total_supserv1`
--

DROP TABLE IF EXISTS `dep_total_supserv1`;
/*!50001 DROP VIEW IF EXISTS `dep_total_supserv1`*/;
SET @saved_cs_client     = @@character_set_client;
/*!50503 SET character_set_client = utf8mb4 */;
/*!50001 CREATE VIEW `dep_total_supserv1` AS SELECT 
 1 AS `contracts_id`,
 1 AS `dep_id`,
 1 AS `sub_serv`,
 1 AS `worker_id`,
 1 AS `SUM(quantity)`,
 1 AS `mnth1`,
 1 AS `year1`*/;
SET character_set_client = @saved_cs_client;

--
-- Table structure for table `dhw_has_client`
--

DROP TABLE IF EXISTS `dhw_has_client`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `dhw_has_client` (
  `dhw_id` int unsigned NOT NULL COMMENT '// TODO: check worker otd of  manager otd',
  `client_id` int unsigned NOT NULL,
  `note` varchar(256) DEFAULT NULL COMMENT 'Note',
  KEY `dhw_has_client_dhw_id_IDX` (`dhw_id`) USING BTREE,
  KEY `dhw_has_client_FK_1` (`client_id`),
  CONSTRAINT `dhw_has_client_FK` FOREIGN KEY (`dhw_id`) REFERENCES `dep_has_worker` (`id`) ON DELETE CASCADE ON UPDATE CASCADE,
  CONSTRAINT `dhw_has_client_FK_1` FOREIGN KEY (`client_id`) REFERENCES `client` (`id`) ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Temporary view structure for view `fioofdepbyserv`
--

DROP TABLE IF EXISTS `fioofdepbyserv`;
/*!50001 DROP VIEW IF EXISTS `fioofdepbyserv`*/;
SET @saved_cs_client     = @@character_set_client;
/*!50503 SET character_set_client = utf8mb4 */;
/*!50001 CREATE VIEW `fioofdepbyserv` AS SELECT 
 1 AS `client`,
 1 AS `client_short`,
 1 AS `clientbirth`,
 1 AS `ESRN`,
 1 AS `clientDeath`*/;
SET character_set_client = @saved_cs_client;

--
-- Temporary view structure for view `fioofdepbyset`
--

DROP TABLE IF EXISTS `fioofdepbyset`;
/*!50001 DROP VIEW IF EXISTS `fioofdepbyset`*/;
SET @saved_cs_client     = @@character_set_client;
/*!50503 SET character_set_client = utf8mb4 */;
/*!50001 CREATE VIEW `fioofdepbyset` AS SELECT 
 1 AS `client`,
 1 AS `client_short`,
 1 AS `clientbirth`,
 1 AS `ESRN`,
 1 AS `clientDeath`*/;
SET character_set_client = @saved_cs_client;

--
-- Table structure for table `holiday`
--

DROP TABLE IF EXISTS `holiday`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `holiday` (
  `holiday` date NOT NULL,
  `note` varchar(255) DEFAULT NULL,
  PRIMARY KEY (`holiday`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `invoice`
--

DROP TABLE IF EXISTS `invoice`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `invoice` (
  `id` int unsigned NOT NULL AUTO_INCREMENT,
  `client_id` int unsigned NOT NULL,
  `give_date` date DEFAULT NULL,
  `money` decimal(10,2) DEFAULT NULL,
  `filled` decimal(10,2) DEFAULT NULL,
  `note` varchar(255) DEFAULT NULL,
  `dep_id` int unsigned NOT NULL,
  `create` datetime DEFAULT CURRENT_TIMESTAMP,
  `ts` datetime DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  `cr_by` int DEFAULT NULL,
  `upd_by` int DEFAULT NULL,
  `dismissed` tinyint DEFAULT '0',
  `pay_period_end` date DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `fk_invoice_client1_idx` (`client_id`),
  KEY `fk_invoice_dep1_idx` (`dep_id`),
  CONSTRAINT `fk_invoice_client1` FOREIGN KEY (`client_id`) REFERENCES `client` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;
/*!50003 SET @saved_cs_client      = @@character_set_client */ ;
/*!50003 SET @saved_cs_results     = @@character_set_results */ ;
/*!50003 SET @saved_col_connection = @@collation_connection */ ;
/*!50003 SET character_set_client  = utf8mb4 */ ;
/*!50003 SET character_set_results = utf8mb4 */ ;
/*!50003 SET collation_connection  = utf8mb4_0900_ai_ci */ ;
/*!50003 SET @saved_sql_mode       = @@sql_mode */ ;
/*!50003 SET sql_mode              = 'ONLY_FULL_GROUP_BY,STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_ENGINE_SUBSTITUTION' */ ;
DELIMITER @@
/*!50003 CREATE*/ /*!50017 DEFINER=`root`@`localhost`*/ /*!50003 TRIGGER `invoice_BEFORE_INSERT` BEFORE INSERT ON `invoice` FOR EACH ROW BEGIN

SET  NEW.cr_by = get_wID();
SET  NEW.upd_by = get_wID();
END */@@
DELIMITER ;
/*!50003 SET sql_mode              = @saved_sql_mode */ ;
/*!50003 SET character_set_client  = @saved_cs_client */ ;
/*!50003 SET character_set_results = @saved_cs_results */ ;
/*!50003 SET collation_connection  = @saved_col_connection */ ;
/*!50003 SET @saved_cs_client      = @@character_set_client */ ;
/*!50003 SET @saved_cs_results     = @@character_set_results */ ;
/*!50003 SET @saved_col_connection = @@collation_connection */ ;
/*!50003 SET character_set_client  = utf8mb4 */ ;
/*!50003 SET character_set_results = utf8mb4 */ ;
/*!50003 SET collation_connection  = utf8mb4_0900_ai_ci */ ;
/*!50003 SET @saved_sql_mode       = @@sql_mode */ ;
/*!50003 SET sql_mode              = 'ONLY_FULL_GROUP_BY,STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_ENGINE_SUBSTITUTION' */ ;
DELIMITER @@
/*!50003 CREATE*/ /*!50017 DEFINER=`root`@`localhost`*/ /*!50003 TRIGGER `invoice_BEFORE_UPDATE` BEFORE UPDATE ON `invoice` FOR EACH ROW BEGIN

SET  NEW.upd_by = get_wID(CURRENT_USER);
END */@@
DELIMITER ;
/*!50003 SET sql_mode              = @saved_sql_mode */ ;
/*!50003 SET character_set_client  = @saved_cs_client */ ;
/*!50003 SET character_set_results = @saved_cs_results */ ;
/*!50003 SET collation_connection  = @saved_col_connection */ ;

--
-- Table structure for table `invoice_has_payment`
--

DROP TABLE IF EXISTS `invoice_has_payment`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `invoice_has_payment` (
  `invoice_id` int unsigned NOT NULL,
  `payment_id` int unsigned NOT NULL,
  PRIMARY KEY (`invoice_id`,`payment_id`),
  KEY `fk_invoice_has_payment_payment1_idx` (`payment_id`),
  KEY `fk_invoice_has_payment_invoice1_idx` (`invoice_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;
/*!50003 SET @saved_cs_client      = @@character_set_client */ ;
/*!50003 SET @saved_cs_results     = @@character_set_results */ ;
/*!50003 SET @saved_col_connection = @@collation_connection */ ;
/*!50003 SET character_set_client  = utf8mb4 */ ;
/*!50003 SET character_set_results = utf8mb4 */ ;
/*!50003 SET collation_connection  = utf8mb4_0900_ai_ci */ ;
/*!50003 SET @saved_sql_mode       = @@sql_mode */ ;
/*!50003 SET sql_mode              = 'ONLY_FULL_GROUP_BY,STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_ENGINE_SUBSTITUTION' */ ;
DELIMITER @@
/*!50003 CREATE*/ /*!50017 DEFINER=`root`@`localhost`*/ /*!50003 TRIGGER `invoice_has_payment_BEFORE_INSERT` BEFORE INSERT ON `invoice_has_payment` FOR EACH ROW BEGIN
declare inv int;
declare pay int;
# check duplicates
END */@@
DELIMITER ;
/*!50003 SET sql_mode              = @saved_sql_mode */ ;
/*!50003 SET character_set_client  = @saved_cs_client */ ;
/*!50003 SET character_set_results = @saved_cs_results */ ;
/*!50003 SET collation_connection  = @saved_col_connection */ ;

--
-- Table structure for table `job`
--

DROP TABLE IF EXISTS `job`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `job` (
  `id` int unsigned NOT NULL AUTO_INCREMENT,
  `job` varchar(255) DEFAULT NULL,
  `note` varchar(45) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=16 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `job_has_jobgroup`
--

DROP TABLE IF EXISTS `job_has_jobgroup`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `job_has_jobgroup` (
  `job_id` int unsigned NOT NULL,
  `jobGroup_id` int NOT NULL,
  PRIMARY KEY (`job_id`,`jobGroup_id`),
  KEY `fk_job_has_jobGroup_jobGroup1_idx` (`jobGroup_id`),
  KEY `fk_job_has_jobGroup_job1_idx` (`job_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `job_has_serv`
--

DROP TABLE IF EXISTS `job_has_serv`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `job_has_serv` (
  `job_id` int unsigned NOT NULL,
  `serv_id` int unsigned NOT NULL,
  PRIMARY KEY (`job_id`,`serv_id`),
  KEY `fk_job_has_serv_serv1_idx` (`serv_id`),
  KEY `fk_job_has_serv_job1_idx` (`job_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `jobgroup`
--

DROP TABLE IF EXISTS `jobgroup`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `jobgroup` (
  `id` int NOT NULL,
  `jobGroup` varchar(255) DEFAULT NULL,
  `note` varchar(1024) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Temporary view structure for view `last_used_workers`
--

DROP TABLE IF EXISTS `last_used_workers`;
/*!50001 DROP VIEW IF EXISTS `last_used_workers`*/;
SET @saved_cs_client     = @@character_set_client;
/*!50503 SET character_set_client = utf8mb4 */;
/*!50001 CREATE VIEW `last_used_workers` AS SELECT 
 1 AS `id`,
 1 AS `worker`*/;
SET character_set_client = @saved_cs_client;

--
-- Table structure for table `live_min`
--

DROP TABLE IF EXISTS `live_min`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `live_min` (
  `id` int NOT NULL AUTO_INCREMENT,
  `lmdate` date NOT NULL COMMENT 'Используется с ',
  `live_min_p` decimal(10,2) NOT NULL,
  `live_min_w` decimal(10,2) NOT NULL,
  `live_min_c` decimal(10,2) NOT NULL,
  `live_min_all` decimal(10,2) DEFAULT NULL,
  `post` varchar(255) DEFAULT NULL,
  `post_date` date DEFAULT NULL,
  `create` datetime DEFAULT CURRENT_TIMESTAMP,
  `ts` datetime DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  `cr_by` int DEFAULT NULL,
  `upd_by` int DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=24 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;
/*!50003 SET @saved_cs_client      = @@character_set_client */ ;
/*!50003 SET @saved_cs_results     = @@character_set_results */ ;
/*!50003 SET @saved_col_connection = @@collation_connection */ ;
/*!50003 SET character_set_client  = utf8mb4 */ ;
/*!50003 SET character_set_results = utf8mb4 */ ;
/*!50003 SET collation_connection  = utf8mb4_0900_ai_ci */ ;
/*!50003 SET @saved_sql_mode       = @@sql_mode */ ;
/*!50003 SET sql_mode              = 'STRICT_TRANS_TABLES,NO_ENGINE_SUBSTITUTION' */ ;
DELIMITER @@
/*!50003 CREATE*/ /*!50017 DEFINER=`root`@`localhost`*/ /*!50003 TRIGGER `live_min_BEFORE_INSERT` BEFORE INSERT ON `live_min` FOR EACH ROW BEGIN
	SET  NEW.cr_by = get_wID();
	SET  NEW.upd_by = get_wID();
END */@@
DELIMITER ;
/*!50003 SET sql_mode              = @saved_sql_mode */ ;
/*!50003 SET character_set_client  = @saved_cs_client */ ;
/*!50003 SET character_set_results = @saved_cs_results */ ;
/*!50003 SET collation_connection  = @saved_col_connection */ ;
/*!50003 SET @saved_cs_client      = @@character_set_client */ ;
/*!50003 SET @saved_cs_results     = @@character_set_results */ ;
/*!50003 SET @saved_col_connection = @@collation_connection */ ;
/*!50003 SET character_set_client  = utf8mb4 */ ;
/*!50003 SET character_set_results = utf8mb4 */ ;
/*!50003 SET collation_connection  = utf8mb4_0900_ai_ci */ ;
/*!50003 SET @saved_sql_mode       = @@sql_mode */ ;
/*!50003 SET sql_mode              = 'STRICT_TRANS_TABLES,NO_ENGINE_SUBSTITUTION' */ ;
DELIMITER @@
/*!50003 CREATE*/ /*!50017 DEFINER=`root`@`localhost`*/ /*!50003 TRIGGER `live_min_BEFORE_UPDATE` BEFORE UPDATE ON `live_min` FOR EACH ROW BEGIN
	SET  NEW.upd_by = get_wID();
END */@@
DELIMITER ;
/*!50003 SET sql_mode              = @saved_sql_mode */ ;
/*!50003 SET character_set_client  = @saved_cs_client */ ;
/*!50003 SET character_set_results = @saved_cs_results */ ;
/*!50003 SET collation_connection  = @saved_col_connection */ ;

--
-- Table structure for table `log_edit_archive`
--

DROP TABLE IF EXISTS `log_edit_archive`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `log_edit_archive` (
  `id` int NOT NULL AUTO_INCREMENT,
  `worker_id` int unsigned NOT NULL,
  `table` varchar(45) DEFAULT NULL,
  `table_id` varchar(45) DEFAULT NULL,
  `column` int DEFAULT NULL,
  `old_val` varchar(255) DEFAULT NULL,
  `new_val` varchar(255) DEFAULT NULL,
  `ts` datetime NOT NULL DEFAULT CURRENT_TIMESTAMP,
  `note` varchar(255) DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `fk_log_edit_archive_worker1_idx` (`worker_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `main`
--

DROP TABLE IF EXISTS `main`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `main` (
  `id` bigint unsigned NOT NULL AUTO_INCREMENT,
  `contracts_id` int unsigned NOT NULL,
  `dep_id` int unsigned NOT NULL,
  `client_id` int unsigned NOT NULL,
  `serv_id` int unsigned NOT NULL,
  `dep_has_worker_id` int unsigned NOT NULL DEFAULT '0',
  `worker_id` int unsigned NOT NULL,
  `vdate` date NOT NULL COMMENT 'дата оказания услуги',
  `quantity` int DEFAULT '0' COMMENT 'Количество услуг',
  `note` varchar(255) DEFAULT NULL,
  `create` datetime DEFAULT CURRENT_TIMESTAMP,
  `ts` datetime DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  `cr_by` int DEFAULT NULL,
  `upd_by` int DEFAULT NULL,
  `reported` tinyint DEFAULT '0',
  `wdate` datetime DEFAULT NULL COMMENT 'дата ввода услуги',
  `overdid` tinyint DEFAULT '0',
  `prev_quantity` int(11) unsigned zerofill DEFAULT '00000000000',
  PRIMARY KEY (`id`),
  KEY `fk_main2_serv1_idx` (`serv_id`),
  KEY `fk_main2_dep1_idx` (`dep_id`),
  KEY `fk_main2_client1_idx` (`client_id`),
  KEY `fk_main2_contracts1_idx` (`contracts_id`),
  KEY `fk_main2_worker1_idx` (`worker_id`),
  KEY `fk_main2_dep_has_worker1_idx` (`dep_has_worker_id`),
  KEY `vdate_` (`vdate`),
  KEY `ts` (`ts`) /*!80000 INVISIBLE */,
  KEY `upd_by` (`upd_by`),
  KEY `create_by` (`cr_by`),
  CONSTRAINT `fk_main2_contracts` FOREIGN KEY (`contracts_id`) REFERENCES `contracts` (`id`),
  CONSTRAINT `fk_main2_dep` FOREIGN KEY (`dep_id`) REFERENCES `dep` (`id`),
  CONSTRAINT `fk_main2_serv1` FOREIGN KEY (`serv_id`) REFERENCES `serv` (`id`),
  CONSTRAINT `worker` FOREIGN KEY (`worker_id`) REFERENCES `worker` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=175276 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci COMMENT='main table';
/*!40101 SET character_set_client = @saved_cs_client */;
/*!50003 SET @saved_cs_client      = @@character_set_client */ ;
/*!50003 SET @saved_cs_results     = @@character_set_results */ ;
/*!50003 SET @saved_col_connection = @@collation_connection */ ;
/*!50003 SET character_set_client  = utf8mb4 */ ;
/*!50003 SET character_set_results = utf8mb4 */ ;
/*!50003 SET collation_connection  = utf8mb4_0900_ai_ci */ ;
/*!50003 SET @saved_sql_mode       = @@sql_mode */ ;
/*!50003 SET sql_mode              = 'STRICT_TRANS_TABLES,NO_ENGINE_SUBSTITUTION' */ ;
DELIMITER @@
/*!50003 CREATE*/ /*!50017 DEFINER=`root`@`localhost`*/ /*!50003 TRIGGER `main_BEFORE_INSERT` BEFORE INSERT ON `main` FOR EACH ROW BEGIN
  declare ovdid int default 0;
  declare planned int default 0;
  declare filled int default 0;
 
 
select s.planned - s.filled - new.quantity, s.planned , s.filled  into  ovdid, planned , filled   from  contracts_has_serv s where
  s.contracts_id = new.contracts_id  and
  s.serv_id =  new.serv_id ;
  
	if (ovdid < 0) then
		set @last_message_text = CONCAT ( "ошибка: эта услуга переполнена, осталось ", planned - filled, " услуг" );
		SIGNAL SQLSTATE '45000'
		SET MESSAGE_TEXT = @last_message_text;
	end if;


    if coalesce(New.worker_id, 0) = 0 then
		set new.worker_id = (select worker_id from dep_has_worker where id = new.dep_has_worker_id );
    end if;
    
	SET NEW.prev_quantity=0;
	SET  NEW.cr_by = get_wID();
	SET  NEW.upd_by = get_wID();
END */@@
DELIMITER ;
/*!50003 SET sql_mode              = @saved_sql_mode */ ;
/*!50003 SET character_set_client  = @saved_cs_client */ ;
/*!50003 SET character_set_results = @saved_cs_results */ ;
/*!50003 SET collation_connection  = @saved_col_connection */ ;
/*!50003 SET @saved_cs_client      = @@character_set_client */ ;
/*!50003 SET @saved_cs_results     = @@character_set_results */ ;
/*!50003 SET @saved_col_connection = @@collation_connection */ ;
/*!50003 SET character_set_client  = utf8mb4 */ ;
/*!50003 SET character_set_results = utf8mb4 */ ;
/*!50003 SET collation_connection  = utf8mb4_0900_ai_ci */ ;
/*!50003 SET @saved_sql_mode       = @@sql_mode */ ;
/*!50003 SET sql_mode              = 'STRICT_TRANS_TABLES,NO_ENGINE_SUBSTITUTION' */ ;
DELIMITER @@
/*!50003 CREATE*/ /*!50017 DEFINER=`root`@`localhost`*/ /*!50003 TRIGGER `main_AFTER_INSERT` AFTER INSERT ON `main` FOR EACH ROW BEGIN

	INSERT INTO  contracts_has_serv (filled, contracts_id, serv_id)
	values
	(new.quantity, new.contracts_id, new.serv_id)
	ON DUPLICATE KEY UPDATE  filled = filled  + new.quantity;
END */@@
DELIMITER ;
/*!50003 SET sql_mode              = @saved_sql_mode */ ;
/*!50003 SET character_set_client  = @saved_cs_client */ ;
/*!50003 SET character_set_results = @saved_cs_results */ ;
/*!50003 SET collation_connection  = @saved_col_connection */ ;
/*!50003 SET @saved_cs_client      = @@character_set_client */ ;
/*!50003 SET @saved_cs_results     = @@character_set_results */ ;
/*!50003 SET @saved_col_connection = @@collation_connection */ ;
/*!50003 SET character_set_client  = utf8mb4 */ ;
/*!50003 SET character_set_results = utf8mb4 */ ;
/*!50003 SET collation_connection  = utf8mb4_0900_ai_ci */ ;
/*!50003 SET @saved_sql_mode       = @@sql_mode */ ;
/*!50003 SET sql_mode              = 'STRICT_TRANS_TABLES,NO_ENGINE_SUBSTITUTION' */ ;
DELIMITER @@
/*!50003 CREATE*/ /*!50017 DEFINER=`root`@`localhost`*/ /*!50003 TRIGGER `main_BEFORE_UPDATE` BEFORE UPDATE ON `main` FOR EACH ROW BEGIN

  declare ovdid int default 0;
  declare planned int default 0;
  declare filled int default 0;
  declare wid int default 0;
   set new.serv_id=old.serv_id,
   new.contracts_id=old.contracts_id,
   new.client_id=old.client_id,
   new.dep_id=old.dep_id;


select s.planned - s.filled - new.quantity + old.quantity, s.planned , s.filled  into  ovdid, planned , filled   from  contracts_has_serv s where
  s.contracts_id = new.contracts_id  and
  s.serv_id =  new.serv_id ;
  
	if (ovdid < 0) then
		set @last_message_text = CONCAT ( "ошибка: эта услуга переполнена, осталось ", planned - filled, " услуг" );
		SIGNAL SQLSTATE '45000'
		SET MESSAGE_TEXT = @last_message_text;
	end if;


	set wid = (select worker_id from dep_has_worker where id = new.dep_has_worker_id );
    if coalesce(New.worker_id, 0) <> wid   then
		set new.worker_id = wid;
    end if;
    
    
    if NEW.prev_quantity != old.quantity then
		SET NEW.prev_quantity=old.quantity;
    end if;
    
	SET NEW.upd_by=get_wID();
END */@@
DELIMITER ;
/*!50003 SET sql_mode              = @saved_sql_mode */ ;
/*!50003 SET character_set_client  = @saved_cs_client */ ;
/*!50003 SET character_set_results = @saved_cs_results */ ;
/*!50003 SET collation_connection  = @saved_col_connection */ ;
/*!50003 SET @saved_cs_client      = @@character_set_client */ ;
/*!50003 SET @saved_cs_results     = @@character_set_results */ ;
/*!50003 SET @saved_col_connection = @@collation_connection */ ;
/*!50003 SET character_set_client  = utf8mb4 */ ;
/*!50003 SET character_set_results = utf8mb4 */ ;
/*!50003 SET collation_connection  = utf8mb4_0900_ai_ci */ ;
/*!50003 SET @saved_sql_mode       = @@sql_mode */ ;
/*!50003 SET sql_mode              = 'STRICT_TRANS_TABLES,NO_ENGINE_SUBSTITUTION' */ ;
DELIMITER @@
/*!50003 CREATE*/ /*!50017 DEFINER=`root`@`localhost`*/ /*!50003 TRIGGER `main_AFTER_UPDATE` AFTER UPDATE ON `main` FOR EACH ROW BEGIN

	UPDATE contracts_has_serv set filled=filled+new.quantity-old.quantity
		where contracts_id=new.contracts_id and serv_id=new.serv_id;
END */@@
DELIMITER ;
/*!50003 SET sql_mode              = @saved_sql_mode */ ;
/*!50003 SET character_set_client  = @saved_cs_client */ ;
/*!50003 SET character_set_results = @saved_cs_results */ ;
/*!50003 SET collation_connection  = @saved_col_connection */ ;
/*!50003 SET @saved_cs_client      = @@character_set_client */ ;
/*!50003 SET @saved_cs_results     = @@character_set_results */ ;
/*!50003 SET @saved_col_connection = @@collation_connection */ ;
/*!50003 SET character_set_client  = utf8mb4 */ ;
/*!50003 SET character_set_results = utf8mb4 */ ;
/*!50003 SET collation_connection  = utf8mb4_0900_ai_ci */ ;
/*!50003 SET @saved_sql_mode       = @@sql_mode */ ;
/*!50003 SET sql_mode              = 'STRICT_TRANS_TABLES,NO_ENGINE_SUBSTITUTION' */ ;
DELIMITER @@
/*!50003 CREATE*/ /*!50017 DEFINER=`root`@`localhost`*/ /*!50003 TRIGGER `main_AFTER_DELETE` AFTER DELETE ON `main` FOR EACH ROW BEGIN
	UPDATE contracts_has_serv set filled=filled-old.quantity
		where contracts_id=old.contracts_id and serv_id=old.serv_id;
END */@@
DELIMITER ;
/*!50003 SET sql_mode              = @saved_sql_mode */ ;
/*!50003 SET character_set_client  = @saved_cs_client */ ;
/*!50003 SET character_set_results = @saved_cs_results */ ;
/*!50003 SET collation_connection  = @saved_col_connection */ ;

--
-- Temporary view structure for view `main_cprice`
--

DROP TABLE IF EXISTS `main_cprice`;
/*!50001 DROP VIEW IF EXISTS `main_cprice`*/;
SET @saved_cs_client     = @@character_set_client;
/*!50503 SET character_set_client = utf8mb4 */;
/*!50001 CREATE VIEW `main_cprice` AS SELECT 
 1 AS `id`,
 1 AS `contracts_id`,
 1 AS `dep_id`,
 1 AS `client_id`,
 1 AS `serv_id`,
 1 AS `dep_has_worker_id`,
 1 AS `worker_id`,
 1 AS `vdate`,
 1 AS `quantity`,
 1 AS `note`,
 1 AS `create`,
 1 AS `ts`,
 1 AS `cr_by`,
 1 AS `upd_by`,
 1 AS `reported`,
 1 AS `wdate`,
 1 AS `overdid`,
 1 AS `prev_quantity`,
 1 AS `perc`,
 1 AS `price`,
 1 AS `price2`,
 1 AS `price3`,
 1 AS `servform_id`,
 1 AS `to_pay`,
 1 AS `to_pay2`*/;
SET character_set_client = @saved_cs_client;

--
-- Table structure for table `main_has_ugroup`
--

DROP TABLE IF EXISTS `main_has_ugroup`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `main_has_ugroup` (
  `main_id` bigint unsigned NOT NULL,
  `ugroup_id` int NOT NULL,
  PRIMARY KEY (`main_id`,`ugroup_id`),
  KEY `fk_main_has_ugroup_ugroup1_idx` (`ugroup_id`),
  KEY `fk_main_has_ugroup_main1_idx` (`main_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Temporary view structure for view `main_nz`
--

DROP TABLE IF EXISTS `main_nz`;
/*!50001 DROP VIEW IF EXISTS `main_nz`*/;
SET @saved_cs_client     = @@character_set_client;
/*!50503 SET character_set_client = utf8mb4 */;
/*!50001 CREATE VIEW `main_nz` AS SELECT 
 1 AS `id`,
 1 AS `contracts_id`,
 1 AS `dep_id`,
 1 AS `client_id`,
 1 AS `serv_id`,
 1 AS `dep_has_worker_id`,
 1 AS `worker_id`,
 1 AS `vdate`,
 1 AS `quantity`,
 1 AS `note`,
 1 AS `create`,
 1 AS `ts`,
 1 AS `cr_by`,
 1 AS `upd_by`,
 1 AS `reported`,
 1 AS `wdate`,
 1 AS `overdid`,
 1 AS `prev_quantity`*/;
SET character_set_client = @saved_cs_client;

--
-- Temporary view structure for view `max_pay_in_month`
--

DROP TABLE IF EXISTS `max_pay_in_month`;
/*!50001 DROP VIEW IF EXISTS `max_pay_in_month`*/;
SET @saved_cs_client     = @@character_set_client;
/*!50503 SET character_set_client = utf8mb4 */;
/*!50001 CREATE VIEW `max_pay_in_month` AS SELECT 
 1 AS `contracts_id`,
 1 AS `ripso_id`,
 1 AS `pddate`,
 1 AS `sdd`,
 1 AS `servform_id`,
 1 AS `lm`,
 1 AS `perc`,
 1 AS `work_livemin`,
 1 AS `client_id`,
 1 AS `max_pay`,
 1 AS `new_at`*/;
SET character_set_client = @saved_cs_client;

--
-- Temporary view structure for view `max_pay_in_month_50`
--

DROP TABLE IF EXISTS `max_pay_in_month_50`;
/*!50001 DROP VIEW IF EXISTS `max_pay_in_month_50`*/;
SET @saved_cs_client     = @@character_set_client;
/*!50503 SET character_set_client = utf8mb4 */;
/*!50001 CREATE VIEW `max_pay_in_month_50` AS SELECT 
 1 AS `contracts_id`,
 1 AS `ripso_id`,
 1 AS `pddate`,
 1 AS `sdd`,
 1 AS `servform_id`,
 1 AS `lm`,
 1 AS `max_pay`*/;
SET character_set_client = @saved_cs_client;

--
-- Temporary view structure for view `max_pay_in_month_75`
--

DROP TABLE IF EXISTS `max_pay_in_month_75`;
/*!50001 DROP VIEW IF EXISTS `max_pay_in_month_75`*/;
SET @saved_cs_client     = @@character_set_client;
/*!50503 SET character_set_client = utf8mb4 */;
/*!50001 CREATE VIEW `max_pay_in_month_75` AS SELECT 
 1 AS `contracts_id`,
 1 AS `ripso_id`,
 1 AS `pddate`,
 1 AS `sdd`,
 1 AS `servform_id`,
 1 AS `lm`,
 1 AS `max_pay`*/;
SET character_set_client = @saved_cs_client;

--
-- Table structure for table `notifies`
--

DROP TABLE IF EXISTS `notifies`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `notifies` (
  `id` int NOT NULL AUTO_INCREMENT,
  `active` tinyint DEFAULT '1',
  `date` datetime NOT NULL DEFAULT CURRENT_TIMESTAMP,
  `msg` varchar(255) NOT NULL,
  `onlyFor` tinyint DEFAULT NULL,
  `worker_id` int unsigned DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `fk_notifies_worker1_idx` (`worker_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `payment`
--

DROP TABLE IF EXISTS `payment`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `payment` (
  `id` int unsigned NOT NULL AUTO_INCREMENT,
  `client_id` int unsigned NOT NULL,
  `paydate` date DEFAULT NULL,
  `sum` decimal(10,2) DEFAULT NULL,
  `note` varchar(255) DEFAULT NULL,
  `ts` varchar(45) DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `fk_payment_client1_idx` (`client_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `pcat`
--

DROP TABLE IF EXISTS `pcat`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `pcat` (
  `id` int unsigned NOT NULL,
  `pcat` varchar(255) NOT NULL,
  `note` varchar(45) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `ripso`
--

DROP TABLE IF EXISTS `ripso`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `ripso` (
  `id` int unsigned NOT NULL AUTO_INCREMENT,
  `ripso` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL,
  `ripso_short` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL,
  `year` year NOT NULL,
  `archive` tinyint DEFAULT '0',
  `servform_id` int unsigned NOT NULL,
  `months` int DEFAULT NULL,
  `pcat_id` int unsigned NOT NULL DEFAULT '1',
  PRIMARY KEY (`id`),
  KEY `fk_ripso_servform1_idx` (`servform_id`),
  KEY `fk_ripso_pcat1_idx` (`pcat_id`)
) ENGINE=InnoDB AUTO_INCREMENT=26 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `ripso_has_serv`
--

DROP TABLE IF EXISTS `ripso_has_serv`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `ripso_has_serv` (
  `planned` int DEFAULT NULL,
  `serv_id` int unsigned NOT NULL,
  `ripso_id` int unsigned NOT NULL,
  `year` year DEFAULT NULL,
  `archive` tinyint DEFAULT '0',
  PRIMARY KEY (`serv_id`,`ripso_id`),
  KEY `fk_ripso_has_serv_ripso1_idx` (`ripso_id`),
  CONSTRAINT `fk_ripso_has_serv_serv1` FOREIGN KEY (`serv_id`) REFERENCES `serv` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `rname`
--

DROP TABLE IF EXISTS `rname`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `rname` (
  `id` int unsigned NOT NULL AUTO_INCREMENT,
  `Rname` varchar(45) DEFAULT NULL,
  `note` varchar(255) DEFAULT NULL,
  `ts` timestamp NULL DEFAULT CURRENT_TIMESTAMP,
  `cr_ts` timestamp NULL DEFAULT CURRENT_TIMESTAMP,
  `scheduled` tinyint DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `role`
--

DROP TABLE IF EXISTS `role`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `role` (
  `id` int unsigned NOT NULL AUTO_INCREMENT,
  `role` varchar(45) DEFAULT NULL,
  `note` varchar(255) DEFAULT NULL,
  `role_sqlname` varchar(100) DEFAULT 'info',
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=10 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `serv`
--

DROP TABLE IF EXISTS `serv`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `serv` (
  `id` int unsigned NOT NULL AUTO_INCREMENT,
  `serv` varchar(716) GENERATED ALWAYS AS (concat(`tnum`,_utf8mb4' ',`serv_text`)) VIRTUAL,
  `serv_text` varchar(700) NOT NULL,
  `tnum` varchar(15) NOT NULL,
  `year` year NOT NULL,
  `sub_serv` int DEFAULT NULL,
  `sub_serv_str` varchar(10) DEFAULT NULL,
  `price` decimal(10,2) DEFAULT NULL,
  `price2` decimal(10,2) DEFAULT NULL,
  `price3` decimal(10,2) DEFAULT NULL,
  `archive` tinyint DEFAULT '0',
  `replacedby` int DEFAULT '0' COMMENT 'id of service which replaced this service than it was archivated',
  `total` tinyint DEFAULT '0',
  `acronym` varchar(45) DEFAULT NULL,
  `workload` int DEFAULT NULL,
  `content` varchar(1000) DEFAULT NULL,
  `create` datetime DEFAULT CURRENT_TIMESTAMP,
  `ts` datetime DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  `cr_by` int DEFAULT NULL,
  `upd_by` int DEFAULT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `tnum_UNIQUE` (`tnum`),
  UNIQUE KEY `servcol_UNIQUE` (`serv`),
  KEY `serv_sub_serv_IDX` (`sub_serv`) USING BTREE,
  KEY `serv_sub_serv_str_IDX` (`sub_serv_str`) USING BTREE
) ENGINE=InnoDB AUTO_INCREMENT=1098 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;
/*!50003 SET @saved_cs_client      = @@character_set_client */ ;
/*!50003 SET @saved_cs_results     = @@character_set_results */ ;
/*!50003 SET @saved_col_connection = @@collation_connection */ ;
/*!50003 SET character_set_client  = utf8mb4 */ ;
/*!50003 SET character_set_results = utf8mb4 */ ;
/*!50003 SET collation_connection  = utf8mb4_0900_ai_ci */ ;
/*!50003 SET @saved_sql_mode       = @@sql_mode */ ;
/*!50003 SET sql_mode              = 'STRICT_TRANS_TABLES,NO_ENGINE_SUBSTITUTION' */ ;
DELIMITER @@
/*!50003 CREATE*/ /*!50017 DEFINER=`root`@`localhost`*/ /*!50003 TRIGGER `serv_BEFORE_INSERT` BEFORE INSERT ON `serv` FOR EACH ROW BEGIN

	SET  NEW.cr_by = get_wID();
	SET  NEW.upd_by = get_wID();
END */@@
DELIMITER ;
/*!50003 SET sql_mode              = @saved_sql_mode */ ;
/*!50003 SET character_set_client  = @saved_cs_client */ ;
/*!50003 SET character_set_results = @saved_cs_results */ ;
/*!50003 SET collation_connection  = @saved_col_connection */ ;
/*!50003 SET @saved_cs_client      = @@character_set_client */ ;
/*!50003 SET @saved_cs_results     = @@character_set_results */ ;
/*!50003 SET @saved_col_connection = @@collation_connection */ ;
/*!50003 SET character_set_client  = utf8mb4 */ ;
/*!50003 SET character_set_results = utf8mb4 */ ;
/*!50003 SET collation_connection  = utf8mb4_0900_ai_ci */ ;
/*!50003 SET @saved_sql_mode       = @@sql_mode */ ;
/*!50003 SET sql_mode              = 'STRICT_TRANS_TABLES,NO_ENGINE_SUBSTITUTION' */ ;
DELIMITER @@
/*!50003 CREATE*/ /*!50017 DEFINER=`root`@`localhost`*/ /*!50003 TRIGGER `serv_BEFORE_UPDATE` BEFORE UPDATE ON `serv` FOR EACH ROW BEGIN

	SET  NEW.cr_by = get_wID();
	SET  NEW.upd_by = get_wID();
END */@@
DELIMITER ;
/*!50003 SET sql_mode              = @saved_sql_mode */ ;
/*!50003 SET character_set_client  = @saved_cs_client */ ;
/*!50003 SET character_set_results = @saved_cs_results */ ;
/*!50003 SET collation_connection  = @saved_col_connection */ ;

--
-- Table structure for table `serv_images`
--

DROP TABLE IF EXISTS `serv_images`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `serv_images` (
  `expr` varchar(255) NOT NULL,
  `image` varchar(255) DEFAULT NULL,
  `words` varchar(100) DEFAULT NULL,
  `archiv` tinyint(1) DEFAULT '0'
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `servform`
--

DROP TABLE IF EXISTS `servform`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `servform` (
  `id` int NOT NULL AUTO_INCREMENT,
  `servform` varchar(255) DEFAULT NULL,
  `note` varchar(255) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=5 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Temporary view structure for view `servofripso`
--

DROP TABLE IF EXISTS `servofripso`;
/*!50001 DROP VIEW IF EXISTS `servofripso`*/;
SET @saved_cs_client     = @@character_set_client;
/*!50503 SET character_set_client = utf8mb4 */;
/*!50001 CREATE VIEW `servofripso` AS SELECT 
 1 AS `id`,
 1 AS `tnum`,
 1 AS `serv`,
 1 AS `year`,
 1 AS `sub_serv`,
 1 AS `sub_serv_str`,
 1 AS `price`,
 1 AS `price2`,
 1 AS `price3`,
 1 AS `archive`,
 1 AS `total`,
 1 AS `acronym`,
 1 AS `workload`,
 1 AS `content`,
 1 AS `r_id`,
 1 AS `ripso`*/;
SET character_set_client = @saved_cs_client;

--
-- Temporary view structure for view `servofyear`
--

DROP TABLE IF EXISTS `servofyear`;
/*!50001 DROP VIEW IF EXISTS `servofyear`*/;
SET @saved_cs_client     = @@character_set_client;
/*!50503 SET character_set_client = utf8mb4 */;
/*!50001 CREATE VIEW `servofyear` AS SELECT 
 1 AS `id`,
 1 AS `contracts_id`,
 1 AS `dep_id`,
 1 AS `client_id`,
 1 AS `serv_id`,
 1 AS `dep_has_worker_id`,
 1 AS `worker_id`,
 1 AS `vdate`,
 1 AS `quantity`,
 1 AS `note`,
 1 AS `create`,
 1 AS `ts`,
 1 AS `cr_by`,
 1 AS `upd_by`,
 1 AS `reported`,
 1 AS `wdate`,
 1 AS `overdid`,
 1 AS `prev_quantity`*/;
SET character_set_client = @saved_cs_client;

--
-- Table structure for table `setting`
--

DROP TABLE IF EXISTS `setting`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `setting` (
  `id` int NOT NULL AUTO_INCREMENT,
  `archive` tinyint DEFAULT '0',
  `setting` varchar(45) DEFAULT NULL,
  `value` varchar(1024) DEFAULT NULL,
  `note` varchar(1024) DEFAULT NULL,
  `sdate` datetime NOT NULL DEFAULT CURRENT_TIMESTAMP,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Temporary view structure for view `should_perc`
--

DROP TABLE IF EXISTS `should_perc`;
/*!50001 DROP VIEW IF EXISTS `should_perc`*/;
SET @saved_cs_client     = @@character_set_client;
/*!50503 SET character_set_client = utf8mb4 */;
/*!50001 CREATE VIEW `should_perc` AS SELECT 
 1 AS `contracts_id`,
 1 AS `pddate`,
 1 AS `ripso_id`,
 1 AS `sdd`,
 1 AS `servform_id`,
 1 AS `lm`,
 1 AS `category_id`,
 1 AS `perc`,
 1 AS `should_perc`*/;
SET character_set_client = @saved_cs_client;

--
-- Table structure for table `street_home`
--

DROP TABLE IF EXISTS `street_home`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `street_home` (
  `id` int NOT NULL,
  `street_home` varchar(255) DEFAULT NULL,
  `note` varchar(255) DEFAULT NULL,
  `create` datetime DEFAULT CURRENT_TIMESTAMP,
  `ts` datetime DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  `cr_by` int DEFAULT NULL,
  `upd_by` int DEFAULT NULL,
  `coordinate` point DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `stub_model`
--

DROP TABLE IF EXISTS `stub_model`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `stub_model` (
  `id` int NOT NULL,
  `msg` varchar(45) DEFAULT NULL,
  `msg1` varchar(45) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci COMMENT='Used as default table model if right model  not implemented yet';
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `tables_checksums`
--

DROP TABLE IF EXISTS `tables_checksums`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `tables_checksums` (
  `id` int NOT NULL AUTO_INCREMENT,
  `table` varchar(45) NOT NULL,
  `checksum` varchar(45) DEFAULT NULL,
  `lastid` int DEFAULT NULL,
  PRIMARY KEY (`id`,`table`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `test`
--

DROP TABLE IF EXISTS `test`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `test` (
  `id` int NOT NULL AUTO_INCREMENT,
  `date` date DEFAULT NULL,
  `datetime` datetime DEFAULT NULL,
  `str` varchar(45) DEFAULT NULL,
  `decimal` decimal(10,2) DEFAULT NULL,
  `double` double DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Temporary view structure for view `total_cprice_in_month`
--

DROP TABLE IF EXISTS `total_cprice_in_month`;
/*!50001 DROP VIEW IF EXISTS `total_cprice_in_month`*/;
SET @saved_cs_client     = @@character_set_client;
/*!50503 SET character_set_client = utf8mb4 */;
/*!50001 CREATE VIEW `total_cprice_in_month` AS SELECT 
 1 AS `contracts_id`,
 1 AS `SUM(to_pay)`*/;
SET character_set_client = @saved_cs_client;

--
-- Table structure for table `ugroup`
--

DROP TABLE IF EXISTS `ugroup`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `ugroup` (
  `id` int NOT NULL,
  `ugroup` varchar(45) NOT NULL,
  `dep_id` int unsigned DEFAULT '0',
  `worker_id` int unsigned DEFAULT '0',
  `note` varchar(255) DEFAULT NULL,
  `ugroupcol` varchar(45) DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `fk_ugroup_dep1_idx` (`dep_id`),
  KEY `fk_ugroup_worker1_idx` (`worker_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `ugroup_has_client`
--

DROP TABLE IF EXISTS `ugroup_has_client`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `ugroup_has_client` (
  `ugroup_id` int NOT NULL,
  `client_id` int unsigned NOT NULL,
  PRIMARY KEY (`ugroup_id`,`client_id`),
  KEY `fk_ugroup_has_client_client1_idx` (`client_id`),
  KEY `fk_ugroup_has_client_ugroup1_idx` (`ugroup_id`),
  CONSTRAINT `fk_ugroup_has_client_ugroup1` FOREIGN KEY (`ugroup_id`) REFERENCES `ugroup` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `ui_select_fiolist`
--

DROP TABLE IF EXISTS `ui_select_fiolist`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `ui_select_fiolist` (
  `id` int NOT NULL,
  `list_name` varchar(200) NOT NULL,
  `sql_table` varchar(100) DEFAULT NULL,
  `col` int DEFAULT NULL,
  `orderby` int DEFAULT NULL,
  `note` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Temporary view structure for view `upd_by`
--

DROP TABLE IF EXISTS `upd_by`;
/*!50001 DROP VIEW IF EXISTS `upd_by`*/;
SET @saved_cs_client     = @@character_set_client;
/*!50503 SET character_set_client = utf8mb4 */;
/*!50001 CREATE VIEW `upd_by` AS SELECT 
 1 AS `id`,
 1 AS `upd_by`,
 1 AS `user`,
 1 AS `note`,
 1 AS `role_id`,
 1 AS `dep_id`,
 1 AS `archive`*/;
SET character_set_client = @saved_cs_client;

--
-- Temporary view structure for view `updatable_2__dep_has_client`
--

DROP TABLE IF EXISTS `updatable_2__dep_has_client`;
/*!50001 DROP VIEW IF EXISTS `updatable_2__dep_has_client`*/;
SET @saved_cs_client     = @@character_set_client;
/*!50503 SET character_set_client = utf8mb4 */;
/*!50001 CREATE VIEW `updatable_2__dep_has_client` AS SELECT 
 1 AS `id`,
 1 AS `client`,
 1 AS `client_short`,
 1 AS `clientDeath`,
 1 AS `clientbirth`,
 1 AS `ESRN`,
 1 AS `note`,
 1 AS `phone`,
 1 AS `snils`,
 1 AS `curator`,
 1 AS `create`,
 1 AS `ts`,
 1 AS `cr_by`,
 1 AS `upd_by`,
 1 AS `cr_dep_id`*/;
SET character_set_client = @saved_cs_client;

--
-- Temporary view structure for view `updatable__contr_has_add_info`
--

DROP TABLE IF EXISTS `updatable__contr_has_add_info`;
/*!50001 DROP VIEW IF EXISTS `updatable__contr_has_add_info`*/;
SET @saved_cs_client     = @@character_set_client;
/*!50503 SET character_set_client = utf8mb4 */;
/*!50001 CREATE VIEW `updatable__contr_has_add_info` AS SELECT 
 1 AS `pddate`,
 1 AS `contracts_id`,
 1 AS `predv_money`,
 1 AS `curFIO`,
 1 AS `psp`,
 1 AS `address`,
 1 AS `sdd`,
 1 AS `sdd_date`,
 1 AS `perc`,
 1 AS `not_standart_contract`,
 1 AS `not_standart_act`,
 1 AS `note`,
 1 AS `create`,
 1 AS `ts`,
 1 AS `cr_by`,
 1 AS `upd_by`,
 1 AS `repr_FIO`,
 1 AS `repr_addr`,
 1 AS `repr_psp`,
 1 AS `work_livemin`*/;
SET character_set_client = @saved_cs_client;

--
-- Temporary view structure for view `updatable__dep_has_add_info`
--

DROP TABLE IF EXISTS `updatable__dep_has_add_info`;
/*!50001 DROP VIEW IF EXISTS `updatable__dep_has_add_info`*/;
SET @saved_cs_client     = @@character_set_client;
/*!50503 SET character_set_client = utf8mb4 */;
/*!50001 CREATE VIEW `updatable__dep_has_add_info` AS SELECT 
 1 AS `pddate`,
 1 AS `contracts_id`,
 1 AS `predv_money`,
 1 AS `curFIO`,
 1 AS `psp`,
 1 AS `address`,
 1 AS `sdd`,
 1 AS `sdd_date`,
 1 AS `perc`,
 1 AS `not_standart_contract`,
 1 AS `not_standart_act`,
 1 AS `note`,
 1 AS `create`,
 1 AS `ts`,
 1 AS `cr_by`,
 1 AS `upd_by`,
 1 AS `repr_FIO`,
 1 AS `repr_addr`,
 1 AS `repr_psp`,
 1 AS `work_livemin`*/;
SET character_set_client = @saved_cs_client;

--
-- Temporary view structure for view `updatable__dep_has_client`
--

DROP TABLE IF EXISTS `updatable__dep_has_client`;
/*!50001 DROP VIEW IF EXISTS `updatable__dep_has_client`*/;
SET @saved_cs_client     = @@character_set_client;
/*!50503 SET character_set_client = utf8mb4 */;
/*!50001 CREATE VIEW `updatable__dep_has_client` AS SELECT 
 1 AS `id`,
 1 AS `client`,
 1 AS `client_short`,
 1 AS `clientDeath`,
 1 AS `clientbirth`,
 1 AS `ESRN`,
 1 AS `note`,
 1 AS `phone`,
 1 AS `snils`,
 1 AS `curator`,
 1 AS `create`,
 1 AS `ts`,
 1 AS `cr_by`,
 1 AS `upd_by`,
 1 AS `cr_dep_id`*/;
SET character_set_client = @saved_cs_client;

--
-- Temporary view structure for view `updatable__dep_has_contracts`
--

DROP TABLE IF EXISTS `updatable__dep_has_contracts`;
/*!50001 DROP VIEW IF EXISTS `updatable__dep_has_contracts`*/;
SET @saved_cs_client     = @@character_set_client;
/*!50503 SET character_set_client = utf8mb4 */;
/*!50001 CREATE VIEW `updatable__dep_has_contracts` AS SELECT 
 1 AS `id`,
 1 AS `contracts`,
 1 AS `contracts2`,
 1 AS `client_id`,
 1 AS `dep_id`,
 1 AS `ripso_id`,
 1 AS `blocked`,
 1 AS `startdate`,
 1 AS `enddate`,
 1 AS `ippsuNum`,
 1 AS `note`,
 1 AS `create`,
 1 AS `ts`,
 1 AS `cr_by`,
 1 AS `upd_by`,
 1 AS `to_recheck`,
 1 AS `check_date`,
 1 AS `pyc_prim`*/;
SET character_set_client = @saved_cs_client;

--
-- Temporary view structure for view `updatable__dep_has_main`
--

DROP TABLE IF EXISTS `updatable__dep_has_main`;
/*!50001 DROP VIEW IF EXISTS `updatable__dep_has_main`*/;
SET @saved_cs_client     = @@character_set_client;
/*!50503 SET character_set_client = utf8mb4 */;
/*!50001 CREATE VIEW `updatable__dep_has_main` AS SELECT 
 1 AS `id`,
 1 AS `contracts_id`,
 1 AS `dep_id`,
 1 AS `client_id`,
 1 AS `serv_id`,
 1 AS `dep_has_worker_id`,
 1 AS `worker_id`,
 1 AS `vdate`,
 1 AS `quantity`,
 1 AS `note`,
 1 AS `create`,
 1 AS `ts`,
 1 AS `cr_by`,
 1 AS `upd_by`,
 1 AS `reported`,
 1 AS `wdate`,
 1 AS `overdid`,
 1 AS `prev_quantity`*/;
SET character_set_client = @saved_cs_client;

--
-- Temporary view structure for view `updatable__user_has_main`
--

DROP TABLE IF EXISTS `updatable__user_has_main`;
/*!50001 DROP VIEW IF EXISTS `updatable__user_has_main`*/;
SET @saved_cs_client     = @@character_set_client;
/*!50503 SET character_set_client = utf8mb4 */;
/*!50001 CREATE VIEW `updatable__user_has_main` AS SELECT 
 1 AS `id`,
 1 AS `contracts_id`,
 1 AS `dep_id`,
 1 AS `client_id`,
 1 AS `serv_id`,
 1 AS `dep_has_worker_id`,
 1 AS `worker_id`,
 1 AS `vdate`,
 1 AS `quantity`,
 1 AS `note`,
 1 AS `create`,
 1 AS `ts`,
 1 AS `cr_by`,
 1 AS `upd_by`,
 1 AS `reported`,
 1 AS `wdate`,
 1 AS `overdid`,
 1 AS `prev_quantity`*/;
SET character_set_client = @saved_cs_client;

--
-- Temporary view structure for view `updatable_add_info`
--

DROP TABLE IF EXISTS `updatable_add_info`;
/*!50001 DROP VIEW IF EXISTS `updatable_add_info`*/;
SET @saved_cs_client     = @@character_set_client;
/*!50503 SET character_set_client = utf8mb4 */;
/*!50001 CREATE VIEW `updatable_add_info` AS SELECT 
 1 AS `pddate`,
 1 AS `contracts_id`,
 1 AS `predv_money`,
 1 AS `curFIO`,
 1 AS `psp`,
 1 AS `address`,
 1 AS `sdd`,
 1 AS `sdd_date`,
 1 AS `perc`,
 1 AS `not_standart_contract`,
 1 AS `not_standart_act`,
 1 AS `note`,
 1 AS `create`,
 1 AS `ts`,
 1 AS `cr_by`,
 1 AS `upd_by`,
 1 AS `repr_FIO`,
 1 AS `repr_addr`,
 1 AS `repr_psp`,
 1 AS `work_livemin`*/;
SET character_set_client = @saved_cs_client;

--
-- Temporary view structure for view `updatable_client`
--

DROP TABLE IF EXISTS `updatable_client`;
/*!50001 DROP VIEW IF EXISTS `updatable_client`*/;
SET @saved_cs_client     = @@character_set_client;
/*!50503 SET character_set_client = utf8mb4 */;
/*!50001 CREATE VIEW `updatable_client` AS SELECT 
 1 AS `id`,
 1 AS `client`,
 1 AS `client_short`,
 1 AS `clientDeath`,
 1 AS `clientbirth`,
 1 AS `ESRN`,
 1 AS `note`,
 1 AS `phone`,
 1 AS `snils`,
 1 AS `curator`,
 1 AS `create`,
 1 AS `ts`,
 1 AS `cr_by`,
 1 AS `upd_by`,
 1 AS `cr_dep_id`*/;
SET character_set_client = @saved_cs_client;

--
-- Temporary view structure for view `updatable_contracts`
--

DROP TABLE IF EXISTS `updatable_contracts`;
/*!50001 DROP VIEW IF EXISTS `updatable_contracts`*/;
SET @saved_cs_client     = @@character_set_client;
/*!50503 SET character_set_client = utf8mb4 */;
/*!50001 CREATE VIEW `updatable_contracts` AS SELECT 
 1 AS `id`,
 1 AS `contracts`,
 1 AS `contracts2`,
 1 AS `client_id`,
 1 AS `dep_id`,
 1 AS `ripso_id`,
 1 AS `blocked`,
 1 AS `startdate`,
 1 AS `enddate`,
 1 AS `ippsuNum`,
 1 AS `note`,
 1 AS `create`,
 1 AS `ts`,
 1 AS `cr_by`,
 1 AS `upd_by`,
 1 AS `to_recheck`,
 1 AS `check_date`,
 1 AS `pyc_prim`*/;
SET character_set_client = @saved_cs_client;

--
-- Temporary view structure for view `updatable_contracts_has_serv`
--

DROP TABLE IF EXISTS `updatable_contracts_has_serv`;
/*!50001 DROP VIEW IF EXISTS `updatable_contracts_has_serv`*/;
SET @saved_cs_client     = @@character_set_client;
/*!50503 SET character_set_client = utf8mb4 */;
/*!50001 CREATE VIEW `updatable_contracts_has_serv` AS SELECT 
 1 AS `serv_id`,
 1 AS `contracts_id`,
 1 AS `planned`,
 1 AS `filled`,
 1 AS `note`,
 1 AS `archive`,
 1 AS `create`,
 1 AS `ts`,
 1 AS `cr_by`,
 1 AS `upd_by`,
 1 AS `to_recheck`,
 1 AS `check_date`,
 1 AS `filled_old`*/;
SET character_set_client = @saved_cs_client;

--
-- Temporary view structure for view `updatable_main`
--

DROP TABLE IF EXISTS `updatable_main`;
/*!50001 DROP VIEW IF EXISTS `updatable_main`*/;
SET @saved_cs_client     = @@character_set_client;
/*!50503 SET character_set_client = utf8mb4 */;
/*!50001 CREATE VIEW `updatable_main` AS SELECT 
 1 AS `id`,
 1 AS `contracts_id`,
 1 AS `dep_id`,
 1 AS `client_id`,
 1 AS `serv_id`,
 1 AS `dep_has_worker_id`,
 1 AS `worker_id`,
 1 AS `vdate`,
 1 AS `quantity`,
 1 AS `note`,
 1 AS `create`,
 1 AS `ts`,
 1 AS `cr_by`,
 1 AS `upd_by`,
 1 AS `reported`,
 1 AS `wdate`,
 1 AS `overdid`,
 1 AS `prev_quantity`*/;
SET character_set_client = @saved_cs_client;

--
-- Table structure for table `user_change`
--

DROP TABLE IF EXISTS `user_change`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `user_change` (
  `id` int NOT NULL AUTO_INCREMENT,
  `old_login` varchar(16) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci DEFAULT NULL,
  `p` varchar(32) DEFAULT NULL,
  `new_login` varchar(16) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL,
  `p2` varchar(32) DEFAULT NULL,
  `note` varchar(255) DEFAULT NULL,
  `create` datetime DEFAULT CURRENT_TIMESTAMP,
  `ts` datetime DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  `cr_by` int DEFAULT NULL,
  `upd_by` int DEFAULT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `user_change_id_IDX` (`id`) USING BTREE
) ENGINE=InnoDB AUTO_INCREMENT=6 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;
/*!50003 SET @saved_cs_client      = @@character_set_client */ ;
/*!50003 SET @saved_cs_results     = @@character_set_results */ ;
/*!50003 SET @saved_col_connection = @@collation_connection */ ;
/*!50003 SET character_set_client  = utf8mb4 */ ;
/*!50003 SET character_set_results = utf8mb4 */ ;
/*!50003 SET collation_connection  = utf8mb4_0900_ai_ci */ ;
/*!50003 SET @saved_sql_mode       = @@sql_mode */ ;
/*!50003 SET sql_mode              = 'STRICT_TRANS_TABLES,NO_ENGINE_SUBSTITUTION' */ ;
DELIMITER @@
/*!50003 CREATE*/ /*!50017 DEFINER=`root`@`localhost`*/ /*!50003 TRIGGER `user_change_before_insert` BEFORE INSERT ON `user_change` FOR EACH ROW begin
	SET  NEW.cr_by = get_wID();
	SET  NEW.upd_by = get_wID();
end */@@
DELIMITER ;
/*!50003 SET sql_mode              = @saved_sql_mode */ ;
/*!50003 SET character_set_client  = @saved_cs_client */ ;
/*!50003 SET character_set_results = @saved_cs_results */ ;
/*!50003 SET collation_connection  = @saved_col_connection */ ;
/*!50003 SET @saved_cs_client      = @@character_set_client */ ;
/*!50003 SET @saved_cs_results     = @@character_set_results */ ;
/*!50003 SET @saved_col_connection = @@collation_connection */ ;
/*!50003 SET character_set_client  = utf8mb4 */ ;
/*!50003 SET character_set_results = utf8mb4 */ ;
/*!50003 SET collation_connection  = utf8mb4_0900_ai_ci */ ;
/*!50003 SET @saved_sql_mode       = @@sql_mode */ ;
/*!50003 SET sql_mode              = 'STRICT_TRANS_TABLES,NO_ENGINE_SUBSTITUTION' */ ;
DELIMITER @@
/*!50003 CREATE*/ /*!50017 DEFINER=`root`@`localhost`*/ /*!50003 TRIGGER `user_change_before_update` BEFORE UPDATE ON `user_change` FOR EACH ROW begin
	SET  NEW.cr_by = old.cr_by;
	SET  NEW.upd_by = get_wID();
end */@@
DELIMITER ;
/*!50003 SET sql_mode              = @saved_sql_mode */ ;
/*!50003 SET character_set_client  = @saved_cs_client */ ;
/*!50003 SET character_set_results = @saved_cs_results */ ;
/*!50003 SET collation_connection  = @saved_col_connection */ ;

--
-- Temporary view structure for view `user_has_serv`
--

DROP TABLE IF EXISTS `user_has_serv`;
/*!50001 DROP VIEW IF EXISTS `user_has_serv`*/;
SET @saved_cs_client     = @@character_set_client;
/*!50503 SET character_set_client = utf8mb4 */;
/*!50001 CREATE VIEW `user_has_serv` AS SELECT 
 1 AS `id`,
 1 AS `contracts_id`,
 1 AS `dep_id`,
 1 AS `client_id`,
 1 AS `serv_id`,
 1 AS `dep_has_worker_id`,
 1 AS `worker_id`,
 1 AS `vdate`,
 1 AS `quantity`,
 1 AS `note`,
 1 AS `create`,
 1 AS `ts`,
 1 AS `cr_by`,
 1 AS `upd_by`,
 1 AS `reported`,
 1 AS `wdate`,
 1 AS `overdid`,
 1 AS `prev_quantity`*/;
SET character_set_client = @saved_cs_client;

--
-- Table structure for table `worker`
--

DROP TABLE IF EXISTS `worker`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `worker` (
  `id` int unsigned NOT NULL AUTO_INCREMENT,
  `worker` varchar(255) NOT NULL,
  `user` varchar(16) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci DEFAULT NULL COMMENT 'user login',
  `note` varchar(145) DEFAULT NULL,
  `role_id` int unsigned NOT NULL DEFAULT '1' COMMENT 'default role',
  `dep_id` int unsigned NOT NULL DEFAULT '1',
  `archive` tinyint DEFAULT '0',
  PRIMARY KEY (`id`),
  UNIQUE KEY `worker_UNIQUE` (`worker`),
  KEY `fk_worker_roles1_idx` (`role_id`),
  KEY `fk_worker_dep1_idx` (`dep_id`),
  CONSTRAINT `fk_worker_roles1` FOREIGN KEY (`role_id`) REFERENCES `role` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=161 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;
/*!50003 SET @saved_cs_client      = @@character_set_client */ ;
/*!50003 SET @saved_cs_results     = @@character_set_results */ ;
/*!50003 SET @saved_col_connection = @@collation_connection */ ;
/*!50003 SET character_set_client  = utf8mb4 */ ;
/*!50003 SET character_set_results = utf8mb4 */ ;
/*!50003 SET collation_connection  = utf8mb4_0900_ai_ci */ ;
/*!50003 SET @saved_sql_mode       = @@sql_mode */ ;
/*!50003 SET sql_mode              = 'ONLY_FULL_GROUP_BY,STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_ENGINE_SUBSTITUTION' */ ;
DELIMITER @@
/*!50003 CREATE*/ /*!50017 DEFINER=`root`@`localhost`*/ /*!50003 TRIGGER `worker_AFTER_INSERT` AFTER INSERT ON `worker` FOR EACH ROW BEGIN
	INSERT INTO worker_settings (id) values (new.id);
END */@@
DELIMITER ;
/*!50003 SET sql_mode              = @saved_sql_mode */ ;
/*!50003 SET character_set_client  = @saved_cs_client */ ;
/*!50003 SET character_set_results = @saved_cs_results */ ;
/*!50003 SET collation_connection  = @saved_col_connection */ ;

--
-- Temporary view structure for view `worker_has_dep`
--

DROP TABLE IF EXISTS `worker_has_dep`;
/*!50001 DROP VIEW IF EXISTS `worker_has_dep`*/;
SET @saved_cs_client     = @@character_set_client;
/*!50503 SET character_set_client = utf8mb4 */;
/*!50001 CREATE VIEW `worker_has_dep` AS SELECT 
 1 AS `id`,
 1 AS `dep`*/;
SET character_set_client = @saved_cs_client;

--
-- Table structure for table `worker_settings`
--

DROP TABLE IF EXISTS `worker_settings`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `worker_settings` (
  `id` int unsigned NOT NULL,
  `last_tab` varchar(145) DEFAULT NULL,
  `last_dep` int unsigned DEFAULT NULL,
  `last_client` int unsigned DEFAULT NULL,
  `last_contr` int unsigned DEFAULT NULL,
  `last_client_filter` int DEFAULT NULL,
  `last_year` int DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping routines for database 'kcson'
--
/*!50003 DROP FUNCTION IF EXISTS `CHECK_OVERDID` */;
/*!50003 SET @saved_cs_client      = @@character_set_client */ ;
/*!50003 SET @saved_cs_results     = @@character_set_results */ ;
/*!50003 SET @saved_col_connection = @@collation_connection */ ;
/*!50003 SET character_set_client  = utf8mb4 */ ;
/*!50003 SET character_set_results = utf8mb4 */ ;
/*!50003 SET collation_connection  = utf8mb4_0900_ai_ci */ ;
/*!50003 SET @saved_sql_mode       = @@sql_mode */ ;
/*!50003 SET sql_mode              = 'ONLY_FULL_GROUP_BY,STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_ENGINE_SUBSTITUTION' */ ;
DELIMITER @@
CREATE DEFINER=`root`@`localhost` FUNCTION `CHECK_OVERDID`( CONTR  int, SERV int) RETURNS int
    READS SQL DATA
    DETERMINISTIC
    COMMENT 'check overdid return serv left \n    no existence check!!!'
BEGIN

    
return COALESCE((select  planned - filled 
from  contracts_has_serv where
  contracts_id = CONTR and  serv_id = SERV), 0);
  
END @@
DELIMITER ;
/*!50003 SET sql_mode              = @saved_sql_mode */ ;
/*!50003 SET character_set_client  = @saved_cs_client */ ;
/*!50003 SET character_set_results = @saved_cs_results */ ;
/*!50003 SET collation_connection  = @saved_col_connection */ ;
/*!50003 DROP FUNCTION IF EXISTS `GET_CONTR` */;
/*!50003 SET @saved_cs_client      = @@character_set_client */ ;
/*!50003 SET @saved_cs_results     = @@character_set_results */ ;
/*!50003 SET @saved_col_connection = @@collation_connection */ ;
/*!50003 SET character_set_client  = utf8mb4 */ ;
/*!50003 SET character_set_results = utf8mb4 */ ;
/*!50003 SET collation_connection  = utf8mb4_0900_ai_ci */ ;
/*!50003 SET @saved_sql_mode       = @@sql_mode */ ;
/*!50003 SET sql_mode              = 'STRICT_TRANS_TABLES,NO_ENGINE_SUBSTITUTION' */ ;
DELIMITER @@
CREATE DEFINER=`root`@`localhost` FUNCTION `GET_CONTR`(
 `idfio` INT, `vdate` date, `idep` int
) RETURNS int
    READS SQL DATA
    DETERMINISTIC
    COMMENT 'get idcontract at date'
BEGIN
	declare cc int (0);
	declare rr varchar (255);
	set cc = (select count(id) from contracts where ripso_id in  
		(select ripso_id from dep_has_ripso  where dep_id=idep) 
        and startdate <= vdate  and enddate  >= vdate and (blocked=0 or blocked is null) and client_id=idfio);
	if cc = 1 then 
		return (select id from contracts where ripso_id in  
			(select ripso_id from dep_has_ripso  where dep_id=idep) 
            and startdate <= vdate  and enddate  >= vdate and (blocked=0 or blocked is null ) and client_id=idfio);
	elseif cc = 0 then 
		set rr = CONCAT ('Нет договора в этот период для этого человека в этом отделении' , idfio , vdate, idep);
		SIGNAL SQLSTATE '45000' SET MESSAGE_TEXT = rr;
		return 0;
	else
		set rr = CONCAT ("Несколько договоров в этот период для этого человека в этом отделении",idfio , vdate, idep );
		SIGNAL SQLSTATE '45000' SET MESSAGE_TEXT  = rr;
		return -1;
	end if;
END @@
DELIMITER ;
/*!50003 SET sql_mode              = @saved_sql_mode */ ;
/*!50003 SET character_set_client  = @saved_cs_client */ ;
/*!50003 SET character_set_results = @saved_cs_results */ ;
/*!50003 SET collation_connection  = @saved_col_connection */ ;
/*!50003 DROP FUNCTION IF EXISTS `GET_DEP` */;
/*!50003 SET @saved_cs_client      = @@character_set_client */ ;
/*!50003 SET @saved_cs_results     = @@character_set_results */ ;
/*!50003 SET @saved_col_connection = @@collation_connection */ ;
/*!50003 SET character_set_client  = utf8mb4 */ ;
/*!50003 SET character_set_results = utf8mb4 */ ;
/*!50003 SET collation_connection  = utf8mb4_0900_ai_ci */ ;
/*!50003 SET @saved_sql_mode       = @@sql_mode */ ;
/*!50003 SET sql_mode              = 'ONLY_FULL_GROUP_BY,STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_ENGINE_SUBSTITUTION' */ ;
DELIMITER @@
CREATE DEFINER=`root`@`localhost` FUNCTION `GET_DEP`(
 `wrkID` INT
) RETURNS int
    READS SQL DATA
    SQL SECURITY INVOKER
    COMMENT 'get default department '
BEGIN
	
	declare dep_id int (0);
	set dep_id = (select last_dep from worker_settings  where id=wrkID);
	
    if dep_id is null then
		set dep_id = (select max(dep_id) from dep_has_worker  where worker_id=wrkID and (archive=0 or archive is null));
			if dep_id > 0  then 
				update worker_settings set last_dep=dep_id  where id=wrkID;
				return dep_id;
			else
				return 1;
				# 1 - undefined dep
			end if;
    end if;
    
	if dep_id > 0  then 
		return dep_id;
	else
		set dep_id = (select max(dep_id) from dep_has_worker  where worker_id=wrkID and (archive=0 or archive is null));
        if dep_id > 0  then 
			update worker_settings set last_dep=dep_id  where id=wrkID;
			return dep_id;
		else
			return 1;
			# 1 - undefined dep
		end if;
            
	end if;
END @@
DELIMITER ;
/*!50003 SET sql_mode              = @saved_sql_mode */ ;
/*!50003 SET character_set_client  = @saved_cs_client */ ;
/*!50003 SET character_set_results = @saved_cs_results */ ;
/*!50003 SET collation_connection  = @saved_col_connection */ ;
/*!50003 DROP FUNCTION IF EXISTS `get_last_client` */;
/*!50003 SET @saved_cs_client      = @@character_set_client */ ;
/*!50003 SET @saved_cs_results     = @@character_set_results */ ;
/*!50003 SET @saved_col_connection = @@collation_connection */ ;
/*!50003 SET character_set_client  = utf8mb4 */ ;
/*!50003 SET character_set_results = utf8mb4 */ ;
/*!50003 SET collation_connection  = utf8mb4_0900_ai_ci */ ;
/*!50003 SET @saved_sql_mode       = @@sql_mode */ ;
/*!50003 SET sql_mode              = 'ONLY_FULL_GROUP_BY,STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_ENGINE_SUBSTITUTION' */ ;
DELIMITER @@
CREATE DEFINER=`root`@`localhost` FUNCTION `get_last_client`() RETURNS int
    READS SQL DATA
    DETERMINISTIC
    COMMENT 'check overdid return serv left \n    no existence check!!!'
BEGIN
	
	
	
		
	return (select last_client from worker_settings where id = GET_WID());
    
END @@
DELIMITER ;
/*!50003 SET sql_mode              = @saved_sql_mode */ ;
/*!50003 SET character_set_client  = @saved_cs_client */ ;
/*!50003 SET character_set_results = @saved_cs_results */ ;
/*!50003 SET collation_connection  = @saved_col_connection */ ;
/*!50003 DROP FUNCTION IF EXISTS `get_last_contr` */;
/*!50003 SET @saved_cs_client      = @@character_set_client */ ;
/*!50003 SET @saved_cs_results     = @@character_set_results */ ;
/*!50003 SET @saved_col_connection = @@collation_connection */ ;
/*!50003 SET character_set_client  = utf8mb4 */ ;
/*!50003 SET character_set_results = utf8mb4 */ ;
/*!50003 SET collation_connection  = utf8mb4_0900_ai_ci */ ;
/*!50003 SET @saved_sql_mode       = @@sql_mode */ ;
/*!50003 SET sql_mode              = 'ONLY_FULL_GROUP_BY,STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_ENGINE_SUBSTITUTION' */ ;
DELIMITER @@
CREATE DEFINER=`root`@`localhost` FUNCTION `get_last_contr`() RETURNS int
    READS SQL DATA
    DETERMINISTIC
    COMMENT 'check overdid return serv left \n    no existence check!!!'
BEGIN
	
	
	
		
	return (select last_contr from worker_settings where id = GET_WID());
    
END @@
DELIMITER ;
/*!50003 SET sql_mode              = @saved_sql_mode */ ;
/*!50003 SET character_set_client  = @saved_cs_client */ ;
/*!50003 SET character_set_results = @saved_cs_results */ ;
/*!50003 SET collation_connection  = @saved_col_connection */ ;
/*!50003 DROP FUNCTION IF EXISTS `GET_wID` */;
/*!50003 SET @saved_cs_client      = @@character_set_client */ ;
/*!50003 SET @saved_cs_results     = @@character_set_results */ ;
/*!50003 SET @saved_col_connection = @@collation_connection */ ;
/*!50003 SET character_set_client  = utf8mb4 */ ;
/*!50003 SET character_set_results = utf8mb4 */ ;
/*!50003 SET collation_connection  = utf8mb4_0900_ai_ci */ ;
/*!50003 SET @saved_sql_mode       = @@sql_mode */ ;
/*!50003 SET sql_mode              = 'ONLY_FULL_GROUP_BY,STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_ENGINE_SUBSTITUTION' */ ;
DELIMITER @@
CREATE DEFINER=`root`@`localhost` FUNCTION `GET_wID`(
) RETURNS int
    READS SQL DATA
    SQL SECURITY INVOKER
    COMMENT 'get default department '
BEGIN
	return (select id from worker w where w.user=SUBSTRING_INDEX(user(), '@', 1));
END @@
DELIMITER ;
/*!50003 SET sql_mode              = @saved_sql_mode */ ;
/*!50003 SET character_set_client  = @saved_cs_client */ ;
/*!50003 SET character_set_results = @saved_cs_results */ ;
/*!50003 SET collation_connection  = @saved_col_connection */ ;
/*!50003 DROP FUNCTION IF EXISTS `GET_YEAR` */;
/*!50003 SET @saved_cs_client      = @@character_set_client */ ;
/*!50003 SET @saved_cs_results     = @@character_set_results */ ;
/*!50003 SET @saved_col_connection = @@collation_connection */ ;
/*!50003 SET character_set_client  = utf8mb4 */ ;
/*!50003 SET character_set_results = utf8mb4 */ ;
/*!50003 SET collation_connection  = utf8mb4_0900_ai_ci */ ;
/*!50003 SET @saved_sql_mode       = @@sql_mode */ ;
/*!50003 SET sql_mode              = 'ONLY_FULL_GROUP_BY,STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_ENGINE_SUBSTITUTION' */ ;
DELIMITER @@
CREATE DEFINER=`root`@`localhost` FUNCTION `GET_YEAR`(
 `wrkID` INT
) RETURNS int
    READS SQL DATA
    SQL SECURITY INVOKER
    COMMENT 'get current year '
BEGIN
	declare var int (0);
	
	set var = (select last_year from worker_settings  where id=wrkID);
	
	if var > 0 then 
		return var;
	else
		set var = year(current_date());
        if var > 0  then 
			return var;
		else
			return 1;
			# 1 - undefined dep
        end if;
	end if;
END @@
DELIMITER ;
/*!50003 SET sql_mode              = @saved_sql_mode */ ;
/*!50003 SET character_set_client  = @saved_cs_client */ ;
/*!50003 SET character_set_results = @saved_cs_results */ ;
/*!50003 SET collation_connection  = @saved_col_connection */ ;
/*!50003 DROP FUNCTION IF EXISTS `IS_ADMIN` */;
/*!50003 SET @saved_cs_client      = @@character_set_client */ ;
/*!50003 SET @saved_cs_results     = @@character_set_results */ ;
/*!50003 SET @saved_col_connection = @@collation_connection */ ;
/*!50003 SET character_set_client  = utf8mb4 */ ;
/*!50003 SET character_set_results = utf8mb4 */ ;
/*!50003 SET collation_connection  = utf8mb4_0900_ai_ci */ ;
/*!50003 SET @saved_sql_mode       = @@sql_mode */ ;
/*!50003 SET sql_mode              = 'STRICT_TRANS_TABLES,NO_ENGINE_SUBSTITUTION' */ ;
DELIMITER @@
CREATE DEFINER=`root`@`localhost` FUNCTION `IS_ADMIN`() RETURNS int
    DETERMINISTIC
begin
	DECLARE CONTINUE HANDLER FOR NOT FOUND return 0;

if (STRCMP( 'root' , SUBSTRING_INDEX(user(),'@',1)) = 0) then
	return 1;
end if;

   -- get role of current user
    set @is_admin = (select true from dep_has_worker dhw inner join  worker w  on
		w.id = dhw.worker_id
		where w.`user` = SUBSTRING_INDEX(user(),'@',1)
		and (dhw.role_id  in  (7, 8) )
		order by dhw.role_id desc
		limit 1);
	
	if COALESCE( @is_admin, False)  then
		return 1;
	else
		return 0;
	end if;
		
END @@
DELIMITER ;
/*!50003 SET sql_mode              = @saved_sql_mode */ ;
/*!50003 SET character_set_client  = @saved_cs_client */ ;
/*!50003 SET character_set_results = @saved_cs_results */ ;
/*!50003 SET collation_connection  = @saved_col_connection */ ;
/*!50003 DROP FUNCTION IF EXISTS `IS_CUR_DEP` */;
/*!50003 SET @saved_cs_client      = @@character_set_client */ ;
/*!50003 SET @saved_cs_results     = @@character_set_results */ ;
/*!50003 SET @saved_col_connection = @@collation_connection */ ;
/*!50003 SET character_set_client  = utf8mb4 */ ;
/*!50003 SET character_set_results = utf8mb4 */ ;
/*!50003 SET collation_connection  = utf8mb4_0900_ai_ci */ ;
/*!50003 SET @saved_sql_mode       = @@sql_mode */ ;
/*!50003 SET sql_mode              = 'ONLY_FULL_GROUP_BY,STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_ENGINE_SUBSTITUTION' */ ;
DELIMITER @@
CREATE DEFINER=`root`@`localhost` FUNCTION `IS_CUR_DEP`(
 `depID_par` INT
) RETURNS int
    READS SQL DATA
    SQL SECURITY INVOKER
    COMMENT 'check is current dep (support complex_dep)'
BEGIN
	declare wrkID int default GET_WID();
	declare depID int default GET_DEP(wrkID);
    declare complexDep int;
    
    set complexDep=(select complex_dep_id from dep where id = depID);
    if coalesce(complexDep, 0)  = 0 then
		if depID = depID_par then 
			return 1;
		else
			return 0;
        end if;
	else
		return (select depID_par in (select dep_id from complex_dep_has_dep where complexDep = complex_dep_id));
    end if;
END @@
DELIMITER ;
/*!50003 SET sql_mode              = @saved_sql_mode */ ;
/*!50003 SET character_set_client  = @saved_cs_client */ ;
/*!50003 SET character_set_results = @saved_cs_results */ ;
/*!50003 SET collation_connection  = @saved_col_connection */ ;
/*!50003 DROP FUNCTION IF EXISTS `IS_CUR_DEP_STATIC` */;
/*!50003 SET @saved_cs_client      = @@character_set_client */ ;
/*!50003 SET @saved_cs_results     = @@character_set_results */ ;
/*!50003 SET @saved_col_connection = @@collation_connection */ ;
/*!50003 SET character_set_client  = utf8mb4 */ ;
/*!50003 SET character_set_results = utf8mb4 */ ;
/*!50003 SET collation_connection  = utf8mb4_0900_ai_ci */ ;
/*!50003 SET @saved_sql_mode       = @@sql_mode */ ;
/*!50003 SET sql_mode              = 'STRICT_TRANS_TABLES,NO_ENGINE_SUBSTITUTION' */ ;
DELIMITER @@
CREATE DEFINER=`root`@`localhost` FUNCTION `IS_CUR_DEP_STATIC`(
 `depID_par` INT
) RETURNS int
    READS SQL DATA
    SQL SECURITY INVOKER
    COMMENT 'check is current dep (support complex_dep)'
BEGIN
	declare wrkID int default GET_WID();
	declare depID int;
    
    declare complexDep int;
    
    set depID = (select last_dep from worker_settings  where id=wrkID);
    set complexDep=(
		select complex_dep_id from dep d join worker_settings w on  d.id = w.last_dep where d.id=depID    and   w.id=wrkID
    );
    if coalesce(complexDep, 0)  = 0 then
		if depID = depID_par then 
			return 1;
		else
			return 0;
        end if;
	else
		return (select depID_par in (select dep_id from complex_dep_has_dep where complexDep = complex_dep_id
        ));
    end if;
END @@
DELIMITER ;
/*!50003 SET sql_mode              = @saved_sql_mode */ ;
/*!50003 SET character_set_client  = @saved_cs_client */ ;
/*!50003 SET character_set_results = @saved_cs_results */ ;
/*!50003 SET collation_connection  = @saved_col_connection */ ;
/*!50003 DROP FUNCTION IF EXISTS `IS_SPECIALIST` */;
/*!50003 SET @saved_cs_client      = @@character_set_client */ ;
/*!50003 SET @saved_cs_results     = @@character_set_results */ ;
/*!50003 SET @saved_col_connection = @@collation_connection */ ;
/*!50003 SET character_set_client  = utf8mb4 */ ;
/*!50003 SET character_set_results = utf8mb4 */ ;
/*!50003 SET collation_connection  = utf8mb4_0900_ai_ci */ ;
/*!50003 SET @saved_sql_mode       = @@sql_mode */ ;
/*!50003 SET sql_mode              = 'STRICT_TRANS_TABLES,NO_ENGINE_SUBSTITUTION' */ ;
DELIMITER @@
CREATE DEFINER=`root`@`localhost` FUNCTION `IS_SPECIALIST`() RETURNS int
    DETERMINISTIC
begin
	
	DECLARE CONTINUE HANDLER FOR NOT FOUND return 0;

if (STRCMP( 'root' , SUBSTRING_INDEX(user(),'@',1)) = 0) then
	return 1;
end if;

   -- get role of current user
    set @is_spe = (select true from dep_has_worker dhw inner join  worker w  on
		w.id = dhw.worker_id
		where w.`user` = SUBSTRING_INDEX(user(),'@',1)
		and (dhw.role_id  in  (4, 5, 6, 7, 8) )
		order by dhw.role_id desc
		limit 1);
	
	if COALESCE( @is_spe, False)  then
		return 1;
	else
		return 0;
	end if;
END @@
DELIMITER ;
/*!50003 SET sql_mode              = @saved_sql_mode */ ;
/*!50003 SET character_set_client  = @saved_cs_client */ ;
/*!50003 SET character_set_results = @saved_cs_results */ ;
/*!50003 SET collation_connection  = @saved_col_connection */ ;
/*!50003 DROP FUNCTION IF EXISTS `SET_DEP` */;
/*!50003 SET @saved_cs_client      = @@character_set_client */ ;
/*!50003 SET @saved_cs_results     = @@character_set_results */ ;
/*!50003 SET @saved_col_connection = @@collation_connection */ ;
/*!50003 SET character_set_client  = utf8mb4 */ ;
/*!50003 SET character_set_results = utf8mb4 */ ;
/*!50003 SET collation_connection  = utf8mb4_0900_ai_ci */ ;
/*!50003 SET @saved_sql_mode       = @@sql_mode */ ;
/*!50003 SET sql_mode              = 'STRICT_TRANS_TABLES,NO_ENGINE_SUBSTITUTION' */ ;
DELIMITER @@
CREATE DEFINER=`root`@`localhost` FUNCTION `SET_DEP`(
	`depId` INT
) RETURNS int
    MODIFIES SQL DATA
    DETERMINISTIC
    COMMENT 'set default department (with checking is it possible)'
BEGIN
	declare wrkID int ;
	declare res int default 0;
	set  wrkID=get_WID();

	select IS_ADMIN() into @allow;
	if (@allow = 1) then
		set res = (select distinct dep_id from dep_has_worker  where (archive=0 or archive is null));
	else
		set res = (select distinct dep_id from dep_has_worker  where worker_id=wrkID and (archive=0 or archive is null));
	end if;

	if res > 0 then 
		update worker_settings set last_dep=depId where id = wrkID;
		# call GET_PRIVILEGES();
		# TODO: set role for invoker
		# set role info;
		# call DROP_ROLES;
		

	
		#update worker_has_dep set active=0 where(worker_id=wrkID);
		#update worker_has_dep set active=1 where(worker_id=wrkID and dep_id=depId);
		return depId;
	else
		return 0;
	end if;
END @@
DELIMITER ;
/*!50003 SET sql_mode              = @saved_sql_mode */ ;
/*!50003 SET character_set_client  = @saved_cs_client */ ;
/*!50003 SET character_set_results = @saved_cs_results */ ;
/*!50003 SET collation_connection  = @saved_col_connection */ ;
/*!50003 DROP FUNCTION IF EXISTS `set_last_client` */;
/*!50003 SET @saved_cs_client      = @@character_set_client */ ;
/*!50003 SET @saved_cs_results     = @@character_set_results */ ;
/*!50003 SET @saved_col_connection = @@collation_connection */ ;
/*!50003 SET character_set_client  = utf8mb4 */ ;
/*!50003 SET character_set_results = utf8mb4 */ ;
/*!50003 SET collation_connection  = utf8mb4_0900_ai_ci */ ;
/*!50003 SET @saved_sql_mode       = @@sql_mode */ ;
/*!50003 SET sql_mode              = 'ONLY_FULL_GROUP_BY,STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_ENGINE_SUBSTITUTION' */ ;
DELIMITER @@
CREATE DEFINER=`root`@`localhost` FUNCTION `set_last_client`(client int) RETURNS int
    DETERMINISTIC
    COMMENT 'check overdid return serv left \n    no existence check!!!'
BEGIN

	update worker_settings set last_client=client where id = GET_WID();
    return 1;
    
END @@
DELIMITER ;
/*!50003 SET sql_mode              = @saved_sql_mode */ ;
/*!50003 SET character_set_client  = @saved_cs_client */ ;
/*!50003 SET character_set_results = @saved_cs_results */ ;
/*!50003 SET collation_connection  = @saved_col_connection */ ;
/*!50003 DROP FUNCTION IF EXISTS `set_last_contr` */;
/*!50003 SET @saved_cs_client      = @@character_set_client */ ;
/*!50003 SET @saved_cs_results     = @@character_set_results */ ;
/*!50003 SET @saved_col_connection = @@collation_connection */ ;
/*!50003 SET character_set_client  = utf8mb4 */ ;
/*!50003 SET character_set_results = utf8mb4 */ ;
/*!50003 SET collation_connection  = utf8mb4_0900_ai_ci */ ;
/*!50003 SET @saved_sql_mode       = @@sql_mode */ ;
/*!50003 SET sql_mode              = 'ONLY_FULL_GROUP_BY,STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_ENGINE_SUBSTITUTION' */ ;
DELIMITER @@
CREATE DEFINER=`root`@`localhost` FUNCTION `set_last_contr`(contr int) RETURNS int
    DETERMINISTIC
    COMMENT 'check overdid return serv left \n    no existence check!!!'
BEGIN

	update worker_settings set last_contr=contr where id = GET_WID();
    return 1;
END @@
DELIMITER ;
/*!50003 SET sql_mode              = @saved_sql_mode */ ;
/*!50003 SET character_set_client  = @saved_cs_client */ ;
/*!50003 SET character_set_results = @saved_cs_results */ ;
/*!50003 SET collation_connection  = @saved_col_connection */ ;
/*!50003 DROP FUNCTION IF EXISTS `set_last_dep` */;
/*!50003 SET @saved_cs_client      = @@character_set_client */ ;
/*!50003 SET @saved_cs_results     = @@character_set_results */ ;
/*!50003 SET @saved_col_connection = @@collation_connection */ ;
/*!50003 SET character_set_client  = utf8mb4 */ ;
/*!50003 SET character_set_results = utf8mb4 */ ;
/*!50003 SET collation_connection  = utf8mb4_0900_ai_ci */ ;
/*!50003 SET @saved_sql_mode       = @@sql_mode */ ;
/*!50003 SET sql_mode              = 'STRICT_TRANS_TABLES,NO_ENGINE_SUBSTITUTION' */ ;
DELIMITER @@
CREATE DEFINER=`root`@`localhost` FUNCTION `set_last_dep`(dep int) RETURNS int
    DETERMINISTIC
BEGIN
	declare ret int ;
    set ret = (select SET_DEP(dep));
    if ret = 0 then
		set ret = get_dep(GET_WID()) ;
		update worker_settings set last_dep=get_dep(GET_WID()) where id = GET_WID();
    end if;
	
    return ret;
END @@
DELIMITER ;
/*!50003 SET sql_mode              = @saved_sql_mode */ ;
/*!50003 SET character_set_client  = @saved_cs_client */ ;
/*!50003 SET character_set_results = @saved_cs_results */ ;
/*!50003 SET collation_connection  = @saved_col_connection */ ;
/*!50003 DROP FUNCTION IF EXISTS `SET_YEAR` */;
/*!50003 SET @saved_cs_client      = @@character_set_client */ ;
/*!50003 SET @saved_cs_results     = @@character_set_results */ ;
/*!50003 SET @saved_col_connection = @@collation_connection */ ;
/*!50003 SET character_set_client  = utf8mb4 */ ;
/*!50003 SET character_set_results = utf8mb4 */ ;
/*!50003 SET collation_connection  = utf8mb4_0900_ai_ci */ ;
/*!50003 SET @saved_sql_mode       = @@sql_mode */ ;
/*!50003 SET sql_mode              = 'STRICT_TRANS_TABLES,NO_ENGINE_SUBSTITUTION' */ ;
DELIMITER @@
CREATE DEFINER=`root`@`localhost` FUNCTION `SET_YEAR`(
 `yr` INT
) RETURNS int
    READS SQL DATA
    COMMENT 'set current year '
BEGIN
	update worker_settings set last_year=yr where id = GET_WID();
    return yr;
END @@
DELIMITER ;
/*!50003 SET sql_mode              = @saved_sql_mode */ ;
/*!50003 SET character_set_client  = @saved_cs_client */ ;
/*!50003 SET character_set_results = @saved_cs_results */ ;
/*!50003 SET collation_connection  = @saved_col_connection */ ;
/*!50003 DROP FUNCTION IF EXISTS `SPLIT_STR` */;
/*!50003 SET @saved_cs_client      = @@character_set_client */ ;
/*!50003 SET @saved_cs_results     = @@character_set_results */ ;
/*!50003 SET @saved_col_connection = @@collation_connection */ ;
/*!50003 SET character_set_client  = utf8mb4 */ ;
/*!50003 SET character_set_results = utf8mb4 */ ;
/*!50003 SET collation_connection  = utf8mb4_0900_ai_ci */ ;
/*!50003 SET @saved_sql_mode       = @@sql_mode */ ;
/*!50003 SET sql_mode              = 'ONLY_FULL_GROUP_BY,STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_ENGINE_SUBSTITUTION' */ ;
DELIMITER @@
CREATE DEFINER=`root`@`localhost` FUNCTION `SPLIT_STR`(
  x VARCHAR(4096),
  delim VARCHAR(100),
  pos INT
) RETURNS varchar(4096) CHARSET utf8mb4
    DETERMINISTIC
    SQL SECURITY INVOKER
RETURN REPLACE(SUBSTRING(SUBSTRING_INDEX(x, delim, pos),
       LENGTH(SUBSTRING_INDEX(x, delim, pos -1)) + 1),
       delim, '') @@
DELIMITER ;
/*!50003 SET sql_mode              = @saved_sql_mode */ ;
/*!50003 SET character_set_client  = @saved_cs_client */ ;
/*!50003 SET character_set_results = @saved_cs_results */ ;
/*!50003 SET collation_connection  = @saved_col_connection */ ;
/*!50003 DROP FUNCTION IF EXISTS `SPLIT_STR_ARR_LEN` */;
/*!50003 SET @saved_cs_client      = @@character_set_client */ ;
/*!50003 SET @saved_cs_results     = @@character_set_results */ ;
/*!50003 SET @saved_col_connection = @@collation_connection */ ;
/*!50003 SET character_set_client  = utf8mb4 */ ;
/*!50003 SET character_set_results = utf8mb4 */ ;
/*!50003 SET collation_connection  = utf8mb4_0900_ai_ci */ ;
/*!50003 SET @saved_sql_mode       = @@sql_mode */ ;
/*!50003 SET sql_mode              = 'ONLY_FULL_GROUP_BY,STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_ENGINE_SUBSTITUTION' */ ;
DELIMITER @@
CREATE DEFINER=`root`@`localhost` FUNCTION `SPLIT_STR_ARR_LEN`(
  x VARCHAR(4096),
  delim VARCHAR(100)
) RETURNS varchar(4096) CHARSET utf8mb4
    DETERMINISTIC
    SQL SECURITY INVOKER
RETURN ROUND (   
        (
             CHAR_LENGTH(x)
            -  CHAR_LENGTH( REPLACE ( x, delim, "") ) 
        ) /  CHAR_LENGTH(delim)  ) @@
DELIMITER ;
/*!50003 SET sql_mode              = @saved_sql_mode */ ;
/*!50003 SET character_set_client  = @saved_cs_client */ ;
/*!50003 SET character_set_results = @saved_cs_results */ ;
/*!50003 SET collation_connection  = @saved_col_connection */ ;
/*!50003 DROP PROCEDURE IF EXISTS `contract_pay_inmonth` */;
/*!50003 SET @saved_cs_client      = @@character_set_client */ ;
/*!50003 SET @saved_cs_results     = @@character_set_results */ ;
/*!50003 SET @saved_col_connection = @@collation_connection */ ;
/*!50003 SET character_set_client  = utf8mb4 */ ;
/*!50003 SET character_set_results = utf8mb4 */ ;
/*!50003 SET collation_connection  = utf8mb4_0900_ai_ci */ ;
/*!50003 SET @saved_sql_mode       = @@sql_mode */ ;
/*!50003 SET sql_mode              = 'STRICT_TRANS_TABLES,NO_ENGINE_SUBSTITUTION' */ ;
DELIMITER @@
CREATE DEFINER=`root`@`localhost` PROCEDURE `contract_pay_inmonth`( IN UID INT, IN STARTDATE DATE, IN ENDDATE DATE)
BEGIN
	IF EXISTS (SELECT 1 FROM `main` where client_id = UID and vdate BETWEEN STARTDATE AND ENDDATE)
	THEN
		
	        with ai as (
	        SELECT 
	            perc, pddate
	        FROM
	            add_info pd
	                JOIN
	            contracts c ON pd.contracts_id = c.id
	        WHERE
	            c.client_id = UID AND pddate <= ENDDATE
	        ORDER BY pddate DESC
	        LIMIT 1
	                )
	
	    SELECT 
	        SUM(((`f`.`perc` * `f`.`quantity`) * `f`.`price`)) AS to_pay,
	        f.perc,
	        `f`.`quantity` as quantity,
	        f.client_id,
	        f.servform_id,
	        f.contracts,
	        f.contracts_id,       
	        f.startdate,
	        f.enddate,     
	        MONTH(vdate) AS vdate_m,
	        YEAR(vdate) AS vdate_y
	    FROM
	        (SELECT 
	            `m`.`id` AS `id`,
	                `m`.`contracts_id` AS `contracts_id`,
	                `m`.`dep_id` AS `dep_id`,
	                `m`.`client_id` AS `client_id`,
	                `m`.`serv_id` AS `serv_id`,
	                `m`.`vdate` AS `vdate`,
	                `m`.`quantity` AS `quantity`,
	                c.contracts,
	                c.startdate,
	                c.enddate,
	                (SELECT 
	                        perc
	                    FROM
	                        `ai`) AS `perc`,
	                `s`.`price` AS `price`,
	                `r`.`servform_id` AS `servform_id`
	        FROM
	            (((`main` `m`
	        JOIN `serv` `s` ON ((`m`.`serv_id` = `s`.`id`)))
	        JOIN `contracts` `c` ON ((`m`.`contracts_id` = `c`.`id`)))
	        JOIN `ripso` `r` ON ((`c`.`ripso_id` = `r`.`id`)))) `f`
	    WHERE
	        client_id = UID
	            AND vdate BETWEEN STARTDATE AND ENDDATE
	    GROUP BY client_id, vdate_m , vdate_y, servform_id, perc, f.contracts_id;

	  
	else 
	
		with ai as (
			select
				perc,
				pddate
			from
				add_info pd
			join contracts c on
				pd.contracts_id = c.id
			where
				c.client_id = UID
				and pddate <= ENDDATE
			order by
				pddate desc
			limit 1 )
	
	    select
			0 as to_pay,
			 (SELECT 
		                        perc
		                    FROM
		                        `ai`) AS `perc`,
	        0 AS `price`,
			0 as quantity,
			client_id,
			servform_id,
			contracts,
			c.id as contracts_id,
			startdate,
			enddate,
			month(STARTDATE) as vdate_m,
			year(STARTDATE) as vdate_y
		from
			contracts c JOIN `ripso` `r` ON ((`c`.`ripso_id` = `r`.`id`))
		where
			c.client_id = UID
			and 
			c.startdate <= ENDDATE and
			c.enddate >= STARTDATE;
	end if;
	
end @@
DELIMITER ;
/*!50003 SET sql_mode              = @saved_sql_mode */ ;
/*!50003 SET character_set_client  = @saved_cs_client */ ;
/*!50003 SET character_set_results = @saved_cs_results */ ;
/*!50003 SET collation_connection  = @saved_col_connection */ ;
/*!50003 DROP PROCEDURE IF EXISTS `CREATE_PIVOT` */;
/*!50003 SET @saved_cs_client      = @@character_set_client */ ;
/*!50003 SET @saved_cs_results     = @@character_set_results */ ;
/*!50003 SET @saved_col_connection = @@collation_connection */ ;
/*!50003 SET character_set_client  = utf8mb4 */ ;
/*!50003 SET character_set_results = utf8mb4 */ ;
/*!50003 SET collation_connection  = utf8mb4_0900_ai_ci */ ;
/*!50003 SET @saved_sql_mode       = @@sql_mode */ ;
/*!50003 SET sql_mode              = 'STRICT_TRANS_TABLES,NO_ENGINE_SUBSTITUTION' */ ;
DELIMITER @@
CREATE DEFINER=`reporter`@`localhost` PROCEDURE `CREATE_PIVOT`(
    IN tbl_qry VARCHAR(10000),       -- table name (or db.tbl)
    IN base_cols VARCHAR(200),       -- column(s) on the left, separated by commas
    IN pivot_col VARCHAR(64),        -- name of column to put across the top
    IN tally_col VARCHAR(64),        -- name of column to SUM up
    IN where_clause VARCHAR(1000),   -- empty string or "WHERE ..."
    IN order_by VARCHAR(99),         -- empty string or "ORDER BY ..."; usually the base_cols
    IN w_rollup VARCHAR(99) , 
    IN temp_table_name VARCHAR(99) 
    )
    DETERMINISTIC
BEGIN 
    call CREATE_PIVOT_(tbl_qry, base_cols, pivot_col, tally_col, where_clause, order_by, w_rollup, temp_table_name, true, False );
END @@
DELIMITER ;
/*!50003 SET sql_mode              = @saved_sql_mode */ ;
/*!50003 SET character_set_client  = @saved_cs_client */ ;
/*!50003 SET character_set_results = @saved_cs_results */ ;
/*!50003 SET collation_connection  = @saved_col_connection */ ;
/*!50003 DROP PROCEDURE IF EXISTS `CREATE_PIVOT_` */;
/*!50003 SET @saved_cs_client      = @@character_set_client */ ;
/*!50003 SET @saved_cs_results     = @@character_set_results */ ;
/*!50003 SET @saved_col_connection = @@collation_connection */ ;
/*!50003 SET character_set_client  = utf8mb4 */ ;
/*!50003 SET character_set_results = utf8mb4 */ ;
/*!50003 SET collation_connection  = utf8mb4_0900_ai_ci */ ;
/*!50003 SET @saved_sql_mode       = @@sql_mode */ ;
/*!50003 SET sql_mode              = 'STRICT_TRANS_TABLES,NO_ENGINE_SUBSTITUTION' */ ;
DELIMITER @@
CREATE DEFINER=`reporter`@`localhost` PROCEDURE `CREATE_PIVOT_`(
    IN tbl_qry VARCHAR(10000),       -- table name (or db.tbl)
    IN base_cols VARCHAR(200),       -- column(s) on the left, separated by commas
    IN pivot_col VARCHAR(64),        -- name of column to put across the top
    IN tally_col VARCHAR(64),        -- name of column to SUM up
    IN where_clause VARCHAR(1000),   -- empty string or "WHERE ..."
    IN order_by VARCHAR(99),         -- empty string or "ORDER BY ..."; usually the base_cols
    IN w_rollup VARCHAR(99) , 
    IN temp_table_name VARCHAR(99) ,
    IN sum_not_count bool , 
    IN debug bool 
    )
    DETERMINISTIC
BEGIN 
    #############################
    # prepares
    # ---------------------------
    declare base_col VARCHAR(200);
	declare base_cols_grouping VARCHAR(10000)  ;
	declare i int  ;
	SET debug = IFNULL(debug, False);
	SET sum_not_count = IFNULL(sum_not_count, True);
    SET SESSION group_concat_max_len = 50000;   -- just in case
    
    #############################
    # prepare subquery  @cc4
    # ---------------------------
    SET @subq = CONCAT('SELECT DISTINCT ', pivot_col, ' AS val ',
                    ' FROM ', tbl_qry, ' ', where_clause, ' ORDER BY 1');
	if sum_not_count then
    	SET @cc1 = "CONCAT('SUM(IF(&p = ', &v, ', &t, 0)) AS ', &v)";
    else
    	SET @cc1 = "CONCAT('COUNT(IF(&p = ', &v, ', &t, 0)) AS ', &v)";
    end if;
    SET @cc2 = REPLACE(@cc1, '&p', pivot_col);
    SET @cc3 = REPLACE(@cc2, '&t', tally_col);
    
    SET @qval = CONCAT("'\"', val, '\"'");
    
    SET @cc4 = REPLACE(@cc3, '&v', @qval);
    # select @cc4;

    #############################
    # get  @sums
    # ---------------------------
    if true then
	    SET @stmt = CONCAT(
	            'SELECT  GROUP_CONCAT(', @cc4, ' SEPARATOR ",\n")  INTO @sums',
	            ' FROM ( ', @subq, ' ) AS top');
		#SELECT @stmt;
	    PREPARE _sql FROM @stmt;
	    EXECUTE _sql;                      -- 2nd step: build SQL for columns
	    DEALLOCATE PREPARE _sql;
    end if;
   
	#SELECT      @sums;
    #############################
    # prepare list of columns
    # ---------------------------
    -- use base_cols with grouping
#select base_cols;
    set base_col = SPLIT_STR(base_cols,",",1) ;
    set base_cols_grouping = CONCAT("IF(GROUPING(", base_col, "), 'Total', ", base_col, ") AS ", base_col );
    #for i in SPLIT_STR_ARR_LEN(base_cols)    ;
    set i=1;
    WHILE i <= SPLIT_STR_ARR_LEN(base_cols, ",") DO
        set i = i+1;
		set base_col = SPLIT_STR(base_cols,",",i) ;
		set base_cols_grouping = CONCAT(base_cols_grouping,  ", " , "IF(GROUPING(", base_col, "), 'Total', ", base_col, ") AS ", base_col); 
    END WHILE;
    #SELECT base_cols_grouping;
    -- 3rd: Construct the query and perform it
    
    #############################
    # delete old table
    # ---------------------------
SET @stmt11 = CONCAT( ' drop temporary table   IF EXISTS ', temp_table_name);
    PREPARE _sql FROM @stmt11;
    EXECUTE _sql;                     -- The resulting pivot table ouput
    DEALLOCATE PREPARE _sql;
SET @stmt11 = CONCAT( ' drop temporary table   IF EXISTS kcson_tmp.', temp_table_name);
    PREPARE _sql FROM @stmt11;
    EXECUTE _sql;                     -- The resulting pivot table ouput
    DEALLOCATE PREPARE _sql;
    
    #############################
    # create temporary table
    # ---------------------------
    SET @stmt2 = CONCAT(
            ' create temporary table ', temp_table_name, ' SELECT ',
                base_cols_grouping, ',\n',
                @sums,
                ',\n SUM(', tally_col, ') AS Total'
            '\n FROM ', tbl_qry, ' ',
            where_clause,
            ' GROUP BY ', base_cols,
            ' \n ', w_rollup,
            ' \n ', order_by
        );
    #SELECT @stmt2;                    -- The statement that generates the result


    #############################
    # debug
    # ---------------------------
    if debug then
	    SELECT @stmt2; 
    end if; 
    #############################
    # create copy of temporary table
    # ---------------------------
    -- copy in schema with select right
    PREPARE _sql FROM @stmt2;
    EXECUTE _sql;                     -- The resulting pivot table ouput
    DEALLOCATE PREPARE _sql;
         SET @stmt2 = CONCAT(
            ' create temporary table kcson_tmp.', temp_table_name, ' SELECT ',
                base_cols, ',\n',
                @sums,
                ',\n SUM(', tally_col, ') AS Total'
            '\n FROM ', tbl_qry, ' ',
            where_clause,
            ' GROUP BY ', base_cols,
            ' \n ', w_rollup,
            ' \n ', order_by
        );
#SELECT @stmt2;                    -- The statement that generates the result
    PREPARE _sql FROM @stmt2;
    EXECUTE _sql;                     -- The resulting pivot table ouput
    DEALLOCATE PREPARE _sql;
   
    #############################
    # select temporary table
    # ---------------------------
SET @stmt3 = CONCAT( ' SELECT * from ', temp_table_name);
    PREPARE _sql FROM @stmt3;
    EXECUTE _sql;                     -- The resulting pivot table ouput
    DEALLOCATE PREPARE _sql;

    -- For debugging / tweaking, SELECT the various @variables after CALLing.
END @@
DELIMITER ;
/*!50003 SET sql_mode              = @saved_sql_mode */ ;
/*!50003 SET character_set_client  = @saved_cs_client */ ;
/*!50003 SET character_set_results = @saved_cs_results */ ;
/*!50003 SET collation_connection  = @saved_col_connection */ ;
/*!50003 DROP PROCEDURE IF EXISTS `debug_msg` */;
/*!50003 SET @saved_cs_client      = @@character_set_client */ ;
/*!50003 SET @saved_cs_results     = @@character_set_results */ ;
/*!50003 SET @saved_col_connection = @@collation_connection */ ;
/*!50003 SET character_set_client  = utf8mb4 */ ;
/*!50003 SET character_set_results = utf8mb4 */ ;
/*!50003 SET collation_connection  = utf8mb4_0900_ai_ci */ ;
/*!50003 SET @saved_sql_mode       = @@sql_mode */ ;
/*!50003 SET sql_mode              = 'STRICT_TRANS_TABLES,NO_ENGINE_SUBSTITUTION' */ ;
DELIMITER @@
CREATE DEFINER=`root`@`localhost` PROCEDURE `debug_msg`(msg VARCHAR(255))
BEGIN

    select concat('** ', msg) AS '** DEBUG:';

END @@
DELIMITER ;
/*!50003 SET sql_mode              = @saved_sql_mode */ ;
/*!50003 SET character_set_client  = @saved_cs_client */ ;
/*!50003 SET character_set_results = @saved_cs_results */ ;
/*!50003 SET collation_connection  = @saved_col_connection */ ;
/*!50003 DROP PROCEDURE IF EXISTS `dep_serv_total` */;
/*!50003 SET @saved_cs_client      = @@character_set_client */ ;
/*!50003 SET @saved_cs_results     = @@character_set_results */ ;
/*!50003 SET @saved_col_connection = @@collation_connection */ ;
/*!50003 SET character_set_client  = utf8mb4 */ ;
/*!50003 SET character_set_results = utf8mb4 */ ;
/*!50003 SET collation_connection  = utf8mb4_0900_ai_ci */ ;
/*!50003 SET @saved_sql_mode       = @@sql_mode */ ;
/*!50003 SET sql_mode              = 'ONLY_FULL_GROUP_BY,STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_ENGINE_SUBSTITUTION' */ ;
DELIMITER @@
CREATE DEFINER=`root`@`localhost` PROCEDURE `dep_serv_total`()
    DETERMINISTIC
BEGIN
	call CREATE_PIVOT("
	(select tnum, s.id, client_id, serv_id , quantity
	from main_NZ m inner join serv s on m.serv_id=s.id
	where dep_id = GET_DEP(GET_wID())
	)  main1",

	 "client_id", "tnum", "quantity" , "" , "");

END @@
DELIMITER ;
/*!50003 SET sql_mode              = @saved_sql_mode */ ;
/*!50003 SET character_set_client  = @saved_cs_client */ ;
/*!50003 SET character_set_results = @saved_cs_results */ ;
/*!50003 SET collation_connection  = @saved_col_connection */ ;
/*!50003 DROP PROCEDURE IF EXISTS `GET_DEPS` */;
/*!50003 SET @saved_cs_client      = @@character_set_client */ ;
/*!50003 SET @saved_cs_results     = @@character_set_results */ ;
/*!50003 SET @saved_col_connection = @@collation_connection */ ;
/*!50003 SET character_set_client  = utf8mb4 */ ;
/*!50003 SET character_set_results = utf8mb4 */ ;
/*!50003 SET collation_connection  = utf8mb4_0900_ai_ci */ ;
/*!50003 SET @saved_sql_mode       = @@sql_mode */ ;
/*!50003 SET sql_mode              = 'STRICT_TRANS_TABLES,NO_ENGINE_SUBSTITUTION' */ ;
DELIMITER @@
CREATE DEFINER=`root`@`localhost` PROCEDURE `GET_DEPS`(
 `wrkID` INT )
    READS SQL DATA
    SQL SECURITY INVOKER
    COMMENT 'get  departments '
begin
	select IS_ADMIN() into @allow;
	if (@allow = 1) then
		select distinct dep_id from dep_has_worker  where (archive=0 or archive is null);
	else
		select distinct dep_id from dep_has_worker  where worker_id=wrkID and (archive=0 or archive is null);
	end if;
END @@
DELIMITER ;
/*!50003 SET sql_mode              = @saved_sql_mode */ ;
/*!50003 SET character_set_client  = @saved_cs_client */ ;
/*!50003 SET character_set_results = @saved_cs_results */ ;
/*!50003 SET collation_connection  = @saved_col_connection */ ;
/*!50003 DROP PROCEDURE IF EXISTS `GET_DEPS_TABLE` */;
/*!50003 SET @saved_cs_client      = @@character_set_client */ ;
/*!50003 SET @saved_cs_results     = @@character_set_results */ ;
/*!50003 SET @saved_col_connection = @@collation_connection */ ;
/*!50003 SET character_set_client  = utf8mb4 */ ;
/*!50003 SET character_set_results = utf8mb4 */ ;
/*!50003 SET collation_connection  = utf8mb4_0900_ai_ci */ ;
/*!50003 SET @saved_sql_mode       = @@sql_mode */ ;
/*!50003 SET sql_mode              = 'STRICT_TRANS_TABLES,NO_ENGINE_SUBSTITUTION' */ ;
DELIMITER @@
CREATE DEFINER=`root`@`localhost` PROCEDURE `GET_DEPS_TABLE`(
 `wrkID` INT )
    READS SQL DATA
    SQL SECURITY INVOKER
    COMMENT 'get  departments - to get list before login '
BEGIN
	
	select distinct dep_id from dep_has_worker  where worker_id=wrkID and (archive=0 or archive is null);
END @@
DELIMITER ;
/*!50003 SET sql_mode              = @saved_sql_mode */ ;
/*!50003 SET character_set_client  = @saved_cs_client */ ;
/*!50003 SET character_set_results = @saved_cs_results */ ;
/*!50003 SET collation_connection  = @saved_col_connection */ ;
/*!50003 DROP PROCEDURE IF EXISTS `GET_PRIVILEGES` */;
/*!50003 SET @saved_cs_client      = @@character_set_client */ ;
/*!50003 SET @saved_cs_results     = @@character_set_results */ ;
/*!50003 SET @saved_col_connection = @@collation_connection */ ;
/*!50003 SET character_set_client  = utf8mb4 */ ;
/*!50003 SET character_set_results = utf8mb4 */ ;
/*!50003 SET collation_connection  = utf8mb4_0900_ai_ci */ ;
/*!50003 SET @saved_sql_mode       = @@sql_mode */ ;
/*!50003 SET sql_mode              = 'STRICT_TRANS_TABLES,NO_ENGINE_SUBSTITUTION' */ ;
DELIMITER @@
CREATE DEFINER=`root`@`localhost` PROCEDURE `GET_PRIVILEGES`()
BEGIN


  DECLARE cursor_n VARCHAR(100) DEFAULT '';
  DECLARE cursor_rol VARCHAR(100) DEFAULT '';
  DECLARE done INT DEFAULT FALSE;
  DECLARE drop_priv INT DEFAULT TRUE;
  DECLARE cursor_i CURSOR FOR
	select  w.`user`, role_sqlname from  kcson.dep_has_worker dhw join  kcson.`role` r on r.id = dhw.role_id join  kcson.worker w on dhw.worker_id = w.id
	where worker_id=get_WID() and dhw.dep_id = GET_DEP(get_WID()) and w.`user` <> "root";

# for mariaDB
DECLARE CONTINUE HANDLER FOR SQLSTATE 'HY000' SET @error_revoke = 1;
DECLARE CONTINUE HANDLER FOR SQLSTATE '42000' SET @error_revoke = 1;

DECLARE CONTINUE handler FOR NOT FOUND SET done = TRUE;

  OPEN cursor_i;
  read_loop: LOOP
    FETCH cursor_i INTO cursor_n, cursor_rol;

    IF drop_priv THEN
     	SET @queryStringRP = CONCAT('REVOKE ALL on *.* FROM  ', cursor_n, ';  ' );
		PREPARE stmt FROM @queryStringRP;
		EXECUTE stmt;
		DEALLOCATE PREPARE stmt;

     	SET @queryStringRP = CONCAT('grant execute, usage on kcson.* to  ', cursor_n, ';  ' );
		PREPARE stmt FROM @queryStringRP;
		EXECUTE stmt;
		DEALLOCATE PREPARE stmt;

	    # applies after user relogin
     	SET @queryStringRP = CONCAT('REVOKE manager, worker, specialist, trusted_specialist  FROM  ', cursor_n, ';  ' ); # admin, part_admin
		PREPARE stmt FROM @queryStringRP;
		EXECUTE stmt;
		DEALLOCATE PREPARE stmt;

        set drop_priv = false;
    END IF;

    IF done THEN
      LEAVE read_loop;
    END IF;

		SET @queryString = CONCAT('GRANT ',  cursor_rol , ' TO ', cursor_n, ';');
		# select @queryString;
		PREPARE stmt FROM @queryString;
		EXECUTE stmt;
		DEALLOCATE PREPARE stmt;

  END LOOP;
  # set role all;
  # select CURRENT_ROLE() ;
  CLOSE cursor_i;
END @@
DELIMITER ;
/*!50003 SET sql_mode              = @saved_sql_mode */ ;
/*!50003 SET character_set_client  = @saved_cs_client */ ;
/*!50003 SET character_set_results = @saved_cs_results */ ;
/*!50003 SET collation_connection  = @saved_col_connection */ ;
/*!50003 DROP PROCEDURE IF EXISTS `GET_VER` */;
/*!50003 SET @saved_cs_client      = @@character_set_client */ ;
/*!50003 SET @saved_cs_results     = @@character_set_results */ ;
/*!50003 SET @saved_col_connection = @@collation_connection */ ;
/*!50003 SET character_set_client  = utf8mb4 */ ;
/*!50003 SET character_set_results = utf8mb4 */ ;
/*!50003 SET collation_connection  = utf8mb4_0900_ai_ci */ ;
/*!50003 SET @saved_sql_mode       = @@sql_mode */ ;
/*!50003 SET sql_mode              = 'STRICT_TRANS_TABLES,NO_ENGINE_SUBSTITUTION' */ ;
DELIMITER @@
CREATE DEFINER=`root`@`localhost` PROCEDURE `GET_VER`()
    DETERMINISTIC
    COMMENT 'return sql version, change if tables changed'
begin

select 90;

end @@
DELIMITER ;
/*!50003 SET sql_mode              = @saved_sql_mode */ ;
/*!50003 SET character_set_client  = @saved_cs_client */ ;
/*!50003 SET character_set_results = @saved_cs_results */ ;
/*!50003 SET collation_connection  = @saved_col_connection */ ;
/*!50003 DROP PROCEDURE IF EXISTS `INIT_SECURITY` */;
/*!50003 SET @saved_cs_client      = @@character_set_client */ ;
/*!50003 SET @saved_cs_results     = @@character_set_results */ ;
/*!50003 SET @saved_col_connection = @@collation_connection */ ;
/*!50003 SET character_set_client  = utf8mb4 */ ;
/*!50003 SET character_set_results = utf8mb4 */ ;
/*!50003 SET collation_connection  = utf8mb4_0900_ai_ci */ ;
/*!50003 SET @saved_sql_mode       = @@sql_mode */ ;
/*!50003 SET sql_mode              = 'STRICT_TRANS_TABLES,NO_ENGINE_SUBSTITUTION' */ ;
DELIMITER @@
CREATE DEFINER=`root`@`localhost` PROCEDURE `INIT_SECURITY`()
BEGIN

    #############################
    # create roles
    # ---------------------------
    create role if not exists reporter,  none1, info, worker, specialist, trusted_specialist, manager, part_admin, admin, booker;
    #############################
    # grang temporary tables
    # ---------------------------
    create SCHEMA IF NOT EXISTS `kcson_tmp` DEFAULT CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci ;
    grant execute,select, create TEMPORARY TABLES on kcson.* to reporter;
    grant execute,select, create TEMPORARY TABLES on kcson_tmp.* to reporter;
    grant execute,select, create TEMPORARY TABLES on kcson_tmp.* to info;


    #############################
    # TODO reset all permissions
    # ---------------------------
    #REVOKE ALL PRIVILEGES FROM info;
    REVOKE ALL on *.* FROM info;
    grant execute on kcson.* to info;
    grant create TEMPORARY TABLES on kcson.* to info;


    #############################
    grant select on kcson._information_schema_columns to info;
    grant select on kcson._active_dep to info;

    grant select on kcson._bm_dep_has_client to info;
    grant select on kcson._bm_dep_has_client_other_year to info;
    grant select on kcson._bm_dep_has_client_year to info;
    grant select on kcson._categ_list_client to info;
    grant select on kcson._contr_has_main to info;
    grant select on kcson._contr_has_serv_predv to info;
    grant select on kcson._contracts to info;
    grant select on kcson._contracts_has_serv to info;
    grant select on kcson._dep_has_contracts to info;
    grant select on kcson._dep_has_main to info;
    grant select on kcson._dep_has_new_client to info;
    grant select on kcson._dep_has_ripso to info;
    grant select on kcson._dep_has_client to info;
    grant select on kcson._dep_has_client_blocked_in_year to info;
    grant select on kcson._dep_has_client_by_ripso to info;
    grant select on kcson._dep_has_client_contracts to info;
    grant select on kcson._dep_has_client_count_2month to info;
    grant select on kcson._dep_has_client_count_main_year to info;
    grant select on kcson._dep_has_client_count_month to info;
    grant select on kcson._dep_has_client_ended to info;
    grant select on kcson._dep_has_client_ending to info;
    grant select on kcson._dep_has_client_ripso to info;
    grant select on kcson._dep_has_client_ripso_or_contracts to info;
    grant select on kcson._dep_has_client_year to info;
    grant select on kcson._dep_has_worker to info;
    grant select on kcson._g_categ_list_client_for_dep_for_year to info;
    grant select on kcson._g_serv_list_for_dep_for_year to info;
    grant select on kcson._g_serv_total_you to info;
    grant select on kcson._main__months to info;
    grant select on kcson._main_cprice to info;
    grant select on kcson._main_cprice_for_contracts to info;
    grant select on kcson._main_for_dep to info;
    grant select on kcson._main_for_you to info;
    grant select on kcson._main_months to info;
    grant select on kcson._main_serv_name to info;
    grant select on kcson._main_serv_name_ripso to info;
    grant select on kcson._main_serv_name_ripso_static to info;
    grant select on kcson._main_serv_name_static to info;
    grant select on kcson._serv_activ to info;
    grant select on kcson._serv_total to info;
    grant select on kcson._client to info;
    grant select on kcson._client_has_category_for_last_client to info;
    grant select on kcson._client_has_contracts to info; # TODO: delete this
    grant select on kcson._client_has_invalid_contracts to info;
    grant select on kcson._client_has_main to info;
    grant select on kcson._client_has_valid_contracts to info;
    grant select on kcson._user_has_main to info;
    grant select on kcson._user_has_main_limit30 to info;
    grant select on kcson._user_has_main_today to info;
    grant select on kcson._worker_has_dep to info;
    grant select on kcson._worker_has_main to info;
    grant select on kcson._worker_settings to info;
--    grant select on kcson.audit to info;
    grant select on kcson.category to info;
    grant select on kcson.complex_dep to info;
    grant select on kcson.complex_dep_has_dep to info;
    grant select on kcson.contracts to info;
    grant select on kcson.contracts_has_serv to info;
    grant select on kcson.cr_by to info;
    grant select on kcson.cr_dep to info;
    grant select on kcson.cr_dep_id to info;
    grant select on kcson.data_log to info;
    grant select on kcson.dep to info;
    grant select on kcson.dep_has_main to info;
    grant select on kcson.dep_has_ripso to info;
    grant select on kcson.dep_has_serv to info;
    grant select on kcson.dep_has_client_by_contr to info;
    grant select on kcson.dep_has_client_by_ripso to info;
    grant select on kcson.dep_has_worker to info;
    grant select on kcson.dep_total_serv to info;
    grant select on kcson.dep_total_supserv1 to info;
    grant select on kcson.fioofdepbyserv to info;
    grant select on kcson.fioofdepbyset to info;
    grant select on kcson.holiday to info;
    grant select on kcson.invoice to info;
    grant select on kcson.invoice_has_payment to info;
    grant select on kcson.job to info;
    grant select on kcson.job_has_jobgroup to info;
    grant select on kcson.job_has_serv to info;
    grant select on kcson.jobgroup to info;
    grant select on kcson.last_used_workers to info;
    grant select on kcson.live_min to info;
--    grant select on kcson.log_edit_archive to info;
    grant select on kcson.main to info;
    grant select on kcson.main_cprice to info;
    grant select on kcson.main_has_ugroup to info;
    grant select on kcson.main_nz to info;
    grant select on kcson.max_pay_in_month to info;
    grant select on kcson.max_pay_in_month_50 to info;
    grant select on kcson.max_pay_in_month_75 to info;
    grant select on kcson.notifies to info;
    grant select on kcson.payment to info;
    grant select on kcson.pcat to info;
    grant select on kcson.ripso to info;
    grant select on kcson.ripso_has_serv to info;
    grant select on kcson.rname to info;
    grant select on kcson.role to info;
    grant select on kcson.serv to info;
    grant select on kcson.servform to info;
    grant select on kcson.servofripso to info;
    grant select on kcson.servofyear to info;
    grant select on kcson.setting to info;
    grant select on kcson.should_perc to info;
    grant select on kcson.street_home to info;
    grant select on kcson.stub_model to info;
    grant select on kcson.tables_checksums to info;
    grant select on kcson.test to info;
    grant select on kcson.total_cprice_in_month to info;
    grant select on kcson.client to info;
    grant select on kcson.client_has_category to info;
    grant select on kcson.ugroup to info;
    grant select on kcson.ugroup_has_client to info;
    grant select on kcson.ui_select_fiolist to info;
    grant select on kcson.upd_by to info;
    grant select on kcson.user_has_serv to info;
    grant select on kcson.worker to info;
    grant select on kcson.worker_has_dep to info;
    grant select on kcson.worker_settings to info;
    grant select on kcson._dep_has_workers to info;

    #############################
    # grant perm. to web_info
    # ---------------------------
   	GRANT Select ON kcson.`_apikey_has_contracts` TO 'web_info'@'%';
   	GRANT insert,update ON kcson.`api_key_insert_main` TO 'web_info'@'%';
   	GRANT select ON kcson.`api_key_insert_main` TO 'web_info'@'%'; -- maybe use procedure instead of this?
   	GRANT Select ON kcson.`_api_key_planned` TO 'web_info'@'%';
   	GRANT Select ON kcson.`_api_key_services` TO 'web_info'@'%';




    #############################
    # grant execute perm. to info role
    # ---------------------------


    #############################
    # grant perm. to worker role
    # ---------------------------
    grant info to worker;
    grant select,insert on kcson.updatable_main TO worker;
    grant select,insert on kcson.updatable__dep_has_main TO worker;
    grant update ON kcson.updatable__dep_has_main TO worker;




    #############################
    # grant perm. to specialist role
    # ---------------------------
    grant worker to specialist;
    grant reporter to specialist;
    grant select on kcson._dep_has_client_more to info;
    grant select on kcson._contr_has_add_info to specialist;
    grant select on kcson._dep_has_add_info to specialist;
    grant select on kcson._client_has_add_info to specialist;
    grant select on kcson.add_info to specialist;
    grant select on kcson.add_info_for_client to specialist;

    grant select on kcson.updatable__contr_has_add_info to specialist;
    grant select on kcson.updatable__dep_has_add_info to specialist;
    grant select on kcson.updatable_add_info to specialist;

    grant select,update,insert on kcson.updatable__contr_has_add_info TO specialist;
    grant select,update,insert on kcson.updatable__dep_has_add_info TO specialist;
    # grant update,insert ON kcson.updatable_add_info TO specialist;



    #############################
    # grant perm. to trusted_specialist role
    # ---------------------------
    grant specialist to trusted_specialist;
    grant select,update,insert on kcson.updatable_2__dep_has_client TO trusted_specialist;
    grant select,update,insert on kcson.updatable__contr_has_add_info TO trusted_specialist;
    grant select,update,insert on kcson.updatable__dep_has_add_info TO trusted_specialist;
    grant select,update,insert on kcson.updatable__dep_has_contracts TO trusted_specialist;
    grant select,update,insert on kcson.updatable__dep_has_main TO trusted_specialist;
    grant select,update,insert on kcson.updatable__dep_has_client TO trusted_specialist;
    grant select,update,insert on kcson.updatable__user_has_main TO trusted_specialist;
    grant select,update,insert on kcson.updatable_add_info TO trusted_specialist;
    grant select,update,insert on kcson.updatable_contracts TO trusted_specialist;
    grant select,update,insert on kcson.updatable_contracts_has_serv TO trusted_specialist;
    grant select,update,insert on kcson.updatable_main TO trusted_specialist;
    grant select,update,insert on kcson.updatable_client TO trusted_specialist;



    grant select,update,insert on kcson.invoice TO trusted_specialist;
    grant select,update,insert on kcson.invoice_has_payment TO trusted_specialist;



    grant select,update,insert on kcson._contracts_has_serv TO trusted_specialist;
    grant select,update,insert on kcson.client_has_category TO trusted_specialist;
    #############################
    # grant perm. to manager role
    # ---------------------------
    grant trusted_specialist to manager;
    grant select,insert on kcson.category TO manager;
    grant select,insert,delete on kcson._dhw_has_client TO manager;
   

    #############################
    # grant perm. to booker role
    # ---------------------------
    grant info to booker;
    grant select,update,insert on kcson.payment TO booker;

    #############################
    # grant perm. to part_admin role
    # ---------------------------
    grant manager to part_admin;
    grant booker to part_admin;
    grant select,update,insert on kcson.holiday TO part_admin;
    grant select,update,insert on kcson.live_min TO part_admin;
    grant select,update,insert on kcson.notifies TO part_admin;
    grant select,update,insert on kcson.category TO part_admin;


    grant select,update,insert on kcson.job TO part_admin;
    grant select,update,insert on kcson.job_has_jobgroup TO part_admin;
    grant select,update,insert on kcson.job_has_serv TO part_admin;
    grant select,update,insert on kcson.jobgroup TO part_admin;



    grant select,update,insert on kcson.serv TO part_admin;
    grant select,update,insert on kcson.ripso TO part_admin;
    grant select,update,insert on kcson.ripso_has_serv TO part_admin;
    grant select,update,insert on kcson.dep TO part_admin;
    grant select,update,insert on kcson.dep_has_worker TO part_admin;
    grant select,update,insert on kcson.dep_has_ripso TO part_admin;
    grant select,update,insert on kcson.worker TO part_admin;
    grant select,update,insert on kcson.ripso TO part_admin;
    grant select,update,insert on kcson.ripso_has_serv TO part_admin;
    grant select,update,insert on kcson.servform TO part_admin;

    grant select,update,insert  on kcson.category to part_admin;
    grant select,update,insert  on kcson.complex_dep to part_admin;
    grant select,update,insert,delete on kcson.complex_dep_has_dep to part_admin;
    grant select,update,insert,delete on kcson.holiday to part_admin;
    grant select,update,insert,delete on kcson.ui_select_fiolist to part_admin;

    grant select,insert on kcson.user_change to part_admin;

    #############################
    # grant perm. to admin role
    # ---------------------------
    grant part_admin to admin;

END @@
DELIMITER ;
/*!50003 SET sql_mode              = @saved_sql_mode */ ;
/*!50003 SET character_set_client  = @saved_cs_client */ ;
/*!50003 SET character_set_results = @saved_cs_results */ ;
/*!50003 SET collation_connection  = @saved_col_connection */ ;
/*!50003 DROP PROCEDURE IF EXISTS `KILL_USER_SESSION` */;
/*!50003 SET @saved_cs_client      = @@character_set_client */ ;
/*!50003 SET @saved_cs_results     = @@character_set_results */ ;
/*!50003 SET @saved_col_connection = @@collation_connection */ ;
/*!50003 SET character_set_client  = utf8mb4 */ ;
/*!50003 SET character_set_results = utf8mb4 */ ;
/*!50003 SET collation_connection  = utf8mb4_0900_ai_ci */ ;
/*!50003 SET @saved_sql_mode       = @@sql_mode */ ;
/*!50003 SET sql_mode              = 'STRICT_TRANS_TABLES,NO_ENGINE_SUBSTITUTION' */ ;
DELIMITER @@
CREATE DEFINER=`root`@`localhost` PROCEDURE `KILL_USER_SESSION`()
BEGIN
  
  DECLARE uid int default 0;
  DECLARE name VARCHAR(64) DEFAULT ''; 
  DECLARE done INT DEFAULT FALSE;
  DECLARE kill_i CURSOR for
  	SELECT t.id, t.user FROM information_schema.processlist t where t.user = SUBSTRING_INDEX(user(),'@',1);

  DECLARE CONTINUE HANDLER FOR NOT FOUND SET done = TRUE;
   
	select IS_ADMIN() into @allow;
	if (@allow = 0) then
			SIGNAL SQLSTATE '45000' SET MESSAGE_TEXT =  'Ошибка: у вас нет доступа!';
	end if;
 
  OPEN kill_i;
  kill_loop: LOOP
    FETCH kill_i INTO uid, name;
    IF done THEN
      LEAVE kill_loop;
    END IF;
     	kill uid;
  END LOOP;
  CLOSE kill_i;
  
  
END @@
DELIMITER ;
/*!50003 SET sql_mode              = @saved_sql_mode */ ;
/*!50003 SET character_set_client  = @saved_cs_client */ ;
/*!50003 SET character_set_results = @saved_cs_results */ ;
/*!50003 SET collation_connection  = @saved_col_connection */ ;
/*!50003 DROP PROCEDURE IF EXISTS `Pivot` */;
/*!50003 SET @saved_cs_client      = @@character_set_client */ ;
/*!50003 SET @saved_cs_results     = @@character_set_results */ ;
/*!50003 SET @saved_col_connection = @@collation_connection */ ;
/*!50003 SET character_set_client  = utf8mb4 */ ;
/*!50003 SET character_set_results = utf8mb4 */ ;
/*!50003 SET collation_connection  = utf8mb4_0900_ai_ci */ ;
/*!50003 SET @saved_sql_mode       = @@sql_mode */ ;
/*!50003 SET sql_mode              = 'ONLY_FULL_GROUP_BY,STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_ENGINE_SUBSTITUTION' */ ;
DELIMITER @@
CREATE DEFINER=`root`@`localhost` PROCEDURE `Pivot`(
    IN tbl_name VARCHAR(99),       -- table name (or db.tbl)
    IN base_cols VARCHAR(99),      -- column(s) on the left, separated by commas
    IN pivot_col VARCHAR(64),      -- name of column to put across the top
    IN tally_col VARCHAR(64),      -- name of column to SUM up
    IN where_clause VARCHAR(99),   -- empty string or "WHERE ..."
    IN order_by VARCHAR(99)        -- empty string or "ORDER BY ..."; usually the base_cols
    )
    DETERMINISTIC
    SQL SECURITY INVOKER
BEGIN
    -- GET the SUM()s
    SET @subq = CONCAT('SELECT DISTINCT ', pivot_col, ' AS val ',
                    ' FROM ', tbl_name, ' ', where_clause, ' ORDER BY 1');

    SET @cc1 = "CONCAT('SUM(IF(&p = ', &v, ', &t, 0)) AS ', &v)";
    SET @cc2 = REPLACE(@cc1, '&p', pivot_col);
    SET @cc3 = REPLACE(@cc2, '&t', tally_col);
    -- select @cc2, @cc3;
    SET @qval = CONCAT("'\"', val, '\"'");
    -- select @qval;
    SET @cc4 = REPLACE(@cc3, '&v', @qval);
    -- select @cc4;

    SET SESSION group_concat_max_len = 10000;   -- just in case
    SET @stmt = CONCAT(
            'SELECT  GROUP_CONCAT(', @cc4, ' SEPARATOR ",\n")  INTO @sums',
            ' FROM ( ', @subq, ' ) AS top');
     select @stmt;
    PREPARE _sql FROM @stmt;
    EXECUTE _sql;                      -- 2nd step: build SQL for columns
    DEALLOCATE PREPARE _sql;
    -- 3rd: Construct the query and perform it
    SET @stmt2 = CONCAT(
            'SELECT ',
                base_cols, ',\n',
                @sums,
                ',\n SUM(', tally_col, ') AS Total'
            '\n FROM ', tbl_name, ' ',
            where_clause,
            ' GROUP BY ', base_cols,
            '\n WITH ROLLUP',
            '\n', order_by
        );
    select @stmt2;                    -- The statement that generates the result
    PREPARE _sql FROM @stmt2;
    EXECUTE _sql;                     -- The resulting pivot table ouput
    DEALLOCATE PREPARE _sql;
    -- For debugging / tweaking, SELECT the various @variables after CALLing.
END @@
DELIMITER ;
/*!50003 SET sql_mode              = @saved_sql_mode */ ;
/*!50003 SET character_set_client  = @saved_cs_client */ ;
/*!50003 SET character_set_results = @saved_cs_results */ ;
/*!50003 SET collation_connection  = @saved_col_connection */ ;
/*!50003 DROP PROCEDURE IF EXISTS `replace_user` */;
/*!50003 SET @saved_cs_client      = @@character_set_client */ ;
/*!50003 SET @saved_cs_results     = @@character_set_results */ ;
/*!50003 SET @saved_col_connection = @@collation_connection */ ;
/*!50003 SET character_set_client  = utf8mb4 */ ;
/*!50003 SET character_set_results = utf8mb4 */ ;
/*!50003 SET collation_connection  = utf8mb4_0900_ai_ci */ ;
/*!50003 SET @saved_sql_mode       = @@sql_mode */ ;
/*!50003 SET sql_mode              = 'STRICT_TRANS_TABLES,NO_ENGINE_SUBSTITUTION' */ ;
DELIMITER @@
CREATE DEFINER=`root`@`localhost` PROCEDURE `replace_user`(IN `p_Name` VARCHAR(16), IN `p_Passw` VARCHAR(32), IN wID int)
this_proc:BEGIN
    DECLARE `_HOST` CHAR(64);
    DECLARE cuser CHAR(16);
    DECLARE crole int;
    DECLARE wrole int;
    DECLARE old_login CHAR(16);

	DECLARE CONTINUE HANDLER FOR NOT FOUND SET @done = 1;
    	-- select 'start ';

    set `_HOST` = '@\'%\'';
   -- get role of current user
   	SET cuser := SUBSTRING_INDEX(user(),'@',1);
    set crole := (select dhw.role_id  from dep_has_worker dhw inner join  worker w  on
		w.id = dhw.worker_id
		where w.`user` = cuser and (dhw.role_id  in  (6, 7, 8) )
		order by dhw.role_id desc
		limit 1);
	-- select crole;

   -- get role of user whom we trying to change here
    set wrole := (select dhw.role_id  from dep_has_worker dhw
		where dhw.id = wID
		order by dhw.role_id desc
		limit 1);
	-- select wrole;

    -- check privileges
    if (  crole is null ) then
    	select 'rejected: current user role is null';
    	LEAVE this_proc;
    elseif ( crole = 7 or crole = 8 ) then -- admin and part admin
    	set crole = crole;  -- ok
    elseif wrole is null then
    	select 'rejected: worker user role is null';
    	LEAVE this_proc; -- maybe assign minimal role here?
    elseif (( crole = 6 ) and crole > wrole ) then -- manager change login of worker
    	set crole = crole;  -- ok
    else
    	select 'rejected: unknown';
    	LEAVE this_proc;
    end if;

   	-- remove old login
   set old_login := (select w.`user` from dep_has_worker dhw inner join  worker w  on
		w.id = dhw.worker_id
		where dhw.id = wId
		limit 1);
   if ( old_login is not null ) then
		SET @`sql` := CONCAT('DROP USER IF EXISTS ', old_login, `_HOST`);
		PREPARE `stmt` FROM @`sql`;
		EXECUTE `stmt`;
   end if;

  -- create new login
    SET `p_Name` := CONCAT('\'', REPLACE(TRIM(`p_Name`), CHAR(39), CONCAT(CHAR(92), CHAR(39))), '\'');
    set `p_Passw` := CONCAT('\'', REPLACE(`p_Passw`, CHAR(39), CONCAT(CHAR(92), CHAR(39))), '\'');

    SET @`sql` := CONCAT('DROP USER IF EXISTS ', `p_Name`, `_HOST`);
    PREPARE `stmt` FROM @`sql`;
    EXECUTE `stmt`;
    SET @`sql` := CONCAT('CREATE USER ', `p_Name`, `_HOST`, ' IDENTIFIED  with mysql_native_password BY ', `p_Passw`);
    PREPARE `stmt` FROM @`sql`;
    EXECUTE `stmt`;
    SET @`sql` := CONCAT('GRANT execute ON kcson.* TO ', `p_Name`, `_HOST` );
    PREPARE `stmt` FROM @`sql`;
    EXECUTE `stmt`;
    DEALLOCATE PREPARE `stmt`;

   insert into user_change(old_login, new_login)
   	values(old_login, p_Name);

    FLUSH PRIVILEGES;
    select "finished" ;
END @@
DELIMITER ;
/*!50003 SET sql_mode              = @saved_sql_mode */ ;
/*!50003 SET character_set_client  = @saved_cs_client */ ;
/*!50003 SET character_set_results = @saved_cs_results */ ;
/*!50003 SET collation_connection  = @saved_col_connection */ ;
/*!50003 DROP PROCEDURE IF EXISTS `RESET_PRIVILEGES` */;
/*!50003 SET @saved_cs_client      = @@character_set_client */ ;
/*!50003 SET @saved_cs_results     = @@character_set_results */ ;
/*!50003 SET @saved_col_connection = @@collation_connection */ ;
/*!50003 SET character_set_client  = utf8mb4 */ ;
/*!50003 SET character_set_results = utf8mb4 */ ;
/*!50003 SET collation_connection  = utf8mb4_0900_ai_ci */ ;
/*!50003 SET @saved_sql_mode       = @@sql_mode */ ;
/*!50003 SET sql_mode              = 'STRICT_TRANS_TABLES,NO_ENGINE_SUBSTITUTION' */ ;
DELIMITER @@
CREATE DEFINER=`root`@`localhost` PROCEDURE `RESET_PRIVILEGES`()
    SQL SECURITY INVOKER
BEGIN
  DECLARE cursor_n VARCHAR(100) DEFAULT '';
  DECLARE cursor_rol VARCHAR(100) DEFAULT '';
  DECLARE done INT DEFAULT FALSE;
  DECLARE cursor_i CURSOR FOR  
	select distinct w.`user`, 'info' from  kcson.dep_has_worker dhw join  kcson.`role` r on r.id = dhw.role_id join  kcson.worker w on dhw.worker_id = w.id
	where  w.`user` <> "" and w.`user` <> "root" ;
  DECLARE CONTINUE handler FOR NOT FOUND SET done = TRUE;
 
    
	select IS_ADMIN() into @allow;
	if (@allow = 0) then
			SIGNAL SQLSTATE '45000' SET MESSAGE_TEXT =  'Ошибка: у вас нет доступа!';
	end if;
 
 
  OPEN cursor_i;
  read_loop: LOOP
    FETCH cursor_i INTO cursor_n, cursor_rol;
   
    IF done THEN
      LEAVE read_loop;
    END IF;
	
     	SET @queryStringRP = CONCAT('REVOKE ALL on *.* FROM  ', cursor_n, ';  ' );
		PREPARE stmt FROM @queryStringRP;
		EXECUTE stmt;
		DEALLOCATE PREPARE stmt; 
     	SET @queryStringRP = CONCAT('grant execute, usage on kcson.* to  ', cursor_n, ';  ' );
		PREPARE stmt FROM @queryStringRP;
		EXECUTE stmt;
		DEALLOCATE PREPARE stmt; 
  END LOOP;
  CLOSE cursor_i;
END @@
DELIMITER ;
/*!50003 SET sql_mode              = @saved_sql_mode */ ;
/*!50003 SET character_set_client  = @saved_cs_client */ ;
/*!50003 SET character_set_results = @saved_cs_results */ ;
/*!50003 SET collation_connection  = @saved_col_connection */ ;
/*!50003 DROP PROCEDURE IF EXISTS `serv_dep_total` */;
/*!50003 SET @saved_cs_client      = @@character_set_client */ ;
/*!50003 SET @saved_cs_results     = @@character_set_results */ ;
/*!50003 SET @saved_col_connection = @@collation_connection */ ;
/*!50003 SET character_set_client  = utf8mb4 */ ;
/*!50003 SET character_set_results = utf8mb4 */ ;
/*!50003 SET collation_connection  = utf8mb4_0900_ai_ci */ ;
/*!50003 SET @saved_sql_mode       = @@sql_mode */ ;
/*!50003 SET sql_mode              = 'ONLY_FULL_GROUP_BY,STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_ENGINE_SUBSTITUTION' */ ;
DELIMITER @@
CREATE DEFINER=`root`@`localhost` PROCEDURE `serv_dep_total`()
    DETERMINISTIC
BEGIN
	call CREATE_PIVOT("
	(select serv_tnum, s.id, client_id, serv_id , quantity
	from main_NZ m inner join serv s on m.serv_id=s.id
	where dep_id = GET_DEP(GET_wID())
	)  main1",

	 "client_id", "serv_tnum", "quantity" , "" , "");
     
END @@
DELIMITER ;
/*!50003 SET sql_mode              = @saved_sql_mode */ ;
/*!50003 SET character_set_client  = @saved_cs_client */ ;
/*!50003 SET character_set_results = @saved_cs_results */ ;
/*!50003 SET collation_connection  = @saved_col_connection */ ;
/*!50003 DROP PROCEDURE IF EXISTS `SET_DEP_` */;
/*!50003 SET @saved_cs_client      = @@character_set_client */ ;
/*!50003 SET @saved_cs_results     = @@character_set_results */ ;
/*!50003 SET @saved_col_connection = @@collation_connection */ ;
/*!50003 SET character_set_client  = utf8mb4 */ ;
/*!50003 SET character_set_results = utf8mb4 */ ;
/*!50003 SET collation_connection  = utf8mb4_0900_ai_ci */ ;
/*!50003 SET @saved_sql_mode       = @@sql_mode */ ;
/*!50003 SET sql_mode              = 'STRICT_TRANS_TABLES,NO_ENGINE_SUBSTITUTION' */ ;
DELIMITER @@
CREATE DEFINER=`root`@`localhost` PROCEDURE `SET_DEP_`(`depId` INT)
    MODIFIES SQL DATA
    COMMENT 'set default department (with checking is it possible)'
begin
	declare wrkID int ;
	declare res int default 0;

	  declare uid int default 0;
	  DECLARE name VARCHAR(64) DEFAULT '';
	  declare done int default false;
  
 	  DECLARE kill_i CURSOR for
	  select t.id, t.user from information_schema.processlist t where t.user = substring_index(user(),'@',1);



	set  wrkID=get_WID();
	select IS_ADMIN() into @allow;
	if (@allow = 1) then
		set res = (select distinct dep_id from dep_has_worker  where (archive=0 or archive is null));
	else
		set res = (select distinct dep_id from dep_has_worker  where worker_id=wrkID and (archive=0 or archive is null));
	end if;

	if res > 0 then 
	    SET @queryStringRP = CONCAT('REVOKE ALL on *.* FROM  "', SUBSTRING_INDEX(user(),'@',1), '";  ' );
-- 	   select  @queryStringRP;
		PREPARE stmt FROM @queryStringRP;
		EXECUTE stmt;
		DEALLOCATE PREPARE stmt; 
	
		SET @queryStringRP = CONCAT('REVOKE reporter, info, worker, specialist, trusted_specialist, manager, part_admin, admin, booker FROM  "', SUBSTRING_INDEX(user(),'@',1), '";  ' );
-- 	   select  @queryStringRP;
		PREPARE stmt FROM @queryStringRP;
		EXECUTE stmt;
		DEALLOCATE PREPARE stmt; 
	
		update worker_settings set last_dep=depId where id = wrkID;
		# call GET_PRIVILEGES();
		# TODO: set role for invoker
		# set role info;

     	SET @queryStringRP = CONCAT('grant execute, usage  on kcson.* to  "', SUBSTRING_INDEX(user(),'@',1), '";  ' );
		PREPARE stmt FROM @queryStringRP;
		EXECUTE stmt;
		DEALLOCATE PREPARE stmt; 
	
		# update worker_has_dep set active=0 where(worker_id=wrkID);
		# update worker_has_dep set active=1 where(worker_id=wrkID and dep_id=depId);
		select last_dep from worker_settings where id = wrkID;
	
		SET done = False;
		  open kill_i;
		  kill_loop: LOOP
		    FETCH kill_i INTO uid, name;
		    IF done THEN
		      LEAVE kill_loop;
		    END IF;
		     	kill uid;
		     	select "kill",uid;
		  END LOOP;
		  CLOSE kill_i;
	else
		select 0;
	end if;
END @@
DELIMITER ;
/*!50003 SET sql_mode              = @saved_sql_mode */ ;
/*!50003 SET character_set_client  = @saved_cs_client */ ;
/*!50003 SET character_set_results = @saved_cs_results */ ;
/*!50003 SET collation_connection  = @saved_col_connection */ ;
/*!50003 DROP PROCEDURE IF EXISTS `SHOW_COL` */;
/*!50003 SET @saved_cs_client      = @@character_set_client */ ;
/*!50003 SET @saved_cs_results     = @@character_set_results */ ;
/*!50003 SET @saved_col_connection = @@collation_connection */ ;
/*!50003 SET character_set_client  = utf8mb4 */ ;
/*!50003 SET character_set_results = utf8mb4 */ ;
/*!50003 SET collation_connection  = utf8mb4_0900_ai_ci */ ;
/*!50003 SET @saved_sql_mode       = @@sql_mode */ ;
/*!50003 SET sql_mode              = 'STRICT_TRANS_TABLES,NO_ENGINE_SUBSTITUTION' */ ;
DELIMITER @@
CREATE DEFINER=`root`@`localhost` PROCEDURE `SHOW_COL`(IN sqlToShow TEXT)
    READS SQL DATA
    DETERMINISTIC
BEGIN
    DROP TEMPORARY TABLE IF EXISTS tempTable;
    SET @sqlLimit0 = CONCAT('CREATE TEMPORARY TABLE tempTable AS (SELECT * FROM (',
                            sqlToShow, ') subq LIMIT 0)');
    #select  @sqlLimit0;
    PREPARE stmt FROM @sqlLimit0;
    EXECUTE stmt;
    SHOW COLUMNS FROM tempTable; 
    DEALLOCATE PREPARE stmt;
END @@
DELIMITER ;
/*!50003 SET sql_mode              = @saved_sql_mode */ ;
/*!50003 SET character_set_client  = @saved_cs_client */ ;
/*!50003 SET character_set_results = @saved_cs_results */ ;
/*!50003 SET collation_connection  = @saved_col_connection */ ;
/*!50003 DROP PROCEDURE IF EXISTS `SHOW_COL1` */;
/*!50003 SET @saved_cs_client      = @@character_set_client */ ;
/*!50003 SET @saved_cs_results     = @@character_set_results */ ;
/*!50003 SET @saved_col_connection = @@collation_connection */ ;
/*!50003 SET character_set_client  = utf8mb4 */ ;
/*!50003 SET character_set_results = utf8mb4 */ ;
/*!50003 SET collation_connection  = utf8mb4_0900_ai_ci */ ;
/*!50003 SET @saved_sql_mode       = @@sql_mode */ ;
/*!50003 SET sql_mode              = 'STRICT_TRANS_TABLES,NO_ENGINE_SUBSTITUTION' */ ;
DELIMITER @@
CREATE DEFINER=`root`@`localhost` PROCEDURE `SHOW_COL1`(IN sqlToShow TEXT)
    READS SQL DATA
    DETERMINISTIC
BEGIN
    DROP TEMPORARY TABLE IF EXISTS tempTable;
    SET @sqlLimit0 = CONCAT('CREATE TEMPORARY TABLE tempTable AS (SELECT * FROM (',
                            sqlToShow, ') subq LIMIT 1)');
    #select  @sqlLimit0;
    PREPARE stmt FROM @sqlLimit0;
    EXECUTE stmt;
    SHOW COLUMNS FROM tempTable;   
    DEALLOCATE PREPARE stmt;
END @@
DELIMITER ;
/*!50003 SET sql_mode              = @saved_sql_mode */ ;
/*!50003 SET character_set_client  = @saved_cs_client */ ;
/*!50003 SET character_set_results = @saved_cs_results */ ;
/*!50003 SET collation_connection  = @saved_col_connection */ ;
/*!50003 DROP PROCEDURE IF EXISTS `show_cols_root` */;
/*!50003 SET @saved_cs_client      = @@character_set_client */ ;
/*!50003 SET @saved_cs_results     = @@character_set_results */ ;
/*!50003 SET @saved_col_connection = @@collation_connection */ ;
/*!50003 SET character_set_client  = utf8mb4 */ ;
/*!50003 SET character_set_results = utf8mb4 */ ;
/*!50003 SET collation_connection  = utf8mb4_0900_ai_ci */ ;
/*!50003 SET @saved_sql_mode       = @@sql_mode */ ;
/*!50003 SET sql_mode              = 'STRICT_TRANS_TABLES,NO_ENGINE_SUBSTITUTION' */ ;
DELIMITER @@
CREATE DEFINER=`root`@`localhost` PROCEDURE `show_cols_root`(IN tname TEXT)
    READS SQL DATA
    DETERMINISTIC
begin
    set @show_cols_root = CONCAT('show columns from ', tname);
    PREPARE stmt FROM @show_cols_root;
    execute stmt;
    DEALLOCATE PREPARE stmt;
end @@
DELIMITER ;
/*!50003 SET sql_mode              = @saved_sql_mode */ ;
/*!50003 SET character_set_client  = @saved_cs_client */ ;
/*!50003 SET character_set_results = @saved_cs_results */ ;
/*!50003 SET collation_connection  = @saved_col_connection */ ;
/*!50003 DROP PROCEDURE IF EXISTS `UPDATE_ALL_IPPSU` */;
/*!50003 SET @saved_cs_client      = @@character_set_client */ ;
/*!50003 SET @saved_cs_results     = @@character_set_results */ ;
/*!50003 SET @saved_col_connection = @@collation_connection */ ;
/*!50003 SET character_set_client  = utf8mb4 */ ;
/*!50003 SET character_set_results = utf8mb4 */ ;
/*!50003 SET collation_connection  = utf8mb4_0900_ai_ci */ ;
/*!50003 SET @saved_sql_mode       = @@sql_mode */ ;
/*!50003 SET sql_mode              = 'STRICT_TRANS_TABLES,NO_ENGINE_SUBSTITUTION' */ ;
DELIMITER @@
CREATE DEFINER=`root`@`localhost` PROCEDURE `UPDATE_ALL_IPPSU`()
BEGIN



	select IS_ADMIN() into @allow;

	if (@allow = 0) then

			SIGNAL SQLSTATE '45000' SET MESSAGE_TEXT =  'Ошибка: у вас нет доступа!';

	end if;



	update `contracts_has_serv`  chs

		INNER JOIN serv s ON s.id = chs.serv_id

		INNER JOIN contracts c ON c.id = `chs`.`contracts_id`

		SET serv_id = replacedby

	where replacedby > 0 and  `c`.`blocked` = false  ;

END @@
DELIMITER ;
/*!50003 SET sql_mode              = @saved_sql_mode */ ;
/*!50003 SET character_set_client  = @saved_cs_client */ ;
/*!50003 SET character_set_results = @saved_cs_results */ ;
/*!50003 SET collation_connection  = @saved_col_connection */ ;
/*!50003 DROP PROCEDURE IF EXISTS `UPDATE_RIPSO` */;
/*!50003 SET @saved_cs_client      = @@character_set_client */ ;
/*!50003 SET @saved_cs_results     = @@character_set_results */ ;
/*!50003 SET @saved_col_connection = @@collation_connection */ ;
/*!50003 SET character_set_client  = utf8mb4 */ ;
/*!50003 SET character_set_results = utf8mb4 */ ;
/*!50003 SET collation_connection  = utf8mb4_0900_ai_ci */ ;
/*!50003 SET @saved_sql_mode       = @@sql_mode */ ;
/*!50003 SET sql_mode              = 'STRICT_TRANS_TABLES,NO_ENGINE_SUBSTITUTION' */ ;
DELIMITER @@
CREATE DEFINER=`root`@`localhost` PROCEDURE `UPDATE_RIPSO`()
BEGIN

    

	select IS_ADMIN() into @allow;

	if (@allow = 0) then

			SIGNAL SQLSTATE '45000' SET MESSAGE_TEXT =  'Ошибка: у вас нет доступа!';

	end if;

 

	update ripso_has_serv  

		INNER JOIN serv ON id = serv_id

		SET serv_id = replacedby

	where replacedby > 0;

END @@
DELIMITER ;
/*!50003 SET sql_mode              = @saved_sql_mode */ ;
/*!50003 SET character_set_client  = @saved_cs_client */ ;
/*!50003 SET character_set_results = @saved_cs_results */ ;
/*!50003 SET collation_connection  = @saved_col_connection */ ;

--
-- Final view structure for view `_active_dep`
--

/*!50001 DROP VIEW IF EXISTS `_active_dep`*/;
/*!50001 SET @saved_cs_client          = @@character_set_client */;
/*!50001 SET @saved_cs_results         = @@character_set_results */;
/*!50001 SET @saved_col_connection     = @@collation_connection */;
/*!50001 SET character_set_client      = utf8mb4 */;
/*!50001 SET character_set_results     = utf8mb4 */;
/*!50001 SET collation_connection      = utf8mb4_0900_ai_ci */;
/*!50001 CREATE ALGORITHM=UNDEFINED */
/*!50013 DEFINER=`root`@`localhost` SQL SECURITY DEFINER */
/*!50001 VIEW `_active_dep` AS select `dep`.`id` AS `id`,`dep`.`dep` AS `dep`,`dep`.`dep_full_name` AS `dep_full_name`,`dep`.`dep_puname` AS `dep_puname`,`dep`.`note` AS `note`,`dep`.`archive` AS `archive`,`dep`.`complex_dep_id` AS `complex_dep_id` from `dep` where ((0 <> `IS_CUR_DEP_STATIC`(`dep`.`id`)) and (`dep`.`complex_dep_id` = 0)) group by `dep`.`dep` */;
/*!50001 SET character_set_client      = @saved_cs_client */;
/*!50001 SET character_set_results     = @saved_cs_results */;
/*!50001 SET collation_connection      = @saved_col_connection */;

--
-- Final view structure for view `_active_dep_static`
--

/*!50001 DROP VIEW IF EXISTS `_active_dep_static`*/;
/*!50001 SET @saved_cs_client          = @@character_set_client */;
/*!50001 SET @saved_cs_results         = @@character_set_results */;
/*!50001 SET @saved_col_connection     = @@collation_connection */;
/*!50001 SET character_set_client      = utf8mb4 */;
/*!50001 SET character_set_results     = utf8mb4 */;
/*!50001 SET collation_connection      = utf8mb4_0900_ai_ci */;
/*!50001 CREATE ALGORITHM=UNDEFINED */
/*!50013 DEFINER=`root`@`localhost` SQL SECURITY DEFINER */
/*!50001 VIEW `_active_dep_static` AS select `dep`.`id` AS `id`,`dep`.`dep` AS `dep`,`dep`.`dep_full_name` AS `dep_full_name`,`dep`.`dep_puname` AS `dep_puname`,`dep`.`note` AS `note`,`dep`.`archive` AS `archive`,`dep`.`complex_dep_id` AS `complex_dep_id` from `dep` where ((0 <> `IS_CUR_DEP_STATIC`(`dep`.`id`)) and (`dep`.`complex_dep_id` = 0)) group by `dep`.`dep` */;
/*!50001 SET character_set_client      = @saved_cs_client */;
/*!50001 SET character_set_results     = @saved_cs_results */;
/*!50001 SET collation_connection      = @saved_col_connection */;

--
-- Final view structure for view `_api_key_planned`
--

/*!50001 DROP VIEW IF EXISTS `_api_key_planned`*/;
/*!50001 SET @saved_cs_client          = @@character_set_client */;
/*!50001 SET @saved_cs_results         = @@character_set_results */;
/*!50001 SET @saved_col_connection     = @@collation_connection */;
/*!50001 SET character_set_client      = utf8mb4 */;
/*!50001 SET character_set_results     = utf8mb4 */;
/*!50001 SET collation_connection      = utf8mb4_0900_ai_ci */;
/*!50001 CREATE ALGORITHM=UNDEFINED */
/*!50013 DEFINER=`root`@`localhost` SQL SECURITY DEFINER */
/*!50001 VIEW `_api_key_planned` AS select `ahc`.`contract_id` AS `contract_id`,`chs`.`serv_id` AS `serv_id`,`chs`.`planned` AS `planned`,`chs`.`filled` AS `filled`,`ahc`.`api_key` AS `api_key` from (`contracts_has_serv` `chs` join `_apikey_has_contracts` `ahc` on((`ahc`.`contract_id` = `chs`.`contracts_id`))) */;
/*!50001 SET character_set_client      = @saved_cs_client */;
/*!50001 SET character_set_results     = @saved_cs_results */;
/*!50001 SET collation_connection      = @saved_col_connection */;

--
-- Final view structure for view `_api_key_services`
--

/*!50001 DROP VIEW IF EXISTS `_api_key_services`*/;
/*!50001 SET @saved_cs_client          = @@character_set_client */;
/*!50001 SET @saved_cs_results         = @@character_set_results */;
/*!50001 SET @saved_col_connection     = @@collation_connection */;
/*!50001 SET character_set_client      = utf8mb4 */;
/*!50001 SET character_set_results     = utf8mb4 */;
/*!50001 SET collation_connection      = utf8mb4_0900_ai_ci */;
/*!50001 CREATE ALGORITHM=UNDEFINED */
/*!50013 DEFINER=`root`@`localhost` SQL SECURITY DEFINER */
/*!50001 VIEW `_api_key_services` AS select `sa`.`id` AS `id`,`sa`.`serv` AS `serv`,`sa`.`serv_text` AS `serv_text`,`sa`.`tnum` AS `tnum`,`sa`.`price` AS `price`,`sa`.`total` AS `total`,`sa`.`sub_serv` AS `sub_serv`,`sa`.`serv_id_list` AS `serv_id_list`,`si`.`image` AS `image`,`si`.`expr` AS `expr`,`si`.`words` AS `short_text` from (`_serv_activ` `sa` left join `serv_images` `si` on((`sa`.`serv_text` like `si`.`expr`))) */;
/*!50001 SET character_set_client      = @saved_cs_client */;
/*!50001 SET character_set_results     = @saved_cs_results */;
/*!50001 SET collation_connection      = @saved_col_connection */;

--
-- Final view structure for view `_apikey_has_contracts`
--

/*!50001 DROP VIEW IF EXISTS `_apikey_has_contracts`*/;
/*!50001 SET @saved_cs_client          = @@character_set_client */;
/*!50001 SET @saved_cs_results         = @@character_set_results */;
/*!50001 SET @saved_col_connection     = @@collation_connection */;
/*!50001 SET character_set_client      = utf8mb4 */;
/*!50001 SET character_set_results     = utf8mb4 */;
/*!50001 SET collation_connection      = utf8mb4_0900_ai_ci */;
/*!50001 CREATE ALGORITHM=UNDEFINED */
/*!50013 DEFINER=`root`@`localhost` SQL SECURITY DEFINER */
/*!50001 VIEW `_apikey_has_contracts` AS select `dhw`.`api_key` AS `api_key`,`c`.`id` AS `contract_id`,`c`.`dep_id` AS `dep_id`,`c`.`client_id` AS `client_id`,`c`.`contracts` AS `contract`,concat(substr(`u`.`client`,1,3),'. *. ',substr(substring_index(`u`.`client`,' ',-(1)),1,1),'-',substr(substring_index(`u`.`client`,' ',-(1)),-(2),2)) AS `client`,`dhw`.`id` AS `dhw_id` from ((`dep_has_worker` `dhw` join `contracts` `c` on((`c`.`dep_id` = `dhw`.`dep_id`))) join `client` `u` on((`u`.`id` = `c`.`client_id`))) */;
/*!50001 SET character_set_client      = @saved_cs_client */;
/*!50001 SET character_set_results     = @saved_cs_results */;
/*!50001 SET collation_connection      = @saved_col_connection */;

--
-- Final view structure for view `_bm_dep_has_client`
--

/*!50001 DROP VIEW IF EXISTS `_bm_dep_has_client`*/;
/*!50001 SET @saved_cs_client          = @@character_set_client */;
/*!50001 SET @saved_cs_results         = @@character_set_results */;
/*!50001 SET @saved_col_connection     = @@collation_connection */;
/*!50001 SET character_set_client      = utf8mb4 */;
/*!50001 SET character_set_results     = utf8mb4 */;
/*!50001 SET collation_connection      = utf8mb4_0900_ai_ci */;
/*!50001 CREATE ALGORITHM=UNDEFINED */
/*!50013 DEFINER=`root`@`localhost` SQL SECURITY DEFINER */
/*!50001 VIEW `_bm_dep_has_client` AS select `u`.`id` AS `id`,`u`.`client` AS `client`,`u`.`client_short` AS `client_short`,`u`.`clientDeath` AS `clientDeath`,`u`.`clientbirth` AS `clientbirth`,`u`.`ESRN` AS `ESRN`,`u`.`note` AS `note`,`u`.`phone` AS `phone`,`u`.`snils` AS `snils`,`u`.`curator` AS `curator`,`u`.`create` AS `create`,`u`.`ts` AS `ts`,`u`.`cr_by` AS `cr_by`,`u`.`upd_by` AS `upd_by`,`u`.`cr_dep_id` AS `cr_dep_id` from `client` `u` where `u`.`id` in (select `m`.`client_id` from `main` `m` where `m`.`dep_id` in (select `_active_dep`.`id` from `_active_dep`)) */;
/*!50001 SET character_set_client      = @saved_cs_client */;
/*!50001 SET character_set_results     = @saved_cs_results */;
/*!50001 SET collation_connection      = @saved_col_connection */;

--
-- Final view structure for view `_bm_dep_has_client_other_year`
--

/*!50001 DROP VIEW IF EXISTS `_bm_dep_has_client_other_year`*/;
/*!50001 SET @saved_cs_client          = @@character_set_client */;
/*!50001 SET @saved_cs_results         = @@character_set_results */;
/*!50001 SET @saved_col_connection     = @@collation_connection */;
/*!50001 SET character_set_client      = utf8mb4 */;
/*!50001 SET character_set_results     = utf8mb4 */;
/*!50001 SET collation_connection      = utf8mb4_0900_ai_ci */;
/*!50001 CREATE ALGORITHM=UNDEFINED */
/*!50013 DEFINER=`root`@`localhost` SQL SECURITY DEFINER */
/*!50001 VIEW `_bm_dep_has_client_other_year` AS select `_bm_dep_has_client`.`id` AS `id`,`_bm_dep_has_client`.`client` AS `client`,`_bm_dep_has_client`.`client_short` AS `client_short`,`_bm_dep_has_client`.`clientDeath` AS `clientDeath`,`_bm_dep_has_client`.`clientbirth` AS `clientbirth`,`_bm_dep_has_client`.`ESRN` AS `ESRN`,`_bm_dep_has_client`.`note` AS `note`,`_bm_dep_has_client`.`phone` AS `phone`,`_bm_dep_has_client`.`snils` AS `snils`,`_bm_dep_has_client`.`curator` AS `curator`,`_bm_dep_has_client`.`create` AS `create`,`_bm_dep_has_client`.`ts` AS `ts`,`_bm_dep_has_client`.`cr_by` AS `cr_by`,`_bm_dep_has_client`.`upd_by` AS `upd_by`,`_bm_dep_has_client`.`cr_dep_id` AS `cr_dep_id` from `_bm_dep_has_client` where `_bm_dep_has_client`.`id` in (select `_bm_dep_has_client_year`.`id` from `_bm_dep_has_client_year`) is false */;
/*!50001 SET character_set_client      = @saved_cs_client */;
/*!50001 SET character_set_results     = @saved_cs_results */;
/*!50001 SET collation_connection      = @saved_col_connection */;

--
-- Final view structure for view `_bm_dep_has_client_year`
--

/*!50001 DROP VIEW IF EXISTS `_bm_dep_has_client_year`*/;
/*!50001 SET @saved_cs_client          = @@character_set_client */;
/*!50001 SET @saved_cs_results         = @@character_set_results */;
/*!50001 SET @saved_col_connection     = @@collation_connection */;
/*!50001 SET character_set_client      = utf8mb4 */;
/*!50001 SET character_set_results     = utf8mb4 */;
/*!50001 SET collation_connection      = utf8mb4_0900_ai_ci */;
/*!50001 CREATE ALGORITHM=UNDEFINED */
/*!50013 DEFINER=`root`@`localhost` SQL SECURITY DEFINER */
/*!50001 VIEW `_bm_dep_has_client_year` AS select `u`.`id` AS `id`,`u`.`client` AS `client`,`u`.`client_short` AS `client_short`,`u`.`clientDeath` AS `clientDeath`,`u`.`clientbirth` AS `clientbirth`,`u`.`ESRN` AS `ESRN`,`u`.`note` AS `note`,`u`.`phone` AS `phone`,`u`.`snils` AS `snils`,`u`.`curator` AS `curator`,`u`.`create` AS `create`,`u`.`ts` AS `ts`,`u`.`cr_by` AS `cr_by`,`u`.`upd_by` AS `upd_by`,`u`.`cr_dep_id` AS `cr_dep_id` from `client` `u` where `u`.`id` in (select `m`.`client_id` from `main` `m` where (`m`.`dep_id` in (select `_active_dep`.`id` from `_active_dep`) and (year(`m`.`vdate`) = `GET_YEAR`(`GET_WID`())))) */;
/*!50001 SET character_set_client      = @saved_cs_client */;
/*!50001 SET character_set_results     = @saved_cs_results */;
/*!50001 SET collation_connection      = @saved_col_connection */;

--
-- Final view structure for view `_categ_list_client`
--

/*!50001 DROP VIEW IF EXISTS `_categ_list_client`*/;
/*!50001 SET @saved_cs_client          = @@character_set_client */;
/*!50001 SET @saved_cs_results         = @@character_set_results */;
/*!50001 SET @saved_col_connection     = @@collation_connection */;
/*!50001 SET character_set_client      = utf8mb4 */;
/*!50001 SET character_set_results     = utf8mb4 */;
/*!50001 SET collation_connection      = utf8mb4_0900_ai_ci */;
/*!50001 CREATE ALGORITHM=UNDEFINED */
/*!50013 DEFINER=`root`@`localhost` SQL SECURITY DEFINER */
/*!50001 VIEW `_categ_list_client` AS select `uhc`.`category_id` AS `category_id`,`m`.`client_id` AS `client_id`,`m`.`quantity` AS `quantity`,`m`.`vdate` AS `vdate`,`s`.`tnum` AS `serv` from ((`main` `m` join `client_has_category` `uhc` on((`m`.`client_id` = `uhc`.`client_id`))) join `serv` `s` on((`s`.`id` = `m`.`serv_id`))) where (`m`.`dep_id` in (select `_active_dep_static`.`id` from `_active_dep_static`) and (coalesce(`uhc`.`archive`,0) = 0)) */;
/*!50001 SET character_set_client      = @saved_cs_client */;
/*!50001 SET character_set_results     = @saved_cs_results */;
/*!50001 SET collation_connection      = @saved_col_connection */;

--
-- Final view structure for view `_client`
--

/*!50001 DROP VIEW IF EXISTS `_client`*/;
/*!50001 SET @saved_cs_client          = @@character_set_client */;
/*!50001 SET @saved_cs_results         = @@character_set_results */;
/*!50001 SET @saved_col_connection     = @@collation_connection */;
/*!50001 SET character_set_client      = utf8mb4 */;
/*!50001 SET character_set_results     = utf8mb4 */;
/*!50001 SET collation_connection      = utf8mb4_0900_ai_ci */;
/*!50001 CREATE ALGORITHM=UNDEFINED */
/*!50013 DEFINER=`root`@`localhost` SQL SECURITY DEFINER */
/*!50001 VIEW `_client` AS select `client`.`id` AS `id`,`client`.`client` AS `client`,`client`.`client_short` AS `client_short`,`client`.`clientDeath` AS `clientDeath`,`client`.`clientbirth` AS `clientbirth`,`client`.`ESRN` AS `ESRN`,`client`.`note` AS `note`,`client`.`phone` AS `phone`,`client`.`snils` AS `snils`,`client`.`curator` AS `curator`,`client`.`create` AS `create`,`client`.`ts` AS `ts`,`client`.`cr_by` AS `cr_by`,`client`.`upd_by` AS `upd_by`,`client`.`cr_dep_id` AS `cr_dep_id` from `client` */;
/*!50001 SET character_set_client      = @saved_cs_client */;
/*!50001 SET character_set_results     = @saved_cs_results */;
/*!50001 SET collation_connection      = @saved_col_connection */;

--
-- Final view structure for view `_client_has_add_info`
--

/*!50001 DROP VIEW IF EXISTS `_client_has_add_info`*/;
/*!50001 SET @saved_cs_client          = @@character_set_client */;
/*!50001 SET @saved_cs_results         = @@character_set_results */;
/*!50001 SET @saved_col_connection     = @@collation_connection */;
/*!50001 SET character_set_client      = utf8mb4 */;
/*!50001 SET character_set_results     = utf8mb4 */;
/*!50001 SET collation_connection      = utf8mb4_0900_ai_ci */;
/*!50001 CREATE ALGORITHM=UNDEFINED */
/*!50013 DEFINER=`root`@`localhost` SQL SECURITY DEFINER */
/*!50001 VIEW `_client_has_add_info` AS select `u`.`id` AS `client_id`,`a`.`pddate` AS `pddate`,`a`.`contracts_id` AS `contracts_id`,`a`.`predv_money` AS `predv_money`,`a`.`curFIO` AS `curFIO`,`a`.`psp` AS `psp`,`a`.`address` AS `address`,`a`.`sdd` AS `sdd`,`a`.`sdd_date` AS `sdd_date`,`a`.`perc` AS `perc`,`a`.`not_standart_contract` AS `not_standart_contract`,`a`.`not_standart_act` AS `not_standart_act`,`a`.`note` AS `note`,`a`.`create` AS `create`,`a`.`ts` AS `ts`,`a`.`cr_by` AS `cr_by`,`a`.`upd_by` AS `upd_by`,`a`.`repr_FIO` AS `repr_FIO`,`a`.`repr_addr` AS `repr_addr`,`a`.`repr_psp` AS `repr_psp`,`a`.`work_livemin` AS `work_livemin` from ((`add_info` `a` join `contracts` `c` on((`c`.`id` = `a`.`contracts_id`))) join `client` `u` on((`c`.`client_id` = `u`.`id`))) order by `a`.`pddate` desc */;
/*!50001 SET character_set_client      = @saved_cs_client */;
/*!50001 SET character_set_results     = @saved_cs_results */;
/*!50001 SET collation_connection      = @saved_col_connection */;

--
-- Final view structure for view `_client_has_category_for_last_client`
--

/*!50001 DROP VIEW IF EXISTS `_client_has_category_for_last_client`*/;
/*!50001 SET @saved_cs_client          = @@character_set_client */;
/*!50001 SET @saved_cs_results         = @@character_set_results */;
/*!50001 SET @saved_col_connection     = @@collation_connection */;
/*!50001 SET character_set_client      = utf8mb4 */;
/*!50001 SET character_set_results     = utf8mb4 */;
/*!50001 SET collation_connection      = utf8mb4_0900_ai_ci */;
/*!50001 CREATE ALGORITHM=UNDEFINED */
/*!50013 DEFINER=`root`@`localhost` SQL SECURITY DEFINER */
/*!50001 VIEW `_client_has_category_for_last_client` AS select `uhc`.`client_id` AS `client_id`,`uhc`.`category_id` AS `category_id`,`uhc`.`get_date` AS `get_date`,`uhc`.`archive` AS `archive`,`uhc`.`note` AS `note`,`uhc`.`create` AS `create`,`uhc`.`ts` AS `ts`,`uhc`.`cr_by` AS `cr_by`,`uhc`.`upd_by` AS `upd_by` from `client_has_category` `uhc` where (`uhc`.`client_id` = `get_last_client`()) */;
/*!50001 SET character_set_client      = @saved_cs_client */;
/*!50001 SET character_set_results     = @saved_cs_results */;
/*!50001 SET collation_connection      = @saved_col_connection */;

--
-- Final view structure for view `_client_has_contracts`
--

/*!50001 DROP VIEW IF EXISTS `_client_has_contracts`*/;
/*!50001 SET @saved_cs_client          = @@character_set_client */;
/*!50001 SET @saved_cs_results         = @@character_set_results */;
/*!50001 SET @saved_col_connection     = @@collation_connection */;
/*!50001 SET character_set_client      = utf8mb4 */;
/*!50001 SET character_set_results     = utf8mb4 */;
/*!50001 SET collation_connection      = utf8mb4_0900_ai_ci */;
/*!50001 CREATE ALGORITHM=UNDEFINED */
/*!50013 DEFINER=`root`@`localhost` SQL SECURITY DEFINER */
/*!50001 VIEW `_client_has_contracts` AS select `c`.`id` AS `id`,`c`.`contracts` AS `contracts`,`c`.`contracts2` AS `contracts2`,`c`.`client_id` AS `client_id`,`c`.`dep_id` AS `dep_id`,`c`.`ripso_id` AS `ripso_id`,`c`.`blocked` AS `blocked`,`c`.`startdate` AS `startdate`,`c`.`enddate` AS `enddate`,`c`.`ippsuNum` AS `ippsuNum`,`c`.`note` AS `note`,`c`.`create` AS `create`,`c`.`ts` AS `ts`,`c`.`cr_by` AS `cr_by`,`c`.`upd_by` AS `upd_by`,`c`.`to_recheck` AS `to_recheck`,`c`.`check_date` AS `check_date`,`c`.`pyc_prim` AS `pyc_prim` from `contracts` `c` order by `c`.`blocked` */;
/*!50001 SET character_set_client      = @saved_cs_client */;
/*!50001 SET character_set_results     = @saved_cs_results */;
/*!50001 SET collation_connection      = @saved_col_connection */;

--
-- Final view structure for view `_client_has_invalid_contracts`
--

/*!50001 DROP VIEW IF EXISTS `_client_has_invalid_contracts`*/;
/*!50001 SET @saved_cs_client          = @@character_set_client */;
/*!50001 SET @saved_cs_results         = @@character_set_results */;
/*!50001 SET @saved_col_connection     = @@collation_connection */;
/*!50001 SET character_set_client      = utf8mb4 */;
/*!50001 SET character_set_results     = utf8mb4 */;
/*!50001 SET collation_connection      = utf8mb4_0900_ai_ci */;
/*!50001 CREATE ALGORITHM=UNDEFINED */
/*!50013 DEFINER=`root`@`localhost` SQL SECURITY DEFINER */
/*!50001 VIEW `_client_has_invalid_contracts` AS select `u`.`client` AS `client`,`c`.`id` AS `id`,`c`.`contracts` AS `contracts`,`c`.`client_id` AS `client_id`,`c`.`dep_id` AS `dep_id`,`c`.`ripso_id` AS `ripso_id`,`c`.`blocked` AS `blocked`,`c`.`startdate` AS `startdate`,`c`.`enddate` AS `enddate`,`c`.`ippsuNum` AS `ippsuNum`,`c`.`note` AS `note`,`c`.`create` AS `create`,`c`.`ts` AS `ts`,`c`.`cr_by` AS `cr_by`,`c`.`upd_by` AS `upd_by`,`c`.`to_recheck` AS `to_recheck`,`c`.`check_date` AS `check_date` from (`client` `u` join `contracts` `c` on((`c`.`client_id` = `u`.`id`))) where (`c`.`enddate` < curdate()) */;
/*!50001 SET character_set_client      = @saved_cs_client */;
/*!50001 SET character_set_results     = @saved_cs_results */;
/*!50001 SET collation_connection      = @saved_col_connection */;

--
-- Final view structure for view `_client_has_main`
--

/*!50001 DROP VIEW IF EXISTS `_client_has_main`*/;
/*!50001 SET @saved_cs_client          = @@character_set_client */;
/*!50001 SET @saved_cs_results         = @@character_set_results */;
/*!50001 SET @saved_col_connection     = @@collation_connection */;
/*!50001 SET character_set_client      = utf8mb4 */;
/*!50001 SET character_set_results     = utf8mb4 */;
/*!50001 SET collation_connection      = utf8mb4_0900_ai_ci */;
/*!50001 CREATE ALGORITHM=UNDEFINED */
/*!50013 DEFINER=`root`@`localhost` SQL SECURITY DEFINER */
/*!50001 VIEW `_client_has_main` AS select `main`.`id` AS `id`,`main`.`contracts_id` AS `contracts_id`,`main`.`dep_id` AS `dep_id`,`main`.`client_id` AS `client_id`,`main`.`serv_id` AS `serv_id`,`main`.`dep_has_worker_id` AS `dep_has_worker_id`,`main`.`worker_id` AS `worker_id`,`main`.`vdate` AS `vdate`,`main`.`quantity` AS `quantity`,`main`.`note` AS `note`,`main`.`create` AS `create`,`main`.`ts` AS `ts`,`main`.`cr_by` AS `cr_by`,`main`.`upd_by` AS `upd_by`,`main`.`reported` AS `reported`,`main`.`wdate` AS `wdate`,`main`.`overdid` AS `overdid`,`main`.`prev_quantity` AS `prev_quantity` from `main` where (`main`.`client_id` = `get_last_client`()) */;
/*!50001 SET character_set_client      = @saved_cs_client */;
/*!50001 SET character_set_results     = @saved_cs_results */;
/*!50001 SET collation_connection      = @saved_col_connection */;

--
-- Final view structure for view `_client_has_valid_contracts`
--

/*!50001 DROP VIEW IF EXISTS `_client_has_valid_contracts`*/;
/*!50001 SET @saved_cs_client          = @@character_set_client */;
/*!50001 SET @saved_cs_results         = @@character_set_results */;
/*!50001 SET @saved_col_connection     = @@collation_connection */;
/*!50001 SET character_set_client      = utf8mb4 */;
/*!50001 SET character_set_results     = utf8mb4 */;
/*!50001 SET collation_connection      = utf8mb4_0900_ai_ci */;
/*!50001 CREATE ALGORITHM=UNDEFINED */
/*!50013 DEFINER=`root`@`localhost` SQL SECURITY DEFINER */
/*!50001 VIEW `_client_has_valid_contracts` AS select `u`.`client` AS `client`,`c`.`id` AS `id`,`c`.`contracts` AS `contracts`,`c`.`client_id` AS `client_id`,`c`.`dep_id` AS `dep_id`,`c`.`ripso_id` AS `ripso_id`,`c`.`blocked` AS `blocked`,`c`.`startdate` AS `startdate`,`c`.`enddate` AS `enddate`,`c`.`ippsuNum` AS `ippsuNum`,`c`.`note` AS `note`,`c`.`create` AS `create`,`c`.`ts` AS `ts`,`c`.`cr_by` AS `cr_by`,`c`.`upd_by` AS `upd_by`,`c`.`to_recheck` AS `to_recheck`,`c`.`check_date` AS `check_date` from (`client` `u` join `contracts` `c` on((`c`.`client_id` = `u`.`id`))) where (`c`.`enddate` > curdate()) */;
/*!50001 SET character_set_client      = @saved_cs_client */;
/*!50001 SET character_set_results     = @saved_cs_results */;
/*!50001 SET collation_connection      = @saved_col_connection */;

--
-- Final view structure for view `_contr_has_add_info`
--

/*!50001 DROP VIEW IF EXISTS `_contr_has_add_info`*/;
/*!50001 SET @saved_cs_client          = @@character_set_client */;
/*!50001 SET @saved_cs_results         = @@character_set_results */;
/*!50001 SET @saved_col_connection     = @@collation_connection */;
/*!50001 SET character_set_client      = utf8mb4 */;
/*!50001 SET character_set_results     = utf8mb4 */;
/*!50001 SET collation_connection      = utf8mb4_0900_ai_ci */;
/*!50001 CREATE ALGORITHM=UNDEFINED */
/*!50013 DEFINER=`root`@`localhost` SQL SECURITY DEFINER */
/*!50001 VIEW `_contr_has_add_info` AS select `add_info`.`pddate` AS `pddate`,`add_info`.`contracts_id` AS `contracts_id`,`add_info`.`predv_money` AS `predv_money`,`add_info`.`curFIO` AS `curFIO`,`add_info`.`psp` AS `psp`,`add_info`.`address` AS `address`,`add_info`.`sdd` AS `sdd`,`add_info`.`sdd_date` AS `sdd_date`,`add_info`.`perc` AS `perc`,`add_info`.`not_standart_contract` AS `not_standart_contract`,`add_info`.`not_standart_act` AS `not_standart_act`,`add_info`.`note` AS `note`,`add_info`.`create` AS `create`,`add_info`.`ts` AS `ts`,`add_info`.`cr_by` AS `cr_by`,`add_info`.`upd_by` AS `upd_by`,`add_info`.`repr_FIO` AS `repr_FIO`,`add_info`.`repr_addr` AS `repr_addr`,`add_info`.`repr_psp` AS `repr_psp`,`add_info`.`work_livemin` AS `work_livemin` from `add_info` where (`add_info`.`contracts_id` = `get_last_contr`()) */;
/*!50001 SET character_set_client      = @saved_cs_client */;
/*!50001 SET character_set_results     = @saved_cs_results */;
/*!50001 SET collation_connection      = @saved_col_connection */;

--
-- Final view structure for view `_contr_has_main`
--

/*!50001 DROP VIEW IF EXISTS `_contr_has_main`*/;
/*!50001 SET @saved_cs_client          = @@character_set_client */;
/*!50001 SET @saved_cs_results         = @@character_set_results */;
/*!50001 SET @saved_col_connection     = @@collation_connection */;
/*!50001 SET character_set_client      = utf8mb4 */;
/*!50001 SET character_set_results     = utf8mb4 */;
/*!50001 SET collation_connection      = utf8mb4_0900_ai_ci */;
/*!50001 CREATE ALGORITHM=UNDEFINED */
/*!50013 DEFINER=`root`@`localhost` SQL SECURITY DEFINER */
/*!50001 VIEW `_contr_has_main` AS select `m`.`id` AS `id`,`m`.`contracts_id` AS `contracts_id`,`m`.`dep_id` AS `dep_id`,`m`.`client_id` AS `client_id`,`m`.`serv_id` AS `serv_id`,`m`.`dep_has_worker_id` AS `dep_has_worker_id`,`m`.`worker_id` AS `worker_id`,`m`.`vdate` AS `vdate`,`m`.`quantity` AS `quantity`,`m`.`note` AS `note`,`m`.`create` AS `create`,`m`.`ts` AS `ts`,`m`.`cr_by` AS `cr_by`,`m`.`upd_by` AS `upd_by`,`m`.`reported` AS `reported`,`m`.`wdate` AS `wdate`,`m`.`overdid` AS `overdid`,`m`.`prev_quantity` AS `prev_quantity` from (`main` `m` join `contracts` `c` on((`m`.`contracts_id` = `c`.`id`))) */;
/*!50001 SET character_set_client      = @saved_cs_client */;
/*!50001 SET character_set_results     = @saved_cs_results */;
/*!50001 SET collation_connection      = @saved_col_connection */;

--
-- Final view structure for view `_contr_has_serv_predv`
--

/*!50001 DROP VIEW IF EXISTS `_contr_has_serv_predv`*/;
/*!50001 SET @saved_cs_client          = @@character_set_client */;
/*!50001 SET @saved_cs_results         = @@character_set_results */;
/*!50001 SET @saved_col_connection     = @@collation_connection */;
/*!50001 SET character_set_client      = utf8mb4 */;
/*!50001 SET character_set_results     = utf8mb4 */;
/*!50001 SET collation_connection      = utf8mb4_0900_ai_ci */;
/*!50001 CREATE ALGORITHM=UNDEFINED */
/*!50013 DEFINER=`root`@`localhost` SQL SECURITY DEFINER */
/*!50001 VIEW `_contr_has_serv_predv` AS select `f`.`contracts_id` AS `contracts_id`,(`f`.`quantity` * `f`.`price`) AS `full_price`,`f`.`tnum` AS `tnum`,`f`.`serv` AS `serv`,`f`.`serv_text` AS `serv_text`,`f`.`quantity` AS `quantity`,`f`.`price` AS `price`,((`f`.`quantity` * `f`.`price`) * `f`.`perc`) AS `to_pay`,`f`.`servform_id` AS `servform_id`,`f`.`serv_id` AS `serv_id`,`f`.`sub_serv` AS `sub_serv`,`f`.`vdate` AS `vdate`,`f`.`dep_id` AS `dep_id`,`f`.`perc` AS `perc`,`f`.`year` AS `year` from (select `s`.`year` AS `year`,`khs`.`contracts_id` AS `contracts_id`,`s`.`tnum` AS `tnum`,`s`.`serv_text` AS `serv_text`,`s`.`serv` AS `serv`,if((round((`khs`.`planned` / `r`.`months`),0) = 0),ceiling((`khs`.`planned` / `r`.`months`)),round((`khs`.`planned` / `r`.`months`),0)) AS `quantity`,`s`.`price` AS `price`,`r`.`servform_id` AS `servform_id`,`khs`.`serv_id` AS `serv_id`,`s`.`sub_serv` AS `sub_serv`,`c`.`startdate` AS `vdate`,`c`.`dep_id` AS `dep_id`,(select `pd`.`perc` from `add_info` `pd` where ((`pd`.`pddate` <= `c`.`startdate`) and (`pd`.`contracts_id` = `khs`.`contracts_id`)) order by `pd`.`pddate` desc limit 1) AS `perc` from ((((`_contracts_has_serv` `khs` join `contracts` `c` on((`c`.`id` = `khs`.`contracts_id`))) join `serv` `s` on((`s`.`id` = `khs`.`serv_id`))) join `ripso` `r` on((`r`.`id` = `c`.`ripso_id`))) join `servform` `sf` on((`r`.`servform_id` = `sf`.`id`)))) `f` */;
/*!50001 SET character_set_client      = @saved_cs_client */;
/*!50001 SET character_set_results     = @saved_cs_results */;
/*!50001 SET collation_connection      = @saved_col_connection */;

--
-- Final view structure for view `_contracts`
--

/*!50001 DROP VIEW IF EXISTS `_contracts`*/;
/*!50001 SET @saved_cs_client          = @@character_set_client */;
/*!50001 SET @saved_cs_results         = @@character_set_results */;
/*!50001 SET @saved_col_connection     = @@collation_connection */;
/*!50001 SET character_set_client      = utf8mb4 */;
/*!50001 SET character_set_results     = utf8mb4 */;
/*!50001 SET collation_connection      = utf8mb4_0900_ai_ci */;
/*!50001 CREATE ALGORITHM=UNDEFINED */
/*!50013 DEFINER=`root`@`localhost` SQL SECURITY DEFINER */
/*!50001 VIEW `_contracts` AS select `c`.`id` AS `id`,`c`.`contracts` AS `contracts`,`c`.`client_id` AS `client_id`,`c`.`dep_id` AS `dep_id`,`c`.`ripso_id` AS `ripso_id`,`c`.`blocked` AS `blocked`,`c`.`startdate` AS `startdate`,`c`.`enddate` AS `enddate`,`c`.`ippsuNum` AS `ippsuNum`,`c`.`note` AS `note`,`c`.`create` AS `create`,`c`.`ts` AS `ts`,`c`.`cr_by` AS `cr_by`,`c`.`upd_by` AS `upd_by`,`c`.`to_recheck` AS `to_recheck`,`c`.`check_date` AS `check_date`,`r`.`servform_id` AS `servform_id` from (`contracts` `c` left join `ripso` `r` on((`r`.`id` = `c`.`ripso_id`))) */;
/*!50001 SET character_set_client      = @saved_cs_client */;
/*!50001 SET character_set_results     = @saved_cs_results */;
/*!50001 SET collation_connection      = @saved_col_connection */;

--
-- Final view structure for view `_contracts_has_serv`
--

/*!50001 DROP VIEW IF EXISTS `_contracts_has_serv`*/;
/*!50001 SET @saved_cs_client          = @@character_set_client */;
/*!50001 SET @saved_cs_results         = @@character_set_results */;
/*!50001 SET @saved_col_connection     = @@collation_connection */;
/*!50001 SET character_set_client      = utf8mb4 */;
/*!50001 SET character_set_results     = utf8mb4 */;
/*!50001 SET collation_connection      = utf8mb4_0900_ai_ci */;
/*!50001 CREATE ALGORITHM=UNDEFINED */
/*!50013 DEFINER=`root`@`localhost` SQL SECURITY DEFINER */
/*!50001 VIEW `_contracts_has_serv` AS select `chs`.`serv_id` AS `serv_id`,`chs`.`contracts_id` AS `contracts_id`,`chs`.`planned` AS `planned`,`chs`.`filled` AS `filled`,`chs`.`note` AS `note`,`chs`.`archive` AS `archive`,`chs`.`create` AS `create`,`chs`.`ts` AS `ts`,`chs`.`cr_by` AS `cr_by`,`chs`.`upd_by` AS `upd_by`,`chs`.`to_recheck` AS `to_recheck`,`chs`.`check_date` AS `check_date`,`chs`.`filled_old` AS `filled_old`,`s`.`tnum` AS `tnum` from (`contracts_has_serv` `chs` join `serv` `s` on((`s`.`id` = `chs`.`serv_id`))) */;
/*!50001 SET character_set_client      = @saved_cs_client */;
/*!50001 SET character_set_results     = @saved_cs_results */;
/*!50001 SET collation_connection      = @saved_col_connection */;

--
-- Final view structure for view `_dep_has_add_info`
--

/*!50001 DROP VIEW IF EXISTS `_dep_has_add_info`*/;
/*!50001 SET @saved_cs_client          = @@character_set_client */;
/*!50001 SET @saved_cs_results         = @@character_set_results */;
/*!50001 SET @saved_col_connection     = @@collation_connection */;
/*!50001 SET character_set_client      = utf8mb4 */;
/*!50001 SET character_set_results     = utf8mb4 */;
/*!50001 SET collation_connection      = utf8mb4_0900_ai_ci */;
/*!50001 CREATE ALGORITHM=UNDEFINED */
/*!50013 DEFINER=`root`@`localhost` SQL SECURITY DEFINER */
/*!50001 VIEW `_dep_has_add_info` AS select `ai`.`pddate` AS `pddate`,`ai`.`contracts_id` AS `contracts_id`,`ai`.`predv_money` AS `predv_money`,`ai`.`curFIO` AS `curFIO`,`ai`.`psp` AS `psp`,`ai`.`address` AS `address`,`ai`.`sdd` AS `sdd`,`ai`.`sdd_date` AS `sdd_date`,`ai`.`perc` AS `perc`,`ai`.`not_standart_contract` AS `not_standart_contract`,`ai`.`not_standart_act` AS `not_standart_act`,`ai`.`note` AS `note`,`ai`.`create` AS `create`,`ai`.`ts` AS `ts`,`ai`.`cr_by` AS `cr_by`,`ai`.`upd_by` AS `upd_by`,`ai`.`repr_FIO` AS `repr_FIO`,`ai`.`repr_addr` AS `repr_addr`,`ai`.`repr_psp` AS `repr_psp`,`ai`.`work_livemin` AS `work_livemin` from (`add_info` `ai` join `contracts` `c` on((`c`.`id` = `ai`.`contracts_id`))) where `c`.`dep_id` in (select `_active_dep`.`id` from `_active_dep`) */;
/*!50001 SET character_set_client      = @saved_cs_client */;
/*!50001 SET character_set_results     = @saved_cs_results */;
/*!50001 SET collation_connection      = @saved_col_connection */;

--
-- Final view structure for view `_dep_has_client`
--

/*!50001 DROP VIEW IF EXISTS `_dep_has_client`*/;
/*!50001 SET @saved_cs_client          = @@character_set_client */;
/*!50001 SET @saved_cs_results         = @@character_set_results */;
/*!50001 SET @saved_col_connection     = @@collation_connection */;
/*!50001 SET character_set_client      = utf8mb4 */;
/*!50001 SET character_set_results     = utf8mb4 */;
/*!50001 SET collation_connection      = utf8mb4_0900_ai_ci */;
/*!50001 CREATE ALGORITHM=MERGE */
/*!50013 DEFINER=`root`@`localhost` SQL SECURITY DEFINER */
/*!50001 VIEW `_dep_has_client` AS select `u1`.`id` AS `id`,`u1`.`client` AS `client`,`u1`.`client_short` AS `client_short`,`u1`.`clientDeath` AS `clientDeath`,`u1`.`clientbirth` AS `clientbirth`,`u1`.`ESRN` AS `ESRN`,`u1`.`note` AS `note`,`u1`.`phone` AS `phone`,`u1`.`snils` AS `snils`,`u1`.`curator` AS `curator`,`u1`.`create` AS `create`,`u1`.`ts` AS `ts`,`u1`.`cr_by` AS `cr_by`,`u1`.`upd_by` AS `upd_by`,`u1`.`cr_dep_id` AS `cr_dep_id` from (select distinct `u`.`id` AS `id`,`u`.`client` AS `client`,`u`.`client_short` AS `client_short`,`u`.`clientDeath` AS `clientDeath`,`u`.`clientbirth` AS `clientbirth`,`u`.`ESRN` AS `ESRN`,`u`.`note` AS `note`,`u`.`phone` AS `phone`,`u`.`snils` AS `snils`,`u`.`curator` AS `curator`,`u`.`create` AS `create`,`u`.`ts` AS `ts`,`u`.`cr_by` AS `cr_by`,`u`.`upd_by` AS `upd_by`,`u`.`cr_dep_id` AS `cr_dep_id` from (`client` `u` join `contracts` `c` on((`c`.`client_id` = `u`.`id`))) where ((`c`.`blocked` = false) and (`u`.`cr_dep_id` in (select `_active_dep`.`id` from `_active_dep`) or `c`.`dep_id` in (select `_active_dep`.`id` from `_active_dep`)))) `u1` */;
/*!50001 SET character_set_client      = @saved_cs_client */;
/*!50001 SET character_set_results     = @saved_cs_results */;
/*!50001 SET collation_connection      = @saved_col_connection */;

--
-- Final view structure for view `_dep_has_client_blocked_in_year`
--

/*!50001 DROP VIEW IF EXISTS `_dep_has_client_blocked_in_year`*/;
/*!50001 SET @saved_cs_client          = @@character_set_client */;
/*!50001 SET @saved_cs_results         = @@character_set_results */;
/*!50001 SET @saved_col_connection     = @@collation_connection */;
/*!50001 SET character_set_client      = utf8mb4 */;
/*!50001 SET character_set_results     = utf8mb4 */;
/*!50001 SET collation_connection      = utf8mb4_0900_ai_ci */;
/*!50001 CREATE ALGORITHM=UNDEFINED */
/*!50013 DEFINER=`root`@`localhost` SQL SECURITY DEFINER */
/*!50001 VIEW `_dep_has_client_blocked_in_year` AS select `u`.`id` AS `id`,`u`.`client` AS `client`,`u`.`client_short` AS `client_short`,`u`.`clientDeath` AS `clientDeath`,`u`.`clientbirth` AS `clientbirth`,`u`.`ESRN` AS `ESRN`,`u`.`note` AS `note`,`u`.`phone` AS `phone`,`u`.`snils` AS `snils`,`u`.`curator` AS `curator`,`u`.`create` AS `create`,`u`.`ts` AS `ts`,`u`.`cr_by` AS `cr_by`,`u`.`upd_by` AS `upd_by`,`u`.`cr_dep_id` AS `cr_dep_id` from (`client` `u` join `contracts` `c` on((`c`.`client_id` = `u`.`id`))) where ((`c`.`blocked` = true) and (year(`c`.`enddate`) = `get_year`(`get_WID`())) and (`u`.`cr_dep_id` in (select `_active_dep`.`id` from `_active_dep`) or `c`.`dep_id` in (select `_active_dep`.`id` from `_active_dep`))) */;
/*!50001 SET character_set_client      = @saved_cs_client */;
/*!50001 SET character_set_results     = @saved_cs_results */;
/*!50001 SET collation_connection      = @saved_col_connection */;

--
-- Final view structure for view `_dep_has_client_by_ripso`
--

/*!50001 DROP VIEW IF EXISTS `_dep_has_client_by_ripso`*/;
/*!50001 SET @saved_cs_client          = @@character_set_client */;
/*!50001 SET @saved_cs_results         = @@character_set_results */;
/*!50001 SET @saved_col_connection     = @@collation_connection */;
/*!50001 SET character_set_client      = utf8mb4 */;
/*!50001 SET character_set_results     = utf8mb4 */;
/*!50001 SET collation_connection      = utf8mb4_0900_ai_ci */;
/*!50001 CREATE ALGORITHM=UNDEFINED */
/*!50013 DEFINER=`root`@`localhost` SQL SECURITY DEFINER */
/*!50001 VIEW `_dep_has_client_by_ripso` AS select `client`.`id` AS `id`,`client`.`client` AS `client`,`client`.`client_short` AS `client_short`,`client`.`clientDeath` AS `clientDeath`,`client`.`clientbirth` AS `clientbirth`,`client`.`ESRN` AS `ESRN`,`client`.`note` AS `note`,`client`.`phone` AS `phone`,`client`.`snils` AS `snils`,`client`.`curator` AS `curator`,`client`.`create` AS `create`,`client`.`ts` AS `ts`,`client`.`cr_by` AS `cr_by`,`client`.`upd_by` AS `upd_by` from `client` where `client`.`id` in (select `c`.`client_id` from (`contracts` `c` join `dep_has_ripso` `rod` on((`rod`.`ripso_id` = `c`.`ripso_id`))) where `rod`.`dep_id` in (select `_active_dep`.`id` from `_active_dep`)) */;
/*!50001 SET character_set_client      = @saved_cs_client */;
/*!50001 SET character_set_results     = @saved_cs_results */;
/*!50001 SET collation_connection      = @saved_col_connection */;

--
-- Final view structure for view `_dep_has_client_contracts`
--

/*!50001 DROP VIEW IF EXISTS `_dep_has_client_contracts`*/;
/*!50001 SET @saved_cs_client          = @@character_set_client */;
/*!50001 SET @saved_cs_results         = @@character_set_results */;
/*!50001 SET @saved_col_connection     = @@collation_connection */;
/*!50001 SET character_set_client      = utf8mb4 */;
/*!50001 SET character_set_results     = utf8mb4 */;
/*!50001 SET collation_connection      = utf8mb4_0900_ai_ci */;
/*!50001 CREATE ALGORITHM=UNDEFINED */
/*!50013 DEFINER=`root`@`localhost` SQL SECURITY DEFINER */
/*!50001 VIEW `_dep_has_client_contracts` AS select `u`.`id` AS `id`,`u`.`client` AS `client`,`u`.`client_short` AS `client_short`,`u`.`clientDeath` AS `clientDeath`,`u`.`clientbirth` AS `clientbirth`,`u`.`ESRN` AS `ESRN`,`u`.`note` AS `note`,`u`.`phone` AS `phone`,`u`.`snils` AS `snils`,`u`.`curator` AS `curator`,`u`.`create` AS `create`,`u`.`ts` AS `ts`,`u`.`cr_by` AS `cr_by`,`u`.`upd_by` AS `upd_by`,`u`.`cr_dep_id` AS `cr_dep_id` from (`client` `u` join `contracts` `c` on((`c`.`client_id` = `u`.`id`))) where `c`.`dep_id` in (select `_active_dep`.`id` from `_active_dep`) */;
/*!50001 SET character_set_client      = @saved_cs_client */;
/*!50001 SET character_set_results     = @saved_cs_results */;
/*!50001 SET collation_connection      = @saved_col_connection */;

--
-- Final view structure for view `_dep_has_client_count_2month`
--

/*!50001 DROP VIEW IF EXISTS `_dep_has_client_count_2month`*/;
/*!50001 SET @saved_cs_client          = @@character_set_client */;
/*!50001 SET @saved_cs_results         = @@character_set_results */;
/*!50001 SET @saved_col_connection     = @@collation_connection */;
/*!50001 SET character_set_client      = utf8mb4 */;
/*!50001 SET character_set_results     = utf8mb4 */;
/*!50001 SET collation_connection      = utf8mb4_0900_ai_ci */;
/*!50001 CREATE ALGORITHM=UNDEFINED */
/*!50013 DEFINER=`root`@`localhost` SQL SECURITY DEFINER */
/*!50001 VIEW `_dep_has_client_count_2month` AS select sum(`m`.`quantity`) AS `quantity`,`u`.`id` AS `id`,`u`.`client` AS `client`,`u`.`client_short` AS `client_short`,`u`.`clientDeath` AS `clientDeath`,`u`.`clientbirth` AS `clientbirth`,`u`.`ESRN` AS `ESRN`,`u`.`note` AS `note`,`u`.`phone` AS `phone`,`u`.`snils` AS `snils`,`u`.`curator` AS `curator`,`u`.`create` AS `create`,`u`.`ts` AS `ts`,`u`.`cr_by` AS `cr_by`,`u`.`upd_by` AS `upd_by`,`u`.`cr_dep_id` AS `cr_dep_id` from (`client` `u` join `dep_has_main` `m` on((`m`.`client_id` = `u`.`id`))) where (year(`m`.`vdate`) in (select `GET_YEAR`(`GET_WID`())) and (month(`m`.`vdate`) in (month(curdate()),(month(curdate()) - 1)))) group by `u`.`id` */;
/*!50001 SET character_set_client      = @saved_cs_client */;
/*!50001 SET character_set_results     = @saved_cs_results */;
/*!50001 SET collation_connection      = @saved_col_connection */;

--
-- Final view structure for view `_dep_has_client_count_main_year`
--

/*!50001 DROP VIEW IF EXISTS `_dep_has_client_count_main_year`*/;
/*!50001 SET @saved_cs_client          = @@character_set_client */;
/*!50001 SET @saved_cs_results         = @@character_set_results */;
/*!50001 SET @saved_col_connection     = @@collation_connection */;
/*!50001 SET character_set_client      = utf8mb4 */;
/*!50001 SET character_set_results     = utf8mb4 */;
/*!50001 SET collation_connection      = utf8mb4_0900_ai_ci */;
/*!50001 CREATE ALGORITHM=UNDEFINED */
/*!50013 DEFINER=`root`@`localhost` SQL SECURITY DEFINER */
/*!50001 VIEW `_dep_has_client_count_main_year` AS select sum(`m`.`quantity`) AS `quantity`,`u`.`id` AS `id`,`u`.`client` AS `client`,`u`.`client_short` AS `client_short`,`u`.`clientDeath` AS `clientDeath`,`u`.`clientbirth` AS `clientbirth`,`u`.`ESRN` AS `ESRN`,`u`.`note` AS `note`,`u`.`phone` AS `phone`,`u`.`snils` AS `snils`,`u`.`curator` AS `curator`,`u`.`create` AS `create`,`u`.`ts` AS `ts`,`u`.`cr_by` AS `cr_by`,`u`.`upd_by` AS `upd_by`,`u`.`cr_dep_id` AS `cr_dep_id` from (`client` `u` join `dep_has_main` `m` on((`m`.`client_id` = `u`.`id`))) where year(`m`.`vdate`) in (select `GET_YEAR`(`GET_WID`())) group by `u`.`id` */;
/*!50001 SET character_set_client      = @saved_cs_client */;
/*!50001 SET character_set_results     = @saved_cs_results */;
/*!50001 SET collation_connection      = @saved_col_connection */;

--
-- Final view structure for view `_dep_has_client_count_month`
--

/*!50001 DROP VIEW IF EXISTS `_dep_has_client_count_month`*/;
/*!50001 SET @saved_cs_client          = @@character_set_client */;
/*!50001 SET @saved_cs_results         = @@character_set_results */;
/*!50001 SET @saved_col_connection     = @@collation_connection */;
/*!50001 SET character_set_client      = utf8mb4 */;
/*!50001 SET character_set_results     = utf8mb4 */;
/*!50001 SET collation_connection      = utf8mb4_0900_ai_ci */;
/*!50001 CREATE ALGORITHM=UNDEFINED */
/*!50013 DEFINER=`root`@`localhost` SQL SECURITY DEFINER */
/*!50001 VIEW `_dep_has_client_count_month` AS select sum(`m`.`quantity`) AS `quantity`,`u`.`id` AS `id`,`u`.`client` AS `client`,`u`.`client_short` AS `client_short`,`u`.`clientDeath` AS `clientDeath`,`u`.`clientbirth` AS `clientbirth`,`u`.`ESRN` AS `ESRN`,`u`.`note` AS `note`,`u`.`phone` AS `phone`,`u`.`snils` AS `snils`,`u`.`curator` AS `curator`,`u`.`create` AS `create`,`u`.`ts` AS `ts`,`u`.`cr_by` AS `cr_by`,`u`.`upd_by` AS `upd_by`,`u`.`cr_dep_id` AS `cr_dep_id` from (`client` `u` join `dep_has_main` `m` on((`m`.`client_id` = `u`.`id`))) where (year(`m`.`vdate`) in (select `GET_YEAR`(`GET_WID`())) and (month(`m`.`vdate`) = month(curdate()))) group by `u`.`id` */;
/*!50001 SET character_set_client      = @saved_cs_client */;
/*!50001 SET character_set_results     = @saved_cs_results */;
/*!50001 SET collation_connection      = @saved_col_connection */;

--
-- Final view structure for view `_dep_has_client_ended`
--

/*!50001 DROP VIEW IF EXISTS `_dep_has_client_ended`*/;
/*!50001 SET @saved_cs_client          = @@character_set_client */;
/*!50001 SET @saved_cs_results         = @@character_set_results */;
/*!50001 SET @saved_col_connection     = @@collation_connection */;
/*!50001 SET character_set_client      = utf8mb4 */;
/*!50001 SET character_set_results     = utf8mb4 */;
/*!50001 SET collation_connection      = utf8mb4_0900_ai_ci */;
/*!50001 CREATE ALGORITHM=UNDEFINED */
/*!50013 DEFINER=`root`@`localhost` SQL SECURITY DEFINER */
/*!50001 VIEW `_dep_has_client_ended` AS select `u`.`client` AS `client`,`c`.`id` AS `id`,`c`.`contracts` AS `contracts`,`c`.`client_id` AS `client_id`,`c`.`dep_id` AS `dep_id`,`c`.`ripso_id` AS `ripso_id`,`c`.`blocked` AS `blocked`,`c`.`startdate` AS `startdate`,`c`.`enddate` AS `enddate`,`c`.`ippsuNum` AS `ippsuNum`,`c`.`note` AS `note`,`c`.`create` AS `create`,`c`.`ts` AS `ts`,`c`.`cr_by` AS `cr_by`,`c`.`upd_by` AS `upd_by`,`c`.`to_recheck` AS `to_recheck`,`c`.`check_date` AS `check_date` from (`client` `u` join `contracts` `c` on((`c`.`client_id` = `u`.`id`))) where ((`c`.`enddate` < curdate()) and `c`.`dep_id` in (select `_active_dep`.`id` from `_active_dep`)) */;
/*!50001 SET character_set_client      = @saved_cs_client */;
/*!50001 SET character_set_results     = @saved_cs_results */;
/*!50001 SET collation_connection      = @saved_col_connection */;

--
-- Final view structure for view `_dep_has_client_ending`
--

/*!50001 DROP VIEW IF EXISTS `_dep_has_client_ending`*/;
/*!50001 SET @saved_cs_client          = @@character_set_client */;
/*!50001 SET @saved_cs_results         = @@character_set_results */;
/*!50001 SET @saved_col_connection     = @@collation_connection */;
/*!50001 SET character_set_client      = utf8mb4 */;
/*!50001 SET character_set_results     = utf8mb4 */;
/*!50001 SET collation_connection      = utf8mb4_0900_ai_ci */;
/*!50001 CREATE ALGORITHM=UNDEFINED */
/*!50013 DEFINER=`root`@`localhost` SQL SECURITY DEFINER */
/*!50001 VIEW `_dep_has_client_ending` AS select `u`.`client` AS `client`,`c`.`id` AS `id`,`c`.`contracts` AS `contracts`,`c`.`client_id` AS `client_id`,`c`.`dep_id` AS `dep_id`,`c`.`ripso_id` AS `ripso_id`,`c`.`blocked` AS `blocked`,`c`.`startdate` AS `startdate`,`c`.`enddate` AS `enddate`,`c`.`ippsuNum` AS `ippsuNum`,`c`.`note` AS `note`,`c`.`create` AS `create`,`c`.`ts` AS `ts`,`c`.`cr_by` AS `cr_by`,`c`.`upd_by` AS `upd_by`,`c`.`to_recheck` AS `to_recheck`,`c`.`check_date` AS `check_date` from (`client` `u` join `contracts` `c` on((`c`.`client_id` = `u`.`id`))) where (`c`.`enddate` between (curdate() - 30) and (curdate() + 30)) */;
/*!50001 SET character_set_client      = @saved_cs_client */;
/*!50001 SET character_set_results     = @saved_cs_results */;
/*!50001 SET collation_connection      = @saved_col_connection */;

--
-- Final view structure for view `_dep_has_client_more`
--

/*!50001 DROP VIEW IF EXISTS `_dep_has_client_more`*/;
/*!50001 SET @saved_cs_client          = @@character_set_client */;
/*!50001 SET @saved_cs_results         = @@character_set_results */;
/*!50001 SET @saved_col_connection     = @@collation_connection */;
/*!50001 SET character_set_client      = utf8mb4 */;
/*!50001 SET character_set_results     = utf8mb4 */;
/*!50001 SET collation_connection      = utf8mb4_0900_ai_ci */;
/*!50001 CREATE ALGORITHM=UNDEFINED */
/*!50013 DEFINER=`root`@`localhost` SQL SECURITY DEFINER */
/*!50001 VIEW `_dep_has_client_more` AS select `du`.`id` AS `id`,`du`.`client` AS `client`,`du`.`client_short` AS `client_short`,`du`.`clientDeath` AS `clientDeath`,`du`.`clientbirth` AS `clientbirth`,`du`.`ESRN` AS `ESRN`,`du`.`note` AS `prim_fio`,`du`.`phone` AS `phone`,`du`.`snils` AS `snils`,`du`.`curator` AS `curator_fio`,`du`.`create` AS `create_fio`,`du`.`ts` AS `ts_fio`,`du`.`cr_by` AS `cr_by_fio`,`du`.`upd_by` AS `upd_by_fio`,`au`.`client_id` AS `client_id`,`au`.`pddate` AS `pddate`,`au`.`contracts_id` AS `contracts_id`,`au`.`predv_money` AS `predv_money`,`au`.`curFIO` AS `curFIO`,`au`.`psp` AS `psp`,`au`.`address` AS `address`,`au`.`sdd` AS `sdd`,`au`.`sdd_date` AS `sdd_date`,`au`.`perc` AS `perc`,`au`.`not_standart_contract` AS `not_standart_contract`,`au`.`not_standart_act` AS `not_standart_act`,`au`.`note` AS `note`,`au`.`create` AS `create`,`au`.`ts` AS `ts`,`au`.`cr_by` AS `cr_by`,`au`.`upd_by` AS `upd_by`,`au`.`repr_FIO` AS `repr_FIO`,`au`.`repr_addr` AS `repr_addr`,`au`.`repr_psp` AS `repr_psp`,`au`.`work_livemin` AS `work_livemin` from ((select `t2`.`client_id` AS `client_id`,`t2`.`pddate` AS `pddate`,`t2`.`contracts_id` AS `contracts_id`,`t2`.`predv_money` AS `predv_money`,`t2`.`curFIO` AS `curFIO`,`t2`.`psp` AS `psp`,`t2`.`address` AS `address`,`t2`.`sdd` AS `sdd`,`t2`.`sdd_date` AS `sdd_date`,`t2`.`perc` AS `perc`,`t2`.`not_standart_contract` AS `not_standart_contract`,`t2`.`not_standart_act` AS `not_standart_act`,`t2`.`note` AS `note`,`t2`.`create` AS `create`,`t2`.`ts` AS `ts`,`t2`.`cr_by` AS `cr_by`,`t2`.`upd_by` AS `upd_by`,`t2`.`repr_FIO` AS `repr_FIO`,`t2`.`repr_addr` AS `repr_addr`,`t2`.`repr_psp` AS `repr_psp`,`t2`.`work_livemin` AS `work_livemin` from (select `au1`.`client_id` AS `client_id`,`au1`.`pddate` AS `pddate`,`au1`.`contracts_id` AS `contracts_id`,`au1`.`predv_money` AS `predv_money`,`au1`.`curFIO` AS `curFIO`,`au1`.`psp` AS `psp`,`au1`.`address` AS `address`,`au1`.`sdd` AS `sdd`,`au1`.`sdd_date` AS `sdd_date`,`au1`.`perc` AS `perc`,`au1`.`not_standart_contract` AS `not_standart_contract`,`au1`.`not_standart_act` AS `not_standart_act`,`au1`.`note` AS `note`,`au1`.`create` AS `create`,`au1`.`ts` AS `ts`,`au1`.`cr_by` AS `cr_by`,`au1`.`upd_by` AS `upd_by`,`au1`.`repr_FIO` AS `repr_FIO`,`au1`.`repr_addr` AS `repr_addr`,`au1`.`repr_psp` AS `repr_psp`,`au1`.`work_livemin` AS `work_livemin` from `add_info_for_client` `au1` order by `au1`.`pddate` desc) `t2` group by `t2`.`client_id`) `au` join `_dep_has_client` `du` on((`du`.`id` = `au`.`client_id`))) order by `au`.`pddate` desc */;
/*!50001 SET character_set_client      = @saved_cs_client */;
/*!50001 SET character_set_results     = @saved_cs_results */;
/*!50001 SET collation_connection      = @saved_col_connection */;

--
-- Final view structure for view `_dep_has_client_ripso`
--

/*!50001 DROP VIEW IF EXISTS `_dep_has_client_ripso`*/;
/*!50001 SET @saved_cs_client          = @@character_set_client */;
/*!50001 SET @saved_cs_results         = @@character_set_results */;
/*!50001 SET @saved_col_connection     = @@collation_connection */;
/*!50001 SET character_set_client      = utf8mb4 */;
/*!50001 SET character_set_results     = utf8mb4 */;
/*!50001 SET collation_connection      = utf8mb4_0900_ai_ci */;
/*!50001 CREATE ALGORITHM=UNDEFINED */
/*!50013 DEFINER=`root`@`localhost` SQL SECURITY DEFINER */
/*!50001 VIEW `_dep_has_client_ripso` AS select `client`.`id` AS `id`,`client`.`client` AS `client`,`client`.`client_short` AS `client_short`,`client`.`clientDeath` AS `clientDeath`,`client`.`clientbirth` AS `clientbirth`,`client`.`ESRN` AS `ESRN`,`client`.`note` AS `note`,`client`.`phone` AS `phone`,`client`.`snils` AS `snils`,`client`.`curator` AS `curator`,`client`.`create` AS `create`,`client`.`ts` AS `ts`,`client`.`cr_by` AS `cr_by`,`client`.`upd_by` AS `upd_by`,`client`.`cr_dep_id` AS `cr_dep_id` from `client` where `client`.`id` in (select `c`.`client_id` from (`contracts` `c` join `dep_has_ripso` `rod` on((`rod`.`ripso_id` = `c`.`ripso_id`))) where `rod`.`dep_id` in (select `_active_dep`.`id` from `_active_dep`)) */;
/*!50001 SET character_set_client      = @saved_cs_client */;
/*!50001 SET character_set_results     = @saved_cs_results */;
/*!50001 SET collation_connection      = @saved_col_connection */;

--
-- Final view structure for view `_dep_has_client_ripso_or_contracts`
--

/*!50001 DROP VIEW IF EXISTS `_dep_has_client_ripso_or_contracts`*/;
/*!50001 SET @saved_cs_client          = @@character_set_client */;
/*!50001 SET @saved_cs_results         = @@character_set_results */;
/*!50001 SET @saved_col_connection     = @@collation_connection */;
/*!50001 SET character_set_client      = utf8mb4 */;
/*!50001 SET character_set_results     = utf8mb4 */;
/*!50001 SET collation_connection      = utf8mb4_0900_ai_ci */;
/*!50001 CREATE ALGORITHM=UNDEFINED */
/*!50013 DEFINER=`root`@`localhost` SQL SECURITY DEFINER */
/*!50001 VIEW `_dep_has_client_ripso_or_contracts` AS select `client`.`id` AS `id`,`client`.`client` AS `client`,`client`.`client_short` AS `client_short`,`client`.`clientDeath` AS `clientDeath`,`client`.`clientbirth` AS `clientbirth`,`client`.`ESRN` AS `ESRN`,`client`.`note` AS `note`,`client`.`phone` AS `phone`,`client`.`snils` AS `snils`,`client`.`curator` AS `curator`,`client`.`create` AS `create`,`client`.`ts` AS `ts`,`client`.`cr_by` AS `cr_by`,`client`.`upd_by` AS `upd_by`,`client`.`cr_dep_id` AS `cr_dep_id` from `client` where `client`.`id` in (select `c`.`client_id` from (`contracts` `c` join `dep_has_ripso` `rod` on((`rod`.`ripso_id` = `c`.`ripso_id`))) where (`rod`.`dep_id` in (select `_active_dep`.`id` from `_active_dep`) or `c`.`dep_id` in (select `_active_dep`.`id` from `_active_dep`))) */;
/*!50001 SET character_set_client      = @saved_cs_client */;
/*!50001 SET character_set_results     = @saved_cs_results */;
/*!50001 SET collation_connection      = @saved_col_connection */;

--
-- Final view structure for view `_dep_has_client_year`
--

/*!50001 DROP VIEW IF EXISTS `_dep_has_client_year`*/;
/*!50001 SET @saved_cs_client          = @@character_set_client */;
/*!50001 SET @saved_cs_results         = @@character_set_results */;
/*!50001 SET @saved_col_connection     = @@collation_connection */;
/*!50001 SET character_set_client      = utf8mb4 */;
/*!50001 SET character_set_results     = utf8mb4 */;
/*!50001 SET collation_connection      = utf8mb4_0900_ai_ci */;
/*!50001 CREATE ALGORITHM=UNDEFINED */
/*!50013 DEFINER=`root`@`localhost` SQL SECURITY DEFINER */
/*!50001 VIEW `_dep_has_client_year` AS select `client`.`id` AS `id`,`client`.`client` AS `client`,`client`.`client_short` AS `client_short`,`client`.`clientDeath` AS `clientDeath`,`client`.`clientbirth` AS `clientbirth`,`client`.`ESRN` AS `ESRN`,`client`.`note` AS `note`,`client`.`phone` AS `phone`,`client`.`snils` AS `snils`,`client`.`curator` AS `curator`,`client`.`create` AS `create`,`client`.`ts` AS `ts`,`client`.`cr_by` AS `cr_by`,`client`.`upd_by` AS `upd_by`,`client`.`cr_dep_id` AS `cr_dep_id` from `client` where `client`.`id` in (select `c`.`client_id` from (`contracts` `c` join `dep_has_ripso` `rod` on((`rod`.`ripso_id` = `c`.`ripso_id`))) where ((`rod`.`dep_id` in (select `_active_dep`.`id` from `_active_dep`) or `c`.`dep_id` in (select `_active_dep`.`id` from `_active_dep`)) and ((year(`c`.`startdate`) = `GET_YEAR`(`GET_wID`())) or (year(`c`.`startdate`) = `GET_YEAR`(`GET_wID`()))))) */;
/*!50001 SET character_set_client      = @saved_cs_client */;
/*!50001 SET character_set_results     = @saved_cs_results */;
/*!50001 SET collation_connection      = @saved_col_connection */;

--
-- Final view structure for view `_dep_has_contracts`
--

/*!50001 DROP VIEW IF EXISTS `_dep_has_contracts`*/;
/*!50001 SET @saved_cs_client          = @@character_set_client */;
/*!50001 SET @saved_cs_results         = @@character_set_results */;
/*!50001 SET @saved_col_connection     = @@collation_connection */;
/*!50001 SET character_set_client      = utf8mb4 */;
/*!50001 SET character_set_results     = utf8mb4 */;
/*!50001 SET collation_connection      = utf8mb4_0900_ai_ci */;
/*!50001 CREATE ALGORITHM=UNDEFINED */
/*!50013 DEFINER=`root`@`localhost` SQL SECURITY DEFINER */
/*!50001 VIEW `_dep_has_contracts` AS select `u`.`client` AS `client`,`c`.`id` AS `id`,`c`.`contracts` AS `contracts`,`c`.`contracts2` AS `contracts2`,`c`.`client_id` AS `client_id`,`c`.`dep_id` AS `dep_id`,`c`.`ripso_id` AS `ripso_id`,`c`.`blocked` AS `blocked`,`c`.`startdate` AS `startdate`,`c`.`enddate` AS `enddate`,`c`.`ippsuNum` AS `ippsuNum`,`c`.`note` AS `note`,`c`.`create` AS `create`,`c`.`ts` AS `ts`,`c`.`cr_by` AS `cr_by`,`c`.`upd_by` AS `upd_by`,`c`.`to_recheck` AS `to_recheck`,`c`.`check_date` AS `check_date`,`c`.`pyc_prim` AS `pyc_prim` from (`client` `u` join `contracts` `c` on((`c`.`client_id` = `u`.`id`))) where `c`.`dep_id` in (select `_active_dep`.`id` from `_active_dep`) */;
/*!50001 SET character_set_client      = @saved_cs_client */;
/*!50001 SET character_set_results     = @saved_cs_results */;
/*!50001 SET collation_connection      = @saved_col_connection */;

--
-- Final view structure for view `_dep_has_main`
--

/*!50001 DROP VIEW IF EXISTS `_dep_has_main`*/;
/*!50001 SET @saved_cs_client          = @@character_set_client */;
/*!50001 SET @saved_cs_results         = @@character_set_results */;
/*!50001 SET @saved_col_connection     = @@collation_connection */;
/*!50001 SET character_set_client      = utf8mb4 */;
/*!50001 SET character_set_results     = utf8mb4 */;
/*!50001 SET collation_connection      = utf8mb4_0900_ai_ci */;
/*!50001 CREATE ALGORITHM=UNDEFINED */
/*!50013 DEFINER=`root`@`localhost` SQL SECURITY DEFINER */
/*!50001 VIEW `_dep_has_main` AS select `main`.`id` AS `id`,`main`.`contracts_id` AS `contracts_id`,`main`.`dep_id` AS `dep_id`,`main`.`client_id` AS `client_id`,`main`.`serv_id` AS `serv_id`,`main`.`dep_has_worker_id` AS `dep_has_worker_id`,`main`.`worker_id` AS `worker_id`,`main`.`vdate` AS `vdate`,`main`.`quantity` AS `quantity`,`main`.`note` AS `note`,`main`.`create` AS `create`,`main`.`ts` AS `ts`,`main`.`cr_by` AS `cr_by`,`main`.`upd_by` AS `upd_by`,`main`.`reported` AS `reported`,`main`.`wdate` AS `wdate`,`main`.`overdid` AS `overdid`,`main`.`prev_quantity` AS `prev_quantity` from `main` where `main`.`dep_id` in (select `_active_dep`.`id` from `_active_dep`) */;
/*!50001 SET character_set_client      = @saved_cs_client */;
/*!50001 SET character_set_results     = @saved_cs_results */;
/*!50001 SET collation_connection      = @saved_col_connection */;

--
-- Final view structure for view `_dep_has_new_client`
--

/*!50001 DROP VIEW IF EXISTS `_dep_has_new_client`*/;
/*!50001 SET @saved_cs_client          = @@character_set_client */;
/*!50001 SET @saved_cs_results         = @@character_set_results */;
/*!50001 SET @saved_col_connection     = @@collation_connection */;
/*!50001 SET character_set_client      = utf8mb4 */;
/*!50001 SET character_set_results     = utf8mb4 */;
/*!50001 SET collation_connection      = utf8mb4_0900_ai_ci */;
/*!50001 CREATE ALGORITHM=UNDEFINED */
/*!50013 DEFINER=`root`@`localhost` SQL SECURITY DEFINER */
/*!50001 VIEW `_dep_has_new_client` AS select `u`.`id` AS `id`,`u`.`client` AS `client`,`u`.`client_short` AS `client_short`,`u`.`clientDeath` AS `clientDeath`,`u`.`clientbirth` AS `clientbirth`,`u`.`ESRN` AS `ESRN`,`u`.`note` AS `note`,`u`.`phone` AS `phone`,`u`.`snils` AS `snils`,`u`.`curator` AS `curator`,`u`.`create` AS `create`,`u`.`ts` AS `ts`,`u`.`cr_by` AS `cr_by`,`u`.`upd_by` AS `upd_by`,`u`.`cr_dep_id` AS `cr_dep_id` from `client` `u` where `u`.`id` in (select `u1`.`id` from (`client` `u1` left join `contracts` `c` on((`c`.`client_id` = `u1`.`id`))) where `u1`.`cr_dep_id` in (select `_active_dep`.`id` from `_active_dep`)) */;
/*!50001 SET character_set_client      = @saved_cs_client */;
/*!50001 SET character_set_results     = @saved_cs_results */;
/*!50001 SET collation_connection      = @saved_col_connection */;

--
-- Final view structure for view `_dep_has_ripso`
--

/*!50001 DROP VIEW IF EXISTS `_dep_has_ripso`*/;
/*!50001 SET @saved_cs_client          = @@character_set_client */;
/*!50001 SET @saved_cs_results         = @@character_set_results */;
/*!50001 SET @saved_col_connection     = @@collation_connection */;
/*!50001 SET character_set_client      = utf8mb4 */;
/*!50001 SET character_set_results     = utf8mb4 */;
/*!50001 SET collation_connection      = utf8mb4_0900_ai_ci */;
/*!50001 CREATE ALGORITHM=UNDEFINED */
/*!50013 DEFINER=`root`@`localhost` SQL SECURITY DEFINER */
/*!50001 VIEW `_dep_has_ripso` AS select `dhr`.`ripso_id` AS `ripso_id`,`r`.`ripso` AS `ripso` from (`dep_has_ripso` `dhr` join `ripso` `r` on((`dhr`.`ripso_id` = `r`.`id`))) where `dhr`.`dep_id` in (select `_active_dep`.`id` from `_active_dep`) */;
/*!50001 SET character_set_client      = @saved_cs_client */;
/*!50001 SET character_set_results     = @saved_cs_results */;
/*!50001 SET collation_connection      = @saved_col_connection */;

--
-- Final view structure for view `_dep_has_worker`
--

/*!50001 DROP VIEW IF EXISTS `_dep_has_worker`*/;
/*!50001 SET @saved_cs_client          = @@character_set_client */;
/*!50001 SET @saved_cs_results         = @@character_set_results */;
/*!50001 SET @saved_col_connection     = @@collation_connection */;
/*!50001 SET character_set_client      = utf8mb4 */;
/*!50001 SET character_set_results     = utf8mb4 */;
/*!50001 SET collation_connection      = utf8mb4_0900_ai_ci */;
/*!50001 CREATE ALGORITHM=UNDEFINED */
/*!50013 DEFINER=`root`@`localhost` SQL SECURITY DEFINER */
/*!50001 VIEW `_dep_has_worker` AS select `dhr`.`id` AS `id`,`dhr`.`dep_has_worker` AS `dep_has_worker`,`dhr`.`worker_id` AS `worker_id`,`dhr`.`dep_id` AS `dep_id`,`dhr`.`job_id` AS `job_id`,`dhr`.`note` AS `note`,`dhr`.`archive` AS `archive`,`dhr`.`from` AS `from`,`dhr`.`till` AS `till`,`dhr`.`role_id` AS `role_id`,`dhr`.`api_key` AS `api_key` from `dep_has_worker` `dhr` where `dhr`.`dep_id` in (select `_active_dep`.`id` from `_active_dep`) */;
/*!50001 SET character_set_client      = @saved_cs_client */;
/*!50001 SET character_set_results     = @saved_cs_results */;
/*!50001 SET collation_connection      = @saved_col_connection */;

--
-- Final view structure for view `_dep_has_workers`
--

/*!50001 DROP VIEW IF EXISTS `_dep_has_workers`*/;
/*!50001 SET @saved_cs_client          = @@character_set_client */;
/*!50001 SET @saved_cs_results         = @@character_set_results */;
/*!50001 SET @saved_col_connection     = @@collation_connection */;
/*!50001 SET character_set_client      = utf8mb4 */;
/*!50001 SET character_set_results     = utf8mb4 */;
/*!50001 SET collation_connection      = utf8mb4_0900_ai_ci */;
/*!50001 CREATE ALGORITHM=UNDEFINED */
/*!50013 DEFINER=`root`@`localhost` SQL SECURITY DEFINER */
/*!50001 VIEW `_dep_has_workers` AS select `dhr`.`id` AS `id`,`dhr`.`worker` AS `worker`,`dhr`.`user` AS `user`,`dhr`.`note` AS `note`,`dhr`.`role_id` AS `role_id`,`dhr`.`dep_id` AS `dep_id`,`dhr`.`archive` AS `archive` from `worker` `dhr` where `dhr`.`dep_id` in (select `_active_dep`.`id` from `_active_dep`) */;
/*!50001 SET character_set_client      = @saved_cs_client */;
/*!50001 SET character_set_results     = @saved_cs_results */;
/*!50001 SET collation_connection      = @saved_col_connection */;

--
-- Final view structure for view `_dhw_has_client`
--

/*!50001 DROP VIEW IF EXISTS `_dhw_has_client`*/;
/*!50001 SET @saved_cs_client          = @@character_set_client */;
/*!50001 SET @saved_cs_results         = @@character_set_results */;
/*!50001 SET @saved_col_connection     = @@collation_connection */;
/*!50001 SET character_set_client      = utf8mb4 */;
/*!50001 SET character_set_results     = utf8mb4 */;
/*!50001 SET collation_connection      = utf8mb4_0900_ai_ci */;
/*!50001 CREATE ALGORITHM=UNDEFINED */
/*!50013 DEFINER=`root`@`localhost` SQL SECURITY DEFINER */
/*!50001 VIEW `_dhw_has_client` AS select `dhwu`.`dhw_id` AS `dhw_id`,`dhwu`.`client_id` AS `client_id`,`dhwu`.`note` AS `note` from `dhw_has_client` `dhwu` where `dhwu`.`dhw_id` in (select `_dep_has_worker`.`id` from `_dep_has_worker`) */;
/*!50001 SET character_set_client      = @saved_cs_client */;
/*!50001 SET character_set_results     = @saved_cs_results */;
/*!50001 SET collation_connection      = @saved_col_connection */;

--
-- Final view structure for view `_g_categ_list_client_for_dep_for_year`
--

/*!50001 DROP VIEW IF EXISTS `_g_categ_list_client_for_dep_for_year`*/;
/*!50001 SET @saved_cs_client          = @@character_set_client */;
/*!50001 SET @saved_cs_results         = @@character_set_results */;
/*!50001 SET @saved_col_connection     = @@collation_connection */;
/*!50001 SET character_set_client      = utf8mb4 */;
/*!50001 SET character_set_results     = utf8mb4 */;
/*!50001 SET collation_connection      = utf8mb4_0900_ai_ci */;
/*!50001 CREATE ALGORITHM=UNDEFINED */
/*!50013 DEFINER=`root`@`localhost` SQL SECURITY DEFINER */
/*!50001 VIEW `_g_categ_list_client_for_dep_for_year` AS select `uhc`.`category_id` AS `category_id`,`m`.`client_id` AS `client_id`,sum(`m`.`quantity`) AS `SUM(quantity)` from (`main` `m` join `client_has_category` `uhc` on((`m`.`client_id` = `uhc`.`client_id`))) where (`m`.`dep_id` in (select `_active_dep`.`id` from `_active_dep`) and (coalesce(`uhc`.`archive`,0) = 0) and (coalesce(year(`uhc`.`create`),0) = `GET_YEAR`(`GET_WID`()))) group by `uhc`.`category_id`,`m`.`client_id` */;
/*!50001 SET character_set_client      = @saved_cs_client */;
/*!50001 SET character_set_results     = @saved_cs_results */;
/*!50001 SET collation_connection      = @saved_col_connection */;

--
-- Final view structure for view `_g_serv_list_for_dep_for_year`
--

/*!50001 DROP VIEW IF EXISTS `_g_serv_list_for_dep_for_year`*/;
/*!50001 SET @saved_cs_client          = @@character_set_client */;
/*!50001 SET @saved_cs_results         = @@character_set_results */;
/*!50001 SET @saved_col_connection     = @@collation_connection */;
/*!50001 SET character_set_client      = utf8mb4 */;
/*!50001 SET character_set_results     = utf8mb4 */;
/*!50001 SET collation_connection      = utf8mb4_0900_ai_ci */;
/*!50001 CREATE ALGORITHM=UNDEFINED */
/*!50013 DEFINER=`root`@`localhost` SQL SECURITY DEFINER */
/*!50001 VIEW `_g_serv_list_for_dep_for_year` AS select `t`.`category_id` AS `category_id`,count(`t`.`client_id`) AS `count(client_id)`,sum(`t`.`quantity`) AS `SUM(quantity)` from (select `uhc`.`category_id` AS `category_id`,`m`.`client_id` AS `client_id`,sum(`m`.`quantity`) AS `quantity` from (`main` `m` left join `client_has_category` `uhc` on((`m`.`client_id` = `uhc`.`client_id`))) where (`m`.`dep_id` in (select `_active_dep`.`id` from `_active_dep`) and (coalesce(`uhc`.`archive`,0) = 0) and (coalesce(year(`uhc`.`get_date`),0) <= `GET_YEAR`(`GET_WID`()))) group by `uhc`.`category_id`,`m`.`client_id`) `t` group by `t`.`category_id` */;
/*!50001 SET character_set_client      = @saved_cs_client */;
/*!50001 SET character_set_results     = @saved_cs_results */;
/*!50001 SET collation_connection      = @saved_col_connection */;

--
-- Final view structure for view `_g_serv_total_you`
--

/*!50001 DROP VIEW IF EXISTS `_g_serv_total_you`*/;
/*!50001 SET @saved_cs_client          = @@character_set_client */;
/*!50001 SET @saved_cs_results         = @@character_set_results */;
/*!50001 SET @saved_col_connection     = @@collation_connection */;
/*!50001 SET character_set_client      = utf8mb4 */;
/*!50001 SET character_set_results     = utf8mb4 */;
/*!50001 SET collation_connection      = utf8mb4_0900_ai_ci */;
/*!50001 CREATE ALGORITHM=UNDEFINED */
/*!50013 DEFINER=`root`@`localhost` SQL SECURITY DEFINER */
/*!50001 VIEW `_g_serv_total_you` AS select `m`.`serv_id` AS `serv_id`,sum(`m`.`quantity`) AS `quantity`,(select count(0) from (select `mfd`.`client_id` AS `client_id` from `_main_for_dep` `mfd` where (`mfd`.`serv_id` = `mfd`.`serv_id`) group by `mfd`.`client_id`) `t`) AS `client_id_count`,`m`.`client_id` AS `client_id`,count(`m`.`client_id`) AS `records` from `_main_for_dep` `m` group by `m`.`serv_id`,`m`.`client_id` order by `m`.`serv_id` */;
/*!50001 SET character_set_client      = @saved_cs_client */;
/*!50001 SET character_set_results     = @saved_cs_results */;
/*!50001 SET collation_connection      = @saved_col_connection */;

--
-- Final view structure for view `_information_schema_columns`
--

-- kcson.`_information_schema_columns` source

CREATE OR REPLACE
ALGORITHM = UNDEFINED VIEW `_information_schema_columns` AS
select
    `information_schema`.`COLUMNS`.`TABLE_NAME` AS `TABLE_NAME`,
    `information_schema`.`COLUMNS`.`ORDINAL_POSITION` AS `ORDINAL_POSITION`,
    `information_schema`.`COLUMNS`.`COLUMN_NAME` AS `COLUMN_NAME`,
    `information_schema`.`COLUMNS`.`IS_NULLABLE` AS `IS_NULLABLE`,
    `information_schema`.`COLUMNS`.`COLUMN_DEFAULT` AS `COLUMN_DEFAULT`,
    `information_schema`.`COLUMNS`.`DATA_TYPE` AS `DATA_TYPE`,
    `information_schema`.`COLUMNS`.`NUMERIC_PRECISION` AS `NUMERIC_PRECISION`,
    `information_schema`.`COLUMNS`.`COLUMN_TYPE` AS `COLUMN_TYPE`,
    `information_schema`.`COLUMNS`.`CHARACTER_MAXIMUM_LENGTH` AS `CHARACTER_MAXIMUM_LENGTH`
from
    `information_schema`.`COLUMNS`
where
    `information_schema`.`COLUMNS`.`TABLE_SCHEMA` = 'kcson'
order by
    `information_schema`.`COLUMNS`.`TABLE_NAME`,
    `information_schema`.`COLUMNS`.`ORDINAL_POSITION`; 


--
-- Final view structure for view `_main__months`
--

/*!50001 DROP VIEW IF EXISTS `_main__months`*/;
/*!50001 SET @saved_cs_client          = @@character_set_client */;
/*!50001 SET @saved_cs_results         = @@character_set_results */;
/*!50001 SET @saved_col_connection     = @@collation_connection */;
/*!50001 SET character_set_client      = utf8mb4 */;
/*!50001 SET character_set_results     = utf8mb4 */;
/*!50001 SET collation_connection      = utf8mb4_0900_ai_ci */;
/*!50001 CREATE ALGORITHM=UNDEFINED */
/*!50013 DEFINER=`root`@`localhost` SQL SECURITY DEFINER */
/*!50001 VIEW `_main__months` AS with `m1` as (select `main`.`client_id` AS `client_id`,`main`.`dep_id` AS `dep_id`,`main`.`contracts_id` AS `contracts_id`,`main`.`serv_id` AS `serv_id`,month(`main`.`vdate`) AS `month1`,year(`main`.`vdate`) AS `year1`,`main`.`dep_has_worker_id` AS `dep_has_worker_id`,`main`.`quantity` AS `quantity` from `main`) select `m1`.`serv_id` AS `serv_id`,`m1`.`dep_id` AS `dep_id`,`m1`.`contracts_id` AS `contracts_id`,`m1`.`year1` AS `year1`,`m1`.`dep_has_worker_id` AS `dep_has_worker_id`,sum((case when (`m1`.`month1` = 1) then `m1`.`quantity` else 0 end)) AS `month1`,sum((case when (`m1`.`month1` = 2) then `m1`.`quantity` else 0 end)) AS `month2`,sum((case when (`m1`.`month1` = 3) then `m1`.`quantity` else 0 end)) AS `month3`,sum((case when (`m1`.`month1` = 4) then `m1`.`quantity` else 0 end)) AS `month4`,sum((case when (`m1`.`month1` = 5) then `m1`.`quantity` else 0 end)) AS `month5`,sum((case when (`m1`.`month1` = 6) then `m1`.`quantity` else 0 end)) AS `month6`,sum((case when (`m1`.`month1` = 7) then `m1`.`quantity` else 0 end)) AS `month7`,sum((case when (`m1`.`month1` = 8) then `m1`.`quantity` else 0 end)) AS `month8`,sum((case when (`m1`.`month1` = 9) then `m1`.`quantity` else 0 end)) AS `month9`,sum((case when (`m1`.`month1` = 10) then `m1`.`quantity` else 0 end)) AS `month10`,sum((case when (`m1`.`month1` = 11) then `m1`.`quantity` else 0 end)) AS `month11`,sum((case when (`m1`.`month1` = 12) then `m1`.`quantity` else 0 end)) AS `month12` from `m1` group by `m1`.`dep_id`,`m1`.`contracts_id`,`m1`.`serv_id`,`m1`.`dep_has_worker_id` */;
/*!50001 SET character_set_client      = @saved_cs_client */;
/*!50001 SET character_set_results     = @saved_cs_results */;
/*!50001 SET collation_connection      = @saved_col_connection */;

--
-- Final view structure for view `_main_cprice`
--

/*!50001 DROP VIEW IF EXISTS `_main_cprice`*/;
/*!50001 SET @saved_cs_client          = @@character_set_client */;
/*!50001 SET @saved_cs_results         = @@character_set_results */;
/*!50001 SET @saved_col_connection     = @@collation_connection */;
/*!50001 SET character_set_client      = utf8mb4 */;
/*!50001 SET character_set_results     = utf8mb4 */;
/*!50001 SET collation_connection      = utf8mb4_0900_ai_ci */;
/*!50001 CREATE ALGORITHM=UNDEFINED */
/*!50013 DEFINER=`root`@`localhost` SQL SECURITY DEFINER */
/*!50001 VIEW `_main_cprice` AS select `f`.`id` AS `id`,`f`.`contracts_id` AS `contracts_id`,`f`.`dep_id` AS `dep_id`,`f`.`client_id` AS `client_id`,`f`.`serv_id` AS `serv_id`,`f`.`dep_has_worker_id` AS `dep_has_worker_id`,`f`.`worker_id` AS `worker_id`,`f`.`vdate` AS `vdate`,`f`.`quantity` AS `quantity`,`f`.`note` AS `note`,`f`.`create` AS `create`,`f`.`ts` AS `ts`,`f`.`cr_by` AS `cr_by`,`f`.`upd_by` AS `upd_by`,`f`.`reported` AS `reported`,`f`.`wdate` AS `wdate`,`f`.`overdid` AS `overdid`,`f`.`prev_quantity` AS `prev_quantity`,`f`.`perc` AS `perc`,`f`.`price` AS `price`,`f`.`price2` AS `price2`,`f`.`price3` AS `price3`,`f`.`servform_id` AS `servform_id`,`f`.`tnum` AS `tnum`,`f`.`serv` AS `serv`,`f`.`serv_text` AS `serv_text`,`f`.`sub_serv` AS `sub_serv`,((`f`.`perc` * `f`.`quantity`) * `f`.`price`) AS `to_pay`,((`f`.`perc` * `f`.`quantity`) * `f`.`price2`) AS `to_pay2` from (select `m`.`id` AS `id`,`m`.`contracts_id` AS `contracts_id`,`m`.`dep_id` AS `dep_id`,`m`.`client_id` AS `client_id`,`m`.`serv_id` AS `serv_id`,`m`.`dep_has_worker_id` AS `dep_has_worker_id`,`m`.`worker_id` AS `worker_id`,`m`.`vdate` AS `vdate`,`m`.`quantity` AS `quantity`,`m`.`note` AS `note`,`m`.`create` AS `create`,`m`.`ts` AS `ts`,`m`.`cr_by` AS `cr_by`,`m`.`upd_by` AS `upd_by`,`m`.`reported` AS `reported`,`m`.`wdate` AS `wdate`,`m`.`overdid` AS `overdid`,`m`.`prev_quantity` AS `prev_quantity`,(select `pd`.`perc` from `add_info` `pd` where ((`pd`.`pddate` <= `m`.`vdate`) and (`pd`.`contracts_id` = `m`.`contracts_id`)) order by `pd`.`pddate` desc limit 1) AS `perc`,`s`.`price` AS `price`,`s`.`price2` AS `price2`,`s`.`price3` AS `price3`,`r`.`servform_id` AS `servform_id`,`s`.`tnum` AS `tnum`,`s`.`serv` AS `serv`,`s`.`serv_text` AS `serv_text`,`s`.`sub_serv` AS `sub_serv` from (((`main` `m` join `serv` `s` on((`m`.`serv_id` = `s`.`id`))) join `contracts` `c` on((`m`.`contracts_id` = `c`.`id`))) left join `ripso` `r` on((`c`.`ripso_id` = `r`.`id`)))) `f` */;
/*!50001 SET character_set_client      = @saved_cs_client */;
/*!50001 SET character_set_results     = @saved_cs_results */;
/*!50001 SET collation_connection      = @saved_col_connection */;

--
-- Final view structure for view `_main_cprice_for_contracts`
--

/*!50001 DROP VIEW IF EXISTS `_main_cprice_for_contracts`*/;
/*!50001 SET @saved_cs_client          = @@character_set_client */;
/*!50001 SET @saved_cs_results         = @@character_set_results */;
/*!50001 SET @saved_col_connection     = @@collation_connection */;
/*!50001 SET character_set_client      = utf8mb4 */;
/*!50001 SET character_set_results     = utf8mb4 */;
/*!50001 SET collation_connection      = utf8mb4_0900_ai_ci */;
/*!50001 CREATE ALGORITHM=UNDEFINED */
/*!50013 DEFINER=`root`@`localhost` SQL SECURITY DEFINER */
/*!50001 VIEW `_main_cprice_for_contracts` AS select `f`.`id` AS `id`,`f`.`contracts_id` AS `contracts_id`,`f`.`dep_id` AS `dep_id`,`f`.`client_id` AS `client_id`,`f`.`serv_id` AS `serv_id`,`f`.`dep_has_worker_id` AS `dep_has_worker_id`,`f`.`worker_id` AS `worker_id`,`f`.`vdate` AS `vdate`,`f`.`quantity` AS `quantity`,`f`.`note` AS `note`,`f`.`create` AS `create`,`f`.`ts` AS `ts`,`f`.`cr_by` AS `cr_by`,`f`.`upd_by` AS `upd_by`,`f`.`reported` AS `reported`,`f`.`wdate` AS `wdate`,`f`.`overdid` AS `overdid`,`f`.`prev_quantity` AS `prev_quantity`,`f`.`perc` AS `perc`,`f`.`price` AS `price`,`f`.`price2` AS `price2`,`f`.`price3` AS `price3`,`f`.`servform_id` AS `servform_id`,((`f`.`perc` * `f`.`quantity`) * `f`.`price`) AS `to_pay`,((`f`.`perc` * `f`.`quantity`) * `f`.`price2`) AS `to_pay2` from (select `m`.`id` AS `id`,`m`.`contracts_id` AS `contracts_id`,`m`.`dep_id` AS `dep_id`,`m`.`client_id` AS `client_id`,`m`.`serv_id` AS `serv_id`,`m`.`dep_has_worker_id` AS `dep_has_worker_id`,`m`.`worker_id` AS `worker_id`,`m`.`vdate` AS `vdate`,`m`.`quantity` AS `quantity`,`m`.`note` AS `note`,`m`.`create` AS `create`,`m`.`ts` AS `ts`,`m`.`cr_by` AS `cr_by`,`m`.`upd_by` AS `upd_by`,`m`.`reported` AS `reported`,`m`.`wdate` AS `wdate`,`m`.`overdid` AS `overdid`,`m`.`prev_quantity` AS `prev_quantity`,(select `pd`.`perc` from `add_info` `pd` where ((`pd`.`pddate` <= `m`.`vdate`) and (`pd`.`contracts_id` = `m`.`contracts_id`)) order by `pd`.`pddate` desc limit 1) AS `perc`,`s`.`price` AS `price`,`s`.`price2` AS `price2`,`s`.`price3` AS `price3`,`r`.`servform_id` AS `servform_id` from (((`main` `m` join `serv` `s` on((`m`.`serv_id` = `s`.`id`))) join (select `contracts`.`id` AS `id`,`contracts`.`contracts` AS `contracts`,`contracts`.`contracts2` AS `contracts2`,`contracts`.`client_id` AS `client_id`,`contracts`.`dep_id` AS `dep_id`,`contracts`.`ripso_id` AS `ripso_id`,`contracts`.`blocked` AS `blocked`,`contracts`.`startdate` AS `startdate`,`contracts`.`enddate` AS `enddate`,`contracts`.`ippsuNum` AS `ippsuNum`,`contracts`.`note` AS `note`,`contracts`.`create` AS `create`,`contracts`.`ts` AS `ts`,`contracts`.`cr_by` AS `cr_by`,`contracts`.`upd_by` AS `upd_by`,`contracts`.`to_recheck` AS `to_recheck`,`contracts`.`check_date` AS `check_date`,`contracts`.`pyc_prim` AS `pyc_prim` from `contracts` where (`contracts`.`id` = `get_last_contr`())) `c` on((`m`.`contracts_id` = `c`.`id`))) left join `ripso` `r` on((`c`.`ripso_id` = `r`.`id`)))) `f` */;
/*!50001 SET character_set_client      = @saved_cs_client */;
/*!50001 SET character_set_results     = @saved_cs_results */;
/*!50001 SET collation_connection      = @saved_col_connection */;

--
-- Final view structure for view `_main_for_dep`
--

/*!50001 DROP VIEW IF EXISTS `_main_for_dep`*/;
/*!50001 SET @saved_cs_client          = @@character_set_client */;
/*!50001 SET @saved_cs_results         = @@character_set_results */;
/*!50001 SET @saved_col_connection     = @@collation_connection */;
/*!50001 SET character_set_client      = utf8mb4 */;
/*!50001 SET character_set_results     = utf8mb4 */;
/*!50001 SET collation_connection      = utf8mb4_0900_ai_ci */;
/*!50001 CREATE ALGORITHM=UNDEFINED */
/*!50013 DEFINER=`root`@`localhost` SQL SECURITY DEFINER */
/*!50001 VIEW `_main_for_dep` AS select `main`.`id` AS `id`,`main`.`contracts_id` AS `contracts_id`,`main`.`dep_id` AS `dep_id`,`main`.`client_id` AS `client_id`,`main`.`serv_id` AS `serv_id`,`main`.`dep_has_worker_id` AS `dep_has_worker_id`,`main`.`worker_id` AS `worker_id`,`main`.`vdate` AS `vdate`,`main`.`quantity` AS `quantity`,`main`.`note` AS `note`,`main`.`create` AS `create`,`main`.`ts` AS `ts`,`main`.`cr_by` AS `cr_by`,`main`.`upd_by` AS `upd_by`,`main`.`reported` AS `reported`,`main`.`wdate` AS `wdate`,`main`.`overdid` AS `overdid`,`main`.`prev_quantity` AS `prev_quantity` from `main` where `main`.`dep_id` in (select `_active_dep`.`id` from `_active_dep`) */;
/*!50001 SET character_set_client      = @saved_cs_client */;
/*!50001 SET character_set_results     = @saved_cs_results */;
/*!50001 SET collation_connection      = @saved_col_connection */;

--
-- Final view structure for view `_main_for_you`
--

/*!50001 DROP VIEW IF EXISTS `_main_for_you`*/;
/*!50001 SET @saved_cs_client          = @@character_set_client */;
/*!50001 SET @saved_cs_results         = @@character_set_results */;
/*!50001 SET @saved_col_connection     = @@collation_connection */;
/*!50001 SET character_set_client      = utf8mb4 */;
/*!50001 SET character_set_results     = utf8mb4 */;
/*!50001 SET collation_connection      = utf8mb4_0900_ai_ci */;
/*!50001 CREATE ALGORITHM=UNDEFINED */
/*!50013 DEFINER=`root`@`localhost` SQL SECURITY DEFINER */
/*!50001 VIEW `_main_for_you` AS select `main`.`id` AS `id`,`main`.`contracts_id` AS `contracts_id`,`main`.`dep_id` AS `dep_id`,`main`.`client_id` AS `client_id`,`main`.`serv_id` AS `serv_id`,`main`.`dep_has_worker_id` AS `dep_has_worker_id`,`main`.`worker_id` AS `worker_id`,`main`.`vdate` AS `vdate`,`main`.`quantity` AS `quantity`,`main`.`note` AS `note`,`main`.`create` AS `create`,`main`.`ts` AS `ts`,`main`.`cr_by` AS `cr_by`,`main`.`upd_by` AS `upd_by`,`main`.`reported` AS `reported`,`main`.`wdate` AS `wdate`,`main`.`overdid` AS `overdid`,`main`.`prev_quantity` AS `prev_quantity` from `main` where (`main`.`worker_id` = `GET_WID`()) */;
/*!50001 SET character_set_client      = @saved_cs_client */;
/*!50001 SET character_set_results     = @saved_cs_results */;
/*!50001 SET collation_connection      = @saved_col_connection */;

--
-- Final view structure for view `_main_months`
--

/*!50001 DROP VIEW IF EXISTS `_main_months`*/;
/*!50001 SET @saved_cs_client          = @@character_set_client */;
/*!50001 SET @saved_cs_results         = @@character_set_results */;
/*!50001 SET @saved_col_connection     = @@collation_connection */;
/*!50001 SET character_set_client      = utf8mb4 */;
/*!50001 SET character_set_results     = utf8mb4 */;
/*!50001 SET collation_connection      = utf8mb4_0900_ai_ci */;
/*!50001 CREATE ALGORITHM=UNDEFINED */
/*!50013 DEFINER=`root`@`localhost` SQL SECURITY DEFINER */
/*!50001 VIEW `_main_months` AS with `m1` as (select `main`.`client_id` AS `client_id`,`main`.`dep_id` AS `dep_id`,`main`.`contracts_id` AS `contracts_id`,`main`.`serv_id` AS `serv_id`,month(`main`.`vdate`) AS `month1`,year(`main`.`vdate`) AS `year1`,`main`.`dep_has_worker_id` AS `dep_has_worker_id`,`main`.`quantity` AS `quantity` from `main`) select `m1`.`serv_id` AS `serv_id`,`m1`.`dep_id` AS `dep_id`,`m1`.`contracts_id` AS `contracts_id`,`m1`.`year1` AS `year1`,`m1`.`dep_has_worker_id` AS `dep_has_worker_id`,sum((case when (`m1`.`month1` = 1) then `m1`.`quantity` else 0 end)) AS `month1`,sum((case when (`m1`.`month1` = 2) then `m1`.`quantity` else 0 end)) AS `month2`,sum((case when (`m1`.`month1` = 3) then `m1`.`quantity` else 0 end)) AS `month3`,sum((case when (`m1`.`month1` = 4) then `m1`.`quantity` else 0 end)) AS `month4`,sum((case when (`m1`.`month1` = 5) then `m1`.`quantity` else 0 end)) AS `month5`,sum((case when (`m1`.`month1` = 6) then `m1`.`quantity` else 0 end)) AS `month6`,sum((case when (`m1`.`month1` = 7) then `m1`.`quantity` else 0 end)) AS `month7`,sum((case when (`m1`.`month1` = 8) then `m1`.`quantity` else 0 end)) AS `month8`,sum((case when (`m1`.`month1` = 9) then `m1`.`quantity` else 0 end)) AS `month9`,sum((case when (`m1`.`month1` = 10) then `m1`.`quantity` else 0 end)) AS `month10`,sum((case when (`m1`.`month1` = 11) then `m1`.`quantity` else 0 end)) AS `month11`,sum((case when (`m1`.`month1` = 12) then `m1`.`quantity` else 0 end)) AS `month12` from `m1` group by `m1`.`dep_id`,`m1`.`contracts_id`,`m1`.`serv_id`,`m1`.`dep_has_worker_id` */;
/*!50001 SET character_set_client      = @saved_cs_client */;
/*!50001 SET character_set_results     = @saved_cs_results */;
/*!50001 SET collation_connection      = @saved_col_connection */;

--
-- Final view structure for view `_main_serv_name`
--

/*!50001 DROP VIEW IF EXISTS `_main_serv_name`*/;
/*!50001 SET @saved_cs_client          = @@character_set_client */;
/*!50001 SET @saved_cs_results         = @@character_set_results */;
/*!50001 SET @saved_col_connection     = @@collation_connection */;
/*!50001 SET character_set_client      = utf8mb4 */;
/*!50001 SET character_set_results     = utf8mb4 */;
/*!50001 SET collation_connection      = utf8mb4_0900_ai_ci */;
/*!50001 CREATE ALGORITHM=UNDEFINED */
/*!50013 DEFINER=`root`@`localhost` SQL SECURITY DEFINER */
/*!50001 VIEW `_main_serv_name` AS select `s`.`tnum` AS `serv`,`m`.`id` AS `id`,`m`.`contracts_id` AS `contracts_id`,`m`.`dep_id` AS `dep_id`,`m`.`client_id` AS `client_id`,`m`.`serv_id` AS `serv_id`,`m`.`dep_has_worker_id` AS `dep_has_worker_id`,`m`.`worker_id` AS `worker_id`,`m`.`vdate` AS `vdate`,`m`.`quantity` AS `quantity`,`m`.`note` AS `note`,`m`.`create` AS `create`,`m`.`ts` AS `ts`,`m`.`cr_by` AS `cr_by`,`m`.`upd_by` AS `upd_by`,`m`.`reported` AS `reported`,`m`.`wdate` AS `wdate`,`m`.`overdid` AS `overdid`,`m`.`prev_quantity` AS `prev_quantity` from (`main` `m` join `serv` `s` on((`s`.`id` = `m`.`serv_id`))) where `m`.`dep_id` in (select `_active_dep`.`id` from `_active_dep`) */;
/*!50001 SET character_set_client      = @saved_cs_client */;
/*!50001 SET character_set_results     = @saved_cs_results */;
/*!50001 SET collation_connection      = @saved_col_connection */;

--
-- Final view structure for view `_main_serv_name_ripso`
--

/*!50001 DROP VIEW IF EXISTS `_main_serv_name_ripso`*/;
/*!50001 SET @saved_cs_client          = @@character_set_client */;
/*!50001 SET @saved_cs_results         = @@character_set_results */;
/*!50001 SET @saved_col_connection     = @@collation_connection */;
/*!50001 SET character_set_client      = utf8mb4 */;
/*!50001 SET character_set_results     = utf8mb4 */;
/*!50001 SET collation_connection      = utf8mb4_0900_ai_ci */;
/*!50001 CREATE ALGORITHM=UNDEFINED */
/*!50013 DEFINER=`root`@`localhost` SQL SECURITY DEFINER */
/*!50001 VIEW `_main_serv_name_ripso` AS select `s`.`tnum` AS `serv`,`c`.`ripso_id` AS `ripso_id`,`m`.`id` AS `id`,`m`.`contracts_id` AS `contracts_id`,`m`.`dep_id` AS `dep_id`,`m`.`client_id` AS `client_id`,`m`.`serv_id` AS `serv_id`,`m`.`dep_has_worker_id` AS `dep_has_worker_id`,`m`.`worker_id` AS `worker_id`,`m`.`vdate` AS `vdate`,`m`.`quantity` AS `quantity`,`m`.`note` AS `note`,`m`.`create` AS `create`,`m`.`ts` AS `ts`,`m`.`cr_by` AS `cr_by`,`m`.`upd_by` AS `upd_by`,`m`.`reported` AS `reported`,`m`.`wdate` AS `wdate`,`m`.`overdid` AS `overdid`,`m`.`prev_quantity` AS `prev_quantity` from ((`main` `m` join `serv` `s` on((`s`.`id` = `m`.`serv_id`))) join `contracts` `c` on((`c`.`id` = `m`.`contracts_id`))) where `m`.`dep_id` in (select `_active_dep`.`id` from `_active_dep`) */;
/*!50001 SET character_set_client      = @saved_cs_client */;
/*!50001 SET character_set_results     = @saved_cs_results */;
/*!50001 SET collation_connection      = @saved_col_connection */;

--
-- Final view structure for view `_main_serv_name_ripso_static`
--

/*!50001 DROP VIEW IF EXISTS `_main_serv_name_ripso_static`*/;
/*!50001 SET @saved_cs_client          = @@character_set_client */;
/*!50001 SET @saved_cs_results         = @@character_set_results */;
/*!50001 SET @saved_col_connection     = @@collation_connection */;
/*!50001 SET character_set_client      = utf8mb4 */;
/*!50001 SET character_set_results     = utf8mb4 */;
/*!50001 SET collation_connection      = utf8mb4_0900_ai_ci */;
/*!50001 CREATE ALGORITHM=UNDEFINED */
/*!50013 DEFINER=`root`@`localhost` SQL SECURITY DEFINER */
/*!50001 VIEW `_main_serv_name_ripso_static` AS select `s`.`tnum` AS `serv`,`c`.`ripso_id` AS `ripso_id`,`m`.`id` AS `id`,`m`.`contracts_id` AS `contracts_id`,`m`.`dep_id` AS `dep_id`,`m`.`client_id` AS `client_id`,`m`.`serv_id` AS `serv_id`,`m`.`dep_has_worker_id` AS `dep_has_worker_id`,`m`.`worker_id` AS `worker_id`,`m`.`vdate` AS `vdate`,`m`.`quantity` AS `quantity`,`m`.`note` AS `note`,`m`.`create` AS `create`,`m`.`ts` AS `ts`,`m`.`cr_by` AS `cr_by`,`m`.`upd_by` AS `upd_by`,`m`.`reported` AS `reported`,`m`.`wdate` AS `wdate`,`m`.`overdid` AS `overdid`,`m`.`prev_quantity` AS `prev_quantity` from ((`main` `m` join `serv` `s` on((`s`.`id` = `m`.`serv_id`))) join `contracts` `c` on((`c`.`id` = `m`.`contracts_id`))) where `m`.`dep_id` in (select `_active_dep_static`.`id` from `_active_dep_static`) */;
/*!50001 SET character_set_client      = @saved_cs_client */;
/*!50001 SET character_set_results     = @saved_cs_results */;
/*!50001 SET collation_connection      = @saved_col_connection */;

--
-- Final view structure for view `_main_serv_name_static`
--

/*!50001 DROP VIEW IF EXISTS `_main_serv_name_static`*/;
/*!50001 SET @saved_cs_client          = @@character_set_client */;
/*!50001 SET @saved_cs_results         = @@character_set_results */;
/*!50001 SET @saved_col_connection     = @@collation_connection */;
/*!50001 SET character_set_client      = utf8mb4 */;
/*!50001 SET character_set_results     = utf8mb4 */;
/*!50001 SET collation_connection      = utf8mb4_0900_ai_ci */;
/*!50001 CREATE ALGORITHM=UNDEFINED */
/*!50013 DEFINER=`root`@`localhost` SQL SECURITY DEFINER */
/*!50001 VIEW `_main_serv_name_static` AS select `s`.`tnum` AS `serv`,`m`.`id` AS `id`,`m`.`contracts_id` AS `contracts_id`,`m`.`dep_id` AS `dep_id`,`m`.`client_id` AS `client_id`,`m`.`serv_id` AS `serv_id`,`m`.`dep_has_worker_id` AS `dep_has_worker_id`,`m`.`worker_id` AS `worker_id`,`m`.`vdate` AS `vdate`,`m`.`quantity` AS `quantity`,`m`.`note` AS `note`,`m`.`create` AS `create`,`m`.`ts` AS `ts`,`m`.`cr_by` AS `cr_by`,`m`.`upd_by` AS `upd_by`,`m`.`reported` AS `reported`,`m`.`wdate` AS `wdate`,`m`.`overdid` AS `overdid`,`m`.`prev_quantity` AS `prev_quantity` from (`main` `m` join `serv` `s` on((`s`.`id` = `m`.`serv_id`))) where `m`.`dep_id` in (select `_active_dep_static`.`id` from `_active_dep_static`) */;
/*!50001 SET character_set_client      = @saved_cs_client */;
/*!50001 SET character_set_results     = @saved_cs_results */;
/*!50001 SET collation_connection      = @saved_col_connection */;

--
-- Final view structure for view `_serv_activ`
--

/*!50001 DROP VIEW IF EXISTS `_serv_activ`*/;
/*!50001 SET @saved_cs_client          = @@character_set_client */;
/*!50001 SET @saved_cs_results         = @@character_set_results */;
/*!50001 SET @saved_col_connection     = @@collation_connection */;
/*!50001 SET character_set_client      = utf8mb4 */;
/*!50001 SET character_set_results     = utf8mb4 */;
/*!50001 SET collation_connection      = utf8mb4_0900_ai_ci */;
/*!50001 CREATE ALGORITHM=TEMPTABLE */
/*!50013 DEFINER=`root`@`localhost` SQL SECURITY DEFINER */
/*!50001 VIEW `_serv_activ` AS with `sa` as (select `serv`.`id` AS `id`,`serv`.`serv` AS `serv`,`serv`.`serv_text` AS `serv_text`,`serv`.`tnum` AS `tnum`,`serv`.`year` AS `year`,`serv`.`sub_serv` AS `sub_serv`,`serv`.`sub_serv_str` AS `sub_serv_str`,`serv`.`price` AS `price`,`serv`.`price2` AS `price2`,`serv`.`price3` AS `price3`,`serv`.`archive` AS `archive`,`serv`.`total` AS `total`,`serv`.`acronym` AS `acronym`,`serv`.`workload` AS `workload`,`serv`.`content` AS `content`,`serv`.`create` AS `create`,`serv`.`ts` AS `ts`,`serv`.`cr_by` AS `cr_by`,`serv`.`upd_by` AS `upd_by` from `serv` where (`serv`.`year` = `Get_year`(`Get_WID`()))), `slvl` as (select `s`.`id` AS `id`,(select trim(trailing ',' from (select concat(`s`.`id`,',',coalesce(group_concat(`s1`.`id` separator ','),'')) from `sa` `s1` where (`s1`.`sub_serv` = `s`.`id`)))) AS `lvl`,(select trim(trailing ',' from (select concat(coalesce(group_concat(`s2`.`id` separator ','),'')) from (`sa` `s1` join `sa` `s2` on((`s2`.`sub_serv` = `s1`.`id`))) where (`s1`.`sub_serv` = `s`.`id`)))) AS `lvl2`,(select trim(trailing ',' from concat(coalesce(group_concat(`s3`.`id` separator ','),''))) from ((`sa` `s1` join `sa` `s2` on((`s2`.`sub_serv` = `s1`.`id`))) join `sa` `s3` on((`s3`.`sub_serv` = `s2`.`id`))) where (`s1`.`sub_serv` = `s`.`id`)) AS `lvl3`,(select trim(trailing ',' from concat(coalesce(group_concat(`s4`.`id` separator ','),''))) from (((`sa` `s1` join `sa` `s2` on((`s2`.`sub_serv` = `s1`.`id`))) join `sa` `s3` on((`s3`.`sub_serv` = `s2`.`id`))) join `sa` `s4` on((`s4`.`sub_serv` = `s3`.`id`))) where (`s1`.`sub_serv` = `s`.`id`)) AS `lvl4`,(select trim(trailing ',' from concat(coalesce(group_concat(`s5`.`id` separator ','),''))) from ((((`sa` `s1` join `sa` `s2` on((`s2`.`sub_serv` = `s1`.`id`))) join `sa` `s3` on((`s3`.`sub_serv` = `s2`.`id`))) join `sa` `s4` on((`s4`.`sub_serv` = `s3`.`id`))) join `sa` `s5` on((`s5`.`sub_serv` = `s4`.`id`))) where (`s1`.`sub_serv` = `s`.`id`)) AS `lvl5` from `sa` `s`), `sid_list` as (select `sa`.`id` AS `id`,trim(trailing ',' from concat(`l`.`lvl`,',',`l`.`lvl2`,',',`l`.`lvl3`,',',`l`.`lvl4`,',',`l`.`lvl5`,',')) AS `serv_id_list` from (`sa` join `slvl` `l` on((`sa`.`id` = `l`.`id`)))) select `s`.`id` AS `id`,`s`.`serv` AS `serv`,`s`.`serv_text` AS `serv_text`,`s`.`tnum` AS `tnum`,`s`.`price` AS `price`,`s`.`total` AS `total`,`s`.`sub_serv` AS `sub_serv`,`sl`.`serv_id_list` AS `serv_id_list` from (`sa` `s` left join `sid_list` `sl` on((`sl`.`id` = `s`.`id`))) */;
/*!50001 SET character_set_client      = @saved_cs_client */;
/*!50001 SET character_set_results     = @saved_cs_results */;
/*!50001 SET collation_connection      = @saved_col_connection */;

--
-- Final view structure for view `_serv_total`
--

/*!50001 DROP VIEW IF EXISTS `_serv_total`*/;
/*!50001 SET @saved_cs_client          = @@character_set_client */;
/*!50001 SET @saved_cs_results         = @@character_set_results */;
/*!50001 SET @saved_col_connection     = @@collation_connection */;
/*!50001 SET character_set_client      = utf8mb4 */;
/*!50001 SET character_set_results     = utf8mb4 */;
/*!50001 SET collation_connection      = utf8mb4_0900_ai_ci */;
/*!50001 CREATE ALGORITHM=UNDEFINED */
/*!50013 DEFINER=`root`@`localhost` SQL SECURITY DEFINER */
/*!50001 VIEW `_serv_total` AS select `serv`.`id` AS `id`,`serv`.`serv` AS `serv`,`serv`.`serv_text` AS `serv_text`,`serv`.`tnum` AS `tnum`,`serv`.`year` AS `year`,`serv`.`sub_serv` AS `sub_serv`,`serv`.`sub_serv_str` AS `sub_serv_str`,`serv`.`price` AS `price`,`serv`.`price2` AS `price2`,`serv`.`price3` AS `price3`,`serv`.`archive` AS `archive`,`serv`.`total` AS `total`,`serv`.`acronym` AS `acronym`,`serv`.`workload` AS `workload`,`serv`.`content` AS `content`,`serv`.`create` AS `create`,`serv`.`ts` AS `ts`,`serv`.`cr_by` AS `cr_by`,`serv`.`upd_by` AS `upd_by` from `serv` where (`serv`.`total` = 1) */;
/*!50001 SET character_set_client      = @saved_cs_client */;
/*!50001 SET character_set_results     = @saved_cs_results */;
/*!50001 SET collation_connection      = @saved_col_connection */;

--
-- Final view structure for view `_user_has_main`
--

/*!50001 DROP VIEW IF EXISTS `_user_has_main`*/;
/*!50001 SET @saved_cs_client          = @@character_set_client */;
/*!50001 SET @saved_cs_results         = @@character_set_results */;
/*!50001 SET @saved_col_connection     = @@collation_connection */;
/*!50001 SET character_set_client      = utf8mb4 */;
/*!50001 SET character_set_results     = utf8mb4 */;
/*!50001 SET collation_connection      = utf8mb4_0900_ai_ci */;
/*!50001 CREATE ALGORITHM=UNDEFINED */
/*!50013 DEFINER=`root`@`localhost` SQL SECURITY DEFINER */
/*!50001 VIEW `_user_has_main` AS select `main`.`id` AS `id`,`main`.`contracts_id` AS `contracts_id`,`main`.`dep_id` AS `dep_id`,`main`.`client_id` AS `client_id`,`main`.`serv_id` AS `serv_id`,`main`.`dep_has_worker_id` AS `dep_has_worker_id`,`main`.`worker_id` AS `worker_id`,`main`.`vdate` AS `vdate`,`main`.`quantity` AS `quantity`,`main`.`note` AS `note`,`main`.`create` AS `create`,`main`.`ts` AS `ts`,`main`.`cr_by` AS `cr_by`,`main`.`upd_by` AS `upd_by`,`main`.`reported` AS `reported`,`main`.`wdate` AS `wdate`,`main`.`overdid` AS `overdid`,`main`.`prev_quantity` AS `prev_quantity` from `main` where ((`main`.`cr_by` = `GET_WID`()) or (`main`.`upd_by` = `GET_WID`())) order by `main`.`ts` desc */;
/*!50001 SET character_set_client      = @saved_cs_client */;
/*!50001 SET character_set_results     = @saved_cs_results */;
/*!50001 SET collation_connection      = @saved_col_connection */;

--
-- Final view structure for view `_user_has_main_limit30`
--

/*!50001 DROP VIEW IF EXISTS `_user_has_main_limit30`*/;
/*!50001 SET @saved_cs_client          = @@character_set_client */;
/*!50001 SET @saved_cs_results         = @@character_set_results */;
/*!50001 SET @saved_col_connection     = @@collation_connection */;
/*!50001 SET character_set_client      = utf8mb4 */;
/*!50001 SET character_set_results     = utf8mb4 */;
/*!50001 SET collation_connection      = utf8mb4_0900_ai_ci */;
/*!50001 CREATE ALGORITHM=UNDEFINED */
/*!50013 DEFINER=`root`@`localhost` SQL SECURITY DEFINER */
/*!50001 VIEW `_user_has_main_limit30` AS select `main`.`id` AS `id`,`main`.`contracts_id` AS `contracts_id`,`main`.`dep_id` AS `dep_id`,`main`.`client_id` AS `client_id`,`main`.`serv_id` AS `serv_id`,`main`.`dep_has_worker_id` AS `dep_has_worker_id`,`main`.`worker_id` AS `worker_id`,`main`.`vdate` AS `vdate`,`main`.`quantity` AS `quantity`,`main`.`note` AS `note`,`main`.`create` AS `create`,`main`.`ts` AS `ts`,`main`.`cr_by` AS `cr_by`,`main`.`upd_by` AS `upd_by`,`main`.`reported` AS `reported`,`main`.`wdate` AS `wdate`,`main`.`overdid` AS `overdid`,`main`.`prev_quantity` AS `prev_quantity` from `main` where ((`main`.`cr_by` = `GET_WID`()) or (`main`.`upd_by` = `GET_WID`())) order by `main`.`id` desc limit 30 */;
/*!50001 SET character_set_client      = @saved_cs_client */;
/*!50001 SET character_set_results     = @saved_cs_results */;
/*!50001 SET collation_connection      = @saved_col_connection */;

--
-- Final view structure for view `_user_has_main_today`
--

/*!50001 DROP VIEW IF EXISTS `_user_has_main_today`*/;
/*!50001 SET @saved_cs_client          = @@character_set_client */;
/*!50001 SET @saved_cs_results         = @@character_set_results */;
/*!50001 SET @saved_col_connection     = @@collation_connection */;
/*!50001 SET character_set_client      = utf8mb4 */;
/*!50001 SET character_set_results     = utf8mb4 */;
/*!50001 SET collation_connection      = utf8mb4_0900_ai_ci */;
/*!50001 CREATE ALGORITHM=UNDEFINED */
/*!50013 DEFINER=`root`@`localhost` SQL SECURITY DEFINER */
/*!50001 VIEW `_user_has_main_today` AS select `main`.`id` AS `id`,`main`.`contracts_id` AS `contracts_id`,`main`.`dep_id` AS `dep_id`,`main`.`client_id` AS `client_id`,`main`.`serv_id` AS `serv_id`,`main`.`dep_has_worker_id` AS `dep_has_worker_id`,`main`.`worker_id` AS `worker_id`,`main`.`vdate` AS `vdate`,`main`.`quantity` AS `quantity`,`main`.`note` AS `note`,`main`.`create` AS `create`,`main`.`ts` AS `ts`,`main`.`cr_by` AS `cr_by`,`main`.`upd_by` AS `upd_by`,`main`.`reported` AS `reported`,`main`.`wdate` AS `wdate`,`main`.`overdid` AS `overdid`,`main`.`prev_quantity` AS `prev_quantity` from `main` where (((`main`.`cr_by` = `GET_WID`()) or (`main`.`upd_by` = `GET_WID`())) and (`main`.`ts` = curdate())) order by `main`.`ts` desc */;
/*!50001 SET character_set_client      = @saved_cs_client */;
/*!50001 SET character_set_results     = @saved_cs_results */;
/*!50001 SET collation_connection      = @saved_col_connection */;

--
-- Final view structure for view `_worker_has_dep`
--

/*!50001 DROP VIEW IF EXISTS `_worker_has_dep`*/;
/*!50001 SET @saved_cs_client          = @@character_set_client */;
/*!50001 SET @saved_cs_results         = @@character_set_results */;
/*!50001 SET @saved_col_connection     = @@collation_connection */;
/*!50001 SET character_set_client      = utf8mb4 */;
/*!50001 SET character_set_results     = utf8mb4 */;
/*!50001 SET collation_connection      = utf8mb4_0900_ai_ci */;
/*!50001 CREATE ALGORITHM=UNDEFINED */
/*!50013 DEFINER=`root`@`localhost` SQL SECURITY DEFINER */
/*!50001 VIEW `_worker_has_dep` AS select `dw`.`dep_id` AS `id`,`d`.`dep` AS `dep` from ((`dep_has_worker` `dw` join `dep` `d` on((`d`.`id` = `dw`.`dep_id`))) join `worker` `w` on((`dw`.`worker_id` = `w`.`id`))) where ((`dw`.`worker_id` = `GET_wID`()) and (`dw`.`archive` = 0)) */;
/*!50001 SET character_set_client      = @saved_cs_client */;
/*!50001 SET character_set_results     = @saved_cs_results */;
/*!50001 SET collation_connection      = @saved_col_connection */;

--
-- Final view structure for view `_worker_has_main`
--

/*!50001 DROP VIEW IF EXISTS `_worker_has_main`*/;
/*!50001 SET @saved_cs_client          = @@character_set_client */;
/*!50001 SET @saved_cs_results         = @@character_set_results */;
/*!50001 SET @saved_col_connection     = @@collation_connection */;
/*!50001 SET character_set_client      = utf8mb4 */;
/*!50001 SET character_set_results     = utf8mb4 */;
/*!50001 SET collation_connection      = utf8mb4_0900_ai_ci */;
/*!50001 CREATE ALGORITHM=UNDEFINED */
/*!50013 DEFINER=`root`@`localhost` SQL SECURITY DEFINER */
/*!50001 VIEW `_worker_has_main` AS select `main`.`id` AS `id`,`main`.`contracts_id` AS `contracts_id`,`main`.`dep_id` AS `dep_id`,`main`.`client_id` AS `client_id`,`main`.`serv_id` AS `serv_id`,`main`.`dep_has_worker_id` AS `dep_has_worker_id`,`main`.`worker_id` AS `worker_id`,`main`.`vdate` AS `vdate`,`main`.`quantity` AS `quantity`,`main`.`note` AS `note`,`main`.`create` AS `create`,`main`.`ts` AS `ts`,`main`.`cr_by` AS `cr_by`,`main`.`upd_by` AS `upd_by`,`main`.`reported` AS `reported`,`main`.`wdate` AS `wdate`,`main`.`overdid` AS `overdid`,`main`.`prev_quantity` AS `prev_quantity` from `main` where (`main`.`worker_id` = `GET_WID`()) */;
/*!50001 SET character_set_client      = @saved_cs_client */;
/*!50001 SET character_set_results     = @saved_cs_results */;
/*!50001 SET collation_connection      = @saved_col_connection */;

--
-- Final view structure for view `_worker_settings`
--

/*!50001 DROP VIEW IF EXISTS `_worker_settings`*/;
/*!50001 SET @saved_cs_client          = @@character_set_client */;
/*!50001 SET @saved_cs_results         = @@character_set_results */;
/*!50001 SET @saved_col_connection     = @@collation_connection */;
/*!50001 SET character_set_client      = utf8mb4 */;
/*!50001 SET character_set_results     = utf8mb4 */;
/*!50001 SET collation_connection      = utf8mb4_0900_ai_ci */;
/*!50001 CREATE ALGORITHM=UNDEFINED */
/*!50013 DEFINER=`root`@`localhost` SQL SECURITY DEFINER */
/*!50001 VIEW `_worker_settings` AS select `worker_settings`.`id` AS `id`,`worker_settings`.`last_tab` AS `last_tab`,`worker_settings`.`last_dep` AS `last_dep`,`worker_settings`.`last_client` AS `last_client`,`worker_settings`.`last_contr` AS `last_contr`,`worker_settings`.`last_client_filter` AS `last_client_filter`,`worker_settings`.`last_year` AS `last_year` from `worker_settings` where (`worker_settings`.`id` = `GET_wID`()) */;
/*!50001 SET character_set_client      = @saved_cs_client */;
/*!50001 SET character_set_results     = @saved_cs_results */;
/*!50001 SET collation_connection      = @saved_col_connection */;

--
-- Final view structure for view `add_info_for_client`
--

/*!50001 DROP VIEW IF EXISTS `add_info_for_client`*/;
/*!50001 SET @saved_cs_client          = @@character_set_client */;
/*!50001 SET @saved_cs_results         = @@character_set_results */;
/*!50001 SET @saved_col_connection     = @@collation_connection */;
/*!50001 SET character_set_client      = utf8mb4 */;
/*!50001 SET character_set_results     = utf8mb4 */;
/*!50001 SET collation_connection      = utf8mb4_0900_ai_ci */;
/*!50001 CREATE ALGORITHM=UNDEFINED */
/*!50013 DEFINER=`root`@`localhost` SQL SECURITY DEFINER */
/*!50001 VIEW `add_info_for_client` AS select `u`.`id` AS `client_id`,`a`.`pddate` AS `pddate`,`a`.`contracts_id` AS `contracts_id`,`a`.`predv_money` AS `predv_money`,`a`.`curFIO` AS `curFIO`,`a`.`psp` AS `psp`,`a`.`address` AS `address`,`a`.`sdd` AS `sdd`,`a`.`sdd_date` AS `sdd_date`,`a`.`perc` AS `perc`,`a`.`not_standart_contract` AS `not_standart_contract`,`a`.`not_standart_act` AS `not_standart_act`,`a`.`note` AS `note`,`a`.`create` AS `create`,`a`.`ts` AS `ts`,`a`.`cr_by` AS `cr_by`,`a`.`upd_by` AS `upd_by`,`a`.`repr_FIO` AS `repr_FIO`,`a`.`repr_addr` AS `repr_addr`,`a`.`repr_psp` AS `repr_psp`,`a`.`work_livemin` AS `work_livemin` from ((`add_info` `a` join `contracts` `c` on((`c`.`id` = `a`.`contracts_id`))) join `client` `u` on((`c`.`client_id` = `u`.`id`))) order by `a`.`pddate` desc */;
/*!50001 SET character_set_client      = @saved_cs_client */;
/*!50001 SET character_set_results     = @saved_cs_results */;
/*!50001 SET collation_connection      = @saved_col_connection */;

--
-- Final view structure for view `cr_by`
--

/*!50001 DROP VIEW IF EXISTS `cr_by`*/;
/*!50001 SET @saved_cs_client          = @@character_set_client */;
/*!50001 SET @saved_cs_results         = @@character_set_results */;
/*!50001 SET @saved_col_connection     = @@collation_connection */;
/*!50001 SET character_set_client      = utf8mb4 */;
/*!50001 SET character_set_results     = utf8mb4 */;
/*!50001 SET collation_connection      = utf8mb4_0900_ai_ci */;
/*!50001 CREATE ALGORITHM=UNDEFINED */
/*!50013 DEFINER=`root`@`localhost` SQL SECURITY DEFINER */
/*!50001 VIEW `cr_by` AS select `worker`.`id` AS `id`,`worker`.`worker` AS `cr_by`,`worker`.`user` AS `user`,`worker`.`note` AS `note`,`worker`.`role_id` AS `role_id`,`worker`.`dep_id` AS `dep_id`,`worker`.`archive` AS `archive` from `worker` */;
/*!50001 SET character_set_client      = @saved_cs_client */;
/*!50001 SET character_set_results     = @saved_cs_results */;
/*!50001 SET collation_connection      = @saved_col_connection */;

--
-- Final view structure for view `cr_dep`
--

/*!50001 DROP VIEW IF EXISTS `cr_dep`*/;
/*!50001 SET @saved_cs_client          = @@character_set_client */;
/*!50001 SET @saved_cs_results         = @@character_set_results */;
/*!50001 SET @saved_col_connection     = @@collation_connection */;
/*!50001 SET character_set_client      = utf8mb4 */;
/*!50001 SET character_set_results     = utf8mb4 */;
/*!50001 SET collation_connection      = utf8mb4_0900_ai_ci */;
/*!50001 CREATE ALGORITHM=UNDEFINED */
/*!50013 DEFINER=`root`@`localhost` SQL SECURITY DEFINER */
/*!50001 VIEW `cr_dep` AS select `dep`.`id` AS `id`,`dep`.`dep` AS `cr_dep` from `dep` */;
/*!50001 SET character_set_client      = @saved_cs_client */;
/*!50001 SET character_set_results     = @saved_cs_results */;
/*!50001 SET collation_connection      = @saved_col_connection */;

--
-- Final view structure for view `cr_dep_id`
--

/*!50001 DROP VIEW IF EXISTS `cr_dep_id`*/;
/*!50001 SET @saved_cs_client          = @@character_set_client */;
/*!50001 SET @saved_cs_results         = @@character_set_results */;
/*!50001 SET @saved_col_connection     = @@collation_connection */;
/*!50001 SET character_set_client      = utf8mb4 */;
/*!50001 SET character_set_results     = utf8mb4 */;
/*!50001 SET collation_connection      = utf8mb4_0900_ai_ci */;
/*!50001 CREATE ALGORITHM=UNDEFINED */
/*!50013 DEFINER=`root`@`localhost` SQL SECURITY DEFINER */
/*!50001 VIEW `cr_dep_id` AS select `dep`.`id` AS `id`,`dep`.`dep` AS `dep`,`dep`.`dep_full_name` AS `dep_full_name`,`dep`.`dep_puname` AS `dep_puname`,`dep`.`note` AS `note`,`dep`.`archive` AS `archive`,`dep`.`complex_dep_id` AS `complex_dep_id` from `dep` */;
/*!50001 SET character_set_client      = @saved_cs_client */;
/*!50001 SET character_set_results     = @saved_cs_results */;
/*!50001 SET collation_connection      = @saved_col_connection */;

--
-- Final view structure for view `dep_has_client_by_contr`
--

/*!50001 DROP VIEW IF EXISTS `dep_has_client_by_contr`*/;
/*!50001 SET @saved_cs_client          = @@character_set_client */;
/*!50001 SET @saved_cs_results         = @@character_set_results */;
/*!50001 SET @saved_col_connection     = @@collation_connection */;
/*!50001 SET character_set_client      = utf8mb4 */;
/*!50001 SET character_set_results     = utf8mb4 */;
/*!50001 SET collation_connection      = utf8mb4_0900_ai_ci */;
/*!50001 CREATE ALGORITHM=UNDEFINED */
/*!50013 DEFINER=`root`@`localhost` SQL SECURITY DEFINER */
/*!50001 VIEW `dep_has_client_by_contr` AS select `client`.`id` AS `id`,`client`.`client` AS `client`,`client`.`client_short` AS `client_short`,`client`.`clientDeath` AS `clientDeath`,`client`.`clientbirth` AS `clientbirth`,`client`.`ESRN` AS `ESRN`,`client`.`note` AS `note`,`client`.`phone` AS `phone`,`client`.`snils` AS `snils`,`client`.`curator` AS `curator`,`client`.`create` AS `create`,`client`.`ts` AS `ts`,`client`.`cr_by` AS `cr_by`,`client`.`upd_by` AS `upd_by`,`client`.`cr_dep_id` AS `cr_dep_id` from `client` where `client`.`id` in (select `c`.`client_id` from `contracts` `c` where (`c`.`dep_id` = `GET_DEP`(`GET_wID`()))) */;
/*!50001 SET character_set_client      = @saved_cs_client */;
/*!50001 SET character_set_results     = @saved_cs_results */;
/*!50001 SET collation_connection      = @saved_col_connection */;

--
-- Final view structure for view `dep_has_client_by_ripso`
--

/*!50001 DROP VIEW IF EXISTS `dep_has_client_by_ripso`*/;
/*!50001 SET @saved_cs_client          = @@character_set_client */;
/*!50001 SET @saved_cs_results         = @@character_set_results */;
/*!50001 SET @saved_col_connection     = @@collation_connection */;
/*!50001 SET character_set_client      = utf8mb4 */;
/*!50001 SET character_set_results     = utf8mb4 */;
/*!50001 SET collation_connection      = utf8mb4_0900_ai_ci */;
/*!50001 CREATE ALGORITHM=UNDEFINED */
/*!50013 DEFINER=`root`@`localhost` SQL SECURITY DEFINER */
/*!50001 VIEW `dep_has_client_by_ripso` AS select `client`.`id` AS `id`,`client`.`client` AS `client`,`client`.`client_short` AS `client_short`,`client`.`clientDeath` AS `clientDeath`,`client`.`clientbirth` AS `clientbirth`,`client`.`ESRN` AS `ESRN`,`client`.`note` AS `note`,`client`.`phone` AS `phone`,`client`.`snils` AS `snils`,`client`.`curator` AS `curator`,`client`.`create` AS `create`,`client`.`ts` AS `ts`,`client`.`cr_by` AS `cr_by`,`client`.`upd_by` AS `upd_by`,`client`.`cr_dep_id` AS `cr_dep_id` from `client` where `client`.`id` in (select `c`.`client_id` from (`contracts` `c` join `dep_has_ripso` `rod` on((`rod`.`ripso_id` = `c`.`ripso_id`))) where `rod`.`dep_id` in (select `_active_dep`.`id` from `_active_dep`)) */;
/*!50001 SET character_set_client      = @saved_cs_client */;
/*!50001 SET character_set_results     = @saved_cs_results */;
/*!50001 SET collation_connection      = @saved_col_connection */;

--
-- Final view structure for view `dep_has_main`
--

/*!50001 DROP VIEW IF EXISTS `dep_has_main`*/;
/*!50001 SET @saved_cs_client          = @@character_set_client */;
/*!50001 SET @saved_cs_results         = @@character_set_results */;
/*!50001 SET @saved_col_connection     = @@collation_connection */;
/*!50001 SET character_set_client      = utf8mb4 */;
/*!50001 SET character_set_results     = utf8mb4 */;
/*!50001 SET collation_connection      = utf8mb4_0900_ai_ci */;
/*!50001 CREATE ALGORITHM=UNDEFINED */
/*!50013 DEFINER=`root`@`localhost` SQL SECURITY DEFINER */
/*!50001 VIEW `dep_has_main` AS select `main`.`id` AS `id`,`main`.`contracts_id` AS `contracts_id`,`main`.`dep_id` AS `dep_id`,`main`.`client_id` AS `client_id`,`main`.`serv_id` AS `serv_id`,`main`.`dep_has_worker_id` AS `dep_has_worker_id`,`main`.`worker_id` AS `worker_id`,`main`.`vdate` AS `vdate`,`main`.`quantity` AS `quantity`,`main`.`note` AS `note`,`main`.`create` AS `create`,`main`.`ts` AS `ts`,`main`.`cr_by` AS `cr_by`,`main`.`upd_by` AS `upd_by`,`main`.`reported` AS `reported`,`main`.`wdate` AS `wdate`,`main`.`overdid` AS `overdid`,`main`.`prev_quantity` AS `prev_quantity` from `main` where `main`.`dep_id` in (select `_active_dep`.`id` from `_active_dep`) */;
/*!50001 SET character_set_client      = @saved_cs_client */;
/*!50001 SET character_set_results     = @saved_cs_results */;
/*!50001 SET collation_connection      = @saved_col_connection */;

--
-- Final view structure for view `dep_has_serv`
--

/*!50001 DROP VIEW IF EXISTS `dep_has_serv`*/;
/*!50001 SET @saved_cs_client          = @@character_set_client */;
/*!50001 SET @saved_cs_results         = @@character_set_results */;
/*!50001 SET @saved_col_connection     = @@collation_connection */;
/*!50001 SET character_set_client      = utf8mb4 */;
/*!50001 SET character_set_results     = utf8mb4 */;
/*!50001 SET collation_connection      = utf8mb4_0900_ai_ci */;
/*!50001 CREATE ALGORITHM=UNDEFINED */
/*!50013 DEFINER=`root`@`localhost` SQL SECURITY DEFINER */
/*!50001 VIEW `dep_has_serv` AS select `s`.`id` AS `id`,`s`.`tnum` AS `tnum`,`s`.`serv` AS `serv`,`s`.`year` AS `year`,`s`.`sub_serv` AS `sub_serv`,`s`.`sub_serv_str` AS `sub_serv_str`,`s`.`price` AS `price`,`s`.`price2` AS `price2`,`s`.`price3` AS `price3`,`s`.`archive` AS `archive`,`s`.`total` AS `total`,`s`.`acronym` AS `acronym`,`s`.`workload` AS `workload`,`s`.`content` AS `content` from ((`serv` `s` join `ripso_has_serv` `rhs` on((`rhs`.`serv_id` = `s`.`id`))) join `dep_has_ripso` `dhr` on((`rhs`.`ripso_id` = `dhr`.`ripso_id`))) where `dhr`.`dep_id` in (select `_active_dep`.`id` from `_active_dep`) */;
/*!50001 SET character_set_client      = @saved_cs_client */;
/*!50001 SET character_set_results     = @saved_cs_results */;
/*!50001 SET collation_connection      = @saved_col_connection */;

--
-- Final view structure for view `dep_total_serv`
--

/*!50001 DROP VIEW IF EXISTS `dep_total_serv`*/;
/*!50001 SET @saved_cs_client          = @@character_set_client */;
/*!50001 SET @saved_cs_results         = @@character_set_results */;
/*!50001 SET @saved_col_connection     = @@collation_connection */;
/*!50001 SET character_set_client      = utf8mb4 */;
/*!50001 SET character_set_results     = utf8mb4 */;
/*!50001 SET collation_connection      = utf8mb4_0900_ai_ci */;
/*!50001 CREATE ALGORITHM=UNDEFINED */
/*!50013 DEFINER=`root`@`localhost` SQL SECURITY DEFINER */
/*!50001 VIEW `dep_total_serv` AS select `main`.`contracts_id` AS `contracts_id`,`main`.`dep_id` AS `dep_id`,`main`.`serv_id` AS `serv_id`,`main`.`worker_id` AS `worker_id`,sum(`main`.`quantity`) AS `SUM(quantity)`,month(`main`.`vdate`) AS `MONTH(vdate)`,year(`main`.`vdate`) AS `YEAR(vdate)` from `main` where `main`.`dep_id` in (select `_active_dep`.`id` from `_active_dep`) group by `main`.`contracts_id`,`main`.`dep_id`,`main`.`serv_id`,`main`.`worker_id`,month(`main`.`vdate`),year(`main`.`vdate`) */;
/*!50001 SET character_set_client      = @saved_cs_client */;
/*!50001 SET character_set_results     = @saved_cs_results */;
/*!50001 SET collation_connection      = @saved_col_connection */;

--
-- Final view structure for view `dep_total_supserv1`
--

/*!50001 DROP VIEW IF EXISTS `dep_total_supserv1`*/;
/*!50001 SET @saved_cs_client          = @@character_set_client */;
/*!50001 SET @saved_cs_results         = @@character_set_results */;
/*!50001 SET @saved_col_connection     = @@collation_connection */;
/*!50001 SET character_set_client      = utf8mb4 */;
/*!50001 SET character_set_results     = utf8mb4 */;
/*!50001 SET collation_connection      = utf8mb4_0900_ai_ci */;
/*!50001 CREATE ALGORITHM=UNDEFINED */
/*!50013 DEFINER=`root`@`localhost` SQL SECURITY DEFINER */
/*!50001 VIEW `dep_total_supserv1` AS select `m`.`contracts_id` AS `contracts_id`,`m`.`dep_id` AS `dep_id`,`s`.`sub_serv` AS `sub_serv`,`m`.`worker_id` AS `worker_id`,sum(`m`.`quantity`) AS `SUM(quantity)`,`m`.`mnth1` AS `mnth1`,`m`.`year1` AS `year1` from (`serv` `s` left join (select `main`.`contracts_id` AS `contracts_id`,`main`.`dep_id` AS `dep_id`,`main`.`serv_id` AS `serv_id`,`main`.`worker_id` AS `worker_id`,sum(`main`.`quantity`) AS `quantity`,month(`main`.`vdate`) AS `mnth1`,year(`main`.`vdate`) AS `year1` from `main` group by `main`.`contracts_id`,`main`.`dep_id`,`main`.`serv_id`,`main`.`worker_id`,month(`main`.`vdate`),year(`main`.`vdate`)) `m` on((`m`.`serv_id` = `s`.`id`))) group by `m`.`contracts_id`,`m`.`dep_id`,`s`.`sub_serv`,`m`.`worker_id`,`m`.`mnth1`,`m`.`year1` */;
/*!50001 SET character_set_client      = @saved_cs_client */;
/*!50001 SET character_set_results     = @saved_cs_results */;
/*!50001 SET collation_connection      = @saved_col_connection */;

--
-- Final view structure for view `fioofdepbyserv`
--

/*!50001 DROP VIEW IF EXISTS `fioofdepbyserv`*/;
/*!50001 SET @saved_cs_client          = @@character_set_client */;
/*!50001 SET @saved_cs_results         = @@character_set_results */;
/*!50001 SET @saved_col_connection     = @@collation_connection */;
/*!50001 SET character_set_client      = utf8mb4 */;
/*!50001 SET character_set_results     = utf8mb4 */;
/*!50001 SET collation_connection      = utf8mb4_0900_ai_ci */;
/*!50001 CREATE ALGORITHM=UNDEFINED */
/*!50013 DEFINER=`root`@`localhost` SQL SECURITY DEFINER */
/*!50001 VIEW `fioofdepbyserv` AS select `client`.`client` AS `client`,`client`.`client_short` AS `client_short`,`client`.`clientbirth` AS `clientbirth`,`client`.`ESRN` AS `ESRN`,`client`.`clientDeath` AS `clientDeath` from `client` where `client`.`id` in (select `client`.`id` from ((`main` join `client` on((`main`.`client_id` = `client`.`id`))) join `dep` on((`main`.`dep_id` = `dep`.`id`))) where (`main`.`cr_by` = `GET_wID`())) */;
/*!50001 SET character_set_client      = @saved_cs_client */;
/*!50001 SET character_set_results     = @saved_cs_results */;
/*!50001 SET collation_connection      = @saved_col_connection */;

--
-- Final view structure for view `fioofdepbyset`
--

/*!50001 DROP VIEW IF EXISTS `fioofdepbyset`*/;
/*!50001 SET @saved_cs_client          = @@character_set_client */;
/*!50001 SET @saved_cs_results         = @@character_set_results */;
/*!50001 SET @saved_col_connection     = @@collation_connection */;
/*!50001 SET character_set_client      = utf8mb4 */;
/*!50001 SET character_set_results     = utf8mb4 */;
/*!50001 SET collation_connection      = utf8mb4_0900_ai_ci */;
/*!50001 CREATE ALGORITHM=UNDEFINED */
/*!50013 DEFINER=`root`@`localhost` SQL SECURITY DEFINER */
/*!50001 VIEW `fioofdepbyset` AS select `client`.`client` AS `client`,`client`.`client_short` AS `client_short`,`client`.`clientbirth` AS `clientbirth`,`client`.`ESRN` AS `ESRN`,`client`.`clientDeath` AS `clientDeath` from `client` where `client`.`id` in (select `client`.`id` from ((`main` join `client` on((`main`.`client_id` = `client`.`id`))) join `dep` on((`main`.`dep_id` = `dep`.`id`))) where (`main`.`cr_by` = `GET_wID`())) */;
/*!50001 SET character_set_client      = @saved_cs_client */;
/*!50001 SET character_set_results     = @saved_cs_results */;
/*!50001 SET collation_connection      = @saved_col_connection */;

--
-- Final view structure for view `last_used_workers`
--

/*!50001 DROP VIEW IF EXISTS `last_used_workers`*/;
/*!50001 SET @saved_cs_client          = @@character_set_client */;
/*!50001 SET @saved_cs_results         = @@character_set_results */;
/*!50001 SET @saved_col_connection     = @@collation_connection */;
/*!50001 SET character_set_client      = utf8mb4 */;
/*!50001 SET character_set_results     = utf8mb4 */;
/*!50001 SET collation_connection      = utf8mb4_0900_ai_ci */;
/*!50001 CREATE ALGORITHM=UNDEFINED */
/*!50013 DEFINER=`root`@`localhost` SQL SECURITY DEFINER */
/*!50001 VIEW `last_used_workers` AS select `worker`.`id` AS `id`,`worker`.`worker` AS `worker` from (`worker` join `main` on((`worker`.`id` = `main`.`worker_id`))) where (`main`.`cr_by` = `GET_wID`()) group by `worker`.`id`,`worker`.`worker` order by `worker`.`worker` limit 30 */;
/*!50001 SET character_set_client      = @saved_cs_client */;
/*!50001 SET character_set_results     = @saved_cs_results */;
/*!50001 SET collation_connection      = @saved_col_connection */;

--
-- Final view structure for view `main_cprice`
--

/*!50001 DROP VIEW IF EXISTS `main_cprice`*/;
/*!50001 SET @saved_cs_client          = @@character_set_client */;
/*!50001 SET @saved_cs_results         = @@character_set_results */;
/*!50001 SET @saved_col_connection     = @@collation_connection */;
/*!50001 SET character_set_client      = utf8mb4 */;
/*!50001 SET character_set_results     = utf8mb4 */;
/*!50001 SET collation_connection      = utf8mb4_0900_ai_ci */;
/*!50001 CREATE ALGORITHM=UNDEFINED */
/*!50013 DEFINER=`root`@`localhost` SQL SECURITY DEFINER */
/*!50001 VIEW `main_cprice` AS select `f`.`id` AS `id`,`f`.`contracts_id` AS `contracts_id`,`f`.`dep_id` AS `dep_id`,`f`.`client_id` AS `client_id`,`f`.`serv_id` AS `serv_id`,`f`.`dep_has_worker_id` AS `dep_has_worker_id`,`f`.`worker_id` AS `worker_id`,`f`.`vdate` AS `vdate`,`f`.`quantity` AS `quantity`,`f`.`note` AS `note`,`f`.`create` AS `create`,`f`.`ts` AS `ts`,`f`.`cr_by` AS `cr_by`,`f`.`upd_by` AS `upd_by`,`f`.`reported` AS `reported`,`f`.`wdate` AS `wdate`,`f`.`overdid` AS `overdid`,`f`.`prev_quantity` AS `prev_quantity`,`f`.`perc` AS `perc`,`f`.`price` AS `price`,`f`.`price2` AS `price2`,`f`.`price3` AS `price3`,`f`.`servform_id` AS `servform_id`,((`f`.`perc` * `f`.`quantity`) * `f`.`price`) AS `to_pay`,((`f`.`perc` * `f`.`quantity`) * `f`.`price2`) AS `to_pay2` from (select `m`.`id` AS `id`,`m`.`contracts_id` AS `contracts_id`,`m`.`dep_id` AS `dep_id`,`m`.`client_id` AS `client_id`,`m`.`serv_id` AS `serv_id`,`m`.`dep_has_worker_id` AS `dep_has_worker_id`,`m`.`worker_id` AS `worker_id`,`m`.`vdate` AS `vdate`,`m`.`quantity` AS `quantity`,`m`.`note` AS `note`,`m`.`create` AS `create`,`m`.`ts` AS `ts`,`m`.`cr_by` AS `cr_by`,`m`.`upd_by` AS `upd_by`,`m`.`reported` AS `reported`,`m`.`wdate` AS `wdate`,`m`.`overdid` AS `overdid`,`m`.`prev_quantity` AS `prev_quantity`,(select `pd`.`perc` from `add_info` `pd` where ((`pd`.`pddate` <= `m`.`vdate`) and (`pd`.`contracts_id` = `m`.`contracts_id`)) order by `pd`.`pddate` desc limit 1) AS `perc`,`s`.`price` AS `price`,`s`.`price2` AS `price2`,`s`.`price3` AS `price3`,`r`.`servform_id` AS `servform_id` from (((`main` `m` join `serv` `s` on((`m`.`serv_id` = `s`.`id`))) join `contracts` `c` on((`m`.`contracts_id` = `c`.`id`))) left join `ripso` `r` on((`c`.`ripso_id` = `r`.`id`)))) `f` */;
/*!50001 SET character_set_client      = @saved_cs_client */;
/*!50001 SET character_set_results     = @saved_cs_results */;
/*!50001 SET collation_connection      = @saved_col_connection */;

--
-- Final view structure for view `main_nz`
--

/*!50001 DROP VIEW IF EXISTS `main_nz`*/;
/*!50001 SET @saved_cs_client          = @@character_set_client */;
/*!50001 SET @saved_cs_results         = @@character_set_results */;
/*!50001 SET @saved_col_connection     = @@collation_connection */;
/*!50001 SET character_set_client      = utf8mb4 */;
/*!50001 SET character_set_results     = utf8mb4 */;
/*!50001 SET collation_connection      = utf8mb4_0900_ai_ci */;
/*!50001 CREATE ALGORITHM=UNDEFINED */
/*!50013 DEFINER=`root`@`localhost` SQL SECURITY DEFINER */
/*!50001 VIEW `main_nz` AS select `main`.`id` AS `id`,`main`.`contracts_id` AS `contracts_id`,`main`.`dep_id` AS `dep_id`,`main`.`client_id` AS `client_id`,`main`.`serv_id` AS `serv_id`,`main`.`dep_has_worker_id` AS `dep_has_worker_id`,`main`.`worker_id` AS `worker_id`,`main`.`vdate` AS `vdate`,`main`.`quantity` AS `quantity`,`main`.`note` AS `note`,`main`.`create` AS `create`,`main`.`ts` AS `ts`,`main`.`cr_by` AS `cr_by`,`main`.`upd_by` AS `upd_by`,`main`.`reported` AS `reported`,`main`.`wdate` AS `wdate`,`main`.`overdid` AS `overdid`,`main`.`prev_quantity` AS `prev_quantity` from `main` where (`main`.`quantity` > 0) */;
/*!50001 SET character_set_client      = @saved_cs_client */;
/*!50001 SET character_set_results     = @saved_cs_results */;
/*!50001 SET collation_connection      = @saved_col_connection */;

--
-- Final view structure for view `max_pay_in_month`
--

/*!50001 DROP VIEW IF EXISTS `max_pay_in_month`*/;
/*!50001 SET @saved_cs_client          = @@character_set_client */;
/*!50001 SET @saved_cs_results         = @@character_set_results */;
/*!50001 SET @saved_col_connection     = @@collation_connection */;
/*!50001 SET character_set_client      = utf8mb4 */;
/*!50001 SET character_set_results     = utf8mb4 */;
/*!50001 SET collation_connection      = utf8mb4_0900_ai_ci */;
/*!50001 CREATE ALGORITHM=UNDEFINED */
/*!50013 DEFINER=`root`@`localhost` SQL SECURITY DEFINER */
/*!50001 VIEW `max_pay_in_month` AS select `d`.`contracts_id` AS `contracts_id`,`d`.`ripso_id` AS `ripso_id`,`d`.`pddate` AS `pddate`,`d`.`sdd` AS `sdd`,`d`.`servform_id` AS `servform_id`,`d`.`lm` AS `lm`,`d`.`perc` AS `perc`,`d`.`work_livemin` AS `work_livemin`,`d`.`client_id` AS `client_id`,(case when (`d`.`max_pay` >= 0) then `d`.`max_pay` when (`d`.`max_pay` < 0) then 0 else -(1) end) AS `max_pay`,`d`.`new_at` AS `new_at` from (select `t`.`contracts_id` AS `contracts_id`,`t`.`ripso_id` AS `ripso_id`,`t`.`pddate` AS `pddate`,`t`.`sdd` AS `sdd`,`t`.`servform_id` AS `servform_id`,`t`.`lm` AS `lm`,`t`.`perc` AS `perc`,`t`.`work_livemin` AS `work_livemin`,`t`.`client_id` AS `client_id`,(case when (`t`.`servform_id` in (1,2,3)) then ((`t`.`sdd` - (`t`.`lm` * 1.5)) / 2) when (`t`.`servform_id` = 4) then (`t`.`sdd` * 0.75) end) AS `max_pay`,(select `a`.`pddate` from (`add_info` `a` join `contracts` `c` on((`c`.`id` = `a`.`contracts_id`))) where ((`c`.`client_id` = `t`.`client_id`) and (`c`.`id` <> `t`.`contracts_id`) and (`a`.`pddate` > `t`.`pddate`)) order by `a`.`pddate` limit 1) AS `new_at` from (select `a`.`contracts_id` AS `contracts_id`,`c`.`ripso_id` AS `ripso_id`,`a`.`pddate` AS `pddate`,`a`.`sdd` AS `sdd`,`r`.`servform_id` AS `servform_id`,`a`.`perc` AS `perc`,`a`.`work_livemin` AS `work_livemin`,`c`.`client_id` AS `client_id`,(select if((`a`.`work_livemin` = 0),`live_min`.`live_min_p`,`live_min`.`live_min_w`) AS `live_min` from `live_min` where (`a`.`pddate` > `live_min`.`lmdate`) order by `live_min`.`lmdate` desc limit 1) AS `lm` from ((`add_info` `a` join `contracts` `c` on((`c`.`id` = `a`.`contracts_id`))) join `ripso` `r` on((`r`.`id` = `c`.`ripso_id`)))) `t` order by `t`.`pddate`) `d` */;
/*!50001 SET character_set_client      = @saved_cs_client */;
/*!50001 SET character_set_results     = @saved_cs_results */;
/*!50001 SET collation_connection      = @saved_col_connection */;

--
-- Final view structure for view `max_pay_in_month_50`
--

/*!50001 DROP VIEW IF EXISTS `max_pay_in_month_50`*/;
/*!50001 SET @saved_cs_client          = @@character_set_client */;
/*!50001 SET @saved_cs_results         = @@character_set_results */;
/*!50001 SET @saved_col_connection     = @@collation_connection */;
/*!50001 SET character_set_client      = utf8mb4 */;
/*!50001 SET character_set_results     = utf8mb4 */;
/*!50001 SET collation_connection      = utf8mb4_0900_ai_ci */;
/*!50001 CREATE ALGORITHM=UNDEFINED */
/*!50013 DEFINER=`root`@`localhost` SQL SECURITY DEFINER */
/*!50001 VIEW `max_pay_in_month_50` AS select `t`.`contracts_id` AS `contracts_id`,`t`.`ripso_id` AS `ripso_id`,`t`.`pddate` AS `pddate`,`t`.`sdd` AS `sdd`,`t`.`servform_id` AS `servform_id`,`t`.`lm` AS `lm`,((`t`.`sdd` - (`t`.`lm` * 1.5)) / 2) AS `max_pay` from (select `a`.`contracts_id` AS `contracts_id`,`c`.`ripso_id` AS `ripso_id`,`a`.`pddate` AS `pddate`,`a`.`sdd` AS `sdd`,`r`.`servform_id` AS `servform_id`,(select if((`a`.`work_livemin` = 0),`live_min`.`live_min_p`,`live_min`.`live_min_w`) AS `live_min` from `live_min` where (`a`.`pddate` > `live_min`.`lmdate`) order by `live_min`.`lmdate` desc limit 1) AS `lm` from ((`add_info` `a` join `contracts` `c` on((`c`.`id` = `a`.`contracts_id`))) join `ripso` `r` on((`r`.`id` = `c`.`ripso_id`))) where (`r`.`servform_id` in (1,2,3))) `t` order by `t`.`pddate` */;
/*!50001 SET character_set_client      = @saved_cs_client */;
/*!50001 SET character_set_results     = @saved_cs_results */;
/*!50001 SET collation_connection      = @saved_col_connection */;

--
-- Final view structure for view `max_pay_in_month_75`
--

/*!50001 DROP VIEW IF EXISTS `max_pay_in_month_75`*/;
/*!50001 SET @saved_cs_client          = @@character_set_client */;
/*!50001 SET @saved_cs_results         = @@character_set_results */;
/*!50001 SET @saved_col_connection     = @@collation_connection */;
/*!50001 SET character_set_client      = utf8mb4 */;
/*!50001 SET character_set_results     = utf8mb4 */;
/*!50001 SET collation_connection      = utf8mb4_0900_ai_ci */;
/*!50001 CREATE ALGORITHM=UNDEFINED */
/*!50013 DEFINER=`root`@`localhost` SQL SECURITY DEFINER */
/*!50001 VIEW `max_pay_in_month_75` AS select `t`.`contracts_id` AS `contracts_id`,`t`.`ripso_id` AS `ripso_id`,`t`.`pddate` AS `pddate`,`t`.`sdd` AS `sdd`,`t`.`servform_id` AS `servform_id`,`t`.`lm` AS `lm`,(`t`.`sdd` * 0.75) AS `max_pay` from (select `a`.`contracts_id` AS `contracts_id`,`c`.`ripso_id` AS `ripso_id`,`a`.`pddate` AS `pddate`,`a`.`sdd` AS `sdd`,`r`.`servform_id` AS `servform_id`,(select if((`a`.`work_livemin` = 0),`live_min`.`live_min_p`,`live_min`.`live_min_w`) AS `live_min` from `live_min` where (`a`.`pddate` > `live_min`.`lmdate`) order by `live_min`.`lmdate` desc limit 1) AS `lm` from ((`add_info` `a` join `contracts` `c` on((`c`.`id` = `a`.`contracts_id`))) join `ripso` `r` on((`r`.`id` = `c`.`ripso_id`))) where (`r`.`servform_id` = 4)) `t` order by `t`.`pddate` */;
/*!50001 SET character_set_client      = @saved_cs_client */;
/*!50001 SET character_set_results     = @saved_cs_results */;
/*!50001 SET collation_connection      = @saved_col_connection */;

--
-- Final view structure for view `servofripso`
--

/*!50001 DROP VIEW IF EXISTS `servofripso`*/;
/*!50001 SET @saved_cs_client          = @@character_set_client */;
/*!50001 SET @saved_cs_results         = @@character_set_results */;
/*!50001 SET @saved_col_connection     = @@collation_connection */;
/*!50001 SET character_set_client      = utf8mb4 */;
/*!50001 SET character_set_results     = utf8mb4 */;
/*!50001 SET collation_connection      = utf8mb4_0900_ai_ci */;
/*!50001 CREATE ALGORITHM=UNDEFINED */
/*!50013 DEFINER=`root`@`localhost` SQL SECURITY DEFINER */
/*!50001 VIEW `servofripso` AS select `s`.`id` AS `id`,`s`.`tnum` AS `tnum`,`s`.`serv` AS `serv`,`s`.`year` AS `year`,`s`.`sub_serv` AS `sub_serv`,`s`.`sub_serv_str` AS `sub_serv_str`,`s`.`price` AS `price`,`s`.`price2` AS `price2`,`s`.`price3` AS `price3`,`s`.`archive` AS `archive`,`s`.`total` AS `total`,`s`.`acronym` AS `acronym`,`s`.`workload` AS `workload`,`s`.`content` AS `content`,`r`.`id` AS `r_id`,`r`.`ripso` AS `ripso` from ((`ripso` `r` join `ripso_has_serv` `fr` on((`fr`.`ripso_id` = `r`.`id`))) join `serv` `s` on((`s`.`id` = `fr`.`ripso_id`))) where ((`s`.`archive` = 0) and (`r`.`archive` = 0)) */;
/*!50001 SET character_set_client      = @saved_cs_client */;
/*!50001 SET character_set_results     = @saved_cs_results */;
/*!50001 SET collation_connection      = @saved_col_connection */;

--
-- Final view structure for view `servofyear`
--

/*!50001 DROP VIEW IF EXISTS `servofyear`*/;
/*!50001 SET @saved_cs_client          = @@character_set_client */;
/*!50001 SET @saved_cs_results         = @@character_set_results */;
/*!50001 SET @saved_col_connection     = @@collation_connection */;
/*!50001 SET character_set_client      = utf8mb4 */;
/*!50001 SET character_set_results     = utf8mb4 */;
/*!50001 SET collation_connection      = utf8mb4_0900_ai_ci */;
/*!50001 CREATE ALGORITHM=UNDEFINED */
/*!50013 DEFINER=`root`@`localhost` SQL SECURITY DEFINER */
/*!50001 VIEW `servofyear` AS select `m`.`id` AS `id`,`m`.`contracts_id` AS `contracts_id`,`m`.`dep_id` AS `dep_id`,`m`.`client_id` AS `client_id`,`m`.`serv_id` AS `serv_id`,`m`.`dep_has_worker_id` AS `dep_has_worker_id`,`m`.`worker_id` AS `worker_id`,`m`.`vdate` AS `vdate`,`m`.`quantity` AS `quantity`,`m`.`note` AS `note`,`m`.`create` AS `create`,`m`.`ts` AS `ts`,`m`.`cr_by` AS `cr_by`,`m`.`upd_by` AS `upd_by`,`m`.`reported` AS `reported`,`m`.`wdate` AS `wdate`,`m`.`overdid` AS `overdid`,`m`.`prev_quantity` AS `prev_quantity` from `main` `m` where (year(`m`.`vdate`) = year(curdate())) */;
/*!50001 SET character_set_client      = @saved_cs_client */;
/*!50001 SET character_set_results     = @saved_cs_results */;
/*!50001 SET collation_connection      = @saved_col_connection */;

--
-- Final view structure for view `should_perc`
--

/*!50001 DROP VIEW IF EXISTS `should_perc`*/;
/*!50001 SET @saved_cs_client          = @@character_set_client */;
/*!50001 SET @saved_cs_results         = @@character_set_results */;
/*!50001 SET @saved_col_connection     = @@collation_connection */;
/*!50001 SET character_set_client      = utf8mb4 */;
/*!50001 SET character_set_results     = utf8mb4 */;
/*!50001 SET collation_connection      = utf8mb4_0900_ai_ci */;
/*!50001 CREATE ALGORITHM=UNDEFINED */
/*!50013 DEFINER=`root`@`localhost` SQL SECURITY DEFINER */
/*!50001 VIEW `should_perc` AS select `t`.`contracts_id` AS `contracts_id`,`t`.`pddate` AS `pddate`,`t`.`ripso_id` AS `ripso_id`,`t`.`sdd` AS `sdd`,`t`.`servform_id` AS `servform_id`,`t`.`lm` AS `lm`,`t`.`category_id` AS `category_id`,`t`.`perc` AS `perc`,(case when (`t`.`category_id` = 5) then (case when (`t`.`servform_id` = 4) then 0.10 else 0.5 end) else (case when (`t`.`servform_id` = 4) then 0.35 else (case when ((`t`.`sdd` - (`t`.`lm` * 4)) > 0) then 0.4 when ((`t`.`sdd` - (`t`.`lm` * 3)) > 0) then 0.3 when ((`t`.`sdd` - (`t`.`lm` * 2.5)) > 0) then 0.2 when ((`t`.`sdd` - (`t`.`lm` * 2)) > 0) then 0.15 when ((`t`.`sdd` - (`t`.`lm` * 1.5)) > 0) then 0.1 else 0 end) end) end) AS `should_perc` from (select `a`.`contracts_id` AS `contracts_id`,`c`.`ripso_id` AS `ripso_id`,`a`.`pddate` AS `pddate`,`a`.`sdd` AS `sdd`,`r`.`servform_id` AS `servform_id`,`uhc`.`category_id` AS `category_id`,`a`.`perc` AS `perc`,(select if((`a`.`work_livemin` = 0),`live_min`.`live_min_p`,`live_min`.`live_min_w`) AS `live_min` from `live_min` where (`a`.`pddate` > `live_min`.`lmdate`) order by `live_min`.`lmdate` desc limit 1) AS `lm` from ((((`add_info` `a` left join `contracts` `c` on((`c`.`id` = `a`.`contracts_id`))) left join `ripso` `r` on((`r`.`id` = `c`.`ripso_id`))) left join `client` `u` on((`u`.`id` = `c`.`client_id`))) left join `client_has_category` `uhc` on(((`uhc`.`client_id` = `c`.`client_id`) and (`uhc`.`get_date` < `a`.`pddate`) and (`uhc`.`category_id` = 5))))) `t` order by `t`.`pddate` */;
/*!50001 SET character_set_client      = @saved_cs_client */;
/*!50001 SET character_set_results     = @saved_cs_results */;
/*!50001 SET collation_connection      = @saved_col_connection */;

--
-- Final view structure for view `total_cprice_in_month`
--

/*!50001 DROP VIEW IF EXISTS `total_cprice_in_month`*/;
/*!50001 SET @saved_cs_client          = @@character_set_client */;
/*!50001 SET @saved_cs_results         = @@character_set_results */;
/*!50001 SET @saved_col_connection     = @@collation_connection */;
/*!50001 SET character_set_client      = utf8mb4 */;
/*!50001 SET character_set_results     = utf8mb4 */;
/*!50001 SET collation_connection      = utf8mb4_0900_ai_ci */;
/*!50001 CREATE ALGORITHM=UNDEFINED */
/*!50013 DEFINER=`root`@`localhost` SQL SECURITY DEFINER */
/*!50001 VIEW `total_cprice_in_month` AS select `main_cprice`.`contracts_id` AS `contracts_id`,sum(`main_cprice`.`to_pay`) AS `SUM(to_pay)` from `main_cprice` group by month(`main_cprice`.`vdate`),year(`main_cprice`.`vdate`) */;
/*!50001 SET character_set_client      = @saved_cs_client */;
/*!50001 SET character_set_results     = @saved_cs_results */;
/*!50001 SET collation_connection      = @saved_col_connection */;

--
-- Final view structure for view `upd_by`
--

/*!50001 DROP VIEW IF EXISTS `upd_by`*/;
/*!50001 SET @saved_cs_client          = @@character_set_client */;
/*!50001 SET @saved_cs_results         = @@character_set_results */;
/*!50001 SET @saved_col_connection     = @@collation_connection */;
/*!50001 SET character_set_client      = utf8mb4 */;
/*!50001 SET character_set_results     = utf8mb4 */;
/*!50001 SET collation_connection      = utf8mb4_0900_ai_ci */;
/*!50001 CREATE ALGORITHM=UNDEFINED */
/*!50013 DEFINER=`root`@`localhost` SQL SECURITY DEFINER */
/*!50001 VIEW `upd_by` AS select `worker`.`id` AS `id`,`worker`.`worker` AS `upd_by`,`worker`.`user` AS `user`,`worker`.`note` AS `note`,`worker`.`role_id` AS `role_id`,`worker`.`dep_id` AS `dep_id`,`worker`.`archive` AS `archive` from `worker` */;
/*!50001 SET character_set_client      = @saved_cs_client */;
/*!50001 SET character_set_results     = @saved_cs_results */;
/*!50001 SET collation_connection      = @saved_col_connection */;

--
-- Final view structure for view `updatable_2__dep_has_client`
--

/*!50001 DROP VIEW IF EXISTS `updatable_2__dep_has_client`*/;
/*!50001 SET @saved_cs_client          = @@character_set_client */;
/*!50001 SET @saved_cs_results         = @@character_set_results */;
/*!50001 SET @saved_col_connection     = @@collation_connection */;
/*!50001 SET character_set_client      = utf8mb4 */;
/*!50001 SET character_set_results     = utf8mb4 */;
/*!50001 SET collation_connection      = utf8mb4_0900_ai_ci */;
/*!50001 CREATE ALGORITHM=UNDEFINED */
/*!50013 DEFINER=`root`@`localhost` SQL SECURITY DEFINER */
/*!50001 VIEW `updatable_2__dep_has_client` AS select `u`.`id` AS `id`,`u`.`client` AS `client`,`u`.`client_short` AS `client_short`,`u`.`clientDeath` AS `clientDeath`,`u`.`clientbirth` AS `clientbirth`,`u`.`ESRN` AS `ESRN`,`u`.`note` AS `note`,`u`.`phone` AS `phone`,`u`.`snils` AS `snils`,`u`.`curator` AS `curator`,`u`.`create` AS `create`,`u`.`ts` AS `ts`,`u`.`cr_by` AS `cr_by`,`u`.`upd_by` AS `upd_by`,`u`.`cr_dep_id` AS `cr_dep_id` from `client` `u` where `u`.`cr_dep_id` in (select `_active_dep`.`id` from `_active_dep`) */;
/*!50001 SET character_set_client      = @saved_cs_client */;
/*!50001 SET character_set_results     = @saved_cs_results */;
/*!50001 SET collation_connection      = @saved_col_connection */;

--
-- Final view structure for view `updatable__contr_has_add_info`
--

/*!50001 DROP VIEW IF EXISTS `updatable__contr_has_add_info`*/;
/*!50001 SET @saved_cs_client          = @@character_set_client */;
/*!50001 SET @saved_cs_results         = @@character_set_results */;
/*!50001 SET @saved_col_connection     = @@collation_connection */;
/*!50001 SET character_set_client      = utf8mb4 */;
/*!50001 SET character_set_results     = utf8mb4 */;
/*!50001 SET collation_connection      = utf8mb4_0900_ai_ci */;
/*!50001 CREATE ALGORITHM=UNDEFINED */
/*!50013 DEFINER=`root`@`localhost` SQL SECURITY DEFINER */
/*!50001 VIEW `updatable__contr_has_add_info` AS select `_contr_has_add_info`.`pddate` AS `pddate`,`_contr_has_add_info`.`contracts_id` AS `contracts_id`,`_contr_has_add_info`.`predv_money` AS `predv_money`,`_contr_has_add_info`.`curFIO` AS `curFIO`,`_contr_has_add_info`.`psp` AS `psp`,`_contr_has_add_info`.`address` AS `address`,`_contr_has_add_info`.`sdd` AS `sdd`,`_contr_has_add_info`.`sdd_date` AS `sdd_date`,`_contr_has_add_info`.`perc` AS `perc`,`_contr_has_add_info`.`not_standart_contract` AS `not_standart_contract`,`_contr_has_add_info`.`not_standart_act` AS `not_standart_act`,`_contr_has_add_info`.`note` AS `note`,`_contr_has_add_info`.`create` AS `create`,`_contr_has_add_info`.`ts` AS `ts`,`_contr_has_add_info`.`cr_by` AS `cr_by`,`_contr_has_add_info`.`upd_by` AS `upd_by`,`_contr_has_add_info`.`repr_FIO` AS `repr_FIO`,`_contr_has_add_info`.`repr_addr` AS `repr_addr`,`_contr_has_add_info`.`repr_psp` AS `repr_psp`,`_contr_has_add_info`.`work_livemin` AS `work_livemin` from `_contr_has_add_info` */;
/*!50001 SET character_set_client      = @saved_cs_client */;
/*!50001 SET character_set_results     = @saved_cs_results */;
/*!50001 SET collation_connection      = @saved_col_connection */;

--
-- Final view structure for view `updatable__dep_has_add_info`
--

/*!50001 DROP VIEW IF EXISTS `updatable__dep_has_add_info`*/;
/*!50001 SET @saved_cs_client          = @@character_set_client */;
/*!50001 SET @saved_cs_results         = @@character_set_results */;
/*!50001 SET @saved_col_connection     = @@collation_connection */;
/*!50001 SET character_set_client      = utf8mb4 */;
/*!50001 SET character_set_results     = utf8mb4 */;
/*!50001 SET collation_connection      = utf8mb4_0900_ai_ci */;
/*!50001 CREATE ALGORITHM=UNDEFINED */
/*!50013 DEFINER=`root`@`localhost` SQL SECURITY DEFINER */
/*!50001 VIEW `updatable__dep_has_add_info` AS select `ai`.`pddate` AS `pddate`,`ai`.`contracts_id` AS `contracts_id`,`ai`.`predv_money` AS `predv_money`,`ai`.`curFIO` AS `curFIO`,`ai`.`psp` AS `psp`,`ai`.`address` AS `address`,`ai`.`sdd` AS `sdd`,`ai`.`sdd_date` AS `sdd_date`,`ai`.`perc` AS `perc`,`ai`.`not_standart_contract` AS `not_standart_contract`,`ai`.`not_standart_act` AS `not_standart_act`,`ai`.`note` AS `note`,`ai`.`create` AS `create`,`ai`.`ts` AS `ts`,`ai`.`cr_by` AS `cr_by`,`ai`.`upd_by` AS `upd_by`,`ai`.`repr_FIO` AS `repr_FIO`,`ai`.`repr_addr` AS `repr_addr`,`ai`.`repr_psp` AS `repr_psp`,`ai`.`work_livemin` AS `work_livemin` from (`add_info` `ai` join `contracts` `c` on((`c`.`id` = `ai`.`contracts_id`))) where `c`.`dep_id` in (select `_active_dep`.`id` from `_active_dep`) */;
/*!50001 SET character_set_client      = @saved_cs_client */;
/*!50001 SET character_set_results     = @saved_cs_results */;
/*!50001 SET collation_connection      = @saved_col_connection */;

--
-- Final view structure for view `updatable__dep_has_client`
--

/*!50001 DROP VIEW IF EXISTS `updatable__dep_has_client`*/;
/*!50001 SET @saved_cs_client          = @@character_set_client */;
/*!50001 SET @saved_cs_results         = @@character_set_results */;
/*!50001 SET @saved_col_connection     = @@collation_connection */;
/*!50001 SET character_set_client      = utf8mb4 */;
/*!50001 SET character_set_results     = utf8mb4 */;
/*!50001 SET collation_connection      = utf8mb4_0900_ai_ci */;
/*!50001 CREATE ALGORITHM=UNDEFINED */
/*!50013 DEFINER=`root`@`localhost` SQL SECURITY DEFINER */
/*!50001 VIEW `updatable__dep_has_client` AS select `u`.`id` AS `id`,`u`.`client` AS `client`,`u`.`client_short` AS `client_short`,`u`.`clientDeath` AS `clientDeath`,`u`.`clientbirth` AS `clientbirth`,`u`.`ESRN` AS `ESRN`,`u`.`note` AS `note`,`u`.`phone` AS `phone`,`u`.`snils` AS `snils`,`u`.`curator` AS `curator`,`u`.`create` AS `create`,`u`.`ts` AS `ts`,`u`.`cr_by` AS `cr_by`,`u`.`upd_by` AS `upd_by`,`u`.`cr_dep_id` AS `cr_dep_id` from (`client` `u` join `contracts` `c` on((`c`.`client_id` = `u`.`id`))) where `c`.`dep_id` in (select `_active_dep`.`id` from `_active_dep`) */;
/*!50001 SET character_set_client      = @saved_cs_client */;
/*!50001 SET character_set_results     = @saved_cs_results */;
/*!50001 SET collation_connection      = @saved_col_connection */;

--
-- Final view structure for view `updatable__dep_has_contracts`
--

/*!50001 DROP VIEW IF EXISTS `updatable__dep_has_contracts`*/;
/*!50001 SET @saved_cs_client          = @@character_set_client */;
/*!50001 SET @saved_cs_results         = @@character_set_results */;
/*!50001 SET @saved_col_connection     = @@collation_connection */;
/*!50001 SET character_set_client      = utf8mb4 */;
/*!50001 SET character_set_results     = utf8mb4 */;
/*!50001 SET collation_connection      = utf8mb4_0900_ai_ci */;
/*!50001 CREATE ALGORITHM=UNDEFINED */
/*!50013 DEFINER=`root`@`localhost` SQL SECURITY DEFINER */
/*!50001 VIEW `updatable__dep_has_contracts` AS select `c`.`id` AS `id`,`c`.`contracts` AS `contracts`,`c`.`contracts2` AS `contracts2`,`c`.`client_id` AS `client_id`,`c`.`dep_id` AS `dep_id`,`c`.`ripso_id` AS `ripso_id`,`c`.`blocked` AS `blocked`,`c`.`startdate` AS `startdate`,`c`.`enddate` AS `enddate`,`c`.`ippsuNum` AS `ippsuNum`,`c`.`note` AS `note`,`c`.`create` AS `create`,`c`.`ts` AS `ts`,`c`.`cr_by` AS `cr_by`,`c`.`upd_by` AS `upd_by`,`c`.`to_recheck` AS `to_recheck`,`c`.`check_date` AS `check_date`,`c`.`pyc_prim` AS `pyc_prim` from `contracts` `c` where `c`.`dep_id` in (select `_active_dep`.`id` from `_active_dep`) */;
/*!50001 SET character_set_client      = @saved_cs_client */;
/*!50001 SET character_set_results     = @saved_cs_results */;
/*!50001 SET collation_connection      = @saved_col_connection */;

--
-- Final view structure for view `updatable__dep_has_main`
--

/*!50001 DROP VIEW IF EXISTS `updatable__dep_has_main`*/;
/*!50001 SET @saved_cs_client          = @@character_set_client */;
/*!50001 SET @saved_cs_results         = @@character_set_results */;
/*!50001 SET @saved_col_connection     = @@collation_connection */;
/*!50001 SET character_set_client      = utf8mb4 */;
/*!50001 SET character_set_results     = utf8mb4 */;
/*!50001 SET collation_connection      = utf8mb4_0900_ai_ci */;
/*!50001 CREATE ALGORITHM=UNDEFINED */
/*!50013 DEFINER=`root`@`localhost` SQL SECURITY DEFINER */
/*!50001 VIEW `updatable__dep_has_main` AS select `main`.`id` AS `id`,`main`.`contracts_id` AS `contracts_id`,`main`.`dep_id` AS `dep_id`,`main`.`client_id` AS `client_id`,`main`.`serv_id` AS `serv_id`,`main`.`dep_has_worker_id` AS `dep_has_worker_id`,`main`.`worker_id` AS `worker_id`,`main`.`vdate` AS `vdate`,`main`.`quantity` AS `quantity`,`main`.`note` AS `note`,`main`.`create` AS `create`,`main`.`ts` AS `ts`,`main`.`cr_by` AS `cr_by`,`main`.`upd_by` AS `upd_by`,`main`.`reported` AS `reported`,`main`.`wdate` AS `wdate`,`main`.`overdid` AS `overdid`,`main`.`prev_quantity` AS `prev_quantity` from `main` where `main`.`dep_id` in (select `_active_dep`.`id` from `_active_dep`) */;
/*!50001 SET character_set_client      = @saved_cs_client */;
/*!50001 SET character_set_results     = @saved_cs_results */;
/*!50001 SET collation_connection      = @saved_col_connection */;

--
-- Final view structure for view `updatable__user_has_main`
--

/*!50001 DROP VIEW IF EXISTS `updatable__user_has_main`*/;
/*!50001 SET @saved_cs_client          = @@character_set_client */;
/*!50001 SET @saved_cs_results         = @@character_set_results */;
/*!50001 SET @saved_col_connection     = @@collation_connection */;
/*!50001 SET character_set_client      = utf8mb4 */;
/*!50001 SET character_set_results     = utf8mb4 */;
/*!50001 SET collation_connection      = utf8mb4_0900_ai_ci */;
/*!50001 CREATE ALGORITHM=UNDEFINED */
/*!50013 DEFINER=`root`@`localhost` SQL SECURITY DEFINER */
/*!50001 VIEW `updatable__user_has_main` AS select `main`.`id` AS `id`,`main`.`contracts_id` AS `contracts_id`,`main`.`dep_id` AS `dep_id`,`main`.`client_id` AS `client_id`,`main`.`serv_id` AS `serv_id`,`main`.`dep_has_worker_id` AS `dep_has_worker_id`,`main`.`worker_id` AS `worker_id`,`main`.`vdate` AS `vdate`,`main`.`quantity` AS `quantity`,`main`.`note` AS `note`,`main`.`create` AS `create`,`main`.`ts` AS `ts`,`main`.`cr_by` AS `cr_by`,`main`.`upd_by` AS `upd_by`,`main`.`reported` AS `reported`,`main`.`wdate` AS `wdate`,`main`.`overdid` AS `overdid`,`main`.`prev_quantity` AS `prev_quantity` from `main` where ((`main`.`cr_by` = `GET_WID`()) or (`main`.`upd_by` = `GET_WID`())) order by `main`.`ts` desc */;
/*!50001 SET character_set_client      = @saved_cs_client */;
/*!50001 SET character_set_results     = @saved_cs_results */;
/*!50001 SET collation_connection      = @saved_col_connection */;

--
-- Final view structure for view `updatable_add_info`
--

/*!50001 DROP VIEW IF EXISTS `updatable_add_info`*/;
/*!50001 SET @saved_cs_client          = @@character_set_client */;
/*!50001 SET @saved_cs_results         = @@character_set_results */;
/*!50001 SET @saved_col_connection     = @@collation_connection */;
/*!50001 SET character_set_client      = utf8mb4 */;
/*!50001 SET character_set_results     = utf8mb4 */;
/*!50001 SET collation_connection      = utf8mb4_0900_ai_ci */;
/*!50001 CREATE ALGORITHM=UNDEFINED */
/*!50013 DEFINER=`root`@`localhost` SQL SECURITY DEFINER */
/*!50001 VIEW `updatable_add_info` AS select `add_info`.`pddate` AS `pddate`,`add_info`.`contracts_id` AS `contracts_id`,`add_info`.`predv_money` AS `predv_money`,`add_info`.`curFIO` AS `curFIO`,`add_info`.`psp` AS `psp`,`add_info`.`address` AS `address`,`add_info`.`sdd` AS `sdd`,`add_info`.`sdd_date` AS `sdd_date`,`add_info`.`perc` AS `perc`,`add_info`.`not_standart_contract` AS `not_standart_contract`,`add_info`.`not_standart_act` AS `not_standart_act`,`add_info`.`note` AS `note`,`add_info`.`create` AS `create`,`add_info`.`ts` AS `ts`,`add_info`.`cr_by` AS `cr_by`,`add_info`.`upd_by` AS `upd_by`,`add_info`.`repr_FIO` AS `repr_FIO`,`add_info`.`repr_addr` AS `repr_addr`,`add_info`.`repr_psp` AS `repr_psp`,`add_info`.`work_livemin` AS `work_livemin` from `add_info` */;
/*!50001 SET character_set_client      = @saved_cs_client */;
/*!50001 SET character_set_results     = @saved_cs_results */;
/*!50001 SET collation_connection      = @saved_col_connection */;

--
-- Final view structure for view `updatable_client`
--

/*!50001 DROP VIEW IF EXISTS `updatable_client`*/;
/*!50001 SET @saved_cs_client          = @@character_set_client */;
/*!50001 SET @saved_cs_results         = @@character_set_results */;
/*!50001 SET @saved_col_connection     = @@collation_connection */;
/*!50001 SET character_set_client      = utf8mb4 */;
/*!50001 SET character_set_results     = utf8mb4 */;
/*!50001 SET collation_connection      = utf8mb4_0900_ai_ci */;
/*!50001 CREATE ALGORITHM=UNDEFINED */
/*!50013 DEFINER=`root`@`localhost` SQL SECURITY DEFINER */
/*!50001 VIEW `updatable_client` AS select `client`.`id` AS `id`,`client`.`client` AS `client`,`client`.`client_short` AS `client_short`,`client`.`clientDeath` AS `clientDeath`,`client`.`clientbirth` AS `clientbirth`,`client`.`ESRN` AS `ESRN`,`client`.`note` AS `note`,`client`.`phone` AS `phone`,`client`.`snils` AS `snils`,`client`.`curator` AS `curator`,`client`.`create` AS `create`,`client`.`ts` AS `ts`,`client`.`cr_by` AS `cr_by`,`client`.`upd_by` AS `upd_by`,`client`.`cr_dep_id` AS `cr_dep_id` from `client` */;
/*!50001 SET character_set_client      = @saved_cs_client */;
/*!50001 SET character_set_results     = @saved_cs_results */;
/*!50001 SET collation_connection      = @saved_col_connection */;

--
-- Final view structure for view `updatable_contracts`
--

/*!50001 DROP VIEW IF EXISTS `updatable_contracts`*/;
/*!50001 SET @saved_cs_client          = @@character_set_client */;
/*!50001 SET @saved_cs_results         = @@character_set_results */;
/*!50001 SET @saved_col_connection     = @@collation_connection */;
/*!50001 SET character_set_client      = utf8mb4 */;
/*!50001 SET character_set_results     = utf8mb4 */;
/*!50001 SET collation_connection      = utf8mb4_0900_ai_ci */;
/*!50001 CREATE ALGORITHM=UNDEFINED */
/*!50013 DEFINER=`root`@`localhost` SQL SECURITY DEFINER */
/*!50001 VIEW `updatable_contracts` AS select `contracts`.`id` AS `id`,`contracts`.`contracts` AS `contracts`,`contracts`.`contracts2` AS `contracts2`,`contracts`.`client_id` AS `client_id`,`contracts`.`dep_id` AS `dep_id`,`contracts`.`ripso_id` AS `ripso_id`,`contracts`.`blocked` AS `blocked`,`contracts`.`startdate` AS `startdate`,`contracts`.`enddate` AS `enddate`,`contracts`.`ippsuNum` AS `ippsuNum`,`contracts`.`note` AS `note`,`contracts`.`create` AS `create`,`contracts`.`ts` AS `ts`,`contracts`.`cr_by` AS `cr_by`,`contracts`.`upd_by` AS `upd_by`,`contracts`.`to_recheck` AS `to_recheck`,`contracts`.`check_date` AS `check_date`,`contracts`.`pyc_prim` AS `pyc_prim` from `contracts` */;
/*!50001 SET character_set_client      = @saved_cs_client */;
/*!50001 SET character_set_results     = @saved_cs_results */;
/*!50001 SET collation_connection      = @saved_col_connection */;

--
-- Final view structure for view `updatable_contracts_has_serv`
--

/*!50001 DROP VIEW IF EXISTS `updatable_contracts_has_serv`*/;
/*!50001 SET @saved_cs_client          = @@character_set_client */;
/*!50001 SET @saved_cs_results         = @@character_set_results */;
/*!50001 SET @saved_col_connection     = @@collation_connection */;
/*!50001 SET character_set_client      = utf8mb4 */;
/*!50001 SET character_set_results     = utf8mb4 */;
/*!50001 SET collation_connection      = utf8mb4_0900_ai_ci */;
/*!50001 CREATE ALGORITHM=UNDEFINED */
/*!50013 DEFINER=`root`@`localhost` SQL SECURITY DEFINER */
/*!50001 VIEW `updatable_contracts_has_serv` AS select `contracts_has_serv`.`serv_id` AS `serv_id`,`contracts_has_serv`.`contracts_id` AS `contracts_id`,`contracts_has_serv`.`planned` AS `planned`,`contracts_has_serv`.`filled` AS `filled`,`contracts_has_serv`.`note` AS `note`,`contracts_has_serv`.`archive` AS `archive`,`contracts_has_serv`.`create` AS `create`,`contracts_has_serv`.`ts` AS `ts`,`contracts_has_serv`.`cr_by` AS `cr_by`,`contracts_has_serv`.`upd_by` AS `upd_by`,`contracts_has_serv`.`to_recheck` AS `to_recheck`,`contracts_has_serv`.`check_date` AS `check_date`,`contracts_has_serv`.`filled_old` AS `filled_old` from `contracts_has_serv` */;
/*!50001 SET character_set_client      = @saved_cs_client */;
/*!50001 SET character_set_results     = @saved_cs_results */;
/*!50001 SET collation_connection      = @saved_col_connection */;

--
-- Final view structure for view `updatable_main`
--

/*!50001 DROP VIEW IF EXISTS `updatable_main`*/;
/*!50001 SET @saved_cs_client          = @@character_set_client */;
/*!50001 SET @saved_cs_results         = @@character_set_results */;
/*!50001 SET @saved_col_connection     = @@collation_connection */;
/*!50001 SET character_set_client      = utf8mb4 */;
/*!50001 SET character_set_results     = utf8mb4 */;
/*!50001 SET collation_connection      = utf8mb4_0900_ai_ci */;
/*!50001 CREATE ALGORITHM=UNDEFINED */
/*!50013 DEFINER=`root`@`localhost` SQL SECURITY DEFINER */
/*!50001 VIEW `updatable_main` AS select `main`.`id` AS `id`,`main`.`contracts_id` AS `contracts_id`,`main`.`dep_id` AS `dep_id`,`main`.`client_id` AS `client_id`,`main`.`serv_id` AS `serv_id`,`main`.`dep_has_worker_id` AS `dep_has_worker_id`,`main`.`worker_id` AS `worker_id`,`main`.`vdate` AS `vdate`,`main`.`quantity` AS `quantity`,`main`.`note` AS `note`,`main`.`create` AS `create`,`main`.`ts` AS `ts`,`main`.`cr_by` AS `cr_by`,`main`.`upd_by` AS `upd_by`,`main`.`reported` AS `reported`,`main`.`wdate` AS `wdate`,`main`.`overdid` AS `overdid`,`main`.`prev_quantity` AS `prev_quantity` from `main` */;
/*!50001 SET character_set_client      = @saved_cs_client */;
/*!50001 SET character_set_results     = @saved_cs_results */;
/*!50001 SET collation_connection      = @saved_col_connection */;

--
-- Final view structure for view `user_has_serv`
--

/*!50001 DROP VIEW IF EXISTS `user_has_serv`*/;
/*!50001 SET @saved_cs_client          = @@character_set_client */;
/*!50001 SET @saved_cs_results         = @@character_set_results */;
/*!50001 SET @saved_col_connection     = @@collation_connection */;
/*!50001 SET character_set_client      = utf8mb4 */;
/*!50001 SET character_set_results     = utf8mb4 */;
/*!50001 SET collation_connection      = utf8mb4_0900_ai_ci */;
/*!50001 CREATE ALGORITHM=UNDEFINED */
/*!50013 DEFINER=`root`@`localhost` SQL SECURITY DEFINER */
/*!50001 VIEW `user_has_serv` AS select `main`.`id` AS `id`,`main`.`contracts_id` AS `contracts_id`,`main`.`dep_id` AS `dep_id`,`main`.`client_id` AS `client_id`,`main`.`serv_id` AS `serv_id`,`main`.`dep_has_worker_id` AS `dep_has_worker_id`,`main`.`worker_id` AS `worker_id`,`main`.`vdate` AS `vdate`,`main`.`quantity` AS `quantity`,`main`.`note` AS `note`,`main`.`create` AS `create`,`main`.`ts` AS `ts`,`main`.`cr_by` AS `cr_by`,`main`.`upd_by` AS `upd_by`,`main`.`reported` AS `reported`,`main`.`wdate` AS `wdate`,`main`.`overdid` AS `overdid`,`main`.`prev_quantity` AS `prev_quantity` from `main` where (`main`.`cr_by` = `GET_wID`()) */;
/*!50001 SET character_set_client      = @saved_cs_client */;
/*!50001 SET character_set_results     = @saved_cs_results */;
/*!50001 SET collation_connection      = @saved_col_connection */;

--
-- Final view structure for view `worker_has_dep`
--

/*!50001 DROP VIEW IF EXISTS `worker_has_dep`*/;
/*!50001 SET @saved_cs_client          = @@character_set_client */;
/*!50001 SET @saved_cs_results         = @@character_set_results */;
/*!50001 SET @saved_col_connection     = @@collation_connection */;
/*!50001 SET character_set_client      = utf8mb4 */;
/*!50001 SET character_set_results     = utf8mb4 */;
/*!50001 SET collation_connection      = utf8mb4_0900_ai_ci */;
/*!50001 CREATE ALGORITHM=UNDEFINED */
/*!50013 DEFINER=`root`@`localhost` SQL SECURITY DEFINER */
/*!50001 VIEW `worker_has_dep` AS select `dw`.`dep_id` AS `id`,`d`.`dep` AS `dep` from ((`dep_has_worker` `dw` join `dep` `d` on((`d`.`id` = `dw`.`dep_id`))) join `worker` `w` on((`dw`.`worker_id` = `w`.`id`))) where ((`dw`.`worker_id` = `GET_wID`()) and (`dw`.`archive` = 0)) */;
/*!50001 SET character_set_client      = @saved_cs_client */;
/*!50001 SET character_set_results     = @saved_cs_results */;
/*!50001 SET collation_connection      = @saved_col_connection */;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2022-03-10 17:15:36
