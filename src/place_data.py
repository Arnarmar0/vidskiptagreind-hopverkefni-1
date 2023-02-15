import pandas as pd
import openpyxl
import numpy as np

import psycopg2
import psycopg2.extras

# Connect to the database
conn = psycopg2.connect("dbname=Vidskiptagreind_hop1 user=postgres password=1234 port=5432")
print(conn)

# Create a cursor object
cur = conn.cursor()

# # Create a dictionary cursor
cur = conn.cursor(cursor_factory=psycopg2.extras.DictCursor)

# Create a table
cur.execute("CREATE TABLE brautskraning (id serial PRIMARY KEY, Year integer, Braut varchar, tegund_nams varchar, kk integer, kv integer, samtals integer);")

braut = pd.ExcelFile("data/brautskraning/all.xlsx")

sheet_list = braut.sheet_names

for sheet in sheet_list[1::]:
    df = braut.parse(sheet)
    df = df.dropna(thresh=4)
    df["Karl"].fillna(0, inplace=True)
    df["Kona"].fillna(0, inplace=True)
    df["Alls"].fillna(0, inplace=True)

    # print(df)
    df = df.drop(columns=[df.columns[0]])
    # print(df)
    df = df.rename(columns={"Unnamed: 2": "tegund_nams"})

    # df  = df.to_csv("test2.csv", encoding="utf-8-sig")
    df_isnan = df.isnull()
    # print(df_isnan)
    # Insert some data
    temp_year = []
    temp_deild = []
    temp_tegund_nams = []
    temp_kk = []
    temp_kv = []
    temp_total = []
    counter = 0

    for i in df["Karl"].keys():
        if df_isnan['Deild'][i] == False:
            temp_deild.append(df["Deild"][i])
            temp_tegund_nams.append(None)
            temp_kk.append(df["Karl"][i])
            temp_kv.append(df["Kona"][i])
            temp_total.append(df["Alls"][i])
        else:
            temp_deild.append(temp_deild[-1])
            temp_tegund_nams.append(df["tegund_nams"][i])
            temp_kk.append(df["Karl"][i])
            temp_kv.append(df["Kona"][i])
            temp_total.append(df["Alls"][i])

    for i in range(len(temp_deild)):
        print("made")
        cur.execute("INSERT INTO brautskraning (Year, Braut, tegund_nams, kk, kv, samtals) VALUES (%s, %s, %s, %s, %s, %s)", (sheet, temp_deild[i], temp_tegund_nams[i], temp_kk[i], temp_kv[i], temp_total[i]))

# Insert one row
# cur.execute("INSERT INTO test (num, data) VALUES (%s, %s)", (100, "abc'def"))

# # Insert multiple rows
# cur.executemany("INSERT INTO test (num, data) VALUES (%s, %s)", [(1, "abc"), (2, "def")])

# # Query the database and obtain data as Python objects
# cur.execute("SELECT * FROM test;")
# cur.fetchone()
# cur.fetchmany(2)
# cur.fetchall()


# # Close the cursor
# cur.close()

# # Commit the transaction
# conn.commit()

# # Close the connection
# conn.close()

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

