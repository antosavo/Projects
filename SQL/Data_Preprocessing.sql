/*This SQL script preprocess the data for the interaction of two signals in an optical fiber. The target variable is the energy E. There are three input files that are joined and united in a single data-set. Finally, the new data-set is cleaned and explored.*/

-- use the "my_database" database

USE my_database;

SHOW TABLES;

-- create table from file Data-Energy-1.dat

CREATE TABLE IF NOT EXISTS Data_Energy_1
(
    B2 DECIMAL(6,3),
    G DECIMAL(6,3),
    DO DECIMAL(6,3),
    Dz DECIMAL(6,3),
    P1 DECIMAL(6,3),
    P2 DECIMAL(6,3),
    E DECIMAL(6,3)
);
 
-- Load file

LOAD DATA LOCAL INFILE 'Data-Energy-1.dat' INTO TABLE Data_Energy_1
FIELDS TERMINATED BY ','
LINES TERMINATED BY '\n'
IGNORE 1 LINES; -- To skip the header

EXPLAIN Data_Energy_1;

SELECT * FROM Data_Energy_1;

-- create table from file Data-Energy-2-P1.dat

CREATE TABLE IF NOT EXISTS Data_Energy_2_P1
(
    B2 DECIMAL(6,3),
    G DECIMAL(6,3),
    DO DECIMAL(6,3),
    Dz DECIMAL(6,3),
    P1 DECIMAL(6,3),
    E DECIMAL(6,3)
);
 
-- Load file

LOAD DATA LOCAL INFILE 'Data-Energy-2-P1.dat' INTO TABLE Data_Energy_2_P1
FIELDS TERMINATED BY ','
LINES TERMINATED BY '\n'
IGNORE 1 LINES; -- To skip the header

CREATE TABLE DE1 AS (SELECT DISTINCT * FROM Data_Energy_2_P1);

DROP TABLE IF EXISTS Data_Energy_2_P1;

SELECT * FROM DE1;

-- create a table from file Data-Energy-2-P2.dat

CREATE TABLE IF NOT EXISTS Data_Energy_2_P2
(
    B2 DECIMAL(6,3),
    G DECIMAL(6,3),
    DO DECIMAL(6,3),
    Dz DECIMAL(6,3),
    P2 DECIMAL(6,3),
    E DECIMAL(6,3)
);
 
-- Load file

LOAD DATA LOCAL INFILE 'Data-Energy-2-P2.dat' INTO TABLE Data_Energy_2_P2
FIELDS TERMINATED BY ','
LINES TERMINATED BY '\n'
IGNORE 1 LINES; -- To skip the header

CREATE TABLE DE2 AS (SELECT DISTINCT * FROM Data_Energy_2_P2);

DROP TABLE IF EXISTS Data_Energy_2_P2;

SELECT * FROM DE2;

-- Join DE1 and DE2 into DE12

CREATE TABLE DE12 AS (SELECT DE1.B2, DE1.G, DE1.DO, DE1.Dz, DE1.P1, DE2.P2, DE1.E
FROM DE1, DE2
WHERE DE1.B2 = DE2.B2
AND DE1.G = DE2.G
AND DE1.DO = DE2.DO
AND DE1.Dz = DE2.Dz
AND	DE1.E = DE2.E);

DROP TABLE IF EXISTS DE1;

DROP TABLE IF EXISTS DE2;
                      
SELECT * FROM DE12;

-- Create table with all data in "Data_Energy_1" and "D12"

CREATE TABLE Data_Energy
SELECT * FROM Data_Energy_1
UNION ALL
SELECT * FROM DE12;

DROP TABLE IF EXISTS Data_Energy_1;

DROP TABLE IF EXISTS DE12;

SELECT * FROM Data_Energy;

-- Explore the data set Data_Energy

EXPLAIN Data_Energy;

-- Statistics

SELECT AVG(E), STDDEV(E), MIN(E), MAX(E), COUNT(E) FROM Data_Energy;

-- Distinct P1

SELECT DISTINCT P1 AS distinct_P1 
FROM Data_Energy;

-- Number of distinct P1

SELECT COUNT(DISTINCT P1) AS num_distinct_P1 
FROM Data_Energy;

-- Count of distinct P1

SELECT P1, COUNT(P1)
FROM Data_Energy 
GROUP BY P1;

-- Avg by P1

SELECT P1, AVG(B2), AVG(G), AVG(DO), AVG(DZ), AVG(P2), AVG(E) 
FROM Data_Energy  
GROUP BY P1;

-- correlation <P1,E>

SELECT (AVG(P1*E)-AVG(P1)*AVG(E))/(STDDEV(P1)*STDDEV(E)) AS correlation 
FROM Data_Energy;

-- Add and select ID

ALTER TABLE Data_Energy ADD COLUMN id INT UNIQUE AUTO_INCREMENT;

SELECT * FROM Data_Energy WHERE id > 5 && id <10;

SELECT * FROM Data_Energy WHERE id = 7;

SELECT * FROM Data_Energy WHERE id <= 5 || id >=38;

-- Save Data_Energy into file in /usr/local/mysql/data/my_database

/*
SELECT * FROM Data_Energy 
INTO OUTFILE 'Data_Energy.dat'
FIELDS TERMINATED BY ','
LINES TERMINATED BY '\n';
*/

-- Drop tables

DROP TABLE IF EXISTS Data_Energy;