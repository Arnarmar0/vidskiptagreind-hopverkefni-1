import pandas as pd
import openpyxl

import psycopg2
import psycopg2.extras

# Connect to the database
conn = psycopg2.connect("dbname=vidskiptagreind_hop1 user=postgres password=ykkarPasswordHér port=5432")

# Create a cursor object
cur = conn.cursor()

# Create a dictionary cursor
cur = conn.cursor(cursor_factory=psycopg2.extras.DictCursor)

# Create a table
cur.execute("CREATE TABLE test (id serial PRIMARY KEY, num integer, data varchar);")

# Insert some data

# Insert one row
cur.execute("INSERT INTO test (num, data) VALUES (%s, %s)", (100, "abc'def"))

# Insert multiple rows
cur.executemany("INSERT INTO test (num, data) VALUES (%s, %s)", [(1, "abc"), (2, "def")])

# Query the database and obtain data as Python objects
cur.execute("SELECT * FROM test;")
cur.fetchone()
cur.fetchmany(2)
cur.fetchall()


# Close the cursor
cur.close()

# Commit the transaction
conn.commit()

# Close the connection
conn.close()

#
# years = ['2006-01', '2006-02',
#          '2007-01', '2007-02',
#          '2008-01', '2008-02',
#          '2009-01', '2009-02',
#          '2010-01', '2010-02',
#          '2011-01', '2011-02',
#          '2012-01', '2012-02',
#          '2013-01', '2013-02',
#          '2014-01', '2014-02',
#          '2015-01', '2015-02',
#          '2016-01', '2016-02',
#          '2017-01', '2017-02',
#          '2018-01', '2018-02',
#          '2019-01', '2019-02',
#          '2020-01', '2020-02',
#          '2021-01', '2021-02']

# for year in years:

