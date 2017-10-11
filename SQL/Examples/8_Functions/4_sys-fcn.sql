-- get the version number and current user
SELECT VERSION(), USER();
SHOW VARIABLES WHERE Variable_name LIKE '%host%';
SHOW VARIABLES WHERE Variable_name LIKE '%port%';

-- get the thread identity
SHOW PROCESSLIST;

-- create a new user with full privileges
-- CREATE USER 'anto'@'localhost' IDENTIFIED BY 'anto131284';
-- GRANT ALL PRIVILEGES ON *.* TO 'anto'@'localhost' WITH GRANT OPTION;
-- CREATE USER 'anto'@'%' IDENTIFIED BY 'anto131284';
-- GRANT ALL PRIVILEGES ON *.* TO 'anto'@'%' WITH GRANT OPTION;

-- confirm privileges for the new user
SHOW GRANTS FOR anto@localhost;


