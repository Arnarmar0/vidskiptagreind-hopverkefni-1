/* Need to create a test table */

CREATE TABLE test (id INT NOT NULL PRIMARY KEY, name VARCHAR(20) NOT NULL);

/* Now insert a row into the test table */

INSERT INTO test VALUES (1, 'bob');

/* Now we can use the table */

SELECT * FROM test;

/* To delete the table */

DROP TABLE test;