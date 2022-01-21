from typing import Dict

from qtpy.QtCore import QDate

from global_constants import SQL_DATE_FORMAT


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
                serv_id, client_id, uslnum, {0} as start_vdate, {1} as end_vdate
            from
                _dep_has_main
            where
                vdate between '{0}' and '{1}')
                
            select
                m.serv_id as serv_id,
                client_id,
                sum(m.uslnum) as uslnum,
                count(m.client_id) as records
            from
                m
            group by
                m.serv_id,
                m.client_id
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
                serv_id, client_id, worker_id, dep_has_worker_id, uslnum,  {0} as start_vdate, {1} as end_vdate
            from
                _dep_has_main
            where
                vdate between '{0}' and '{1}')
                
            select
                m.serv_id as serv_id,
                client_id, worker_id, dep_has_worker_id, 
                sum(m.uslnum) as uslnum,
                count(m.client_id) as records
            from
                m
            group by
                m.serv_id,
                m.client_id,
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
            call CREATE_PIVOT("_main_serv_name_ripso_static", "client_id, worker_id, ripso_id", "serv", "uslnum", 
            "where vdate between '{0}' and '{1}' ", "" , "", "{2}");

            """  # last - WITH ROLLUP
        #############################
        # _call_workers_total
        # ---------------------------
        sql_query_stub_data["_call_workers_total"] = (QDate(1950, 1, 1).toString(SQL_DATE_FORMAT),
                                                      QDate(1950, 1, 31).toString(SQL_DATE_FORMAT),
                                                      "_call_workers_total")
        sql_query["_call_workers_total"] = """
            call CREATE_PIVOT("_main_serv_name_static", "worker_id, client_id", "serv", "uslnum", 
            "where vdate between '{0}' and '{1}' ", "" , " WITH ROLLUP ", "{2}");

            """  # last - WITH ROLLUP
        #############################
        # _g_categ_list_client
        # ---------------------------
        sql_query_stub_data["_g_categ_list_client"] = (QDate(1950, 1, 1).toString(SQL_DATE_FORMAT),
                                                     QDate(1950, 1, 31).toString(SQL_DATE_FORMAT),
                                                     "")
        sql_query["_g_categ_list_client"] = """
            select
                `uhc`.`category_id` as `category_id`,
                `m`.`client_id` as `client_id`,
                sum(`m`.`uslnum`) as `SUM(uslnum)`
            from
                (`_dep_has_main` `m`
            join `client_has_category` `uhc` on
                ((`m`.`client_id` = `uhc`.`client_id`)))
            where
                 (coalesce(`uhc`.`archive`,    0) = 0)
                and (vdate between '{0}' and '{1}')
            group by
                `uhc`.`category_id`,
                `m`.`client_id`
            # {2}
            """
        #############################
        # _call_categ_list_client_total
        # ---------------------------
        sql_query_stub_data["_call_categ_list_client_total"] = (QDate(1950, 1, 1).toString(SQL_DATE_FORMAT),
                                                              QDate(1950, 1, 31).toString(SQL_DATE_FORMAT),
                                                              "_call_categ_list_client_total")
        sql_query["_call_categ_list_client_total"] = """
            call CREATE_PIVOT("_categ_list_client", "category_id", "serv", "uslnum", 
            "where vdate between '{0}' and '{1}' ", "" , " WITH ROLLUP ", "{2}");

            """
        #############################
        # _g_dep_serv_client_statistic
        # ---------------------------
        sql_query_stub_data["_g_dep_serv_client_statistic"] = (QDate(1950, 1, 1).toString(SQL_DATE_FORMAT),
                                                             QDate(1950, 1, 31).toString(SQL_DATE_FORMAT),
                                                             "_g_dep_serv_client_statistic")
        sql_query["_g_dep_serv_client_statistic"] = """SELECT 
            `m`.`serv_id` AS `serv_id`,
            SUM(`m`.`uslnum`) AS `uslnum`,
            client_id,
            COUNT(`m`.`client_id`) AS `records`
        FROM
            `_dep_has_main` `m`
        where vdate between '{0}' and '{1}'
        GROUP BY `m`.`serv_id` , `m`.`client_id`
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
        `m`.`client_id` as client_id,
                
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
                
                
        COUNT(`m`.`client_id`) AS `records`
        
    FROM
        `_dep_has_main` `m`
    WHERE
         `m`.vdate between '{0}' and '{1}'
    GROUP BY `m`.`serv_id` , `m`.`client_id`
    ORDER BY `m`.`serv_id`
    # {2}
    """

        #############################
        # _g_category_total_uslnum_client
        # ---------------------------
        sql_query_stub_data["_g_category_total_uslnum_client"] = (QDate(1950, 1, 1).toString(SQL_DATE_FORMAT),
                                                                QDate(1950, 1, 31).toString(SQL_DATE_FORMAT),
                                                                "_g_category_total_uslnum_client")
        sql_query["_g_category_total_uslnum_client"] = """
SELECT 
    t.category_id AS `category_id`,
    COUNT(t.`client_id`) AS `client_id`,
    SUM(t.`uslnum`) AS `uslnum`
FROM
    (SELECT 
        `uhc`.`category_id` AS `category_id`,
            `m`.`client_id`,
            SUM(`m`.`uslnum`) AS `uslnum`
    FROM
        (`main` `m`
    JOIN `client_has_category` `uhc` ON ((`m`.`client_id` = `uhc`.`client_id`)))
    WHERE
        (`m`.`dep_id` IN (31)
            AND (COALESCE(`uhc`.`archive`, 0) = 0)
            AND `m`.vdate between '{0}' and '{1}'
            AND (COALESCE(YEAR(`uhc`.`get_date`), 0) <= (SELECT GET_YEAR(GET_WID()))))
    GROUP BY `uhc`.`category_id` , `m`.`client_id`) t
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
    `t`.`client_id`,
    SUM(`t`.`uslnum`) AS `SUM(uslnum)`
FROM
    (SELECT 
        `uhc`.`category_id` AS `category_id`,
            `m`.`client_id` AS `client_id`,
            SUM(`m`.`uslnum`) AS `uslnum`
    FROM
        (`main` `m`
    LEFT JOIN `client_has_category` `uhc` ON ((`m`.`client_id` = `uhc`.`client_id`)))
    WHERE
        (`m`.`dep_id` IN (SELECT 
                `_active_dep`.`id`
            FROM
                `_active_dep`)
            AND m.vdate between '{0}' and '{1}'
            AND m.client_id NOT IN (SELECT distinct 
                client_id
            FROM
                main
            WHERE
                YEAR(vdate) >= YEAR('{0}')
                and vdate < '{0}')
            AND (COALESCE(`uhc`.`archive`, 0) = 0)
            AND (COALESCE(YEAR(`uhc`.`get_date`), 0) <= GET_YEAR(GET_WID())))
    GROUP BY `uhc`.`category_id` , `m`.`client_id`) t
GROUP BY `t`.`category_id`,client_id
    # {2}
    """
