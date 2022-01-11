USE `kcson`;

select * from kcson.role;
# show tables;

# KNOWN ISSUES
# all user connection will be disconnected then user chang department - to immediatly force revoke role privileges


#############################
# routine GET_PRIVILEGES
# ---------------------------
drop procedure IF EXISTS INIT_SECURITY;
delimiter $$
create procedure INIT_SECURITY()
    SQL SECURITY DEFINER
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

    grant select on kcson._bm_dep_has_ufio to info;
    grant select on kcson._bm_dep_has_ufio_other_year to info;
    grant select on kcson._bm_dep_has_ufio_year to info;
    grant select on kcson._categ_list_ufio to info;
    grant select on kcson._contr_has_main to info;
    grant select on kcson._contr_has_serv_predv to info;
    grant select on kcson._contracts to info;
    grant select on kcson._contracts_has_serv to info;
    grant select on kcson._dep_has_contracts to info;
    grant select on kcson._dep_has_main to info;
    grant select on kcson._dep_has_new_ufio to info;
    grant select on kcson._dep_has_ripso to info;
    grant select on kcson._dep_has_ufio to info;
    grant select on kcson._dep_has_ufio_blocked_in_year to info;
    grant select on kcson._dep_has_ufio_by_ripso to info;
    grant select on kcson._dep_has_ufio_contracts to info;
    grant select on kcson._dep_has_ufio_count_2month to info;
    grant select on kcson._dep_has_ufio_count_main_year to info;
    grant select on kcson._dep_has_ufio_count_month to info;
    grant select on kcson._dep_has_ufio_ended to info;
    grant select on kcson._dep_has_ufio_ending to info;
    grant select on kcson._dep_has_ufio_ripso to info;
    grant select on kcson._dep_has_ufio_ripso_or_contracts to info;
    grant select on kcson._dep_has_ufio_year to info;
    grant select on kcson._dep_has_worker to info;
    grant select on kcson._g_categ_list_ufio_for_dep_for_year to info;
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
    grant select on kcson._ufio to info;
    grant select on kcson._ufio_has_category_for_last_ufio to info;
    grant select on kcson._ufio_has_contracts to info; # TODO: delete this
    grant select on kcson._ufio_has_invalid_contracts to info;
    grant select on kcson._ufio_has_main to info;
    grant select on kcson._ufio_has_valid_contracts to info;
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
    grant select on kcson.dep_has_ufio_by_contr to info;
    grant select on kcson.dep_has_ufio_by_ripso to info;
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
    grant select on kcson.permiss to info;
    grant select on kcson.rdata to info;
    grant select on kcson.rdep to info;
    grant select on kcson.ripso to info;
    grant select on kcson.ripso_has_serv to info;
    grant select on kcson.rname to info;
    grant select on kcson.role to info;
    grant select on kcson.role_has_permiss to info;
    grant select on kcson.rperiod to info;
    grant select on kcson.rperiodsofrname to info;
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
    grant select on kcson.ufio to info;
    grant select on kcson.ufio_has_category to info;
    grant select on kcson.ugroup to info;
    grant select on kcson.ugroup_has_ufio to info;
    grant select on kcson.ui_select_fiolist to info;
    grant select on kcson.upd_by to info;
    -- grant select on kcson.updatable_2__dep_has_ufio to info;
    -- grant select on kcson.updatable__dep_has_contracts to info;
    -- grant select on kcson.updatable__dep_has_main to info;
    -- grant select on kcson.updatable__dep_has_ufio to info;
    -- grant select on kcson.updatable__user_has_main to info;
    -- grant select on kcson.updatable_contracts to info;
    -- grant select on kcson.updatable_contracts_has_serv to info;
    -- grant select on kcson.updatable_main to info;
    -- grant select on kcson.updatable_ufio to info;
    grant select on kcson.user_has_serv to info;
    grant select on kcson.worker to info;
    grant select on kcson.worker_has_dep to info;
    grant select on kcson.worker_settings to info;
    grant select on kcson._dep_has_workers to info;
    -- grant select on kcson._apikey_has_contracts to info;
   
    #############################
    # grant perm. to web_info
    # ---------------------------
   	GRANT Select ON kcson.`_apikey_has_contracts` TO 'web_info'@'%';
   	# todo: make procedure for insert
   	GRANT insert ON kcson.`api_key_insert_main` TO 'web_info'@'%';
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
    grant select on kcson._dep_has_ufio_more to info;
    grant select on kcson._contr_has_add_info to specialist;
    grant select on kcson._dep_has_add_info to specialist;
    grant select on kcson._ufio_has_add_info to specialist;
    grant select on kcson.add_info to specialist;
    grant select on kcson.add_info_for_ufio to specialist;

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
    grant select,update,insert on kcson.updatable_2__dep_has_ufio TO trusted_specialist;
    grant select,update,insert on kcson.updatable__contr_has_add_info TO trusted_specialist;
    grant select,update,insert on kcson.updatable__dep_has_add_info TO trusted_specialist;
    grant select,update,insert on kcson.updatable__dep_has_contracts TO trusted_specialist;
    grant select,update,insert on kcson.updatable__dep_has_main TO trusted_specialist;
    grant select,update,insert on kcson.updatable__dep_has_ufio TO trusted_specialist;
    grant select,update,insert on kcson.updatable__user_has_main TO trusted_specialist;
    grant select,update,insert on kcson.updatable_add_info TO trusted_specialist;
    grant select,update,insert on kcson.updatable_contracts TO trusted_specialist;
    grant select,update,insert on kcson.updatable_contracts_has_serv TO trusted_specialist;
    grant select,update,insert on kcson.updatable_main TO trusted_specialist;
    grant select,update,insert on kcson.updatable_ufio TO trusted_specialist;



    grant select,update,insert on kcson.invoice TO trusted_specialist;
    grant select,update,insert on kcson.invoice_has_payment TO trusted_specialist;



    grant select,update,insert on kcson._contracts_has_serv TO trusted_specialist;
    grant select,update,insert on kcson.ufio_has_category TO trusted_specialist;
    #############################
    # grant perm. to manager role
    # ---------------------------
    grant trusted_specialist to manager;
    grant select,insert on kcson.category TO manager;
    grant select,insert,delete on kcson._dhw_has_ufio TO manager;
   

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

    #############################
    # grant perm. to admin role
    # ---------------------------
    grant part_admin to admin;

