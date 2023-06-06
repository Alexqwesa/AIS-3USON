# since filling test data for every new year is tiresome, test database will always use 2022 year internally
DELIMITER @@
CREATE
    DEFINER = `root`@`localhost` FUNCTION `GET_YEAR`(
    `wrkID` INT
) RETURNS int
    READS SQL DATA
    SQL SECURITY INVOKER
    COMMENT 'get current year test version, always returns 2022'
BEGIN
    declare var int(0);

    set var = 2022; # (select last_year from worker_settings where id = wrkID);

    if var > 0 then
        return var;
    else
        set var = 2022;
        if var > 0 then
            return var;
        else
            return 1;
            # 1 - undefined dep
        end if;
    end if;
END @@
DELIMITER ;