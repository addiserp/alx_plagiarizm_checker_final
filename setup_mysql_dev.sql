-- prepares a MySQL server for the projectdb
-- plag_MYSQL_USER=plag_dev plag_MYSQL_PWD=plag_dev_pwd plag_MYSQL_HOST=localhost plag_MYSQL_DB=plag_dev_db plag_TYPE_STORAGE=db
drop DATABASE plag_dev_db;
CREATE DATABASE IF NOT EXISTS plag_dev_db;
CREATE USER IF NOT EXISTS 'plag_dev'@'localhost' IDENTIFIED BY 'plag_dev_pwd';
GRANT ALL PRIVILEGES ON `plag_dev_db`.* TO 'plag_dev'@'localhost';
GRANT SELECT ON `performance_schema`.* TO 'plag_dev'@'localhost';
FLUSH PRIVILEGES;

drop DATABASE plag_dev_db1;
CREATE DATABASE IF NOT EXISTS plag_dev_db1;
CREATE USER IF NOT EXISTS 'plag_dev1'@'localhost' IDENTIFIED BY 'plag_dev_pwd1';
GRANT ALL PRIVILEGES ON `plag_dev_db1`.* TO 'plag_dev1'@'localhost';
GRANT SELECT ON `performance_schema`.* TO 'plag_dev1'@'localhost';
FLUSH PRIVILEGES;