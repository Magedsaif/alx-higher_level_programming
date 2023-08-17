-- -- create database and TABLE states
CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;
CREATE TABLE IF NOT EXISTS hbtn_0d_usa.states(
    id INT PRIMARY KEY NOT NULL AUTO_INCREMENT,
    name VARCHAR(256)
);