END $$
delimiter ;


# SET DEFAULT ROLE info to 


#############################
# routine GET_PRIVILEGES
# ---------------------------
drop procedure IF EXISTS GET_PRIVILEGES;
delimiter $$
create procedure GET_PRIVILEGES()
    SQL SECURITY DEFINER
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
END $$
delimiter ;

#############################
# routine RESET_PRIVILEGES
# ---------------------------
drop procedure IF EXISTS RESET_PRIVILEGES;
delimiter $$
create procedure RESET_PRIVILEGES()
    SQL SECURITY invoker
BEGIN
  DECLARE cursor_n VARCHAR(100) DEFAULT '';
  DECLARE cursor_rol VARCHAR(100) DEFAULT '';
  DECLARE done INT DEFAULT FALSE;
  DECLARE cursor_i CURSOR FOR  
	select distinct w.`user`, 'info' from  kcson.dep_has_worker dhw join  kcson.`role` r on r.id = dhw.role_id join  kcson.worker w on dhw.worker_id = w.id
	where  w.`user` <> "" and w.`user` <> "root" ;
  DECLARE CONTINUE handler FOR NOT FOUND SET done = TRUE;
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
END $$
delimiter ;



#############################
# routine DROP_ROLES
# ---------------------------
drop procedure IF EXISTS DROP_ROLES;
delimiter $$
create procedure DROP_ROLES()
    SQL SECURITY invoker
BEGIN
	# select CURRENT_ROLE() , user(), current_user(); 
	set role info;
	# select CURRENT_ROLE() , user(), current_user(); 
END $$
delimiter ;





#############################
# routine SET_DEP_
# ---------------------------
drop procedure IF EXISTS SET_DEP_;
delimiter $$
create definer=`root`@`localhost` PROCEDURE `kcson`.`SET_DEP_`(`depId` INT)
    MODIFIES SQL DATA
    COMMENT 'set default department (with checking is it possible)'
begin
	declare wrkID int ;
	declare res int default 0;

	  declare uid int default 0;
	  DECLARE name VARCHAR(64) DEFAULT ''; #32?
	  declare done int default false;
  
 	  DECLARE kill_i CURSOR for
	  select t.id, t.user from information_schema.processlist t where t.user = substring_index(user(),'@',1);



	set  wrkID=get_WID();
	
	set res = (select dep_id from dep_has_worker  where worker_id=wrkID and dep_id=depId);
	#set cursor_n = (select w.`user` from worker  where w.id=wrkID);
-- 	select 1;
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
		# call DROP_ROLES;
		
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
END
$$
delimiter ;


# grant worker to newuser;
# create ROLE none, info, worker, specialist, trusted_specialist, manager, part_admin, admin, booker;

#############################
# routine HELPER show_cols_root
# ---------------------------

drop procedure IF EXISTS show_cols_root;
delimiter $$
create definer=`root`@`localhost` PROCEDURE `kcson`.`show_cols_root`(IN tname TEXT)
    READS SQL DATA
    DETERMINISTIC
begin
    set @show_cols_root = CONCAT('show columns from ', tname);
    PREPARE stmt FROM @show_cols_root;
    execute stmt;
    DEALLOCATE PREPARE stmt;
end $$
delimiter ;



#############################
# allow all see percents: contract_pay_inmonth
# ---------------------------
drop procedure IF EXISTS contract_pay_inmonth;
delimiter $$
create procedure kcson.contract_pay_inmonth(IN UID INT, IN STARTDATE DATE, IN ENDDATE DATE)
sql security definer
begin
	
	IF EXISTS (SELECT 1 FROM `main` where ufio_id = UID and vdate BETWEEN STARTDATE AND ENDDATE)
	THEN
		
	        with ai as (
	        SELECT 
	            perc, pddate
	        FROM
	            add_info pd
	                JOIN
	            contracts c ON pd.contracts_id = c.id
	        WHERE
	            c.ufio_id = UID AND pddate <= ENDDATE
	        ORDER BY pddate DESC
	        LIMIT 1
	                )
	
	    SELECT 
	        SUM(((`f`.`perc` * `f`.`uslnum`) * `f`.`price`)) AS to_pay,
	        f.perc,
	        `f`.`uslnum` as uslnum,
	        f.ufio_id,
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
	                `m`.`ufio_id` AS `ufio_id`,
	                `m`.`serv_id` AS `serv_id`,
	                `m`.`vdate` AS `vdate`,
	                `m`.`uslnum` AS `uslnum`,
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
	        ufio_id = UID 
	            AND vdate BETWEEN STARTDATE AND ENDDATE
	    GROUP BY ufio_id, vdate_m , vdate_y, servform_id, perc, f.contracts_id;
	    # and servform_id = 
	  
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
				c.ufio_id = UID
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
			0 as uslnum,
			ufio_id,
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
			c.ufio_id = UID
			and 
			c.startdate <= ENDDATE and
			c.enddate >= STARTDATE;
	end if;
	
end
$$

delimiter ;


call INIT_SECURITY();

--
--
-- show processlist;
-- show GRANTS for info;
-- show GRANTS for specialist;

