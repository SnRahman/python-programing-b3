
-- select any column from table
SELECT `first_name` FROM `users`;

-- Select multiple columns from table
SELECT `first_name`,`email` FROM `users`;

-- select all columns from table
SELECT * FROM `users`;

-- Select limited records/rows from table
SELECT * FROM `users` LIMIT 1;

-- select rows using where clause 
SELECT * FROM `users` WHERE `id`=7;
SELECT * FROM `users` WHERE `email`= 'ahmadadeel@gmail.com';
SELECT * FROM `users` WHERE `email`= 'ahmadadeel@gmail.com' LIMIT 1;

-- select rows using multiple columns check using AND operator
SELECT * FROM `users` WHERE `email`= 'ahmadadeel@gmail.com' AND `password` = 'admin';

-- select rows using multiple columns check using OR operator
SELECT * FROM `users` WHERE `email`= 'ahmadadeel@gmail.com' OR `password` = 'admin';

-- select data using is null keywords
SELECT * FROM `users` WHERE `last_name` IS NULL

-- order by selected data
SELECT * FROM `users` ORDER BY `first_name` DESC;
SELECT * FROM `users` ORDER BY `id` ASC;

-- select highest value from any column
SELECT MAX(price) FROM Products ;

-- select lowest value from any column
SELECT MIN(price) FROM Products ;

-- GEt average value from any column
SELECT AVG(price) FROM Products ;

-- sum the column value from may table
SELECT SUM(price) FROM Products ;

-- return total number of rows/ records
SELECT COUNT(price) FROM Products ;

-- select using like keyword
SELECT * FROM `users` WHERE `first_name` LIKE '%Ahmad%';
SELECT * FROM `users` WHERE `first_name` LIKE 'Ahmad%';
SELECT * FROM `users` WHERE `first_name` LIKE '%Ahmad';

-- get records using multiple values
SELECT * FROM `users` WHERE `id` IN (8,9,4,6);

-- get records using range
SELECT * FROM `users` WHERE `id` BETWEEN  1 AND 7;

-- insert data into table
INSERT INTO `users` VALUES(9,'Babar','Azam','ba@gmail.com','babar')
INSERT INTO `users` (`first_name`,`last_name`,`email`,`password`)  VALUES('Babar','Azam','ba@gmail.com','babar');
INSERT INTO `users` (`first_name`,`email`,`password`)  VALUES('Babar','','babar');

-- update row into table
UPDATE `users` SET `last_name` = 'Azam' WHERE `id`=10;
UPDATE `users` SET `last_name` = 'shafique' , `first_name` = 'Abdullah' WHERE `id`=10;

-- delete data from table
DELETE FROM `users` WHERE `id` = 13
DELETE FROM `users` WHERE `last_name`= NULL OR `email` ='';
DELETE FROM `users` WHERE `last_name` IS NULL OR `email` ='';