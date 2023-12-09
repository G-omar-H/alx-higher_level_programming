-- script to creat user_0d_2 ans the database htbn_0d_2 on the MYSQL server.
CREATE DATABASE IF NOT EXISTS `hbtn_0d_2`;
CREATE USER IF NOT EXISTS 'user_0d_2'@'localhost' IDENTIFIED BY 'user_0d_2_pwd';
GRANT SELECT  ON `hbtn_0d_2`.* TO `user_0d_2`@`localhost`;
