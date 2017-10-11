-- use the "my_database" database
USE my_database;

-- create a table called "critters"
CREATE TABLE critters
(
  id		INT		PRIMARY KEY,
  name		VARCHAR(20)	NOT NULL
);

-- insert 5 records into the "critters" table
INSERT INTO critters (id, name) VALUES 
(3,"Beaver"),
(1,"Duck"),
(4,"Aardvark"),
(2,"Elephant"),
(5,"Camel");

-- show all data in the "critters" table
SELECT * FROM critters;

-- show all data in "critters" numerically ordered
SELECT * FROM critters ORDER BY id;

-- show the "name" column in "critters" alphabetically ordered
SELECT name FROM critters ORDER BY name;
--SELECT * FROM critters ORDER BY name;

-- delete this sample table
DROP TABLE critters;