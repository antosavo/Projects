-- use the "my_database" database
USE my_database;

-- create a table named "df" with 4 columns
CREATE TABLE IF NOT EXISTS df
(
  id	INT	PRIMARY KEY,
  color	VARCHAR(20),
  object	VARCHAR(20),
  price	FLOAT(5,2)
);

-- insert 3 records into the "df" table
INSERT INTO df VALUES
(1,"blue","ball",1.2), 
(2, "green","pen",1.0), 
(3, "yellow","pencil",0.6),
(4,"red","paper",0.9);

-- show all "df" data
SELECT * FROM df;

