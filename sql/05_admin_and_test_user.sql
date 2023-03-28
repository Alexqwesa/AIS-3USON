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


-- test user with preset readonly privileges
CREATE USER 'newuser'@'%' IDENTIFIED BY 'newuser';
GRANT Usage ON *.* TO 'newuser'@'%';
GRANT execute ON kcson.* TO 'newuser'@'%';