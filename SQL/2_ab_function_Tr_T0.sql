-- use the "my_database" database
USE my_database;

SHOW TABLES;

-- create a table
CREATE TABLE IF NOT EXISTS ab_function_Tr
(   
P1 DECIMAL(6,3), 
P2 DECIMAL(6,3),
a DECIMAL(6,3),
b DECIMAL(6,3),
Tr DECIMAL(6,3)
);
 
-- Load file cvs
LOAD DATA LOCAL INFILE 'ab_funtion_Tr.dat' INTO TABLE ab_function_Tr
FIELDS TERMINATED BY '\t'
LINES TERMINATED BY '\n'
IGNORE 1 LINES; -- To skip the header

EXPLAIN ab_function_Tr;

SELECT * FROM ab_function_Tr;

-- create a table
CREATE TABLE IF NOT EXISTS ab_function_T0
(   
P1 DECIMAL(6,3), 
P2 DECIMAL(6,3),
a DECIMAL(6,3),
b DECIMAL(6,3),
T0 DECIMAL(6,3)
);
 
-- Load file cvs
LOAD DATA LOCAL INFILE 'ab_funtion_T0.dat' INTO TABLE ab_function_T0
FIELDS TERMINATED BY '\t'
LINES TERMINATED BY '\n'
IGNORE 1 LINES; -- To skip the header

EXPLAIN ab_function_T0;

SELECT * FROM ab_function_T0;

-- Create table with natural join

CREATE TABLE new_table
SELECT 	ab_function_Tr.P1, ab_function_Tr.Tr, ab_function_T0.T0
FROM 	ab_function_Tr, ab_function_T0
WHERE 	ab_function_Tr.P1 = ab_function_T0.P1;

SELECT * FROM new_table;

-- Statistics

SELECT AVG(a), STDDEV(a), AVG(b), STDDEV(b) FROM new_table;

-- Delete tables

DROP TABLE IF EXISTS ab_function_Tr;

DROP TABLE IF EXISTS ab_function_T0;

DROP TABLE IF EXISTS new_table;