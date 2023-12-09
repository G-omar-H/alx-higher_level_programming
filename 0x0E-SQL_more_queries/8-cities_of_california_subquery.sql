-- script that lists all the cities of California that can be found in the database hbtn_0d_usa.
-- list by city.id in ascending order.
SELECT id, name FROM cities WHERE state_id =  (SELECT state_id FROM states WHERE name = 'California') ORDER BY id ASC;
