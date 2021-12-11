from typing import Dict

from qtpy.QtCore import QDate

from global_contsants import SQL_DATE_FORMAT


class _data_worker_SQL_CODE:
    def __init__(self):
        #############################
        # sql queries dict
        # ---------------------------
        self.sql_query = {}
        self.sql_query_stub_data: dict[str, tuple] = {}
        sql_query_stub_data = self.sql_query_stub_data
        sql_query = self.sql_query
        #############################
        # _g_serv_total_dep
        # ---------------------------
        sql_query_stub_data["_g_serv_total_dep"] = (QDate(1950, 1, 1).toString(SQL_DATE_FORMAT),
                                                    QDate(1950, 1, 31).toString(SQL_DATE_FORMAT),
                                                    "_g_serv_total_dep")
        sql_query["_g_serv_total_dep"] = """
            with m as (
            select
                serv_id, ufio_id, uslnum, {0} as start_vdate, {1} as end_vdate
            from
                _dep_has_main
            where
                vdate between '{0}' and '{1}')
                
            select
                m.serv_id as serv_id,
                ufio_id,
                sum(m.uslnum) as uslnum,
                count(m.ufio_id) as records
            from
                m
            group by
                m.serv_id,
                m.ufio_id
            order by
                m.serv_id
                # {2}
        """
        #############################
        # _g_serv_total_dep_with_worker
        # ---------------------------
        sql_query_stub_data["_g_serv_total_dep_with_worker"] = (QDate(1950, 1, 1).toString(SQL_DATE_FORMAT),
                                                                QDate(1950, 1, 31).toString(SQL_DATE_FORMAT),
                                                                "_g_serv_total_dep_with_worker")
        sql_query["_g_serv_total_dep_with_worker"] = """
            with m as (
            select
                serv_id, ufio_id, worker_id, dep_has_worker_id, uslnum,  {0} as start_vdate, {1} as end_vdate
            from
                _dep_has_main
            where
                vdate between '{0}' and '{1}')
                
            select
                m.serv_id as serv_id,
                ufio_id, worker_id, dep_has_worker_id, 
                sum(m.uslnum) as uslnum,
                count(m.ufio_id) as records
            from
                m
            group by
                m.serv_id,
                m.ufio_id,
                m.worker_id,
                m.dep_has_worker_id
            order by
                m.worker_id,
                m.serv_id
                # {2}
        """
        #############################
        # stub
        # ---------------------------
        sql_query["stub"] = """
                select * from stub_model
            """
        #############################
        # _call_export_dep
        # ---------------------------
        sql_query_stub_data["_call_export_dep"] = (QDate(1950, 1, 1).toString(SQL_DATE_FORMAT),
                                                   QDate(1950, 1, 31).toString(SQL_DATE_FORMAT),
                                                   "_call_export_dep")
        sql_query["_call_export_dep"] = """
            call CREATE_PIVOT("_main_serv_name_ripso_static", "ufio_id, worker_id, ripso_id", "serv", "uslnum", 
            "where vdate between '{0}' and '{1}' ", "" , "", "{2}");

            """  # last - WITH ROLLUP
        #############################
        # _call_workers_total
        # ---------------------------
        sql_query_stub_data["_call_workers_total"] = (QDate(1950, 1, 1).toString(SQL_DATE_FORMAT),
                                                      QDate(1950, 1, 31).toString(SQL_DATE_FORMAT),
                                                      "_call_workers_total")
        sql_query["_call_workers_total"] = """
            call CREATE_PIVOT("_main_serv_name_static", "worker_id, ufio_id", "serv", "uslnum", 
            "where vdate between '{0}' and '{1}' ", "" , " WITH ROLLUP ", "{2}");

            """  # last - WITH ROLLUP
        #############################
        # _g_categ_list_ufio
        # ---------------------------
        sql_query_stub_data["_g_categ_list_ufio"] = (QDate(1950, 1, 1).toString(SQL_DATE_FORMAT),
                                                     QDate(1950, 1, 31).toString(SQL_DATE_FORMAT),
                                                     "")
        sql_query["_g_categ_list_ufio"] = """
            select
                `uhc`.`category_id` as `category_id`,
                `m`.`ufio_id` as `ufio_id`,
                sum(`m`.`uslnum`) as `SUM(uslnum)`
            from
                (`_dep_has_main` `m`
            join `ufio_has_category` `uhc` on
                ((`m`.`ufio_id` = `uhc`.`ufio_id`)))
            where
                 (coalesce(`uhc`.`archive`,    0) = 0)
                and (vdate between '{0}' and '{1}')
            group by
                `uhc`.`category_id`,
                `m`.`ufio_id`
            # {2}
            """
        #############################
        # _call_categ_list_ufio_total
        # ---------------------------
        sql_query_stub_data["_call_categ_list_ufio_total"] = (QDate(1950, 1, 1).toString(SQL_DATE_FORMAT),
                                                              QDate(1950, 1, 31).toString(SQL_DATE_FORMAT),
                                                              "_call_categ_list_ufio_total")
        sql_query["_call_categ_list_ufio_total"] = """
            call CREATE_PIVOT("_categ_list_ufio", "category_id", "serv", "uslnum", 
            "where vdate between '{0}' and '{1}' ", "" , " WITH ROLLUP ", "{2}");

            """
        #############################
        # _g_dep_serv_ufio_statistic
        # ---------------------------
        sql_query_stub_data["_g_dep_serv_ufio_statistic"] = (QDate(1950, 1, 1).toString(SQL_DATE_FORMAT),
                                                             QDate(1950, 1, 31).toString(SQL_DATE_FORMAT),
                                                             "_g_dep_serv_ufio_statistic")
        sql_query["_g_dep_serv_ufio_statistic"] = """SELECT 
            `m`.`serv_id` AS `serv_id`,
            SUM(`m`.`uslnum`) AS `uslnum`,
            ufio_id,
            COUNT(`m`.`ufio_id`) AS `records`
        FROM
            `_dep_has_main` `m`
        where vdate between '{0}' and '{1}'
        GROUP BY `m`.`serv_id` , `m`.`ufio_id`
        ORDER BY `m`.`serv_id` # {2}
        """

        #############################
        # _g_serv_total_you
        # ---------------------------
        sql_query_stub_data["_g_serv_total_you"] = (QDate(1950, 1, 1).toString(SQL_DATE_FORMAT),
                                                    QDate(1950, 1, 31).toString(SQL_DATE_FORMAT),
                                                    "_g_serv_total_you")
        sql_query["_g_serv_total_you"] = """
    SELECT 
        `m`.`serv_id` AS `serv_id`,
        SUM(`m`.`uslnum`) AS `uslnum`,
        `m`.`ufio_id` as ufio_id,
                
            (
                    SELECT 
                        min(vdate)
                    FROM
                        `_dep_has_main` `mfd`
                    WHERE
                        (`m`.`serv_id` = `mfd`.`serv_id`)
                         and
                         `mfd`.vdate between '{0}' and '{1}'
                ) AS `first_vdate`,
                
                (
                    SELECT 
                        max(vdate)
                    FROM
                        `_dep_has_main` `mfd`
                    WHERE
                        (`m`.`serv_id` = `mfd`.`serv_id`)
                         and
                         `mfd`.vdate between '{0}' and '{1}'
                ) AS `last_vdate`,
                
                
        COUNT(`m`.`ufio_id`) AS `records`
        
    FROM
        `_dep_has_main` `m`
    WHERE
         `m`.vdate between '{0}' and '{1}'
    GROUP BY `m`.`serv_id` , `m`.`ufio_id`
    ORDER BY `m`.`serv_id`
    # {2}
    """

        #############################
        # _g_category_total_uslnum_ufio
        # ---------------------------
        sql_query_stub_data["_g_category_total_uslnum_ufio"] = (QDate(1950, 1, 1).toString(SQL_DATE_FORMAT),
                                                                QDate(1950, 1, 31).toString(SQL_DATE_FORMAT),
                                                                "_g_category_total_uslnum_ufio")
        sql_query["_g_category_total_uslnum_ufio"] = """
SELECT 
    t.category_id AS `category_id`,
    COUNT(t.`ufio_id`) AS `ufio_id`,
    SUM(t.`uslnum`) AS `uslnum`
FROM
    (SELECT 
        `uhc`.`category_id` AS `category_id`,
            `m`.`ufio_id`,
            SUM(`m`.`uslnum`) AS `uslnum`
    FROM
        (`main` `m`
    JOIN `ufio_has_category` `uhc` ON ((`m`.`ufio_id` = `uhc`.`ufio_id`)))
    WHERE
        (`m`.`dep_id` IN (31)
            AND (COALESCE(`uhc`.`archive`, 0) = 0)
            AND `m`.vdate between '{0}' and '{1}'
            AND (COALESCE(YEAR(`uhc`.`get_date`), 0) <= (SELECT GET_YEAR(GET_WID()))))
    GROUP BY `uhc`.`category_id` , `m`.`ufio_id`) t
GROUP BY t.`category_id`
    # {2}
    """

        #############################
        # _g_category_total_new
        # ---------------------------
        sql_query_stub_data["_g_category_total_new"] = (QDate(1950, 1, 1).toString(SQL_DATE_FORMAT),
                                                        QDate(1950, 1, 31).toString(SQL_DATE_FORMAT),
                                                        "_g_category_total_new")
        sql_query["_g_category_total_new"] = """
SELECT 
    COALESCE(`t`.`category_id`, 'Прочие') AS `category_id`,
    `t`.`ufio_id`,
    SUM(`t`.`uslnum`) AS `SUM(uslnum)`
FROM
    (SELECT 
        `uhc`.`category_id` AS `category_id`,
            `m`.`ufio_id` AS `ufio_id`,
            SUM(`m`.`uslnum`) AS `uslnum`
    FROM
        (`main` `m`
    LEFT JOIN `ufio_has_category` `uhc` ON ((`m`.`ufio_id` = `uhc`.`ufio_id`)))
    WHERE
        (`m`.`dep_id` IN (SELECT 
                `_active_dep`.`id`
            FROM
                `_active_dep`)
            AND m.vdate between '{0}' and '{1}'
            AND m.ufio_id NOT IN (SELECT distinct 
                ufio_id
            FROM
                main
            WHERE
                YEAR(vdate) >= YEAR('{0}')
                and vdate < '{0}')
            AND (COALESCE(`uhc`.`archive`, 0) = 0)
            AND (COALESCE(YEAR(`uhc`.`get_date`), 0) <= GET_YEAR(GET_WID())))
    GROUP BY `uhc`.`category_id` , `m`.`ufio_id`) t
GROUP BY `t`.`category_id`,ufio_id
    # {2}
    """
