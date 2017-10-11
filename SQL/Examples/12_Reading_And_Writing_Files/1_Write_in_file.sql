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

-- insert 5 records into the "games" table
INSERT INTO games (id, vendor, name, price) VALUES
("371/2209", 1, "Scrabble", 14.50),
("373/2296", 2, "Jenga", 6.99),
("360/9659", 1, "Uno", 11.99),
("373/5372", 3, "Connect", 5.99),
("370/9470", 3, "Bingo", 8.99);

SELECT * FROM games 
INTO OUTFILE 'Table_games_A.txt';-- save in /usr/local/mysql/data/my_database

SELECT * FROM games 
INTO OUTFILE 'Table_games_B.txt'
FIELDS TERMINATED BY ','
LINES TERMINATED BY '\n';

SELECT * FROM games 
INTO OUTFILE 'Table_games_C.txt'
FIELDS TERMINATED BY ',' ENCLOSED BY '"'
LINES TERMINATED BY '\n';

-- delete these sample tables
DROP TABLE games;