/*!50001 SET character_set_client = utf8mb4 */;
/*!50001 SET character_set_results = utf8mb4 */;
/*!50001 SET collation_connection = utf8mb4_0900_ai_ci */;

-- administrator
CREATE USER 'admin2'@'%' IDENTIFIED BY 'admin2';
GRANT Usage ON *.* TO 'admin2'@'%';
GRANT execute ON kcson.* TO 'admin2'@'%';
-- assign admin role (allow to login and get privileges)
INSERT INTO kcson.worker (id, worker, `user`, note, role_id, dep_id, archive)
VALUES (3, 'admin2', 'admin2', NULL, 1, 1, 0);
INSERT INTO kcson.dep_has_worker (id, dep_has_worker, worker_id, dep_id, job_id, note, archive, `from`, till, role_id,
                                  api_key)
VALUES (3, 'admin2', 3, 2, 1, NULL, 0, '2000-01-01', '2050-01-01', 8, '');
ALTER USER 'admin2'@'%' account unlock;


-- test user with preset readonly privileges
CREATE USER 'newuser'@'%' IDENTIFIED BY 'newuser';
GRANT Usage ON *.* TO 'newuser'@'%';
GRANT execute ON kcson.* TO 'newuser'@'%';
ALTER USER 'newuser'@'%' account unlock;

-- allow access for web_info from any host (change it if necessary)
# CREATE USER 'web_info'@'%' IDENTIFIED BY 'nopassword';
# GRANT web_info to 'web_info'@'%';
ALTER USER 'web_info'@'%' account unlock;


flush privileges;