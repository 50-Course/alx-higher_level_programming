-- Creates a database htbn_0d_2 and grants user user_0d_2 SELECT access
CREATE DATABASE 
    IF NOT EXISTS 'hbtn_0d_2'; -- create database

CREATE USER
    IF NOT EXISTS 'user_0d_2'@'localhost'
    IDENTIFIED BY 'user_0d_2_pwd'; -- creates the user

GRANT SELECT
    ON 'hbtn_0d_2'.*
    TO 'user_0d_2'@'localhost'; -- Gives READ access to user
