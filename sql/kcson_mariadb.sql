-- MySQL Workbench Forward Engineering

SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0;
SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0;
SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='ONLY_FULL_GROUP_BY,STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_ENGINE_SUBSTITUTION';

-- -----------------------------------------------------
-- Schema kcson
-- -----------------------------------------------------
DROP SCHEMA IF EXISTS `kcson` ;

-- -----------------------------------------------------
-- Schema kcson
-- -----------------------------------------------------
CREATE SCHEMA IF NOT EXISTS `kcson` DEFAULT CHARACTER SET utf8mb4  ;
USE `kcson` ;

-- -----------------------------------------------------
-- Table `kcson`.`dep`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `kcson`.`dep` ;

CREATE TABLE IF NOT EXISTS `kcson`.`dep` (
  `id` INT UNSIGNED NOT NULL AUTO_INCREMENT,
  `dep` VARCHAR(45) NOT NULL,
  `dep_full_name` VARCHAR(255) NULL,
  `dep_puname` VARCHAR(255) NULL,
  `note` VARCHAR(255) NULL DEFAULT NULL,
  `archive` TINYINT NULL DEFAULT 0,
  `complex_dep_id` INT UNSIGNED NULL DEFAULT 0,
  PRIMARY KEY (`id`),
  UNIQUE INDEX `dep_UNIQUE` (`dep` ASC) )
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8mb4

COMMENT = 'Departments';


-- -----------------------------------------------------
-- Table `kcson`.`serv`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `kcson`.`serv` ;

CREATE TABLE IF NOT EXISTS `kcson`.`serv` (
  `id` INT UNSIGNED NOT NULL AUTO_INCREMENT,
  `tnum` VARCHAR(10) NOT NULL COMMENT 'короткое имя услуги',
  `serv` VARCHAR(1000) NULL DEFAULT NULL,
  `year` YEAR(4) NOT NULL,
  `sub_serv` INT NULL DEFAULT NULL,
  `sub_serv_str` VARCHAR(10) NULL DEFAULT NULL,
  `price` DECIMAL(10,2) NULL,
  `price2` DECIMAL(10,2) NULL,
  `price3` DECIMAL(10,2) NULL,
  `archive` TINYINT NULL DEFAULT 0,
  `total` TINYINT NULL DEFAULT 0,
  `acronym` VARCHAR(45) NULL,
  `workload` INT NULL,
  `content` VARCHAR(1000) NULL,
  PRIMARY KEY (`id`),
  UNIQUE INDEX `serv_num_UNIQUE` (`tnum` ASC) )
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8mb4
;


-- -----------------------------------------------------
-- Table `kcson`.`ufio`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `kcson`.`ufio` ;

CREATE TABLE IF NOT EXISTS `kcson`.`ufio` (
  `id` INT UNSIGNED NOT NULL AUTO_INCREMENT,
  `ufio` VARCHAR(255) NOT NULL,
  `ufio_short` VARCHAR(150) NULL,
  `ufioDeath` DATE NULL DEFAULT NULL,
  `ufiobirth` DATE NULL,
  `ESRN` BIGINT NULL,
  `prim` VARCHAR(255) NULL,
  `phone` VARCHAR(45) NULL,
  `snils` VARCHAR(14) NULL,
  `curator` VARCHAR(45) NULL,
  `create` DATETIME NULL DEFAULT CURRENT_TIMESTAMP,
  `ts` DATETIME NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  `cr_by` INT NULL,
  `upd_by` INT NULL,
  PRIMARY KEY (`id`),
  UNIQUE INDEX `ufio_UNIQUE` (`ufio` ASC) )
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `kcson`.`servform`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `kcson`.`servform` ;

CREATE TABLE IF NOT EXISTS `kcson`.`servform` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `servform` VARCHAR(255) NULL,
  `prim` VARCHAR(255) NULL,
  PRIMARY KEY (`id`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `kcson`.`pcat`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `kcson`.`pcat` ;

CREATE TABLE IF NOT EXISTS `kcson`.`pcat` (
  `id` INT UNSIGNED NOT NULL,
  `pcat` VARCHAR(255) NOT NULL,
  `prim` VARCHAR(45) NULL,
  PRIMARY KEY (`id`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `kcson`.`ripso`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `kcson`.`ripso` ;

CREATE TABLE IF NOT EXISTS `kcson`.`ripso` (
  `id` INT UNSIGNED NOT NULL AUTO_INCREMENT,
  `ripso` VARCHAR(20) NOT NULL,
  `year` YEAR(4) NOT NULL,
  `archive` TINYINT NULL DEFAULT 0,
  `servform_id` INT NOT NULL,
  `months` INT NULL,
  `pcat_id` INT UNSIGNED NOT NULL DEFAULT 1,
  PRIMARY KEY (`id`),
  INDEX `fk_ripso_servform1_idx` (`servform_id` ASC) ,
  INDEX `fk_ripso_pcat1_idx` (`pcat_id` ASC) ,
  CONSTRAINT `fk_ripso_servform1`
    FOREIGN KEY (`servform_id`)
    REFERENCES `kcson`.`servform` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_ripso_pcat1`
    FOREIGN KEY (`pcat_id`)
    REFERENCES `kcson`.`pcat` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `kcson`.`contracts`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `kcson`.`contracts` ;

CREATE TABLE IF NOT EXISTS `kcson`.`contracts` (
  `id` INT UNSIGNED NOT NULL AUTO_INCREMENT,
  `contracts` VARCHAR(45) NULL,
  `ufio_id` INT UNSIGNED NOT NULL,
  `dep_id` INT UNSIGNED NOT NULL,
  `ripso_id` INT UNSIGNED NULL,
  `blocked` TINYINT NULL DEFAULT 0,
  `startdate` DATE NOT NULL COMMENT 'дата оказания услуги',
  `enddate` DATE NOT NULL,
  `ippsuNum` INT(12) NULL,
  `note` VARCHAR(255) NULL,
  `create` DATETIME NULL DEFAULT CURRENT_TIMESTAMP,
  `ts` DATETIME NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  `cr_by` INT NULL,
  `upd_by` INT NULL,
  PRIMARY KEY (`id`),
  INDEX `fk_contract_ufio1_idx` (`ufio_id` ASC) ,
  INDEX `fk_contracts_ripso1_idx` (`ripso_id` ASC) ,
  INDEX `fk_contracts_dep1_idx` (`dep_id` ASC) ,
  CONSTRAINT `fk_contract_ufio1`
    FOREIGN KEY (`ufio_id`)
    REFERENCES `kcson`.`ufio` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_contracts_ripso1`
    FOREIGN KEY (`ripso_id`)
    REFERENCES `kcson`.`ripso` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_contracts_dep1`
    FOREIGN KEY (`dep_id`)
    REFERENCES `kcson`.`dep` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `kcson`.`role`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `kcson`.`role` ;

CREATE TABLE IF NOT EXISTS `kcson`.`role` (
  `id` INT UNSIGNED NOT NULL AUTO_INCREMENT,
  `role` VARCHAR(45) NULL,
  `prim` VARCHAR(255) NULL,
  PRIMARY KEY (`id`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `kcson`.`worker`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `kcson`.`worker` ;

CREATE TABLE IF NOT EXISTS `kcson`.`worker` (
  `id` INT UNSIGNED NOT NULL AUTO_INCREMENT,
  `worker` VARCHAR(255) NOT NULL,
  `user` VARCHAR(32) NULL COMMENT 'user login',
  `prim` VARCHAR(145) NULL,
  `role_id` INT UNSIGNED NOT NULL DEFAULT 1 COMMENT 'default role',
  `dep_id` INT UNSIGNED NOT NULL DEFAULT 1,
  `archive` TINYINT NULL DEFAULT 0,
  PRIMARY KEY (`id`),
  INDEX `fk_worker_roles1_idx` (`role_id` ASC) ,
  INDEX `fk_worker_dep1_idx` (`dep_id` ASC) ,
  UNIQUE INDEX `worker_UNIQUE` (`worker` ASC) ,
  CONSTRAINT `fk_worker_roles1`
    FOREIGN KEY (`role_id`)
    REFERENCES `kcson`.`role` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_worker_dep1`
    FOREIGN KEY (`dep_id`)
    REFERENCES `kcson`.`dep` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `kcson`.`job`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `kcson`.`job` ;

CREATE TABLE IF NOT EXISTS `kcson`.`job` (
  `id` INT UNSIGNED NOT NULL AUTO_INCREMENT,
  `job` VARCHAR(255) NULL,
  `prim` VARCHAR(45) NULL,
  PRIMARY KEY (`id`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `kcson`.`dep_has_worker`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `kcson`.`dep_has_worker` ;

CREATE TABLE IF NOT EXISTS `kcson`.`dep_has_worker` (
  `id` INT UNSIGNED NOT NULL AUTO_INCREMENT,
  `dep_has_worker` VARCHAR(255) NOT NULL,
  `worker_id` INT UNSIGNED NOT NULL,
  `dep_id` INT UNSIGNED NOT NULL,
  `job_id` INT UNSIGNED NOT NULL,
  `prim` VARCHAR(145) NULL,
  `archive` TINYINT NULL DEFAULT 0,
  `from` DATE NULL DEFAULT "2000-01-01",
  `till` DATE NULL DEFAULT "2050-01-01",
  `role_id` INT UNSIGNED NOT NULL DEFAULT 1,
  INDEX `fk_dep_has_worker_dep1_idx` (`dep_id` ASC) ,
  UNIQUE INDEX `wid_UNIQUE` (`id` ASC) ,
  INDEX `fk_dep_has_worker_job1_idx` (`job_id` ASC) ,
  PRIMARY KEY (`id`),
  INDEX `fk_dep_has_worker_role1_idx` (`role_id` ASC) ,
  UNIQUE INDEX `dep_has_worker_UNIQUE` (`dep_has_worker` ASC) ,
  CONSTRAINT `fk_dep_has_worker_worker1`
    FOREIGN KEY (`worker_id`)
    REFERENCES `kcson`.`worker` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_dep_has_worker_dep1`
    FOREIGN KEY (`dep_id`)
    REFERENCES `kcson`.`dep` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_dep_has_worker_job1`
    FOREIGN KEY (`job_id`)
    REFERENCES `kcson`.`job` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_dep_has_worker_role1`
    FOREIGN KEY (`role_id`)
    REFERENCES `kcson`.`role` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `kcson`.`main`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `kcson`.`main` ;

CREATE TABLE IF NOT EXISTS `kcson`.`main` (
  `id` BIGINT UNSIGNED NOT NULL AUTO_INCREMENT,
  `contracts_id` INT UNSIGNED NOT NULL,
  `dep_id` INT UNSIGNED NOT NULL,
  `ufio_id` INT UNSIGNED NOT NULL,
  `serv_id` INT UNSIGNED NOT NULL,
  `dep_has_worker_id` INT UNSIGNED NOT NULL DEFAULT 0,
  `worker_id` INT UNSIGNED NOT NULL,
  `vdate` DATE NOT NULL COMMENT 'дата оказания услуги',
  `uslnum` INT(4) NULL DEFAULT 0 COMMENT 'Количество услуг',
  `note` VARCHAR(255) NULL,
  `create` DATETIME NULL DEFAULT CURRENT_TIMESTAMP,
  `ts` DATETIME NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  `cr_by` INT NULL,
  `upd_by` INT NULL,
  `reported` TINYINT NULL DEFAULT 0,
  `wdate` DATETIME NULL DEFAULT NULL COMMENT 'дата ввода услуги',
  `overdid` TINYINT NULL DEFAULT 0,
  PRIMARY KEY (`id`),
  INDEX `fk_main_serv1_idx` (`serv_id` ASC) ,
  INDEX `fk_main_dep1_idx` (`dep_id` ASC) ,
  INDEX `fk_main_ufio1_idx` (`ufio_id` ASC) ,
  INDEX `fk_main_contracts1_idx` (`contracts_id` ASC) ,
  INDEX `fk_main_worker1_idx` (`worker_id` ASC) ,
  INDEX `fk_main_dep_has_worker1_idx` (`dep_has_worker_id` ASC) ,
  CONSTRAINT `fk_main_serv1`
    FOREIGN KEY (`serv_id`)
    REFERENCES `kcson`.`serv` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_main_dep1`
    FOREIGN KEY (`dep_id`)
    REFERENCES `kcson`.`dep` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_main_ufio1`
    FOREIGN KEY (`ufio_id`)
    REFERENCES `kcson`.`ufio` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_main_contracts1`
    FOREIGN KEY (`contracts_id`)
    REFERENCES `kcson`.`contracts` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_main_worker1`
    FOREIGN KEY (`worker_id`)
    REFERENCES `kcson`.`worker` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_main_dep_has_worker1`
    FOREIGN KEY (`dep_has_worker_id`)
    REFERENCES `kcson`.`dep_has_worker` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8mb4

COMMENT = 'main table';


-- -----------------------------------------------------
-- Table `kcson`.`holiday`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `kcson`.`holiday` ;

CREATE TABLE IF NOT EXISTS `kcson`.`holiday` (
  `holiday` DATE NOT NULL,
  `prim` VARCHAR(255) NULL,
  PRIMARY KEY (`holiday`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `kcson`.`category`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `kcson`.`category` ;

CREATE TABLE IF NOT EXISTS `kcson`.`category` (
  `id` INT UNSIGNED NOT NULL AUTO_INCREMENT,
  `category` VARCHAR(45) NOT NULL,
  `archive` TINYINT NULL DEFAULT 0,
  `prim` VARCHAR(255) NULL,
  `total` TINYINT NULL DEFAULT 0,
  `subof` INT NULL,
  PRIMARY KEY (`id`),
  UNIQUE INDEX `category_UNIQUE` (`category` ASC) );


-- -----------------------------------------------------
-- Table `kcson`.`tables_checksums`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `kcson`.`tables_checksums` ;

CREATE TABLE IF NOT EXISTS `kcson`.`tables_checksums` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `table` VARCHAR(45) NOT NULL,
  `checksum` VARCHAR(45) NULL,
  `lastid` INT NULL,
  PRIMARY KEY (`id`, `table`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `kcson`.`permiss`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `kcson`.`permiss` ;

CREATE TABLE IF NOT EXISTS `kcson`.`permiss` (
  `id` INT(10) UNSIGNED NOT NULL,
  `perm` VARCHAR(50) NOT NULL,
  `prim` VARCHAR(255) NULL,
  PRIMARY KEY (`id`))
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8mb4
;


-- -----------------------------------------------------
-- Table `kcson`.`contracts_has_serv`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `kcson`.`contracts_has_serv` ;

CREATE TABLE IF NOT EXISTS `kcson`.`contracts_has_serv` (
  `serv_id` INT UNSIGNED NOT NULL,
  `contracts_id` INT UNSIGNED NOT NULL,
  `planned` INT NULL DEFAULT 0,
  `filled` INT NULL DEFAULT 0,
  `prim` VARCHAR(255) NULL,
  `archive` TINYINT NULL DEFAULT 0,
  `create` DATETIME NULL DEFAULT CURRENT_TIMESTAMP,
  `ts` DATETIME NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  `cr_by` INT NULL,
  `upd_by` INT NULL,
  PRIMARY KEY (`serv_id`, `contracts_id`),
  INDEX `fk_contracts_has_serv_contracts1_idx` (`contracts_id` ASC) ,
  CONSTRAINT `fk_contracts_has_serv_serv1`
    FOREIGN KEY (`serv_id`)
    REFERENCES `kcson`.`serv` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_contracts_has_serv_contracts1`
    FOREIGN KEY (`contracts_id`)
    REFERENCES `kcson`.`contracts` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `kcson`.`audit`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `kcson`.`audit` ;

CREATE TABLE IF NOT EXISTS `kcson`.`audit` (
  `id` INT NOT NULL,
  `date` DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP,
  `action` VARCHAR(45) NULL,
  `user` VARCHAR(32) NULL,
  `host` VARCHAR(45) NULL,
  PRIMARY KEY (`id`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `kcson`.`data_log`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `kcson`.`data_log` ;

CREATE TABLE IF NOT EXISTS `kcson`.`data_log` (
  `id` INT NOT NULL,
  `message` VARCHAR(255) NULL,
  `date` DATETIME NOT NULL,
  `prim` VARCHAR(255) NULL,
  PRIMARY KEY (`id`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `kcson`.`setting`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `kcson`.`setting` ;

CREATE TABLE IF NOT EXISTS `kcson`.`setting` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `archive` TINYINT NULL DEFAULT 0,
  `setting` VARCHAR(45) NULL,
  `value` VARCHAR(255) NULL,
  `prim` VARCHAR(255) NULL,
  `sdate` DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP,
  PRIMARY KEY (`id`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `kcson`.`notifies`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `kcson`.`notifies` ;

CREATE TABLE IF NOT EXISTS `kcson`.`notifies` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `active` TINYINT NULL DEFAULT 1,
  `date` DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP,
  `msg` VARCHAR(255) NOT NULL,
  `onlyFor` TINYINT NULL,
  `worker_id` INT UNSIGNED NULL,
  PRIMARY KEY (`id`),
  INDEX `fk_notifies_worker1_idx` (`worker_id` ASC) ,
  CONSTRAINT `fk_notifies_worker1`
    FOREIGN KEY (`worker_id`)
    REFERENCES `kcson`.`worker` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `kcson`.`Rperiod`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `kcson`.`Rperiod` ;

CREATE TABLE IF NOT EXISTS `kcson`.`Rperiod` (
  `id` INT UNSIGNED NOT NULL AUTO_INCREMENT,
  `Rperiod` VARCHAR(45) NOT NULL,
  `st_mnth` INT NOT NULL,
  `end_mnth` INT NOT NULL,
  `st_day` INT NULL DEFAULT 0,
  `end_day` INT NULL DEFAULT 0,
  `prim` VARCHAR(255) NULL,
  `archive` TINYINT NULL DEFAULT 0,
  PRIMARY KEY (`id`),
  UNIQUE INDEX `period_UNIQUE` (`Rperiod` ASC) )
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `kcson`.`Rdata`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `kcson`.`Rdata` ;

CREATE TABLE IF NOT EXISTS `kcson`.`Rdata` (
  `id` INT UNSIGNED NOT NULL AUTO_INCREMENT,
  `saved` TINYINT NULL DEFAULT 0,
  `ts` DATETIME NULL DEFAULT current_timestamp,
  `year` YEAR NULL,
  `uslnum` INT NULL,
  `money` INT NULL,
  `2ndmoney` INT NULL,
  `ufio_id` INT UNSIGNED NOT NULL,
  `dep_id` INT UNSIGNED NOT NULL,
  `serv_id` INT UNSIGNED NOT NULL,
  `worker_id` INT UNSIGNED NOT NULL,
  PRIMARY KEY (`id`),
  INDEX `fk_Rdata_ufio1_idx` (`ufio_id` ASC) ,
  INDEX `fk_Rdata_dep1_idx` (`dep_id` ASC) ,
  INDEX `fk_Rdata_serv1_idx` (`serv_id` ASC) ,
  INDEX `fk_Rdata_worker1_idx` (`worker_id` ASC) ,
  CONSTRAINT `fk_Rdata_ufio1`
    FOREIGN KEY (`ufio_id`)
    REFERENCES `kcson`.`ufio` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_Rdata_dep1`
    FOREIGN KEY (`dep_id`)
    REFERENCES `kcson`.`dep` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_Rdata_serv1`
    FOREIGN KEY (`serv_id`)
    REFERENCES `kcson`.`serv` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_Rdata_worker1`
    FOREIGN KEY (`worker_id`)
    REFERENCES `kcson`.`worker` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `kcson`.`Rdep`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `kcson`.`Rdep` ;

CREATE TABLE IF NOT EXISTS `kcson`.`Rdep` (
  `id` INT UNSIGNED NOT NULL AUTO_INCREMENT,
  `saved` TINYINT NULL DEFAULT 0,
  `ts` DATETIME NULL DEFAULT current_timestamp,
  `year` YEAR NULL,
  `uslnum` INT NULL,
  `money` INT NULL,
  `2ndmoney` INT NULL,
  `peoples` INT NULL,
  PRIMARY KEY (`id`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `kcson`.`Rname`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `kcson`.`Rname` ;

CREATE TABLE IF NOT EXISTS `kcson`.`Rname` (
  `id` INT UNSIGNED NOT NULL AUTO_INCREMENT,
  `Rname` VARCHAR(45) NULL,
  `prim` VARCHAR(255) NULL,
  `ts` TIMESTAMP NULL DEFAULT current_TIMESTAMP,
  `cr_ts` TIMESTAMP NULL DEFAULT current_TIMESTAMP,
  `scheduled` TINYINT NULL,
  PRIMARY KEY (`id`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `kcson`.`RperiodsOFRname`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `kcson`.`RperiodsOFRname` ;

CREATE TABLE IF NOT EXISTS `kcson`.`RperiodsOFRname` (
  `Rname_id` INT UNSIGNED NOT NULL,
  `Rperiod_id` INT UNSIGNED NOT NULL,
  INDEX `fk_RperiodsOFRname_Rname1_idx` (`Rname_id` ASC) ,
  PRIMARY KEY (`Rperiod_id`, `Rname_id`),
  CONSTRAINT `fk_RperiodsOFRname_Rname1`
    FOREIGN KEY (`Rname_id`)
    REFERENCES `kcson`.`Rname` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_RperiodsOFRname_Rperiod1`
    FOREIGN KEY (`Rperiod_id`)
    REFERENCES `kcson`.`Rperiod` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `kcson`.`jobGroup`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `kcson`.`jobGroup` ;

CREATE TABLE IF NOT EXISTS `kcson`.`jobGroup` (
  `id` INT NOT NULL,
  `jobGroup` VARCHAR(25) NULL,
  `prim` VARCHAR(45) NULL,
  PRIMARY KEY (`id`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `kcson`.`add_info`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `kcson`.`add_info` ;

CREATE TABLE IF NOT EXISTS `kcson`.`add_info` (
  `pddate` DATE NOT NULL,
  `contracts_id` INT UNSIGNED NOT NULL,
  `predv_money` DECIMAL(10,2) NULL,
  `curFIO` VARCHAR(255) NULL,
  `psp` VARCHAR(255) NULL,
  `address` VARCHAR(255) NULL,
  `sdd` DECIMAL(10,2) NULL,
  `sdd_date` DATE NULL COMMENT 'Дата первое число месяца в котором проверяли СДД (будут взяты 12 предшествующих этой дате месяцев)',
  `perc` DOUBLE NULL,
  `not_standart_contract` TINYINT NULL,
  `not_standart_act` TINYINT NULL,
  `prim` VARCHAR(255) NULL,
  `create` DATETIME NULL DEFAULT CURRENT_TIMESTAMP,
  `ts` DATETIME NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  `cr_by` INT NULL,
  `upd_by` INT NULL,
  `repr_FIO` VARCHAR(255) NULL,
  `repr_addr` VARCHAR(255) NULL,
  `repr_psp` VARCHAR(255) NULL,
  `work_livemin` TINYINT NULL DEFAULT 0,
  PRIMARY KEY (`pddate`, `contracts_id`),
  INDEX `fk_add_info_contracts1_idx` (`contracts_id` ASC) ,
  CONSTRAINT `fk_add_info_contracts1`
    FOREIGN KEY (`contracts_id`)
    REFERENCES `kcson`.`contracts` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `kcson`.`log_edit_archive`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `kcson`.`log_edit_archive` ;

CREATE TABLE IF NOT EXISTS `kcson`.`log_edit_archive` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `worker_id` INT UNSIGNED NOT NULL,
  `table` VARCHAR(45) NULL,
  `table_id` VARCHAR(45) NULL,
  `column` INT NULL,
  `old_val` VARCHAR(255) NULL,
  `new_val` VARCHAR(255) NULL,
  `ts` DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP,
  `note` VARCHAR(255) NULL,
  PRIMARY KEY (`id`),
  INDEX `fk_log_edit_archive_worker1_idx` (`worker_id` ASC) ,
  CONSTRAINT `fk_log_edit_archive_worker1`
    FOREIGN KEY (`worker_id`)
    REFERENCES `kcson`.`worker` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `kcson`.`ripso_has_serv`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `kcson`.`ripso_has_serv` ;

CREATE TABLE IF NOT EXISTS `kcson`.`ripso_has_serv` (
  `planned` INT NULL,
  `serv_id` INT UNSIGNED NOT NULL,
  `ripso_id` INT UNSIGNED NOT NULL,
  PRIMARY KEY (`serv_id`, `ripso_id`),
  INDEX `fk_ripso_has_serv_ripso1_idx` (`ripso_id` ASC) ,
  CONSTRAINT `fk_ripso_has_serv_serv1`
    FOREIGN KEY (`serv_id`)
    REFERENCES `kcson`.`serv` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_ripso_has_serv_ripso1`
    FOREIGN KEY (`ripso_id`)
    REFERENCES `kcson`.`ripso` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8mb4
;


-- -----------------------------------------------------
-- Table `kcson`.`dep_has_ripso`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `kcson`.`dep_has_ripso` ;

CREATE TABLE IF NOT EXISTS `kcson`.`dep_has_ripso` (
  `dep_id` INT UNSIGNED NOT NULL,
  `ripso_id` INT UNSIGNED NOT NULL,
  PRIMARY KEY (`dep_id`, `ripso_id`),
  INDEX `fk_dep_has_ripso_ripso1_idx` (`ripso_id` ASC) ,
  INDEX `fk_dep_has_ripso_dep1_idx` (`dep_id` ASC) ,
  CONSTRAINT `fk_dep_has_ripso_dep1`
    FOREIGN KEY (`dep_id`)
    REFERENCES `kcson`.`dep` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_dep_has_ripso_ripso1`
    FOREIGN KEY (`ripso_id`)
    REFERENCES `kcson`.`ripso` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8mb4
;


-- -----------------------------------------------------
-- Table `kcson`.`job_has_jobGroup`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `kcson`.`job_has_jobGroup` ;

CREATE TABLE IF NOT EXISTS `kcson`.`job_has_jobGroup` (
  `job_id` INT UNSIGNED NOT NULL,
  `jobGroup_id` INT NOT NULL,
  PRIMARY KEY (`job_id`, `jobGroup_id`),
  INDEX `fk_job_has_jobGroup_jobGroup1_idx` (`jobGroup_id` ASC) ,
  INDEX `fk_job_has_jobGroup_job1_idx` (`job_id` ASC) ,
  CONSTRAINT `fk_job_has_jobGroup_job1`
    FOREIGN KEY (`job_id`)
    REFERENCES `kcson`.`job` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_job_has_jobGroup_jobGroup1`
    FOREIGN KEY (`jobGroup_id`)
    REFERENCES `kcson`.`jobGroup` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `kcson`.`role_has_permiss`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `kcson`.`role_has_permiss` ;

CREATE TABLE IF NOT EXISTS `kcson`.`role_has_permiss` (
  `role_id` INT UNSIGNED NOT NULL,
  `permiss_id` INT(10) UNSIGNED NOT NULL,
  PRIMARY KEY (`role_id`, `permiss_id`),
  INDEX `fk_role_has_permiss_permiss1_idx` (`permiss_id` ASC) IN,
  INDEX `fk_role_has_permiss_roles1_idx` (`role_id` ASC) ,
  CONSTRAINT `fk_role_has_permiss_roles1`
    FOREIGN KEY (`role_id`)
    REFERENCES `kcson`.`role` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_role_has_permiss_permiss1`
    FOREIGN KEY (`permiss_id`)
    REFERENCES `kcson`.`permiss` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `kcson`.`payment`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `kcson`.`payment` ;

CREATE TABLE IF NOT EXISTS `kcson`.`payment` (
  `id` INT UNSIGNED NOT NULL AUTO_INCREMENT,
  `ufio_id` INT UNSIGNED NOT NULL,
  `paydate` DATE NULL,
  `sum` DECIMAL(10,2) NULL,
  `prim` VARCHAR(255) NULL,
  `ts` VARCHAR(45) NULL,
  PRIMARY KEY (`id`),
  INDEX `fk_payment_ufio1_idx` (`ufio_id` ASC) ,
  CONSTRAINT `fk_payment_ufio1`
    FOREIGN KEY (`ufio_id`)
    REFERENCES `kcson`.`ufio` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `kcson`.`invoice`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `kcson`.`invoice` ;

CREATE TABLE IF NOT EXISTS `kcson`.`invoice` (
  `id` INT UNSIGNED NOT NULL AUTO_INCREMENT,
  `ufio_id` INT UNSIGNED NOT NULL,
  `give_date` DATE NULL,
  `money` DECIMAL(10,2) NULL,
  `filled` DECIMAL(10,2) NULL,
  `prim` VARCHAR(255) NULL,
  `dep_id` INT UNSIGNED NOT NULL,
  `create` DATETIME NULL DEFAULT CURRENT_TIMESTAMP,
  `ts` DATETIME NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  `cr_by` INT NULL,
  `upd_by` INT NULL,
  `dismissed` TINYINT NULL DEFAULT 0,
  `pay_period_end` DATE NULL,
  PRIMARY KEY (`id`),
  INDEX `fk_invoice_ufio1_idx` (`ufio_id` ASC) ,
  INDEX `fk_invoice_dep1_idx` (`dep_id` ASC) ,
  CONSTRAINT `fk_invoice_ufio1`
    FOREIGN KEY (`ufio_id`)
    REFERENCES `kcson`.`ufio` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_invoice_dep1`
    FOREIGN KEY (`dep_id`)
    REFERENCES `kcson`.`dep` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `kcson`.`invoice_has_payment`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `kcson`.`invoice_has_payment` ;

CREATE TABLE IF NOT EXISTS `kcson`.`invoice_has_payment` (
  `invoice_id` INT UNSIGNED NOT NULL,
  `payment_id` INT UNSIGNED NOT NULL,
  PRIMARY KEY (`invoice_id`, `payment_id`),
  INDEX `fk_invoice_has_payment_payment1_idx` (`payment_id` ASC) ,
  INDEX `fk_invoice_has_payment_invoice1_idx` (`invoice_id` ASC) ,
  CONSTRAINT `fk_invoice_has_payment_invoice1`
    FOREIGN KEY (`invoice_id`)
    REFERENCES `kcson`.`invoice` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_invoice_has_payment_payment1`
    FOREIGN KEY (`payment_id`)
    REFERENCES `kcson`.`payment` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `kcson`.`ufio_has_category`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `kcson`.`ufio_has_category` ;

CREATE TABLE IF NOT EXISTS `kcson`.`ufio_has_category` (
  `ufio_id` INT UNSIGNED NOT NULL,
  `category_id` INT UNSIGNED NOT NULL,
  `get_date` DATE NULL DEFAULT '2018-01-01',
  `archive` TINYINT NULL DEFAULT 0,
  `prim` VARCHAR(255) NULL,
  `create` DATETIME NULL DEFAULT CURRENT_TIMESTAMP,
  `ts` DATETIME NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  `cr_by` INT NULL,
  `upd_by` INT NULL,
  PRIMARY KEY (`ufio_id`, `category_id`),
  INDEX `fk_ufio_has_category_category1_idx` (`category_id` ASC) ,
  INDEX `fk_ufio_has_category_ufio1_idx` (`ufio_id` ASC) ,
  CONSTRAINT `fk_ufio_has_category_ufio1`
    FOREIGN KEY (`ufio_id`)
    REFERENCES `kcson`.`ufio` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_ufio_has_category_category1`
    FOREIGN KEY (`category_id`)
    REFERENCES `kcson`.`category` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `kcson`.`live_min`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `kcson`.`live_min` ;

CREATE TABLE IF NOT EXISTS `kcson`.`live_min` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `lmdate` DATE NOT NULL COMMENT 'Используется с ',
  `live_min_p` DECIMAL(10,2) NOT NULL,
  `live_min_w` DECIMAL(10,2) NOT NULL,
  `live_min_c` DECIMAL(10,2) NOT NULL,
  `live_min_all` DECIMAL(10,2) NULL,
  `post` VARCHAR(255) NULL,
  `post_date` DATE NULL,
  `create` DATETIME NULL DEFAULT CURRENT_TIMESTAMP,
  `ts` DATETIME NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  `cr_by` INT NULL,
  `upd_by` INT NULL,
  PRIMARY KEY (`id`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `kcson`.`ugroup`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `kcson`.`ugroup` ;

CREATE TABLE IF NOT EXISTS `kcson`.`ugroup` (
  `id` INT NOT NULL,
  `ugroup` VARCHAR(45) NOT NULL,
  `dep_id` INT UNSIGNED NULL DEFAULT 0,
  `worker_id` INT UNSIGNED NULL DEFAULT 0,
  `prim` VARCHAR(255) NULL,
  `ugroupcol` VARCHAR(45) NULL,
  PRIMARY KEY (`id`),
  INDEX `fk_ugroup_dep1_idx` (`dep_id` ASC) ,
  INDEX `fk_ugroup_worker1_idx` (`worker_id` ASC) ,
  CONSTRAINT `fk_ugroup_dep1`
    FOREIGN KEY (`dep_id`)
    REFERENCES `kcson`.`dep` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_ugroup_worker1`
    FOREIGN KEY (`worker_id`)
    REFERENCES `kcson`.`worker` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `kcson`.`ugroup_has_ufio`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `kcson`.`ugroup_has_ufio` ;

CREATE TABLE IF NOT EXISTS `kcson`.`ugroup_has_ufio` (
  `ugroup_id` INT NOT NULL,
  `ufio_id` INT UNSIGNED NOT NULL,
  PRIMARY KEY (`ugroup_id`, `ufio_id`),
  INDEX `fk_ugroup_has_ufio_ufio1_idx` (`ufio_id` ASC) ,
  INDEX `fk_ugroup_has_ufio_ugroup1_idx` (`ugroup_id` ASC) ,
  CONSTRAINT `fk_ugroup_has_ufio_ugroup1`
    FOREIGN KEY (`ugroup_id`)
    REFERENCES `kcson`.`ugroup` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_ugroup_has_ufio_ufio1`
    FOREIGN KEY (`ufio_id`)
    REFERENCES `kcson`.`ufio` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `kcson`.`main_has_ugroup`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `kcson`.`main_has_ugroup` ;

CREATE TABLE IF NOT EXISTS `kcson`.`main_has_ugroup` (
  `main_id` BIGINT UNSIGNED NOT NULL,
  `ugroup_id` INT NOT NULL,
  PRIMARY KEY (`main_id`, `ugroup_id`),
  INDEX `fk_main_has_ugroup_ugroup1_idx` (`ugroup_id` ASC) ,
  INDEX `fk_main_has_ugroup_main1_idx` (`main_id` ASC) ,
  CONSTRAINT `fk_main_has_ugroup_main1`
    FOREIGN KEY (`main_id`)
    REFERENCES `kcson`.`main` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_main_has_ugroup_ugroup1`
    FOREIGN KEY (`ugroup_id`)
    REFERENCES `kcson`.`ugroup` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8mb4
;


-- -----------------------------------------------------
-- Table `kcson`.`job_has_serv`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `kcson`.`job_has_serv` ;

CREATE TABLE IF NOT EXISTS `kcson`.`job_has_serv` (
  `job_id` INT UNSIGNED NOT NULL,
  `serv_id` INT UNSIGNED NOT NULL,
  PRIMARY KEY (`job_id`, `serv_id`),
  INDEX `fk_job_has_serv_serv1_idx` (`serv_id` ASC) ,
  INDEX `fk_job_has_serv_job1_idx` (`job_id` ASC) ,
  CONSTRAINT `fk_job_has_serv_job1`
    FOREIGN KEY (`job_id`)
    REFERENCES `kcson`.`job` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_job_has_serv_serv1`
    FOREIGN KEY (`serv_id`)
    REFERENCES `kcson`.`serv` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `kcson`.`street_home`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `kcson`.`street_home` ;

CREATE TABLE IF NOT EXISTS `kcson`.`street_home` (
  `id` INT NOT NULL,
  `street_home` VARCHAR(255) NULL,
  `prim` VARCHAR(255) NULL,
  `create` DATETIME NULL DEFAULT CURRENT_TIMESTAMP,
  `ts` DATETIME NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  `cr_by` INT NULL,
  `upd_by` INT NULL,
  `coordinate` POINT NULL,
  PRIMARY KEY (`id`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `kcson`.`worker_settings`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `kcson`.`worker_settings` ;

CREATE TABLE IF NOT EXISTS `kcson`.`worker_settings` (
  `id` INT UNSIGNED NOT NULL,
  `last_tab` VARCHAR(145) NULL,
  `last_dep` INT UNSIGNED NULL,
  `last_ufio` INT UNSIGNED NULL,
  `last_contr` INT UNSIGNED NULL,
  `last_ufio_filter` INT NULL,
  `last_year` INT NULL,
  PRIMARY KEY (`id`),
  CONSTRAINT `fk_worker_settings_worker1`
    FOREIGN KEY (`id`)
    REFERENCES `kcson`.`worker` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `kcson`.`stub_model`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `kcson`.`stub_model` ;

CREATE TABLE IF NOT EXISTS `kcson`.`stub_model` (
  `id` INT NOT NULL,
  `msg` VARCHAR(45) NULL,
  `msg1` VARCHAR(45) NULL,
  PRIMARY KEY (`id`))
ENGINE = InnoDB
COMMENT = 'Used as default table model if right model  not implemented yet';


-- -----------------------------------------------------
-- Table `kcson`.`ui_select_fiolist`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `kcson`.`ui_select_fiolist` ;

CREATE TABLE IF NOT EXISTS `kcson`.`ui_select_fiolist` (
  `id` INT NOT NULL,
  `list_name` VARCHAR(45) NOT NULL,
  `sql_table` VARCHAR(45) NULL,
  `col` INT NULL,
  `orderby` INT NULL,
  `prim` VARCHAR(45) NULL,
  PRIMARY KEY (`id`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `kcson`.`test`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `kcson`.`test` ;

CREATE TABLE IF NOT EXISTS `kcson`.`test` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `date` DATE NULL,
  `datetime` DATETIME NULL,
  `str` VARCHAR(45) NULL,
  `decimal` DECIMAL(10,2) NULL,
  `double` DOUBLE NULL,
  PRIMARY KEY (`id`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `kcson`.`complex_dep`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `kcson`.`complex_dep` ;

CREATE TABLE IF NOT EXISTS `kcson`.`complex_dep` (
  `id` INT UNSIGNED NOT NULL,
  `complex_dep` VARCHAR(255) NULL,
  `note` VARCHAR(255) NULL,
  PRIMARY KEY (`id`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `kcson`.`complex_dep_has_dep`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `kcson`.`complex_dep_has_dep` ;

CREATE TABLE IF NOT EXISTS `kcson`.`complex_dep_has_dep` (
  `complex_dep_id` INT UNSIGNED NOT NULL,
  `dep_id` INT UNSIGNED NOT NULL,
  PRIMARY KEY (`complex_dep_id`, `dep_id`),
  INDEX `fk_complex_dep_has_dep_dep1_idx` (`dep_id` ASC) ,
  INDEX `fk_complex_dep_has_dep_complex_dep1_idx` (`complex_dep_id` ASC) ,
  CONSTRAINT `fk_complex_dep_has_dep_complex_dep1`
    FOREIGN KEY (`complex_dep_id`)
    REFERENCES `kcson`.`complex_dep` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_complex_dep_has_dep_dep1`
    FOREIGN KEY (`dep_id`)
    REFERENCES `kcson`.`dep` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;

USE `kcson` ;

-- -----------------------------------------------------
-- Placeholder table for view `kcson`.`user_has_serv`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `kcson`.`user_has_serv` (`id` INT, `contracts_id` INT, `dep_id` INT, `ufio_id` INT, `serv_id` INT, `dep_has_worker_id` INT, `worker_id` INT, `vdate` INT, `uslnum` INT, `note` INT, `create` INT, `ts` INT, `cr_by` INT, `upd_by` INT, `reported` INT, `wdate` INT, `overdid` INT);

-- -----------------------------------------------------
-- Placeholder table for view `kcson`.`dep_has_main`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `kcson`.`dep_has_main` (`id` INT, `contracts_id` INT, `dep_id` INT, `ufio_id` INT, `serv_id` INT, `dep_has_worker_id` INT, `worker_id` INT, `vdate` INT, `uslnum` INT, `note` INT, `create` INT, `ts` INT, `cr_by` INT, `upd_by` INT, `reported` INT, `wdate` INT, `overdid` INT);

-- -----------------------------------------------------
-- Placeholder table for view `kcson`.`last_used_workers`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `kcson`.`last_used_workers` (`id` INT, `worker` INT);

-- -----------------------------------------------------
-- Placeholder table for view `kcson`.`_serv_activ`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `kcson`.`_serv_activ` (`id` INT, `tserv` INT, `price` INT, `total` INT, `sub_serv` INT, `serv` INT);

-- -----------------------------------------------------
-- Placeholder table for view `kcson`.`servOFripso`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `kcson`.`servOFripso` (`id` INT, `tnum` INT, `serv` INT, `year` INT, `sub_serv` INT, `sub_serv_str` INT, `price` INT, `price2` INT, `price3` INT, `archive` INT, `total` INT, `acronym` INT, `workload` INT, `content` INT, `r_id` INT, `ripso` INT);

-- -----------------------------------------------------
-- Placeholder table for view `kcson`.`fioOFdepBYserv`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `kcson`.`fioOFdepBYserv` (`ufio` INT, `ufio_short` INT, `ufiobirth` INT, `ESRN` INT, `ufioDeath` INT);

-- -----------------------------------------------------
-- Placeholder table for view `kcson`.`servOFyear`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `kcson`.`servOFyear` (`id` INT, `contracts_id` INT, `dep_id` INT, `ufio_id` INT, `serv_id` INT, `dep_has_worker_id` INT, `worker_id` INT, `vdate` INT, `uslnum` INT, `note` INT, `create` INT, `ts` INT, `cr_by` INT, `upd_by` INT, `reported` INT, `wdate` INT, `overdid` INT);

-- -----------------------------------------------------
-- Placeholder table for view `kcson`.`servOFyear-2`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `kcson`.`servOFyear-2` (`id` INT, `contracts_id` INT, `dep_id` INT, `ufio_id` INT, `serv_id` INT, `dep_has_worker_id` INT, `worker_id` INT, `vdate` INT, `uslnum` INT, `note` INT, `create` INT, `ts` INT, `cr_by` INT, `upd_by` INT, `reported` INT, `wdate` INT, `overdid` INT);

-- -----------------------------------------------------
-- Placeholder table for view `kcson`.`servOFyear-3`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `kcson`.`servOFyear-3` (`id` INT, `contracts_id` INT, `dep_id` INT, `ufio_id` INT, `serv_id` INT, `dep_has_worker_id` INT, `worker_id` INT, `vdate` INT, `uslnum` INT, `note` INT, `create` INT, `ts` INT, `cr_by` INT, `upd_by` INT, `reported` INT, `wdate` INT, `overdid` INT);

-- -----------------------------------------------------
-- Placeholder table for view `kcson`.`servOFyear-1`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `kcson`.`servOFyear-1` (`id` INT, `contracts_id` INT, `dep_id` INT, `ufio_id` INT, `serv_id` INT, `dep_has_worker_id` INT, `worker_id` INT, `vdate` INT, `uslnum` INT, `note` INT, `create` INT, `ts` INT, `cr_by` INT, `upd_by` INT, `reported` INT, `wdate` INT, `overdid` INT);

-- -----------------------------------------------------
-- Placeholder table for view `kcson`.`fioOFdepBYset`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `kcson`.`fioOFdepBYset` (`ufio` INT, `ufio_short` INT, `ufiobirth` INT, `ESRN` INT, `ufioDeath` INT);

-- -----------------------------------------------------
-- Placeholder table for view `kcson`.`_dep_has_ufio_by_ripso`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `kcson`.`_dep_has_ufio_by_ripso` (`id` INT, `ufio` INT, `ufio_short` INT, `ufioDeath` INT, `ufiobirth` INT, `ESRN` INT, `prim` INT, `phone` INT, `snils` INT, `curator` INT, `create` INT, `ts` INT, `cr_by` INT, `upd_by` INT);

-- -----------------------------------------------------
-- Placeholder table for view `kcson`.`worker_has_dep`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `kcson`.`worker_has_dep` (`dep_id` INT, `dep` INT);

-- -----------------------------------------------------
-- Placeholder table for view `kcson`.`dep_has_serv`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `kcson`.`dep_has_serv` (`id` INT, `tnum` INT, `serv` INT, `year` INT, `sub_serv` INT, `sub_serv_str` INT, `price` INT, `price2` INT, `price3` INT, `archive` INT, `total` INT, `acronym` INT, `workload` INT, `content` INT);

-- -----------------------------------------------------
-- Placeholder table for view `kcson`.`main_cprice`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `kcson`.`main_cprice` (`*` INT, `to_pay` INT, `to_pay2` INT);

-- -----------------------------------------------------
-- Placeholder table for view `kcson`.`main_NZ`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `kcson`.`main_NZ` (`id` INT, `contracts_id` INT, `dep_id` INT, `ufio_id` INT, `serv_id` INT, `dep_has_worker_id` INT, `worker_id` INT, `vdate` INT, `uslnum` INT, `note` INT, `create` INT, `ts` INT, `cr_by` INT, `upd_by` INT, `reported` INT, `wdate` INT, `overdid` INT);

-- -----------------------------------------------------
-- Placeholder table for view `kcson`.`dep_total_serv`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `kcson`.`dep_total_serv` (`contracts_id` INT, `dep_id` INT, `serv_id` INT, `worker_id` INT, `SUM(uslnum)` INT, `MONTH(vdate)` INT, `YEAR(vdate)` INT);

-- -----------------------------------------------------
-- Placeholder table for view `kcson`.`dep_total_supserv1`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `kcson`.`dep_total_supserv1` (`contracts_id` INT, `dep_id` INT, `sub_serv` INT, `worker_id` INT, `SUM(uslnum)` INT, `mnth1` INT, `year1` INT);

-- -----------------------------------------------------
-- Placeholder table for view `kcson`.`max_pay_in_month_50`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `kcson`.`max_pay_in_month_50` (`*` INT, `max_pay` INT);

-- -----------------------------------------------------
-- Placeholder table for view `kcson`.`max_pay_in_month_75`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `kcson`.`max_pay_in_month_75` (`*` INT, `max_pay` INT);

-- -----------------------------------------------------
-- Placeholder table for view `kcson`.`max_pay_in_month`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `kcson`.`max_pay_in_month` (`id` INT);

-- -----------------------------------------------------
-- Placeholder table for view `kcson`.`total_cprice_in_month`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `kcson`.`total_cprice_in_month` (`contracts_id` INT, `SUM(to_pay)` INT);

-- -----------------------------------------------------
-- Placeholder table for view `kcson`.`_dep_has_ufio_ending`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `kcson`.`_dep_has_ufio_ending` (`ufio` INT, `id` INT, `contracts` INT, `ufio_id` INT, `dep_id` INT, `ripso_id` INT, `blocked` INT, `startdate` INT, `enddate` INT, `ippsuNum` INT, `note` INT, `create` INT, `ts` INT, `cr_by` INT, `upd_by` INT);

-- -----------------------------------------------------
-- Placeholder table for view `kcson`.`_dep_has_ufio_ended`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `kcson`.`_dep_has_ufio_ended` (`ufio` INT, `id` INT, `contracts` INT, `ufio_id` INT, `dep_id` INT, `ripso_id` INT, `blocked` INT, `startdate` INT, `enddate` INT, `ippsuNum` INT, `note` INT, `create` INT, `ts` INT, `cr_by` INT, `upd_by` INT);

-- -----------------------------------------------------
-- Placeholder table for view `kcson`.`add_info_for_ufio`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `kcson`.`add_info_for_ufio` (`ufio_id` INT, `pddate` INT, `contracts_id` INT, `predv_money` INT, `curFIO` INT, `psp` INT, `address` INT, `sdd` INT, `sdd_date` INT, `perc` INT, `not_standart_contract` INT, `not_standart_act` INT, `prim` INT, `create` INT, `ts` INT, `cr_by` INT, `upd_by` INT, `repr_FIO` INT, `repr_addr` INT, `repr_psp` INT, `work_livemin` INT);

-- -----------------------------------------------------
-- Placeholder table for view `kcson`.`_worker_settings`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `kcson`.`_worker_settings` (`id` INT, `last_tab` INT, `last_dep` INT, `last_ufio` INT, `last_contr` INT, `last_ufio_filter` INT, `last_year` INT);

-- -----------------------------------------------------
-- Placeholder table for view `kcson`.`_ufio_has_contracts`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `kcson`.`_ufio_has_contracts` (`id` INT, `contracts` INT, `ufio_id` INT, `dep_id` INT, `ripso_id` INT, `blocked` INT, `startdate` INT, `enddate` INT, `ippsuNum` INT, `note` INT, `create` INT, `ts` INT, `cr_by` INT, `upd_by` INT);

-- -----------------------------------------------------
-- Placeholder table for view `kcson`.`_contr_has_serv`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `kcson`.`_contr_has_serv` (`serv_id` INT, `contracts_id` INT, `planned` INT, `filled` INT, `prim` INT, `archive` INT, `create` INT, `ts` INT, `cr_by` INT, `upd_by` INT);

-- -----------------------------------------------------
-- Placeholder table for view `kcson`.`_contr_has_add_info`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `kcson`.`_contr_has_add_info` (`pddate` INT, `contracts_id` INT, `predv_money` INT, `curFIO` INT, `psp` INT, `address` INT, `sdd` INT, `sdd_date` INT, `perc` INT, `not_standart_contract` INT, `not_standart_act` INT, `prim` INT, `create` INT, `ts` INT, `cr_by` INT, `upd_by` INT, `repr_FIO` INT, `repr_addr` INT, `repr_psp` INT, `work_livemin` INT);

-- -----------------------------------------------------
-- Placeholder table for view `kcson`.`_ufio_has_main`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `kcson`.`_ufio_has_main` (`id` INT, `contracts_id` INT, `dep_id` INT, `ufio_id` INT, `serv_id` INT, `dep_has_worker_id` INT, `worker_id` INT, `vdate` INT, `uslnum` INT, `note` INT, `create` INT, `ts` INT, `cr_by` INT, `upd_by` INT, `reported` INT, `wdate` INT, `overdid` INT);

-- -----------------------------------------------------
-- Placeholder table for view `kcson`.`_ufio_has_category_for_last_ufio`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `kcson`.`_ufio_has_category_for_last_ufio` (`ufio_id` INT, `category_id` INT, `get_date` INT, `archive` INT, `prim` INT, `create` INT, `ts` INT, `cr_by` INT, `upd_by` INT);

-- -----------------------------------------------------
-- Placeholder table for view `kcson`.`_dep_has_ufio_by_contr`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `kcson`.`_dep_has_ufio_by_contr` (`id` INT, `ufio` INT, `ufio_short` INT, `ufioDeath` INT, `ufiobirth` INT, `ESRN` INT, `prim` INT, `phone` INT, `snils` INT, `curator` INT, `create` INT, `ts` INT, `cr_by` INT, `upd_by` INT);

-- -----------------------------------------------------
-- Placeholder table for view `kcson`.`_dep_has_ufio`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `kcson`.`_dep_has_ufio` (`id` INT, `ufio` INT, `ufio_short` INT, `ufioDeath` INT, `ufiobirth` INT, `ESRN` INT, `prim` INT, `phone` INT, `snils` INT, `curator` INT, `create` INT, `ts` INT, `cr_by` INT, `upd_by` INT);

-- -----------------------------------------------------
-- Placeholder table for view `kcson`.`__dep_has_ufio_more`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `kcson`.`__dep_has_ufio_more` (`id` INT, `ufio` INT, `ufio_short` INT, `ufioDeath` INT, `ufiobirth` INT, `ESRN` INT, `prim_fio` INT, `phone` INT, `snils` INT, `curator_fio` INT, `create_fio` INT, `ts_fio` INT, `cr_by_fio` INT, `upd_by_fio` INT);

-- -----------------------------------------------------
-- Placeholder table for view `kcson`.`_main_for_dep`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `kcson`.`_main_for_dep` (`id` INT, `contracts_id` INT, `dep_id` INT, `ufio_id` INT, `serv_id` INT, `dep_has_worker_id` INT, `worker_id` INT, `vdate` INT, `uslnum` INT, `note` INT, `create` INT, `ts` INT, `cr_by` INT, `upd_by` INT, `reported` INT, `wdate` INT, `overdid` INT);

-- -----------------------------------------------------
-- Placeholder table for view `kcson`.`_g_categ_list_ufio_for_dep_for_year`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `kcson`.`_g_categ_list_ufio_for_dep_for_year` (`category_id` INT, `ufio_id` INT, `SUM(uslnum)` INT);

-- -----------------------------------------------------
-- Placeholder table for view `kcson`.`_contr_has_main`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `kcson`.`_contr_has_main` (`id` INT, `contracts_id` INT, `dep_id` INT, `ufio_id` INT, `serv_id` INT, `dep_has_worker_id` INT, `worker_id` INT, `vdate` INT, `uslnum` INT, `note` INT, `create` INT, `ts` INT, `cr_by` INT, `upd_by` INT, `reported` INT, `wdate` INT, `overdid` INT);

-- -----------------------------------------------------
-- Placeholder table for view `kcson`.`_worker_has_main`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `kcson`.`_worker_has_main` (`id` INT, `contracts_id` INT, `dep_id` INT, `ufio_id` INT, `serv_id` INT, `dep_has_worker_id` INT, `worker_id` INT, `vdate` INT, `uslnum` INT, `note` INT, `create` INT, `ts` INT, `cr_by` INT, `upd_by` INT, `reported` INT, `wdate` INT, `overdid` INT);

-- -----------------------------------------------------
-- Placeholder table for view `kcson`.`_contracts`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `kcson`.`_contracts` (`id` INT, `contracts` INT, `ufio_id` INT, `dep_id` INT, `ripso_id` INT, `blocked` INT, `startdate` INT, `enddate` INT, `ippsuNum` INT, `note` INT, `create` INT, `ts` INT, `cr_by` INT, `upd_by` INT, `servform_id` INT);

-- -----------------------------------------------------
-- Placeholder table for view `kcson`.`_main_cprice`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `kcson`.`_main_cprice` (`*` INT, `to_pay` INT, `to_pay2` INT);

-- -----------------------------------------------------
-- Placeholder table for view `kcson`.`_user_has_main`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `kcson`.`_user_has_main` (`id` INT, `contracts_id` INT, `dep_id` INT, `ufio_id` INT, `serv_id` INT, `dep_has_worker_id` INT, `worker_id` INT, `vdate` INT, `uslnum` INT, `note` INT, `create` INT, `ts` INT, `cr_by` INT, `upd_by` INT, `reported` INT, `wdate` INT, `overdid` INT);

-- -----------------------------------------------------
-- Placeholder table for view `kcson`.`_user_has_main_limit30`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `kcson`.`_user_has_main_limit30` (`id` INT, `contracts_id` INT, `dep_id` INT, `ufio_id` INT, `serv_id` INT, `dep_has_worker_id` INT, `worker_id` INT, `vdate` INT, `uslnum` INT, `note` INT, `create` INT, `ts` INT, `cr_by` INT, `upd_by` INT, `reported` INT, `wdate` INT, `overdid` INT);

-- -----------------------------------------------------
-- Placeholder table for view `kcson`.`_dep_has_worker`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `kcson`.`_dep_has_worker` (`id` INT, `dep_has_worker` INT, `worker_id` INT, `dep_id` INT, `job_id` INT, `prim` INT, `archive` INT, `from` INT, `till` INT, `role_id` INT);

-- -----------------------------------------------------
-- Placeholder table for view `kcson`.`_g_serv_total_dep`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `kcson`.`_g_serv_total_dep` (`serv_id` INT, `uslnum` INT, `ufio_id` INT, `records` INT);

-- -----------------------------------------------------
-- Placeholder table for view `kcson`.`_ufio_has_invalid_contracts`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `kcson`.`_ufio_has_invalid_contracts` (`ufio` INT, `id` INT, `contracts` INT, `ufio_id` INT, `dep_id` INT, `ripso_id` INT, `blocked` INT, `startdate` INT, `enddate` INT, `ippsuNum` INT, `note` INT, `create` INT, `ts` INT, `cr_by` INT, `upd_by` INT);

-- -----------------------------------------------------
-- Placeholder table for view `kcson`.`_ufio_has_valid_contracts`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `kcson`.`_ufio_has_valid_contracts` (`ufio` INT, `id` INT, `contracts` INT, `ufio_id` INT, `dep_id` INT, `ripso_id` INT, `blocked` INT, `startdate` INT, `enddate` INT, `ippsuNum` INT, `note` INT, `create` INT, `ts` INT, `cr_by` INT, `upd_by` INT);

-- -----------------------------------------------------
-- Placeholder table for view `kcson`.`_dep_has_ripso`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `kcson`.`_dep_has_ripso` (`ripso_id` INT, `ripso` INT);

-- -----------------------------------------------------
-- Placeholder table for view `kcson`.`_user_has_main_today`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `kcson`.`_user_has_main_today` (`id` INT, `contracts_id` INT, `dep_id` INT, `ufio_id` INT, `serv_id` INT, `dep_has_worker_id` INT, `worker_id` INT, `vdate` INT, `uslnum` INT, `note` INT, `create` INT, `ts` INT, `cr_by` INT, `upd_by` INT, `reported` INT, `wdate` INT, `overdid` INT);

-- -----------------------------------------------------
-- Placeholder table for view `kcson`.`_active_dep`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `kcson`.`_active_dep` (`id` INT, `dep` INT, `dep_full_name` INT, `dep_puname` INT, `note` INT, `archive` INT, `complex_dep_id` INT);

-- -----------------------------------------------------
-- procedure my_procedure
-- -----------------------------------------------------

USE `kcson`;
DROP procedure IF EXISTS `kcson`.`my_procedure`;

DELIMITER $$
USE `kcson`$$
CREATE PROCEDURE my_procedure ()
BEGIN    

	#declare userN varchar(32);
    #declare uDepId int;
	/* Inside the procedure, individual statements terminate with ; */
	#SET SESSION userN = substring_index(user(), '@', 1);
    #CURRENT_ROLE() 
	#SET SESSION uDepId = substring_index(user(), '@', 1);
/* whole procedure ends with the custom delimiter */
END$$

DELIMITER ;

-- -----------------------------------------------------
-- procedure rbac
-- -----------------------------------------------------

USE `kcson`;
DROP procedure IF EXISTS `kcson`.`rbac`;

DELIMITER $$
USE `kcson`$$
CREATE PROCEDURE rbac()
BEGIN    


GRANT SELECT ON sakila.actor TO newuser@localhost ;

CREATE USER 'newuser'@'%'  IDENTIFIED BY 'mysql local work';

GRANT SELECT, INSERT, UPDATE, DELETE
  ON TABLE sakila.actor
TO 'newuser'@'%';

end$$

DELIMITER ;

-- -----------------------------------------------------
-- procedure rbac_example
-- -----------------------------------------------------

USE `kcson`;
DROP procedure IF EXISTS `kcson`.`rbac_example`;

DELIMITER $$
USE `kcson`$$
CREATE PROCEDURE rbac_example ()
BEGIN    


	#GRANT SELECT ON kcson.actor TO newuser@localhost ;

	CREATE USER 'newuser'@'%'  IDENTIFIED BY 'mysql local work';




	CREATE ROLE 'app_developer', 'app_read', 'app_write';

	GRANT ALL ON app_db.* TO 'app_developer';
	GRANT SELECT ON app_db.* TO 'app_read';
	GRANT INSERT, UPDATE, DELETE ON app_db.* TO 'app_write';

	CREATE USER 'dev1'@'localhost' IDENTIFIED BY 'dev1pass';
	CREATE USER 'read_user1'@'localhost' IDENTIFIED BY 'read_user1pass';
	CREATE USER 'read_user2'@'localhost' IDENTIFIED BY 'read_user2pass';
	CREATE USER 'rw_user1'@'localhost' IDENTIFIED BY 'rw_user1pass';

	GRANT 'app_developer' TO 'dev1'@'localhost';
	GRANT 'app_read' TO 'read_user1'@'localhost', 'read_user2'@'localhost';
	GRANT 'app_read', 'app_write' TO 'rw_user1'@'localhost';
	#SET PERSIST mandatory_roles  = 'role1,role2@localhost,r3@%.example.com'; # it also global # to all users!

	#Activating Roles  on login!!!
	SET DEFAULT ROLE ALL TO
	  'dev1'@'localhost',
	  'read_user1'@'localhost',
	  'read_user2'@'localhost',
	  'rw_user1'@'localhost';
	#OR
	#SET PERSIST activate_all_roles_on_login = True;
	  
	SELECT CURRENT_ROLE();




	GRANT SELECT, INSERT
	  ON TABLE sakila.actor
	TO 'newuser'@'%';


/* whole procedure ends with the custom delimiter */
END$$

DELIMITER ;

-- -----------------------------------------------------
-- function SET_DEP
-- -----------------------------------------------------

USE `kcson`;
DROP function IF EXISTS `kcson`.`SET_DEP`;

DELIMITER $$
USE `kcson`$$
CREATE DEFINER=`root`@`localhost` FUNCTION `SET_DEP`(
	`depId` INT
) RETURNS int(11)
    MODIFIES SQL DATA
    COMMENT 'set default department (with checking is it possible)'
BEGIN
	declare wrkID int ;
	declare res int default 0;
	set  wrkID=get_WID();
	
	set res = (select dep_id from dep_has_worker  where worker_id=wrkID and dep_id=depId);
	
	if res > 0 then 
		update worker_settings set last_dep=depId where id = wrkID;
		#update worker_has_dep set active=0 where(worker_id=wrkID);
		#update worker_has_dep set active=1 where(worker_id=wrkID and dep_id=depId);
		return depId;
	else
		return 0;
	end if;
END$$

DELIMITER ;

-- -----------------------------------------------------
-- procedure import_serv_all
-- -----------------------------------------------------

USE `kcson`;
DROP procedure IF EXISTS `kcson`.`import_serv_all`;

DELIMITER $$
USE `kcson`$$
CREATE DEFINER=`root`@`localhost` PROCEDURE `import_serv_all`()
BEGIN
START TRANSACTION;
#USE `kcson`;
INSERT INTO `kcson`.`serv` (`id`, `serv_tnum`, `serv_name`, `year`, `sub_serv`, `sub_serv_str`, `price`, `2ndprice`, `3rdprice`, `active`, `total`) VALUES (1, 'Итог', 'Итого:', 2019,0 , '',0 ,0 , 0, 1, 1);
INSERT INTO `kcson`.`serv` (`id`, `serv_tnum`, `serv_name`, `year`, `sub_serv`, `sub_serv_str`, `price`, `2ndprice`, `3rdprice`, `active`, `total`) VALUES (2, '1', 'В форме социального обслуживания на дому', 2019, 1, 'Итог',0 ,0 , 0, 1, 1);
INSERT INTO `kcson`.`serv` (`id`, `serv_tnum`, `serv_name`, `year`, `sub_serv`, `sub_serv_str`, `price`, `2ndprice`, `3rdprice`, `active`, `total`) VALUES (3, '1.1', 'Социально-бытовые услуги:', 2019, 2, '1',0 ,0 , 0, 1, 1);
INSERT INTO `kcson`.`serv` (`id`, `serv_tnum`, `serv_name`, `year`, `sub_serv`, `sub_serv_str`, `price`, `2ndprice`, `3rdprice`, `active`, `total`) VALUES (4, '1.1.1', 'Покупка за счет средств получателя социальных услуг и доставка на дом продуктов питания, промышленных товаров первой необходимости, средств санитарии и гигиены, средств ухода', 2019, 3, '1.1', 245.29, 245.29, 0, 1, 0);
INSERT INTO `kcson`.`serv` (`id`, `serv_tnum`, `serv_name`, `year`, `sub_serv`, `sub_serv_str`, `price`, `2ndprice`, `3rdprice`, `active`, `total`) VALUES (5, '1.1.2', 'Помощь в приготовлении пищи', 2019, 3, '1.1', 183.48, 183.48, 0, 1, 0);
INSERT INTO `kcson`.`serv` (`id`, `serv_tnum`, `serv_name`, `year`, `sub_serv`, `sub_serv_str`, `price`, `2ndprice`, `3rdprice`, `active`, `total`) VALUES (6, '1.1.3', 'Помощь в приеме пищи (кормление)', 2019, 3, '1.1', 212.02, 212.02, 0, 1, 0);
INSERT INTO `kcson`.`serv` (`id`, `serv_tnum`, `serv_name`, `year`, `sub_serv`, `sub_serv_str`, `price`, `2ndprice`, `3rdprice`, `active`, `total`) VALUES (7, '1.1.4', 'Помощь в одевании и переодевании лицам, не способным по состоянию здоровья самостоятельно осуществлять за собой уход', 2019, 3, '1.1', 191.82, 191.82, 0, 1, 0);
INSERT INTO `kcson`.`serv` (`id`, `serv_tnum`, `serv_name`, `year`, `sub_serv`, `sub_serv_str`, `price`, `2ndprice`, `3rdprice`, `active`, `total`) VALUES (8, '1.1.5', 'Смена (помощь в смене) постельного белья', 2019, 3, '1.1', 89.71, 89.71, 0, 1, 0);
INSERT INTO `kcson`.`serv` (`id`, `serv_tnum`, `serv_name`, `year`, `sub_serv`, `sub_serv_str`, `price`, `2ndprice`, `3rdprice`, `active`, `total`) VALUES (9, '1.1.6', 'Смена подгузников и абсорбирующего белья лицам, не способным по состоянию здоровья самостоятельно осуществлять за собой уход', 2019, 3, '1.1', 89.71, 89.71, 0, 1, 0);
INSERT INTO `kcson`.`serv` (`id`, `serv_tnum`, `serv_name`, `year`, `sub_serv`, `sub_serv_str`, `price`, `2ndprice`, `3rdprice`, `active`, `total`) VALUES (10, '1.1.7', 'Предоставление гигиенических услуг лицам, не способным по состоянию здоровья самостоятельно осуществлять за собой уход', 2019, 3, '1.1', 150.87, 150.87, 0, 1, 0);
INSERT INTO `kcson`.`serv` (`id`, `serv_tnum`, `serv_name`, `year`, `sub_serv`, `sub_serv_str`, `price`, `2ndprice`, `3rdprice`, `active`, `total`) VALUES (11, '1.1.8', 'Содействие за счет средств получателя социальных услуг в оказании парикмахерских услуг', 2019, 3, '1.1', 61.16, 61.16, 0, 1, 0);
INSERT INTO `kcson`.`serv` (`id`, `serv_tnum`, `serv_name`, `year`, `sub_serv`, `sub_serv_str`, `price`, `2ndprice`, `3rdprice`, `active`, `total`) VALUES (12, '1.1.9', 'Сопровождение в баню (для проживающих в жилых помещениях без горячего водоснабжения)', 2019, 3, '1.1', 733.89, 733.89, 0, 1, 0);
INSERT INTO `kcson`.`serv` (`id`, `serv_tnum`, `serv_name`, `year`, `sub_serv`, `sub_serv_str`, `price`, `2ndprice`, `3rdprice`, `active`, `total`) VALUES (13, '1.1.10', 'Вызов врача на дом, в том числе запись на прием к врачу', 2019, 3, '1.1', 183.48, 183.48, 0, 1, 0);
INSERT INTO `kcson`.`serv` (`id`, `serv_tnum`, `serv_name`, `year`, `sub_serv`, `sub_serv_str`, `price`, `2ndprice`, `3rdprice`, `active`, `total`) VALUES (14, '1.1.11', 'Сопровождение к врачу', 2019, 3, '1.1', 733.89, 733.89, 0, 1, 0);
INSERT INTO `kcson`.`serv` (`id`, `serv_tnum`, `serv_name`, `year`, `sub_serv`, `sub_serv_str`, `price`, `2ndprice`, `3rdprice`, `active`, `total`) VALUES (15, '1.1.12', 'Содействие в получении лекарственных препаратов, изделий медицинского назначения, предоставляемых в соответствии с действующим законодательством', 2019, 3, '1.1', 550.42, 550.42, 0, 1, 0);
INSERT INTO `kcson`.`serv` (`id`, `serv_tnum`, `serv_name`, `year`, `sub_serv`, `sub_serv_str`, `price`, `2ndprice`, `3rdprice`, `active`, `total`) VALUES (16, '1.1.13', 'Содействие в организации санаторно-курортного лечения или оздоровительного отдыха, предоставляемого в соответствии с действующим законодательством', 2019, 3, '1.1', 460.13, 460.13, 0, 1, 0);
INSERT INTO `kcson`.`serv` (`id`, `serv_tnum`, `serv_name`, `year`, `sub_serv`, `sub_serv_str`, `price`, `2ndprice`, `3rdprice`, `active`, `total`) VALUES (17, '1.1.14', 'Помощь при подготовке вещей для выезда на отдых за пределы города', 2019, 3, '1.1', 197.2, 197.2, 0, 1, 0);
INSERT INTO `kcson`.`serv` (`id`, `serv_tnum`, `serv_name`, `year`, `sub_serv`, `sub_serv_str`, `price`, `2ndprice`, `3rdprice`, `active`, `total`) VALUES (18, '1.1.15', 'Сдача за счет средств получателя социальных услуг вещей в стирку, химчистку, ремонт, обратная их доставка', 2019, 3, '1.1', 150.87, 150.87, 0, 1, 0);
INSERT INTO `kcson`.`serv` (`id`, `serv_tnum`, `serv_name`, `year`, `sub_serv`, `sub_serv_str`, `price`, `2ndprice`, `3rdprice`, `active`, `total`) VALUES (19, '1.1.16', 'Содействие в обеспечении топливом (для проживающих в жилых помещениях без центрального отопления)', 2019, 3, '1.1', 122.31, 122.31, 0, 1, 0);
INSERT INTO `kcson`.`serv` (`id`, `serv_tnum`, `serv_name`, `year`, `sub_serv`, `sub_serv_str`, `price`, `2ndprice`, `3rdprice`, `active`, `total`) VALUES (20, '1.1.17', 'Топка печей (для проживающих в жилых помещениях без центрального отопления)', 2019, 3, '1.1', 183.48, 183.48, 0, 1, 0);
INSERT INTO `kcson`.`serv` (`id`, `serv_tnum`, `serv_name`, `year`, `sub_serv`, `sub_serv_str`, `price`, `2ndprice`, `3rdprice`, `active`, `total`) VALUES (21, '1.1.18', 'Доставка воды (для проживающих в жилых помещениях без центрального водоснабжения)', 2019, 3, '1.1', 122.31, 122.31, 0, 1, 0);
INSERT INTO `kcson`.`serv` (`id`, `serv_tnum`, `serv_name`, `year`, `sub_serv`, `sub_serv_str`, `price`, `2ndprice`, `3rdprice`, `active`, `total`) VALUES (22, '1.1.19', 'Организация помощи в проведении за счет средств получателя социальных услуг ремонта жилых помещений', 2019, 3, '1.1', 244.9, 244.9, 0, 1, 0);
INSERT INTO `kcson`.`serv` (`id`, `serv_tnum`, `serv_name`, `year`, `sub_serv`, `sub_serv_str`, `price`, `2ndprice`, `3rdprice`, `active`, `total`) VALUES (23, '1.1.20', 'Содействие в проведении за счет средств получателя социальных услуг уборки жилых помещений, мытья окон', 2019, 3, '1.1', 122.45, 122.45, 0, 1, 0);
INSERT INTO `kcson`.`serv` (`id`, `serv_tnum`, `serv_name`, `year`, `sub_serv`, `sub_serv_str`, `price`, `2ndprice`, `3rdprice`, `active`, `total`) VALUES (24, '1.1.21', 'Вынос мусора', 2019, 3, '1.1', 120.29, 120.29, 0, 1, 0);
INSERT INTO `kcson`.`serv` (`id`, `serv_tnum`, `serv_name`, `year`, `sub_serv`, `sub_serv_str`, `price`, `2ndprice`, `3rdprice`, `active`, `total`) VALUES (25, '1.1.22', 'Оплата за счет средств получателя социальных услуг жилищно-коммунальных услуг и услуг связи', 2019, 3, '1.1', 183.66, 183.66, 0, 1, 0);
INSERT INTO `kcson`.`serv` (`id`, `serv_tnum`, `serv_name`, `year`, `sub_serv`, `sub_serv_str`, `price`, `2ndprice`, `3rdprice`, `active`, `total`) VALUES (26, '1.1.23', 'Оформление за счет средств получателя социальных услуг подписки на газеты и журналы', 2019, 3, '1.1', 184.13, 184.13, 0, 1, 0);
INSERT INTO `kcson`.`serv` (`id`, `serv_tnum`, `serv_name`, `year`, `sub_serv`, `sub_serv_str`, `price`, `2ndprice`, `3rdprice`, `active`, `total`) VALUES (27, '1.1.24', 'Отправка за счет средств получателя социальных услуг почтовой корреспонденции', 2019, 3, '1.1', 122.31, 122.31, 0, 1, 0);
INSERT INTO `kcson`.`serv` (`id`, `serv_tnum`, `serv_name`, `year`, `sub_serv`, `sub_serv_str`, `price`, `2ndprice`, `3rdprice`, `active`, `total`) VALUES (28, '1.1.25', 'Обеспечение кратковременного присмотра за детьми', 2019, 3, '1.1', 733.89, 733.89, 0, 1, 0);
INSERT INTO `kcson`.`serv` (`id`, `serv_tnum`, `serv_name`, `year`, `sub_serv`, `sub_serv_str`, `price`, `2ndprice`, `3rdprice`, `active`, `total`) VALUES (29, '1.1.26', 'Консультирование по вопросам оборудования специальными средствами и приспособлениями жилого помещения, занимаемого получателем социальных услуг (для инвалидов (детей-инвалидов), имеющих стойкие расстройства опорно-двигательного аппарата, зрения, слуха, умственные отклонения)', 2019, 3, '1.1', 366.94, 366.94, 0, 1, 0);
INSERT INTO `kcson`.`serv` (`id`, `serv_tnum`, `serv_name`, `year`, `sub_serv`, `sub_serv_str`, `price`, `2ndprice`, `3rdprice`, `active`, `total`) VALUES (30, '1.1.27', 'Содействие в оформлении документов и выдача напрокат технических средств реабилитации', 2019, 3, '1.1', 371.87, 371.87, 0, 1, 0);
INSERT INTO `kcson`.`serv` (`id`, `serv_tnum`, `serv_name`, `year`, `sub_serv`, `sub_serv_str`, `price`, `2ndprice`, `3rdprice`, `active`, `total`) VALUES (31, '1.1.28', 'Содействие в обеспечении техническими средствами реабилитации, предоставляемыми в соответствии с действующим законодательством либо за счет средств получателя социальных услуг', 2019, 3, '1.1', 555.35, 555.35, 0, 1, 0);
INSERT INTO `kcson`.`serv` (`id`, `serv_tnum`, `serv_name`, `year`, `sub_serv`, `sub_serv_str`, `price`, `2ndprice`, `3rdprice`, `active`, `total`) VALUES (32, '1.1.29', 'Оповещение родственников', 2019, 3, '1.1', 125.23, 125.23, 0, 1, 0);
INSERT INTO `kcson`.`serv` (`id`, `serv_tnum`, `serv_name`, `year`, `sub_serv`, `sub_serv_str`, `price`, `2ndprice`, `3rdprice`, `active`, `total`) VALUES (33, '1.1.30', 'Организация (содействие в оказании) ритуальных услуг', 2019, 3, '1.1', 375.67, 375.67, 0, 1, 0);
INSERT INTO `kcson`.`serv` (`id`, `serv_tnum`, `serv_name`, `year`, `sub_serv`, `sub_serv_str`, `price`, `2ndprice`, `3rdprice`, `active`, `total`) VALUES (34, '1.1.31', 'Консультирование по вопросам самообслуживания и социально-бытовой адаптации', 2019, 3, '1.1', 122.31, 122.31, 0, 1, 0);
INSERT INTO `kcson`.`serv` (`id`, `serv_tnum`, `serv_name`, `year`, `sub_serv`, `sub_serv_str`, `price`, `2ndprice`, `3rdprice`, `active`, `total`) VALUES (35, '1.1.32', 'Предоставление лицам, нуждающимся по состоянию здоровья, специализированных услуг экстренной помощи «тревожная кнопка»:', 2019, 3, '1.1',0 ,0 , 0, 1, 1);
INSERT INTO `kcson`.`serv` (`id`, `serv_tnum`, `serv_name`, `year`, `sub_serv`, `sub_serv_str`, `price`, `2ndprice`, `3rdprice`, `active`, `total`) VALUES (36, '1.1.32.1', 'монтаж, подключение, программирование функций устройства для предоставления получателю социальной услуги «Предоставление лицам, нуждающимся по состоянию здоровья, специализированных услуг экстренной помощи «тревожная кнопка»', 2019, 35, '1.1.32', 362.95, 362.95, 0, 1, 0);
INSERT INTO `kcson`.`serv` (`id`, `serv_tnum`, `serv_name`, `year`, `sub_serv`, `sub_serv_str`, `price`, `2ndprice`, `3rdprice`, `active`, `total`) VALUES (37, '1.1.32.2', 'обслуживание получателя социальной услуги «Предоставление лицам, нуждающимся по состоянию здоровья, специализированных услуг экстренной помощи «тревожная кнопка»', 2019, 35, '1.1.32', 686.1, 686.1, 0, 1, 0);
INSERT INTO `kcson`.`serv` (`id`, `serv_tnum`, `serv_name`, `year`, `sub_serv`, `sub_serv_str`, `price`, `2ndprice`, `3rdprice`, `active`, `total`) VALUES (38, '1.2', 'Социально-медицинские услуги:', 2019, 2, '1',0 ,0 , 0, 1, 1);
INSERT INTO `kcson`.`serv` (`id`, `serv_tnum`, `serv_name`, `year`, `sub_serv`, `sub_serv_str`, `price`, `2ndprice`, `3rdprice`, `active`, `total`) VALUES (39, '1.2.1', 'Консультирование по социально-медицинским вопросам', 2019, 38, '1.2', 127.78, 127.78, 0, 1, 0);
INSERT INTO `kcson`.`serv` (`id`, `serv_tnum`, `serv_name`, `year`, `sub_serv`, `sub_serv_str`, `price`, `2ndprice`, `3rdprice`, `active`, `total`) VALUES (40, '1.2.2', 'Систематическое наблюдение за получателем социальных услуг в целях выявления отклонений в состоянии его здоровья', 2019, 38, '1.2', 175.74, 175.74, 0, 1, 0);
INSERT INTO `kcson`.`serv` (`id`, `serv_tnum`, `serv_name`, `year`, `sub_serv`, `sub_serv_str`, `price`, `2ndprice`, `3rdprice`, `active`, `total`) VALUES (41, '1.2.3', 'Выполнение процедур, связанных с организацией ухода, наблюдением за состоянием здоровья получателя социальных услуг', 2019, 38, '1.2', 362.93, 362.93, 0, 1, 0);
INSERT INTO `kcson`.`serv` (`id`, `serv_tnum`, `serv_name`, `year`, `sub_serv`, `sub_serv_str`, `price`, `2ndprice`, `3rdprice`, `active`, `total`) VALUES (42, '1.2.4', 'Обеспечение приема получателем социальных услуг лекарственных средств в соответствии с назначением врача', 2019, 38, '1.2', 83.27, 83.27, 0, 1, 0);
INSERT INTO `kcson`.`serv` (`id`, `serv_tnum`, `serv_name`, `year`, `sub_serv`, `sub_serv_str`, `price`, `2ndprice`, `3rdprice`, `active`, `total`) VALUES (43, '1.2.5', 'Проведение мероприятий, направленных на формирование здорового образа жизни', 2019, 38, '1.2', 183.48, 183.48, 0, 1, 0);
INSERT INTO `kcson`.`serv` (`id`, `serv_tnum`, `serv_name`, `year`, `sub_serv`, `sub_serv_str`, `price`, `2ndprice`, `3rdprice`, `active`, `total`) VALUES (44, '1.3', 'Социально-психологические услуги:', 2019, 2, '1',0 ,0 , 0, 1, 1);
INSERT INTO `kcson`.`serv` (`id`, `serv_tnum`, `serv_name`, `year`, `sub_serv`, `sub_serv_str`, `price`, `2ndprice`, `3rdprice`, `active`, `total`) VALUES (45, '1.3.1', 'Социально-психологическое консультирование (в том числе по вопросам внутрисемейных отношений)', 2019, 44, '1.3',0 , 437.1, 0, 1, 0);
INSERT INTO `kcson`.`serv` (`id`, `serv_tnum`, `serv_name`, `year`, `sub_serv`, `sub_serv_str`, `price`, `2ndprice`, `3rdprice`, `active`, `total`) VALUES (46, '1.3.2', 'Социально-психологический патронаж', 2019, 44, '1.3',0 , 293.96, 0, 1, 0);
INSERT INTO `kcson`.`serv` (`id`, `serv_tnum`, `serv_name`, `year`, `sub_serv`, `sub_serv_str`, `price`, `2ndprice`, `3rdprice`, `active`, `total`) VALUES (47, '1.4', 'Социально-педагогические услуги:', 2019, 2, '1',0 ,0 , 0, 1, 1);
INSERT INTO `kcson`.`serv` (`id`, `serv_tnum`, `serv_name`, `year`, `sub_serv`, `sub_serv_str`, `price`, `2ndprice`, `3rdprice`, `active`, `total`) VALUES (48, '1.4.1', 'Консультирование получателя социальных услуг и (или) его ближайшего окружения по вопросам социальной реабилитации', 2019, 47, '1.4',0 , 214.49, 0, 1, 0);
INSERT INTO `kcson`.`serv` (`id`, `serv_tnum`, `serv_name`, `year`, `sub_serv`, `sub_serv_str`, `price`, `2ndprice`, `3rdprice`, `active`, `total`) VALUES (49, '1.4.2', 'Обучение практическим навыкам общего ухода за тяжелобольными получателями социальных услуг, получателями социальных услуг, имеющими ограничения жизнедеятельности, в том числе за детьми-инвалидами', 2019, 47, '1.4',0 , 176.21, 0, 1, 0);
INSERT INTO `kcson`.`serv` (`id`, `serv_tnum`, `serv_name`, `year`, `sub_serv`, `sub_serv_str`, `price`, `2ndprice`, `3rdprice`, `active`, `total`) VALUES (50, '1.4.3', 'Чтение журналов, газет, книг', 2019, 47, '1.4',0 , 366.94, 0, 1, 0);
INSERT INTO `kcson`.`serv` (`id`, `serv_tnum`, `serv_name`, `year`, `sub_serv`, `sub_serv_str`, `price`, `2ndprice`, `3rdprice`, `active`, `total`) VALUES (51, '1.5', 'Социально-трудовые услуги:', 2019, 2, '1',0 ,0 , 0, 1, 1);
INSERT INTO `kcson`.`serv` (`id`, `serv_tnum`, `serv_name`, `year`, `sub_serv`, `sub_serv_str`, `price`, `2ndprice`, `3rdprice`, `active`, `total`) VALUES (52, '1.5.1', 'Содействие родственникам получателя социальных услуг в нахождении работы по гибкому графику', 2019, 51, '1.5',0 , 212.6, 0, 1, 0);
INSERT INTO `kcson`.`serv` (`id`, `serv_tnum`, `serv_name`, `year`, `sub_serv`, `sub_serv_str`, `price`, `2ndprice`, `3rdprice`, `active`, `total`) VALUES (53, '1.6', 'Социально-правовые услуги:', 2019, 2, '1',0 ,0 , 0, 1, 1);
INSERT INTO `kcson`.`serv` (`id`, `serv_tnum`, `serv_name`, `year`, `sub_serv`, `sub_serv_str`, `price`, `2ndprice`, `3rdprice`, `active`, `total`) VALUES (54, '1.6.1', 'Оказание помощи в оформлении документов и восстановлении утраченных документов получателя социальных услуг', 2019, 53, '1.6',0 , 149.17, 0, 1, 0);
INSERT INTO `kcson`.`serv` (`id`, `serv_tnum`, `serv_name`, `year`, `sub_serv`, `sub_serv_str`, `price`, `2ndprice`, `3rdprice`, `active`, `total`) VALUES (55, '1.6.2', 'Содействие в получении полиса обязательного медицинского страхования', 2019, 53, '1.6',0 , 461.26, 0, 1, 0);
INSERT INTO `kcson`.`serv` (`id`, `serv_tnum`, `serv_name`, `year`, `sub_serv`, `sub_serv_str`, `price`, `2ndprice`, `3rdprice`, `active`, `total`) VALUES (56, '1.6.3', 'Содействие в оформлении документов, необходимых для помещения в стационарную организацию социального обслуживания', 2019, 53, '1.6',0 , 550.42, 0, 1, 0);
INSERT INTO `kcson`.`serv` (`id`, `serv_tnum`, `serv_name`, `year`, `sub_serv`, `sub_serv_str`, `price`, `2ndprice`, `3rdprice`, `active`, `total`) VALUES (57, '1.6.4', 'Содействие в восстановлении утраченного (сохранении занимаемого) жилья, наследства', 2019, 53, '1.6',0 , 435.25, 0, 1, 0);
INSERT INTO `kcson`.`serv` (`id`, `serv_tnum`, `serv_name`, `year`, `sub_serv`, `sub_serv_str`, `price`, `2ndprice`, `3rdprice`, `active`, `total`) VALUES (58, '1.6.5', 'Оказание помощи в получении юридических услуг (в том числе бесплатно)', 2019, 53, '1.6',0 , 866.53, 0, 1, 0);
INSERT INTO `kcson`.`serv` (`id`, `serv_tnum`, `serv_name`, `year`, `sub_serv`, `sub_serv_str`, `price`, `2ndprice`, `3rdprice`, `active`, `total`) VALUES (59, '1.6.6', 'Оказание помощи в защите прав и законных интересов получателя социальных услуг', 2019, 53, '1.6',0 , 197.23, 0, 1, 0);
INSERT INTO `kcson`.`serv` (`id`, `serv_tnum`, `serv_name`, `year`, `sub_serv`, `sub_serv_str`, `price`, `2ndprice`, `3rdprice`, `active`, `total`) VALUES (60, '1.7', 'Услуги в целях повышения коммуникативного потенциала получателей социальных услуг, имеющих ограничения жизнедеятельности, в том числе детей-инвалидов:', 2019, 2, '1',0 ,0 , 0, 1, 1);
INSERT INTO `kcson`.`serv` (`id`, `serv_tnum`, `serv_name`, `year`, `sub_serv`, `sub_serv_str`, `price`, `2ndprice`, `3rdprice`, `active`, `total`) VALUES (61, '1.7.1', 'Консультирование по вопросам социально-средовой реабилитации', 2019, 60, '1.7',0 , 368.08, 0, 1, 0);
INSERT INTO `kcson`.`serv` (`id`, `serv_tnum`, `serv_name`, `year`, `sub_serv`, `sub_serv_str`, `price`, `2ndprice`, `3rdprice`, `active`, `total`) VALUES (62, '1.7.2', 'Обучение инвалидов (детей-инвалидов) пользованию средствами ухода и техническими средствами реабилитации', 2019, 60, '1.7',0 , 230.06, 0, 1, 0);
INSERT INTO `kcson`.`serv` (`id`, `serv_tnum`, `serv_name`, `year`, `sub_serv`, `sub_serv_str`, `price`, `2ndprice`, `3rdprice`, `active`, `total`) VALUES (63, '1.7.3', 'Обучение навыкам (поддержание навыков) поведения в быту и общественных местах', 2019, 60, '1.7',0 , 282.58, 0, 1, 0);
INSERT INTO `kcson`.`serv` (`id`, `serv_tnum`, `serv_name`, `year`, `sub_serv`, `sub_serv_str`, `price`, `2ndprice`, `3rdprice`, `active`, `total`) VALUES (64, '2', 'В полустационарной форме социального обслуживания', 2019, 1, 'Итог',0 ,0 , 0, 1, 1);
INSERT INTO `kcson`.`serv` (`id`, `serv_tnum`, `serv_name`, `year`, `sub_serv`, `sub_serv_str`, `price`, `2ndprice`, `3rdprice`, `active`, `total`) VALUES (65, '2.1', 'Социально-бытовые услуги:', 2019, 64, '2',0 ,0 , 0, 1, 1);
INSERT INTO `kcson`.`serv` (`id`, `serv_tnum`, `serv_name`, `year`, `sub_serv`, `sub_serv_str`, `price`, `2ndprice`, `3rdprice`, `active`, `total`) VALUES (66, '2.1.1', 'Обеспечение площадью жилых помещений в соответствии с утвержденными нормативами', 2019, 65, '2.1', 190.4, 190.4, 0, 1, 0);
INSERT INTO `kcson`.`serv` (`id`, `serv_tnum`, `serv_name`, `year`, `sub_serv`, `sub_serv_str`, `price`, `2ndprice`, `3rdprice`, `active`, `total`) VALUES (67, '2.1.2', 'Обеспечение мягким инвентарем (одеждой, обувью, нательным бельем и постельными принадлежностями) в соответствии с утвержденными нормативами*:', 2019, 65, '2.1',0 ,0 , 0, 1, 1);
INSERT INTO `kcson`.`serv` (`id`, `serv_tnum`, `serv_name`, `year`, `sub_serv`, `sub_serv_str`, `price`, `2ndprice`, `3rdprice`, `active`, `total`) VALUES (68, '2.1.2.1', 'гражданам пожилого и трудоспособного возраста без определенного места жительства (бездомным)', 2019, 67, '2.1.2', 97.09, 97.09, 0, 1, 0);
INSERT INTO `kcson`.`serv` (`id`, `serv_tnum`, `serv_name`, `year`, `sub_serv`, `sub_serv_str`, `price`, `2ndprice`, `3rdprice`, `active`, `total`) VALUES (69, '2.1.3', 'Обеспечение питанием согласно утвержденным нормативам**:', 2019, 65, '2.1',0 ,0 , 0, 1, 1);
INSERT INTO `kcson`.`serv` (`id`, `serv_tnum`, `serv_name`, `year`, `sub_serv`, `sub_serv_str`, `price`, `2ndprice`, `3rdprice`, `active`, `total`) VALUES (70, '2.1.3.1', 'граждан пожилого возраста и инвалидов, находящихся в учреждениях социального обслуживания населения, за исключением психоневрологических интернатов', 2019, 69, '2.1.3', 382.91, 382.91, 0, 1, 0);
INSERT INTO `kcson`.`serv` (`id`, `serv_tnum`, `serv_name`, `year`, `sub_serv`, `sub_serv_str`, `price`, `2ndprice`, `3rdprice`, `active`, `total`) VALUES (71, '2.1.3.2', 'граждан пожилого возраста и инвалидов при заболеваниях сахарным диабетом, находящихся в учреждениях социального обслуживания населения, за исключением психоневрологических интернатов', 2019, 69, '2.1.3', 367.87, 367.87, 0, 1, 0);
INSERT INTO `kcson`.`serv` (`id`, `serv_tnum`, `serv_name`, `year`, `sub_serv`, `sub_serv_str`, `price`, `2ndprice`, `3rdprice`, `active`, `total`) VALUES (72, '2.1.3.3', 'граждан пожилого возраста и инвалидов, находящихся в учреждениях социального обслуживания населения - психоневрологических интернатах', 2019, 69, '2.1.3', 424.89, 424.89, 0, 1, 0);
INSERT INTO `kcson`.`serv` (`id`, `serv_tnum`, `serv_name`, `year`, `sub_serv`, `sub_serv_str`, `price`, `2ndprice`, `3rdprice`, `active`, `total`) VALUES (73, '2.1.3.4', 'граждан пожилого возраста и инвалидов при заболеваниях сахарным диабетом, находящихся в учреждениях социального обслуживания населения - психоневрологических интернатах', 2019, 69, '2.1.3', 380.46, 380.46, 0, 1, 0);
INSERT INTO `kcson`.`serv` (`id`, `serv_tnum`, `serv_name`, `year`, `sub_serv`, `sub_serv_str`, `price`, `2ndprice`, `3rdprice`, `active`, `total`) VALUES (74, '2.1.3.5', 'беременных женщин в учреждениях социального обслуживания населения', 2019, 69, '2.1.3', 391.21, 391.21, 0, 1, 0);
INSERT INTO `kcson`.`serv` (`id`, `serv_tnum`, `serv_name`, `year`, `sub_serv`, `sub_serv_str`, `price`, `2ndprice`, `3rdprice`, `active`, `total`) VALUES (75, '2.1.3.6', 'кормящих матерей в учреждениях социального обслуживания населения', 2019, 69, '2.1.3', 363.84, 363.84, 0, 1, 0);
INSERT INTO `kcson`.`serv` (`id`, `serv_tnum`, `serv_name`, `year`, `sub_serv`, `sub_serv_str`, `price`, `2ndprice`, `3rdprice`, `active`, `total`) VALUES (76, '2.1.3.7', 'детей первого года жизни от 0-4 мес., проживающих с матерями - получателями социальных услуг', 2019, 69, '2.1.3', 152.93, 152.93, 0, 1, 0);
INSERT INTO `kcson`.`serv` (`id`, `serv_tnum`, `serv_name`, `year`, `sub_serv`, `sub_serv_str`, `price`, `2ndprice`, `3rdprice`, `active`, `total`) VALUES (77, '2.1.3.8', 'детей первого года жизни от 4-6 мес., проживающих с матерями - получателями социальных услуг', 2019, 69, '2.1.3', 219, 219, 0, 1, 0);
INSERT INTO `kcson`.`serv` (`id`, `serv_tnum`, `serv_name`, `year`, `sub_serv`, `sub_serv_str`, `price`, `2ndprice`, `3rdprice`, `active`, `total`) VALUES (78, '2.1.3.9', 'детей первого года жизни от 6-9 мес., проживающих с матерями - получателями социальных услуг', 2019, 69, '2.1.3', 232.71, 232.71, 0, 1, 0);
INSERT INTO `kcson`.`serv` (`id`, `serv_tnum`, `serv_name`, `year`, `sub_serv`, `sub_serv_str`, `price`, `2ndprice`, `3rdprice`, `active`, `total`) VALUES (79, '2.1.3.10', 'детей первого года жизни от 9-12 мес., проживающих с матерями - получателями социальных услуг', 2019, 69, '2.1.3', 377.56, 377.56, 0, 1, 0);
INSERT INTO `kcson`.`serv` (`id`, `serv_tnum`, `serv_name`, `year`, `sub_serv`, `sub_serv_str`, `price`, `2ndprice`, `3rdprice`, `active`, `total`) VALUES (80, '2.1.3.11', 'детей в возрасте от 1 до 3 лет', 2019, 69, '2.1.3', 203.48, 203.48, 0, 1, 0);
INSERT INTO `kcson`.`serv` (`id`, `serv_tnum`, `serv_name`, `year`, `sub_serv`, `sub_serv_str`, `price`, `2ndprice`, `3rdprice`, `active`, `total`) VALUES (81, '2.1.3.12', 'детей в возрасте от 3 до 7 лет', 2019, 69, '2.1.3', 354.4, 354.4, 0, 1, 0);
INSERT INTO `kcson`.`serv` (`id`, `serv_tnum`, `serv_name`, `year`, `sub_serv`, `sub_serv_str`, `price`, `2ndprice`, `3rdprice`, `active`, `total`) VALUES (82, '2.1.3.13', 'детей в возрасте от 7 до 11лет', 2019, 69, '2.1.3', 417.96, 417.96, 0, 1, 0);
INSERT INTO `kcson`.`serv` (`id`, `serv_tnum`, `serv_name`, `year`, `sub_serv`, `sub_serv_str`, `price`, `2ndprice`, `3rdprice`, `active`, `total`) VALUES (83, '2.1.3.14', 'детей в возрасте от 12 до 18 лет', 2019, 69, '2.1.3', 470.15, 470.15, 0, 1, 0);
INSERT INTO `kcson`.`serv` (`id`, `serv_tnum`, `serv_name`, `year`, `sub_serv`, `sub_serv_str`, `price`, `2ndprice`, `3rdprice`, `active`, `total`) VALUES (84, '2.1.3.15', 'граждан без определенного места жительства (бездомных)', 2019, 69, '2.1.3', 105.06, 105.06, 0, 1, 0);
INSERT INTO `kcson`.`serv` (`id`, `serv_tnum`, `serv_name`, `year`, `sub_serv`, `sub_serv_str`, `price`, `2ndprice`, `3rdprice`, `active`, `total`) VALUES (85, '2.1.4', 'Обеспечение бесплатным горячим питанием или набором продуктов:', 2019, 65, '2.1',0 ,0 , 0, 1, 1);
INSERT INTO `kcson`.`serv` (`id`, `serv_tnum`, `serv_name`, `year`, `sub_serv`, `sub_serv_str`, `price`, `2ndprice`, `3rdprice`, `active`, `total`) VALUES (86, '2.1.4.1', 'Обеспечение бесплатным горячим питанием', 2019, 85, '2.1.4', 196.93, 196.93, 0, 1, 0);
INSERT INTO `kcson`.`serv` (`id`, `serv_tnum`, `serv_name`, `year`, `sub_serv`, `sub_serv_str`, `price`, `2ndprice`, `3rdprice`, `active`, `total`) VALUES (87, '2.1.4.2', 'Обеспечение бесплатным набором продуктов', 2019, 85, '2.1.4', 506.45, 506.45, 0, 1, 0);
INSERT INTO `kcson`.`serv` (`id`, `serv_tnum`, `serv_name`, `year`, `sub_serv`, `sub_serv_str`, `price`, `2ndprice`, `3rdprice`, `active`, `total`) VALUES (88, '2.1.5', 'Помощь в одевании и переодевании лицам, не способным по состоянию здоровья самостоятельно осуществлять за собой уход', 2019, 65, '2.1', 182.81, 182.81, 0, 1, 0);
INSERT INTO `kcson`.`serv` (`id`, `serv_tnum`, `serv_name`, `year`, `sub_serv`, `sub_serv_str`, `price`, `2ndprice`, `3rdprice`, `active`, `total`) VALUES (89, '2.1.6', 'Смена подгузников и абсорбирующего белья лицам, не способным по состоянию здоровья самостоятельно осуществлять за собой уход', 2019, 65, '2.1', 155.9, 155.9, 0, 1, 0);
INSERT INTO `kcson`.`serv` (`id`, `serv_tnum`, `serv_name`, `year`, `sub_serv`, `sub_serv_str`, `price`, `2ndprice`, `3rdprice`, `active`, `total`) VALUES (90, '2.1.7', 'Предоставление гигиенических услуг лицам, не способным по состоянию здоровья самостоятельно осуществлять за собой уход', 2019, 65, '2.1', 130.89, 130.89, 0, 1, 0);
INSERT INTO `kcson`.`serv` (`id`, `serv_tnum`, `serv_name`, `year`, `sub_serv`, `sub_serv_str`, `price`, `2ndprice`, `3rdprice`, `active`, `total`) VALUES (91, '2.1.8', 'Содействие в организации санаторно-курортного лечения или оздоровительного отдыха, предоставляемого в соответствии с действующим законодательством', 2019, 65, '2.1', 460.13, 460.13, 0, 1, 0);
INSERT INTO `kcson`.`serv` (`id`, `serv_tnum`, `serv_name`, `year`, `sub_serv`, `sub_serv_str`, `price`, `2ndprice`, `3rdprice`, `active`, `total`) VALUES (92, '2.1.9', 'Отправка за счет средств получателя социальных услуг почтовой корреспонденции', 2019, 65, '2.1', 103.99, 103.99, 0, 1, 0);
INSERT INTO `kcson`.`serv` (`id`, `serv_tnum`, `serv_name`, `year`, `sub_serv`, `sub_serv_str`, `price`, `2ndprice`, `3rdprice`, `active`, `total`) VALUES (93, '2.1.10', 'Обеспечение кратковременного присмотра за детьми', 2019, 65, '2.1', 613.51, 613.51, 0, 1, 0);
INSERT INTO `kcson`.`serv` (`id`, `serv_tnum`, `serv_name`, `year`, `sub_serv`, `sub_serv_str`, `price`, `2ndprice`, `3rdprice`, `active`, `total`) VALUES (94, '2.1.11', 'Консультирование по вопросам оборудования специальными средствами и приспособлениями жилого помещения, занимаемого получателем социальных услуг (для инвалидов (детей-инвалидов), имеющих стойкие расстройства опорно-двигательного аппарата, зрения, слуха, умственные отклонения)', 2019, 65, '2.1', 306.75, 306.75, 0, 1, 0);
INSERT INTO `kcson`.`serv` (`id`, `serv_tnum`, `serv_name`, `year`, `sub_serv`, `sub_serv_str`, `price`, `2ndprice`, `3rdprice`, `active`, `total`) VALUES (95, '2.1.12', 'Содействие в оформлении документов и выдача напрокат технических средств реабилитации', 2019, 65, '2.1', 371.87, 371.87, 0, 1, 0);
INSERT INTO `kcson`.`serv` (`id`, `serv_tnum`, `serv_name`, `year`, `sub_serv`, `sub_serv_str`, `price`, `2ndprice`, `3rdprice`, `active`, `total`) VALUES (96, '2.1.13', 'Содействие в обеспечении техническими средствами реабилитации, предоставляемыми в соответствии с действующим законодательством либо за счет средств получателя социальных услуг', 2019, 65, '2.1', 428.8, 428.8, 0, 1, 0);
INSERT INTO `kcson`.`serv` (`id`, `serv_tnum`, `serv_name`, `year`, `sub_serv`, `sub_serv_str`, `price`, `2ndprice`, `3rdprice`, `active`, `total`) VALUES (97, '2.1.14', 'Консультирование по вопросам самообслуживания и социально-бытовой адаптации', 2019, 65, '2.1', 125.23, 125.23, 0, 1, 0);
INSERT INTO `kcson`.`serv` (`id`, `serv_tnum`, `serv_name`, `year`, `sub_serv`, `sub_serv_str`, `price`, `2ndprice`, `3rdprice`, `active`, `total`) VALUES (98, '2.2', 'Социально-медицинские услуги:', 2019, 64, '2',0 ,0 , 0, 1, 1);
INSERT INTO `kcson`.`serv` (`id`, `serv_tnum`, `serv_name`, `year`, `sub_serv`, `sub_serv_str`, `price`, `2ndprice`, `3rdprice`, `active`, `total`) VALUES (99, '2.2.1', 'Консультирование по социально-медицинским вопросам', 2019, 98, '2.2', 169.64, 169.64, 0, 1, 0);
INSERT INTO `kcson`.`serv` (`id`, `serv_tnum`, `serv_name`, `year`, `sub_serv`, `sub_serv_str`, `price`, `2ndprice`, `3rdprice`, `active`, `total`) VALUES (100, '2.2.2', 'Систематическое наблюдение за получателем социальных услуг в целях выявления отклонений в состоянии его здоровья', 2019, 98, '2.2', 88.43, 88.43, 0, 1, 0);
INSERT INTO `kcson`.`serv` (`id`, `serv_tnum`, `serv_name`, `year`, `sub_serv`, `sub_serv_str`, `price`, `2ndprice`, `3rdprice`, `active`, `total`) VALUES (101, '2.2.3', 'Выполнение процедур, связанных с организацией ухода, наблюдением за состоянием здоровья получателя социальных услуг', 2019, 98, '2.2', 189.28, 189.28, 0, 1, 0);
INSERT INTO `kcson`.`serv` (`id`, `serv_tnum`, `serv_name`, `year`, `sub_serv`, `sub_serv_str`, `price`, `2ndprice`, `3rdprice`, `active`, `total`) VALUES (102, '2.2.4', 'Обеспечение приема получателем социальных услуг лекарственных средств в соответствии с назначением врача', 2019, 98, '2.2', 83.27, 83.27, 0, 1, 0);
INSERT INTO `kcson`.`serv` (`id`, `serv_tnum`, `serv_name`, `year`, `sub_serv`, `sub_serv_str`, `price`, `2ndprice`, `3rdprice`, `active`, `total`) VALUES (103, '2.2.5', 'Проведение мероприятий, направленных на формирование здорового образа жизни', 2019, 98, '2.2', 187.83, 187.83, 0, 1, 0);
INSERT INTO `kcson`.`serv` (`id`, `serv_tnum`, `serv_name`, `year`, `sub_serv`, `sub_serv_str`, `price`, `2ndprice`, `3rdprice`, `active`, `total`) VALUES (104, '2.2.6', 'Проведение лечебно-оздоровительных мероприятий (в том числе с использованием реабилитационного оборудования)', 2019, 98, '2.2', 292.48, 292.48, 0, 1, 0);
INSERT INTO `kcson`.`serv` (`id`, `serv_tnum`, `serv_name`, `year`, `sub_serv`, `sub_serv_str`, `price`, `2ndprice`, `3rdprice`, `active`, `total`) VALUES (105, '2.2.7', 'Проведение занятий по адаптивной физической культуре', 2019, 98, '2.2', 496.99, 496.99, 0, 1, 0);
INSERT INTO `kcson`.`serv` (`id`, `serv_tnum`, `serv_name`, `year`, `sub_serv`, `sub_serv_str`, `price`, `2ndprice`, `3rdprice`, `active`, `total`) VALUES (106, '2.2.8', 'Санитарная обработка (обработка волосистых поверхностей тела дезинфицирующими растворами от педикулеза, помывка)', 2019, 98, '2.2', 293.07, 293.07, 0, 1, 0);
INSERT INTO `kcson`.`serv` (`id`, `serv_tnum`, `serv_name`, `year`, `sub_serv`, `sub_serv_str`, `price`, `2ndprice`, `3rdprice`, `active`, `total`) VALUES (107, '2.3', 'Социально-психологические услуги:', 2019, 64, '2',0 ,0 , 0, 1, 1);
INSERT INTO `kcson`.`serv` (`id`, `serv_tnum`, `serv_name`, `year`, `sub_serv`, `sub_serv_str`, `price`, `2ndprice`, `3rdprice`, `active`, `total`) VALUES (108, '2.3.1', 'Социально-психологическое консультирование (в том числе семейное консультирование)', 2019, 107, '2.3',0 , 303.22, 0, 1, 0);
INSERT INTO `kcson`.`serv` (`id`, `serv_tnum`, `serv_name`, `year`, `sub_serv`, `sub_serv_str`, `price`, `2ndprice`, `3rdprice`, `active`, `total`) VALUES (109, '2.3.2', 'Социально-психологический патронаж', 2019, 107, '2.3',0 , 418.67, 0, 1, 0);
INSERT INTO `kcson`.`serv` (`id`, `serv_tnum`, `serv_name`, `year`, `sub_serv`, `sub_serv_str`, `price`, `2ndprice`, `3rdprice`, `active`, `total`) VALUES (110, '2.3.3', 'Проведение социально-психологических тренингов', 2019, 107, '2.3',0 , 72.19, 0, 1, 0);
INSERT INTO `kcson`.`serv` (`id`, `serv_tnum`, `serv_name`, `year`, `sub_serv`, `sub_serv_str`, `price`, `2ndprice`, `3rdprice`, `active`, `total`) VALUES (111, '2.4', 'Социально-педагогические услуги:', 2019, 64, '2',0 ,0 , 0, 1, 1);
INSERT INTO `kcson`.`serv` (`id`, `serv_tnum`, `serv_name`, `year`, `sub_serv`, `sub_serv_str`, `price`, `2ndprice`, `3rdprice`, `active`, `total`) VALUES (112, '2.4.1', 'Консультирование получателя социальных услуг и (или) ближайшего окружения получателя социальных услуг по вопросам социальной реабилитации', 2019, 111, '2.4',0 , 214.49, 0, 1, 0);
INSERT INTO `kcson`.`serv` (`id`, `serv_tnum`, `serv_name`, `year`, `sub_serv`, `sub_serv_str`, `price`, `2ndprice`, `3rdprice`, `active`, `total`) VALUES (113, '2.4.2', 'Социально-педагогическая коррекция, включая диагностику и консультирование', 2019, 111, '2.4',0 , 1693.08, 0, 1, 0);
INSERT INTO `kcson`.`serv` (`id`, `serv_tnum`, `serv_name`, `year`, `sub_serv`, `sub_serv_str`, `price`, `2ndprice`, `3rdprice`, `active`, `total`) VALUES (114, '2.4.3', 'Социально-педагогический патронаж', 2019, 111, '2.4',0 , 411.98, 0, 1, 0);
INSERT INTO `kcson`.`serv` (`id`, `serv_tnum`, `serv_name`, `year`, `sub_serv`, `sub_serv_str`, `price`, `2ndprice`, `3rdprice`, `active`, `total`) VALUES (115, '2.4.4', 'Обучение родительским функциям', 2019, 111, '2.4',0 , 598.31, 0, 1, 0);
INSERT INTO `kcson`.`serv` (`id`, `serv_tnum`, `serv_name`, `year`, `sub_serv`, `sub_serv_str`, `price`, `2ndprice`, `3rdprice`, `active`, `total`) VALUES (116, '2.4.5', 'Обучение матери созданию социально-бытовой среды для развития ребенка', 2019, 111, '2.4',0 , 191.01, 0, 1, 0);
INSERT INTO `kcson`.`serv` (`id`, `serv_tnum`, `serv_name`, `year`, `sub_serv`, `sub_serv_str`, `price`, `2ndprice`, `3rdprice`, `active`, `total`) VALUES (117, '2.4.6', 'Консультирование ближайшего окружения ребенка по развитию игровой и продуктивной деятельности', 2019, 111, '2.4',0 , 207.12, 0, 1, 0);
INSERT INTO `kcson`.`serv` (`id`, `serv_tnum`, `serv_name`, `year`, `sub_serv`, `sub_serv_str`, `price`, `2ndprice`, `3rdprice`, `active`, `total`) VALUES (118, '2.4.7', 'Консультирование по организации учебной деятельности несовершеннолетнего в домашних условиях', 2019, 111, '2.4',0 , 207.12, 0, 1, 0);
INSERT INTO `kcson`.`serv` (`id`, `serv_tnum`, `serv_name`, `year`, `sub_serv`, `sub_serv_str`, `price`, `2ndprice`, `3rdprice`, `active`, `total`) VALUES (119, '2.4.8', 'Обучение практическим навыкам общего ухода за тяжелобольными получателями социальных услуг, получателями социальных услуг, имеющими ограничения жизнедеятельности, в том числе за детьми-инвалидами', 2019, 111, '2.4',0 , 176.21, 0, 1, 0);
INSERT INTO `kcson`.`serv` (`id`, `serv_tnum`, `serv_name`, `year`, `sub_serv`, `sub_serv_str`, `price`, `2ndprice`, `3rdprice`, `active`, `total`) VALUES (120, '2.4.9', 'Проведение логопедических занятий', 2019, 111, '2.4',0 , 686.15, 0, 1, 0);
INSERT INTO `kcson`.`serv` (`id`, `serv_tnum`, `serv_name`, `year`, `sub_serv`, `sub_serv_str`, `price`, `2ndprice`, `3rdprice`, `active`, `total`) VALUES (121, '2.4.10', 'Организация помощи родителям и иным законным представителям детей-инвалидов, воспитываемых дома, в обучении таких детей навыкам самообслуживания, общения, направленным на развитие личности', 2019, 111, '2.4',0 , 4823.05, 0, 1, 0);
INSERT INTO `kcson`.`serv` (`id`, `serv_tnum`, `serv_name`, `year`, `sub_serv`, `sub_serv_str`, `price`, `2ndprice`, `3rdprice`, `active`, `total`) VALUES (122, '2.4.11', 'Формирование позитивных интересов (в том числе в сфере досуга)', 2019, 111, '2.4',0 , 1138.4, 0, 1, 0);
INSERT INTO `kcson`.`serv` (`id`, `serv_tnum`, `serv_name`, `year`, `sub_serv`, `sub_serv_str`, `price`, `2ndprice`, `3rdprice`, `active`, `total`) VALUES (123, '2.4.12', 'Проведение занятий в соответствии с разработанным индивидуальным социально-педагогическим планом (сенсорное развитие, предметно-практическая деятельность, социально-бытовая ориентация, изодеятельность, арт-терапия, игровая деятельность, музыкальные занятия, спортивные, досуговые, экскурсионные мероприятия), в том числе групповых', 2019, 111, '2.4',0 , 66.66, 0, 1, 0);
INSERT INTO `kcson`.`serv` (`id`, `serv_tnum`, `serv_name`, `year`, `sub_serv`, `sub_serv_str`, `price`, `2ndprice`, `3rdprice`, `active`, `total`) VALUES (124, '2.4.13', 'Оказание помощи в обучении навыкам компьютерной грамотности', 2019, 111, '2.4',0 , 762.43, 0, 1, 0);
INSERT INTO `kcson`.`serv` (`id`, `serv_tnum`, `serv_name`, `year`, `sub_serv`, `sub_serv_str`, `price`, `2ndprice`, `3rdprice`, `active`, `total`) VALUES (125, '2.4.14', 'Организация досуга (в том числе сопровождение на социокультурные мероприятия)', 2019, 111, '2.4',0 , 43.84, 0, 1, 0);
INSERT INTO `kcson`.`serv` (`id`, `serv_tnum`, `serv_name`, `year`, `sub_serv`, `sub_serv_str`, `price`, `2ndprice`, `3rdprice`, `active`, `total`) VALUES (126, '2.5', 'Социально-трудовые услуги:', 2019, 64, '2',0 ,0 , 0, 1, 1);
INSERT INTO `kcson`.`serv` (`id`, `serv_tnum`, `serv_name`, `year`, `sub_serv`, `sub_serv_str`, `price`, `2ndprice`, `3rdprice`, `active`, `total`) VALUES (127, '2.5.1', 'Проведение мероприятий по использованию трудовых возможностей и обучению доступным профессиональным навыкам', 2019, 126, '2.5',0 , 703.61, 0, 1, 0);
INSERT INTO `kcson`.`serv` (`id`, `serv_tnum`, `serv_name`, `year`, `sub_serv`, `sub_serv_str`, `price`, `2ndprice`, `3rdprice`, `active`, `total`) VALUES (128, '2.5.2', 'Профессиональная ориентация', 2019, 126, '2.5',0 , 358.67, 0, 1, 0);
INSERT INTO `kcson`.`serv` (`id`, `serv_tnum`, `serv_name`, `year`, `sub_serv`, `sub_serv_str`, `price`, `2ndprice`, `3rdprice`, `active`, `total`) VALUES (129, '2.5.3', 'Организация обучения в трудовых мастерских', 2019, 126, '2.5',0 , 125.31, 0, 1, 0);
INSERT INTO `kcson`.`serv` (`id`, `serv_tnum`, `serv_name`, `year`, `sub_serv`, `sub_serv_str`, `price`, `2ndprice`, `3rdprice`, `active`, `total`) VALUES (130, '2.5.4', 'Организация помощи в получении образования, в том числе профессионального образования, инвалидами (детьми- инвалидами) в соответствии с их способностями', 2019, 126, '2.5',0 , 1291.2, 0, 1, 0);
INSERT INTO `kcson`.`serv` (`id`, `serv_tnum`, `serv_name`, `year`, `sub_serv`, `sub_serv_str`, `price`, `2ndprice`, `3rdprice`, `active`, `total`) VALUES (131, '2.5.5', 'Содействие в получении образования и(или) профессии', 2019, 126, '2.5',0 , 212.6, 0, 1, 0);
INSERT INTO `kcson`.`serv` (`id`, `serv_tnum`, `serv_name`, `year`, `sub_serv`, `sub_serv_str`, `price`, `2ndprice`, `3rdprice`, `active`, `total`) VALUES (132, '2.5.6', 'Оказание помощи в трудоустройстве', 2019, 126, '2.5',0 , 213.55, 0, 1, 0);
INSERT INTO `kcson`.`serv` (`id`, `serv_tnum`, `serv_name`, `year`, `sub_serv`, `sub_serv_str`, `price`, `2ndprice`, `3rdprice`, `active`, `total`) VALUES (133, '2.5.7', 'Содействие родственникам получателя социальных услуг в нахождении работы по гибкому графику', 2019, 126, '2.5',0 , 212.6, 0, 1, 0);
INSERT INTO `kcson`.`serv` (`id`, `serv_tnum`, `serv_name`, `year`, `sub_serv`, `sub_serv_str`, `price`, `2ndprice`, `3rdprice`, `active`, `total`) VALUES (134, '2.6', 'Социально-правовые услуги:', 2019, 64, '2',0 ,0 , 0, 1, 1);
INSERT INTO `kcson`.`serv` (`id`, `serv_tnum`, `serv_name`, `year`, `sub_serv`, `sub_serv_str`, `price`, `2ndprice`, `3rdprice`, `active`, `total`) VALUES (135, '2.6.1', 'Оказание помощи в оформлении документов и восстановлении утраченных документов получателя социальных услуг', 2019, 134, '2.6',0 , 149.17, 0, 1, 0);
INSERT INTO `kcson`.`serv` (`id`, `serv_tnum`, `serv_name`, `year`, `sub_serv`, `sub_serv_str`, `price`, `2ndprice`, `3rdprice`, `active`, `total`) VALUES (136, '2.6.2', 'Содействие в получении полиса обязательного медицинского страхования', 2019, 134, '2.6',0 , 461.26, 0, 1, 0);
INSERT INTO `kcson`.`serv` (`id`, `serv_tnum`, `serv_name`, `year`, `sub_serv`, `sub_serv_str`, `price`, `2ndprice`, `3rdprice`, `active`, `total`) VALUES (137, '2.6.3', 'Консультирование по вопросам усыновления (удочерения)', 2019, 134, '2.6',0 , 275.56, 0, 1, 0);
INSERT INTO `kcson`.`serv` (`id`, `serv_tnum`, `serv_name`, `year`, `sub_serv`, `sub_serv_str`, `price`, `2ndprice`, `3rdprice`, `active`, `total`) VALUES (138, '2.6.4', 'Оформление исковых заявлений на лишение родительских прав либо восстановление в родительских правах', 2019, 134, '2.6',0 , 275.56, 0, 1, 0);
INSERT INTO `kcson`.`serv` (`id`, `serv_tnum`, `serv_name`, `year`, `sub_serv`, `sub_serv_str`, `price`, `2ndprice`, `3rdprice`, `active`, `total`) VALUES (139, '2.6.5', 'Содействие в привлечении к уголовной ответственности подозреваемых в психическом и физическом насилии над получателем социальных услуг', 2019, 134, '2.6',0 , 289.12, 0, 1, 0);
INSERT INTO `kcson`.`serv` (`id`, `serv_tnum`, `serv_name`, `year`, `sub_serv`, `sub_serv_str`, `price`, `2ndprice`, `3rdprice`, `active`, `total`) VALUES (140, '2.6.6', 'Содействие в оформлении документов, необходимых для помещения в стационарную организацию социального обслуживания', 2019, 134, '2.6',0 , 319.04, 0, 1, 0);
INSERT INTO `kcson`.`serv` (`id`, `serv_tnum`, `serv_name`, `year`, `sub_serv`, `sub_serv_str`, `price`, `2ndprice`, `3rdprice`, `active`, `total`) VALUES (141, '2.6.7', 'Содействие в восстановлении утраченного (сохранении занимаемого) жилья, наследства', 2019, 134, '2.6',0 , 435.25, 0, 1, 0);
INSERT INTO `kcson`.`serv` (`id`, `serv_tnum`, `serv_name`, `year`, `sub_serv`, `sub_serv_str`, `price`, `2ndprice`, `3rdprice`, `active`, `total`) VALUES (142, '2.6.8', 'Оказание помощи в получении юридических услуг (в том числе бесплатно)', 2019, 134, '2.6',0 , 289.59, 0, 1, 0);
INSERT INTO `kcson`.`serv` (`id`, `serv_tnum`, `serv_name`, `year`, `sub_serv`, `sub_serv_str`, `price`, `2ndprice`, `3rdprice`, `active`, `total`) VALUES (143, '2.6.9', 'Оказание помощи в защите прав и законных интересов получателя социальных услуг', 2019, 134, '2.6',0 , 197.23, 0, 1, 0);
INSERT INTO `kcson`.`serv` (`id`, `serv_tnum`, `serv_name`, `year`, `sub_serv`, `sub_serv_str`, `price`, `2ndprice`, `3rdprice`, `active`, `total`) VALUES (144, '2.7', 'Услуги в целях повышения коммуникативного потенциала получателей социальных услуг, имеющих ограничения жизнедеятельности, в том числе детей-инвалидов:', 2019, 64, '2',0 ,0 , 0, 1, 1);
INSERT INTO `kcson`.`serv` (`id`, `serv_tnum`, `serv_name`, `year`, `sub_serv`, `sub_serv_str`, `price`, `2ndprice`, `3rdprice`, `active`, `total`) VALUES (145, '2.7.1', 'Консультирование по вопросам социально-средовой реабилитации', 2019, 144, '2.7',0 , 376.81, 0, 1, 0);
INSERT INTO `kcson`.`serv` (`id`, `serv_tnum`, `serv_name`, `year`, `sub_serv`, `sub_serv_str`, `price`, `2ndprice`, `3rdprice`, `active`, `total`) VALUES (146, '2.7.2', 'Обучение навыкам социально-средовой ориентации (в том числе самостоятельному передвижению, включая изучение жизненно важных маршрутов передвижения)', 2019, 144, '2.7',0 , 230.06, 0, 1, 0);
INSERT INTO `kcson`.`serv` (`id`, `serv_tnum`, `serv_name`, `year`, `sub_serv`, `sub_serv_str`, `price`, `2ndprice`, `3rdprice`, `active`, `total`) VALUES (147, '2.7.3', 'Обучение инвалидов (детей-инвалидов) пользованию средствами ухода и техническими средствами реабилитации', 2019, 144, '2.7',0 , 317.9, 0, 1, 0);
INSERT INTO `kcson`.`serv` (`id`, `serv_tnum`, `serv_name`, `year`, `sub_serv`, `sub_serv_str`, `price`, `2ndprice`, `3rdprice`, `active`, `total`) VALUES (148, '2.7.4', 'Обучение навыкам (поддержание навыков) поведения в быту и общественных местах', 2019, 144, '2.7',0 , 282.58, 0, 1, 0);
INSERT INTO `kcson`.`serv` (`id`, `serv_tnum`, `serv_name`, `year`, `sub_serv`, `sub_serv_str`, `price`, `2ndprice`, `3rdprice`, `active`, `total`) VALUES (149, '2.7.5', 'Организация коммуникативного пространства и коммуникативных ситуаций по месту проживания (получения социальных услуг)', 2019, 144, '2.7',0 , 312.09, 0, 1, 0);
INSERT INTO `kcson`.`serv` (`id`, `serv_tnum`, `serv_name`, `year`, `sub_serv`, `sub_serv_str`, `price`, `2ndprice`, `3rdprice`, `active`, `total`) VALUES (150, '3', 'В стационарной форме социального обслуживания', 2019, 1, 'Итог',0 ,0 , 0, 1, 1);
INSERT INTO `kcson`.`serv` (`id`, `serv_tnum`, `serv_name`, `year`, `sub_serv`, `sub_serv_str`, `price`, `2ndprice`, `3rdprice`, `active`, `total`) VALUES (151, '3.1', 'Социально-бытовые услуги:', 2019, 150, '3',0 ,0 , 0, 1, 1);
INSERT INTO `kcson`.`serv` (`id`, `serv_tnum`, `serv_name`, `year`, `sub_serv`, `sub_serv_str`, `price`, `2ndprice`, `3rdprice`, `active`, `total`) VALUES (152, '3.1.1', 'Обеспечение площадью жилых помещений в соответствии с утвержденными нормативами', 2019, 151, '3.1', 262.64, 262.64, 0, 1, 0);
INSERT INTO `kcson`.`serv` (`id`, `serv_tnum`, `serv_name`, `year`, `sub_serv`, `sub_serv_str`, `price`, `2ndprice`, `3rdprice`, `active`, `total`) VALUES (153, '3.1.2', 'Обеспечение мягким инвентарем (одеждой, обувью, нательным бельем и постельными принадлежностями) в соответствии с утвержденными нормативами*:', 2019, 151, '3.1',0 ,0 , 0, 1, 1);
INSERT INTO `kcson`.`serv` (`id`, `serv_tnum`, `serv_name`, `year`, `sub_serv`, `sub_serv_str`, `price`, `2ndprice`, `3rdprice`, `active`, `total`) VALUES (154, '3.1.2.1', 'гражданам пожилого возраста, гражданам трудоспособного возраста и инвалидов трудоспособного возраста', 2019, 153, '3.1.2', 133.26, 133.26, 0, 1, 0);
INSERT INTO `kcson`.`serv` (`id`, `serv_tnum`, `serv_name`, `year`, `sub_serv`, `sub_serv_str`, `price`, `2ndprice`, `3rdprice`, `active`, `total`) VALUES (155, '3.1.2.2', 'гражданам пожилого возраста и инвалидам трудоспособного возраста, проживающим в отделениях милосердия', 2019, 153, '3.1.2', 133.26, 133.26, 0, 1, 0);
INSERT INTO `kcson`.`serv` (`id`, `serv_tnum`, `serv_name`, `year`, `sub_serv`, `sub_serv_str`, `price`, `2ndprice`, `3rdprice`, `active`, `total`) VALUES (156, '3.1.2.3', 'детям-инвалидам, детям-сиротам и детям, оставшимся без попечения родителей, несовершеннолетним, находящимся в сложной жизненной ситуации школьного возраста', 2019, 153, '3.1.2', 113.49, 113.49, 0, 1, 0);
INSERT INTO `kcson`.`serv` (`id`, `serv_tnum`, `serv_name`, `year`, `sub_serv`, `sub_serv_str`, `price`, `2ndprice`, `3rdprice`, `active`, `total`) VALUES (157, '3.1.2.4', 'детям-инвалидам, детям-сиротам и детям, оставшимся без попечения родителей, несовершеннолетним, находящимся в сложной жизненной ситуации дошкольного возраста', 2019, 153, '3.1.2', 113.49, 113.49, 0, 1, 0);
INSERT INTO `kcson`.`serv` (`id`, `serv_tnum`, `serv_name`, `year`, `sub_serv`, `sub_serv_str`, `price`, `2ndprice`, `3rdprice`, `active`, `total`) VALUES (158, '3.1.2.5', 'детям-инвалидам, детям-сиротам и детям, оставшимся без попечения родителей, несовершеннолетним, находящимся в сложной жизненной ситуации, проживающим в отделениях милосердия школьного возраста', 2019, 153, '3.1.2', 113.49, 113.49, 0, 1, 0);
INSERT INTO `kcson`.`serv` (`id`, `serv_tnum`, `serv_name`, `year`, `sub_serv`, `sub_serv_str`, `price`, `2ndprice`, `3rdprice`, `active`, `total`) VALUES (159, '3.1.2.6', 'детям-инвалидам, детям-сиротам и детям, оставшимся без попечения родителей, несовершеннолетним, находящимся в сложной жизненной ситуации, проживающим в отделениях милосердия дошкольного возраста', 2019, 153, '3.1.2', 113.49, 113.49, 0, 1, 0);
INSERT INTO `kcson`.`serv` (`id`, `serv_tnum`, `serv_name`, `year`, `sub_serv`, `sub_serv_str`, `price`, `2ndprice`, `3rdprice`, `active`, `total`) VALUES (160, '3.1.2.7', 'женщинам, находящимся в трудной жизненной ситуации или социально опасном положении, в том числе несовершеннолетним беременным', 2019, 153, '3.1.2', 95.84, 95.84, 0, 1, 0);
INSERT INTO `kcson`.`serv` (`id`, `serv_tnum`, `serv_name`, `year`, `sub_serv`, `sub_serv_str`, `price`, `2ndprice`, `3rdprice`, `active`, `total`) VALUES (161, '3.1.2.8', 'женщинам с детьми в возрасте до трех лет, находящимся в трудной жизненной ситуации или социально опасном положении, в том числе несовершеннолетним матерям с младенцами', 2019, 153, '3.1.2', 95.84, 95.84, 0, 1, 0);
INSERT INTO `kcson`.`serv` (`id`, `serv_tnum`, `serv_name`, `year`, `sub_serv`, `sub_serv_str`, `price`, `2ndprice`, `3rdprice`, `active`, `total`) VALUES (162, '3.1.2.9', 'женщинам с детьми старше трех лет, находящимся в трудной жизненной ситуации или социально опасном положении', 2019, 153, '3.1.2', 95.84, 95.84, 0, 1, 0);
INSERT INTO `kcson`.`serv` (`id`, `serv_tnum`, `serv_name`, `year`, `sub_serv`, `sub_serv_str`, `price`, `2ndprice`, `3rdprice`, `active`, `total`) VALUES (163, '3.1.3', 'Обеспечение питанием согласно утвержденным нормативам:', 2019, 151, '3.1',0 ,0 , 0, 1, 1);
INSERT INTO `kcson`.`serv` (`id`, `serv_tnum`, `serv_name`, `year`, `sub_serv`, `sub_serv_str`, `price`, `2ndprice`, `3rdprice`, `active`, `total`) VALUES (164, '3.1.3.1', 'граждан пожилого возраста и инвалидов, находящихся в учреждениях социального обслуживания населения, за исключением психоневрологических интернатов', 2019, 163, '3.1.3', 395.5, 395.5, 0, 1, 0);
INSERT INTO `kcson`.`serv` (`id`, `serv_tnum`, `serv_name`, `year`, `sub_serv`, `sub_serv_str`, `price`, `2ndprice`, `3rdprice`, `active`, `total`) VALUES (165, '3.1.3.2', 'граждан пожилого возраста и инвалидов при заболеваниях сахарным диабетом, находящихся в учреждениях социального обслуживания населения, за исключением психоневрологических интернатов', 2019, 163, '3.1.3', 380.46, 380.46, 0, 1, 0);
INSERT INTO `kcson`.`serv` (`id`, `serv_tnum`, `serv_name`, `year`, `sub_serv`, `sub_serv_str`, `price`, `2ndprice`, `3rdprice`, `active`, `total`) VALUES (166, '3.1.3.3', 'граждан пожилого возраста и инвалидов, находящихся в учреждениях социального обслуживания населения - психоневрологических интернатах', 2019, 163, '3.1.3', 424.89, 424.89, 0, 1, 0);
INSERT INTO `kcson`.`serv` (`id`, `serv_tnum`, `serv_name`, `year`, `sub_serv`, `sub_serv_str`, `price`, `2ndprice`, `3rdprice`, `active`, `total`) VALUES (167, '3.1.3.4', 'граждан пожилого возраста и инвалидов при заболеваниях сахарным диабетом, находящихся в учреждениях социального обслуживания населения - психоневрологических интернатах', 2019, 163, '3.1.3', 380.46, 380.46, 0, 1, 0);
INSERT INTO `kcson`.`serv` (`id`, `serv_tnum`, `serv_name`, `year`, `sub_serv`, `sub_serv_str`, `price`, `2ndprice`, `3rdprice`, `active`, `total`) VALUES (168, '3.1.3.5', 'беременных женщин в учреждениях социального обслуживания населения', 2019, 163, '3.1.3', 396.81, 396.81, 0, 1, 0);
INSERT INTO `kcson`.`serv` (`id`, `serv_tnum`, `serv_name`, `year`, `sub_serv`, `sub_serv_str`, `price`, `2ndprice`, `3rdprice`, `active`, `total`) VALUES (169, '3.1.3.6', 'кормящих матерей в учреждениях социального обслуживания населения', 2019, 163, '3.1.3', 369.43, 369.43, 0, 1, 0);
INSERT INTO `kcson`.`serv` (`id`, `serv_tnum`, `serv_name`, `year`, `sub_serv`, `sub_serv_str`, `price`, `2ndprice`, `3rdprice`, `active`, `total`) VALUES (170, '3.1.3.7', 'детей первого года жизни от 0-4 мес., проживающих с матерями - получателями социальных услуг', 2019, 163, '3.1.3', 158.61, 158.61, 0, 1, 0);
INSERT INTO `kcson`.`serv` (`id`, `serv_tnum`, `serv_name`, `year`, `sub_serv`, `sub_serv_str`, `price`, `2ndprice`, `3rdprice`, `active`, `total`) VALUES (171, '3.1.3.8', 'детей первого года жизни от 4-6 мес., проживающих с матерями - получателями социальных услуг', 2019, 163, '3.1.3', 224.59, 224.59, 0, 1, 0);
INSERT INTO `kcson`.`serv` (`id`, `serv_tnum`, `serv_name`, `year`, `sub_serv`, `sub_serv_str`, `price`, `2ndprice`, `3rdprice`, `active`, `total`) VALUES (172, '3.1.3.9', 'детей первого года жизни от 6-9 мес., проживающих с матерями - получателями социальных услуг', 2019, 163, '3.1.3', 238.31, 238.31, 0, 1, 0);
INSERT INTO `kcson`.`serv` (`id`, `serv_tnum`, `serv_name`, `year`, `sub_serv`, `sub_serv_str`, `price`, `2ndprice`, `3rdprice`, `active`, `total`) VALUES (173, '3.1.3.10', 'детей первого года жизни от 9-12 мес., проживающих с матерями - получателями социальных услуг', 2019, 163, '3.1.3', 383.15, 383.15, 0, 1, 0);
INSERT INTO `kcson`.`serv` (`id`, `serv_tnum`, `serv_name`, `year`, `sub_serv`, `sub_serv_str`, `price`, `2ndprice`, `3rdprice`, `active`, `total`) VALUES (174, '3.1.3.11', 'детей в возрасте от 1 до 3 лет', 2019, 163, '3.1.3', 209.07, 209.07, 0, 1, 0);
INSERT INTO `kcson`.`serv` (`id`, `serv_tnum`, `serv_name`, `year`, `sub_serv`, `sub_serv_str`, `price`, `2ndprice`, `3rdprice`, `active`, `total`) VALUES (175, '3.1.3.12', 'детей в возрасте от 3 до 7 лет', 2019, 163, '3.1.3', 360, 360, 0, 1, 0);
INSERT INTO `kcson`.`serv` (`id`, `serv_tnum`, `serv_name`, `year`, `sub_serv`, `sub_serv_str`, `price`, `2ndprice`, `3rdprice`, `active`, `total`) VALUES (176, '3.1.3.13', 'детей в возрасте от 7 до 11лет', 2019, 163, '3.1.3', 423.57, 423.57, 0, 1, 0);
INSERT INTO `kcson`.`serv` (`id`, `serv_tnum`, `serv_name`, `year`, `sub_serv`, `sub_serv_str`, `price`, `2ndprice`, `3rdprice`, `active`, `total`) VALUES (177, '3.1.3.14', 'детей в возрасте от 12 до 18 лет', 2019, 163, '3.1.3', 475.75, 475.75, 0, 1, 0);
INSERT INTO `kcson`.`serv` (`id`, `serv_tnum`, `serv_name`, `year`, `sub_serv`, `sub_serv_str`, `price`, `2ndprice`, `3rdprice`, `active`, `total`) VALUES (178, '3.1.3.15', 'детей в возрасте от 4 до 18 лет специализированным лечебным сбалансированным энтеральным питанием в организациях социального обслуживания населения:', 2019, 163, '3.1.3',0 ,0 , 0, 1, 1);
INSERT INTO `kcson`.`serv` (`id`, `serv_tnum`, `serv_name`, `year`, `sub_serv`, `sub_serv_str`, `price`, `2ndprice`, `3rdprice`, `active`, `total`) VALUES (179, '3.1.3.15.1', 'находящихся на длительном зондовом питании***', 2019, 178, '3.1.3.15', 19.46, 19.46, 0, 1, 0);
INSERT INTO `kcson`.`serv` (`id`, `serv_tnum`, `serv_name`, `year`, `sub_serv`, `sub_serv_str`, `price`, `2ndprice`, `3rdprice`, `active`, `total`) VALUES (180, '3.1.3.15.2', 'по медицинским показаниям нуждающихся в сухой адаптированной молочной смеси специального назначения (антирефлюкс)', 2019, 178, '3.1.3.15', 287.67, 287.67, 0, 1, 0);
INSERT INTO `kcson`.`serv` (`id`, `serv_tnum`, `serv_name`, `year`, `sub_serv`, `sub_serv_str`, `price`, `2ndprice`, `3rdprice`, `active`, `total`) VALUES (181, '3.1.3.17', 'граждан трудоспособного возраста', 2019, 163, '3.1.3', 7266.55, 7266.55, 0, 1, 0);
INSERT INTO `kcson`.`serv` (`id`, `serv_tnum`, `serv_name`, `year`, `sub_serv`, `sub_serv_str`, `price`, `2ndprice`, `3rdprice`, `active`, `total`) VALUES (182, '3.1.4', 'Помощь в приеме пищи (кормление)', 2019, 151, '3.1', 209.16, 209.16, 0, 1, 0);
INSERT INTO `kcson`.`serv` (`id`, `serv_tnum`, `serv_name`, `year`, `sub_serv`, `sub_serv_str`, `price`, `2ndprice`, `3rdprice`, `active`, `total`) VALUES (183, '3.1.5', 'Помощь в одевании и переодевании лицам, не способным по состоянию здоровья самостоятельно осуществлять за собой уход', 2019, 151, '3.1', 277.66, 277.66, 0, 1, 0);
INSERT INTO `kcson`.`serv` (`id`, `serv_tnum`, `serv_name`, `year`, `sub_serv`, `sub_serv_str`, `price`, `2ndprice`, `3rdprice`, `active`, `total`) VALUES (184, '3.1.6', 'Смена подгузников и абсорбирующего белья лицам, не способным по состоянию здоровья самостоятельно осуществлять за собой уход', 2019, 151, '3.1', 136.56, 136.56, 0, 1, 0);
INSERT INTO `kcson`.`serv` (`id`, `serv_tnum`, `serv_name`, `year`, `sub_serv`, `sub_serv_str`, `price`, `2ndprice`, `3rdprice`, `active`, `total`) VALUES (185, '3.1.7', 'Предоставление гигиенических услуг лицам, не способным по состоянию здоровья самостоятельно осуществлять за собой уход', 2019, 151, '3.1', 136.25, 136.25, 0, 1, 0);
INSERT INTO `kcson`.`serv` (`id`, `serv_tnum`, `serv_name`, `year`, `sub_serv`, `sub_serv_str`, `price`, `2ndprice`, `3rdprice`, `active`, `total`) VALUES (186, '3.1.8', 'Сопровождение в туалет или высаживание на судно лиц, не способных по состоянию здоровья самостоятельно осуществлять за собой уход', 2019, 151, '3.1', 75.74, 75.74, 0, 1, 0);
INSERT INTO `kcson`.`serv` (`id`, `serv_tnum`, `serv_name`, `year`, `sub_serv`, `sub_serv_str`, `price`, `2ndprice`, `3rdprice`, `active`, `total`) VALUES (187, '3.1.9', 'Мытье (помощь в мытье) лиц, не способных по состоянию здоровья самостоятельно осуществлять за собой уход', 2019, 151, '3.1', 155.44, 155.44, 0, 1, 0);
INSERT INTO `kcson`.`serv` (`id`, `serv_tnum`, `serv_name`, `year`, `sub_serv`, `sub_serv_str`, `price`, `2ndprice`, `3rdprice`, `active`, `total`) VALUES (188, '3.1.10', 'Бритье (помощь в бритье) бороды и усов лицам, не способным по состоянию здоровья самостоятельно осуществлять за собой уход', 2019, 151, '3.1', 71.4, 71.4, 0, 1, 0);
INSERT INTO `kcson`.`serv` (`id`, `serv_tnum`, `serv_name`, `year`, `sub_serv`, `sub_serv_str`, `price`, `2ndprice`, `3rdprice`, `active`, `total`) VALUES (189, '3.1.11', 'Стрижка волос', 2019, 151, '3.1', 155.01, 155.01, 0, 1, 0);
INSERT INTO `kcson`.`serv` (`id`, `serv_tnum`, `serv_name`, `year`, `sub_serv`, `sub_serv_str`, `price`, `2ndprice`, `3rdprice`, `active`, `total`) VALUES (190, '3.1.12', 'Сопровождение на прогулках', 2019, 151, '3.1', 820.33, 820.33, 0, 1, 0);
INSERT INTO `kcson`.`serv` (`id`, `serv_tnum`, `serv_name`, `year`, `sub_serv`, `sub_serv_str`, `price`, `2ndprice`, `3rdprice`, `active`, `total`) VALUES (191, '3.1.13', 'Обеспечение за счет средств получателя социальных услуг книгами, журналами, газетами, настольными играми', 2019, 151, '3.1', 239.46, 239.46, 0, 1, 0);
INSERT INTO `kcson`.`serv` (`id`, `serv_tnum`, `serv_name`, `year`, `sub_serv`, `sub_serv_str`, `price`, `2ndprice`, `3rdprice`, `active`, `total`) VALUES (192, '3.1.14', 'Отправка за счет средств получателя социальных услуг почтовой корреспонденции', 2019, 151, '3.1', 121.14, 121.14, 0, 1, 0);
INSERT INTO `kcson`.`serv` (`id`, `serv_tnum`, `serv_name`, `year`, `sub_serv`, `sub_serv_str`, `price`, `2ndprice`, `3rdprice`, `active`, `total`) VALUES (193, '3.1.15', 'Создание условий (оказание помощи) молодым матерям по уходу за детьми младенческого возраста', 2019, 151, '3.1', 239.9, 239.9, 0, 1, 0);
INSERT INTO `kcson`.`serv` (`id`, `serv_tnum`, `serv_name`, `year`, `sub_serv`, `sub_serv_str`, `price`, `2ndprice`, `3rdprice`, `active`, `total`) VALUES (194, '3.1.16', 'Содействие в получении лекарственных препаратов, изделий медицинского назначения, предоставляемых в соответствии с действующим законодательством', 2019, 151, '3.1', 716.39, 716.39, 0, 1, 0);
INSERT INTO `kcson`.`serv` (`id`, `serv_tnum`, `serv_name`, `year`, `sub_serv`, `sub_serv_str`, `price`, `2ndprice`, `3rdprice`, `active`, `total`) VALUES (195, '3.1.17', 'Содействие в организации санаторно-курортного лечения или оздоровительного отдыха, предоставляемого в соответствии с действующим законодательством', 2019, 151, '3.1', 638.51, 638.51, 0, 1, 0);
INSERT INTO `kcson`.`serv` (`id`, `serv_tnum`, `serv_name`, `year`, `sub_serv`, `sub_serv_str`, `price`, `2ndprice`, `3rdprice`, `active`, `total`) VALUES (196, '3.1.18', 'Помощь при подготовке вещей для выезда на отдых за пределы города', 2019, 151, '3.1', 207.21, 207.21, 0, 1, 0);
INSERT INTO `kcson`.`serv` (`id`, `serv_tnum`, `serv_name`, `year`, `sub_serv`, `sub_serv_str`, `price`, `2ndprice`, `3rdprice`, `active`, `total`) VALUES (197, '3.1.19', 'Сдача за счет средств получателя социальных услуг вещей в стирку, химчистку, ремонт, обратная их доставка', 2019, 151, '3.1', 144.39, 144.39, 0, 1, 0);
INSERT INTO `kcson`.`serv` (`id`, `serv_tnum`, `serv_name`, `year`, `sub_serv`, `sub_serv_str`, `price`, `2ndprice`, `3rdprice`, `active`, `total`) VALUES (198, '3.1.20', 'Содействие в обеспечении техническими средствами реабилитации, предоставляемыми в соответствии с действующим законодательством либо за счет средств получателя социальных услуг', 2019, 151, '3.1', 363.12, 363.12, 0, 1, 0);
INSERT INTO `kcson`.`serv` (`id`, `serv_tnum`, `serv_name`, `year`, `sub_serv`, `sub_serv_str`, `price`, `2ndprice`, `3rdprice`, `active`, `total`) VALUES (199, '3.1.21', 'Оповещение родственников', 2019, 151, '3.1', 173.39, 173.39, 0, 1, 0);
INSERT INTO `kcson`.`serv` (`id`, `serv_tnum`, `serv_name`, `year`, `sub_serv`, `sub_serv_str`, `price`, `2ndprice`, `3rdprice`, `active`, `total`) VALUES (200, '3.1.22', 'Организация (содействие в оказании) ритуальных услуг', 2019, 151, '3.1', 520.17, 520.17, 0, 1, 0);
INSERT INTO `kcson`.`serv` (`id`, `serv_tnum`, `serv_name`, `year`, `sub_serv`, `sub_serv_str`, `price`, `2ndprice`, `3rdprice`, `active`, `total`) VALUES (201, '3.1.23', 'Консультирование по вопросам самообслуживания и социально-бытовой адаптации', 2019, 151, '3.1', 173.39, 173.39, 0, 1, 0);
INSERT INTO `kcson`.`serv` (`id`, `serv_tnum`, `serv_name`, `year`, `sub_serv`, `sub_serv_str`, `price`, `2ndprice`, `3rdprice`, `active`, `total`) VALUES (202, '3.2', 'Социально-медицинские услуги:', 2019, 150, '3',0 ,0 , 0, 1, 1);
INSERT INTO `kcson`.`serv` (`id`, `serv_tnum`, `serv_name`, `year`, `sub_serv`, `sub_serv_str`, `price`, `2ndprice`, `3rdprice`, `active`, `total`) VALUES (203, '3.2.1', 'Консультирование по социально-медицинским вопросам', 2019, 202, '3.2', 175.94, 175.94, 0, 1, 0);
INSERT INTO `kcson`.`serv` (`id`, `serv_tnum`, `serv_name`, `year`, `sub_serv`, `sub_serv_str`, `price`, `2ndprice`, `3rdprice`, `active`, `total`) VALUES (204, '3.2.2', 'Систематическое наблюдение за получателем социальных услуг в целях выявления отклонений в состоянии его здоровья', 2019, 202, '3.2', 395.48, 395.48, 0, 1, 0);
INSERT INTO `kcson`.`serv` (`id`, `serv_tnum`, `serv_name`, `year`, `sub_serv`, `sub_serv_str`, `price`, `2ndprice`, `3rdprice`, `active`, `total`) VALUES (205, '3.2.3', 'Выполнение процедур, связанных с организацией ухода, наблюдением за состоянием здоровья получателя социальных услуг', 2019, 202, '3.2', 491.88, 491.88, 0, 1, 0);
INSERT INTO `kcson`.`serv` (`id`, `serv_tnum`, `serv_name`, `year`, `sub_serv`, `sub_serv_str`, `price`, `2ndprice`, `3rdprice`, `active`, `total`) VALUES (206, '3.2.4', 'Обеспечение приема получателем социальных услуг лекарственных средств в соответствии с назначением врача', 2019, 202, '3.2', 78.87, 78.87, 0, 1, 0);
INSERT INTO `kcson`.`serv` (`id`, `serv_tnum`, `serv_name`, `year`, `sub_serv`, `sub_serv_str`, `price`, `2ndprice`, `3rdprice`, `active`, `total`) VALUES (207, '3.2.5', 'Содействие в получении медицинской помощи в соответствии с действующим законодательством', 2019, 202, '3.2', 738.13, 738.13, 0, 1, 0);
INSERT INTO `kcson`.`serv` (`id`, `serv_tnum`, `serv_name`, `year`, `sub_serv`, `sub_serv_str`, `price`, `2ndprice`, `3rdprice`, `active`, `total`) VALUES (208, '3.2.6', 'Проведение мероприятий, направленных на формирование здорового образа жизни', 2019, 202, '3.2', 390.13, 390.13, 0, 1, 0);
INSERT INTO `kcson`.`serv` (`id`, `serv_tnum`, `serv_name`, `year`, `sub_serv`, `sub_serv_str`, `price`, `2ndprice`, `3rdprice`, `active`, `total`) VALUES (209, '3.2.7', 'Проведение лечебно-оздоровительных мероприятий (в том числе с использованием реабилитационного оборудования)', 2019, 202, '3.2', 341.91, 341.91, 0, 1, 0);
INSERT INTO `kcson`.`serv` (`id`, `serv_tnum`, `serv_name`, `year`, `sub_serv`, `sub_serv_str`, `price`, `2ndprice`, `3rdprice`, `active`, `total`) VALUES (210, '3.2.8', 'Проведение занятий по адаптивной физической культуре', 2019, 202, '3.2', 342.25, 342.25, 0, 1, 0);
INSERT INTO `kcson`.`serv` (`id`, `serv_tnum`, `serv_name`, `year`, `sub_serv`, `sub_serv_str`, `price`, `2ndprice`, `3rdprice`, `active`, `total`) VALUES (211, '3.2.9', 'Санитарная обработка (обработка волосистых поверхностей тела дезинфицирующими растворами от педикулеза, помывка)', 2019, 202, '3.2', 360.14, 360.14, 0, 1, 0);
INSERT INTO `kcson`.`serv` (`id`, `serv_tnum`, `serv_name`, `year`, `sub_serv`, `sub_serv_str`, `price`, `2ndprice`, `3rdprice`, `active`, `total`) VALUES (212, '3.3', 'Социально-психологические услуги:', 2019, 150, '3',0 ,0 , 0, 1, 1);
INSERT INTO `kcson`.`serv` (`id`, `serv_tnum`, `serv_name`, `year`, `sub_serv`, `sub_serv_str`, `price`, `2ndprice`, `3rdprice`, `active`, `total`) VALUES (213, '3.3.1', 'Социально-психологическое консультирование (в том числе семейное консультирование)', 2019, 212, '3.3',0 , 564.72, 0, 1, 0);
INSERT INTO `kcson`.`serv` (`id`, `serv_tnum`, `serv_name`, `year`, `sub_serv`, `sub_serv_str`, `price`, `2ndprice`, `3rdprice`, `active`, `total`) VALUES (214, '3.3.2', 'Социально-психологический патронаж', 2019, 212, '3.3',0 , 554.43, 0, 1, 0);
INSERT INTO `kcson`.`serv` (`id`, `serv_tnum`, `serv_name`, `year`, `sub_serv`, `sub_serv_str`, `price`, `2ndprice`, `3rdprice`, `active`, `total`) VALUES (215, '3.3.3', 'Проведение социально-психологических тренингов', 2019, 212, '3.3',0 , 65.28, 0, 1, 0);
INSERT INTO `kcson`.`serv` (`id`, `serv_tnum`, `serv_name`, `year`, `sub_serv`, `sub_serv_str`, `price`, `2ndprice`, `3rdprice`, `active`, `total`) VALUES (216, '3.4', 'Социально-педагогические услуги:', 2019, 150, '3',0 ,0 , 0, 1, 1);
INSERT INTO `kcson`.`serv` (`id`, `serv_tnum`, `serv_name`, `year`, `sub_serv`, `sub_serv_str`, `price`, `2ndprice`, `3rdprice`, `active`, `total`) VALUES (217, '3.4.1', 'Консультирование получателя социальных услуг и(или) ближайшего окружения получателя социальных услуг по вопросам социальной реабилитации', 2019, 216, '3.4',0 , 215.17, 0, 1, 0);
INSERT INTO `kcson`.`serv` (`id`, `serv_tnum`, `serv_name`, `year`, `sub_serv`, `sub_serv_str`, `price`, `2ndprice`, `3rdprice`, `active`, `total`) VALUES (218, '3.4.2', 'Социально-педагогическая коррекция, включая диагностику и консультирование', 2019, 216, '3.4',0 , 1125.8, 0, 1, 0);
INSERT INTO `kcson`.`serv` (`id`, `serv_tnum`, `serv_name`, `year`, `sub_serv`, `sub_serv_str`, `price`, `2ndprice`, `3rdprice`, `active`, `total`) VALUES (219, '3.4.3', 'Социально-педагогический патронаж', 2019, 216, '3.4',0 , 708.95, 0, 1, 0);
INSERT INTO `kcson`.`serv` (`id`, `serv_tnum`, `serv_name`, `year`, `sub_serv`, `sub_serv_str`, `price`, `2ndprice`, `3rdprice`, `active`, `total`) VALUES (220, '3.4.4', 'Обучение родительским функциям', 2019, 216, '3.4',0 , 598.31, 0, 1, 0);
INSERT INTO `kcson`.`serv` (`id`, `serv_tnum`, `serv_name`, `year`, `sub_serv`, `sub_serv_str`, `price`, `2ndprice`, `3rdprice`, `active`, `total`) VALUES (221, '3.4.5', 'Обучение матери созданию социально-бытовой среды для развития ребенка', 2019, 216, '3.4',0 , 285.71, 0, 1, 0);
INSERT INTO `kcson`.`serv` (`id`, `serv_tnum`, `serv_name`, `year`, `sub_serv`, `sub_serv_str`, `price`, `2ndprice`, `3rdprice`, `active`, `total`) VALUES (222, '3.4.6', 'Консультирование ближайшего окружения ребенка по развитию игровой и продуктивной деятельности', 2019, 216, '3.4',0 , 213.75, 0, 1, 0);
INSERT INTO `kcson`.`serv` (`id`, `serv_tnum`, `serv_name`, `year`, `sub_serv`, `sub_serv_str`, `price`, `2ndprice`, `3rdprice`, `active`, `total`) VALUES (223, '3.4.7', 'Консультирование по организации учебной деятельности несовершеннолетнего в домашних условиях', 2019, 216, '3.4',0 , 207.12, 0, 1, 0);
INSERT INTO `kcson`.`serv` (`id`, `serv_tnum`, `serv_name`, `year`, `sub_serv`, `sub_serv_str`, `price`, `2ndprice`, `3rdprice`, `active`, `total`) VALUES (224, '3.4.8', 'Занятия по подготовке к жизни в семье', 2019, 216, '3.4',0 , 186.94, 0, 1, 0);
INSERT INTO `kcson`.`serv` (`id`, `serv_tnum`, `serv_name`, `year`, `sub_serv`, `sub_serv_str`, `price`, `2ndprice`, `3rdprice`, `active`, `total`) VALUES (225, '3.4.9', 'Проведение логопедических занятий', 2019, 216, '3.4',0 , 670.11, 0, 1, 0);
INSERT INTO `kcson`.`serv` (`id`, `serv_tnum`, `serv_name`, `year`, `sub_serv`, `sub_serv_str`, `price`, `2ndprice`, `3rdprice`, `active`, `total`) VALUES (226, '3.4.10', 'Формирование позитивных интересов (в том числе в сфере досуга)', 2019, 216, '3.4',0 , 1059.01, 0, 1, 0);
INSERT INTO `kcson`.`serv` (`id`, `serv_tnum`, `serv_name`, `year`, `sub_serv`, `sub_serv_str`, `price`, `2ndprice`, `3rdprice`, `active`, `total`) VALUES (227, '3.4.11', 'Проведение занятий в соответствии с разработанным индивидуальным социально-педагогическим планом (сенсорное развитие, предметно-практическая деятельность, социально-бытовая ориентация, изодеятельность, арт- терапия, игровая деятельность, музыкальные занятия, спортивные, досуговые, экскурсионные мероприятия), в том числе групповых', 2019, 216, '3.4',0 , 64.27, 0, 1, 0);
INSERT INTO `kcson`.`serv` (`id`, `serv_tnum`, `serv_name`, `year`, `sub_serv`, `sub_serv_str`, `price`, `2ndprice`, `3rdprice`, `active`, `total`) VALUES (228, '3.4.12', 'Оказание помощи в обучении навыкам компьютерной грамотности', 2019, 216, '3.4',0 , 142.56, 0, 1, 0);
INSERT INTO `kcson`.`serv` (`id`, `serv_tnum`, `serv_name`, `year`, `sub_serv`, `sub_serv_str`, `price`, `2ndprice`, `3rdprice`, `active`, `total`) VALUES (229, '3.4.13', 'Организация досуга (в том числе сопровождение на социокультурные мероприятия)', 2019, 216, '3.4',0 , 113.35, 0, 1, 0);
INSERT INTO `kcson`.`serv` (`id`, `serv_tnum`, `serv_name`, `year`, `sub_serv`, `sub_serv_str`, `price`, `2ndprice`, `3rdprice`, `active`, `total`) VALUES (230, '3.4.14', 'Организация летнего отдыха', 2019, 216, '3.4',0 , 940.19, 0, 1, 0);
INSERT INTO `kcson`.`serv` (`id`, `serv_tnum`, `serv_name`, `year`, `sub_serv`, `sub_serv_str`, `price`, `2ndprice`, `3rdprice`, `active`, `total`) VALUES (231, '3.4.15', 'Чтение журналов, газет, книг', 2019, 216, '3.4',0 , 546.88, 0, 1, 0);
INSERT INTO `kcson`.`serv` (`id`, `serv_tnum`, `serv_name`, `year`, `sub_serv`, `sub_serv_str`, `price`, `2ndprice`, `3rdprice`, `active`, `total`) VALUES (232, '3.5', 'Социально-трудовые услуги:', 2019, 150, '3',0 ,0 , 0, 1, 1);
INSERT INTO `kcson`.`serv` (`id`, `serv_tnum`, `serv_name`, `year`, `sub_serv`, `sub_serv_str`, `price`, `2ndprice`, `3rdprice`, `active`, `total`) VALUES (233, '3.5.1', 'Проведение мероприятий по использованию трудовых возможностей и обучению доступным профессиональным навыкам', 2019, 232, '3.5',0 , 671.2, 0, 1, 0);
INSERT INTO `kcson`.`serv` (`id`, `serv_tnum`, `serv_name`, `year`, `sub_serv`, `sub_serv_str`, `price`, `2ndprice`, `3rdprice`, `active`, `total`) VALUES (234, '3.5.2', 'Профессиональная ориентация', 2019, 232, '3.5',0 , 426.84, 0, 1, 0);
INSERT INTO `kcson`.`serv` (`id`, `serv_tnum`, `serv_name`, `year`, `sub_serv`, `sub_serv_str`, `price`, `2ndprice`, `3rdprice`, `active`, `total`) VALUES (235, '3.5.3', 'Организация обучения в трудовых мастерских', 2019, 232, '3.5',0 , 89.46, 0, 1, 0);
INSERT INTO `kcson`.`serv` (`id`, `serv_tnum`, `serv_name`, `year`, `sub_serv`, `sub_serv_str`, `price`, `2ndprice`, `3rdprice`, `active`, `total`) VALUES (236, '3.5.4', 'Организация помощи в получении образования, в том числе профессионального образования, инвалидами (детьми- инвалидами) в соответствии с их способностями', 2019, 232, '3.5',0 , 1582.05, 0, 1, 0);
INSERT INTO `kcson`.`serv` (`id`, `serv_tnum`, `serv_name`, `year`, `sub_serv`, `sub_serv_str`, `price`, `2ndprice`, `3rdprice`, `active`, `total`) VALUES (237, '3.5.5', 'Содействие в получении образования и(или) профессии', 2019, 232, '3.5',0 , 425.89, 0, 1, 0);
INSERT INTO `kcson`.`serv` (`id`, `serv_tnum`, `serv_name`, `year`, `sub_serv`, `sub_serv_str`, `price`, `2ndprice`, `3rdprice`, `active`, `total`) VALUES (238, '3.5.6', 'Оказание помощи в трудоустройстве', 2019, 232, '3.5',0 , 180.71, 0, 1, 0);
INSERT INTO `kcson`.`serv` (`id`, `serv_tnum`, `serv_name`, `year`, `sub_serv`, `sub_serv_str`, `price`, `2ndprice`, `3rdprice`, `active`, `total`) VALUES (239, '3.6', 'Социально-правовые услуги:', 2019, 150, '3',0 ,0 , 0, 1, 1);
INSERT INTO `kcson`.`serv` (`id`, `serv_tnum`, `serv_name`, `year`, `sub_serv`, `sub_serv_str`, `price`, `2ndprice`, `3rdprice`, `active`, `total`) VALUES (240, '3.6.1', 'Оказание помощи в оформлении документов и восстановлении утраченных документов получателя социальных услуг', 2019, 239, '3.6',0 , 184.26, 0, 1, 0);
INSERT INTO `kcson`.`serv` (`id`, `serv_tnum`, `serv_name`, `year`, `sub_serv`, `sub_serv_str`, `price`, `2ndprice`, `3rdprice`, `active`, `total`) VALUES (241, '3.6.2', 'Содействие в получении полиса обязательного медицинского страхования', 2019, 239, '3.6',0 , 538.43, 0, 1, 0);
INSERT INTO `kcson`.`serv` (`id`, `serv_tnum`, `serv_name`, `year`, `sub_serv`, `sub_serv_str`, `price`, `2ndprice`, `3rdprice`, `active`, `total`) VALUES (242, '3.6.3', 'Консультирование по вопросам усыновления (удочерения)', 2019, 239, '3.6',0 , 275.56, 0, 1, 0);
INSERT INTO `kcson`.`serv` (`id`, `serv_tnum`, `serv_name`, `year`, `sub_serv`, `sub_serv_str`, `price`, `2ndprice`, `3rdprice`, `active`, `total`) VALUES (243, '3.6.4', 'Проведение переговоров и консультаций в интересах получателя социальных услуг', 2019, 239, '3.6',0 , 180.47, 0, 1, 0);
INSERT INTO `kcson`.`serv` (`id`, `serv_tnum`, `serv_name`, `year`, `sub_serv`, `sub_serv_str`, `price`, `2ndprice`, `3rdprice`, `active`, `total`) VALUES (244, '3.6.5', 'Оформление исковых заявлений на лишение родительских прав либо восстановление в родительских правах', 2019, 239, '3.6',0 , 275.56, 0, 1, 0);
INSERT INTO `kcson`.`serv` (`id`, `serv_tnum`, `serv_name`, `year`, `sub_serv`, `sub_serv_str`, `price`, `2ndprice`, `3rdprice`, `active`, `total`) VALUES (245, '3.6.6', 'Содействие в привлечении к уголовной ответственности подозреваемых в психическом и физическом насилии над получателем социальных услуг', 2019, 239, '3.6',0 , 359.33, 0, 1, 0);
INSERT INTO `kcson`.`serv` (`id`, `serv_tnum`, `serv_name`, `year`, `sub_serv`, `sub_serv_str`, `price`, `2ndprice`, `3rdprice`, `active`, `total`) VALUES (246, '3.6.7', 'Содействие в оформлении документов, необходимых для помещения в стационарную организацию социального обслуживания', 2019, 239, '3.6',0 , 359.33, 0, 1, 0);
INSERT INTO `kcson`.`serv` (`id`, `serv_tnum`, `serv_name`, `year`, `sub_serv`, `sub_serv_str`, `price`, `2ndprice`, `3rdprice`, `active`, `total`) VALUES (247, '3.6.8', 'Подготовка документов в государственные или муниципальные органы, организации и(или) суды', 2019, 239, '3.6',0 , 359.33, 0, 1, 0);
INSERT INTO `kcson`.`serv` (`id`, `serv_tnum`, `serv_name`, `year`, `sub_serv`, `sub_serv_str`, `price`, `2ndprice`, `3rdprice`, `active`, `total`) VALUES (248, '3.6.9', 'Контроль соблюдения имущественных прав получателя социальных услуг', 2019, 239, '3.6',0 , 183.8, 0, 1, 0);
INSERT INTO `kcson`.`serv` (`id`, `serv_tnum`, `serv_name`, `year`, `sub_serv`, `sub_serv_str`, `price`, `2ndprice`, `3rdprice`, `active`, `total`) VALUES (249, '3.6.10', 'Оформление сберегательных вкладов', 2019, 239, '3.6',0 , 179.76, 0, 1, 0);
INSERT INTO `kcson`.`serv` (`id`, `serv_tnum`, `serv_name`, `year`, `sub_serv`, `sub_serv_str`, `price`, `2ndprice`, `3rdprice`, `active`, `total`) VALUES (250, '3.6.11', 'Содействие в восстановлении утраченного (сохранении занимаемого) жилья, наследства', 2019, 239, '3.6',0 , 540.57, 0, 1, 0);
INSERT INTO `kcson`.`serv` (`id`, `serv_tnum`, `serv_name`, `year`, `sub_serv`, `sub_serv_str`, `price`, `2ndprice`, `3rdprice`, `active`, `total`) VALUES (251, '3.6.12', 'Оказание помощи в получении юридических услуг (в том числе бесплатно)', 2019, 239, '3.6',0 , 359.81, 0, 1, 0);
INSERT INTO `kcson`.`serv` (`id`, `serv_tnum`, `serv_name`, `year`, `sub_serv`, `sub_serv_str`, `price`, `2ndprice`, `3rdprice`, `active`, `total`) VALUES (252, '3.6.13', 'Оказание помощи в защите прав и законных интересов получателя социальных услуг', 2019, 239, '3.6',0 , 244.05, 0, 1, 0);
INSERT INTO `kcson`.`serv` (`id`, `serv_tnum`, `serv_name`, `year`, `sub_serv`, `sub_serv_str`, `price`, `2ndprice`, `3rdprice`, `active`, `total`) VALUES (253, '3.7', 'Услуги в целях повышения коммуникативного потенциала получателей социальных услуг, имеющих ограничения жизнедеятельности, в том числе детей-инвалидов:', 2019, 150, '3',0 ,0 , 0, 1, 1);
INSERT INTO `kcson`.`serv` (`id`, `serv_tnum`, `serv_name`, `year`, `sub_serv`, `sub_serv_str`, `price`, `2ndprice`, `3rdprice`, `active`, `total`) VALUES (254, '3.7.1', 'Консультирование по вопросам социально-средовой реабилитации', 2019, 253, '3.7',0 , 426.37, 0, 1, 0);
INSERT INTO `kcson`.`serv` (`id`, `serv_tnum`, `serv_name`, `year`, `sub_serv`, `sub_serv_str`, `price`, `2ndprice`, `3rdprice`, `active`, `total`) VALUES (255, '3.7.2', 'Обучение навыкам социально-средовой ориентации (в том числе самостоятельному передвижению, включая изучение жизненно важных маршрутов передвижения)', 2019, 253, '3.7',0 , 268.65, 0, 1, 0);
INSERT INTO `kcson`.`serv` (`id`, `serv_tnum`, `serv_name`, `year`, `sub_serv`, `sub_serv_str`, `price`, `2ndprice`, `3rdprice`, `active`, `total`) VALUES (256, '3.7.3', 'Обучение инвалидов (детей-инвалидов) пользованию средствами ухода и техническими средствами реабилитации', 2019, 253, '3.7',0 , 268.65, 0, 1, 0);
INSERT INTO `kcson`.`serv` (`id`, `serv_tnum`, `serv_name`, `year`, `sub_serv`, `sub_serv_str`, `price`, `2ndprice`, `3rdprice`, `active`, `total`) VALUES (257, '3.7.4', 'Обучение навыкам (поддержание навыков) поведения в быту и общественных местах', 2019, 253, '3.7',0 , 238.79, 0, 1, 0);
INSERT INTO `kcson`.`serv` (`id`, `serv_tnum`, `serv_name`, `year`, `sub_serv`, `sub_serv_str`, `price`, `2ndprice`, `3rdprice`, `active`, `total`) VALUES (258, '3.7.5', 'Организация коммуникативного пространства и коммуникативных ситуаций по месту проживания (получения социальных услуг)', 2019, 253, '3.7',0 , 276.03, 0, 1, 0);
INSERT INTO `kcson`.`serv` (`id`, `serv_tnum`, `serv_name`, `year`, `sub_serv`, `sub_serv_str`, `price`, `2ndprice`, `3rdprice`, `active`, `total`) VALUES (259, '4', 'Срочные социальные услуги', 2019, 1, 'Итог',0 ,0 , 0, 1, 1);
INSERT INTO `kcson`.`serv` (`id`, `serv_tnum`, `serv_name`, `year`, `sub_serv`, `sub_serv_str`, `price`, `2ndprice`, `3rdprice`, `active`, `total`) VALUES (260, '4.1', 'Консультирование по вопросам социального обслуживания', 2019, 259, '4',0 , 135.26, 0, 1, 0);
INSERT INTO `kcson`.`serv` (`id`, `serv_tnum`, `serv_name`, `year`, `sub_serv`, `sub_serv_str`, `price`, `2ndprice`, `3rdprice`, `active`, `total`) VALUES (261, '4.2', 'Обеспечение бесплатным горячим питанием или набором продуктов:', 2019, 259, '4',0 ,0 , 0, 1, 1);
INSERT INTO `kcson`.`serv` (`id`, `serv_tnum`, `serv_name`, `year`, `sub_serv`, `sub_serv_str`, `price`, `2ndprice`, `3rdprice`, `active`, `total`) VALUES (262, '4.2.1', 'обеспечение бесплатным горячим питанием граждан пожилого возраста и инвалидов', 2019, 261, '4.2',0 , 153.75, 0, 1, 0);
INSERT INTO `kcson`.`serv` (`id`, `serv_tnum`, `serv_name`, `year`, `sub_serv`, `sub_serv_str`, `price`, `2ndprice`, `3rdprice`, `active`, `total`) VALUES (263, '4.2.2', 'обеспечение набором продуктов граждан пожилого возраста и инвалидов', 2019, 261, '4.2',0 , 655.41, 0, 1, 0);
INSERT INTO `kcson`.`serv` (`id`, `serv_tnum`, `serv_name`, `year`, `sub_serv`, `sub_serv_str`, `price`, `2ndprice`, `3rdprice`, `active`, `total`) VALUES (264, '4.2.3', 'обеспечение набором продуктов семей с детьми', 2019, 261, '4.2',0 , 660.94, 0, 1, 0);
INSERT INTO `kcson`.`serv` (`id`, `serv_tnum`, `serv_name`, `year`, `sub_serv`, `sub_serv_str`, `price`, `2ndprice`, `3rdprice`, `active`, `total`) VALUES (265, '4.3', 'Обеспечение одеждой, обувью и другими предметами первой необходимости', 2019, 259, '4',0 , 7377.42, 0, 1, 0);
INSERT INTO `kcson`.`serv` (`id`, `serv_tnum`, `serv_name`, `year`, `sub_serv`, `sub_serv_str`, `price`, `2ndprice`, `3rdprice`, `active`, `total`) VALUES (266, '4.4', 'Содействие в получении юридической помощи в целях защиты прав и законных интересов получателей социальных услуг', 2019, 259, '4',0 , 127.2, 0, 1, 0);
INSERT INTO `kcson`.`serv` (`id`, `serv_tnum`, `serv_name`, `year`, `sub_serv`, `sub_serv_str`, `price`, `2ndprice`, `3rdprice`, `active`, `total`) VALUES (267, '4.5', 'Содействие в получении временного жилого помещения', 2019, 259, '4',0 , 257.15, 0, 1, 0);
INSERT INTO `kcson`.`serv` (`id`, `serv_tnum`, `serv_name`, `year`, `sub_serv`, `sub_serv_str`, `price`, `2ndprice`, `3rdprice`, `active`, `total`) VALUES (268, '4.6', 'Содействие в получении экстренной психологической помощи с привлечением к этой работе психологов и священнослужителей', 2019, 259, '4',0 , 270.52, 0, 1, 0);
INSERT INTO `kcson`.`serv` (`id`, `serv_tnum`, `serv_name`, `year`, `sub_serv`, `sub_serv_str`, `price`, `2ndprice`, `3rdprice`, `active`, `total`) VALUES (269, '4.7', 'Оказание консультационной психологической помощи, в том числе анонимно с использованием телефона доверия', 2019, 259, '4',0 , 129.09, 0, 1, 0);

COMMIT;
END$$

DELIMITER ;

-- -----------------------------------------------------
-- procedure import_dep_all
-- -----------------------------------------------------

USE `kcson`;
DROP procedure IF EXISTS `kcson`.`import_dep_all`;

DELIMITER $$
USE `kcson`$$
CREATE DEFINER=`root`@`localhost` PROCEDURE `import_dep_all`()
BEGIN
START TRANSACTION;
INSERT INTO `kcson`.`dep` (`id`, `depName`, `depFullName`, `note`) VALUES (DEFAULT, 'Не указано', 'Не указано', NULL);
INSERT INTO `kcson`.`dep` (`id`, `depName`, `depFullName`, `note`) VALUES (DEFAULT, 'СДО-1', 'СДО-1 Социально-досуговое отделение-1', NULL);
INSERT INTO `kcson`.`dep` (`id`, `depName`, `depFullName`, `note`) VALUES (DEFAULT, 'СДО-2', 'СДО-2 Социально-досуговое отделение-2', NULL);
INSERT INTO `kcson`.`dep` (`id`, `depName`, `depFullName`, `note`) VALUES (DEFAULT, 'СОСМОД-1','ОСОД-1 Отделение социального обслуживания на дому граждан пожилого возраста и инвалидов-1',NULL);
INSERT INTO `kcson`.`dep` (`id`, `depName`, `depFullName`, `note`) VALUES (DEFAULT, 'СОСМОД-10','ОСОД-10 Отделение социального обслуживания на дому граждан пожилого возраста и инвалидов-10',NULL);
INSERT INTO `kcson`.`dep` (`id`, `depName`, `depFullName`, `note`) VALUES (DEFAULT, 'СОСМОД-11','ОСОД-11 Отделение социального обслуживания на дому граждан пожилого возраста и инвалидов-11',NULL);
INSERT INTO `kcson`.`dep` (`id`, `depName`, `depFullName`, `note`) VALUES (DEFAULT, 'СОСМОД-12','ОСОД-12 Отделение социального обслуживания на дому граждан пожилого возраста и инвалидов-12',NULL);
INSERT INTO `kcson`.`dep` (`id`, `depName`, `depFullName`, `note`) VALUES (DEFAULT, 'СОСМОД-2','ОСОД-2 Отделение социального обслуживания на дому граждан пожилого возраста и инвалидов-2',NULL);
INSERT INTO `kcson`.`dep` (`id`, `depName`, `depFullName`, `note`) VALUES (DEFAULT, 'СОСМОД-3','ОСОД-3 Отделение социального обслуживания на дому граждан пожилого возраста и инвалидов-3',NULL);
INSERT INTO `kcson`.`dep` (`id`, `depName`, `depFullName`, `note`) VALUES (DEFAULT, 'СОСМОД-4','ОСОД-4 Отделение социального обслуживания на дому граждан пожилого возраста и инвалидов-4',NULL);
INSERT INTO `kcson`.`dep` (`id`, `depName`, `depFullName`, `note`) VALUES (DEFAULT, 'СОСМОД-5','ОСОД-5 Отделение социального обслуживания на дому граждан пожилого возраста и инвалидов-5',NULL);
INSERT INTO `kcson`.`dep` (`id`, `depName`, `depFullName`, `note`) VALUES (DEFAULT, 'СОСМОД-6','ОСОД-6 Отделение социального обслуживания на дому граждан пожилого возраста и инвалидов-6',NULL);
INSERT INTO `kcson`.`dep` (`id`, `depName`, `depFullName`, `note`) VALUES (DEFAULT, 'СОСМОД-7','ОСОД-7 Отделение социального обслуживания на дому граждан пожилого возраста и инвалидов-7',NULL);
INSERT INTO `kcson`.`dep` (`id`, `depName`, `depFullName`, `note`) VALUES (DEFAULT, 'СОСМОД-8','ОСОД-8 Отделение социального обслуживания на дому граждан пожилого возраста и инвалидов-8',NULL);
INSERT INTO `kcson`.`dep` (`id`, `depName`, `depFullName`, `note`) VALUES (DEFAULT, 'СОСМОД-9','ОСОД-9 Отделение социального обслуживания на дому граждан пожилого возраста и инвалидов-9',NULL);
COMMIT;

End$$

DELIMITER ;

-- -----------------------------------------------------
-- procedure import_all
-- -----------------------------------------------------

USE `kcson`;
DROP procedure IF EXISTS `kcson`.`import_all`;

DELIMITER $$
USE `kcson`$$
CREATE DEFINER=`root`@`localhost` PROCEDURE `import_all`()
BEGIN
call import_serv_all;
call import_ripso;
call import_dep_all;
# Error caching here
#call delete_setup_tools;
end$$

DELIMITER ;

-- -----------------------------------------------------
-- function GET_DEP
-- -----------------------------------------------------

USE `kcson`;
DROP function IF EXISTS `kcson`.`GET_DEP`;

DELIMITER $$
USE `kcson`$$
CREATE DEFINER=`root`@`localhost` FUNCTION `GET_DEP`(
 `wrkID` INT
) RETURNS int(11)
	LANGUAGE SQL
	NOT DETERMINISTIC
	READS SQL DATA
    
	SQL SECURITY INVOKER
    COMMENT 'get default department '
BEGIN
	#declare wrkID int (0);
	declare dep_id int (0);
	set dep_id = (select last_dep from worker_settings  where id=wrkID);
	
    if dep_id is null then
		set dep_id = (select max(dep_id) from dep_has_worker  where worker_id=wrkID and archive=0);
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
		set dep_id = (select max(dep_id) from dep_has_worker  where worker_id=wrkID and archive=0);
        if dep_id > 0  then 
			update worker_settings set last_dep=dep_id  where id=wrkID;
			return dep_id;
		else
			return 1;
			# 1 - undefined dep
		end if;
            
	end if;
END;$$

DELIMITER ;

-- -----------------------------------------------------
-- function GET_wID
-- -----------------------------------------------------

USE `kcson`;
DROP function IF EXISTS `kcson`.`GET_wID`;

DELIMITER $$
USE `kcson`$$
CREATE DEFINER=`root`@`localhost` FUNCTION `GET_wID`(
) RETURNS int(11)
	LANGUAGE SQL
	NOT DETERMINISTIC
	READS SQL DATA
    
	SQL SECURITY INVOKER
    COMMENT 'get default department '
BEGIN
	return (select id from worker w where w.user=SUBSTRING_INDEX(user(), '@', 1));
END$$

DELIMITER ;

-- -----------------------------------------------------
-- procedure import_ripso
-- -----------------------------------------------------

USE `kcson`;
DROP procedure IF EXISTS `kcson`.`import_ripso`;

DELIMITER $$
USE `kcson`$$
CREATE DEFINER=`root`@`localhost` PROCEDURE `import_ripso`()
BEGIN
START TRANSACTION;

INSERT INTO `kcson`.`ripso` (`id`, `ripsoNum`, `year`, `active`, `servform`, `months`) 
values 
(default,	'2',	'2019',	'1',	'Полустационарная форма социального обслуживания с периодом пребывания до четырех часов',	12),
(default,	'3',	'2019',	'1',	'',	2),
(default,	'4',	'2019',	'1',	'Стационарная форма социального обслуживания',	3),
(default,	'5',	'2019',	'1',	'',	12),
(default,	'6',	'2019',	'1',	'Социальное обслуживание на дому',	12),
(default,	'7',	'2019',	'1',	'Полустационарная форма социального обслуживания с периодом пребывания до четырех часов',	12),
(default,	'8',	'2019',	'1',	'',	2),
(default,	'9',	'2019',	'1',	'Стационарная форма социального обслуживания',	3),
(default,	'10',	'2019',	'0',		'',	0),
(default,	'11',	'2019',	'0',		'',	0),
(default,	'12',	'2019', '0',		'',	0),
(default,	'13',	'2019',	'0',		'',	0),
(default,	'14',	'2019',	'1',	'Социальное обслуживание на дому',	12),
(default,	'15',	'2019',	'1',	'',	12),
(default,	'16',	'2019',	'1',	'',	12);

COMMIT;

End$$

DELIMITER ;

-- -----------------------------------------------------
-- function GET_CONTR
-- -----------------------------------------------------

USE `kcson`;
DROP function IF EXISTS `kcson`.`GET_CONTR`;

DELIMITER $$
USE `kcson`$$
CREATE DEFINER=`root`@`localhost` FUNCTION `GET_CONTR`(
 `idfio` INT, `vdate` date, `idep` int
) RETURNS int(11)
    READS SQL DATA
    DETERMINISTIC
    COMMENT 'get idcontract '
BEGIN
	declare cc int (0);
	declare rr varchar (255);
	set cc = (select count(id) from contracts where ripso_id in  
		(select ripso_id from dep_has_ripso  where dep_id=idep) 
        and startdate <= vdate  and enddate  >= vdate and blocked=0 and ufio_id=idfio); 
	if cc = 1 then 
		return (select id from contracts where ripso_id in  
			(select ripso_id from dep_has_ripso  where dep_id=idep) 
            and startdate <= vdate  and enddate  >= vdate and blocked=0 and ufio_id=idfio);
	elseif cc = 0 then 
		set rr = CONCAT ('Нет договора в этот период для этого человека в этом отделении' , idfio , vdate, idep);
		SIGNAL SQLSTATE '45001' SET MESSAGE_TEXT = cc;
		return 0;
	else
		set rr = CONCAT ("Несколько договоров в этот период для этого человека в этом отделении",idfio , vdate, idep );
		SIGNAL SQLSTATE '45001' SET MESSAGE_TEXT  = cc;
		return -1;
	end if;
END$$

DELIMITER ;

-- -----------------------------------------------------
-- function CHECK_OVERDID
-- -----------------------------------------------------

USE `kcson`;
DROP function IF EXISTS `kcson`.`CHECK_OVERDID`;

DELIMITER $$
USE `kcson`$$
CREATE DEFINER=`root`@`localhost` FUNCTION `CHECK_OVERDID`( CONTR  int, SERV int) 
RETURNS int(11)
	LANGUAGE SQL
	DETERMINISTIC
	READS SQL DATA
    SQL SECURITY DEFINER
    COMMENT 'check overdid return serv left 
    no existence check!!!'
BEGIN
	DECLARE pln int;
	DECLARE fll int;
    
select  planned, filled into pln, fll 
from  contracts_has_serv where
  contracts_id = CONTR and
  serv_id = SERV;
  
return (pln - fll);
END$$

DELIMITER ;

-- -----------------------------------------------------
-- procedure delete_setup_tools
-- -----------------------------------------------------

USE `kcson`;
DROP procedure IF EXISTS `kcson`.`delete_setup_tools`;

DELIMITER $$
USE `kcson`$$
CREATE DEFINER=`root`@`localhost` PROCEDURE `delete_setup_tools`()
BEGIN
#drop PROCEDURE if exists import_serv_all;
#drop PROCEDURE if exists import_ripso;
#drop PROCEDURE if exists import_dep_all;
end$$

DELIMITER ;

-- -----------------------------------------------------
-- procedure gaver_Rdata
-- -----------------------------------------------------

USE `kcson`;
DROP procedure IF EXISTS `kcson`.`gaver_Rdata`;

DELIMITER $$
USE `kcson`$$
CREATE DEFINER=`root`@`localhost` procedure `gaver_Rdata`(
	`rnameID` INT, `rperiodID` INT
)
    MODIFIES SQL DATA
	NOT DETERMINISTIC
    COMMENT ''
BEGIN
	#declare wrkID int;
	declare res int default 0;
	#set  wrkID= (select id from worker w where w.user=current_user());
	
	insert into Rdata (`year`, uslnum, money, `2ndmoney`, ufio_id, dep_id, serv_id, worker_id )
    select year(vdate), uslnum, uslnum*1, uslnum*1, ufio_id, dep_id, serv_id, worker_id from
    main m inner join contracts c on m.cotracts_id=c.id
    
    ;
END$$

DELIMITER ;

-- -----------------------------------------------------
-- procedure SHOW_COL
-- -----------------------------------------------------

USE `kcson`;
DROP procedure IF EXISTS `kcson`.`SHOW_COL`;

DELIMITER $$
USE `kcson`$$
CREATE PROCEDURE SHOW_COL(IN sqlToShow TEXT)	
	LANGUAGE SQL
	DETERMINISTIC
	READS SQL DATA
    SQL SECURITY DEFINER
    COMMENT ''
BEGIN
    DROP TEMPORARY TABLE IF EXISTS tempTable;
    SET @sqlLimit0 = CONCAT('CREATE TEMPORARY TABLE tempTable AS (SELECT * FROM (',
                            sqlToShow, ') subq LIMIT 0)');
    PREPARE stmt FROM @sqlLimit0;
    EXECUTE stmt;
    DEALLOCATE PREPARE stmt;
    SHOW COLUMNS FROM tempTable;
END$$

DELIMITER ;

-- -----------------------------------------------------
-- procedure Pivot
-- -----------------------------------------------------

USE `kcson`;
DROP procedure IF EXISTS `kcson`.`Pivot`;

DELIMITER $$
USE `kcson`$$
CREATE PROCEDURE Pivot(
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
END;$$

DELIMITER ;

-- -----------------------------------------------------
-- procedure CREATE_PIVOT
-- -----------------------------------------------------

USE `kcson`;
DROP procedure IF EXISTS `kcson`.`CREATE_PIVOT`;

DELIMITER $$
USE `kcson`$$
CREATE PROCEDURE CREATE_PIVOT(
    IN tbl_qry VARCHAR(2000),       -- table name (or db.tbl)
    IN base_cols VARCHAR(99),      -- column(s) on the left, separated by commas
    IN pivot_col VARCHAR(64),      -- name of column to put across the top
    IN tally_col VARCHAR(64),      -- name of column to SUM up
    IN where_clause VARCHAR(1000),   -- empty string or "WHERE ..."
    IN order_by VARCHAR(99)        -- empty string or "ORDER BY ..."; usually the base_cols
    )
    DETERMINISTIC
    SQL SECURITY INVOKER
BEGIN
    -- GET the SUM()s
    SET @subq = CONCAT('SELECT DISTINCT ', pivot_col, ' AS val ',
                    ' FROM ', tbl_qry, ' ', where_clause, ' ORDER BY 1');

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
SELECT @stmt;
    PREPARE _sql FROM @stmt;
    EXECUTE _sql;                      -- 2nd step: build SQL for columns
    DEALLOCATE PREPARE _sql;
    -- 3rd: Construct the query and perform it
    SET @stmt2 = CONCAT(
            'SELECT ',
                base_cols, ',\n',
                @sums,
                ',\n SUM(', tally_col, ') AS Total'
            '\n FROM ', tbl_qry, ' ',
            where_clause,
            ' GROUP BY ', base_cols,
            '\n WITH ROLLUP',
            '\n', order_by
        );
SELECT @stmt2;                    -- The statement that generates the result
    PREPARE _sql FROM @stmt2;
    EXECUTE _sql;                     -- The resulting pivot table ouput
    DEALLOCATE PREPARE _sql;
    -- For debugging / tweaking, SELECT the various @variables after CALLing.
END;$$

DELIMITER ;

-- -----------------------------------------------------
-- procedure serv_dep_total
-- -----------------------------------------------------

USE `kcson`;
DROP procedure IF EXISTS `kcson`.`serv_dep_total`;

DELIMITER $$
USE `kcson`$$
CREATE DEFINER=`root`@`localhost` procedure `serv_dep_total`()
	DETERMINISTIC
    COMMENT ''
BEGIN
	call CREATE_PIVOT("
	(select serv_tnum, s.id, ufio_id, serv_id , uslnum 
	from main_NZ m inner join serv s on m.serv_id=s.id
	where dep_id = GET_DEP(GET_wID())
	)  main1",

	 "ufio_id", "serv_tnum", "uslnum" , "" , "");
     
END;$$

DELIMITER ;

-- -----------------------------------------------------
-- procedure dep_serv_total
-- -----------------------------------------------------

USE `kcson`;
DROP procedure IF EXISTS `kcson`.`dep_serv_total`;

DELIMITER $$
USE `kcson`$$
CREATE DEFINER=`root`@`localhost` procedure `dep_serv_total`()
	DETERMINISTIC
    COMMENT ''
BEGIN
	call CREATE_PIVOT("
	(select tnum, s.id, ufio_id, serv_id , uslnum 
	from main_NZ m inner join serv s on m.serv_id=s.id
	where dep_id = GET_DEP(GET_wID())
	)  main1",

	 "ufio_id", "tnum", "uslnum" , "" , "");
     
END;$$

DELIMITER ;

-- -----------------------------------------------------
-- procedure SET_DEPS_TABLE
-- -----------------------------------------------------

USE `kcson`;
DROP procedure IF EXISTS `kcson`.`SET_DEPS_TABLE`;

DELIMITER $$
USE `kcson`$$
CREATE DEFINER=`root`@`localhost` PROCEDURE `SET_DEPS_TABLE`(
 `wrkID` INT )
    SQL SECURITY DEFINER
    COMMENT 'set  departments '
BEGIN
	#set @wrkID  = (select id from worker w where w.user=user());
    DECLARE CONTINUE HANDLER FOR SQLSTATE '42S02' SET @err = 1;
    SET @err = 0;
    select null from active_deps;

    if @err = 1 then
		CREATE temporary table active_deps select distinct dep_id from dep_has_worker  where worker_id=wrkID and archive=0;
	end if;
END$$

DELIMITER ;

-- -----------------------------------------------------
-- procedure GET_VER
-- -----------------------------------------------------

USE `kcson`;
DROP procedure IF EXISTS `kcson`.`GET_VER`;

DELIMITER $$
USE `kcson`$$
CREATE procedure `GET_VER`()
	DETERMINISTIC
    COMMENT 'return sql version, change if tables changed'
    LANGUAGE SQL 
	select 85;$$

DELIMITER ;

-- -----------------------------------------------------
-- function get_last_contr
-- -----------------------------------------------------

USE `kcson`;
DROP function IF EXISTS `kcson`.`get_last_contr`;

DELIMITER $$
USE `kcson`$$
CREATE DEFINER=`root`@`localhost` FUNCTION `get_last_contr`() 
RETURNS int(11)
	LANGUAGE SQL
	DETERMINISTIC
	READS SQL DATA
    SQL SECURITY DEFINER
    COMMENT 'check overdid return serv left 
    no existence check!!!'
BEGIN
	#if @worker_settings_not_upd then
	#	return @contr 
	#else
		#set @contr = (select last_ufio from worker_settings where id = GET_WID());
	return (select last_contr from worker_settings where id = GET_WID());
    #end if
END$$

DELIMITER ;

-- -----------------------------------------------------
-- function get_last_ufio
-- -----------------------------------------------------

USE `kcson`;
DROP function IF EXISTS `kcson`.`get_last_ufio`;

DELIMITER $$
USE `kcson`$$
CREATE DEFINER=`root`@`localhost` FUNCTION `get_last_ufio`() 
RETURNS int(11)
	LANGUAGE SQL
	DETERMINISTIC
	READS SQL DATA
    SQL SECURITY DEFINER
    COMMENT 'check overdid return serv left 
    no existence check!!!'
BEGIN
	#if @worker_settings_not_upd then
	#	return @contr 
	#else
		#set @contr = (select last_ufio from worker_settings where id = GET_WID());
	return (select last_ufio from worker_settings where id = GET_WID());
    #end if
END$$

DELIMITER ;

-- -----------------------------------------------------
-- function set_last_ufio
-- -----------------------------------------------------

USE `kcson`;
DROP function IF EXISTS `kcson`.`set_last_ufio`;

DELIMITER $$
USE `kcson`$$
CREATE DEFINER=`root`@`localhost` FUNCTION `set_last_ufio`(ufio int) 
RETURNS int(11)
	LANGUAGE SQL
	DETERMINISTIC
    SQL SECURITY DEFINER
    COMMENT 'check overdid return serv left 
    no existence check!!!'
BEGIN

	update worker_settings set last_ufio=ufio where id = GET_WID();
    return 1;
    #end if
END$$

DELIMITER ;

-- -----------------------------------------------------
-- function set_last_contr
-- -----------------------------------------------------

USE `kcson`;
DROP function IF EXISTS `kcson`.`set_last_contr`;

DELIMITER $$
USE `kcson`$$
CREATE DEFINER=`root`@`localhost` FUNCTION `set_last_contr`(contr int) 
RETURNS int(11)
	LANGUAGE SQL
	DETERMINISTIC
    SQL SECURITY DEFINER
    COMMENT 'check overdid return serv left 
    no existence check!!!'
BEGIN

	update worker_settings set last_contr=contr where id = GET_WID();
    return 1;
END$$

DELIMITER ;

-- -----------------------------------------------------
-- function set_last_dep
-- -----------------------------------------------------

USE `kcson`;
DROP function IF EXISTS `kcson`.`set_last_dep`;

DELIMITER $$
USE `kcson`$$
CREATE DEFINER=`root`@`localhost` FUNCTION `set_last_dep`(contr int) 
RETURNS int(11)
	LANGUAGE SQL
	DETERMINISTIC
    SQL SECURITY DEFINER
    COMMENT 'check overdid return serv left 
    no existence check!!!'
BEGIN

	update worker_settings set last_dep=dep where id = GET_WID();
    return 1;
END$$

DELIMITER ;

-- -----------------------------------------------------
-- procedure GET_DEPS
-- -----------------------------------------------------

USE `kcson`;
DROP procedure IF EXISTS `kcson`.`GET_DEPS`;

DELIMITER $$
USE `kcson`$$
CREATE DEFINER=`root`@`localhost` PROCEDURE `GET_DEPS`(
 `wrkID` INT ) 
	LANGUAGE SQL
	NOT DETERMINISTIC
	READS SQL DATA
	SQL SECURITY INVOKER
    COMMENT 'get  departments '
BEGIN
	#set @wrkID  = (select id from worker w where w.user=user());
	select distinct dep_id from dep_has_worker  where worker_id=wrkID and archive=0;
END$$

DELIMITER ;

-- -----------------------------------------------------
-- function GET_YEAR
-- -----------------------------------------------------

USE `kcson`;
DROP function IF EXISTS `kcson`.`GET_YEAR`;

DELIMITER $$
USE `kcson`$$
CREATE DEFINER=`root`@`localhost` FUNCTION `GET_YEAR`(
 `wrkID` INT
) RETURNS int(11)
    READS SQL DATA
    SQL SECURITY INVOKER
    COMMENT 'get current year '
BEGIN
	declare var int (0);
	#set @wrkID  = (select id from worker w where w.user=user());
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
END$$

DELIMITER ;

-- -----------------------------------------------------
-- function IS_CUR_DEP
-- -----------------------------------------------------

USE `kcson`;
DROP function IF EXISTS `kcson`.`IS_CUR_DEP`;

DELIMITER $$
USE `kcson`$$
CREATE DEFINER=`root`@`localhost` FUNCTION `IS_CUR_DEP`(
 `depID_par` INT
) RETURNS int(11)
	LANGUAGE SQL
	NOT DETERMINISTIC
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
END;$$

DELIMITER ;

-- -----------------------------------------------------
-- procedure __INIT__
-- -----------------------------------------------------

USE `kcson`;
DROP procedure IF EXISTS `kcson`.`__INIT__`;

DELIMITER $$
USE `kcson`$$
CREATE PROCEDURE `__INIT__` ()
BEGIN
	call SET_DEPS_TABLE();
END$$

DELIMITER ;

-- -----------------------------------------------------
-- procedure replace_user
-- -----------------------------------------------------

USE `kcson`;
DROP procedure IF EXISTS `kcson`.`replace_user`;

DELIMITER $$
USE `kcson`$$
CREATE DEFINER=`root`@`localhost` PROCEDURE `replace_user`(IN `p_Name` VARCHAR(32), IN `p_Passw` VARCHAR(200))
    SQL SECURITY DEFINER
BEGIN
    DECLARE `_HOST` CHAR(60) DEFAULT '@\'%\'';
    SET `p_Name` := CONCAT('\'', REPLACE(TRIM(`p_Name`), CHAR(39), CONCAT(CHAR(92), CHAR(39))), '\''),
    `p_Passw` := CONCAT('\'', REPLACE(`p_Passw`, CHAR(39), CONCAT(CHAR(92), CHAR(39))), '\'');
    SET @`sql` := CONCAT('DROP USER IF EXISTS ', `p_Name`, `_HOST`);
    PREPARE `stmt` FROM @`sql`;
    EXECUTE `stmt`;
    SET @`sql` := CONCAT('CREATE USER ', `p_Name`, `_HOST`, ' IDENTIFIED  with mysql_native_password BY ', `p_Passw`);
    PREPARE `stmt` FROM @`sql`;
    EXECUTE `stmt`;
    SET @`sql` := CONCAT('GRANT newuser ON *.* TO ', `p_Name`, `_HOST`, " WITH GRANT OPTION ");
    SET @`sql` := CONCAT('GRANT select, insert, update, execute ON kcson.* TO ', `p_Name`, `_HOST`, ' WITH GRANT OPTION ' );
    PREPARE `stmt` FROM @`sql`;
    EXECUTE `stmt`;
    DEALLOCATE PREPARE `stmt`;
    FLUSH PRIVILEGES;
    select 1 ;
END$$

DELIMITER ;

-- -----------------------------------------------------
-- procedure debug_msg
-- -----------------------------------------------------

USE `kcson`;
DROP procedure IF EXISTS `kcson`.`debug_msg`;

DELIMITER $$
USE `kcson`$$
CREATE PROCEDURE debug_msg(msg VARCHAR(255))
BEGIN
    select concat('** ', msg) AS '** DEBUG:';
END$$

DELIMITER ;

-- -----------------------------------------------------
-- View `kcson`.`user_has_serv`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `kcson`.`user_has_serv`;
DROP VIEW IF EXISTS `kcson`.`user_has_serv` ;
USE `kcson`;
CREATE  OR REPLACE VIEW `user_has_serv` AS SELECT * FROM main where (main.cr_by = GET_wID());

-- -----------------------------------------------------
-- View `kcson`.`dep_has_main`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `kcson`.`dep_has_main`;
DROP VIEW IF EXISTS `kcson`.`dep_has_main` ;
USE `kcson`;
CREATE  OR REPLACE VIEW `dep_has_main` AS SELECT * FROM main where  (main.dep_id = GET_DEP( GET_wID() ));

-- -----------------------------------------------------
-- View `kcson`.`last_used_workers`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `kcson`.`last_used_workers`;
DROP VIEW IF EXISTS `kcson`.`last_used_workers` ;
USE `kcson`;
CREATE  OR REPLACE VIEW `last_used_workers` As 
SELECT worker.id, worker.worker 
FROM worker inner join  main  ON worker.id=main.worker_id 
where  (main.cr_by = GET_wID())
 GROUP BY worker.id, worker.worker
    ORDER BY worker.worker 
    LIMIT 30;

-- -----------------------------------------------------
-- View `kcson`.`_serv_activ`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `kcson`.`_serv_activ`;
DROP VIEW IF EXISTS `kcson`.`_serv_activ` ;
USE `kcson`;
CREATE  OR REPLACE VIEW `_serv_activ` AS
    SELECT 
        s.id,
        CONCAT(s.tnum, ' ', s.serv) AS tserv,
        s.price,
        s.total,
        s.sub_serv,
        s.serv as serv
    FROM
        serv s
    WHERE
        archive = 0;
        # AND total = 0;

-- -----------------------------------------------------
-- View `kcson`.`servOFripso`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `kcson`.`servOFripso`;
DROP VIEW IF EXISTS `kcson`.`servOFripso` ;
USE `kcson`;
CREATE  OR REPLACE VIEW `servOFripso` AS
    SELECT 
        s.*, r.id AS r_id, r.ripso
    FROM
        ripso r
            INNER JOIN
        ripso_has_serv fr ON fr.ripso_id = r.id
            INNER JOIN
        serv s ON s.id = fr.ripso_id
    WHERE
        s.archive = 0 AND r.archive = 0;

-- -----------------------------------------------------
-- View `kcson`.`fioOFdepBYserv`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `kcson`.`fioOFdepBYserv`;
DROP VIEW IF EXISTS `kcson`.`fioOFdepBYserv` ;
USE `kcson`;
CREATE  OR REPLACE VIEW `fioOFdepBYserv` AS SELECT
  ufio, ufio_short,ufiobirth,ESRN,ufioDeath 
FROM ufio
where id in (
select ufio.id from main
  INNER JOIN ufio
    ON main.ufio_id = ufio.id
  INNER JOIN dep
    ON main.dep_id = dep.id
    where main.cr_by = GET_wID( )
    );

-- -----------------------------------------------------
-- View `kcson`.`servOFyear`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `kcson`.`servOFyear`;
DROP VIEW IF EXISTS `kcson`.`servOFyear` ;
USE `kcson`;
CREATE  OR REPLACE VIEW `servOFyear` AS SELECT * FROM kcson.main m where year(m.vdate) = year(current_date());

-- -----------------------------------------------------
-- View `kcson`.`servOFyear-2`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `kcson`.`servOFyear-2`;
DROP VIEW IF EXISTS `kcson`.`servOFyear-2` ;
USE `kcson`;
CREATE  OR REPLACE VIEW `servOFyear-2` AS SELECT * FROM kcson.main m where year(m.vdate) = (year(current_date())-2);

-- -----------------------------------------------------
-- View `kcson`.`servOFyear-3`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `kcson`.`servOFyear-3`;
DROP VIEW IF EXISTS `kcson`.`servOFyear-3` ;
USE `kcson`;
CREATE  OR REPLACE VIEW `servOFyear-3` AS SELECT * FROM kcson.main m where year(m.vdate) = (year(current_date())-3);

-- -----------------------------------------------------
-- View `kcson`.`servOFyear-1`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `kcson`.`servOFyear-1`;
DROP VIEW IF EXISTS `kcson`.`servOFyear-1` ;
USE `kcson`;
CREATE  OR REPLACE VIEW `servOFyear-1` AS SELECT * FROM kcson.main m where year(m.vdate) = (year(current_date())-1);

-- -----------------------------------------------------
-- View `kcson`.`fioOFdepBYset`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `kcson`.`fioOFdepBYset`;
DROP VIEW IF EXISTS `kcson`.`fioOFdepBYset` ;
USE `kcson`;
CREATE  OR REPLACE VIEW `fioOFdepBYset` AS SELECT
  ufio, ufio_short,ufiobirth,ESRN,ufioDeath 
FROM ufio
where id in (
select ufio.id from main
  INNER JOIN ufio
    ON main.ufio_id = ufio.id
  INNER JOIN dep
    ON main.dep_id = dep.id
    where main.cr_by = GET_wID(  )
    );

-- -----------------------------------------------------
-- View `kcson`.`_dep_has_ufio_by_ripso`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `kcson`.`_dep_has_ufio_by_ripso`;
DROP VIEW IF EXISTS `kcson`.`_dep_has_ufio_by_ripso` ;
USE `kcson`;
CREATE  OR REPLACE VIEW `_dep_has_ufio_by_ripso` AS
select * from ufio
where id in (
	select ufio_id from contracts c inner join dep_has_ripso rod on rod.ripso_id = c.ripso_id
	where  rod.dep_id=GET_DEP(GET_wID())
);

-- -----------------------------------------------------
-- View `kcson`.`worker_has_dep`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `kcson`.`worker_has_dep`;
DROP VIEW IF EXISTS `kcson`.`worker_has_dep` ;
USE `kcson`;
CREATE  OR REPLACE VIEW `worker_has_dep` AS
    SELECT 
        dw.dep_id, d.dep
    FROM
        dep_has_worker dw
            INNER JOIN
        dep d ON d.id = dw.dep_id
            INNER JOIN
        worker w ON dw.worker_id = w.id
    WHERE
        dw.worker_id = GET_wID()
            AND dw.archive = 0;

-- -----------------------------------------------------
-- View `kcson`.`dep_has_serv`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `kcson`.`dep_has_serv`;
DROP VIEW IF EXISTS `kcson`.`dep_has_serv` ;
USE `kcson`;
CREATE  OR REPLACE VIEW `dep_has_serv` AS 
select s.* 
from 
serv s inner join  ripso_has_serv rhs 
on rhs.serv_id=s.id
inner join dep_has_ripso dhr
on rhs.ripso_id = dhr.ripso_id

where dhr.dep_id = GET_DEP(GET_wID());

-- -----------------------------------------------------
-- View `kcson`.`main_cprice`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `kcson`.`main_cprice`;
DROP VIEW IF EXISTS `kcson`.`main_cprice` ;
USE `kcson`;
CREATE  OR REPLACE VIEW `main_cprice` AS
    SELECT 
        *,
        perc * uslnum * price AS to_pay,
        perc * uslnum * price2 AS to_pay2
    FROM
        (SELECT 
            m.*,
                (SELECT 
                        perc
                    FROM
                        add_info pd
                    WHERE
                        pddate <= m.vdate
                            AND contracts_id = m.contracts_id
                    ORDER BY pddate ASC
                    LIMIT 1) AS perc,
                price,
                price2,
                price3
                , r.servform_id
        FROM
            (main m
        INNER JOIN serv s  ON m.serv_id = s.id)
        INNER JOIN contracts c ON m.contracts_id = c.id
        left JOIN ripso r ON c.ripso_id = r.id
        
        ) f;

-- -----------------------------------------------------
-- View `kcson`.`main_NZ`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `kcson`.`main_NZ`;
DROP VIEW IF EXISTS `kcson`.`main_NZ` ;
USE `kcson`;
CREATE  OR REPLACE VIEW `main_NZ` AS select * from main where uslnum >0;

-- -----------------------------------------------------
-- View `kcson`.`dep_total_serv`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `kcson`.`dep_total_serv`;
DROP VIEW IF EXISTS `kcson`.`dep_total_serv` ;
USE `kcson`;
CREATE  OR REPLACE VIEW `dep_total_serv` AS
    SELECT 
        contracts_id,
        dep_id,
        serv_id,
        worker_id,
        SUM(uslnum),
        MONTH(vdate),
        YEAR(vdate)
    FROM
        main
    GROUP BY contracts_id , dep_id , serv_id , worker_id , MONTH(vdate) , YEAR(vdate);

-- -----------------------------------------------------
-- View `kcson`.`dep_total_supserv1`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `kcson`.`dep_total_supserv1`;
DROP VIEW IF EXISTS `kcson`.`dep_total_supserv1` ;
USE `kcson`;
CREATE  OR REPLACE VIEW `dep_total_supserv1` AS
    SELECT 
        contracts_id, dep_id,
        s.sub_serv, worker_id,
        SUM(uslnum),
        mnth1,
        year1
    FROM
        (SELECT 
            contracts_id,
                dep_id,
                serv_id,
                worker_id,
                SUM(uslnum) uslnum,
                MONTH(vdate) mnth1,
                YEAR(vdate) year1
        FROM
            main
        GROUP BY contracts_id , dep_id , serv_id , worker_id,
                MONTH(vdate) ,
                YEAR(vdate) 
        ) m
            RIGHT JOIN
        serv s ON m.serv_id = s.id
        GROUP BY
                contracts_id, dep_id,
        s.sub_serv, worker_id,
        mnth1,
        year1;

-- -----------------------------------------------------
-- View `kcson`.`max_pay_in_month_50`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `kcson`.`max_pay_in_month_50`;
DROP VIEW IF EXISTS `kcson`.`max_pay_in_month_50` ;
USE `kcson`;
CREATE  OR REPLACE VIEW `max_pay_in_month_50` AS
    SELECT 
        *, (sdd - (lm * 1.5)) / 2 AS max_pay
    FROM
        (SELECT 
            a.contracts_id,
                c.ripso_id,
                a.pddate,
                a.sdd,
				r.servform_id,
                (SELECT 
                        IF(a.work_livemin = 0, live_min_p, live_min_w) AS live_min
                    FROM
                        live_min
                    WHERE
                        a.pddate > lmdate
                    ORDER BY pddate ASC
                    LIMIT 1) AS lm
                    
        FROM
            add_info a
        INNER JOIN contracts c ON c.id = a.contracts_id
        INNER JOIN ripso r ON r.id = c.ripso_id
        WHERE
            r.servform_id IN (1 , 2, 3)) t
            
        order by  pddate;

-- -----------------------------------------------------
-- View `kcson`.`max_pay_in_month_75`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `kcson`.`max_pay_in_month_75`;
DROP VIEW IF EXISTS `kcson`.`max_pay_in_month_75` ;
USE `kcson`;
CREATE  OR REPLACE VIEW `max_pay_in_month_75` AS
    SELECT 
        *, (sdd * 0.75)  AS max_pay
    FROM
        (SELECT 
            a.contracts_id,
                c.ripso_id,
                a.pddate,
                a.sdd,
				r.servform_id,
                (SELECT 
                        IF(a.work_livemin = 0, live_min_p, live_min_w) AS live_min
                    FROM
                        live_min
                    WHERE
                        a.pddate > lmdate
                    ORDER BY pddate ASC
                    LIMIT 1) AS lm
        FROM
            add_info a
        INNER JOIN contracts c ON c.id = a.contracts_id
        INNER JOIN ripso r ON r.id = c.ripso_id
        WHERE
            r.servform_id IN (4)) t
            
        order by  pddate;

-- -----------------------------------------------------
-- View `kcson`.`max_pay_in_month`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `kcson`.`max_pay_in_month`;
DROP VIEW IF EXISTS `kcson`.`max_pay_in_month` ;
USE `kcson`;
CREATE  OR REPLACE VIEW `max_pay_in_month` AS
select * from max_pay_in_month_75
union
select * from max_pay_in_month_50;

-- -----------------------------------------------------
-- View `kcson`.`total_cprice_in_month`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `kcson`.`total_cprice_in_month`;
DROP VIEW IF EXISTS `kcson`.`total_cprice_in_month` ;
USE `kcson`;
CREATE  OR REPLACE VIEW `total_cprice_in_month` AS
    SELECT 
        contracts_id, SUM(to_pay)
    FROM
        main_cprice
    GROUP BY MONTH(vdate) , YEAR(vdate);

-- -----------------------------------------------------
-- View `kcson`.`_dep_has_ufio_ending`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `kcson`.`_dep_has_ufio_ending`;
DROP VIEW IF EXISTS `kcson`.`_dep_has_ufio_ending` ;
USE `kcson`;
CREATE  OR REPLACE VIEW `_dep_has_ufio_ending` AS

select  u.ufio, c.* from ufio u  inner join contracts c  ON  c.ufio_id = u.id
where c.enddate between CURDATE()-30 and CURDATE()+30;

-- -----------------------------------------------------
-- View `kcson`.`_dep_has_ufio_ended`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `kcson`.`_dep_has_ufio_ended`;
DROP VIEW IF EXISTS `kcson`.`_dep_has_ufio_ended` ;
USE `kcson`;
CREATE  OR REPLACE VIEW `_dep_has_ufio_ended` AS
    SELECT 
        u.ufio, c.*
    FROM
        ufio u
            INNER JOIN
        contracts c ON c.ufio_id = u.id
    WHERE
        c.enddate < CURDATE()
            AND c.dep_id = GET_DEP(GET_WID());

-- -----------------------------------------------------
-- View `kcson`.`add_info_for_ufio`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `kcson`.`add_info_for_ufio`;
DROP VIEW IF EXISTS `kcson`.`add_info_for_ufio` ;
USE `kcson`;
CREATE  OR REPLACE VIEW `add_info_for_ufio` AS
    SELECT 
        u.id AS ufio_id, a.*
    FROM
        add_info a
            INNER JOIN
        contracts c ON c.id = a.contracts_id
            INNER JOIN
        ufio u ON c.ufio_id = u.id
    ORDER BY pddate DESC
;
#TODO where  c.dep_id=GET_DEP(GET_wID());

-- -----------------------------------------------------
-- View `kcson`.`_worker_settings`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `kcson`.`_worker_settings`;
DROP VIEW IF EXISTS `kcson`.`_worker_settings` ;
USE `kcson`;
CREATE  OR REPLACE VIEW `_worker_settings` AS
select * from worker_settings
where id = GET_wID();

-- -----------------------------------------------------
-- View `kcson`.`_ufio_has_contracts`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `kcson`.`_ufio_has_contracts`;
DROP VIEW IF EXISTS `kcson`.`_ufio_has_contracts` ;
USE `kcson`;
CREATE  OR REPLACE VIEW `_ufio_has_contracts` AS
select * from contracts c
where c.ufio_id = get_last_ufio();

-- -----------------------------------------------------
-- View `kcson`.`_contr_has_serv`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `kcson`.`_contr_has_serv`;
DROP VIEW IF EXISTS `kcson`.`_contr_has_serv` ;
USE `kcson`;
CREATE  OR REPLACE VIEW `_contr_has_serv` AS
select * from  contracts_has_serv;
#where contracts_id = get_last_contr();

-- -----------------------------------------------------
-- View `kcson`.`_contr_has_add_info`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `kcson`.`_contr_has_add_info`;
DROP VIEW IF EXISTS `kcson`.`_contr_has_add_info` ;
USE `kcson`;
CREATE  OR REPLACE VIEW `_contr_has_add_info` AS
select * from  add_info
where contracts_id = get_last_contr();

-- -----------------------------------------------------
-- View `kcson`.`_ufio_has_main`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `kcson`.`_ufio_has_main`;
DROP VIEW IF EXISTS `kcson`.`_ufio_has_main` ;
USE `kcson`;
CREATE  OR REPLACE VIEW `_ufio_has_main` AS
select * from main
where ufio_id = get_last_ufio();

-- -----------------------------------------------------
-- View `kcson`.`_ufio_has_category_for_last_ufio`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `kcson`.`_ufio_has_category_for_last_ufio`;
DROP VIEW IF EXISTS `kcson`.`_ufio_has_category_for_last_ufio` ;
USE `kcson`;
CREATE  OR REPLACE VIEW `_ufio_has_category_for_last_ufio` AS
select * from ufio_has_category uhc
where uhc.ufio_id = get_last_ufio();

-- -----------------------------------------------------
-- View `kcson`.`_dep_has_ufio_by_contr`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `kcson`.`_dep_has_ufio_by_contr`;
DROP VIEW IF EXISTS `kcson`.`_dep_has_ufio_by_contr` ;
USE `kcson`;
CREATE  OR REPLACE VIEW `_dep_has_ufio_by_contr` AS
select * from ufio
where id in (
	select ufio_id from contracts c
	where  c.dep_id=GET_DEP(GET_wID())
);

-- -----------------------------------------------------
-- View `kcson`.`_dep_has_ufio`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `kcson`.`_dep_has_ufio`;
DROP VIEW IF EXISTS `kcson`.`_dep_has_ufio` ;
USE `kcson`;
CREATE  OR REPLACE VIEW `_dep_has_ufio` AS
select * from ufio
where id in (
	select ufio_id from contracts c inner join dep_has_ripso rod on rod.ripso_id = c.ripso_id
	where  
		rod.dep_id=GET_DEP(GET_wID())
    OR 
		c.dep_id = GET_DEP(GET_wID())
);

-- -----------------------------------------------------
-- View `kcson`.`__dep_has_ufio_more`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `kcson`.`__dep_has_ufio_more`;
DROP VIEW IF EXISTS `kcson`.`__dep_has_ufio_more` ;
USE `kcson`;
CREATE  OR REPLACE VIEW `__dep_has_ufio_more` AS
SELECT 
		`du`.`id` AS `id`,
        `du`.`ufio` AS `ufio`,
        `du`.`ufio_short` AS `ufio_short`,
        `du`.`ufioDeath` AS `ufioDeath`,
        `du`.`ufiobirth` AS `ufiobirth`,
        `du`.`ESRN` AS `ESRN`,
        `du`.`prim` AS `prim_fio`,
        `du`.`phone` AS `phone`,
        `du`.`snils` AS `snils`,
        `du`.`curator` AS `curator_fio`,
        `du`.`create` AS `create_fio`,
        `du`.`ts` AS `ts_fio`,
        `du`.`cr_by` AS `cr_by_fio`,
        `du`.`upd_by` AS `upd_by_fio`,
        `au`.*
FROM
    (SELECT 
        *
		FROM
			(SELECT 
			*
			FROM
				add_info_for_ufio au1
			ORDER BY au1.pddate DESC) t2
			GROUP BY t2.ufio_id) au
	INNER JOIN
    _dep_has_ufio du ON du.id = au.ufio_id
ORDER BY au.pddate DESC;

-- -----------------------------------------------------
-- View `kcson`.`_main_for_dep`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `kcson`.`_main_for_dep`;
DROP VIEW IF EXISTS `kcson`.`_main_for_dep` ;
USE `kcson`;
CREATE  OR REPLACE VIEW `_main_for_dep` AS SELECT * FROM main where  (main.dep_id = GET_DEP( GET_wID() ));

-- -----------------------------------------------------
-- View `kcson`.`_g_categ_list_ufio_for_dep_for_year`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `kcson`.`_g_categ_list_ufio_for_dep_for_year`;
DROP VIEW IF EXISTS `kcson`.`_g_categ_list_ufio_for_dep_for_year` ;
USE `kcson`;
CREATE  OR REPLACE VIEW `_g_categ_list_ufio_for_dep_for_year` AS
    SELECT 
        `uhc`.`category_id` AS `category_id`,
        `m`.`ufio_id` AS `ufio_id`,
        SUM(`m`.`uslnum`) AS `SUM(uslnum)`
    FROM
        (`main` `m`
        INNER JOIN `ufio_has_category` `uhc` ON ((`m`.`ufio_id` = `uhc`.`ufio_id`)))
    WHERE
        ((`m`.`dep_id` = GET_DEP(GET_WID()))
            AND (COALESCE(`uhc`.`archive`, 0) = 0)
            AND (COALESCE(YEAR(`uhc`.`create`), 0) < GET_YEAR(GET_WID())))
    GROUP BY category_id , ufio_id;

-- -----------------------------------------------------
-- View `kcson`.`_contr_has_main`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `kcson`.`_contr_has_main`;
DROP VIEW IF EXISTS `kcson`.`_contr_has_main` ;
USE `kcson`;
CREATE  OR REPLACE VIEW `_contr_has_main` AS

select m.* from  
main m inner join contracts c
on
m.contracts_id = c.id;

#where c.id = get_last_contr();

-- -----------------------------------------------------
-- View `kcson`.`_worker_has_main`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `kcson`.`_worker_has_main`;
DROP VIEW IF EXISTS `kcson`.`_worker_has_main` ;
USE `kcson`;
CREATE  OR REPLACE VIEW `_worker_has_main` AS
select * from main where worker_id = GET_WID();

-- -----------------------------------------------------
-- View `kcson`.`_contracts`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `kcson`.`_contracts`;
DROP VIEW IF EXISTS `kcson`.`_contracts` ;
USE `kcson`;
CREATE  OR REPLACE VIEW `_contracts` AS
select c.*, r.servform_id
from
contracts c left join ripso r
on r.id = c.ripso_id;

-- -----------------------------------------------------
-- View `kcson`.`_main_cprice`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `kcson`.`_main_cprice`;
DROP VIEW IF EXISTS `kcson`.`_main_cprice` ;
USE `kcson`;
CREATE  OR REPLACE VIEW `_main_cprice` AS
    SELECT 
        *,
        perc * uslnum * price AS to_pay,
        perc * uslnum * price2 AS to_pay2
    FROM
        (SELECT 
            m.*,
                (SELECT 
                        perc
                    FROM
                        add_info pd
                    WHERE
                        pddate <= m.vdate
                            AND contracts_id = m.contracts_id
                    ORDER BY pddate ASC
                    LIMIT 1) AS perc,
                price,
                price2,
                price3
                , r.servform_id
                , s.tnum
                , s.serv
        FROM
            (main m
        INNER JOIN serv s  ON m.serv_id = s.id)
        INNER JOIN contracts c ON m.contracts_id = c.id
        left JOIN ripso r ON c.ripso_id = r.id
        
        ) f;

-- -----------------------------------------------------
-- View `kcson`.`_user_has_main`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `kcson`.`_user_has_main`;
DROP VIEW IF EXISTS `kcson`.`_user_has_main` ;
USE `kcson`;
CREATE  OR REPLACE VIEW `_user_has_main` AS
    SELECT 
        *
    FROM
        main
    WHERE
        (main.cr_by = GET_WID()
            OR main.upd_by = GET_WID())
    ORDER BY main.ts DESC;

-- -----------------------------------------------------
-- View `kcson`.`_user_has_main_limit30`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `kcson`.`_user_has_main_limit30`;
DROP VIEW IF EXISTS `kcson`.`_user_has_main_limit30` ;
USE `kcson`;
CREATE  OR REPLACE VIEW `_user_has_main_limit30` AS
    SELECT 
        *
    FROM
        main
    WHERE
        (main.cr_by = GET_WID()
            OR main.upd_by = GET_WID())
    ORDER BY main.ts DESC
    LIMIT 30;

-- -----------------------------------------------------
-- View `kcson`.`_dep_has_worker`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `kcson`.`_dep_has_worker`;
DROP VIEW IF EXISTS `kcson`.`_dep_has_worker` ;
USE `kcson`;
CREATE  OR REPLACE VIEW `_dep_has_worker` AS
select * from
dep_has_worker dhr
where dep_id = get_dep(get_Wid());

-- -----------------------------------------------------
-- View `kcson`.`_g_serv_total_dep`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `kcson`.`_g_serv_total_dep`;
DROP VIEW IF EXISTS `kcson`.`_g_serv_total_dep` ;
USE `kcson`;
CREATE  OR REPLACE VIEW `_g_serv_total_dep` AS
    SELECT 
        m.serv_id,
        SUM(m.uslnum) AS uslnum,
        (SELECT 
                COUNT(*)
            FROM
                (SELECT 
                    ufio_id
                FROM
                    _main_for_dep mfd
                WHERE
                    m.serv_id = mfd.serv_id
                GROUP BY ufio_id) t) AS ufio_id,
        COUNT(m.ufio_id) AS records
    FROM
        _main_for_dep m
    GROUP BY m.serv_id , m.ufio_id
    ORDER BY m.serv_id;

-- -----------------------------------------------------
-- View `kcson`.`_ufio_has_invalid_contracts`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `kcson`.`_ufio_has_invalid_contracts`;
DROP VIEW IF EXISTS `kcson`.`_ufio_has_invalid_contracts` ;
USE `kcson`;
CREATE  OR REPLACE VIEW `_ufio_has_invalid_contracts` AS
    SELECT 
        u.ufio, c.*
    FROM
        ufio u
            INNER JOIN
        contracts c ON c.ufio_id = u.id
    WHERE
        c.enddate <CURDATE();

-- -----------------------------------------------------
-- View `kcson`.`_ufio_has_valid_contracts`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `kcson`.`_ufio_has_valid_contracts`;
DROP VIEW IF EXISTS `kcson`.`_ufio_has_valid_contracts` ;
USE `kcson`;
CREATE  OR REPLACE VIEW `_ufio_has_valid_contracts` AS
    SELECT 
        u.ufio, c.*
    FROM
        ufio u
            INNER JOIN
        contracts c ON c.ufio_id = u.id
    WHERE
        c.enddate >CURDATE();

-- -----------------------------------------------------
-- View `kcson`.`_dep_has_ripso`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `kcson`.`_dep_has_ripso`;
DROP VIEW IF EXISTS `kcson`.`_dep_has_ripso` ;
USE `kcson`;
CREATE  OR REPLACE VIEW `_dep_has_ripso` AS
select ripso_id, ripso from 
dep_has_ripso dhr inner join
ripso r on dhr.ripso_id=r.id
where dhr.dep_id in (get_DEP(GET_WID()));

-- -----------------------------------------------------
-- View `kcson`.`_user_has_main_today`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `kcson`.`_user_has_main_today`;
DROP VIEW IF EXISTS `kcson`.`_user_has_main_today` ;
USE `kcson`;
CREATE  OR REPLACE VIEW `_user_has_main_today` AS
    SELECT 
        *
    FROM
        main
    WHERE
        (main.cr_by = GET_WID()
            OR main.upd_by = GET_WID())
            and
        main.ts = current_date()
    ORDER BY main.ts DESC;

-- -----------------------------------------------------
-- View `kcson`.`_active_dep`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `kcson`.`_active_dep`;
DROP VIEW IF EXISTS `kcson`.`_active_dep` ;
USE `kcson`;
CREATE  OR REPLACE VIEW `_active_dep` AS
select * from dep
where IS_CUR_DEP(id)
and complex_dep_id=0
group by dep; # forbid editions;
USE `kcson`;

DELIMITER $$

USE `kcson`$$
DROP TRIGGER IF EXISTS `kcson`.`dep_AFTER_INSERT` $$
USE `kcson`$$
CREATE DEFINER = CURRENT_USER TRIGGER `kcson`.`dep_AFTER_INSERT` AFTER INSERT ON `dep` FOR EACH ROW
BEGIN
	 insert into complex_dep_has_dep (complex_dep_id, dep_id)
     values(1 , NEW.id);
END$$


USE `kcson`$$
DROP TRIGGER IF EXISTS `kcson`.`ufio_BEFORE_INSERT` $$
USE `kcson`$$
CREATE DEFINER = CURRENT_USER TRIGGER `kcson`.`ufio_BEFORE_INSERT` BEFORE INSERT ON `ufio` FOR EACH ROW
BEGIN

    set new.ufio=trim(new.ufio);
	SET  NEW.cr_by = get_wID();
	SET  NEW.upd_by = get_wID();
END$$


USE `kcson`$$
DROP TRIGGER IF EXISTS `kcson`.`ufio_AFTER_INSERT` $$
USE `kcson`$$
CREATE DEFINER = CURRENT_USER TRIGGER `kcson`.`ufio_AFTER_INSERT` AFTER INSERT ON `ufio` FOR EACH ROW
BEGIN

	if new.id > 2 then
		insert into contracts (ufio_id,dep_id,blocked,startdate,enddate)
			values (new.id, GET_DEP(GET_wID()),1,date(now()),date(now()));
		# stub contract to assign fio to department
    end if;
END$$


USE `kcson`$$
DROP TRIGGER IF EXISTS `kcson`.`ufio_BEFORE_UPDATE` $$
USE `kcson`$$
CREATE DEFINER = CURRENT_USER TRIGGER `kcson`.`ufio_BEFORE_UPDATE` BEFORE UPDATE ON `ufio` FOR EACH ROW
BEGIN
    set new.ufio=trim(new.ufio);
	SET  NEW.upd_by = get_wID();
END$$


USE `kcson`$$
DROP TRIGGER IF EXISTS `kcson`.`contracts_BEFORE_INSERT` $$
USE `kcson`$$
CREATE DEFINER = CURRENT_USER TRIGGER `kcson`.`contracts_BEFORE_INSERT` BEFORE INSERT ON `contracts` FOR EACH ROW
BEGIN

	SET  NEW.cr_by = get_wID();
	SET  NEW.upd_by = get_wID();
    
	IF (NEW.startdate IS NULL) THEN 
        SET NEW.startdate = now();
    END IF;
    
	IF (NEW.enddate IS NULL) THEN 
        SET NEW.enddate = now();
    END IF;
END$$


USE `kcson`$$
DROP TRIGGER IF EXISTS `kcson`.`contracts_AFTER_INSERT` $$
USE `kcson`$$
CREATE DEFINER = CURRENT_USER TRIGGER `kcson`.`contracts_AFTER_INSERT` AFTER INSERT ON `contracts` FOR EACH ROW
BEGIN


	insert into contracts_has_serv (serv_id, contracts_id, planned ) 
		select serv_id, NEW.id, planned 
        from ripso_has_serv
		where ripso_id = NEW.ripso_id;
END$$


USE `kcson`$$
DROP TRIGGER IF EXISTS `kcson`.`contracts_BEFORE_UPDATE` $$
USE `kcson`$$
CREATE DEFINER = CURRENT_USER TRIGGER `kcson`.`contracts_BEFORE_UPDATE` BEFORE UPDATE ON `contracts` FOR EACH ROW
BEGIN

SET  NEW.upd_by = get_wID();
    
	IF (NEW.startdate IS NULL) THEN 
        SET NEW.startdate = now();
    END IF;
    
	IF (NEW.enddate IS NULL) THEN 
        SET NEW.enddate = now();
    END IF;
END$$


USE `kcson`$$
DROP TRIGGER IF EXISTS `kcson`.`worker_AFTER_INSERT` $$
USE `kcson`$$
CREATE DEFINER = CURRENT_USER TRIGGER `kcson`.`worker_AFTER_INSERT` AFTER INSERT ON `worker` FOR EACH ROW
BEGIN
	INSERT INTO worker_settings (id) values (new.id);
END$$


USE `kcson`$$
DROP TRIGGER IF EXISTS `kcson`.`dep_has_worker_BEFORE_INSERT` $$
USE `kcson`$$
CREATE DEFINER = CURRENT_USER TRIGGER `kcson`.`dep_has_worker_BEFORE_INSERT` BEFORE INSERT ON `dep_has_worker` FOR EACH ROW
BEGIN
  if length( coalesce( new.dep_has_worker, "") ) = 0 then
	set new.dep_has_worker = (select concat( worker, " " , job, " ", dep)  
			from worker w join  job j join  dep d 
			where w.id = NEW.worker_id and j.id = NEW.job_id and  d.id = NEW.dep_id);
  end if;
END$$


USE `kcson`$$
DROP TRIGGER IF EXISTS `kcson`.`dep_has_worker_BEFORE_UPDATE` $$
USE `kcson`$$
CREATE DEFINER = CURRENT_USER TRIGGER `kcson`.`dep_has_worker_BEFORE_UPDATE` BEFORE UPDATE ON `dep_has_worker` FOR EACH ROW
BEGIN
  if length( coalesce( new.dep_has_worker, "") ) = 0 then
	set new.dep_has_worker = (select concat( worker, " " , job, " ", dep)  
						from worker w join  job j join  dep d 
						where w.id = NEW.worker_id and j.id = NEW.job_id and  d.id = NEW.dep_id);
  end if;

END$$


USE `kcson`$$
DROP TRIGGER IF EXISTS `kcson`.`main_BEFORE_INSERT` $$
USE `kcson`$$
CREATE DEFINER=`root`@`localhost` TRIGGER `main_BEFORE_INSERT` BEFORE INSERT ON `main` FOR EACH ROW BEGIN 
  declare ovdid boolean default 0;
set ovdid = (select 1  from  contracts_has_serv where
  contracts_id = new.contracts_id  and
  serv_id =  new.serv_id and
  planned  < filled +  new.uslnum);
  
	if ovdid = 1 then
		SET	 NEW.overdid = True;
	else
		SET	 NEW.overdid = False;
	end if;
    if coalesce(New.worker_id, 0) = 0 then
		set new.worker_id = (select worker_id from dep_has_worker where id = new.dep_has_worker_id );
    end if;
    
SET  NEW.cr_by = get_wID();
SET  NEW.upd_by = get_wID();
END$$


USE `kcson`$$
DROP TRIGGER IF EXISTS `kcson`.`main_AFTER_INSERT` $$
USE `kcson`$$
CREATE DEFINER=`root`@`localhost` TRIGGER `main_AFTER_INSERT` AFTER INSERT ON `main` FOR EACH ROW BEGIN

	INSERT INTO  contracts_has_serv (filled, contracts_id, serv_id)
	values
	(new.uslnum, new.contracts_id, new.serv_id)
	ON DUPLICATE KEY UPDATE  filled = filled  + new.uslnum;

END$$


USE `kcson`$$
DROP TRIGGER IF EXISTS `kcson`.`main_BEFORE_UPDATE` $$
USE `kcson`$$
CREATE DEFINER=`root`@`localhost` TRIGGER `main_BEFORE_UPDATE` BEFORE UPDATE ON `main` FOR EACH ROW BEGIN
  declare ovdid boolean default 0;
  declare wid int default 0;
   set new.serv_id=old.serv_id,
   new.contracts_id=old.contracts_id,
   new.ufio_id=old.ufio_id,
   new.dep_id=old.dep_id;
  
set ovdid = (select 1  from  contracts_has_serv where
  contracts_id = new.contracts_id  and
  serv_id =  new.serv_id and
  planned  < filled +  new.uslnum);

	if ovdid = 1 then
		SET	 NEW.overdid = True;
	else
		SET	 NEW.overdid = False;
	end if;
    
	set wid = (select worker_id from dep_has_worker where id = new.dep_has_worker_id );
    if coalesce(New.worker_id, 0) <> wid   then
		set new.worker_id = wid;
    end if;
    
    
	SET NEW.upd_by=get_wID();
END$$


USE `kcson`$$
DROP TRIGGER IF EXISTS `kcson`.`main_AFTER_UPDATE` $$
USE `kcson`$$
CREATE DEFINER=`root`@`localhost` TRIGGER `main_AFTER_UPDATE` AFTER UPDATE ON `main` FOR EACH ROW BEGIN
	UPDATE contracts_has_serv set filled=filled+new.uslnum-old.uslnum
		where contracts_id=new.contracts_id and serv_id=new.serv_id;
END$$


USE `kcson`$$
DROP TRIGGER IF EXISTS `kcson`.`main_AFTER_DELETE` $$
USE `kcson`$$
CREATE DEFINER = CURRENT_USER TRIGGER `kcson`.`main_AFTER_DELETE` AFTER DELETE ON `main` FOR EACH ROW
BEGIN
	UPDATE contracts_has_serv set fill=fill-old.uslnum
		where contracts_id=old.contracts_id and serv_id=old.serv_id;
END$$


USE `kcson`$$
DROP TRIGGER IF EXISTS `kcson`.`contracts_has_serv_BEFORE_INSERT` $$
USE `kcson`$$
CREATE DEFINER = CURRENT_USER TRIGGER `kcson`.`contracts_has_serv_BEFORE_INSERT` BEFORE INSERT ON `contracts_has_serv` FOR EACH ROW
BEGIN
	SET  NEW.cr_by = get_wID();
	SET  NEW.upd_by = get_wID();
END$$


USE `kcson`$$
DROP TRIGGER IF EXISTS `kcson`.`contracts_has_serv_BEFORE_UPDATE` $$
USE `kcson`$$
CREATE DEFINER = CURRENT_USER TRIGGER `kcson`.`contracts_has_serv_BEFORE_UPDATE` BEFORE UPDATE ON `contracts_has_serv` FOR EACH ROW
BEGIN
	SET  NEW.upd_by = get_wID();
END$$


USE `kcson`$$
DROP TRIGGER IF EXISTS `kcson`.`add_info_BEFORE_INSERT` $$
USE `kcson`$$
CREATE DEFINER = CURRENT_USER TRIGGER `kcson`.`add_info_BEFORE_INSERT` BEFORE INSERT ON `add_info` FOR EACH ROW
BEGIN

	SET  NEW.cr_by = get_wID();
	SET  NEW.upd_by = get_wID();
END$$


USE `kcson`$$
DROP TRIGGER IF EXISTS `kcson`.`add_info_AFTER_INSERT` $$
USE `kcson`$$
CREATE DEFINER = CURRENT_USER TRIGGER `kcson`.`add_info_AFTER_INSERT` AFTER INSERT ON `add_info` FOR EACH ROW
BEGIN
	declare ripso int default 0;
    DECLARE CONTINUE HANDLER FOR SQLEXCEPTION set ripso =0 ;
    set ripso = (select ripso_id from contracts where id=new.contracts_id);
    if ripso > 0 then
		insert into contracts_has_serv (serv_id, contracts_id, planned, archive)
			select serv_id, new.contracts_id, planned,0 from ripso_has_serv where ripso_id=ripso;
		# By default ippsu had all services - worker can change it later
    end if;
END$$


USE `kcson`$$
DROP TRIGGER IF EXISTS `kcson`.`add_info_BEFORE_UPDATE` $$
USE `kcson`$$
CREATE DEFINER = CURRENT_USER TRIGGER `kcson`.`add_info_BEFORE_UPDATE` BEFORE UPDATE ON `add_info` FOR EACH ROW
BEGIN

SET  NEW.upd_by = get_wID();
END$$


USE `kcson`$$
DROP TRIGGER IF EXISTS `kcson`.`invoice_BEFORE_INSERT` $$
USE `kcson`$$
CREATE DEFINER = CURRENT_USER TRIGGER `kcson`.`invoice_BEFORE_INSERT` BEFORE INSERT ON `invoice` FOR EACH ROW
BEGIN

SET  NEW.cr_by = get_wID();
SET  NEW.upd_by = get_wID();
END$$


USE `kcson`$$
DROP TRIGGER IF EXISTS `kcson`.`invoice_BEFORE_UPDATE` $$
USE `kcson`$$
CREATE DEFINER = CURRENT_USER TRIGGER `kcson`.`invoice_BEFORE_UPDATE` BEFORE UPDATE ON `invoice` FOR EACH ROW
BEGIN

SET  NEW.upd_by = get_wID(CURRENT_USER);
END$$


USE `kcson`$$
DROP TRIGGER IF EXISTS `kcson`.`invoice_has_payment_BEFORE_INSERT` $$
USE `kcson`$$
CREATE DEFINER = CURRENT_USER TRIGGER `kcson`.`invoice_has_payment_BEFORE_INSERT` BEFORE INSERT ON `invoice_has_payment` FOR EACH ROW
BEGIN
declare inv int;
declare pay int;
# check duplicates
END$$


USE `kcson`$$
DROP TRIGGER IF EXISTS `kcson`.`ufio_has_category_BEFORE_INSERT` $$
USE `kcson`$$
CREATE DEFINER = CURRENT_USER TRIGGER `kcson`.`ufio_has_category_BEFORE_INSERT` BEFORE INSERT ON `ufio_has_category` FOR EACH ROW
BEGIN
	SET  NEW.upd_by = get_wID();
	SET  NEW.cr_by = get_wID();
END$$


USE `kcson`$$
DROP TRIGGER IF EXISTS `kcson`.`ufio_has_category_BEFORE_UPDATE` $$
USE `kcson`$$
CREATE DEFINER = CURRENT_USER TRIGGER `kcson`.`ufio_has_category_BEFORE_UPDATE` BEFORE UPDATE ON `ufio_has_category` FOR EACH ROW
BEGIN

	SET  NEW.upd_by = get_wID();
END$$


DELIMITER ;

-- -----------------------------------------------------
-- Data for table `kcson`.`dep`
-- -----------------------------------------------------
START TRANSACTION;
USE `kcson`;
INSERT INTO `kcson`.`dep` (`id`, `dep`, `dep_full_name`, `dep_puname`, `note`, `archive`, `complex_dep_id`) VALUES (1, 'Не указано1', 'Не указано отделение', NULL, NULL, NULL, 0);
INSERT INTO `kcson`.`dep` (`id`, `dep`, `dep_full_name`, `dep_puname`, `note`, `archive`, `complex_dep_id`) VALUES (2, 'Не указано2', 'Не указано отделение2', NULL, NULL, NULL, 0);
INSERT INTO `kcson`.`dep` (`id`, `dep`, `dep_full_name`, `dep_puname`, `note`, `archive`, `complex_dep_id`) VALUES (3, 'Все отделения организации', NULL, NULL, NULL, NULL, 1);
INSERT INTO `kcson`.`dep` (`id`, `dep`, `dep_full_name`, `dep_puname`, `note`, `archive`, `complex_dep_id`) VALUES (4, 'СОСМОДЫ', NULL, NULL, NULL, NULL, 2);
INSERT INTO `kcson`.`dep` (`id`, `dep`, `dep_full_name`, `dep_puname`, `note`, `archive`, `complex_dep_id`) VALUES (5, 'Полустационарные отделения', NULL, NULL, NULL, NULL, 3);
INSERT INTO `kcson`.`dep` (`id`, `dep`, `dep_full_name`, `dep_puname`, `note`, `archive`, `complex_dep_id`) VALUES (6, 'Стационарные отделения', NULL, NULL, NULL, NULL, 4);
INSERT INTO `kcson`.`dep` (`id`, `dep`, `dep_full_name`, `dep_puname`, `note`, `archive`, `complex_dep_id`) VALUES (7, 'Отделения на дому', NULL, NULL, NULL, NULL, 5);
INSERT INTO `kcson`.`dep` (`id`, `dep`, `dep_full_name`, `dep_puname`, `note`, `archive`, `complex_dep_id`) VALUES (8, 'Срочные отделения', NULL, NULL, NULL, NULL, 6);

COMMIT;


-- -----------------------------------------------------
-- Data for table `kcson`.`serv`
-- -----------------------------------------------------
START TRANSACTION;
USE `kcson`;
INSERT INTO `kcson`.`serv` (`id`, `tnum`, `serv`, `year`, `sub_serv`, `sub_serv_str`, `price`, `price2`, `price3`, `archive`, `total`, `acronym`, `workload`, `content`) VALUES (1, 'Всего', 'Итого:', 2019, 0, '', 0, 0, 0, 0, 1, '', NULL, NULL);
INSERT INTO `kcson`.`serv` (`id`, `tnum`, `serv`, `year`, `sub_serv`, `sub_serv_str`, `price`, `price2`, `price3`, `archive`, `total`, `acronym`, `workload`, `content`) VALUES (2, '1', 'В форме социального обслуживания на дому', 2019, 1, 'Итог', 0, 0, 0, 0, 1, '', NULL, NULL);
INSERT INTO `kcson`.`serv` (`id`, `tnum`, `serv`, `year`, `sub_serv`, `sub_serv_str`, `price`, `price2`, `price3`, `archive`, `total`, `acronym`, `workload`, `content`) VALUES (3, '1.1', 'Социально-бытовые услуги:', 2019, 2, '1', 0, 0, 0, 0, 1, '', NULL, NULL);
INSERT INTO `kcson`.`serv` (`id`, `tnum`, `serv`, `year`, `sub_serv`, `sub_serv_str`, `price`, `price2`, `price3`, `archive`, `total`, `acronym`, `workload`, `content`) VALUES (4, '1.1.1', 'Покупка за счет средств получателя социальных услуг и доставка на дом продуктов питания___промышленных товаров первой необходимости___средств санитарии и гигиены___средств ухода', 2019, 3, '1.1', 245.29, 245.29, 0, 0, 0, '', NULL, NULL);
INSERT INTO `kcson`.`serv` (`id`, `tnum`, `serv`, `year`, `sub_serv`, `sub_serv_str`, `price`, `price2`, `price3`, `archive`, `total`, `acronym`, `workload`, `content`) VALUES (5, '1.1.2', 'Помощь в приготовлении пищи', 2019, 3, '1.1', 183.48, 183.48, 0, 0, 0, '', NULL, NULL);
INSERT INTO `kcson`.`serv` (`id`, `tnum`, `serv`, `year`, `sub_serv`, `sub_serv_str`, `price`, `price2`, `price3`, `archive`, `total`, `acronym`, `workload`, `content`) VALUES (6, '1.1.3', 'Помощь в приеме пищи (кормление)', 2019, 3, '1.1', 212.02, 212.02, 0, 0, 0, '', NULL, NULL);
INSERT INTO `kcson`.`serv` (`id`, `tnum`, `serv`, `year`, `sub_serv`, `sub_serv_str`, `price`, `price2`, `price3`, `archive`, `total`, `acronym`, `workload`, `content`) VALUES (7, '1.1.4', 'Помощь в одевании и переодевании лицам___не способным по состоянию здоровья самостоятельно осуществлять за собой уход', 2019, 3, '1.1', 191.82, 191.82, 0, 0, 0, '', NULL, NULL);
INSERT INTO `kcson`.`serv` (`id`, `tnum`, `serv`, `year`, `sub_serv`, `sub_serv_str`, `price`, `price2`, `price3`, `archive`, `total`, `acronym`, `workload`, `content`) VALUES (8, '1.1.5', 'Смена (помощь в смене) постельного белья', 2019, 3, '1.1', 89.71, 89.71, 0, 0, 0, '', NULL, NULL);
INSERT INTO `kcson`.`serv` (`id`, `tnum`, `serv`, `year`, `sub_serv`, `sub_serv_str`, `price`, `price2`, `price3`, `archive`, `total`, `acronym`, `workload`, `content`) VALUES (9, '1.1.6', 'Смена подгузников и абсорбирующего белья лицам___не способным по состоянию здоровья самостоятельно осуществлять за собой уход', 2019, 3, '1.1', 89.71, 89.71, 0, 0, 0, '', NULL, NULL);
INSERT INTO `kcson`.`serv` (`id`, `tnum`, `serv`, `year`, `sub_serv`, `sub_serv_str`, `price`, `price2`, `price3`, `archive`, `total`, `acronym`, `workload`, `content`) VALUES (10, '1.1.7', 'Предоставление гигиенических услуг лицам___не способным по состоянию здоровья самостоятельно осуществлять за собой уход', 2019, 3, '1.1', 150.87, 150.87, 0, 0, 0, '', NULL, NULL);
INSERT INTO `kcson`.`serv` (`id`, `tnum`, `serv`, `year`, `sub_serv`, `sub_serv_str`, `price`, `price2`, `price3`, `archive`, `total`, `acronym`, `workload`, `content`) VALUES (11, '1.1.8', 'Содействие за счет средств получателя социальных услуг в оказании парикмахерских услуг', 2019, 3, '1.1', 61.16, 61.16, 0, 0, 0, '', NULL, NULL);
INSERT INTO `kcson`.`serv` (`id`, `tnum`, `serv`, `year`, `sub_serv`, `sub_serv_str`, `price`, `price2`, `price3`, `archive`, `total`, `acronym`, `workload`, `content`) VALUES (12, '1.1.9', 'Сопровождение в баню (для проживающих в жилых помещениях без горячего водоснабжения)', 2019, 3, '1.1', 733.89, 733.89, 0, 0, 0, '', NULL, NULL);
INSERT INTO `kcson`.`serv` (`id`, `tnum`, `serv`, `year`, `sub_serv`, `sub_serv_str`, `price`, `price2`, `price3`, `archive`, `total`, `acronym`, `workload`, `content`) VALUES (13, '1.1.10', 'Вызов врача на дом___в том числе запись на прием к врачу', 2019, 3, '1.1', 183.48, 183.48, 0, 0, 0, '', NULL, NULL);
INSERT INTO `kcson`.`serv` (`id`, `tnum`, `serv`, `year`, `sub_serv`, `sub_serv_str`, `price`, `price2`, `price3`, `archive`, `total`, `acronym`, `workload`, `content`) VALUES (14, '1.1.11', 'Сопровождение к врачу', 2019, 3, '1.1', 733.89, 733.89, 0, 0, 0, '', NULL, NULL);
INSERT INTO `kcson`.`serv` (`id`, `tnum`, `serv`, `year`, `sub_serv`, `sub_serv_str`, `price`, `price2`, `price3`, `archive`, `total`, `acronym`, `workload`, `content`) VALUES (15, '1.1.12', 'Содействие в получении лекарственных препаратов___изделий медицинского назначения___предоставляемых в соответствии с действующим законодательством', 2019, 3, '1.1', 550.42, 550.42, 0, 0, 0, '', NULL, NULL);
INSERT INTO `kcson`.`serv` (`id`, `tnum`, `serv`, `year`, `sub_serv`, `sub_serv_str`, `price`, `price2`, `price3`, `archive`, `total`, `acronym`, `workload`, `content`) VALUES (16, '1.1.13', 'Содействие в организации санаторно-курортного лечения или оздоровительного отдыха___предоставляемого в соответствии с действующим законодательством', 2019, 3, '1.1', 460.13, 460.13, 0, 0, 0, '', NULL, NULL);
INSERT INTO `kcson`.`serv` (`id`, `tnum`, `serv`, `year`, `sub_serv`, `sub_serv_str`, `price`, `price2`, `price3`, `archive`, `total`, `acronym`, `workload`, `content`) VALUES (17, '1.1.14', 'Помощь при подготовке вещей для выезда на отдых за пределы города', 2019, 3, '1.1', 197.2, 197.2, 0, 0, 0, '', NULL, NULL);
INSERT INTO `kcson`.`serv` (`id`, `tnum`, `serv`, `year`, `sub_serv`, `sub_serv_str`, `price`, `price2`, `price3`, `archive`, `total`, `acronym`, `workload`, `content`) VALUES (18, '1.1.15', 'Сдача за счет средств получателя социальных услуг вещей в стирку___химчистку___ремонт___обратная их доставка', 2019, 3, '1.1', 150.87, 150.87, 0, 0, 0, '', NULL, NULL);
INSERT INTO `kcson`.`serv` (`id`, `tnum`, `serv`, `year`, `sub_serv`, `sub_serv_str`, `price`, `price2`, `price3`, `archive`, `total`, `acronym`, `workload`, `content`) VALUES (19, '1.1.16', 'Содействие в обеспечении топливом (для проживающих в жилых помещениях без центрального отопления)', 2019, 3, '1.1', 122.31, 122.31, 0, 0, 0, '', NULL, NULL);
INSERT INTO `kcson`.`serv` (`id`, `tnum`, `serv`, `year`, `sub_serv`, `sub_serv_str`, `price`, `price2`, `price3`, `archive`, `total`, `acronym`, `workload`, `content`) VALUES (20, '1.1.17', 'Топка печей (для проживающих в жилых помещениях без центрального отопления)', 2019, 3, '1.1', 183.48, 183.48, 0, 0, 0, '', NULL, NULL);
INSERT INTO `kcson`.`serv` (`id`, `tnum`, `serv`, `year`, `sub_serv`, `sub_serv_str`, `price`, `price2`, `price3`, `archive`, `total`, `acronym`, `workload`, `content`) VALUES (21, '1.1.18', 'Доставка воды (для проживающих в жилых помещениях без центрального водоснабжения)', 2019, 3, '1.1', 122.31, 122.31, 0, 0, 0, '', NULL, NULL);
INSERT INTO `kcson`.`serv` (`id`, `tnum`, `serv`, `year`, `sub_serv`, `sub_serv_str`, `price`, `price2`, `price3`, `archive`, `total`, `acronym`, `workload`, `content`) VALUES (22, '1.1.19', 'Организация помощи в проведении за счет средств получателя социальных услуг ремонта жилых помещений', 2019, 3, '1.1', 244.9, 244.9, 0, 0, 0, '', NULL, NULL);
INSERT INTO `kcson`.`serv` (`id`, `tnum`, `serv`, `year`, `sub_serv`, `sub_serv_str`, `price`, `price2`, `price3`, `archive`, `total`, `acronym`, `workload`, `content`) VALUES (23, '1.1.20', 'Содействие в проведении за счет средств получателя социальных услуг уборки жилых помещений___мытья окон', 2019, 3, '1.1', 122.45, 122.45, 0, 0, 0, '', NULL, NULL);
INSERT INTO `kcson`.`serv` (`id`, `tnum`, `serv`, `year`, `sub_serv`, `sub_serv_str`, `price`, `price2`, `price3`, `archive`, `total`, `acronym`, `workload`, `content`) VALUES (24, '1.1.21', 'Вынос мусора', 2019, 3, '1.1', 120.29, 120.29, 0, 0, 0, '', NULL, NULL);
INSERT INTO `kcson`.`serv` (`id`, `tnum`, `serv`, `year`, `sub_serv`, `sub_serv_str`, `price`, `price2`, `price3`, `archive`, `total`, `acronym`, `workload`, `content`) VALUES (25, '1.1.22', 'Оплата за счет средств получателя социальных услуг жилищно-коммунальных услуг и услуг связи', 2019, 3, '1.1', 183.66, 183.66, 0, 0, 0, '', NULL, NULL);
INSERT INTO `kcson`.`serv` (`id`, `tnum`, `serv`, `year`, `sub_serv`, `sub_serv_str`, `price`, `price2`, `price3`, `archive`, `total`, `acronym`, `workload`, `content`) VALUES (26, '1.1.23', 'Оформление за счет средств получателя социальных услуг подписки на газеты и журналы', 2019, 3, '1.1', 184.13, 184.13, 0, 0, 0, '', NULL, NULL);
INSERT INTO `kcson`.`serv` (`id`, `tnum`, `serv`, `year`, `sub_serv`, `sub_serv_str`, `price`, `price2`, `price3`, `archive`, `total`, `acronym`, `workload`, `content`) VALUES (27, '1.1.24', 'Отправка за счет средств получателя социальных услуг почтовой корреспонденции', 2019, 3, '1.1', 122.31, 122.31, 0, 0, 0, '', NULL, NULL);
INSERT INTO `kcson`.`serv` (`id`, `tnum`, `serv`, `year`, `sub_serv`, `sub_serv_str`, `price`, `price2`, `price3`, `archive`, `total`, `acronym`, `workload`, `content`) VALUES (28, '1.1.25', 'Обеспечение кратковременного присмотра за детьми', 2019, 3, '1.1', 733.89, 733.89, 0, 0, 0, '', NULL, NULL);
INSERT INTO `kcson`.`serv` (`id`, `tnum`, `serv`, `year`, `sub_serv`, `sub_serv_str`, `price`, `price2`, `price3`, `archive`, `total`, `acronym`, `workload`, `content`) VALUES (29, '1.1.26', 'Консультирование по вопросам оборудования специальными средствами и приспособлениями жилого помещения___занимаемого получателем социальных услуг (для инвалидов (детей-инвалидов)___имеющих стойкие расстройства опорно-двигательного аппарата___зрения___слуха___умственные отклонения)', 2019, 3, '1.1', 366.94, 366.94, 0, 0, 0, '', NULL, NULL);
INSERT INTO `kcson`.`serv` (`id`, `tnum`, `serv`, `year`, `sub_serv`, `sub_serv_str`, `price`, `price2`, `price3`, `archive`, `total`, `acronym`, `workload`, `content`) VALUES (30, '1.1.27', 'Содействие в оформлении документов и выдача напрокат технических средств реабилитации', 2019, 3, '1.1', 371.87, 371.87, 0, 0, 0, '', NULL, NULL);
INSERT INTO `kcson`.`serv` (`id`, `tnum`, `serv`, `year`, `sub_serv`, `sub_serv_str`, `price`, `price2`, `price3`, `archive`, `total`, `acronym`, `workload`, `content`) VALUES (31, '1.1.28', 'Содействие в обеспечении техническими средствами реабилитации___предоставляемыми в соответствии с действующим законодательством либо за счет средств получателя социальных услуг', 2019, 3, '1.1', 555.35, 555.35, 0, 0, 0, '', NULL, NULL);
INSERT INTO `kcson`.`serv` (`id`, `tnum`, `serv`, `year`, `sub_serv`, `sub_serv_str`, `price`, `price2`, `price3`, `archive`, `total`, `acronym`, `workload`, `content`) VALUES (32, '1.1.29', 'Оповещение родственников', 2019, 3, '1.1', 125.23, 125.23, 0, 0, 0, '', NULL, NULL);
INSERT INTO `kcson`.`serv` (`id`, `tnum`, `serv`, `year`, `sub_serv`, `sub_serv_str`, `price`, `price2`, `price3`, `archive`, `total`, `acronym`, `workload`, `content`) VALUES (33, '1.1.30', 'Организация (содействие в оказании) ритуальных услуг', 2019, 3, '1.1', 375.67, 375.67, 0, 0, 0, '', NULL, NULL);
INSERT INTO `kcson`.`serv` (`id`, `tnum`, `serv`, `year`, `sub_serv`, `sub_serv_str`, `price`, `price2`, `price3`, `archive`, `total`, `acronym`, `workload`, `content`) VALUES (34, '1.1.31', 'Консультирование по вопросам самообслуживания и социально-бытовой адаптации', 2019, 3, '1.1', 122.31, 122.31, 0, 0, 0, '', NULL, NULL);
INSERT INTO `kcson`.`serv` (`id`, `tnum`, `serv`, `year`, `sub_serv`, `sub_serv_str`, `price`, `price2`, `price3`, `archive`, `total`, `acronym`, `workload`, `content`) VALUES (35, '1.1.32', 'Предоставление лицам___нуждающимся по состоянию здоровья___специализированных услуг экстренной помощи \"тревожная кнопка\":', 2019, 3, '1.1', 0, 0, 0, 0, 1, '', NULL, NULL);
INSERT INTO `kcson`.`serv` (`id`, `tnum`, `serv`, `year`, `sub_serv`, `sub_serv_str`, `price`, `price2`, `price3`, `archive`, `total`, `acronym`, `workload`, `content`) VALUES (36, '1.1.32.1', 'монтаж___подключение___программирование функций устройства для предоставления получателю социальной услуги \"Предоставление лицам___нуждающимся по состоянию здоровья___специализированных услуг экстренной помощи \"тревожная кнопка\"', 2019, 35, '1.1.32', 362.95, 362.95, 0, 0, 0, '', NULL, NULL);
INSERT INTO `kcson`.`serv` (`id`, `tnum`, `serv`, `year`, `sub_serv`, `sub_serv_str`, `price`, `price2`, `price3`, `archive`, `total`, `acronym`, `workload`, `content`) VALUES (37, '1.1.32.2', 'обслуживание получателя социальной услуги \"Предоставление лицам___нуждающимся по состоянию здоровья___специализированных услуг экстренной помощи \"тревожная кнопка\"', 2019, 35, '1.1.32', 686.1, 686.1, 0, 0, 0, '', NULL, NULL);
INSERT INTO `kcson`.`serv` (`id`, `tnum`, `serv`, `year`, `sub_serv`, `sub_serv_str`, `price`, `price2`, `price3`, `archive`, `total`, `acronym`, `workload`, `content`) VALUES (38, '1.2', 'Социально-медицинские услуги:', 2019, 2, '1', 0, 0, 0, 0, 1, '', NULL, NULL);
INSERT INTO `kcson`.`serv` (`id`, `tnum`, `serv`, `year`, `sub_serv`, `sub_serv_str`, `price`, `price2`, `price3`, `archive`, `total`, `acronym`, `workload`, `content`) VALUES (39, '1.2.1', 'Консультирование по социально-медицинским вопросам', 2019, 38, '1.2', 127.78, 127.78, 0, 0, 0, '', NULL, NULL);
INSERT INTO `kcson`.`serv` (`id`, `tnum`, `serv`, `year`, `sub_serv`, `sub_serv_str`, `price`, `price2`, `price3`, `archive`, `total`, `acronym`, `workload`, `content`) VALUES (40, '1.2.2', 'Систематическое наблюдение за получателем социальных услуг в целях выявления отклонений в состоянии его здоровья', 2019, 38, '1.2', 175.74, 175.74, 0, 0, 0, '', NULL, NULL);
INSERT INTO `kcson`.`serv` (`id`, `tnum`, `serv`, `year`, `sub_serv`, `sub_serv_str`, `price`, `price2`, `price3`, `archive`, `total`, `acronym`, `workload`, `content`) VALUES (41, '1.2.3', 'Выполнение процедур___связанных с организацией ухода___наблюдением за состоянием здоровья получателя социальных услуг', 2019, 38, '1.2', 362.93, 362.93, 0, 0, 0, '', NULL, NULL);
INSERT INTO `kcson`.`serv` (`id`, `tnum`, `serv`, `year`, `sub_serv`, `sub_serv_str`, `price`, `price2`, `price3`, `archive`, `total`, `acronym`, `workload`, `content`) VALUES (42, '1.2.4', 'Обеспечение приема получателем социальных услуг лекарственных средств в соответствии с назначением врача', 2019, 38, '1.2', 83.27, 83.27, 0, 0, 0, '', NULL, NULL);
INSERT INTO `kcson`.`serv` (`id`, `tnum`, `serv`, `year`, `sub_serv`, `sub_serv_str`, `price`, `price2`, `price3`, `archive`, `total`, `acronym`, `workload`, `content`) VALUES (43, '1.2.5', 'Проведение мероприятий___направленных на формирование здорового образа жизни', 2019, 38, '1.2', 183.48, 183.48, 0, 0, 0, '', NULL, NULL);
INSERT INTO `kcson`.`serv` (`id`, `tnum`, `serv`, `year`, `sub_serv`, `sub_serv_str`, `price`, `price2`, `price3`, `archive`, `total`, `acronym`, `workload`, `content`) VALUES (44, '1.3', 'Социально-психологические услуги:', 2019, 2, '1', 0, 0, 0, 0, 1, '', NULL, NULL);
INSERT INTO `kcson`.`serv` (`id`, `tnum`, `serv`, `year`, `sub_serv`, `sub_serv_str`, `price`, `price2`, `price3`, `archive`, `total`, `acronym`, `workload`, `content`) VALUES (45, '1.3.1', 'Социально-психологическое консультирование (в том числе по вопросам внутрисемейных отношений)', 2019, 44, '1.3', 0, 437.1, 0, 0, 0, '', NULL, NULL);
INSERT INTO `kcson`.`serv` (`id`, `tnum`, `serv`, `year`, `sub_serv`, `sub_serv_str`, `price`, `price2`, `price3`, `archive`, `total`, `acronym`, `workload`, `content`) VALUES (46, '1.3.2', 'Социально-психологический патронаж', 2019, 44, '1.3', 0, 293.96, 0, 0, 0, '', NULL, NULL);
INSERT INTO `kcson`.`serv` (`id`, `tnum`, `serv`, `year`, `sub_serv`, `sub_serv_str`, `price`, `price2`, `price3`, `archive`, `total`, `acronym`, `workload`, `content`) VALUES (47, '1.4', 'Социально-педагогические услуги:', 2019, 2, '1', 0, 0, 0, 0, 1, '', NULL, NULL);
INSERT INTO `kcson`.`serv` (`id`, `tnum`, `serv`, `year`, `sub_serv`, `sub_serv_str`, `price`, `price2`, `price3`, `archive`, `total`, `acronym`, `workload`, `content`) VALUES (48, '1.4.1', 'Консультирование получателя социальных услуг и (или) его ближайшего окружения по вопросам социальной реабилитации', 2019, 47, '1.4', 0, 214.49, 0, 0, 0, '', NULL, NULL);
INSERT INTO `kcson`.`serv` (`id`, `tnum`, `serv`, `year`, `sub_serv`, `sub_serv_str`, `price`, `price2`, `price3`, `archive`, `total`, `acronym`, `workload`, `content`) VALUES (49, '1.4.2', 'Обучение практическим навыкам общего ухода за тяжелобольными получателями социальных услуг___получателями социальных услуг___имеющими ограничения жизнедеятельности___в том числе за детьми-инвалидами', 2019, 47, '1.4', 0, 176.21, 0, 0, 0, '', NULL, NULL);
INSERT INTO `kcson`.`serv` (`id`, `tnum`, `serv`, `year`, `sub_serv`, `sub_serv_str`, `price`, `price2`, `price3`, `archive`, `total`, `acronym`, `workload`, `content`) VALUES (50, '1.4.3', 'Чтение журналов___газет___книг', 2019, 47, '1.4', 0, 366.94, 0, 0, 0, '', NULL, NULL);
INSERT INTO `kcson`.`serv` (`id`, `tnum`, `serv`, `year`, `sub_serv`, `sub_serv_str`, `price`, `price2`, `price3`, `archive`, `total`, `acronym`, `workload`, `content`) VALUES (51, '1.5', 'Социально-трудовые услуги:', 2019, 2, '1', 0, 0, 0, 0, 1, '', NULL, NULL);
INSERT INTO `kcson`.`serv` (`id`, `tnum`, `serv`, `year`, `sub_serv`, `sub_serv_str`, `price`, `price2`, `price3`, `archive`, `total`, `acronym`, `workload`, `content`) VALUES (52, '1.5.1', 'Содействие родственникам получателя социальных услуг в нахождении работы по гибкому графику', 2019, 51, '1.5', 0, 212.6, 0, 0, 0, '', NULL, NULL);
INSERT INTO `kcson`.`serv` (`id`, `tnum`, `serv`, `year`, `sub_serv`, `sub_serv_str`, `price`, `price2`, `price3`, `archive`, `total`, `acronym`, `workload`, `content`) VALUES (53, '1.6', 'Социально-правовые услуги:', 2019, 2, '1', 0, 0, 0, 0, 1, '', NULL, NULL);
INSERT INTO `kcson`.`serv` (`id`, `tnum`, `serv`, `year`, `sub_serv`, `sub_serv_str`, `price`, `price2`, `price3`, `archive`, `total`, `acronym`, `workload`, `content`) VALUES (54, '1.6.1', 'Оказание помощи в оформлении документов и восстановлении утраченных документов получателя социальных услуг', 2019, 53, '1.6', 0, 149.17, 0, 0, 0, '', NULL, NULL);
INSERT INTO `kcson`.`serv` (`id`, `tnum`, `serv`, `year`, `sub_serv`, `sub_serv_str`, `price`, `price2`, `price3`, `archive`, `total`, `acronym`, `workload`, `content`) VALUES (55, '1.6.2', 'Содействие в получении полиса обязательного медицинского страхования', 2019, 53, '1.6', 0, 461.26, 0, 0, 0, '', NULL, NULL);
INSERT INTO `kcson`.`serv` (`id`, `tnum`, `serv`, `year`, `sub_serv`, `sub_serv_str`, `price`, `price2`, `price3`, `archive`, `total`, `acronym`, `workload`, `content`) VALUES (56, '1.6.3', 'Содействие в оформлении документов___необходимых для помещения в стационарную организацию социального обслуживания', 2019, 53, '1.6', 0, 550.42, 0, 0, 0, '', NULL, NULL);
INSERT INTO `kcson`.`serv` (`id`, `tnum`, `serv`, `year`, `sub_serv`, `sub_serv_str`, `price`, `price2`, `price3`, `archive`, `total`, `acronym`, `workload`, `content`) VALUES (57, '1.6.4', 'Содействие в восстановлении утраченного (сохранении занимаемого) жилья___наследства', 2019, 53, '1.6', 0, 435.25, 0, 0, 0, '', NULL, NULL);
INSERT INTO `kcson`.`serv` (`id`, `tnum`, `serv`, `year`, `sub_serv`, `sub_serv_str`, `price`, `price2`, `price3`, `archive`, `total`, `acronym`, `workload`, `content`) VALUES (58, '1.6.5', 'Оказание помощи в получении юридических услуг (в том числе бесплатно)', 2019, 53, '1.6', 0, 866.53, 0, 0, 0, '', NULL, NULL);
INSERT INTO `kcson`.`serv` (`id`, `tnum`, `serv`, `year`, `sub_serv`, `sub_serv_str`, `price`, `price2`, `price3`, `archive`, `total`, `acronym`, `workload`, `content`) VALUES (59, '1.6.6', 'Оказание помощи в защите прав и законных интересов получателя социальных услуг', 2019, 53, '1.6', 0, 197.23, 0, 0, 0, '', NULL, NULL);
INSERT INTO `kcson`.`serv` (`id`, `tnum`, `serv`, `year`, `sub_serv`, `sub_serv_str`, `price`, `price2`, `price3`, `archive`, `total`, `acronym`, `workload`, `content`) VALUES (60, '1.7', 'Услуги в целях повышения коммуникативного потенциала получателей социальных услуг___имеющих ограничения жизнедеятельности___в том числе детей-инвалидов:', 2019, 2, '1', 0, 0, 0, 0, 1, '', NULL, NULL);
INSERT INTO `kcson`.`serv` (`id`, `tnum`, `serv`, `year`, `sub_serv`, `sub_serv_str`, `price`, `price2`, `price3`, `archive`, `total`, `acronym`, `workload`, `content`) VALUES (61, '1.7.1', 'Консультирование по вопросам социально-средовой реабилитации', 2019, 60, '1.7', 0, 368.08, 0, 0, 0, '', NULL, NULL);
INSERT INTO `kcson`.`serv` (`id`, `tnum`, `serv`, `year`, `sub_serv`, `sub_serv_str`, `price`, `price2`, `price3`, `archive`, `total`, `acronym`, `workload`, `content`) VALUES (62, '1.7.2', 'Обучение инвалидов (детей-инвалидов) пользованию средствами ухода и техническими средствами реабилитации', 2019, 60, '1.7', 0, 230.06, 0, 0, 0, '', NULL, NULL);
INSERT INTO `kcson`.`serv` (`id`, `tnum`, `serv`, `year`, `sub_serv`, `sub_serv_str`, `price`, `price2`, `price3`, `archive`, `total`, `acronym`, `workload`, `content`) VALUES (63, '1.7.3', 'Обучение навыкам (поддержание навыков) поведения в быту и общественных местах', 2019, 60, '1.7', 0, 282.58, 0, 0, 0, '', NULL, NULL);
INSERT INTO `kcson`.`serv` (`id`, `tnum`, `serv`, `year`, `sub_serv`, `sub_serv_str`, `price`, `price2`, `price3`, `archive`, `total`, `acronym`, `workload`, `content`) VALUES (64, '2', 'В полустационарной форме социального обслуживания', 2019, 1, 'Итог', 0, 0, 0, 0, 1, '', NULL, NULL);
INSERT INTO `kcson`.`serv` (`id`, `tnum`, `serv`, `year`, `sub_serv`, `sub_serv_str`, `price`, `price2`, `price3`, `archive`, `total`, `acronym`, `workload`, `content`) VALUES (65, '2.1', 'Социально-бытовые услуги:', 2019, 64, '2', 0, 0, 0, 0, 1, '', NULL, NULL);
INSERT INTO `kcson`.`serv` (`id`, `tnum`, `serv`, `year`, `sub_serv`, `sub_serv_str`, `price`, `price2`, `price3`, `archive`, `total`, `acronym`, `workload`, `content`) VALUES (66, '2.1.1', 'Обеспечение площадью жилых помещений в соответствии с утвержденными нормативами', 2019, 65, '2.1', 190.4, 190.4, 0, 0, 0, '', NULL, NULL);
INSERT INTO `kcson`.`serv` (`id`, `tnum`, `serv`, `year`, `sub_serv`, `sub_serv_str`, `price`, `price2`, `price3`, `archive`, `total`, `acronym`, `workload`, `content`) VALUES (67, '2.1.2', 'Обеспечение мягким инвентарем (одеждой___обувью___нательным бельем и постельными принадлежностями) в соответствии с утвержденными нормативами*:', 2019, 65, '2.1', 0, 0, 0, 0, 1, '', NULL, NULL);
INSERT INTO `kcson`.`serv` (`id`, `tnum`, `serv`, `year`, `sub_serv`, `sub_serv_str`, `price`, `price2`, `price3`, `archive`, `total`, `acronym`, `workload`, `content`) VALUES (68, '2.1.2.1', 'гражданам пожилого и трудоспособного возраста без определенного места жительства (бездомным)', 2019, 67, '2.1.2', 97.09, 97.09, 0, 0, 0, '', NULL, NULL);
INSERT INTO `kcson`.`serv` (`id`, `tnum`, `serv`, `year`, `sub_serv`, `sub_serv_str`, `price`, `price2`, `price3`, `archive`, `total`, `acronym`, `workload`, `content`) VALUES (69, '2.1.3', 'Обеспечение питанием согласно утвержденным нормативам**:', 2019, 65, '2.1', 0, 0, 0, 0, 1, '', NULL, NULL);
INSERT INTO `kcson`.`serv` (`id`, `tnum`, `serv`, `year`, `sub_serv`, `sub_serv_str`, `price`, `price2`, `price3`, `archive`, `total`, `acronym`, `workload`, `content`) VALUES (70, '2.1.3.1', 'граждан пожилого возраста и инвалидов___находящихся в учреждениях социального обслуживания населения___за исключением психоневрологических интернатов', 2019, 69, '2.1.3', 382.91, 382.91, 0, 0, 0, '', NULL, NULL);
INSERT INTO `kcson`.`serv` (`id`, `tnum`, `serv`, `year`, `sub_serv`, `sub_serv_str`, `price`, `price2`, `price3`, `archive`, `total`, `acronym`, `workload`, `content`) VALUES (71, '2.1.3.2', 'граждан пожилого возраста и инвалидов при заболеваниях сахарным диабетом___находящихся в учреждениях социального обслуживания населения___за исключением психоневрологических интернатов', 2019, 69, '2.1.3', 367.87, 367.87, 0, 0, 0, '', NULL, NULL);
INSERT INTO `kcson`.`serv` (`id`, `tnum`, `serv`, `year`, `sub_serv`, `sub_serv_str`, `price`, `price2`, `price3`, `archive`, `total`, `acronym`, `workload`, `content`) VALUES (72, '2.1.3.3', 'граждан пожилого возраста и инвалидов___находящихся в учреждениях социального обслуживания населения - психоневрологических интернатах', 2019, 69, '2.1.3', 424.89, 424.89, 0, 0, 0, '', NULL, NULL);
INSERT INTO `kcson`.`serv` (`id`, `tnum`, `serv`, `year`, `sub_serv`, `sub_serv_str`, `price`, `price2`, `price3`, `archive`, `total`, `acronym`, `workload`, `content`) VALUES (73, '2.1.3.4', 'граждан пожилого возраста и инвалидов при заболеваниях сахарным диабетом___находящихся в учреждениях социального обслуживания населения - психоневрологических интернатах', 2019, 69, '2.1.3', 380.46, 380.46, 0, 0, 0, '', NULL, NULL);
INSERT INTO `kcson`.`serv` (`id`, `tnum`, `serv`, `year`, `sub_serv`, `sub_serv_str`, `price`, `price2`, `price3`, `archive`, `total`, `acronym`, `workload`, `content`) VALUES (74, '2.1.3.5', 'беременных женщин в учреждениях социального обслуживания населения', 2019, 69, '2.1.3', 391.21, 391.21, 0, 0, 0, '', NULL, NULL);
INSERT INTO `kcson`.`serv` (`id`, `tnum`, `serv`, `year`, `sub_serv`, `sub_serv_str`, `price`, `price2`, `price3`, `archive`, `total`, `acronym`, `workload`, `content`) VALUES (75, '2.1.3.6', 'кормящих матерей в учреждениях социального обслуживания населения', 2019, 69, '2.1.3', 363.84, 363.84, 0, 0, 0, '', NULL, NULL);
INSERT INTO `kcson`.`serv` (`id`, `tnum`, `serv`, `year`, `sub_serv`, `sub_serv_str`, `price`, `price2`, `price3`, `archive`, `total`, `acronym`, `workload`, `content`) VALUES (76, '2.1.3.7', 'детей первого года жизни от 0-4 мес.___проживающих с матерями - получателями социальных услуг', 2019, 69, '2.1.3', 152.93, 152.93, 0, 0, 0, '', NULL, NULL);
INSERT INTO `kcson`.`serv` (`id`, `tnum`, `serv`, `year`, `sub_serv`, `sub_serv_str`, `price`, `price2`, `price3`, `archive`, `total`, `acronym`, `workload`, `content`) VALUES (77, '2.1.3.8', 'детей первого года жизни от 4-6 мес.___проживающих с матерями - получателями социальных услуг', 2019, 69, '2.1.3', 219, 219, 0, 0, 0, '', NULL, NULL);
INSERT INTO `kcson`.`serv` (`id`, `tnum`, `serv`, `year`, `sub_serv`, `sub_serv_str`, `price`, `price2`, `price3`, `archive`, `total`, `acronym`, `workload`, `content`) VALUES (78, '2.1.3.9', 'детей первого года жизни от 6-9 мес.___проживающих с матерями - получателями социальных услуг', 2019, 69, '2.1.3', 232.71, 232.71, 0, 0, 0, '', NULL, NULL);
INSERT INTO `kcson`.`serv` (`id`, `tnum`, `serv`, `year`, `sub_serv`, `sub_serv_str`, `price`, `price2`, `price3`, `archive`, `total`, `acronym`, `workload`, `content`) VALUES (79, '2.1.3.10', 'детей первого года жизни от 9-12 мес.___проживающих с матерями - получателями социальных услуг', 2019, 69, '2.1.3', 377.56, 377.56, 0, 0, 0, '', NULL, NULL);
INSERT INTO `kcson`.`serv` (`id`, `tnum`, `serv`, `year`, `sub_serv`, `sub_serv_str`, `price`, `price2`, `price3`, `archive`, `total`, `acronym`, `workload`, `content`) VALUES (80, '2.1.3.11', 'детей в возрасте от 1 до 3 лет', 2019, 69, '2.1.3', 203.48, 203.48, 0, 0, 0, '', NULL, NULL);
INSERT INTO `kcson`.`serv` (`id`, `tnum`, `serv`, `year`, `sub_serv`, `sub_serv_str`, `price`, `price2`, `price3`, `archive`, `total`, `acronym`, `workload`, `content`) VALUES (81, '2.1.3.12', 'детей в возрасте от 3 до 7 лет', 2019, 69, '2.1.3', 354.4, 354.4, 0, 0, 0, '', NULL, NULL);
INSERT INTO `kcson`.`serv` (`id`, `tnum`, `serv`, `year`, `sub_serv`, `sub_serv_str`, `price`, `price2`, `price3`, `archive`, `total`, `acronym`, `workload`, `content`) VALUES (82, '2.1.3.13', 'детей в возрасте от 7 до 11лет', 2019, 69, '2.1.3', 417.96, 417.96, 0, 0, 0, '', NULL, NULL);
INSERT INTO `kcson`.`serv` (`id`, `tnum`, `serv`, `year`, `sub_serv`, `sub_serv_str`, `price`, `price2`, `price3`, `archive`, `total`, `acronym`, `workload`, `content`) VALUES (83, '2.1.3.14', 'детей в возрасте от 12 до 18 лет', 2019, 69, '2.1.3', 470.15, 470.15, 0, 0, 0, '', NULL, NULL);
INSERT INTO `kcson`.`serv` (`id`, `tnum`, `serv`, `year`, `sub_serv`, `sub_serv_str`, `price`, `price2`, `price3`, `archive`, `total`, `acronym`, `workload`, `content`) VALUES (84, '2.1.3.15', 'граждан без определенного места жительства (бездомных)', 2019, 69, '2.1.3', 105.06, 105.06, 0, 0, 0, '', NULL, NULL);
INSERT INTO `kcson`.`serv` (`id`, `tnum`, `serv`, `year`, `sub_serv`, `sub_serv_str`, `price`, `price2`, `price3`, `archive`, `total`, `acronym`, `workload`, `content`) VALUES (85, '2.1.4', 'Обеспечение бесплатным горячим питанием или набором продуктов:', 2019, 65, '2.1', 0, 0, 0, 0, 1, '', NULL, NULL);
INSERT INTO `kcson`.`serv` (`id`, `tnum`, `serv`, `year`, `sub_serv`, `sub_serv_str`, `price`, `price2`, `price3`, `archive`, `total`, `acronym`, `workload`, `content`) VALUES (86, '2.1.4.1', 'Обеспечение бесплатным горячим питанием', 2019, 85, '2.1.4', 196.93, 196.93, 0, 0, 0, '', NULL, NULL);
INSERT INTO `kcson`.`serv` (`id`, `tnum`, `serv`, `year`, `sub_serv`, `sub_serv_str`, `price`, `price2`, `price3`, `archive`, `total`, `acronym`, `workload`, `content`) VALUES (87, '2.1.4.2', 'Обеспечение бесплатным набором продуктов', 2019, 85, '2.1.4', 506.45, 506.45, 0, 0, 0, '', NULL, NULL);
INSERT INTO `kcson`.`serv` (`id`, `tnum`, `serv`, `year`, `sub_serv`, `sub_serv_str`, `price`, `price2`, `price3`, `archive`, `total`, `acronym`, `workload`, `content`) VALUES (88, '2.1.5', 'Помощь в одевании и переодевании лицам___не способным по состоянию здоровья самостоятельно осуществлять за собой уход', 2019, 65, '2.1', 182.81, 182.81, 0, 0, 0, '', NULL, NULL);
INSERT INTO `kcson`.`serv` (`id`, `tnum`, `serv`, `year`, `sub_serv`, `sub_serv_str`, `price`, `price2`, `price3`, `archive`, `total`, `acronym`, `workload`, `content`) VALUES (89, '2.1.6', 'Смена подгузников и абсорбирующего белья лицам___не способным по состоянию здоровья самостоятельно осуществлять за собой уход', 2019, 65, '2.1', 155.9, 155.9, 0, 0, 0, '', NULL, NULL);
INSERT INTO `kcson`.`serv` (`id`, `tnum`, `serv`, `year`, `sub_serv`, `sub_serv_str`, `price`, `price2`, `price3`, `archive`, `total`, `acronym`, `workload`, `content`) VALUES (90, '2.1.7', 'Предоставление гигиенических услуг лицам___не способным по состоянию здоровья самостоятельно осуществлять за собой уход', 2019, 65, '2.1', 130.89, 130.89, 0, 0, 0, '', NULL, NULL);
INSERT INTO `kcson`.`serv` (`id`, `tnum`, `serv`, `year`, `sub_serv`, `sub_serv_str`, `price`, `price2`, `price3`, `archive`, `total`, `acronym`, `workload`, `content`) VALUES (91, '2.1.8', 'Содействие в организации санаторно-курортного лечения или оздоровительного отдыха___предоставляемого в соответствии с действующим законодательством', 2019, 65, '2.1', 460.13, 460.13, 0, 0, 0, '', NULL, NULL);
INSERT INTO `kcson`.`serv` (`id`, `tnum`, `serv`, `year`, `sub_serv`, `sub_serv_str`, `price`, `price2`, `price3`, `archive`, `total`, `acronym`, `workload`, `content`) VALUES (92, '2.1.9', 'Отправка за счет средств получателя социальных услуг почтовой корреспонденции', 2019, 65, '2.1', 103.99, 103.99, 0, 0, 0, '', NULL, NULL);
INSERT INTO `kcson`.`serv` (`id`, `tnum`, `serv`, `year`, `sub_serv`, `sub_serv_str`, `price`, `price2`, `price3`, `archive`, `total`, `acronym`, `workload`, `content`) VALUES (93, '2.1.10', 'Обеспечение кратковременного присмотра за детьми', 2019, 65, '2.1', 613.51, 613.51, 0, 0, 0, '', NULL, NULL);
INSERT INTO `kcson`.`serv` (`id`, `tnum`, `serv`, `year`, `sub_serv`, `sub_serv_str`, `price`, `price2`, `price3`, `archive`, `total`, `acronym`, `workload`, `content`) VALUES (94, '2.1.11', 'Консультирование по вопросам оборудования специальными средствами и приспособлениями жилого помещения___занимаемого получателем социальных услуг (для инвалидов (детей-инвалидов)___имеющих стойкие расстройства опорно-двигательного аппарата___зрения___слуха___умственные отклонения)', 2019, 65, '2.1', 306.75, 306.75, 0, 0, 0, '', NULL, NULL);
INSERT INTO `kcson`.`serv` (`id`, `tnum`, `serv`, `year`, `sub_serv`, `sub_serv_str`, `price`, `price2`, `price3`, `archive`, `total`, `acronym`, `workload`, `content`) VALUES (95, '2.1.12', 'Содействие в оформлении документов и выдача напрокат технических средств реабилитации', 2019, 65, '2.1', 371.87, 371.87, 0, 0, 0, '', NULL, NULL);
INSERT INTO `kcson`.`serv` (`id`, `tnum`, `serv`, `year`, `sub_serv`, `sub_serv_str`, `price`, `price2`, `price3`, `archive`, `total`, `acronym`, `workload`, `content`) VALUES (96, '2.1.13', 'Содействие в обеспечении техническими средствами реабилитации___предоставляемыми в соответствии с действующим законодательством либо за счет средств получателя социальных услуг', 2019, 65, '2.1', 428.8, 428.8, 0, 0, 0, '', NULL, NULL);
INSERT INTO `kcson`.`serv` (`id`, `tnum`, `serv`, `year`, `sub_serv`, `sub_serv_str`, `price`, `price2`, `price3`, `archive`, `total`, `acronym`, `workload`, `content`) VALUES (97, '2.1.14', 'Консультирование по вопросам самообслуживания и социально-бытовой адаптации', 2019, 65, '2.1', 125.23, 125.23, 0, 0, 0, '', NULL, NULL);
INSERT INTO `kcson`.`serv` (`id`, `tnum`, `serv`, `year`, `sub_serv`, `sub_serv_str`, `price`, `price2`, `price3`, `archive`, `total`, `acronym`, `workload`, `content`) VALUES (98, '2.2', 'Социально-медицинские услуги:', 2019, 64, '2', 0, 0, 0, 0, 1, '', NULL, NULL);
INSERT INTO `kcson`.`serv` (`id`, `tnum`, `serv`, `year`, `sub_serv`, `sub_serv_str`, `price`, `price2`, `price3`, `archive`, `total`, `acronym`, `workload`, `content`) VALUES (99, '2.2.1', 'Консультирование по социально-медицинским вопросам', 2019, 98, '2.2', 169.64, 169.64, 0, 0, 0, '', NULL, NULL);
INSERT INTO `kcson`.`serv` (`id`, `tnum`, `serv`, `year`, `sub_serv`, `sub_serv_str`, `price`, `price2`, `price3`, `archive`, `total`, `acronym`, `workload`, `content`) VALUES (100, '2.2.2', 'Систематическое наблюдение за получателем социальных услуг в целях выявления отклонений в состоянии его здоровья', 2019, 98, '2.2', 88.43, 88.43, 0, 0, 0, '', NULL, NULL);
INSERT INTO `kcson`.`serv` (`id`, `tnum`, `serv`, `year`, `sub_serv`, `sub_serv_str`, `price`, `price2`, `price3`, `archive`, `total`, `acronym`, `workload`, `content`) VALUES (101, '2.2.3', 'Выполнение процедур___связанных с организацией ухода___наблюдением за состоянием здоровья получателя социальных услуг', 2019, 98, '2.2', 189.28, 189.28, 0, 0, 0, '', NULL, NULL);
INSERT INTO `kcson`.`serv` (`id`, `tnum`, `serv`, `year`, `sub_serv`, `sub_serv_str`, `price`, `price2`, `price3`, `archive`, `total`, `acronym`, `workload`, `content`) VALUES (102, '2.2.4', 'Обеспечение приема получателем социальных услуг лекарственных средств в соответствии с назначением врача', 2019, 98, '2.2', 83.27, 83.27, 0, 0, 0, '', NULL, NULL);
INSERT INTO `kcson`.`serv` (`id`, `tnum`, `serv`, `year`, `sub_serv`, `sub_serv_str`, `price`, `price2`, `price3`, `archive`, `total`, `acronym`, `workload`, `content`) VALUES (103, '2.2.5', 'Проведение мероприятий___направленных на формирование здорового образа жизни', 2019, 98, '2.2', 187.83, 187.83, 0, 0, 0, '', NULL, NULL);
INSERT INTO `kcson`.`serv` (`id`, `tnum`, `serv`, `year`, `sub_serv`, `sub_serv_str`, `price`, `price2`, `price3`, `archive`, `total`, `acronym`, `workload`, `content`) VALUES (104, '2.2.6', 'Проведение лечебно-оздоровительных мероприятий (в том числе с использованием реабилитационного оборудования)', 2019, 98, '2.2', 292.48, 292.48, 0, 0, 0, '', NULL, NULL);
INSERT INTO `kcson`.`serv` (`id`, `tnum`, `serv`, `year`, `sub_serv`, `sub_serv_str`, `price`, `price2`, `price3`, `archive`, `total`, `acronym`, `workload`, `content`) VALUES (105, '2.2.7', 'Проведение занятий по адаптивной физической культуре', 2019, 98, '2.2', 496.99, 496.99, 0, 0, 0, '', NULL, NULL);
INSERT INTO `kcson`.`serv` (`id`, `tnum`, `serv`, `year`, `sub_serv`, `sub_serv_str`, `price`, `price2`, `price3`, `archive`, `total`, `acronym`, `workload`, `content`) VALUES (106, '2.2.8', 'Санитарная обработка (обработка волосистых поверхностей тела дезинфицирующими растворами от педикулеза___помывка)', 2019, 98, '2.2', 293.07, 293.07, 0, 0, 0, '', NULL, NULL);
INSERT INTO `kcson`.`serv` (`id`, `tnum`, `serv`, `year`, `sub_serv`, `sub_serv_str`, `price`, `price2`, `price3`, `archive`, `total`, `acronym`, `workload`, `content`) VALUES (107, '2.3', 'Социально-психологические услуги:', 2019, 64, '2', 0, 0, 0, 0, 1, '', NULL, NULL);
INSERT INTO `kcson`.`serv` (`id`, `tnum`, `serv`, `year`, `sub_serv`, `sub_serv_str`, `price`, `price2`, `price3`, `archive`, `total`, `acronym`, `workload`, `content`) VALUES (108, '2.3.1', 'Социально-психологическое консультирование (в том числе семейное консультирование)', 2019, 107, '2.3', 0, 303.22, 0, 0, 0, '', NULL, NULL);
INSERT INTO `kcson`.`serv` (`id`, `tnum`, `serv`, `year`, `sub_serv`, `sub_serv_str`, `price`, `price2`, `price3`, `archive`, `total`, `acronym`, `workload`, `content`) VALUES (109, '2.3.2', 'Социально-психологический патронаж', 2019, 107, '2.3', 0, 418.67, 0, 0, 0, '', NULL, NULL);
INSERT INTO `kcson`.`serv` (`id`, `tnum`, `serv`, `year`, `sub_serv`, `sub_serv_str`, `price`, `price2`, `price3`, `archive`, `total`, `acronym`, `workload`, `content`) VALUES (110, '2.3.3', 'Проведение социально-психологических тренингов', 2019, 107, '2.3', 0, 72.19, 0, 0, 0, '', NULL, NULL);
INSERT INTO `kcson`.`serv` (`id`, `tnum`, `serv`, `year`, `sub_serv`, `sub_serv_str`, `price`, `price2`, `price3`, `archive`, `total`, `acronym`, `workload`, `content`) VALUES (111, '2.4', 'Социально-педагогические услуги:', 2019, 64, '2', 0, 0, 0, 0, 1, '', NULL, NULL);
INSERT INTO `kcson`.`serv` (`id`, `tnum`, `serv`, `year`, `sub_serv`, `sub_serv_str`, `price`, `price2`, `price3`, `archive`, `total`, `acronym`, `workload`, `content`) VALUES (112, '2.4.1', 'Консультирование получателя социальных услуг и (или) ближайшего окружения получателя социальных услуг по вопросам социальной реабилитации', 2019, 111, '2.4', 0, 214.49, 0, 0, 0, '', NULL, NULL);
INSERT INTO `kcson`.`serv` (`id`, `tnum`, `serv`, `year`, `sub_serv`, `sub_serv_str`, `price`, `price2`, `price3`, `archive`, `total`, `acronym`, `workload`, `content`) VALUES (113, '2.4.2', 'Социально-педагогическая коррекция___включая диагностику и консультирование', 2019, 111, '2.4', 0, 1693.08, 0, 0, 0, '', NULL, NULL);
INSERT INTO `kcson`.`serv` (`id`, `tnum`, `serv`, `year`, `sub_serv`, `sub_serv_str`, `price`, `price2`, `price3`, `archive`, `total`, `acronym`, `workload`, `content`) VALUES (114, '2.4.3', 'Социально-педагогический патронаж', 2019, 111, '2.4', 0, 411.98, 0, 0, 0, '', NULL, NULL);
INSERT INTO `kcson`.`serv` (`id`, `tnum`, `serv`, `year`, `sub_serv`, `sub_serv_str`, `price`, `price2`, `price3`, `archive`, `total`, `acronym`, `workload`, `content`) VALUES (115, '2.4.4', 'Обучение родительским функциям', 2019, 111, '2.4', 0, 598.31, 0, 0, 0, '', NULL, NULL);
INSERT INTO `kcson`.`serv` (`id`, `tnum`, `serv`, `year`, `sub_serv`, `sub_serv_str`, `price`, `price2`, `price3`, `archive`, `total`, `acronym`, `workload`, `content`) VALUES (116, '2.4.5', 'Обучение матери созданию социально-бытовой среды для развития ребенка', 2019, 111, '2.4', 0, 191.01, 0, 0, 0, '', NULL, NULL);
INSERT INTO `kcson`.`serv` (`id`, `tnum`, `serv`, `year`, `sub_serv`, `sub_serv_str`, `price`, `price2`, `price3`, `archive`, `total`, `acronym`, `workload`, `content`) VALUES (117, '2.4.6', 'Консультирование ближайшего окружения ребенка по развитию игровой и продуктивной деятельности', 2019, 111, '2.4', 0, 207.12, 0, 0, 0, '', NULL, NULL);
INSERT INTO `kcson`.`serv` (`id`, `tnum`, `serv`, `year`, `sub_serv`, `sub_serv_str`, `price`, `price2`, `price3`, `archive`, `total`, `acronym`, `workload`, `content`) VALUES (118, '2.4.7', 'Консультирование по организации учебной деятельности несовершеннолетнего в домашних условиях', 2019, 111, '2.4', 0, 207.12, 0, 0, 0, '', NULL, NULL);
INSERT INTO `kcson`.`serv` (`id`, `tnum`, `serv`, `year`, `sub_serv`, `sub_serv_str`, `price`, `price2`, `price3`, `archive`, `total`, `acronym`, `workload`, `content`) VALUES (119, '2.4.8', 'Обучение практическим навыкам общего ухода за тяжелобольными получателями социальных услуг___получателями социальных услуг___имеющими ограничения жизнедеятельности___в том числе за детьми-инвалидами', 2019, 111, '2.4', 0, 176.21, 0, 0, 0, '', NULL, NULL);
INSERT INTO `kcson`.`serv` (`id`, `tnum`, `serv`, `year`, `sub_serv`, `sub_serv_str`, `price`, `price2`, `price3`, `archive`, `total`, `acronym`, `workload`, `content`) VALUES (120, '2.4.9', 'Проведение логопедических занятий', 2019, 111, '2.4', 0, 686.15, 0, 0, 0, '', NULL, NULL);
INSERT INTO `kcson`.`serv` (`id`, `tnum`, `serv`, `year`, `sub_serv`, `sub_serv_str`, `price`, `price2`, `price3`, `archive`, `total`, `acronym`, `workload`, `content`) VALUES (121, '2.4.10', 'Организация помощи родителям и иным законным представителям детей-инвалидов___воспитываемых дома___в обучении таких детей навыкам самообслуживания___общения___направленным на развитие личности', 2019, 111, '2.4', 0, 4823.05, 0, 0, 0, '', NULL, NULL);
INSERT INTO `kcson`.`serv` (`id`, `tnum`, `serv`, `year`, `sub_serv`, `sub_serv_str`, `price`, `price2`, `price3`, `archive`, `total`, `acronym`, `workload`, `content`) VALUES (122, '2.4.11', 'Формирование позитивных интересов (в том числе в сфере досуга)', 2019, 111, '2.4', 0, 1138.4, 0, 0, 0, '', NULL, NULL);
INSERT INTO `kcson`.`serv` (`id`, `tnum`, `serv`, `year`, `sub_serv`, `sub_serv_str`, `price`, `price2`, `price3`, `archive`, `total`, `acronym`, `workload`, `content`) VALUES (123, '2.4.12', 'Проведение занятий в соответствии с разработанным индивидуальным социально-педагогическим планом (сенсорное развитие___предметно-практическая деятельность___социально-бытовая ориентация___изодеятельность___арт-терапия___игровая деятельность___музыкальные занятия___спортивные___досуговые___экскурсионные мероприятия)___в том числе групповых', 2019, 111, '2.4', 0, 66.66, 0, 0, 0, '', NULL, NULL);
INSERT INTO `kcson`.`serv` (`id`, `tnum`, `serv`, `year`, `sub_serv`, `sub_serv_str`, `price`, `price2`, `price3`, `archive`, `total`, `acronym`, `workload`, `content`) VALUES (124, '2.4.13', 'Оказание помощи в обучении навыкам компьютерной грамотности', 2019, 111, '2.4', 0, 762.43, 0, 0, 0, '', NULL, NULL);
INSERT INTO `kcson`.`serv` (`id`, `tnum`, `serv`, `year`, `sub_serv`, `sub_serv_str`, `price`, `price2`, `price3`, `archive`, `total`, `acronym`, `workload`, `content`) VALUES (125, '2.4.14', 'Организация досуга (в том числе сопровождение на социокультурные мероприятия)', 2019, 111, '2.4', 0, 43.84, 0, 0, 0, '', NULL, NULL);
INSERT INTO `kcson`.`serv` (`id`, `tnum`, `serv`, `year`, `sub_serv`, `sub_serv_str`, `price`, `price2`, `price3`, `archive`, `total`, `acronym`, `workload`, `content`) VALUES (126, '2.5', 'Социально-трудовые услуги:', 2019, 64, '2', 0, 0, 0, 0, 1, '', NULL, NULL);
INSERT INTO `kcson`.`serv` (`id`, `tnum`, `serv`, `year`, `sub_serv`, `sub_serv_str`, `price`, `price2`, `price3`, `archive`, `total`, `acronym`, `workload`, `content`) VALUES (127, '2.5.1', 'Проведение мероприятий по использованию трудовых возможностей и обучению доступным профессиональным навыкам', 2019, 126, '2.5', 0, 703.61, 0, 0, 0, '', NULL, NULL);
INSERT INTO `kcson`.`serv` (`id`, `tnum`, `serv`, `year`, `sub_serv`, `sub_serv_str`, `price`, `price2`, `price3`, `archive`, `total`, `acronym`, `workload`, `content`) VALUES (128, '2.5.2', 'Профессиональная ориентация', 2019, 126, '2.5', 0, 358.67, 0, 0, 0, '', NULL, NULL);
INSERT INTO `kcson`.`serv` (`id`, `tnum`, `serv`, `year`, `sub_serv`, `sub_serv_str`, `price`, `price2`, `price3`, `archive`, `total`, `acronym`, `workload`, `content`) VALUES (129, '2.5.3', 'Организация обучения в трудовых мастерских', 2019, 126, '2.5', 0, 125.31, 0, 0, 0, '', NULL, NULL);
INSERT INTO `kcson`.`serv` (`id`, `tnum`, `serv`, `year`, `sub_serv`, `sub_serv_str`, `price`, `price2`, `price3`, `archive`, `total`, `acronym`, `workload`, `content`) VALUES (130, '2.5.4', 'Организация помощи в получении образования___в том числе профессионального образования___инвалидами (детьми- инвалидами) в соответствии с их способностями', 2019, 126, '2.5', 0, 1291.2, 0, 0, 0, '', NULL, NULL);
INSERT INTO `kcson`.`serv` (`id`, `tnum`, `serv`, `year`, `sub_serv`, `sub_serv_str`, `price`, `price2`, `price3`, `archive`, `total`, `acronym`, `workload`, `content`) VALUES (131, '2.5.5', 'Содействие в получении образования и(или) профессии', 2019, 126, '2.5', 0, 212.6, 0, 0, 0, '', NULL, NULL);
INSERT INTO `kcson`.`serv` (`id`, `tnum`, `serv`, `year`, `sub_serv`, `sub_serv_str`, `price`, `price2`, `price3`, `archive`, `total`, `acronym`, `workload`, `content`) VALUES (132, '2.5.6', 'Оказание помощи в трудоустройстве', 2019, 126, '2.5', 0, 213.55, 0, 0, 0, '', NULL, NULL);
INSERT INTO `kcson`.`serv` (`id`, `tnum`, `serv`, `year`, `sub_serv`, `sub_serv_str`, `price`, `price2`, `price3`, `archive`, `total`, `acronym`, `workload`, `content`) VALUES (133, '2.5.7', 'Содействие родственникам получателя социальных услуг в нахождении работы по гибкому графику', 2019, 126, '2.5', 0, 212.6, 0, 0, 0, '', NULL, NULL);
INSERT INTO `kcson`.`serv` (`id`, `tnum`, `serv`, `year`, `sub_serv`, `sub_serv_str`, `price`, `price2`, `price3`, `archive`, `total`, `acronym`, `workload`, `content`) VALUES (134, '2.6', 'Социально-правовые услуги:', 2019, 64, '2', 0, 0, 0, 0, 1, '', NULL, NULL);
INSERT INTO `kcson`.`serv` (`id`, `tnum`, `serv`, `year`, `sub_serv`, `sub_serv_str`, `price`, `price2`, `price3`, `archive`, `total`, `acronym`, `workload`, `content`) VALUES (135, '2.6.1', 'Оказание помощи в оформлении документов и восстановлении утраченных документов получателя социальных услуг', 2019, 134, '2.6', 0, 149.17, 0, 0, 0, '', NULL, NULL);
INSERT INTO `kcson`.`serv` (`id`, `tnum`, `serv`, `year`, `sub_serv`, `sub_serv_str`, `price`, `price2`, `price3`, `archive`, `total`, `acronym`, `workload`, `content`) VALUES (136, '2.6.2', 'Содействие в получении полиса обязательного медицинского страхования', 2019, 134, '2.6', 0, 461.26, 0, 0, 0, '', NULL, NULL);
INSERT INTO `kcson`.`serv` (`id`, `tnum`, `serv`, `year`, `sub_serv`, `sub_serv_str`, `price`, `price2`, `price3`, `archive`, `total`, `acronym`, `workload`, `content`) VALUES (137, '2.6.3', 'Консультирование по вопросам усыновления (удочерения)', 2019, 134, '2.6', 0, 275.56, 0, 0, 0, '', NULL, NULL);
INSERT INTO `kcson`.`serv` (`id`, `tnum`, `serv`, `year`, `sub_serv`, `sub_serv_str`, `price`, `price2`, `price3`, `archive`, `total`, `acronym`, `workload`, `content`) VALUES (138, '2.6.4', 'Оформление исковых заявлений на лишение родительских прав либо восстановление в родительских правах', 2019, 134, '2.6', 0, 275.56, 0, 0, 0, '', NULL, NULL);
INSERT INTO `kcson`.`serv` (`id`, `tnum`, `serv`, `year`, `sub_serv`, `sub_serv_str`, `price`, `price2`, `price3`, `archive`, `total`, `acronym`, `workload`, `content`) VALUES (139, '2.6.5', 'Содействие в привлечении к уголовной ответственности подозреваемых в психическом и физическом насилии над получателем социальных услуг', 2019, 134, '2.6', 0, 289.12, 0, 0, 0, '', NULL, NULL);
INSERT INTO `kcson`.`serv` (`id`, `tnum`, `serv`, `year`, `sub_serv`, `sub_serv_str`, `price`, `price2`, `price3`, `archive`, `total`, `acronym`, `workload`, `content`) VALUES (140, '2.6.6', 'Содействие в оформлении документов___необходимых для помещения в стационарную организацию социального обслуживания', 2019, 134, '2.6', 0, 319.04, 0, 0, 0, '', NULL, NULL);
INSERT INTO `kcson`.`serv` (`id`, `tnum`, `serv`, `year`, `sub_serv`, `sub_serv_str`, `price`, `price2`, `price3`, `archive`, `total`, `acronym`, `workload`, `content`) VALUES (141, '2.6.7', 'Содействие в восстановлении утраченного (сохранении занимаемого) жилья___наследства', 2019, 134, '2.6', 0, 435.25, 0, 0, 0, '', NULL, NULL);
INSERT INTO `kcson`.`serv` (`id`, `tnum`, `serv`, `year`, `sub_serv`, `sub_serv_str`, `price`, `price2`, `price3`, `archive`, `total`, `acronym`, `workload`, `content`) VALUES (142, '2.6.8', 'Оказание помощи в получении юридических услуг (в том числе бесплатно)', 2019, 134, '2.6', 0, 289.59, 0, 0, 0, '', NULL, NULL);
INSERT INTO `kcson`.`serv` (`id`, `tnum`, `serv`, `year`, `sub_serv`, `sub_serv_str`, `price`, `price2`, `price3`, `archive`, `total`, `acronym`, `workload`, `content`) VALUES (143, '2.6.9', 'Оказание помощи в защите прав и законных интересов получателя социальных услуг', 2019, 134, '2.6', 0, 197.23, 0, 0, 0, '', NULL, NULL);
INSERT INTO `kcson`.`serv` (`id`, `tnum`, `serv`, `year`, `sub_serv`, `sub_serv_str`, `price`, `price2`, `price3`, `archive`, `total`, `acronym`, `workload`, `content`) VALUES (144, '2.7', 'Услуги в целях повышения коммуникативного потенциала получателей социальных услуг___имеющих ограничения жизнедеятельности___в том числе детей-инвалидов:', 2019, 64, '2', 0, 0, 0, 0, 1, '', NULL, NULL);
INSERT INTO `kcson`.`serv` (`id`, `tnum`, `serv`, `year`, `sub_serv`, `sub_serv_str`, `price`, `price2`, `price3`, `archive`, `total`, `acronym`, `workload`, `content`) VALUES (145, '2.7.1', 'Консультирование по вопросам социально-средовой реабилитации', 2019, 144, '2.7', 0, 376.81, 0, 0, 0, '', NULL, NULL);
INSERT INTO `kcson`.`serv` (`id`, `tnum`, `serv`, `year`, `sub_serv`, `sub_serv_str`, `price`, `price2`, `price3`, `archive`, `total`, `acronym`, `workload`, `content`) VALUES (146, '2.7.2', 'Обучение навыкам социально-средовой ориентации (в том числе самостоятельному передвижению___включая изучение жизненно важных маршрутов передвижения)', 2019, 144, '2.7', 0, 230.06, 0, 0, 0, '', NULL, NULL);
INSERT INTO `kcson`.`serv` (`id`, `tnum`, `serv`, `year`, `sub_serv`, `sub_serv_str`, `price`, `price2`, `price3`, `archive`, `total`, `acronym`, `workload`, `content`) VALUES (147, '2.7.3', 'Обучение инвалидов (детей-инвалидов) пользованию средствами ухода и техническими средствами реабилитации', 2019, 144, '2.7', 0, 317.9, 0, 0, 0, '', NULL, NULL);
INSERT INTO `kcson`.`serv` (`id`, `tnum`, `serv`, `year`, `sub_serv`, `sub_serv_str`, `price`, `price2`, `price3`, `archive`, `total`, `acronym`, `workload`, `content`) VALUES (148, '2.7.4', 'Обучение навыкам (поддержание навыков) поведения в быту и общественных местах', 2019, 144, '2.7', 0, 282.58, 0, 0, 0, '', NULL, NULL);
INSERT INTO `kcson`.`serv` (`id`, `tnum`, `serv`, `year`, `sub_serv`, `sub_serv_str`, `price`, `price2`, `price3`, `archive`, `total`, `acronym`, `workload`, `content`) VALUES (149, '2.7.5', 'Организация коммуникативного пространства и коммуникативных ситуаций по месту проживания (получения социальных услуг)', 2019, 144, '2.7', 0, 312.09, 0, 0, 0, '', NULL, NULL);
INSERT INTO `kcson`.`serv` (`id`, `tnum`, `serv`, `year`, `sub_serv`, `sub_serv_str`, `price`, `price2`, `price3`, `archive`, `total`, `acronym`, `workload`, `content`) VALUES (150, '3', 'В стационарной форме социального обслуживания', 2019, 1, 'Итог', 0, 0, 0, 0, 1, '', NULL, NULL);
INSERT INTO `kcson`.`serv` (`id`, `tnum`, `serv`, `year`, `sub_serv`, `sub_serv_str`, `price`, `price2`, `price3`, `archive`, `total`, `acronym`, `workload`, `content`) VALUES (151, '3.1', 'Социально-бытовые услуги:', 2019, 150, '3', 0, 0, 0, 0, 1, '', NULL, NULL);
INSERT INTO `kcson`.`serv` (`id`, `tnum`, `serv`, `year`, `sub_serv`, `sub_serv_str`, `price`, `price2`, `price3`, `archive`, `total`, `acronym`, `workload`, `content`) VALUES (152, '3.1.1', 'Обеспечение площадью жилых помещений в соответствии с утвержденными нормативами', 2019, 151, '3.1', 262.64, 262.64, 0, 0, 0, '', NULL, NULL);
INSERT INTO `kcson`.`serv` (`id`, `tnum`, `serv`, `year`, `sub_serv`, `sub_serv_str`, `price`, `price2`, `price3`, `archive`, `total`, `acronym`, `workload`, `content`) VALUES (153, '3.1.2', 'Обеспечение мягким инвентарем (одеждой___обувью___нательным бельем и постельными принадлежностями) в соответствии с утвержденными нормативами*:', 2019, 151, '3.1', 0, 0, 0, 0, 1, '', NULL, NULL);
INSERT INTO `kcson`.`serv` (`id`, `tnum`, `serv`, `year`, `sub_serv`, `sub_serv_str`, `price`, `price2`, `price3`, `archive`, `total`, `acronym`, `workload`, `content`) VALUES (154, '3.1.2.1', 'гражданам пожилого возраста___гражданам трудоспособного возраста и инвалидов трудоспособного возраста', 2019, 153, '3.1.2', 133.26, 133.26, 0, 0, 0, '', NULL, NULL);
INSERT INTO `kcson`.`serv` (`id`, `tnum`, `serv`, `year`, `sub_serv`, `sub_serv_str`, `price`, `price2`, `price3`, `archive`, `total`, `acronym`, `workload`, `content`) VALUES (155, '3.1.2.2', 'гражданам пожилого возраста и инвалидам трудоспособного возраста___проживающим в отделениях милосердия', 2019, 153, '3.1.2', 133.26, 133.26, 0, 0, 0, '', NULL, NULL);
INSERT INTO `kcson`.`serv` (`id`, `tnum`, `serv`, `year`, `sub_serv`, `sub_serv_str`, `price`, `price2`, `price3`, `archive`, `total`, `acronym`, `workload`, `content`) VALUES (156, '3.1.2.3', 'детям-инвалидам___детям-сиротам и детям___оставшимся без попечения родителей___несовершеннолетним___находящимся в сложной жизненной ситуации школьного возраста', 2019, 153, '3.1.2', 113.49, 113.49, 0, 0, 0, '', NULL, NULL);
INSERT INTO `kcson`.`serv` (`id`, `tnum`, `serv`, `year`, `sub_serv`, `sub_serv_str`, `price`, `price2`, `price3`, `archive`, `total`, `acronym`, `workload`, `content`) VALUES (157, '3.1.2.4', 'детям-инвалидам___детям-сиротам и детям___оставшимся без попечения родителей___несовершеннолетним___находящимся в сложной жизненной ситуации дошкольного возраста', 2019, 153, '3.1.2', 113.49, 113.49, 0, 0, 0, '', NULL, NULL);
INSERT INTO `kcson`.`serv` (`id`, `tnum`, `serv`, `year`, `sub_serv`, `sub_serv_str`, `price`, `price2`, `price3`, `archive`, `total`, `acronym`, `workload`, `content`) VALUES (158, '3.1.2.5', 'детям-инвалидам___детям-сиротам и детям___оставшимся без попечения родителей___несовершеннолетним___находящимся в сложной жизненной ситуации___проживающим в отделениях милосердия школьного возраста', 2019, 153, '3.1.2', 113.49, 113.49, 0, 0, 0, '', NULL, NULL);
INSERT INTO `kcson`.`serv` (`id`, `tnum`, `serv`, `year`, `sub_serv`, `sub_serv_str`, `price`, `price2`, `price3`, `archive`, `total`, `acronym`, `workload`, `content`) VALUES (159, '3.1.2.6', 'детям-инвалидам___детям-сиротам и детям___оставшимся без попечения родителей___несовершеннолетним___находящимся в сложной жизненной ситуации___проживающим в отделениях милосердия дошкольного возраста', 2019, 153, '3.1.2', 113.49, 113.49, 0, 0, 0, '', NULL, NULL);
INSERT INTO `kcson`.`serv` (`id`, `tnum`, `serv`, `year`, `sub_serv`, `sub_serv_str`, `price`, `price2`, `price3`, `archive`, `total`, `acronym`, `workload`, `content`) VALUES (160, '3.1.2.7', 'женщинам___находящимся в трудной жизненной ситуации или социально опасном положении___в том числе несовершеннолетним беременным', 2019, 153, '3.1.2', 95.84, 95.84, 0, 0, 0, '', NULL, NULL);
INSERT INTO `kcson`.`serv` (`id`, `tnum`, `serv`, `year`, `sub_serv`, `sub_serv_str`, `price`, `price2`, `price3`, `archive`, `total`, `acronym`, `workload`, `content`) VALUES (161, '3.1.2.8', 'женщинам с детьми в возрасте до трех лет___находящимся в трудной жизненной ситуации или социально опасном положении___в том числе несовершеннолетним матерям с младенцами', 2019, 153, '3.1.2', 95.84, 95.84, 0, 0, 0, '', NULL, NULL);
INSERT INTO `kcson`.`serv` (`id`, `tnum`, `serv`, `year`, `sub_serv`, `sub_serv_str`, `price`, `price2`, `price3`, `archive`, `total`, `acronym`, `workload`, `content`) VALUES (162, '3.1.2.9', 'женщинам с детьми старше трех лет___находящимся в трудной жизненной ситуации или социально опасном положении', 2019, 153, '3.1.2', 95.84, 95.84, 0, 0, 0, '', NULL, NULL);
INSERT INTO `kcson`.`serv` (`id`, `tnum`, `serv`, `year`, `sub_serv`, `sub_serv_str`, `price`, `price2`, `price3`, `archive`, `total`, `acronym`, `workload`, `content`) VALUES (163, '3.1.3', 'Обеспечение питанием согласно утвержденным нормативам:', 2019, 151, '3.1', 0, 0, 0, 0, 1, '', NULL, NULL);
INSERT INTO `kcson`.`serv` (`id`, `tnum`, `serv`, `year`, `sub_serv`, `sub_serv_str`, `price`, `price2`, `price3`, `archive`, `total`, `acronym`, `workload`, `content`) VALUES (164, '3.1.3.1', 'граждан пожилого возраста и инвалидов___находящихся в учреждениях социального обслуживания населения___за исключением психоневрологических интернатов', 2019, 163, '3.1.3', 395.5, 395.5, 0, 0, 0, '', NULL, NULL);
INSERT INTO `kcson`.`serv` (`id`, `tnum`, `serv`, `year`, `sub_serv`, `sub_serv_str`, `price`, `price2`, `price3`, `archive`, `total`, `acronym`, `workload`, `content`) VALUES (165, '3.1.3.2', 'граждан пожилого возраста и инвалидов при заболеваниях сахарным диабетом___находящихся в учреждениях социального обслуживания населения___за исключением психоневрологических интернатов', 2019, 163, '3.1.3', 380.46, 380.46, 0, 0, 0, '', NULL, NULL);
INSERT INTO `kcson`.`serv` (`id`, `tnum`, `serv`, `year`, `sub_serv`, `sub_serv_str`, `price`, `price2`, `price3`, `archive`, `total`, `acronym`, `workload`, `content`) VALUES (166, '3.1.3.3', 'граждан пожилого возраста и инвалидов___находящихся в учреждениях социального обслуживания населения - психоневрологических интернатах', 2019, 163, '3.1.3', 424.89, 424.89, 0, 0, 0, '', NULL, NULL);
INSERT INTO `kcson`.`serv` (`id`, `tnum`, `serv`, `year`, `sub_serv`, `sub_serv_str`, `price`, `price2`, `price3`, `archive`, `total`, `acronym`, `workload`, `content`) VALUES (167, '3.1.3.4', 'граждан пожилого возраста и инвалидов при заболеваниях сахарным диабетом___находящихся в учреждениях социального обслуживания населения - психоневрологических интернатах', 2019, 163, '3.1.3', 380.46, 380.46, 0, 0, 0, '', NULL, NULL);
INSERT INTO `kcson`.`serv` (`id`, `tnum`, `serv`, `year`, `sub_serv`, `sub_serv_str`, `price`, `price2`, `price3`, `archive`, `total`, `acronym`, `workload`, `content`) VALUES (168, '3.1.3.5', 'беременных женщин в учреждениях социального обслуживания населения', 2019, 163, '3.1.3', 396.81, 396.81, 0, 0, 0, '', NULL, NULL);
INSERT INTO `kcson`.`serv` (`id`, `tnum`, `serv`, `year`, `sub_serv`, `sub_serv_str`, `price`, `price2`, `price3`, `archive`, `total`, `acronym`, `workload`, `content`) VALUES (169, '3.1.3.6', 'кормящих матерей в учреждениях социального обслуживания населения', 2019, 163, '3.1.3', 369.43, 369.43, 0, 0, 0, '', NULL, NULL);
INSERT INTO `kcson`.`serv` (`id`, `tnum`, `serv`, `year`, `sub_serv`, `sub_serv_str`, `price`, `price2`, `price3`, `archive`, `total`, `acronym`, `workload`, `content`) VALUES (170, '3.1.3.7', 'детей первого года жизни от 0-4 мес.___проживающих с матерями - получателями социальных услуг', 2019, 163, '3.1.3', 158.61, 158.61, 0, 0, 0, '', NULL, NULL);
INSERT INTO `kcson`.`serv` (`id`, `tnum`, `serv`, `year`, `sub_serv`, `sub_serv_str`, `price`, `price2`, `price3`, `archive`, `total`, `acronym`, `workload`, `content`) VALUES (171, '3.1.3.8', 'детей первого года жизни от 4-6 мес.___проживающих с матерями - получателями социальных услуг', 2019, 163, '3.1.3', 224.59, 224.59, 0, 0, 0, '', NULL, NULL);
INSERT INTO `kcson`.`serv` (`id`, `tnum`, `serv`, `year`, `sub_serv`, `sub_serv_str`, `price`, `price2`, `price3`, `archive`, `total`, `acronym`, `workload`, `content`) VALUES (172, '3.1.3.9', 'детей первого года жизни от 6-9 мес.___проживающих с матерями - получателями социальных услуг', 2019, 163, '3.1.3', 238.31, 238.31, 0, 0, 0, '', NULL, NULL);
INSERT INTO `kcson`.`serv` (`id`, `tnum`, `serv`, `year`, `sub_serv`, `sub_serv_str`, `price`, `price2`, `price3`, `archive`, `total`, `acronym`, `workload`, `content`) VALUES (173, '3.1.3.10', 'детей первого года жизни от 9-12 мес.___проживающих с матерями - получателями социальных услуг', 2019, 163, '3.1.3', 383.15, 383.15, 0, 0, 0, '', NULL, NULL);
INSERT INTO `kcson`.`serv` (`id`, `tnum`, `serv`, `year`, `sub_serv`, `sub_serv_str`, `price`, `price2`, `price3`, `archive`, `total`, `acronym`, `workload`, `content`) VALUES (174, '3.1.3.11', 'детей в возрасте от 1 до 3 лет', 2019, 163, '3.1.3', 209.07, 209.07, 0, 0, 0, '', NULL, NULL);
INSERT INTO `kcson`.`serv` (`id`, `tnum`, `serv`, `year`, `sub_serv`, `sub_serv_str`, `price`, `price2`, `price3`, `archive`, `total`, `acronym`, `workload`, `content`) VALUES (175, '3.1.3.12', 'детей в возрасте от 3 до 7 лет', 2019, 163, '3.1.3', 360, 360, 0, 0, 0, '', NULL, NULL);
INSERT INTO `kcson`.`serv` (`id`, `tnum`, `serv`, `year`, `sub_serv`, `sub_serv_str`, `price`, `price2`, `price3`, `archive`, `total`, `acronym`, `workload`, `content`) VALUES (176, '3.1.3.13', 'детей в возрасте от 7 до 11лет', 2019, 163, '3.1.3', 423.57, 423.57, 0, 0, 0, '', NULL, NULL);
INSERT INTO `kcson`.`serv` (`id`, `tnum`, `serv`, `year`, `sub_serv`, `sub_serv_str`, `price`, `price2`, `price3`, `archive`, `total`, `acronym`, `workload`, `content`) VALUES (177, '3.1.3.14', 'детей в возрасте от 12 до 18 лет', 2019, 163, '3.1.3', 475.75, 475.75, 0, 0, 0, '', NULL, NULL);
INSERT INTO `kcson`.`serv` (`id`, `tnum`, `serv`, `year`, `sub_serv`, `sub_serv_str`, `price`, `price2`, `price3`, `archive`, `total`, `acronym`, `workload`, `content`) VALUES (178, '3.1.3.15', 'детей в возрасте от 4 до 18 лет специализированным лечебным сбалансированным энтеральным питанием в организациях социального обслуживания населения:', 2019, 163, '3.1.3', 0, 0, 0, 0, 1, '', NULL, NULL);
INSERT INTO `kcson`.`serv` (`id`, `tnum`, `serv`, `year`, `sub_serv`, `sub_serv_str`, `price`, `price2`, `price3`, `archive`, `total`, `acronym`, `workload`, `content`) VALUES (179, '3.1.3.15.1', 'находящихся на длительном зондовом питании***', 2019, 178, '3.1.3.15', 19.46, 19.46, 0, 0, 0, '', NULL, NULL);
INSERT INTO `kcson`.`serv` (`id`, `tnum`, `serv`, `year`, `sub_serv`, `sub_serv_str`, `price`, `price2`, `price3`, `archive`, `total`, `acronym`, `workload`, `content`) VALUES (180, '3.1.3.15.2', 'по медицинским показаниям нуждающихся в сухой адаптированной молочной смеси специального назначения (антирефлюкс)', 2019, 178, '3.1.3.15', 287.67, 287.67, 0, 0, 0, '', NULL, NULL);
INSERT INTO `kcson`.`serv` (`id`, `tnum`, `serv`, `year`, `sub_serv`, `sub_serv_str`, `price`, `price2`, `price3`, `archive`, `total`, `acronym`, `workload`, `content`) VALUES (181, '3.1.3.17', 'граждан трудоспособного возраста', 2019, 163, '3.1.3', 7266.55, 7266.55, 0, 0, 0, '', NULL, NULL);
INSERT INTO `kcson`.`serv` (`id`, `tnum`, `serv`, `year`, `sub_serv`, `sub_serv_str`, `price`, `price2`, `price3`, `archive`, `total`, `acronym`, `workload`, `content`) VALUES (182, '3.1.4', 'Помощь в приеме пищи (кормление)', 2019, 151, '3.1', 209.16, 209.16, 0, 0, 0, '', NULL, NULL);
INSERT INTO `kcson`.`serv` (`id`, `tnum`, `serv`, `year`, `sub_serv`, `sub_serv_str`, `price`, `price2`, `price3`, `archive`, `total`, `acronym`, `workload`, `content`) VALUES (183, '3.1.5', 'Помощь в одевании и переодевании лицам___не способным по состоянию здоровья самостоятельно осуществлять за собой уход', 2019, 151, '3.1', 277.66, 277.66, 0, 0, 0, '', NULL, NULL);
INSERT INTO `kcson`.`serv` (`id`, `tnum`, `serv`, `year`, `sub_serv`, `sub_serv_str`, `price`, `price2`, `price3`, `archive`, `total`, `acronym`, `workload`, `content`) VALUES (184, '3.1.6', 'Смена подгузников и абсорбирующего белья лицам___не способным по состоянию здоровья самостоятельно осуществлять за собой уход', 2019, 151, '3.1', 136.56, 136.56, 0, 0, 0, '', NULL, NULL);
INSERT INTO `kcson`.`serv` (`id`, `tnum`, `serv`, `year`, `sub_serv`, `sub_serv_str`, `price`, `price2`, `price3`, `archive`, `total`, `acronym`, `workload`, `content`) VALUES (185, '3.1.7', 'Предоставление гигиенических услуг лицам___не способным по состоянию здоровья самостоятельно осуществлять за собой уход', 2019, 151, '3.1', 136.25, 136.25, 0, 0, 0, '', NULL, NULL);
INSERT INTO `kcson`.`serv` (`id`, `tnum`, `serv`, `year`, `sub_serv`, `sub_serv_str`, `price`, `price2`, `price3`, `archive`, `total`, `acronym`, `workload`, `content`) VALUES (186, '3.1.8', 'Сопровождение в туалет или высаживание на судно лиц___не способных по состоянию здоровья самостоятельно осуществлять за собой уход', 2019, 151, '3.1', 75.74, 75.74, 0, 0, 0, '', NULL, NULL);
INSERT INTO `kcson`.`serv` (`id`, `tnum`, `serv`, `year`, `sub_serv`, `sub_serv_str`, `price`, `price2`, `price3`, `archive`, `total`, `acronym`, `workload`, `content`) VALUES (187, '3.1.9', 'Мытье (помощь в мытье) лиц___не способных по состоянию здоровья самостоятельно осуществлять за собой уход', 2019, 151, '3.1', 155.44, 155.44, 0, 0, 0, '', NULL, NULL);
INSERT INTO `kcson`.`serv` (`id`, `tnum`, `serv`, `year`, `sub_serv`, `sub_serv_str`, `price`, `price2`, `price3`, `archive`, `total`, `acronym`, `workload`, `content`) VALUES (188, '3.1.10', 'Бритье (помощь в бритье) бороды и усов лицам___не способным по состоянию здоровья самостоятельно осуществлять за собой уход', 2019, 151, '3.1', 71.4, 71.4, 0, 0, 0, '', NULL, NULL);
INSERT INTO `kcson`.`serv` (`id`, `tnum`, `serv`, `year`, `sub_serv`, `sub_serv_str`, `price`, `price2`, `price3`, `archive`, `total`, `acronym`, `workload`, `content`) VALUES (189, '3.1.11', 'Стрижка волос', 2019, 151, '3.1', 155.01, 155.01, 0, 0, 0, '', NULL, NULL);
INSERT INTO `kcson`.`serv` (`id`, `tnum`, `serv`, `year`, `sub_serv`, `sub_serv_str`, `price`, `price2`, `price3`, `archive`, `total`, `acronym`, `workload`, `content`) VALUES (190, '3.1.12', 'Сопровождение на прогулках', 2019, 151, '3.1', 820.33, 820.33, 0, 0, 0, '', NULL, NULL);
INSERT INTO `kcson`.`serv` (`id`, `tnum`, `serv`, `year`, `sub_serv`, `sub_serv_str`, `price`, `price2`, `price3`, `archive`, `total`, `acronym`, `workload`, `content`) VALUES (191, '3.1.13', 'Обеспечение за счет средств получателя социальных услуг книгами___журналами___газетами___настольными играми', 2019, 151, '3.1', 239.46, 239.46, 0, 0, 0, '', NULL, NULL);
INSERT INTO `kcson`.`serv` (`id`, `tnum`, `serv`, `year`, `sub_serv`, `sub_serv_str`, `price`, `price2`, `price3`, `archive`, `total`, `acronym`, `workload`, `content`) VALUES (192, '3.1.14', 'Отправка за счет средств получателя социальных услуг почтовой корреспонденции', 2019, 151, '3.1', 121.14, 121.14, 0, 0, 0, '', NULL, NULL);
INSERT INTO `kcson`.`serv` (`id`, `tnum`, `serv`, `year`, `sub_serv`, `sub_serv_str`, `price`, `price2`, `price3`, `archive`, `total`, `acronym`, `workload`, `content`) VALUES (193, '3.1.15', 'Создание условий (оказание помощи) молодым матерям по уходу за детьми младенческого возраста', 2019, 151, '3.1', 239.9, 239.9, 0, 0, 0, '', NULL, NULL);
INSERT INTO `kcson`.`serv` (`id`, `tnum`, `serv`, `year`, `sub_serv`, `sub_serv_str`, `price`, `price2`, `price3`, `archive`, `total`, `acronym`, `workload`, `content`) VALUES (194, '3.1.16', 'Содействие в получении лекарственных препаратов___изделий медицинского назначения___предоставляемых в соответствии с действующим законодательством', 2019, 151, '3.1', 716.39, 716.39, 0, 0, 0, '', NULL, NULL);
INSERT INTO `kcson`.`serv` (`id`, `tnum`, `serv`, `year`, `sub_serv`, `sub_serv_str`, `price`, `price2`, `price3`, `archive`, `total`, `acronym`, `workload`, `content`) VALUES (195, '3.1.17', 'Содействие в организации санаторно-курортного лечения или оздоровительного отдыха___предоставляемого в соответствии с действующим законодательством', 2019, 151, '3.1', 638.51, 638.51, 0, 0, 0, '', NULL, NULL);
INSERT INTO `kcson`.`serv` (`id`, `tnum`, `serv`, `year`, `sub_serv`, `sub_serv_str`, `price`, `price2`, `price3`, `archive`, `total`, `acronym`, `workload`, `content`) VALUES (196, '3.1.18', 'Помощь при подготовке вещей для выезда на отдых за пределы города', 2019, 151, '3.1', 207.21, 207.21, 0, 0, 0, '', NULL, NULL);
INSERT INTO `kcson`.`serv` (`id`, `tnum`, `serv`, `year`, `sub_serv`, `sub_serv_str`, `price`, `price2`, `price3`, `archive`, `total`, `acronym`, `workload`, `content`) VALUES (197, '3.1.19', 'Сдача за счет средств получателя социальных услуг вещей в стирку___химчистку___ремонт___обратная их доставка', 2019, 151, '3.1', 144.39, 144.39, 0, 0, 0, '', NULL, NULL);
INSERT INTO `kcson`.`serv` (`id`, `tnum`, `serv`, `year`, `sub_serv`, `sub_serv_str`, `price`, `price2`, `price3`, `archive`, `total`, `acronym`, `workload`, `content`) VALUES (198, '3.1.20', 'Содействие в обеспечении техническими средствами реабилитации___предоставляемыми в соответствии с действующим законодательством либо за счет средств получателя социальных услуг', 2019, 151, '3.1', 363.12, 363.12, 0, 0, 0, '', NULL, NULL);
INSERT INTO `kcson`.`serv` (`id`, `tnum`, `serv`, `year`, `sub_serv`, `sub_serv_str`, `price`, `price2`, `price3`, `archive`, `total`, `acronym`, `workload`, `content`) VALUES (199, '3.1.21', 'Оповещение родственников', 2019, 151, '3.1', 173.39, 173.39, 0, 0, 0, '', NULL, NULL);
INSERT INTO `kcson`.`serv` (`id`, `tnum`, `serv`, `year`, `sub_serv`, `sub_serv_str`, `price`, `price2`, `price3`, `archive`, `total`, `acronym`, `workload`, `content`) VALUES (200, '3.1.22', 'Организация (содействие в оказании) ритуальных услуг', 2019, 151, '3.1', 520.17, 520.17, 0, 0, 0, '', NULL, NULL);
INSERT INTO `kcson`.`serv` (`id`, `tnum`, `serv`, `year`, `sub_serv`, `sub_serv_str`, `price`, `price2`, `price3`, `archive`, `total`, `acronym`, `workload`, `content`) VALUES (201, '3.1.23', 'Консультирование по вопросам самообслуживания и социально-бытовой адаптации', 2019, 151, '3.1', 173.39, 173.39, 0, 0, 0, '', NULL, NULL);
INSERT INTO `kcson`.`serv` (`id`, `tnum`, `serv`, `year`, `sub_serv`, `sub_serv_str`, `price`, `price2`, `price3`, `archive`, `total`, `acronym`, `workload`, `content`) VALUES (202, '3.2', 'Социально-медицинские услуги:', 2019, 150, '3', 0, 0, 0, 0, 1, '', NULL, NULL);
INSERT INTO `kcson`.`serv` (`id`, `tnum`, `serv`, `year`, `sub_serv`, `sub_serv_str`, `price`, `price2`, `price3`, `archive`, `total`, `acronym`, `workload`, `content`) VALUES (203, '3.2.1', 'Консультирование по социально-медицинским вопросам', 2019, 202, '3.2', 175.94, 175.94, 0, 0, 0, '', NULL, NULL);
INSERT INTO `kcson`.`serv` (`id`, `tnum`, `serv`, `year`, `sub_serv`, `sub_serv_str`, `price`, `price2`, `price3`, `archive`, `total`, `acronym`, `workload`, `content`) VALUES (204, '3.2.2', 'Систематическое наблюдение за получателем социальных услуг в целях выявления отклонений в состоянии его здоровья', 2019, 202, '3.2', 395.48, 395.48, 0, 0, 0, '', NULL, NULL);
INSERT INTO `kcson`.`serv` (`id`, `tnum`, `serv`, `year`, `sub_serv`, `sub_serv_str`, `price`, `price2`, `price3`, `archive`, `total`, `acronym`, `workload`, `content`) VALUES (205, '3.2.3', 'Выполнение процедур___связанных с организацией ухода___наблюдением за состоянием здоровья получателя социальных услуг', 2019, 202, '3.2', 491.88, 491.88, 0, 0, 0, '', NULL, NULL);
INSERT INTO `kcson`.`serv` (`id`, `tnum`, `serv`, `year`, `sub_serv`, `sub_serv_str`, `price`, `price2`, `price3`, `archive`, `total`, `acronym`, `workload`, `content`) VALUES (206, '3.2.4', 'Обеспечение приема получателем социальных услуг лекарственных средств в соответствии с назначением врача', 2019, 202, '3.2', 78.87, 78.87, 0, 0, 0, '', NULL, NULL);
INSERT INTO `kcson`.`serv` (`id`, `tnum`, `serv`, `year`, `sub_serv`, `sub_serv_str`, `price`, `price2`, `price3`, `archive`, `total`, `acronym`, `workload`, `content`) VALUES (207, '3.2.5', 'Содействие в получении медицинской помощи в соответствии с действующим законодательством', 2019, 202, '3.2', 738.13, 738.13, 0, 0, 0, '', NULL, NULL);
INSERT INTO `kcson`.`serv` (`id`, `tnum`, `serv`, `year`, `sub_serv`, `sub_serv_str`, `price`, `price2`, `price3`, `archive`, `total`, `acronym`, `workload`, `content`) VALUES (208, '3.2.6', 'Проведение мероприятий___направленных на формирование здорового образа жизни', 2019, 202, '3.2', 390.13, 390.13, 0, 0, 0, '', NULL, NULL);
INSERT INTO `kcson`.`serv` (`id`, `tnum`, `serv`, `year`, `sub_serv`, `sub_serv_str`, `price`, `price2`, `price3`, `archive`, `total`, `acronym`, `workload`, `content`) VALUES (209, '3.2.7', 'Проведение лечебно-оздоровительных мероприятий (в том числе с использованием реабилитационного оборудования)', 2019, 202, '3.2', 341.91, 341.91, 0, 0, 0, '', NULL, NULL);
INSERT INTO `kcson`.`serv` (`id`, `tnum`, `serv`, `year`, `sub_serv`, `sub_serv_str`, `price`, `price2`, `price3`, `archive`, `total`, `acronym`, `workload`, `content`) VALUES (210, '3.2.8', 'Проведение занятий по адаптивной физической культуре', 2019, 202, '3.2', 342.25, 342.25, 0, 0, 0, '', NULL, NULL);
INSERT INTO `kcson`.`serv` (`id`, `tnum`, `serv`, `year`, `sub_serv`, `sub_serv_str`, `price`, `price2`, `price3`, `archive`, `total`, `acronym`, `workload`, `content`) VALUES (211, '3.2.9', 'Санитарная обработка (обработка волосистых поверхностей тела дезинфицирующими растворами от педикулеза___помывка)', 2019, 202, '3.2', 360.14, 360.14, 0, 0, 0, '', NULL, NULL);
INSERT INTO `kcson`.`serv` (`id`, `tnum`, `serv`, `year`, `sub_serv`, `sub_serv_str`, `price`, `price2`, `price3`, `archive`, `total`, `acronym`, `workload`, `content`) VALUES (212, '3.3', 'Социально-психологические услуги:', 2019, 150, '3', 0, 0, 0, 0, 1, '', NULL, NULL);
INSERT INTO `kcson`.`serv` (`id`, `tnum`, `serv`, `year`, `sub_serv`, `sub_serv_str`, `price`, `price2`, `price3`, `archive`, `total`, `acronym`, `workload`, `content`) VALUES (213, '3.3.1', 'Социально-психологическое консультирование (в том числе семейное консультирование)', 2019, 212, '3.3', 0, 564.72, 0, 0, 0, '', NULL, NULL);
INSERT INTO `kcson`.`serv` (`id`, `tnum`, `serv`, `year`, `sub_serv`, `sub_serv_str`, `price`, `price2`, `price3`, `archive`, `total`, `acronym`, `workload`, `content`) VALUES (214, '3.3.2', 'Социально-психологический патронаж', 2019, 212, '3.3', 0, 554.43, 0, 0, 0, '', NULL, NULL);
INSERT INTO `kcson`.`serv` (`id`, `tnum`, `serv`, `year`, `sub_serv`, `sub_serv_str`, `price`, `price2`, `price3`, `archive`, `total`, `acronym`, `workload`, `content`) VALUES (215, '3.3.3', 'Проведение социально-психологических тренингов', 2019, 212, '3.3', 0, 65.28, 0, 0, 0, '', NULL, NULL);
INSERT INTO `kcson`.`serv` (`id`, `tnum`, `serv`, `year`, `sub_serv`, `sub_serv_str`, `price`, `price2`, `price3`, `archive`, `total`, `acronym`, `workload`, `content`) VALUES (216, '3.4', 'Социально-педагогические услуги:', 2019, 150, '3', 0, 0, 0, 0, 1, '', NULL, NULL);
INSERT INTO `kcson`.`serv` (`id`, `tnum`, `serv`, `year`, `sub_serv`, `sub_serv_str`, `price`, `price2`, `price3`, `archive`, `total`, `acronym`, `workload`, `content`) VALUES (217, '3.4.1', 'Консультирование получателя социальных услуг и(или) ближайшего окружения получателя социальных услуг по вопросам социальной реабилитации', 2019, 216, '3.4', 0, 215.17, 0, 0, 0, '', NULL, NULL);
INSERT INTO `kcson`.`serv` (`id`, `tnum`, `serv`, `year`, `sub_serv`, `sub_serv_str`, `price`, `price2`, `price3`, `archive`, `total`, `acronym`, `workload`, `content`) VALUES (218, '3.4.2', 'Социально-педагогическая коррекция___включая диагностику и консультирование', 2019, 216, '3.4', 0, 1125.8, 0, 0, 0, '', NULL, NULL);
INSERT INTO `kcson`.`serv` (`id`, `tnum`, `serv`, `year`, `sub_serv`, `sub_serv_str`, `price`, `price2`, `price3`, `archive`, `total`, `acronym`, `workload`, `content`) VALUES (219, '3.4.3', 'Социально-педагогический патронаж', 2019, 216, '3.4', 0, 708.95, 0, 0, 0, '', NULL, NULL);
INSERT INTO `kcson`.`serv` (`id`, `tnum`, `serv`, `year`, `sub_serv`, `sub_serv_str`, `price`, `price2`, `price3`, `archive`, `total`, `acronym`, `workload`, `content`) VALUES (220, '3.4.4', 'Обучение родительским функциям', 2019, 216, '3.4', 0, 598.31, 0, 0, 0, '', NULL, NULL);
INSERT INTO `kcson`.`serv` (`id`, `tnum`, `serv`, `year`, `sub_serv`, `sub_serv_str`, `price`, `price2`, `price3`, `archive`, `total`, `acronym`, `workload`, `content`) VALUES (221, '3.4.5', 'Обучение матери созданию социально-бытовой среды для развития ребенка', 2019, 216, '3.4', 0, 285.71, 0, 0, 0, '', NULL, NULL);
INSERT INTO `kcson`.`serv` (`id`, `tnum`, `serv`, `year`, `sub_serv`, `sub_serv_str`, `price`, `price2`, `price3`, `archive`, `total`, `acronym`, `workload`, `content`) VALUES (222, '3.4.6', 'Консультирование ближайшего окружения ребенка по развитию игровой и продуктивной деятельности', 2019, 216, '3.4', 0, 213.75, 0, 0, 0, '', NULL, NULL);
INSERT INTO `kcson`.`serv` (`id`, `tnum`, `serv`, `year`, `sub_serv`, `sub_serv_str`, `price`, `price2`, `price3`, `archive`, `total`, `acronym`, `workload`, `content`) VALUES (223, '3.4.7', 'Консультирование по организации учебной деятельности несовершеннолетнего в домашних условиях', 2019, 216, '3.4', 0, 207.12, 0, 0, 0, '', NULL, NULL);
INSERT INTO `kcson`.`serv` (`id`, `tnum`, `serv`, `year`, `sub_serv`, `sub_serv_str`, `price`, `price2`, `price3`, `archive`, `total`, `acronym`, `workload`, `content`) VALUES (224, '3.4.8', 'Занятия по подготовке к жизни в семье', 2019, 216, '3.4', 0, 186.94, 0, 0, 0, '', NULL, NULL);
INSERT INTO `kcson`.`serv` (`id`, `tnum`, `serv`, `year`, `sub_serv`, `sub_serv_str`, `price`, `price2`, `price3`, `archive`, `total`, `acronym`, `workload`, `content`) VALUES (225, '3.4.9', 'Проведение логопедических занятий', 2019, 216, '3.4', 0, 670.11, 0, 0, 0, '', NULL, NULL);
INSERT INTO `kcson`.`serv` (`id`, `tnum`, `serv`, `year`, `sub_serv`, `sub_serv_str`, `price`, `price2`, `price3`, `archive`, `total`, `acronym`, `workload`, `content`) VALUES (226, '3.4.10', 'Формирование позитивных интересов (в том числе в сфере досуга)', 2019, 216, '3.4', 0, 1059.01, 0, 0, 0, '', NULL, NULL);
INSERT INTO `kcson`.`serv` (`id`, `tnum`, `serv`, `year`, `sub_serv`, `sub_serv_str`, `price`, `price2`, `price3`, `archive`, `total`, `acronym`, `workload`, `content`) VALUES (227, '3.4.11', 'Проведение занятий в соответствии с разработанным индивидуальным социально-педагогическим планом (сенсорное развитие___предметно-практическая деятельность___социально-бытовая ориентация___изодеятельность___арт- терапия___игровая деятельность___музыкальные занятия___спортивные___досуговые___экскурсионные мероприятия)___в том числе групповых', 2019, 216, '3.4', 0, 64.27, 0, 0, 0, '', NULL, NULL);
INSERT INTO `kcson`.`serv` (`id`, `tnum`, `serv`, `year`, `sub_serv`, `sub_serv_str`, `price`, `price2`, `price3`, `archive`, `total`, `acronym`, `workload`, `content`) VALUES (228, '3.4.12', 'Оказание помощи в обучении навыкам компьютерной грамотности', 2019, 216, '3.4', 0, 142.56, 0, 0, 0, '', NULL, NULL);
INSERT INTO `kcson`.`serv` (`id`, `tnum`, `serv`, `year`, `sub_serv`, `sub_serv_str`, `price`, `price2`, `price3`, `archive`, `total`, `acronym`, `workload`, `content`) VALUES (229, '3.4.13', 'Организация досуга (в том числе сопровождение на социокультурные мероприятия)', 2019, 216, '3.4', 0, 113.35, 0, 0, 0, '', NULL, NULL);
INSERT INTO `kcson`.`serv` (`id`, `tnum`, `serv`, `year`, `sub_serv`, `sub_serv_str`, `price`, `price2`, `price3`, `archive`, `total`, `acronym`, `workload`, `content`) VALUES (230, '3.4.14', 'Организация летнего отдыха', 2019, 216, '3.4', 0, 940.19, 0, 0, 0, '', NULL, NULL);
INSERT INTO `kcson`.`serv` (`id`, `tnum`, `serv`, `year`, `sub_serv`, `sub_serv_str`, `price`, `price2`, `price3`, `archive`, `total`, `acronym`, `workload`, `content`) VALUES (231, '3.4.15', 'Чтение журналов___газет___книг', 2019, 216, '3.4', 0, 546.88, 0, 0, 0, '', NULL, NULL);
INSERT INTO `kcson`.`serv` (`id`, `tnum`, `serv`, `year`, `sub_serv`, `sub_serv_str`, `price`, `price2`, `price3`, `archive`, `total`, `acronym`, `workload`, `content`) VALUES (232, '3.5', 'Социально-трудовые услуги:', 2019, 150, '3', 0, 0, 0, 0, 1, '', NULL, NULL);
INSERT INTO `kcson`.`serv` (`id`, `tnum`, `serv`, `year`, `sub_serv`, `sub_serv_str`, `price`, `price2`, `price3`, `archive`, `total`, `acronym`, `workload`, `content`) VALUES (233, '3.5.1', 'Проведение мероприятий по использованию трудовых возможностей и обучению доступным профессиональным навыкам', 2019, 232, '3.5', 0, 671.2, 0, 0, 0, '', NULL, NULL);
INSERT INTO `kcson`.`serv` (`id`, `tnum`, `serv`, `year`, `sub_serv`, `sub_serv_str`, `price`, `price2`, `price3`, `archive`, `total`, `acronym`, `workload`, `content`) VALUES (234, '3.5.2', 'Профессиональная ориентация', 2019, 232, '3.5', 0, 426.84, 0, 0, 0, '', NULL, NULL);
INSERT INTO `kcson`.`serv` (`id`, `tnum`, `serv`, `year`, `sub_serv`, `sub_serv_str`, `price`, `price2`, `price3`, `archive`, `total`, `acronym`, `workload`, `content`) VALUES (235, '3.5.3', 'Организация обучения в трудовых мастерских', 2019, 232, '3.5', 0, 89.46, 0, 0, 0, '', NULL, NULL);
INSERT INTO `kcson`.`serv` (`id`, `tnum`, `serv`, `year`, `sub_serv`, `sub_serv_str`, `price`, `price2`, `price3`, `archive`, `total`, `acronym`, `workload`, `content`) VALUES (236, '3.5.4', 'Организация помощи в получении образования___в том числе профессионального образования___инвалидами (детьми- инвалидами) в соответствии с их способностями', 2019, 232, '3.5', 0, 1582.05, 0, 0, 0, '', NULL, NULL);
INSERT INTO `kcson`.`serv` (`id`, `tnum`, `serv`, `year`, `sub_serv`, `sub_serv_str`, `price`, `price2`, `price3`, `archive`, `total`, `acronym`, `workload`, `content`) VALUES (237, '3.5.5', 'Содействие в получении образования и(или) профессии', 2019, 232, '3.5', 0, 425.89, 0, 0, 0, '', NULL, NULL);
INSERT INTO `kcson`.`serv` (`id`, `tnum`, `serv`, `year`, `sub_serv`, `sub_serv_str`, `price`, `price2`, `price3`, `archive`, `total`, `acronym`, `workload`, `content`) VALUES (238, '3.5.6', 'Оказание помощи в трудоустройстве', 2019, 232, '3.5', 0, 180.71, 0, 0, 0, '', NULL, NULL);
INSERT INTO `kcson`.`serv` (`id`, `tnum`, `serv`, `year`, `sub_serv`, `sub_serv_str`, `price`, `price2`, `price3`, `archive`, `total`, `acronym`, `workload`, `content`) VALUES (239, '3.6', 'Социально-правовые услуги:', 2019, 150, '3', 0, 0, 0, 0, 1, '', NULL, NULL);
INSERT INTO `kcson`.`serv` (`id`, `tnum`, `serv`, `year`, `sub_serv`, `sub_serv_str`, `price`, `price2`, `price3`, `archive`, `total`, `acronym`, `workload`, `content`) VALUES (240, '3.6.1', 'Оказание помощи в оформлении документов и восстановлении утраченных документов получателя социальных услуг', 2019, 239, '3.6', 0, 184.26, 0, 0, 0, '', NULL, NULL);
INSERT INTO `kcson`.`serv` (`id`, `tnum`, `serv`, `year`, `sub_serv`, `sub_serv_str`, `price`, `price2`, `price3`, `archive`, `total`, `acronym`, `workload`, `content`) VALUES (241, '3.6.2', 'Содействие в получении полиса обязательного медицинского страхования', 2019, 239, '3.6', 0, 538.43, 0, 0, 0, '', NULL, NULL);
INSERT INTO `kcson`.`serv` (`id`, `tnum`, `serv`, `year`, `sub_serv`, `sub_serv_str`, `price`, `price2`, `price3`, `archive`, `total`, `acronym`, `workload`, `content`) VALUES (242, '3.6.3', 'Консультирование по вопросам усыновления (удочерения)', 2019, 239, '3.6', 0, 275.56, 0, 0, 0, '', NULL, NULL);
INSERT INTO `kcson`.`serv` (`id`, `tnum`, `serv`, `year`, `sub_serv`, `sub_serv_str`, `price`, `price2`, `price3`, `archive`, `total`, `acronym`, `workload`, `content`) VALUES (243, '3.6.4', 'Проведение переговоров и консультаций в интересах получателя социальных услуг', 2019, 239, '3.6', 0, 180.47, 0, 0, 0, '', NULL, NULL);
INSERT INTO `kcson`.`serv` (`id`, `tnum`, `serv`, `year`, `sub_serv`, `sub_serv_str`, `price`, `price2`, `price3`, `archive`, `total`, `acronym`, `workload`, `content`) VALUES (244, '3.6.5', 'Оформление исковых заявлений на лишение родительских прав либо восстановление в родительских правах', 2019, 239, '3.6', 0, 275.56, 0, 0, 0, '', NULL, NULL);
INSERT INTO `kcson`.`serv` (`id`, `tnum`, `serv`, `year`, `sub_serv`, `sub_serv_str`, `price`, `price2`, `price3`, `archive`, `total`, `acronym`, `workload`, `content`) VALUES (245, '3.6.6', 'Содействие в привлечении к уголовной ответственности подозреваемых в психическом и физическом насилии над получателем социальных услуг', 2019, 239, '3.6', 0, 359.33, 0, 0, 0, '', NULL, NULL);
INSERT INTO `kcson`.`serv` (`id`, `tnum`, `serv`, `year`, `sub_serv`, `sub_serv_str`, `price`, `price2`, `price3`, `archive`, `total`, `acronym`, `workload`, `content`) VALUES (246, '3.6.7', 'Содействие в оформлении документов___необходимых для помещения в стационарную организацию социального обслуживания', 2019, 239, '3.6', 0, 359.33, 0, 0, 0, '', NULL, NULL);
INSERT INTO `kcson`.`serv` (`id`, `tnum`, `serv`, `year`, `sub_serv`, `sub_serv_str`, `price`, `price2`, `price3`, `archive`, `total`, `acronym`, `workload`, `content`) VALUES (247, '3.6.8', 'Подготовка документов в государственные или муниципальные органы___организации и(или) суды', 2019, 239, '3.6', 0, 359.33, 0, 0, 0, '', NULL, NULL);
INSERT INTO `kcson`.`serv` (`id`, `tnum`, `serv`, `year`, `sub_serv`, `sub_serv_str`, `price`, `price2`, `price3`, `archive`, `total`, `acronym`, `workload`, `content`) VALUES (248, '3.6.9', 'Контроль соблюдения имущественных прав получателя социальных услуг', 2019, 239, '3.6', 0, 183.8, 0, 0, 0, '', NULL, NULL);
INSERT INTO `kcson`.`serv` (`id`, `tnum`, `serv`, `year`, `sub_serv`, `sub_serv_str`, `price`, `price2`, `price3`, `archive`, `total`, `acronym`, `workload`, `content`) VALUES (249, '3.6.10', 'Оформление сберегательных вкладов', 2019, 239, '3.6', 0, 179.76, 0, 0, 0, '', NULL, NULL);
INSERT INTO `kcson`.`serv` (`id`, `tnum`, `serv`, `year`, `sub_serv`, `sub_serv_str`, `price`, `price2`, `price3`, `archive`, `total`, `acronym`, `workload`, `content`) VALUES (250, '3.6.11', 'Содействие в восстановлении утраченного (сохранении занимаемого) жилья___наследства', 2019, 239, '3.6', 0, 540.57, 0, 0, 0, '', NULL, NULL);
INSERT INTO `kcson`.`serv` (`id`, `tnum`, `serv`, `year`, `sub_serv`, `sub_serv_str`, `price`, `price2`, `price3`, `archive`, `total`, `acronym`, `workload`, `content`) VALUES (251, '3.6.12', 'Оказание помощи в получении юридических услуг (в том числе бесплатно)', 2019, 239, '3.6', 0, 359.81, 0, 0, 0, '', NULL, NULL);
INSERT INTO `kcson`.`serv` (`id`, `tnum`, `serv`, `year`, `sub_serv`, `sub_serv_str`, `price`, `price2`, `price3`, `archive`, `total`, `acronym`, `workload`, `content`) VALUES (252, '3.6.13', 'Оказание помощи в защите прав и законных интересов получателя социальных услуг', 2019, 239, '3.6', 0, 244.05, 0, 0, 0, '', NULL, NULL);
INSERT INTO `kcson`.`serv` (`id`, `tnum`, `serv`, `year`, `sub_serv`, `sub_serv_str`, `price`, `price2`, `price3`, `archive`, `total`, `acronym`, `workload`, `content`) VALUES (253, '3.7', 'Услуги в целях повышения коммуникативного потенциала получателей социальных услуг___имеющих ограничения жизнедеятельности___в том числе детей-инвалидов:', 2019, 150, '3', 0, 0, 0, 0, 1, '', NULL, NULL);
INSERT INTO `kcson`.`serv` (`id`, `tnum`, `serv`, `year`, `sub_serv`, `sub_serv_str`, `price`, `price2`, `price3`, `archive`, `total`, `acronym`, `workload`, `content`) VALUES (254, '3.7.1', 'Консультирование по вопросам социально-средовой реабилитации', 2019, 253, '3.7', 0, 426.37, 0, 0, 0, '', NULL, NULL);
INSERT INTO `kcson`.`serv` (`id`, `tnum`, `serv`, `year`, `sub_serv`, `sub_serv_str`, `price`, `price2`, `price3`, `archive`, `total`, `acronym`, `workload`, `content`) VALUES (255, '3.7.2', 'Обучение навыкам социально-средовой ориентации (в том числе самостоятельному передвижению___включая изучение жизненно важных маршрутов передвижения)', 2019, 253, '3.7', 0, 268.65, 0, 0, 0, '', NULL, NULL);
INSERT INTO `kcson`.`serv` (`id`, `tnum`, `serv`, `year`, `sub_serv`, `sub_serv_str`, `price`, `price2`, `price3`, `archive`, `total`, `acronym`, `workload`, `content`) VALUES (256, '3.7.3', 'Обучение инвалидов (детей-инвалидов) пользованию средствами ухода и техническими средствами реабилитации', 2019, 253, '3.7', 0, 268.65, 0, 0, 0, '', NULL, NULL);
INSERT INTO `kcson`.`serv` (`id`, `tnum`, `serv`, `year`, `sub_serv`, `sub_serv_str`, `price`, `price2`, `price3`, `archive`, `total`, `acronym`, `workload`, `content`) VALUES (257, '3.7.4', 'Обучение навыкам (поддержание навыков) поведения в быту и общественных местах', 2019, 253, '3.7', 0, 238.79, 0, 0, 0, '', NULL, NULL);
INSERT INTO `kcson`.`serv` (`id`, `tnum`, `serv`, `year`, `sub_serv`, `sub_serv_str`, `price`, `price2`, `price3`, `archive`, `total`, `acronym`, `workload`, `content`) VALUES (258, '3.7.5', 'Организация коммуникативного пространства и коммуникативных ситуаций по месту проживания (получения социальных услуг)', 2019, 253, '3.7', 0, 276.03, 0, 0, 0, '', NULL, NULL);
INSERT INTO `kcson`.`serv` (`id`, `tnum`, `serv`, `year`, `sub_serv`, `sub_serv_str`, `price`, `price2`, `price3`, `archive`, `total`, `acronym`, `workload`, `content`) VALUES (259, '4', 'Срочные социальные услуги', 2019, 1, 'Итог', 0, 0, 0, 0, 1, '', NULL, NULL);
INSERT INTO `kcson`.`serv` (`id`, `tnum`, `serv`, `year`, `sub_serv`, `sub_serv_str`, `price`, `price2`, `price3`, `archive`, `total`, `acronym`, `workload`, `content`) VALUES (260, '4.1', 'Консультирование по вопросам социального обслуживания', 2019, 259, '4', 0, 135.26, 0, 0, 0, '', NULL, NULL);
INSERT INTO `kcson`.`serv` (`id`, `tnum`, `serv`, `year`, `sub_serv`, `sub_serv_str`, `price`, `price2`, `price3`, `archive`, `total`, `acronym`, `workload`, `content`) VALUES (261, '4.2', 'Обеспечение бесплатным горячим питанием или набором продуктов:', 2019, 259, '4', 0, 0, 0, 0, 1, '', NULL, NULL);
INSERT INTO `kcson`.`serv` (`id`, `tnum`, `serv`, `year`, `sub_serv`, `sub_serv_str`, `price`, `price2`, `price3`, `archive`, `total`, `acronym`, `workload`, `content`) VALUES (262, '4.2.1', 'обеспечение бесплатным горячим питанием граждан пожилого возраста и инвалидов', 2019, 261, '4.2', 0, 153.75, 0, 0, 0, '', NULL, NULL);
INSERT INTO `kcson`.`serv` (`id`, `tnum`, `serv`, `year`, `sub_serv`, `sub_serv_str`, `price`, `price2`, `price3`, `archive`, `total`, `acronym`, `workload`, `content`) VALUES (263, '4.2.2', 'обеспечение набором продуктов граждан пожилого возраста и инвалидов', 2019, 261, '4.2', 0, 655.41, 0, 0, 0, '', NULL, NULL);
INSERT INTO `kcson`.`serv` (`id`, `tnum`, `serv`, `year`, `sub_serv`, `sub_serv_str`, `price`, `price2`, `price3`, `archive`, `total`, `acronym`, `workload`, `content`) VALUES (264, '4.2.3', 'обеспечение набором продуктов семей с детьми', 2019, 261, '4.2', 0, 660.94, 0, 0, 0, '', NULL, NULL);
INSERT INTO `kcson`.`serv` (`id`, `tnum`, `serv`, `year`, `sub_serv`, `sub_serv_str`, `price`, `price2`, `price3`, `archive`, `total`, `acronym`, `workload`, `content`) VALUES (265, '4.3', 'Обеспечение одеждой___обувью и другими предметами первой необходимости', 2019, 259, '4', 0, 7377.42, 0, 0, 0, '', NULL, NULL);
INSERT INTO `kcson`.`serv` (`id`, `tnum`, `serv`, `year`, `sub_serv`, `sub_serv_str`, `price`, `price2`, `price3`, `archive`, `total`, `acronym`, `workload`, `content`) VALUES (266, '4.4', 'Содействие в получении юридической помощи в целях защиты прав и законных интересов получателей социальных услуг', 2019, 259, '4', 0, 127.2, 0, 0, 0, '', NULL, NULL);
INSERT INTO `kcson`.`serv` (`id`, `tnum`, `serv`, `year`, `sub_serv`, `sub_serv_str`, `price`, `price2`, `price3`, `archive`, `total`, `acronym`, `workload`, `content`) VALUES (267, '4.5', 'Содействие в получении временного жилого помещения', 2019, 259, '4', 0, 257.15, 0, 0, 0, '', NULL, NULL);
INSERT INTO `kcson`.`serv` (`id`, `tnum`, `serv`, `year`, `sub_serv`, `sub_serv_str`, `price`, `price2`, `price3`, `archive`, `total`, `acronym`, `workload`, `content`) VALUES (268, '4.6', 'Содействие в получении экстренной психологической помощи с привлечением к этой работе психологов и священнослужителей', 2019, 259, '4', 0, 270.52, 0, 0, 0, '', NULL, NULL);
INSERT INTO `kcson`.`serv` (`id`, `tnum`, `serv`, `year`, `sub_serv`, `sub_serv_str`, `price`, `price2`, `price3`, `archive`, `total`, `acronym`, `workload`, `content`) VALUES (269, '4.7', 'Оказание консультационной психологической помощи___в том числе анонимно с использованием телефона доверия', 2019, 259, '4', 0, 129.09, 0, 0, 0, '', NULL, NULL);

COMMIT;


-- -----------------------------------------------------
-- Data for table `kcson`.`ufio`
-- -----------------------------------------------------
START TRANSACTION;
USE `kcson`;
INSERT INTO `kcson`.`ufio` (`id`, `ufio`, `ufio_short`, `ufioDeath`, `ufiobirth`, `ESRN`, `prim`, `phone`, `snils`, `curator`, `create`, `ts`, `cr_by`, `upd_by`) VALUES (1, 'Тестовый человек', 'Тx', NULL, NULL, 123, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL);
INSERT INTO `kcson`.`ufio` (`id`, `ufio`, `ufio_short`, `ufioDeath`, `ufiobirth`, `ESRN`, `prim`, `phone`, `snils`, `curator`, `create`, `ts`, `cr_by`, `upd_by`) VALUES (2, 'Тестовый чел2', NULL, NULL, NULL, 543, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL);

COMMIT;


-- -----------------------------------------------------
-- Data for table `kcson`.`servform`
-- -----------------------------------------------------
START TRANSACTION;
USE `kcson`;
INSERT INTO `kcson`.`servform` (`id`, `servform`, `prim`) VALUES (1, 'Социальное обслуживание на дому', NULL);
INSERT INTO `kcson`.`servform` (`id`, `servform`, `prim`) VALUES (2, 'Полустационарная форма социального обслуживания с периодом пребывания до четырех часов', NULL);
INSERT INTO `kcson`.`servform` (`id`, `servform`, `prim`) VALUES (3, 'Полустационарная форма социального обслуживания с периодом пребывания свыше четырех часов', NULL);
INSERT INTO `kcson`.`servform` (`id`, `servform`, `prim`) VALUES (4, 'Стационарная форма социального обслуживания при временном проживании', NULL);

COMMIT;


-- -----------------------------------------------------
-- Data for table `kcson`.`pcat`
-- -----------------------------------------------------
START TRANSACTION;
USE `kcson`;
INSERT INTO `kcson`.`pcat` (`id`, `pcat`, `prim`) VALUES (5, 'одиноко проживающие граждане пожилого возраста', NULL);
INSERT INTO `kcson`.`pcat` (`id`, `pcat`, `prim`) VALUES (3, 'граждане пожилого возраста проживающие в семьях', NULL);
INSERT INTO `kcson`.`pcat` (`id`, `pcat`, `prim`) VALUES (4, 'инвалиды трудоспособного возраста', NULL);
INSERT INTO `kcson`.`pcat` (`id`, `pcat`, `prim`) VALUES (2, 'одиноко проживающие супружеские пары пожилого возраста', NULL);
INSERT INTO `kcson`.`pcat` (`id`, `pcat`, `prim`) VALUES (1, 'НЕ УКАЗАН', NULL);

COMMIT;


-- -----------------------------------------------------
-- Data for table `kcson`.`ripso`
-- -----------------------------------------------------
START TRANSACTION;
USE `kcson`;
INSERT INTO `kcson`.`ripso` (`id`, `ripso`, `year`, `archive`, `servform_id`, `months`, `pcat_id`) VALUES (1, '1', 2019, 1, 1, 12, 5);
INSERT INTO `kcson`.`ripso` (`id`, `ripso`, `year`, `archive`, `servform_id`, `months`, `pcat_id`) VALUES (2, '2', 2019, 1, 2, 12, 5);
INSERT INTO `kcson`.`ripso` (`id`, `ripso`, `year`, `archive`, `servform_id`, `months`, `pcat_id`) VALUES (3, '3', 2019, 1, 3, 2, 5);
INSERT INTO `kcson`.`ripso` (`id`, `ripso`, `year`, `archive`, `servform_id`, `months`, `pcat_id`) VALUES (4, '4', 2019, 1, 4, 3, 5);
INSERT INTO `kcson`.`ripso` (`id`, `ripso`, `year`, `archive`, `servform_id`, `months`, `pcat_id`) VALUES (5, '5', 2019, 1, 4, 12, 1);
INSERT INTO `kcson`.`ripso` (`id`, `ripso`, `year`, `archive`, `servform_id`, `months`, `pcat_id`) VALUES (6, '6', 2019, 1, 1, 12, 3);
INSERT INTO `kcson`.`ripso` (`id`, `ripso`, `year`, `archive`, `servform_id`, `months`, `pcat_id`) VALUES (7, '7', 2019, 1, 2, 12, 3);
INSERT INTO `kcson`.`ripso` (`id`, `ripso`, `year`, `archive`, `servform_id`, `months`, `pcat_id`) VALUES (8, '8', 2019, 1, 3, 2, 3);
INSERT INTO `kcson`.`ripso` (`id`, `ripso`, `year`, `archive`, `servform_id`, `months`, `pcat_id`) VALUES (9, '9', 2019, 1, 4, 3, 3);
INSERT INTO `kcson`.`ripso` (`id`, `ripso`, `year`, `archive`, `servform_id`, `months`, `pcat_id`) VALUES (10, '14', 2019, 1, 1, 12, 4);
INSERT INTO `kcson`.`ripso` (`id`, `ripso`, `year`, `archive`, `servform_id`, `months`, `pcat_id`) VALUES (11, '70', 2019, 1, 3, 12, 1);
INSERT INTO `kcson`.`ripso` (`id`, `ripso`, `year`, `archive`, `servform_id`, `months`, `pcat_id`) VALUES (12, '71', 2019, 1, 3, 12, 1);

COMMIT;


-- -----------------------------------------------------
-- Data for table `kcson`.`contracts`
-- -----------------------------------------------------
START TRANSACTION;
USE `kcson`;
INSERT INTO `kcson`.`contracts` (`id`, `contracts`, `ufio_id`, `dep_id`, `ripso_id`, `blocked`, `startdate`, `enddate`, `ippsuNum`, `note`, `create`, `ts`, `cr_by`, `upd_by`) VALUES (DEFAULT, '12312313', 1, 1, 1, 0, '2001-01-01', '2020-12-31', NULL, NULL, NULL, NULL, NULL, NULL);
INSERT INTO `kcson`.`contracts` (`id`, `contracts`, `ufio_id`, `dep_id`, `ripso_id`, `blocked`, `startdate`, `enddate`, `ippsuNum`, `note`, `create`, `ts`, `cr_by`, `upd_by`) VALUES (DEFAULT, '43434', 2, 1, 1, 0, '2001-01-01', '2020-12-31', NULL, NULL, NULL, NULL, NULL, NULL);

COMMIT;


-- -----------------------------------------------------
-- Data for table `kcson`.`role`
-- -----------------------------------------------------
START TRANSACTION;
USE `kcson`;
INSERT INTO `kcson`.`role` (`id`, `role`, `prim`) VALUES (1, 'Роль не указана', NULL);
INSERT INTO `kcson`.`role` (`id`, `role`, `prim`) VALUES (2, 'Общая информация', NULL);
INSERT INTO `kcson`.`role` (`id`, `role`, `prim`) VALUES (3, 'Работник', NULL);
INSERT INTO `kcson`.`role` (`id`, `role`, `prim`) VALUES (4, 'Специалист', NULL);
INSERT INTO `kcson`.`role` (`id`, `role`, `prim`) VALUES (5, 'Доверенный специалист', NULL);
INSERT INTO `kcson`.`role` (`id`, `role`, `prim`) VALUES (6, 'Заведующий отделением', NULL);

COMMIT;


-- -----------------------------------------------------
-- Data for table `kcson`.`worker`
-- -----------------------------------------------------
START TRANSACTION;
USE `kcson`;
INSERT INTO `kcson`.`worker` (`id`, `worker`, `user`, `prim`, `role_id`, `dep_id`, `archive`) VALUES (1, 'Не указан', 'newuser', NULL, DEFAULT, 1, NULL);
INSERT INTO `kcson`.`worker` (`id`, `worker`, `user`, `prim`, `role_id`, `dep_id`, `archive`) VALUES (2, 'Не указан(Админ)', 'root', NULL, DEFAULT, 1, NULL);

COMMIT;


-- -----------------------------------------------------
-- Data for table `kcson`.`job`
-- -----------------------------------------------------
START TRANSACTION;
USE `kcson`;
INSERT INTO `kcson`.`job` (`id`, `job`, `prim`) VALUES (DEFAULT, 'Должность не указана', '');
INSERT INTO `kcson`.`job` (`id`, `job`, `prim`) VALUES (2, 'Медицинская сестра', '');
INSERT INTO `kcson`.`job` (`id`, `job`, `prim`) VALUES (3, 'Социальный работник', '');
INSERT INTO `kcson`.`job` (`id`, `job`, `prim`) VALUES (4, 'Медбрат', '');
INSERT INTO `kcson`.`job` (`id`, `job`, `prim`) VALUES (5, 'Психолог', '');
INSERT INTO `kcson`.`job` (`id`, `job`, `prim`) VALUES (6, 'Культорганизатор', '');
INSERT INTO `kcson`.`job` (`id`, `job`, `prim`) VALUES (7, 'Концертмейстер', '');
INSERT INTO `kcson`.`job` (`id`, `job`, `prim`) VALUES (8, 'Хормейстер', '');
INSERT INTO `kcson`.`job` (`id`, `job`, `prim`) VALUES (9, 'Инструктор по труду', '');
INSERT INTO `kcson`.`job` (`id`, `job`, `prim`) VALUES (10, 'Администратор дежурный', '');
INSERT INTO `kcson`.`job` (`id`, `job`, `prim`) VALUES (11, 'Заведующий отделением', '');
INSERT INTO `kcson`.`job` (`id`, `job`, `prim`) VALUES (12, 'Специалист по социальной работе', '');
INSERT INTO `kcson`.`job` (`id`, `job`, `prim`) VALUES (13, 'Юрист', '');
INSERT INTO `kcson`.`job` (`id`, `job`, `prim`) VALUES (14, 'Инструктор по ЛФК', '');
INSERT INTO `kcson`.`job` (`id`, `job`, `prim`) VALUES (15, 'Медицинский брат', NULL);

COMMIT;


-- -----------------------------------------------------
-- Data for table `kcson`.`dep_has_worker`
-- -----------------------------------------------------
START TRANSACTION;
USE `kcson`;
INSERT INTO `kcson`.`dep_has_worker` (`id`, `dep_has_worker`, `worker_id`, `dep_id`, `job_id`, `prim`, `archive`, `from`, `till`, `role_id`) VALUES (1, 'тестовый работник', 1, 1, 1, NULL, 0, NULL, NULL, 6);
INSERT INTO `kcson`.`dep_has_worker` (`id`, `dep_has_worker`, `worker_id`, `dep_id`, `job_id`, `prim`, `archive`, `from`, `till`, `role_id`) VALUES (2, 'тестовый работник2', 1, 2, 1, NULL, 0, NULL, NULL, 6);
INSERT INTO `kcson`.`dep_has_worker` (`id`, `dep_has_worker`, `worker_id`, `dep_id`, `job_id`, `prim`, `archive`, `from`, `till`, `role_id`) VALUES (3, 'Админ(root)', 2, 3, 1, NULL, 0, NULL, NULL, 6);

COMMIT;


-- -----------------------------------------------------
-- Data for table `kcson`.`main`
-- -----------------------------------------------------
START TRANSACTION;
USE `kcson`;
INSERT INTO `kcson`.`main` (`id`, `contracts_id`, `dep_id`, `ufio_id`, `serv_id`, `dep_has_worker_id`, `worker_id`, `vdate`, `uslnum`, `note`, `create`, `ts`, `cr_by`, `upd_by`, `reported`, `wdate`, `overdid`) VALUES (DEFAULT, 1, 1, 1, 11, DEFAULT, 1, '2001-06-01', 10, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL);
INSERT INTO `kcson`.`main` (`id`, `contracts_id`, `dep_id`, `ufio_id`, `serv_id`, `dep_has_worker_id`, `worker_id`, `vdate`, `uslnum`, `note`, `create`, `ts`, `cr_by`, `upd_by`, `reported`, `wdate`, `overdid`) VALUES (DEFAULT, 1, 1, 1, 17, DEFAULT, 1, '2001-06-02', 11, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL);
INSERT INTO `kcson`.`main` (`id`, `contracts_id`, `dep_id`, `ufio_id`, `serv_id`, `dep_has_worker_id`, `worker_id`, `vdate`, `uslnum`, `note`, `create`, `ts`, `cr_by`, `upd_by`, `reported`, `wdate`, `overdid`) VALUES (DEFAULT, 2, 1, 2, 15, DEFAULT, 1, '2001-06-03', 12, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL);

COMMIT;


-- -----------------------------------------------------
-- Data for table `kcson`.`holiday`
-- -----------------------------------------------------
START TRANSACTION;
USE `kcson`;
INSERT INTO `kcson`.`holiday` (`holiday`, `prim`) VALUES ('2019-01-01', '');
INSERT INTO `kcson`.`holiday` (`holiday`, `prim`) VALUES ('2019-01-02', '');
INSERT INTO `kcson`.`holiday` (`holiday`, `prim`) VALUES ('2019-01-03', '');
INSERT INTO `kcson`.`holiday` (`holiday`, `prim`) VALUES ('2019-01-04', '');
INSERT INTO `kcson`.`holiday` (`holiday`, `prim`) VALUES ('2019-01-05', '');
INSERT INTO `kcson`.`holiday` (`holiday`, `prim`) VALUES ('2019-01-06', '');
INSERT INTO `kcson`.`holiday` (`holiday`, `prim`) VALUES ('2019-01-07', '');
INSERT INTO `kcson`.`holiday` (`holiday`, `prim`) VALUES ('2019-01-08', '');
INSERT INTO `kcson`.`holiday` (`holiday`, `prim`) VALUES ('2019-03-08', '');
INSERT INTO `kcson`.`holiday` (`holiday`, `prim`) VALUES ('2019-05-01', '');
INSERT INTO `kcson`.`holiday` (`holiday`, `prim`) VALUES ('2019-05-02', '');
INSERT INTO `kcson`.`holiday` (`holiday`, `prim`) VALUES ('2019-05-03', '');
INSERT INTO `kcson`.`holiday` (`holiday`, `prim`) VALUES ('2019-05-09', '');
INSERT INTO `kcson`.`holiday` (`holiday`, `prim`) VALUES ('2019-05-10', '');
INSERT INTO `kcson`.`holiday` (`holiday`, `prim`) VALUES ('2019-06-12', '');
INSERT INTO `kcson`.`holiday` (`holiday`, `prim`) VALUES ('2019-11-04', '');

COMMIT;


-- -----------------------------------------------------
-- Data for table `kcson`.`category`
-- -----------------------------------------------------
START TRANSACTION;
USE `kcson`;
INSERT INTO `kcson`.`category` (`id`, `category`, `archive`, `prim`, `total`, `subof`) VALUES (13, 'Инвалид', 0, NULL, 0, NULL);
INSERT INTO `kcson`.`category` (`id`, `category`, `archive`, `prim`, `total`, `subof`) VALUES (14, 'ИПР', NULL, NULL, 0, 13);
INSERT INTO `kcson`.`category` (`id`, `category`, `archive`, `prim`, `total`, `subof`) VALUES (15, 'Социо-культ. ИПР', NULL, NULL, NULL, 14);
INSERT INTO `kcson`.`category` (`id`, `category`, `archive`, `prim`, `total`, `subof`) VALUES (16, 'Социо-псих. ИПР', NULL, NULL, NULL, 14);
INSERT INTO `kcson`.`category` (`id`, `category`, `archive`, `prim`, `total`, `subof`) VALUES (3, 'ВТ', NULL, 'Ветеран труда', NULL, NULL);
INSERT INTO `kcson`.`category` (`id`, `category`, `archive`, `prim`, `total`, `subof`) VALUES (4, 'ПМИНОБ', NULL, 'Пенсионер мин. обороны', NULL, NULL);
INSERT INTO `kcson`.`category` (`id`, `category`, `archive`, `prim`, `total`, `subof`) VALUES (5, 'ИВОВ', NULL, 'Инвалид ВОВ', NULL, 2);
INSERT INTO `kcson`.`category` (`id`, `category`, `archive`, `prim`, `total`, `subof`) VALUES (6, 'УВ', NULL, NULL, NULL, 2);
INSERT INTO `kcson`.`category` (`id`, `category`, `archive`, `prim`, `total`, `subof`) VALUES (7, 'ЖБЛ', NULL, NULL, NULL, 2);
INSERT INTO `kcson`.`category` (`id`, `category`, `archive`, `prim`, `total`, `subof`) VALUES (8, 'ТБЛ', NULL, NULL, NULL, 2);
INSERT INTO `kcson`.`category` (`id`, `category`, `archive`, `prim`, `total`, `subof`) VALUES (11, 'Узники конц.л.', NULL, NULL, NULL, 1);
INSERT INTO `kcson`.`category` (`id`, `category`, `archive`, `prim`, `total`, `subof`) VALUES (12, 'Вдовы ВОВ', NULL, NULL, NULL, 1);
INSERT INTO `kcson`.`category` (`id`, `category`, `archive`, `prim`, `total`, `subof`) VALUES (1, 'УВОВр', 0, 'Участник Отечественной Войны(ЖБЛ,ТБЛ,ТТ,узники, вдовы)', NULL, NULL);
INSERT INTO `kcson`.`category` (`id`, `category`, `archive`, `prim`, `total`, `subof`) VALUES (2, 'УВОВ', 0, 'Участник Отечественной Войны(ЖБЛ,ТБЛ,ТТ)', NULL, 1);
INSERT INTO `kcson`.`category` (`id`, `category`, `archive`, `prim`, `total`, `subof`) VALUES (9, 'ТТ', NULL, NULL, NULL, 2);
INSERT INTO `kcson`.`category` (`id`, `category`, `archive`, `prim`, `total`, `subof`) VALUES (10, 'УТТ', NULL, NULL, NULL, 2);

COMMIT;


-- -----------------------------------------------------
-- Data for table `kcson`.`contracts_has_serv`
-- -----------------------------------------------------
START TRANSACTION;
USE `kcson`;
INSERT INTO `kcson`.`contracts_has_serv` (`serv_id`, `contracts_id`, `planned`, `filled`, `prim`, `archive`, `create`, `ts`, `cr_by`, `upd_by`) VALUES (1, 1, 10, NULL, NULL, NULL, NULL, NULL, NULL, NULL);
INSERT INTO `kcson`.`contracts_has_serv` (`serv_id`, `contracts_id`, `planned`, `filled`, `prim`, `archive`, `create`, `ts`, `cr_by`, `upd_by`) VALUES (2, 1, 10, NULL, NULL, NULL, NULL, NULL, NULL, NULL);
INSERT INTO `kcson`.`contracts_has_serv` (`serv_id`, `contracts_id`, `planned`, `filled`, `prim`, `archive`, `create`, `ts`, `cr_by`, `upd_by`) VALUES (3, 1, 10, NULL, NULL, NULL, NULL, NULL, NULL, NULL);
INSERT INTO `kcson`.`contracts_has_serv` (`serv_id`, `contracts_id`, `planned`, `filled`, `prim`, `archive`, `create`, `ts`, `cr_by`, `upd_by`) VALUES (4, 1, 100, NULL, NULL, NULL, NULL, NULL, NULL, NULL);
INSERT INTO `kcson`.`contracts_has_serv` (`serv_id`, `contracts_id`, `planned`, `filled`, `prim`, `archive`, `create`, `ts`, `cr_by`, `upd_by`) VALUES (5, 1, 100, NULL, NULL, NULL, NULL, NULL, NULL, NULL);
INSERT INTO `kcson`.`contracts_has_serv` (`serv_id`, `contracts_id`, `planned`, `filled`, `prim`, `archive`, `create`, `ts`, `cr_by`, `upd_by`) VALUES (6, 1, 10, NULL, NULL, NULL, NULL, NULL, NULL, NULL);
INSERT INTO `kcson`.`contracts_has_serv` (`serv_id`, `contracts_id`, `planned`, `filled`, `prim`, `archive`, `create`, `ts`, `cr_by`, `upd_by`) VALUES (7, 1, 10, NULL, NULL, NULL, NULL, NULL, NULL, NULL);
INSERT INTO `kcson`.`contracts_has_serv` (`serv_id`, `contracts_id`, `planned`, `filled`, `prim`, `archive`, `create`, `ts`, `cr_by`, `upd_by`) VALUES (8, 1, 10, NULL, NULL, NULL, NULL, NULL, NULL, NULL);
INSERT INTO `kcson`.`contracts_has_serv` (`serv_id`, `contracts_id`, `planned`, `filled`, `prim`, `archive`, `create`, `ts`, `cr_by`, `upd_by`) VALUES (9, 1, 10, NULL, NULL, NULL, NULL, NULL, NULL, NULL);
INSERT INTO `kcson`.`contracts_has_serv` (`serv_id`, `contracts_id`, `planned`, `filled`, `prim`, `archive`, `create`, `ts`, `cr_by`, `upd_by`) VALUES (10, 1, 10, NULL, NULL, NULL, NULL, NULL, NULL, NULL);
INSERT INTO `kcson`.`contracts_has_serv` (`serv_id`, `contracts_id`, `planned`, `filled`, `prim`, `archive`, `create`, `ts`, `cr_by`, `upd_by`) VALUES (1, 2, 10, NULL, NULL, NULL, NULL, NULL, NULL, NULL);
INSERT INTO `kcson`.`contracts_has_serv` (`serv_id`, `contracts_id`, `planned`, `filled`, `prim`, `archive`, `create`, `ts`, `cr_by`, `upd_by`) VALUES (2, 2, 10, NULL, NULL, NULL, NULL, NULL, NULL, NULL);
INSERT INTO `kcson`.`contracts_has_serv` (`serv_id`, `contracts_id`, `planned`, `filled`, `prim`, `archive`, `create`, `ts`, `cr_by`, `upd_by`) VALUES (3, 2, 10, NULL, NULL, NULL, NULL, NULL, NULL, NULL);
INSERT INTO `kcson`.`contracts_has_serv` (`serv_id`, `contracts_id`, `planned`, `filled`, `prim`, `archive`, `create`, `ts`, `cr_by`, `upd_by`) VALUES (4, 2, 10, NULL, NULL, NULL, NULL, NULL, NULL, NULL);
INSERT INTO `kcson`.`contracts_has_serv` (`serv_id`, `contracts_id`, `planned`, `filled`, `prim`, `archive`, `create`, `ts`, `cr_by`, `upd_by`) VALUES (5, 2, 10, NULL, NULL, NULL, NULL, NULL, NULL, NULL);
INSERT INTO `kcson`.`contracts_has_serv` (`serv_id`, `contracts_id`, `planned`, `filled`, `prim`, `archive`, `create`, `ts`, `cr_by`, `upd_by`) VALUES (6, 2, 10, NULL, NULL, NULL, NULL, NULL, NULL, NULL);
INSERT INTO `kcson`.`contracts_has_serv` (`serv_id`, `contracts_id`, `planned`, `filled`, `prim`, `archive`, `create`, `ts`, `cr_by`, `upd_by`) VALUES (7, 2, 10, NULL, NULL, NULL, NULL, NULL, NULL, NULL);
INSERT INTO `kcson`.`contracts_has_serv` (`serv_id`, `contracts_id`, `planned`, `filled`, `prim`, `archive`, `create`, `ts`, `cr_by`, `upd_by`) VALUES (8, 2, 10, NULL, NULL, NULL, NULL, NULL, NULL, NULL);
INSERT INTO `kcson`.`contracts_has_serv` (`serv_id`, `contracts_id`, `planned`, `filled`, `prim`, `archive`, `create`, `ts`, `cr_by`, `upd_by`) VALUES (9, 2, 10, NULL, NULL, NULL, NULL, NULL, NULL, NULL);
INSERT INTO `kcson`.`contracts_has_serv` (`serv_id`, `contracts_id`, `planned`, `filled`, `prim`, `archive`, `create`, `ts`, `cr_by`, `upd_by`) VALUES (10, 2, 10, NULL, NULL, NULL, NULL, NULL, NULL, NULL);

COMMIT;


-- -----------------------------------------------------
-- Data for table `kcson`.`setting`
-- -----------------------------------------------------
START TRANSACTION;
USE `kcson`;
INSERT INTO `kcson`.`setting` (`id`, `archive`, `setting`, `value`, `prim`, `sdate`) VALUES (1, 0, 'org', 'СПБ ГБУСОН \"КЦСОН Адмиралтейского района Санкт-Петербурга\"', NULL, DEFAULT);
INSERT INTO `kcson`.`setting` (`id`, `archive`, `setting`, `value`, `prim`, `sdate`) VALUES (2, 0, 'full_org', 'Санкт-Петербургское государственное бюджетное учреждение социального обслуживания населения «Комплексный центр социального обслуживания населения Адмиралтейского района Санкт-Петербурга»', NULL, DEFAULT);

COMMIT;


-- -----------------------------------------------------
-- Data for table `kcson`.`jobGroup`
-- -----------------------------------------------------
START TRANSACTION;
USE `kcson`;
INSERT INTO `kcson`.`jobGroup` (`id`, `jobGroup`, `prim`) VALUES (1, 'Группа не указана ', NULL);

COMMIT;


-- -----------------------------------------------------
-- Data for table `kcson`.`add_info`
-- -----------------------------------------------------
START TRANSACTION;
USE `kcson`;
INSERT INTO `kcson`.`add_info` (`pddate`, `contracts_id`, `predv_money`, `curFIO`, `psp`, `address`, `sdd`, `sdd_date`, `perc`, `not_standart_contract`, `not_standart_act`, `prim`, `create`, `ts`, `cr_by`, `upd_by`, `repr_FIO`, `repr_addr`, `repr_psp`, `work_livemin`) VALUES ('2001-02-01', 2, 0, NULL, NULL, NULL, 13000, NULL, 0.1, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL);
INSERT INTO `kcson`.`add_info` (`pddate`, `contracts_id`, `predv_money`, `curFIO`, `psp`, `address`, `sdd`, `sdd_date`, `perc`, `not_standart_contract`, `not_standart_act`, `prim`, `create`, `ts`, `cr_by`, `upd_by`, `repr_FIO`, `repr_addr`, `repr_psp`, `work_livemin`) VALUES ('2001-06-01', 2, 0, NULL, NULL, NULL, 17000, NULL, 0.15, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL);
INSERT INTO `kcson`.`add_info` (`pddate`, `contracts_id`, `predv_money`, `curFIO`, `psp`, `address`, `sdd`, `sdd_date`, `perc`, `not_standart_contract`, `not_standart_act`, `prim`, `create`, `ts`, `cr_by`, `upd_by`, `repr_FIO`, `repr_addr`, `repr_psp`, `work_livemin`) VALUES ('2001-03-01', 1, 5284.43 , NULL, NULL, NULL, 24000, NULL, 0.2, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL);

COMMIT;


-- -----------------------------------------------------
-- Data for table `kcson`.`ripso_has_serv`
-- -----------------------------------------------------
START TRANSACTION;
USE `kcson`;
INSERT INTO `kcson`.`ripso_has_serv` (`planned`, `serv_id`, `ripso_id`) VALUES (1768,  1,  1);
INSERT INTO `kcson`.`ripso_has_serv` (`planned`, `serv_id`, `ripso_id`) VALUES (1768,  2,  1);
INSERT INTO `kcson`.`ripso_has_serv` (`planned`, `serv_id`, `ripso_id`) VALUES (1216,  3,  1);
INSERT INTO `kcson`.`ripso_has_serv` (`planned`, `serv_id`, `ripso_id`) VALUES (104,  4,  1);
INSERT INTO `kcson`.`ripso_has_serv` (`planned`, `serv_id`, `ripso_id`) VALUES (156,  5,  1);
INSERT INTO `kcson`.`ripso_has_serv` (`planned`, `serv_id`, `ripso_id`) VALUES (156,  6,  1);
INSERT INTO `kcson`.`ripso_has_serv` (`planned`, `serv_id`, `ripso_id`) VALUES (156,  7,  1);
INSERT INTO `kcson`.`ripso_has_serv` (`planned`, `serv_id`, `ripso_id`) VALUES (52,  8,  1);
INSERT INTO `kcson`.`ripso_has_serv` (`planned`, `serv_id`, `ripso_id`) VALUES (156,  9,  1);
INSERT INTO `kcson`.`ripso_has_serv` (`planned`, `serv_id`, `ripso_id`) VALUES (156,  10,  1);
INSERT INTO `kcson`.`ripso_has_serv` (`planned`, `serv_id`, `ripso_id`) VALUES (12,  11,  1);
INSERT INTO `kcson`.`ripso_has_serv` (`planned`, `serv_id`, `ripso_id`) VALUES (24,  12,  1);
INSERT INTO `kcson`.`ripso_has_serv` (`planned`, `serv_id`, `ripso_id`) VALUES (12,  13,  1);
INSERT INTO `kcson`.`ripso_has_serv` (`planned`, `serv_id`, `ripso_id`) VALUES (12,  14,  1);
INSERT INTO `kcson`.`ripso_has_serv` (`planned`, `serv_id`, `ripso_id`) VALUES (12,  15,  1);
INSERT INTO `kcson`.`ripso_has_serv` (`planned`, `serv_id`, `ripso_id`) VALUES (1,  16,  1);
INSERT INTO `kcson`.`ripso_has_serv` (`planned`, `serv_id`, `ripso_id`) VALUES (1,  17,  1);
INSERT INTO `kcson`.`ripso_has_serv` (`planned`, `serv_id`, `ripso_id`) VALUES (12,  18,  1);
INSERT INTO `kcson`.`ripso_has_serv` (`planned`, `serv_id`, `ripso_id`) VALUES (1,  22,  1);
INSERT INTO `kcson`.`ripso_has_serv` (`planned`, `serv_id`, `ripso_id`) VALUES (12,  23,  1);
INSERT INTO `kcson`.`ripso_has_serv` (`planned`, `serv_id`, `ripso_id`) VALUES (156,  24,  1);
INSERT INTO `kcson`.`ripso_has_serv` (`planned`, `serv_id`, `ripso_id`) VALUES (12,  25,  1);
INSERT INTO `kcson`.`ripso_has_serv` (`planned`, `serv_id`, `ripso_id`) VALUES (2,  26,  1);
INSERT INTO `kcson`.`ripso_has_serv` (`planned`, `serv_id`, `ripso_id`) VALUES (4,  27,  1);
INSERT INTO `kcson`.`ripso_has_serv` (`planned`, `serv_id`, `ripso_id`) VALUES (1,  29,  1);
INSERT INTO `kcson`.`ripso_has_serv` (`planned`, `serv_id`, `ripso_id`) VALUES (1,  30,  1);
INSERT INTO `kcson`.`ripso_has_serv` (`planned`, `serv_id`, `ripso_id`) VALUES (1,  31,  1);
INSERT INTO `kcson`.`ripso_has_serv` (`planned`, `serv_id`, `ripso_id`) VALUES (1,  32,  1);
INSERT INTO `kcson`.`ripso_has_serv` (`planned`, `serv_id`, `ripso_id`) VALUES (1,  33,  1);
INSERT INTO `kcson`.`ripso_has_serv` (`planned`, `serv_id`, `ripso_id`) VALUES (2,  34,  1);
INSERT INTO `kcson`.`ripso_has_serv` (`planned`, `serv_id`, `ripso_id`) VALUES (474,  38,  1);
INSERT INTO `kcson`.`ripso_has_serv` (`planned`, `serv_id`, `ripso_id`) VALUES (2,  39,  1);
INSERT INTO `kcson`.`ripso_has_serv` (`planned`, `serv_id`, `ripso_id`) VALUES (156,  40,  1);
INSERT INTO `kcson`.`ripso_has_serv` (`planned`, `serv_id`, `ripso_id`) VALUES (156,  41,  1);
INSERT INTO `kcson`.`ripso_has_serv` (`planned`, `serv_id`, `ripso_id`) VALUES (156,  42,  1);
INSERT INTO `kcson`.`ripso_has_serv` (`planned`, `serv_id`, `ripso_id`) VALUES (4,  43,  1);
INSERT INTO `kcson`.`ripso_has_serv` (`planned`, `serv_id`, `ripso_id`) VALUES (16,  44,  1);
INSERT INTO `kcson`.`ripso_has_serv` (`planned`, `serv_id`, `ripso_id`) VALUES (4,  45,  1);
INSERT INTO `kcson`.`ripso_has_serv` (`planned`, `serv_id`, `ripso_id`) VALUES (12,  46,  1);
INSERT INTO `kcson`.`ripso_has_serv` (`planned`, `serv_id`, `ripso_id`) VALUES (54,  47,  1);
INSERT INTO `kcson`.`ripso_has_serv` (`planned`, `serv_id`, `ripso_id`) VALUES (1,  48,  1);
INSERT INTO `kcson`.`ripso_has_serv` (`planned`, `serv_id`, `ripso_id`) VALUES (1,  49,  1);
INSERT INTO `kcson`.`ripso_has_serv` (`planned`, `serv_id`, `ripso_id`) VALUES (52,  50,  1);
INSERT INTO `kcson`.`ripso_has_serv` (`planned`, `serv_id`, `ripso_id`) VALUES (6,  53,  1);
INSERT INTO `kcson`.`ripso_has_serv` (`planned`, `serv_id`, `ripso_id`) VALUES (1,  54,  1);
INSERT INTO `kcson`.`ripso_has_serv` (`planned`, `serv_id`, `ripso_id`) VALUES (1,  55,  1);
INSERT INTO `kcson`.`ripso_has_serv` (`planned`, `serv_id`, `ripso_id`) VALUES (1,  56,  1);
INSERT INTO `kcson`.`ripso_has_serv` (`planned`, `serv_id`, `ripso_id`) VALUES (1,  57,  1);
INSERT INTO `kcson`.`ripso_has_serv` (`planned`, `serv_id`, `ripso_id`) VALUES (1,  58,  1);
INSERT INTO `kcson`.`ripso_has_serv` (`planned`, `serv_id`, `ripso_id`) VALUES (1,  59,  1);
INSERT INTO `kcson`.`ripso_has_serv` (`planned`, `serv_id`, `ripso_id`) VALUES (2,  60,  1);
INSERT INTO `kcson`.`ripso_has_serv` (`planned`, `serv_id`, `ripso_id`) VALUES (1,  61,  1);
INSERT INTO `kcson`.`ripso_has_serv` (`planned`, `serv_id`, `ripso_id`) VALUES (1,  62,  1);
INSERT INTO `kcson`.`ripso_has_serv` (`planned`, `serv_id`, `ripso_id`) VALUES (518,  1,  2);
INSERT INTO `kcson`.`ripso_has_serv` (`planned`, `serv_id`, `ripso_id`) VALUES (518,  64,  2);
INSERT INTO `kcson`.`ripso_has_serv` (`planned`, `serv_id`, `ripso_id`) VALUES (4,  65,  2);
INSERT INTO `kcson`.`ripso_has_serv` (`planned`, `serv_id`, `ripso_id`) VALUES (1,  95,  2);
INSERT INTO `kcson`.`ripso_has_serv` (`planned`, `serv_id`, `ripso_id`) VALUES (1,  96,  2);
INSERT INTO `kcson`.`ripso_has_serv` (`planned`, `serv_id`, `ripso_id`) VALUES (2,  97,  2);
INSERT INTO `kcson`.`ripso_has_serv` (`planned`, `serv_id`, `ripso_id`) VALUES (162,  98,  2);
INSERT INTO `kcson`.`ripso_has_serv` (`planned`, `serv_id`, `ripso_id`) VALUES (4,  99,  2);
INSERT INTO `kcson`.`ripso_has_serv` (`planned`, `serv_id`, `ripso_id`) VALUES (10,  101,  2);
INSERT INTO `kcson`.`ripso_has_serv` (`planned`, `serv_id`, `ripso_id`) VALUES (4,  103,  2);
INSERT INTO `kcson`.`ripso_has_serv` (`planned`, `serv_id`, `ripso_id`) VALUES (48,  104,  2);
INSERT INTO `kcson`.`ripso_has_serv` (`planned`, `serv_id`, `ripso_id`) VALUES (96,  105,  2);
INSERT INTO `kcson`.`ripso_has_serv` (`planned`, `serv_id`, `ripso_id`) VALUES (52,  107,  2);
INSERT INTO `kcson`.`ripso_has_serv` (`planned`, `serv_id`, `ripso_id`) VALUES (16,  108,  2);
INSERT INTO `kcson`.`ripso_has_serv` (`planned`, `serv_id`, `ripso_id`) VALUES (12,  109,  2);
INSERT INTO `kcson`.`ripso_has_serv` (`planned`, `serv_id`, `ripso_id`) VALUES (24,  110,  2);
INSERT INTO `kcson`.`ripso_has_serv` (`planned`, `serv_id`, `ripso_id`) VALUES (290,  111,  2);
INSERT INTO `kcson`.`ripso_has_serv` (`planned`, `serv_id`, `ripso_id`) VALUES (2,  112,  2);
INSERT INTO `kcson`.`ripso_has_serv` (`planned`, `serv_id`, `ripso_id`) VALUES (48,  122,  2);
INSERT INTO `kcson`.`ripso_has_serv` (`planned`, `serv_id`, `ripso_id`) VALUES (120,  123,  2);
INSERT INTO `kcson`.`ripso_has_serv` (`planned`, `serv_id`, `ripso_id`) VALUES (24,  124,  2);
INSERT INTO `kcson`.`ripso_has_serv` (`planned`, `serv_id`, `ripso_id`) VALUES (96,  125,  2);
INSERT INTO `kcson`.`ripso_has_serv` (`planned`, `serv_id`, `ripso_id`) VALUES (5,  134,  2);
INSERT INTO `kcson`.`ripso_has_serv` (`planned`, `serv_id`, `ripso_id`) VALUES (1,  135,  2);
INSERT INTO `kcson`.`ripso_has_serv` (`planned`, `serv_id`, `ripso_id`) VALUES (1,  136,  2);
INSERT INTO `kcson`.`ripso_has_serv` (`planned`, `serv_id`, `ripso_id`) VALUES (1,  140,  2);
INSERT INTO `kcson`.`ripso_has_serv` (`planned`, `serv_id`, `ripso_id`) VALUES (1,  142,  2);
INSERT INTO `kcson`.`ripso_has_serv` (`planned`, `serv_id`, `ripso_id`) VALUES (1,  143,  2);
INSERT INTO `kcson`.`ripso_has_serv` (`planned`, `serv_id`, `ripso_id`) VALUES (5,  144,  2);
INSERT INTO `kcson`.`ripso_has_serv` (`planned`, `serv_id`, `ripso_id`) VALUES (1,  145,  2);
INSERT INTO `kcson`.`ripso_has_serv` (`planned`, `serv_id`, `ripso_id`) VALUES (1,  146,  2);
INSERT INTO `kcson`.`ripso_has_serv` (`planned`, `serv_id`, `ripso_id`) VALUES (1,  147,  2);
INSERT INTO `kcson`.`ripso_has_serv` (`planned`, `serv_id`, `ripso_id`) VALUES (1,  148,  2);
INSERT INTO `kcson`.`ripso_has_serv` (`planned`, `serv_id`, `ripso_id`) VALUES (1,  149,  2);
INSERT INTO `kcson`.`ripso_has_serv` (`planned`, `serv_id`, `ripso_id`) VALUES (238,  1,  3);
INSERT INTO `kcson`.`ripso_has_serv` (`planned`, `serv_id`, `ripso_id`) VALUES (238,  64,  3);
INSERT INTO `kcson`.`ripso_has_serv` (`planned`, `serv_id`, `ripso_id`) VALUES (48,  65,  3);
INSERT INTO `kcson`.`ripso_has_serv` (`planned`, `serv_id`, `ripso_id`) VALUES (1,  66,  3);
INSERT INTO `kcson`.`ripso_has_serv` (`planned`, `serv_id`, `ripso_id`) VALUES (44,  70,  3);
INSERT INTO `kcson`.`ripso_has_serv` (`planned`, `serv_id`, `ripso_id`) VALUES (1,  92,  3);
INSERT INTO `kcson`.`ripso_has_serv` (`planned`, `serv_id`, `ripso_id`) VALUES (1,  95,  3);
INSERT INTO `kcson`.`ripso_has_serv` (`planned`, `serv_id`, `ripso_id`) VALUES (1,  97,  3);
INSERT INTO `kcson`.`ripso_has_serv` (`planned`, `serv_id`, `ripso_id`) VALUES (98,  98,  3);
INSERT INTO `kcson`.`ripso_has_serv` (`planned`, `serv_id`, `ripso_id`) VALUES (1,  99,  3);
INSERT INTO `kcson`.`ripso_has_serv` (`planned`, `serv_id`, `ripso_id`) VALUES (44,  100,  3);
INSERT INTO `kcson`.`ripso_has_serv` (`planned`, `serv_id`, `ripso_id`) VALUES (20,  101,  3);
INSERT INTO `kcson`.`ripso_has_serv` (`planned`, `serv_id`, `ripso_id`) VALUES (1,  103,  3);
INSERT INTO `kcson`.`ripso_has_serv` (`planned`, `serv_id`, `ripso_id`) VALUES (16,  104,  3);
INSERT INTO `kcson`.`ripso_has_serv` (`planned`, `serv_id`, `ripso_id`) VALUES (16,  105,  3);
INSERT INTO `kcson`.`ripso_has_serv` (`planned`, `serv_id`, `ripso_id`) VALUES (18,  107,  3);
INSERT INTO `kcson`.`ripso_has_serv` (`planned`, `serv_id`, `ripso_id`) VALUES (2,  108,  3);
INSERT INTO `kcson`.`ripso_has_serv` (`planned`, `serv_id`, `ripso_id`) VALUES (4,  109,  3);
INSERT INTO `kcson`.`ripso_has_serv` (`planned`, `serv_id`, `ripso_id`) VALUES (12,  110,  3);
INSERT INTO `kcson`.`ripso_has_serv` (`planned`, `serv_id`, `ripso_id`) VALUES (69,  111,  3);
INSERT INTO `kcson`.`ripso_has_serv` (`planned`, `serv_id`, `ripso_id`) VALUES (1,  113,  3);
INSERT INTO `kcson`.`ripso_has_serv` (`planned`, `serv_id`, `ripso_id`) VALUES (8,  122,  3);
INSERT INTO `kcson`.`ripso_has_serv` (`planned`, `serv_id`, `ripso_id`) VALUES (20,  123,  3);
INSERT INTO `kcson`.`ripso_has_serv` (`planned`, `serv_id`, `ripso_id`) VALUES (24,  124,  3);
INSERT INTO `kcson`.`ripso_has_serv` (`planned`, `serv_id`, `ripso_id`) VALUES (16,  125,  3);
INSERT INTO `kcson`.`ripso_has_serv` (`planned`, `serv_id`, `ripso_id`) VALUES (3,  134,  3);
INSERT INTO `kcson`.`ripso_has_serv` (`planned`, `serv_id`, `ripso_id`) VALUES (1,  135,  3);
INSERT INTO `kcson`.`ripso_has_serv` (`planned`, `serv_id`, `ripso_id`) VALUES (1,  142,  3);
INSERT INTO `kcson`.`ripso_has_serv` (`planned`, `serv_id`, `ripso_id`) VALUES (1,  143,  3);
INSERT INTO `kcson`.`ripso_has_serv` (`planned`, `serv_id`, `ripso_id`) VALUES (2,  144,  3);
INSERT INTO `kcson`.`ripso_has_serv` (`planned`, `serv_id`, `ripso_id`) VALUES (1,  145,  3);
INSERT INTO `kcson`.`ripso_has_serv` (`planned`, `serv_id`, `ripso_id`) VALUES (1,  149,  3);
INSERT INTO `kcson`.`ripso_has_serv` (`planned`, `serv_id`, `ripso_id`) VALUES (1186,  1,  4);
INSERT INTO `kcson`.`ripso_has_serv` (`planned`, `serv_id`, `ripso_id`) VALUES (1186,  150,  4);
INSERT INTO `kcson`.`ripso_has_serv` (`planned`, `serv_id`, `ripso_id`) VALUES (858,  151,  4);
INSERT INTO `kcson`.`ripso_has_serv` (`planned`, `serv_id`, `ripso_id`) VALUES (1,  152,  4);
INSERT INTO `kcson`.`ripso_has_serv` (`planned`, `serv_id`, `ripso_id`) VALUES (1,  153,  4);
INSERT INTO `kcson`.`ripso_has_serv` (`planned`, `serv_id`, `ripso_id`) VALUES (90,  163,  4);
INSERT INTO `kcson`.`ripso_has_serv` (`planned`, `serv_id`, `ripso_id`) VALUES (270,  182,  4);
INSERT INTO `kcson`.`ripso_has_serv` (`planned`, `serv_id`, `ripso_id`) VALUES (90,  183,  4);
INSERT INTO `kcson`.`ripso_has_serv` (`planned`, `serv_id`, `ripso_id`) VALUES (90,  185,  4);
INSERT INTO `kcson`.`ripso_has_serv` (`planned`, `serv_id`, `ripso_id`) VALUES (180,  186,  4);
INSERT INTO `kcson`.`ripso_has_serv` (`planned`, `serv_id`, `ripso_id`) VALUES (12,  187,  4);
INSERT INTO `kcson`.`ripso_has_serv` (`planned`, `serv_id`, `ripso_id`) VALUES (30,  188,  4);
INSERT INTO `kcson`.`ripso_has_serv` (`planned`, `serv_id`, `ripso_id`) VALUES (90,  190,  4);
INSERT INTO `kcson`.`ripso_has_serv` (`planned`, `serv_id`, `ripso_id`) VALUES (1,  191,  4);
INSERT INTO `kcson`.`ripso_has_serv` (`planned`, `serv_id`, `ripso_id`) VALUES (1,  192,  4);
INSERT INTO `kcson`.`ripso_has_serv` (`planned`, `serv_id`, `ripso_id`) VALUES (1,  198,  4);
INSERT INTO `kcson`.`ripso_has_serv` (`planned`, `serv_id`, `ripso_id`) VALUES (1,  201,  4);
INSERT INTO `kcson`.`ripso_has_serv` (`planned`, `serv_id`, `ripso_id`) VALUES (256,  202,  4);
INSERT INTO `kcson`.`ripso_has_serv` (`planned`, `serv_id`, `ripso_id`) VALUES (90,  204,  4);
INSERT INTO `kcson`.`ripso_has_serv` (`planned`, `serv_id`, `ripso_id`) VALUES (30,  205,  4);
INSERT INTO `kcson`.`ripso_has_serv` (`planned`, `serv_id`, `ripso_id`) VALUES (90,  206,  4);
INSERT INTO `kcson`.`ripso_has_serv` (`planned`, `serv_id`, `ripso_id`) VALUES (2,  208,  4);
INSERT INTO `kcson`.`ripso_has_serv` (`planned`, `serv_id`, `ripso_id`) VALUES (8,  209,  4);
INSERT INTO `kcson`.`ripso_has_serv` (`planned`, `serv_id`, `ripso_id`) VALUES (36,  210,  4);
INSERT INTO `kcson`.`ripso_has_serv` (`planned`, `serv_id`, `ripso_id`) VALUES (18,  212,  4);
INSERT INTO `kcson`.`ripso_has_serv` (`planned`, `serv_id`, `ripso_id`) VALUES (12,  213,  4);
INSERT INTO `kcson`.`ripso_has_serv` (`planned`, `serv_id`, `ripso_id`) VALUES (6,  214,  4);
INSERT INTO `kcson`.`ripso_has_serv` (`planned`, `serv_id`, `ripso_id`) VALUES (48,  216,  4);
INSERT INTO `kcson`.`ripso_has_serv` (`planned`, `serv_id`, `ripso_id`) VALUES (12,  226,  4);
INSERT INTO `kcson`.`ripso_has_serv` (`planned`, `serv_id`, `ripso_id`) VALUES (12,  227,  4);
INSERT INTO `kcson`.`ripso_has_serv` (`planned`, `serv_id`, `ripso_id`) VALUES (24,  229,  4);
INSERT INTO `kcson`.`ripso_has_serv` (`planned`, `serv_id`, `ripso_id`) VALUES (4,  239,  4);
INSERT INTO `kcson`.`ripso_has_serv` (`planned`, `serv_id`, `ripso_id`) VALUES (1,  240,  4);
INSERT INTO `kcson`.`ripso_has_serv` (`planned`, `serv_id`, `ripso_id`) VALUES (1,  241,  4);
INSERT INTO `kcson`.`ripso_has_serv` (`planned`, `serv_id`, `ripso_id`) VALUES (1,  245,  4);
INSERT INTO `kcson`.`ripso_has_serv` (`planned`, `serv_id`, `ripso_id`) VALUES (1,  251,  4);
INSERT INTO `kcson`.`ripso_has_serv` (`planned`, `serv_id`, `ripso_id`) VALUES (2,  253,  4);
INSERT INTO `kcson`.`ripso_has_serv` (`planned`, `serv_id`, `ripso_id`) VALUES (1,  254,  4);
INSERT INTO `kcson`.`ripso_has_serv` (`planned`, `serv_id`, `ripso_id`) VALUES (1,  255,  4);
INSERT INTO `kcson`.`ripso_has_serv` (`planned`, `serv_id`, `ripso_id`) VALUES (6953,  1,  5);
INSERT INTO `kcson`.`ripso_has_serv` (`planned`, `serv_id`, `ripso_id`) VALUES (6953,  150,  5);
INSERT INTO `kcson`.`ripso_has_serv` (`planned`, `serv_id`, `ripso_id`) VALUES (5648,  151,  5);
INSERT INTO `kcson`.`ripso_has_serv` (`planned`, `serv_id`, `ripso_id`) VALUES (1,  152,  5);
INSERT INTO `kcson`.`ripso_has_serv` (`planned`, `serv_id`, `ripso_id`) VALUES (1,  153,  5);
INSERT INTO `kcson`.`ripso_has_serv` (`planned`, `serv_id`, `ripso_id`) VALUES (365,  163,  5);
INSERT INTO `kcson`.`ripso_has_serv` (`planned`, `serv_id`, `ripso_id`) VALUES (1825,  182,  5);
INSERT INTO `kcson`.`ripso_has_serv` (`planned`, `serv_id`, `ripso_id`) VALUES (365,  183,  5);
INSERT INTO `kcson`.`ripso_has_serv` (`planned`, `serv_id`, `ripso_id`) VALUES (1095,  184,  5);
INSERT INTO `kcson`.`ripso_has_serv` (`planned`, `serv_id`, `ripso_id`) VALUES (365,  185,  5);
INSERT INTO `kcson`.`ripso_has_serv` (`planned`, `serv_id`, `ripso_id`) VALUES (1095,  186,  5);
INSERT INTO `kcson`.`ripso_has_serv` (`planned`, `serv_id`, `ripso_id`) VALUES (50,  187,  5);
INSERT INTO `kcson`.`ripso_has_serv` (`planned`, `serv_id`, `ripso_id`) VALUES (100,  188,  5);
INSERT INTO `kcson`.`ripso_has_serv` (`planned`, `serv_id`, `ripso_id`) VALUES (6,  189,  5);
INSERT INTO `kcson`.`ripso_has_serv` (`planned`, `serv_id`, `ripso_id`) VALUES (365,  190,  5);
INSERT INTO `kcson`.`ripso_has_serv` (`planned`, `serv_id`, `ripso_id`) VALUES (4,  191,  5);
INSERT INTO `kcson`.`ripso_has_serv` (`planned`, `serv_id`, `ripso_id`) VALUES (4,  192,  5);
INSERT INTO `kcson`.`ripso_has_serv` (`planned`, `serv_id`, `ripso_id`) VALUES (1,  196,  5);
INSERT INTO `kcson`.`ripso_has_serv` (`planned`, `serv_id`, `ripso_id`) VALUES (1,  197,  5);
INSERT INTO `kcson`.`ripso_has_serv` (`planned`, `serv_id`, `ripso_id`) VALUES (1,  198,  5);
INSERT INTO `kcson`.`ripso_has_serv` (`planned`, `serv_id`, `ripso_id`) VALUES (1,  199,  5);
INSERT INTO `kcson`.`ripso_has_serv` (`planned`, `serv_id`, `ripso_id`) VALUES (1,  200,  5);
INSERT INTO `kcson`.`ripso_has_serv` (`planned`, `serv_id`, `ripso_id`) VALUES (2,  201,  5);
INSERT INTO `kcson`.`ripso_has_serv` (`planned`, `serv_id`, `ripso_id`) VALUES (1078,  202,  5);
INSERT INTO `kcson`.`ripso_has_serv` (`planned`, `serv_id`, `ripso_id`) VALUES (1,  203,  5);
INSERT INTO `kcson`.`ripso_has_serv` (`planned`, `serv_id`, `ripso_id`) VALUES (365,  204,  5);
INSERT INTO `kcson`.`ripso_has_serv` (`planned`, `serv_id`, `ripso_id`) VALUES (150,  205,  5);
INSERT INTO `kcson`.`ripso_has_serv` (`planned`, `serv_id`, `ripso_id`) VALUES (365,  206,  5);
INSERT INTO `kcson`.`ripso_has_serv` (`planned`, `serv_id`, `ripso_id`) VALUES (50,  208,  5);
INSERT INTO `kcson`.`ripso_has_serv` (`planned`, `serv_id`, `ripso_id`) VALUES (96,  209,  5);
INSERT INTO `kcson`.`ripso_has_serv` (`planned`, `serv_id`, `ripso_id`) VALUES (50,  210,  5);
INSERT INTO `kcson`.`ripso_has_serv` (`planned`, `serv_id`, `ripso_id`) VALUES (1,  211,  5);
INSERT INTO `kcson`.`ripso_has_serv` (`planned`, `serv_id`, `ripso_id`) VALUES (132,  212,  5);
INSERT INTO `kcson`.`ripso_has_serv` (`planned`, `serv_id`, `ripso_id`) VALUES (96,  213,  5);
INSERT INTO `kcson`.`ripso_has_serv` (`planned`, `serv_id`, `ripso_id`) VALUES (24,  214,  5);
INSERT INTO `kcson`.`ripso_has_serv` (`planned`, `serv_id`, `ripso_id`) VALUES (12,  215,  5);
INSERT INTO `kcson`.`ripso_has_serv` (`planned`, `serv_id`, `ripso_id`) VALUES (84,  216,  5);
INSERT INTO `kcson`.`ripso_has_serv` (`planned`, `serv_id`, `ripso_id`) VALUES (12,  226,  5);
INSERT INTO `kcson`.`ripso_has_serv` (`planned`, `serv_id`, `ripso_id`) VALUES (12,  227,  5);
INSERT INTO `kcson`.`ripso_has_serv` (`planned`, `serv_id`, `ripso_id`) VALUES (48,  229,  5);
INSERT INTO `kcson`.`ripso_has_serv` (`planned`, `serv_id`, `ripso_id`) VALUES (12,  231,  5);
INSERT INTO `kcson`.`ripso_has_serv` (`planned`, `serv_id`, `ripso_id`) VALUES (9,  239,  5);
INSERT INTO `kcson`.`ripso_has_serv` (`planned`, `serv_id`, `ripso_id`) VALUES (4,  240,  5);
INSERT INTO `kcson`.`ripso_has_serv` (`planned`, `serv_id`, `ripso_id`) VALUES (1,  241,  5);
INSERT INTO `kcson`.`ripso_has_serv` (`planned`, `serv_id`, `ripso_id`) VALUES (1,  245,  5);
INSERT INTO `kcson`.`ripso_has_serv` (`planned`, `serv_id`, `ripso_id`) VALUES (1,  246,  5);
INSERT INTO `kcson`.`ripso_has_serv` (`planned`, `serv_id`, `ripso_id`) VALUES (1,  250,  5);
INSERT INTO `kcson`.`ripso_has_serv` (`planned`, `serv_id`, `ripso_id`) VALUES (1,  251,  5);
INSERT INTO `kcson`.`ripso_has_serv` (`planned`, `serv_id`, `ripso_id`) VALUES (2,  253,  5);
INSERT INTO `kcson`.`ripso_has_serv` (`planned`, `serv_id`, `ripso_id`) VALUES (1,  254,  5);
INSERT INTO `kcson`.`ripso_has_serv` (`planned`, `serv_id`, `ripso_id`) VALUES (1,  256,  5);
INSERT INTO `kcson`.`ripso_has_serv` (`planned`, `serv_id`, `ripso_id`) VALUES (1395,  1,  6);
INSERT INTO `kcson`.`ripso_has_serv` (`planned`, `serv_id`, `ripso_id`) VALUES (1395,  2,  6);
INSERT INTO `kcson`.`ripso_has_serv` (`planned`, `serv_id`, `ripso_id`) VALUES (901,  3,  6);
INSERT INTO `kcson`.`ripso_has_serv` (`planned`, `serv_id`, `ripso_id`) VALUES (104,  4,  6);
INSERT INTO `kcson`.`ripso_has_serv` (`planned`, `serv_id`, `ripso_id`) VALUES (104,  5,  6);
INSERT INTO `kcson`.`ripso_has_serv` (`planned`, `serv_id`, `ripso_id`) VALUES (156,  6,  6);
INSERT INTO `kcson`.`ripso_has_serv` (`planned`, `serv_id`, `ripso_id`) VALUES (156,  7,  6);
INSERT INTO `kcson`.`ripso_has_serv` (`planned`, `serv_id`, `ripso_id`) VALUES (26,  8,  6);
INSERT INTO `kcson`.`ripso_has_serv` (`planned`, `serv_id`, `ripso_id`) VALUES (156,  9,  6);
INSERT INTO `kcson`.`ripso_has_serv` (`planned`, `serv_id`, `ripso_id`) VALUES (156,  10,  6);
INSERT INTO `kcson`.`ripso_has_serv` (`planned`, `serv_id`, `ripso_id`) VALUES (12,  13,  6);
INSERT INTO `kcson`.`ripso_has_serv` (`planned`, `serv_id`, `ripso_id`) VALUES (12,  14,  6);
INSERT INTO `kcson`.`ripso_has_serv` (`planned`, `serv_id`, `ripso_id`) VALUES (12,  15,  6);
INSERT INTO `kcson`.`ripso_has_serv` (`planned`, `serv_id`, `ripso_id`) VALUES (1,  16,  6);
INSERT INTO `kcson`.`ripso_has_serv` (`planned`, `serv_id`, `ripso_id`) VALUES (1,  29,  6);
INSERT INTO `kcson`.`ripso_has_serv` (`planned`, `serv_id`, `ripso_id`) VALUES (1,  30,  6);
INSERT INTO `kcson`.`ripso_has_serv` (`planned`, `serv_id`, `ripso_id`) VALUES (1,  31,  6);
INSERT INTO `kcson`.`ripso_has_serv` (`planned`, `serv_id`, `ripso_id`) VALUES (1,  32,  6);
INSERT INTO `kcson`.`ripso_has_serv` (`planned`, `serv_id`, `ripso_id`) VALUES (2,  34,  6);
INSERT INTO `kcson`.`ripso_has_serv` (`planned`, `serv_id`, `ripso_id`) VALUES (470,  38,  6);
INSERT INTO `kcson`.`ripso_has_serv` (`planned`, `serv_id`, `ripso_id`) VALUES (2,  39,  6);
INSERT INTO `kcson`.`ripso_has_serv` (`planned`, `serv_id`, `ripso_id`) VALUES (156,  40,  6);
INSERT INTO `kcson`.`ripso_has_serv` (`planned`, `serv_id`, `ripso_id`) VALUES (156,  41,  6);
INSERT INTO `kcson`.`ripso_has_serv` (`planned`, `serv_id`, `ripso_id`) VALUES (156,  42,  6);
INSERT INTO `kcson`.`ripso_has_serv` (`planned`, `serv_id`, `ripso_id`) VALUES (16,  44,  6);
INSERT INTO `kcson`.`ripso_has_serv` (`planned`, `serv_id`, `ripso_id`) VALUES (4,  45,  6);
INSERT INTO `kcson`.`ripso_has_serv` (`planned`, `serv_id`, `ripso_id`) VALUES (12,  46,  6);
INSERT INTO `kcson`.`ripso_has_serv` (`planned`, `serv_id`, `ripso_id`) VALUES (2,  47,  6);
INSERT INTO `kcson`.`ripso_has_serv` (`planned`, `serv_id`, `ripso_id`) VALUES (1,  48,  6);
INSERT INTO `kcson`.`ripso_has_serv` (`planned`, `serv_id`, `ripso_id`) VALUES (1,  49,  6);
INSERT INTO `kcson`.`ripso_has_serv` (`planned`, `serv_id`, `ripso_id`) VALUES (4,  53,  6);
INSERT INTO `kcson`.`ripso_has_serv` (`planned`, `serv_id`, `ripso_id`) VALUES (1,  54,  6);
INSERT INTO `kcson`.`ripso_has_serv` (`planned`, `serv_id`, `ripso_id`) VALUES (1,  56,  6);
INSERT INTO `kcson`.`ripso_has_serv` (`planned`, `serv_id`, `ripso_id`) VALUES (1,  58,  6);
INSERT INTO `kcson`.`ripso_has_serv` (`planned`, `serv_id`, `ripso_id`) VALUES (1,  59,  6);
INSERT INTO `kcson`.`ripso_has_serv` (`planned`, `serv_id`, `ripso_id`) VALUES (2,  60,  6);
INSERT INTO `kcson`.`ripso_has_serv` (`planned`, `serv_id`, `ripso_id`) VALUES (1,  61,  6);
INSERT INTO `kcson`.`ripso_has_serv` (`planned`, `serv_id`, `ripso_id`) VALUES (1,  62,  6);
INSERT INTO `kcson`.`ripso_has_serv` (`planned`, `serv_id`, `ripso_id`) VALUES (518,  1,  7);
INSERT INTO `kcson`.`ripso_has_serv` (`planned`, `serv_id`, `ripso_id`) VALUES (518,  64,  7);
INSERT INTO `kcson`.`ripso_has_serv` (`planned`, `serv_id`, `ripso_id`) VALUES (4,  65,  7);
INSERT INTO `kcson`.`ripso_has_serv` (`planned`, `serv_id`, `ripso_id`) VALUES (1,  95,  7);
INSERT INTO `kcson`.`ripso_has_serv` (`planned`, `serv_id`, `ripso_id`) VALUES (1,  96,  7);
INSERT INTO `kcson`.`ripso_has_serv` (`planned`, `serv_id`, `ripso_id`) VALUES (2,  97,  7);
INSERT INTO `kcson`.`ripso_has_serv` (`planned`, `serv_id`, `ripso_id`) VALUES (162,  98,  7);
INSERT INTO `kcson`.`ripso_has_serv` (`planned`, `serv_id`, `ripso_id`) VALUES (4,  99,  7);
INSERT INTO `kcson`.`ripso_has_serv` (`planned`, `serv_id`, `ripso_id`) VALUES (10,  101,  7);
INSERT INTO `kcson`.`ripso_has_serv` (`planned`, `serv_id`, `ripso_id`) VALUES (4,  103,  7);
INSERT INTO `kcson`.`ripso_has_serv` (`planned`, `serv_id`, `ripso_id`) VALUES (48,  104,  7);
INSERT INTO `kcson`.`ripso_has_serv` (`planned`, `serv_id`, `ripso_id`) VALUES (96,  105,  7);
INSERT INTO `kcson`.`ripso_has_serv` (`planned`, `serv_id`, `ripso_id`) VALUES (52,  107,  7);
INSERT INTO `kcson`.`ripso_has_serv` (`planned`, `serv_id`, `ripso_id`) VALUES (16,  108,  7);
INSERT INTO `kcson`.`ripso_has_serv` (`planned`, `serv_id`, `ripso_id`) VALUES (12,  109,  7);
INSERT INTO `kcson`.`ripso_has_serv` (`planned`, `serv_id`, `ripso_id`) VALUES (24,  110,  7);
INSERT INTO `kcson`.`ripso_has_serv` (`planned`, `serv_id`, `ripso_id`) VALUES (290,  111,  7);
INSERT INTO `kcson`.`ripso_has_serv` (`planned`, `serv_id`, `ripso_id`) VALUES (2,  112,  7);
INSERT INTO `kcson`.`ripso_has_serv` (`planned`, `serv_id`, `ripso_id`) VALUES (48,  122,  7);
INSERT INTO `kcson`.`ripso_has_serv` (`planned`, `serv_id`, `ripso_id`) VALUES (120,  123,  7);
INSERT INTO `kcson`.`ripso_has_serv` (`planned`, `serv_id`, `ripso_id`) VALUES (24,  124,  7);
INSERT INTO `kcson`.`ripso_has_serv` (`planned`, `serv_id`, `ripso_id`) VALUES (96,  125,  7);
INSERT INTO `kcson`.`ripso_has_serv` (`planned`, `serv_id`, `ripso_id`) VALUES (5,  134,  7);
INSERT INTO `kcson`.`ripso_has_serv` (`planned`, `serv_id`, `ripso_id`) VALUES (1,  135,  7);
INSERT INTO `kcson`.`ripso_has_serv` (`planned`, `serv_id`, `ripso_id`) VALUES (1,  136,  7);
INSERT INTO `kcson`.`ripso_has_serv` (`planned`, `serv_id`, `ripso_id`) VALUES (1,  140,  7);
INSERT INTO `kcson`.`ripso_has_serv` (`planned`, `serv_id`, `ripso_id`) VALUES (1,  142,  7);
INSERT INTO `kcson`.`ripso_has_serv` (`planned`, `serv_id`, `ripso_id`) VALUES (1,  143,  7);
INSERT INTO `kcson`.`ripso_has_serv` (`planned`, `serv_id`, `ripso_id`) VALUES (5,  144,  7);
INSERT INTO `kcson`.`ripso_has_serv` (`planned`, `serv_id`, `ripso_id`) VALUES (1,  145,  7);
INSERT INTO `kcson`.`ripso_has_serv` (`planned`, `serv_id`, `ripso_id`) VALUES (1,  146,  7);
INSERT INTO `kcson`.`ripso_has_serv` (`planned`, `serv_id`, `ripso_id`) VALUES (1,  147,  7);
INSERT INTO `kcson`.`ripso_has_serv` (`planned`, `serv_id`, `ripso_id`) VALUES (1,  148,  7);
INSERT INTO `kcson`.`ripso_has_serv` (`planned`, `serv_id`, `ripso_id`) VALUES (1,  149,  7);
INSERT INTO `kcson`.`ripso_has_serv` (`planned`, `serv_id`, `ripso_id`) VALUES (237,  1,  8);
INSERT INTO `kcson`.`ripso_has_serv` (`planned`, `serv_id`, `ripso_id`) VALUES (237,  64,  8);
INSERT INTO `kcson`.`ripso_has_serv` (`planned`, `serv_id`, `ripso_id`) VALUES (47,  65,  8);
INSERT INTO `kcson`.`ripso_has_serv` (`planned`, `serv_id`, `ripso_id`) VALUES (1,  66,  8);
INSERT INTO `kcson`.`ripso_has_serv` (`planned`, `serv_id`, `ripso_id`) VALUES (44,  69,  8);
INSERT INTO `kcson`.`ripso_has_serv` (`planned`, `serv_id`, `ripso_id`) VALUES (1,  91,  8);
INSERT INTO `kcson`.`ripso_has_serv` (`planned`, `serv_id`, `ripso_id`) VALUES (1,  97,  8);
INSERT INTO `kcson`.`ripso_has_serv` (`planned`, `serv_id`, `ripso_id`) VALUES (98,  98,  8);
INSERT INTO `kcson`.`ripso_has_serv` (`planned`, `serv_id`, `ripso_id`) VALUES (1,  99,  8);
INSERT INTO `kcson`.`ripso_has_serv` (`planned`, `serv_id`, `ripso_id`) VALUES (44,  100,  8);
INSERT INTO `kcson`.`ripso_has_serv` (`planned`, `serv_id`, `ripso_id`) VALUES (20,  101,  8);
INSERT INTO `kcson`.`ripso_has_serv` (`planned`, `serv_id`, `ripso_id`) VALUES (1,  103,  8);
INSERT INTO `kcson`.`ripso_has_serv` (`planned`, `serv_id`, `ripso_id`) VALUES (16,  104,  8);
INSERT INTO `kcson`.`ripso_has_serv` (`planned`, `serv_id`, `ripso_id`) VALUES (16,  105,  8);
INSERT INTO `kcson`.`ripso_has_serv` (`planned`, `serv_id`, `ripso_id`) VALUES (18,  107,  8);
INSERT INTO `kcson`.`ripso_has_serv` (`planned`, `serv_id`, `ripso_id`) VALUES (2,  108,  8);
INSERT INTO `kcson`.`ripso_has_serv` (`planned`, `serv_id`, `ripso_id`) VALUES (4,  109,  8);
INSERT INTO `kcson`.`ripso_has_serv` (`planned`, `serv_id`, `ripso_id`) VALUES (12,  110,  8);
INSERT INTO `kcson`.`ripso_has_serv` (`planned`, `serv_id`, `ripso_id`) VALUES (69,  111,  8);
INSERT INTO `kcson`.`ripso_has_serv` (`planned`, `serv_id`, `ripso_id`) VALUES (1,  113,  8);
INSERT INTO `kcson`.`ripso_has_serv` (`planned`, `serv_id`, `ripso_id`) VALUES (8,  122,  8);
INSERT INTO `kcson`.`ripso_has_serv` (`planned`, `serv_id`, `ripso_id`) VALUES (20,  123,  8);
INSERT INTO `kcson`.`ripso_has_serv` (`planned`, `serv_id`, `ripso_id`) VALUES (24,  124,  8);
INSERT INTO `kcson`.`ripso_has_serv` (`planned`, `serv_id`, `ripso_id`) VALUES (16,  125,  8);
INSERT INTO `kcson`.`ripso_has_serv` (`planned`, `serv_id`, `ripso_id`) VALUES (3,  134,  8);
INSERT INTO `kcson`.`ripso_has_serv` (`planned`, `serv_id`, `ripso_id`) VALUES (1,  135,  8);
INSERT INTO `kcson`.`ripso_has_serv` (`planned`, `serv_id`, `ripso_id`) VALUES (1,  142,  8);
INSERT INTO `kcson`.`ripso_has_serv` (`planned`, `serv_id`, `ripso_id`) VALUES (1,  143,  8);
INSERT INTO `kcson`.`ripso_has_serv` (`planned`, `serv_id`, `ripso_id`) VALUES (2,  144,  8);
INSERT INTO `kcson`.`ripso_has_serv` (`planned`, `serv_id`, `ripso_id`) VALUES (1,  145,  8);
INSERT INTO `kcson`.`ripso_has_serv` (`planned`, `serv_id`, `ripso_id`) VALUES (1,  149,  8);
INSERT INTO `kcson`.`ripso_has_serv` (`planned`, `serv_id`, `ripso_id`) VALUES (1188,  1,  9);
INSERT INTO `kcson`.`ripso_has_serv` (`planned`, `serv_id`, `ripso_id`) VALUES (1188,  150,  9);
INSERT INTO `kcson`.`ripso_has_serv` (`planned`, `serv_id`, `ripso_id`) VALUES (858,  151,  9);
INSERT INTO `kcson`.`ripso_has_serv` (`planned`, `serv_id`, `ripso_id`) VALUES (1,  152,  9);
INSERT INTO `kcson`.`ripso_has_serv` (`planned`, `serv_id`, `ripso_id`) VALUES (1,  153,  9);
INSERT INTO `kcson`.`ripso_has_serv` (`planned`, `serv_id`, `ripso_id`) VALUES (90,  163,  9);
INSERT INTO `kcson`.`ripso_has_serv` (`planned`, `serv_id`, `ripso_id`) VALUES (270,  182,  9);
INSERT INTO `kcson`.`ripso_has_serv` (`planned`, `serv_id`, `ripso_id`) VALUES (90,  183,  9);
INSERT INTO `kcson`.`ripso_has_serv` (`planned`, `serv_id`, `ripso_id`) VALUES (90,  185,  9);
INSERT INTO `kcson`.`ripso_has_serv` (`planned`, `serv_id`, `ripso_id`) VALUES (180,  186,  9);
INSERT INTO `kcson`.`ripso_has_serv` (`planned`, `serv_id`, `ripso_id`) VALUES (12,  187,  9);
INSERT INTO `kcson`.`ripso_has_serv` (`planned`, `serv_id`, `ripso_id`) VALUES (30,  188,  9);
INSERT INTO `kcson`.`ripso_has_serv` (`planned`, `serv_id`, `ripso_id`) VALUES (90,  190,  9);
INSERT INTO `kcson`.`ripso_has_serv` (`planned`, `serv_id`, `ripso_id`) VALUES (1,  191,  9);
INSERT INTO `kcson`.`ripso_has_serv` (`planned`, `serv_id`, `ripso_id`) VALUES (1,  192,  9);
INSERT INTO `kcson`.`ripso_has_serv` (`planned`, `serv_id`, `ripso_id`) VALUES (1,  198,  9);
INSERT INTO `kcson`.`ripso_has_serv` (`planned`, `serv_id`, `ripso_id`) VALUES (1,  201,  9);
INSERT INTO `kcson`.`ripso_has_serv` (`planned`, `serv_id`, `ripso_id`) VALUES (256,  202,  9);
INSERT INTO `kcson`.`ripso_has_serv` (`planned`, `serv_id`, `ripso_id`) VALUES (90,  204,  9);
INSERT INTO `kcson`.`ripso_has_serv` (`planned`, `serv_id`, `ripso_id`) VALUES (30,  205,  9);
INSERT INTO `kcson`.`ripso_has_serv` (`planned`, `serv_id`, `ripso_id`) VALUES (90,  206,  9);
INSERT INTO `kcson`.`ripso_has_serv` (`planned`, `serv_id`, `ripso_id`) VALUES (2,  208,  9);
INSERT INTO `kcson`.`ripso_has_serv` (`planned`, `serv_id`, `ripso_id`) VALUES (8,  209,  9);
INSERT INTO `kcson`.`ripso_has_serv` (`planned`, `serv_id`, `ripso_id`) VALUES (36,  210,  9);
INSERT INTO `kcson`.`ripso_has_serv` (`planned`, `serv_id`, `ripso_id`) VALUES (18,  212,  9);
INSERT INTO `kcson`.`ripso_has_serv` (`planned`, `serv_id`, `ripso_id`) VALUES (12,  213,  9);
INSERT INTO `kcson`.`ripso_has_serv` (`planned`, `serv_id`, `ripso_id`) VALUES (6,  214,  9);
INSERT INTO `kcson`.`ripso_has_serv` (`planned`, `serv_id`, `ripso_id`) VALUES (48,  216,  9);
INSERT INTO `kcson`.`ripso_has_serv` (`planned`, `serv_id`, `ripso_id`) VALUES (12,  226,  9);
INSERT INTO `kcson`.`ripso_has_serv` (`planned`, `serv_id`, `ripso_id`) VALUES (12,  227,  9);
INSERT INTO `kcson`.`ripso_has_serv` (`planned`, `serv_id`, `ripso_id`) VALUES (24,  229,  9);
INSERT INTO `kcson`.`ripso_has_serv` (`planned`, `serv_id`, `ripso_id`) VALUES (6,  239,  9);
INSERT INTO `kcson`.`ripso_has_serv` (`planned`, `serv_id`, `ripso_id`) VALUES (1,  240,  9);
INSERT INTO `kcson`.`ripso_has_serv` (`planned`, `serv_id`, `ripso_id`) VALUES (1,  241,  9);
INSERT INTO `kcson`.`ripso_has_serv` (`planned`, `serv_id`, `ripso_id`) VALUES (1,  245,  9);
INSERT INTO `kcson`.`ripso_has_serv` (`planned`, `serv_id`, `ripso_id`) VALUES (1,  246,  9);
INSERT INTO `kcson`.`ripso_has_serv` (`planned`, `serv_id`, `ripso_id`) VALUES (1,  251,  9);
INSERT INTO `kcson`.`ripso_has_serv` (`planned`, `serv_id`, `ripso_id`) VALUES (1,  252,  9);
INSERT INTO `kcson`.`ripso_has_serv` (`planned`, `serv_id`, `ripso_id`) VALUES (2,  253,  9);
INSERT INTO `kcson`.`ripso_has_serv` (`planned`, `serv_id`, `ripso_id`) VALUES (1,  254,  9);
INSERT INTO `kcson`.`ripso_has_serv` (`planned`, `serv_id`, `ripso_id`) VALUES (1,  255,  9);
INSERT INTO `kcson`.`ripso_has_serv` (`planned`, `serv_id`, `ripso_id`) VALUES (1664,  1,  10);
INSERT INTO `kcson`.`ripso_has_serv` (`planned`, `serv_id`, `ripso_id`) VALUES (1664,  2,  10);
INSERT INTO `kcson`.`ripso_has_serv` (`planned`, `serv_id`, `ripso_id`) VALUES (1112,  3,  10);
INSERT INTO `kcson`.`ripso_has_serv` (`planned`, `serv_id`, `ripso_id`) VALUES (104,  4,  10);
INSERT INTO `kcson`.`ripso_has_serv` (`planned`, `serv_id`, `ripso_id`) VALUES (156,  5,  10);
INSERT INTO `kcson`.`ripso_has_serv` (`planned`, `serv_id`, `ripso_id`) VALUES (156,  6,  10);
INSERT INTO `kcson`.`ripso_has_serv` (`planned`, `serv_id`, `ripso_id`) VALUES (156,  7,  10);
INSERT INTO `kcson`.`ripso_has_serv` (`planned`, `serv_id`, `ripso_id`) VALUES (52,  8,  10);
INSERT INTO `kcson`.`ripso_has_serv` (`planned`, `serv_id`, `ripso_id`) VALUES (156,  9,  10);
INSERT INTO `kcson`.`ripso_has_serv` (`planned`, `serv_id`, `ripso_id`) VALUES (156,  10,  10);
INSERT INTO `kcson`.`ripso_has_serv` (`planned`, `serv_id`, `ripso_id`) VALUES (12,  11,  10);
INSERT INTO `kcson`.`ripso_has_serv` (`planned`, `serv_id`, `ripso_id`) VALUES (26,  12,  10);
INSERT INTO `kcson`.`ripso_has_serv` (`planned`, `serv_id`, `ripso_id`) VALUES (12,  13,  10);
INSERT INTO `kcson`.`ripso_has_serv` (`planned`, `serv_id`, `ripso_id`) VALUES (12,  14,  10);
INSERT INTO `kcson`.`ripso_has_serv` (`planned`, `serv_id`, `ripso_id`) VALUES (12,  15,  10);
INSERT INTO `kcson`.`ripso_has_serv` (`planned`, `serv_id`, `ripso_id`) VALUES (1,  16,  10);
INSERT INTO `kcson`.`ripso_has_serv` (`planned`, `serv_id`, `ripso_id`) VALUES (1,  17,  10);
INSERT INTO `kcson`.`ripso_has_serv` (`planned`, `serv_id`, `ripso_id`) VALUES (12,  18,  10);
INSERT INTO `kcson`.`ripso_has_serv` (`planned`, `serv_id`, `ripso_id`) VALUES (1,  22,  10);
INSERT INTO `kcson`.`ripso_has_serv` (`planned`, `serv_id`, `ripso_id`) VALUES (12,  23,  10);
INSERT INTO `kcson`.`ripso_has_serv` (`planned`, `serv_id`, `ripso_id`) VALUES (12,  25,  10);
INSERT INTO `kcson`.`ripso_has_serv` (`planned`, `serv_id`, `ripso_id`) VALUES (2,  26,  10);
INSERT INTO `kcson`.`ripso_has_serv` (`planned`, `serv_id`, `ripso_id`) VALUES (2,  27,  10);
INSERT INTO `kcson`.`ripso_has_serv` (`planned`, `serv_id`, `ripso_id`) VALUES (52,  28,  10);
INSERT INTO `kcson`.`ripso_has_serv` (`planned`, `serv_id`, `ripso_id`) VALUES (1,  29,  10);
INSERT INTO `kcson`.`ripso_has_serv` (`planned`, `serv_id`, `ripso_id`) VALUES (1,  30,  10);
INSERT INTO `kcson`.`ripso_has_serv` (`planned`, `serv_id`, `ripso_id`) VALUES (1,  31,  10);
INSERT INTO `kcson`.`ripso_has_serv` (`planned`, `serv_id`, `ripso_id`) VALUES (1,  32,  10);
INSERT INTO `kcson`.`ripso_has_serv` (`planned`, `serv_id`, `ripso_id`) VALUES (1,  33,  10);
INSERT INTO `kcson`.`ripso_has_serv` (`planned`, `serv_id`, `ripso_id`) VALUES (2,  34,  10);
INSERT INTO `kcson`.`ripso_has_serv` (`planned`, `serv_id`, `ripso_id`) VALUES (473,  38,  10);
INSERT INTO `kcson`.`ripso_has_serv` (`planned`, `serv_id`, `ripso_id`) VALUES (1,  39,  10);
INSERT INTO `kcson`.`ripso_has_serv` (`planned`, `serv_id`, `ripso_id`) VALUES (156,  40,  10);
INSERT INTO `kcson`.`ripso_has_serv` (`planned`, `serv_id`, `ripso_id`) VALUES (156,  41,  10);
INSERT INTO `kcson`.`ripso_has_serv` (`planned`, `serv_id`, `ripso_id`) VALUES (156,  42,  10);
INSERT INTO `kcson`.`ripso_has_serv` (`planned`, `serv_id`, `ripso_id`) VALUES (4,  43,  10);
INSERT INTO `kcson`.`ripso_has_serv` (`planned`, `serv_id`, `ripso_id`) VALUES (16,  44,  10);
INSERT INTO `kcson`.`ripso_has_serv` (`planned`, `serv_id`, `ripso_id`) VALUES (4,  45,  10);
INSERT INTO `kcson`.`ripso_has_serv` (`planned`, `serv_id`, `ripso_id`) VALUES (12,  46,  10);
INSERT INTO `kcson`.`ripso_has_serv` (`planned`, `serv_id`, `ripso_id`) VALUES (54,  47,  10);
INSERT INTO `kcson`.`ripso_has_serv` (`planned`, `serv_id`, `ripso_id`) VALUES (1,  48,  10);
INSERT INTO `kcson`.`ripso_has_serv` (`planned`, `serv_id`, `ripso_id`) VALUES (1,  49,  10);
INSERT INTO `kcson`.`ripso_has_serv` (`planned`, `serv_id`, `ripso_id`) VALUES (52,  50,  10);
INSERT INTO `kcson`.`ripso_has_serv` (`planned`, `serv_id`, `ripso_id`) VALUES (1,  51,  10);
INSERT INTO `kcson`.`ripso_has_serv` (`planned`, `serv_id`, `ripso_id`) VALUES (1,  52,  10);
INSERT INTO `kcson`.`ripso_has_serv` (`planned`, `serv_id`, `ripso_id`) VALUES (5,  53,  10);
INSERT INTO `kcson`.`ripso_has_serv` (`planned`, `serv_id`, `ripso_id`) VALUES (1,  54,  10);
INSERT INTO `kcson`.`ripso_has_serv` (`planned`, `serv_id`, `ripso_id`) VALUES (1,  55,  10);
INSERT INTO `kcson`.`ripso_has_serv` (`planned`, `serv_id`, `ripso_id`) VALUES (1,  56,  10);
INSERT INTO `kcson`.`ripso_has_serv` (`planned`, `serv_id`, `ripso_id`) VALUES (1,  58,  10);
INSERT INTO `kcson`.`ripso_has_serv` (`planned`, `serv_id`, `ripso_id`) VALUES (1,  59,  10);
INSERT INTO `kcson`.`ripso_has_serv` (`planned`, `serv_id`, `ripso_id`) VALUES (3,  60,  10);
INSERT INTO `kcson`.`ripso_has_serv` (`planned`, `serv_id`, `ripso_id`) VALUES (1,  61,  10);
INSERT INTO `kcson`.`ripso_has_serv` (`planned`, `serv_id`, `ripso_id`) VALUES (1,  62,  10);
INSERT INTO `kcson`.`ripso_has_serv` (`planned`, `serv_id`, `ripso_id`) VALUES (1,  63,  10);
INSERT INTO `kcson`.`ripso_has_serv` (`planned`, `serv_id`, `ripso_id`) VALUES (81,  1,  11);
INSERT INTO `kcson`.`ripso_has_serv` (`planned`, `serv_id`, `ripso_id`) VALUES (81,  64,  11);
INSERT INTO `kcson`.`ripso_has_serv` (`planned`, `serv_id`, `ripso_id`) VALUES (55,  65,  11);
INSERT INTO `kcson`.`ripso_has_serv` (`planned`, `serv_id`, `ripso_id`) VALUES (52,  85,  11);
INSERT INTO `kcson`.`ripso_has_serv` (`planned`, `serv_id`, `ripso_id`) VALUES (1,  91,  11);
INSERT INTO `kcson`.`ripso_has_serv` (`planned`, `serv_id`, `ripso_id`) VALUES (2,  96,  11);
INSERT INTO `kcson`.`ripso_has_serv` (`planned`, `serv_id`, `ripso_id`) VALUES (10,  98,  11);
INSERT INTO `kcson`.`ripso_has_serv` (`planned`, `serv_id`, `ripso_id`) VALUES (6,  99,  11);
INSERT INTO `kcson`.`ripso_has_serv` (`planned`, `serv_id`, `ripso_id`) VALUES (2,  103,  11);
INSERT INTO `kcson`.`ripso_has_serv` (`planned`, `serv_id`, `ripso_id`) VALUES (2,  106,  11);
INSERT INTO `kcson`.`ripso_has_serv` (`planned`, `serv_id`, `ripso_id`) VALUES (6,  107,  11);
INSERT INTO `kcson`.`ripso_has_serv` (`planned`, `serv_id`, `ripso_id`) VALUES (6,  108,  11);
INSERT INTO `kcson`.`ripso_has_serv` (`planned`, `serv_id`, `ripso_id`) VALUES (1,  126,  11);
INSERT INTO `kcson`.`ripso_has_serv` (`planned`, `serv_id`, `ripso_id`) VALUES (1,  132,  11);
INSERT INTO `kcson`.`ripso_has_serv` (`planned`, `serv_id`, `ripso_id`) VALUES (8,  134,  11);
INSERT INTO `kcson`.`ripso_has_serv` (`planned`, `serv_id`, `ripso_id`) VALUES (2,  135,  11);
INSERT INTO `kcson`.`ripso_has_serv` (`planned`, `serv_id`, `ripso_id`) VALUES (1,  136,  11);
INSERT INTO `kcson`.`ripso_has_serv` (`planned`, `serv_id`, `ripso_id`) VALUES (1,  140,  11);
INSERT INTO `kcson`.`ripso_has_serv` (`planned`, `serv_id`, `ripso_id`) VALUES (1,  141,  11);
INSERT INTO `kcson`.`ripso_has_serv` (`planned`, `serv_id`, `ripso_id`) VALUES (2,  142,  11);
INSERT INTO `kcson`.`ripso_has_serv` (`planned`, `serv_id`, `ripso_id`) VALUES (1,  143,  11);
INSERT INTO `kcson`.`ripso_has_serv` (`planned`, `serv_id`, `ripso_id`) VALUES (1,  144,  11);
INSERT INTO `kcson`.`ripso_has_serv` (`planned`, `serv_id`, `ripso_id`) VALUES (1,  147,  11);
INSERT INTO `kcson`.`ripso_has_serv` (`planned`, `serv_id`, `ripso_id`) VALUES (1327,  1,  12);
INSERT INTO `kcson`.`ripso_has_serv` (`planned`, `serv_id`, `ripso_id`) VALUES (1327,  64,  12);
INSERT INTO `kcson`.`ripso_has_serv` (`planned`, `serv_id`, `ripso_id`) VALUES (904,  65,  12);
INSERT INTO `kcson`.`ripso_has_serv` (`planned`, `serv_id`, `ripso_id`) VALUES (1,  66,  12);
INSERT INTO `kcson`.`ripso_has_serv` (`planned`, `serv_id`, `ripso_id`) VALUES (1,  68,  12);
INSERT INTO `kcson`.`ripso_has_serv` (`planned`, `serv_id`, `ripso_id`) VALUES (180,  84,  12);
INSERT INTO `kcson`.`ripso_has_serv` (`planned`, `serv_id`, `ripso_id`) VALUES (360,  88,  12);
INSERT INTO `kcson`.`ripso_has_serv` (`planned`, `serv_id`, `ripso_id`) VALUES (360,  90,  12);
INSERT INTO `kcson`.`ripso_has_serv` (`planned`, `serv_id`, `ripso_id`) VALUES (1,  96,  12);
INSERT INTO `kcson`.`ripso_has_serv` (`planned`, `serv_id`, `ripso_id`) VALUES (1,  97,  12);
INSERT INTO `kcson`.`ripso_has_serv` (`planned`, `serv_id`, `ripso_id`) VALUES (379,  98,  12);
INSERT INTO `kcson`.`ripso_has_serv` (`planned`, `serv_id`, `ripso_id`) VALUES (6,  99,  12);
INSERT INTO `kcson`.`ripso_has_serv` (`planned`, `serv_id`, `ripso_id`) VALUES (180,  100,  12);
INSERT INTO `kcson`.`ripso_has_serv` (`planned`, `serv_id`, `ripso_id`) VALUES (180,  102,  12);
INSERT INTO `kcson`.`ripso_has_serv` (`planned`, `serv_id`, `ripso_id`) VALUES (12,  103,  12);
INSERT INTO `kcson`.`ripso_has_serv` (`planned`, `serv_id`, `ripso_id`) VALUES (1,  106,  12);
INSERT INTO `kcson`.`ripso_has_serv` (`planned`, `serv_id`, `ripso_id`) VALUES (34,  107,  12);
INSERT INTO `kcson`.`ripso_has_serv` (`planned`, `serv_id`, `ripso_id`) VALUES (26,  108,  12);
INSERT INTO `kcson`.`ripso_has_serv` (`planned`, `serv_id`, `ripso_id`) VALUES (8,  110,  12);
INSERT INTO `kcson`.`ripso_has_serv` (`planned`, `serv_id`, `ripso_id`) VALUES (1,  126,  12);
INSERT INTO `kcson`.`ripso_has_serv` (`planned`, `serv_id`, `ripso_id`) VALUES (1,  132,  12);
INSERT INTO `kcson`.`ripso_has_serv` (`planned`, `serv_id`, `ripso_id`) VALUES (8,  134,  12);
INSERT INTO `kcson`.`ripso_has_serv` (`planned`, `serv_id`, `ripso_id`) VALUES (2,  135,  12);
INSERT INTO `kcson`.`ripso_has_serv` (`planned`, `serv_id`, `ripso_id`) VALUES (1,  136,  12);
INSERT INTO `kcson`.`ripso_has_serv` (`planned`, `serv_id`, `ripso_id`) VALUES (1,  140,  12);
INSERT INTO `kcson`.`ripso_has_serv` (`planned`, `serv_id`, `ripso_id`) VALUES (1,  141,  12);
INSERT INTO `kcson`.`ripso_has_serv` (`planned`, `serv_id`, `ripso_id`) VALUES (2,  142,  12);
INSERT INTO `kcson`.`ripso_has_serv` (`planned`, `serv_id`, `ripso_id`) VALUES (1,  143,  12);
INSERT INTO `kcson`.`ripso_has_serv` (`planned`, `serv_id`, `ripso_id`) VALUES (1,  144,  12);
INSERT INTO `kcson`.`ripso_has_serv` (`planned`, `serv_id`, `ripso_id`) VALUES (1,  147,  12);

COMMIT;


-- -----------------------------------------------------
-- Data for table `kcson`.`dep_has_ripso`
-- -----------------------------------------------------
START TRANSACTION;
USE `kcson`;
INSERT INTO `kcson`.`dep_has_ripso` (`dep_id`, `ripso_id`) VALUES (1, 1);

COMMIT;


-- -----------------------------------------------------
-- Data for table `kcson`.`ufio_has_category`
-- -----------------------------------------------------
START TRANSACTION;
USE `kcson`;
INSERT INTO `kcson`.`ufio_has_category` (`ufio_id`, `category_id`, `get_date`, `archive`, `prim`, `create`, `ts`, `cr_by`, `upd_by`) VALUES (1, 1, NULL, NULL, '4113', NULL, NULL, NULL, NULL);
INSERT INTO `kcson`.`ufio_has_category` (`ufio_id`, `category_id`, `get_date`, `archive`, `prim`, `create`, `ts`, `cr_by`, `upd_by`) VALUES (1, 2, NULL, NULL, NULL, NULL, NULL, NULL, NULL);
INSERT INTO `kcson`.`ufio_has_category` (`ufio_id`, `category_id`, `get_date`, `archive`, `prim`, `create`, `ts`, `cr_by`, `upd_by`) VALUES (1, 5, NULL, NULL, NULL, NULL, NULL, NULL, NULL);
INSERT INTO `kcson`.`ufio_has_category` (`ufio_id`, `category_id`, `get_date`, `archive`, `prim`, `create`, `ts`, `cr_by`, `upd_by`) VALUES (2, 6, NULL, NULL, NULL, NULL, NULL, NULL, NULL);
INSERT INTO `kcson`.`ufio_has_category` (`ufio_id`, `category_id`, `get_date`, `archive`, `prim`, `create`, `ts`, `cr_by`, `upd_by`) VALUES (2, 1, NULL, NULL, NULL, NULL, NULL, NULL, NULL);

COMMIT;


-- -----------------------------------------------------
-- Data for table `kcson`.`stub_model`
-- -----------------------------------------------------
START TRANSACTION;
USE `kcson`;
INSERT INTO `kcson`.`stub_model` (`id`, `msg`, `msg1`) VALUES (1, 'Данная таблица еще не готова', '');
INSERT INTO `kcson`.`stub_model` (`id`, `msg`, `msg1`) VALUES (2, 'This model didn\'t ready yet', NULL);

COMMIT;


-- -----------------------------------------------------
-- Data for table `kcson`.`ui_select_fiolist`
-- -----------------------------------------------------
START TRANSACTION;
USE `kcson`;
INSERT INTO `kcson`.`ui_select_fiolist` (`id`, `list_name`, `sql_table`, `col`, `orderby`, `prim`) VALUES (1, 'Обслуживаются на отделении', '_dep_has_ufio', 1, 1, NULL);

COMMIT;


-- -----------------------------------------------------
-- Data for table `kcson`.`complex_dep`
-- -----------------------------------------------------
START TRANSACTION;
USE `kcson`;
INSERT INTO `kcson`.`complex_dep` (`id`, `complex_dep`, `note`) VALUES (1, 'Все отделения организации', NULL);
INSERT INTO `kcson`.`complex_dep` (`id`, `complex_dep`, `note`) VALUES (2, 'СОСМОДЫ', NULL);
INSERT INTO `kcson`.`complex_dep` (`id`, `complex_dep`, `note`) VALUES (3, 'Полустационарные отделения', NULL);
INSERT INTO `kcson`.`complex_dep` (`id`, `complex_dep`, `note`) VALUES (4, 'Стационарные отделения', NULL);
INSERT INTO `kcson`.`complex_dep` (`id`, `complex_dep`, `note`) VALUES (5, 'Отделения на дому', NULL);
INSERT INTO `kcson`.`complex_dep` (`id`, `complex_dep`, `note`) VALUES (6, 'Срочные отделения', NULL);

COMMIT;


SET SQL_MODE=@OLD_SQL_MODE;
SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS;
SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS;
