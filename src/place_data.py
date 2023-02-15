import pandas as pd
import openpyxl
import numpy as np

import psycopg2
import psycopg2.extras

# Connect to the database
connection  = psycopg2.connect(user="postgres",
                        password="1234",
                        host="localhost",
                        port="5432",
                        database="Vidskiptagreind_hop1")


# # Create a dictionary cursor
cursor = connection.cursor()
# Print PostgreSQL details
print("PostgreSQL server information")
print(connection.get_dsn_parameters(), "\n")
# Executing a SQL query
cursor.execute("SELECT version();")
# Fetch result
record = cursor.fetchone()
print("You are connected to - ", record, "\n")

# Create a table
cursor.execute("DROP TABLE brautskraning;")
cursor.execute("CREATE TABLE brautskraning (id serial PRIMARY KEY, Year integer, Braut varchar, tegund_nams varchar, kk integer, kv integer, samtals integer);")

braut = pd.ExcelFile("data/brautskraning/all.xlsx")

sheet_list = braut.sheet_names

for sheet in sheet_list[1::]:
    print(sheet)
    df = braut.parse(sheet)
    df = df.dropna(thresh=4)
    df["Karl"].fillna(0, inplace=True)
    df["Kona"].fillna(0, inplace=True)
    df["Alls"].fillna(0, inplace=True)
    df = df.drop(columns=[df.columns[0]])
    df = df.rename(columns={"Unnamed: 2": "tegund_nams"})

    df_isnan = df.isnull()

    temp_deild = ""

    for i in df["Karl"].keys():
        if df_isnan['Deild'][i] == False:
            temp_deild = df["Deild"][i]
            cursor.execute("INSERT INTO brautskraning (Year, Braut, tegund_nams, kk, kv, samtals) VALUES (%s, %s, %s, %s, %s, %s)", 
                           (sheet, df["Deild"][i], None, df["Karl"][i], df["Kona"][i], df["Alls"][i]))
        else:
            cursor.execute("INSERT INTO brautskraning (Year, Braut, tegund_nams, kk, kv, samtals) VALUES (%s, %s, %s, %s, %s, %s)", 
                           (sheet, temp_deild, df["tegund_nams"][i], df["Karl"][i], df["Kona"][i], df["Alls"][i]))

connection.commit()

