-- create the database hbtn_0d_usa
-- create the table states on MySQL server
CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;
CREATE TABLE IF NOT EXISTS states(id INT PRIMARY KEY UNIQUE NOT NULL AUTO_INCREMENT, name VARCHAR(256) NOT NULL);