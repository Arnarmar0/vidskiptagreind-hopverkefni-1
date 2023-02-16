/* Need to create a test table */

CREATE TABLE test (id INT NOT NULL PRIMARY KEY, name VARCHAR(20) NOT NULL);

/* Now insert a row into the test table */

INSERT INTO test VALUES (1, 'bob');

/* Now we can use the table */
CREATE TABLE skraning (id serial PRIMARY KEY, Year integer, Braut varchar, tegund_nams varchar, kk integer, kv integer, samtals integer);
SELECT * FROM brautskraning;
SELECT * FROM skraning;

select Year, Braut, samtals from brautskraning where tegund_nams is null 
COPY brautskraning 
DROP TABLE brautskraning;
COPY brautskraning TO 'C:\Users\hinri\OneDrive\Documents\HR\Viðskiptagreind\vidskiptagreind-hopverkefni-1\data\test.csv' WITH DELIMITER ',' CSV HEADER;

/* To delete the table */

DROP TABLE test;