-- use the "my_database" database
USE my_database;

SHOW TABLES;

-- create a table
CREATE TABLE IF NOT EXISTS ab_function_P1
(   
P1 DECIMAL(6,3), 
P2 DECIMAL(6,3),
a DECIMAL(6,3),
b DECIMAL(6,3)
);
 
-- Load file cvs
LOAD DATA LOCAL INFILE 'ab_funtion_P1.dat' INTO TABLE ab_function_P1
FIELDS TERMINATED BY '\t'
LINES TERMINATED BY '\n'
IGNORE 1 LINES; -- To skip the header

EXPLAIN ab_function_P1;

SELECT * FROM ab_function_P1;

-- create a table
CREATE TABLE IF NOT EXISTS ab_function_P2
(   
P1 DECIMAL(6,3), 
P2 DECIMAL(6,3),
a DECIMAL(6,3),
b DECIMAL(6,3)
);
 
-- Load file cvs
LOAD DATA LOCAL INFILE 'ab_funtion_P2.dat' INTO TABLE ab_function_P2
FIELDS TERMINATED BY '\t'
LINES TERMINATED BY '\n'
IGNORE 1 LINES; -- To skip the header

EXPLAIN ab_function_P2;

SELECT * FROM ab_function_P2;

-- Create table with all data in "ab_function_P2" and "ab_function_P1", also duplicates

CREATE TABLE new_table
SELECT * FROM ab_function_P1
UNION ALL
SELECT * FROM ab_function_P2;

SELECT * FROM new_table;

-- Statistics

SELECT AVG(a), STDDEV(a), AVG(b), STDDEV(b) FROM new_table;

-- Delete tables

DROP TABLE IF EXISTS ab_function_P1;

DROP TABLE IF EXISTS ab_function_P2;

DROP TABLE IF EXISTS new_table;