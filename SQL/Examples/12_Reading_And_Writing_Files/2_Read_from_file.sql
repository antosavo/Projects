-- use the "my_database" database
USE my_database;

-- create a table called "games"
CREATE TABLE IF NOT EXISTS games
(
  id		VARCHAR(10)	PRIMARY KEY,
  vendor	INT		NOT NULL,
  name		CHAR(20)	NOT NULL,
  price		DECIMAL(6,2)	NOT NULL
);


LOAD DATA LOCAL INFILE 'Table_games.txt' INTO TABLE games;

/* 
LOAD DATA LOCAL INFILE 'Table_games.txt' INTO TABLE games
FIELDS TERMINATED BY ','
LINES TERMINATED BY '\n';
*/

SELECT * FROM games;

DROP TABLE games;