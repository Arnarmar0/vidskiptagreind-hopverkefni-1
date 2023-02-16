/* Skiluðu allar færslur sér yfir í SQL/Excel töfluna? */

/* Veljum allar raðirnar */
SELECT * FROM brautskraning;

/* Teljum allar raðirnar */
SELECT COUNT(*) FROM brautskraning;

/* Summa allra brautskráðra nemenda úr HÍ */
SELECT SUM(samtals) FROM brautskraning WHERE tegund_nams IS NULL;
SELECT SUM(samtals) FROM skraning WHERE tegund_nams IS NULL;


/* Summa allra brautskráðra nemenda eftir deildum */
SELECT braut, SUM(samtals) FROM brautskraning GROUP BY braut;

/* Summa allra brautskráðra nemenda eftir kynjum */
SELECT SUM(kk) AS kk , SUM(kv) AS kvk FROM brautskraning WHERE tegund_nams is NULL;
