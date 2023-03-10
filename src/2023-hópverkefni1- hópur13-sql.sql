/* Búum til töflur fyrir brautskráningu og skráningu */
CREATE TABLE brautskraning (id serial PRIMARY KEY, Year integer, Braut varchar, tegund_nams varchar, kk integer, kv integer, samtals integer);
CREATE TABLE skraning (id serial PRIMARY KEY, Year integer, Braut varchar, tegund_nams varchar, kk integer, kv integer, samtals integer);

/* Veljum allar raðirnar í brautskráningartöflunni */
SELECT * FROM brautskraning;

/* Veljum allar raðirnar í skráningartöflunni */
SELECT * FROM skraning;

/* Teljum allar raðirnar í brautskráningartöflunni */
SELECT COUNT(*) FROM brautskraning;

/* Teljum allar raðirnar í skráningartöflunni */
SELECT COUNT(*) FROM skraning;

/* Summa allra skráðra nemenda úr HÍ */
SELECT SUM(samtals) FROM skraning WHERE tegund_nams IS NULL;

/* Summa allra brautskráðra nemenda úr HÍ */
SELECT SUM(samtals) FROM brautskraning WHERE tegund_nams IS NULL;

/* Samtals allra skráðra og brautskráðra nemenda úr HÍ með útskriftarprósentu */
SELECT
  SUM(s.skradir) as samtals_skradir,
  SUM(b.brautskradir) as samtals_brautskradir,
  ROUND((SUM(b.brautskradir) * 100.0 / SUM(s.skradir)), 2) as utskriftarprosenta
FROM
  (SELECT SUM(samtals) as skradir
   FROM skraning
   WHERE tegund_nams is null) s,
  (SELECT SUM(samtals) as brautskradir
   FROM brautskraning
   WHERE tegund_nams is null) b;

/* Summa allra skráðra nemenda í HÍ eftir árum */
SELECT Year, SUM(samtals) as skradir
FROM skraning
WHERE tegund_nams IS NULL
GROUP BY Year
ORDER BY Year;

/* Summa allra brautskráðra nemenda í HÍ eftir árum */
SELECT Year, SUM(samtals) as brautskradir
FROM brautskraning
WHERE tegund_nams IS NULL
GROUP BY Year
ORDER BY Year;

/* Samtals allra skráðra og brautskráðra nemenda úr HÍ eftir árum með útskriftarprósentum */
SELECT s.Year, s.skradir, b.brautskradir, ROUND((b.brautskradir * 100.0 / s.skradir)::numeric, 2) as utskriftarprosenta
FROM
  (SELECT Year, SUM(samtals) as skradir
   FROM skraning
   WHERE tegund_nams IS NULL
   GROUP BY Year) s
LEFT JOIN
  (SELECT Year, SUM(samtals) as brautskradir
   FROM brautskraning
   WHERE tegund_nams IS NULL
   GROUP BY Year) b
ON s.Year = b.Year
ORDER BY s.Year;

/* Summa allra skráðra nemenda eftir deildum */
SELECT braut, SUM(samtals) FROM skraning WHERE tegund_nams IS NULL GROUP BY braut;

/* Summa allra brautskráðra nemenda eftir deildum */
SELECT braut, SUM(samtals) FROM brautskraning WHERE tegund_nams IS NULL GROUP BY braut;

/* Summa allra skráðra og brautskráðra nemenda eftir deildum með útskriftarprósentu */
SELECT s.braut, s.skradir, b.brautskradir, ROUND((b.brautskradir * 100.0 / s.skradir)::numeric, 2) as utskriftarprosenta
FROM
  (SELECT braut, SUM(samtals) as skradir
   FROM skraning
   WHERE tegund_nams IS NULL
   GROUP BY braut) s
LEFT JOIN
    (SELECT braut, SUM(samtals) as brautskradir
     FROM brautskraning
     WHERE tegund_nams IS NULL
     GROUP BY braut) b
ON s.braut = b.braut
ORDER BY s.braut;

/* Summa allra skráðra nemenda eftir kynjum */
SELECT SUM(kk) AS kk , SUM(kv) AS kvk FROM skraning WHERE tegund_nams is NULL;

/* Summa allra brautskráðra nemenda eftir kynjum */
SELECT SUM(kk) AS kk , SUM(kv) AS kvk FROM brautskraning WHERE tegund_nams is NULL;

/* Summa allra brautskráðra og skráðra nemenda eftir kynjum í einni töflu með útskriftarprósentum fyrir kk og kvk */
SELECT s.Year, s.kk_skradir, s.kvk_skradir, b.kk_brautskradir, b.kvk_brautskradir, ROUND((b.kk_brautskradir * 100.0 / s.kk_skradir)::numeric, 2) as utskriftarprosenta_kk, ROUND((b.kvk_brautskradir * 100.0 / s.kvk_skradir)::numeric, 2) as prosenta_kvk
FROM
  (SELECT Year, SUM(kk) as kk_skradir, SUM(kv) as kvk_skradir
   FROM skraning
   WHERE tegund_nams IS NULL
   GROUP BY Year) s
LEFT JOIN
  (SELECT Year, SUM(kk) as kk_brautskradir, SUM(kv) as kvk_brautskradir
   FROM brautskraning
   WHERE tegund_nams IS NULL
   GROUP BY Year) b
ON s.Year = b.Year
ORDER BY s.Year;