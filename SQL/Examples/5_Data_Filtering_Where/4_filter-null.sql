-- use the "my_database" database
USE my_database;

-- create a table called "steam_irons"
CREATE TABLE IF NOT EXISTS steam_irons
(
  id		INT		AUTO_INCREMENT PRIMARY KEY,
  make		VARCHAR(25)	NOT NULL,
  model		VARCHAR(25)	NOT NULL,
  color		VARCHAR(25)
);

-- insert 5 records into the "steam_irons" table
INSERT INTO steam_irons (make, model, color) VALUES
("Philips", "GC3020", "Lilac"),
("Bosch", "TDA8360", "Blue");
INSERT INTO steam_irons (make, model) VALUES
("Morphy Richards", "40608"),
("Tefal", "1819 Avantis"),
("Rowenta", "DM529");


-- show the table format
EXPLAIN steam_irons;

-- show all data in the "steam_irons" table
SELECT * FROM steam_irons;

-- show all records where there is no specified color
SELECT * FROM steam_irons WHERE color IS NULL;

-- delete this sample table
DROP TABLE IF EXISTS steam_irons;