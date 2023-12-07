--script that creates a table second_table in the database hbtn_0c_0 in your MySQL server and add multiples rows.
CREATE TABLE IF NOT EXISTS second_table (
id INT,
name varchar(256),
score INT
)
PARTITION BY LIST COLUMNS(id, name, score) (
	PARTITION P_1 VALUES IN((1, "John", 10), (2, "Alex", 3), (3, "Bob", 14), (4, "George", 8) )
);

