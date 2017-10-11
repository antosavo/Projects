-- use the "my_database" database
USE my_database;

SHOW TABLES;

-- create a table called "Iris"
CREATE TABLE IF NOT EXISTS Iris
(   
sepal_length DECIMAL(6,1), 
sepal_width DECIMAL(6,1),
petal_length DECIMAL(6,1),
petal_width DECIMAL(6,1),
species VARCHAR(10)
);
 
-- Load file cvs
LOAD DATA LOCAL INFILE 'Iris.csv' INTO TABLE Iris
FIELDS TERMINATED BY ','
LINES TERMINATED BY '\n'
IGNORE 1 LINES; -- To skip the header

EXPLAIN Iris;

-- Update the "Iris" table
ALTER TABLE Iris ADD COLUMN id INT UNIQUE AUTO_INCREMENT;

EXPLAIN Iris;

-- Show table
SELECT * FROM Iris;

SELECT sepal_length, sepal_width FROM Iris WHERE id > 1 && id <10;

-- Unique species
SELECT DISTINCT species AS unique_species FROM Iris;

-- Count
SELECT COUNT(*) AS number_of_rows FROM Iris;

-- Percentage
SELECT species, COUNT(species)/(SELECT COUNT(species) FROM Iris) AS  percentage_classes FROM Iris 
GROUP BY species;

-- Avg by species
SELECT species, AVG(sepal_length), AVG(sepal_width), AVG(petal_length), AVG(petal_width) FROM Iris 
GROUP BY species;

-- Stddev by species
SELECT species, STDDEV(sepal_length), STDDEV(sepal_width), STDDEV(petal_length), STDDEV(petal_width) FROM Iris 
GROUP BY species;

-- Covariance
SELECT (SUM(sepal_length*sepal_width) - SUM(sepal_length)*SUM(sepal_width))/(COUNT(sepal_length)*COUNT(sepal_width)) AS covariance FROM Iris;

-- Delete table
DROP TABLE IF EXISTS Iris;
