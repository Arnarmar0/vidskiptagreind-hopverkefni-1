/* Need to create a test table */

CREATE TABLE test (id INT NOT NULL PRIMARY KEY, name VARCHAR(20) NOT NULL);

/* Now insert a row into the test table */

INSERT INTO test VALUES (1, 'bob');

/* Now we can use the table */
CREATE TABLE brautskraning (id serial PRIMARY KEY, Year integer, Braut varchar, tegund_nams varchar, kk integer, kv integer, samtals integer);
SELECT * FROM brautskraning;
DROP TABLE brautskraning;

/* To delete the table */

DROP TABLE test;