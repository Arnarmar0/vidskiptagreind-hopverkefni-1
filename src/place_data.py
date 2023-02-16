import pandas as pd
import openpyxl
import numpy as np

import psycopg2
import psycopg2.extras


def connect_to_postgres():
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
    return (cursor, connection)

def make_tables(cursor):
    # Create a table
    cursor.execute("DROP TABLE brautskraning;")
    cursor.execute("CREATE TABLE brautskraning (id serial PRIMARY KEY, Year integer, Braut varchar, tegund_nams varchar, kk integer, kv integer, samtals integer);")

    cursor.execute("DROP TABLE skraning;")
    cursor.execute("CREATE TABLE skraning (id serial PRIMARY KEY, Year integer, Braut varchar, tegund_nams varchar, kk integer, kv integer, samtals integer);")
    return cursor

def open_brautskraning():
    return pd.ExcelFile("data/brautskraning/all.xlsx")

def open_skraning():
    return pd.ExcelFile("data/skraning/all.xlsx")

def add_to_table(table, cursor, isbraut):
    sheet_list = table.sheet_names
    df_csv = {"Year": [], "Braut": [], "tegund_nams": [], "kk": [], "kv": [], "samtals": []}
    for sheet in sheet_list:
        print(sheet)
        df = table.parse(sheet)
        # print(df)
        df = df.dropna(thresh=4)
        df["Karl"].fillna(0, inplace=True)
        df["Kona"].fillna(0, inplace=True)
        df["Alls"].fillna(0, inplace=True)
        df = df.drop(columns=[df.columns[0]])
        # print(df)
        df = df.rename(columns={"Unnamed: 2": "tegund_nams"})

        df_isnan = df.isnull()

        temp_deild = ""
        # df.to_csv("test.csv")
        for i in df["Karl"].keys():
            if df_isnan['Deild'][i] == False:
                temp_deild = df["Deild"][i]
                df_csv["Year"].append(sheet)
                df_csv["Braut"].append(df["Deild"][i])
                df_csv["tegund_nams"].append(None)
                df_csv["kk"].append(df["Karl"][i])
                df_csv["kv"].append(df["Kona"][i])
                df_csv["samtals"].append(df["Alls"][i])

                if isbraut:
                    cursor.execute("INSERT INTO brautskraning (Year, Braut, tegund_nams, kk, kv, samtals) VALUES (%s, %s, %s, %s, %s, %s)", 
                            (sheet, df["Deild"][i], None, df["Karl"][i], df["Kona"][i], df["Alls"][i]))
                else:
                    cursor.execute("INSERT INTO skraning (Year, Braut, tegund_nams, kk, kv, samtals) VALUES (%s, %s, %s, %s, %s, %s)", 
                            (sheet, df["Deild"][i], None, df["Karl"][i], df["Kona"][i], df["Alls"][i]))
            else:
                df_csv["Year"].append(sheet)
                df_csv["Braut"].append(temp_deild)
                df_csv["tegund_nams"].append(df["tegund_nams"][i])
                df_csv["kk"].append(df["Karl"][i])
                df_csv["kv"].append(df["Kona"][i])
                df_csv["samtals"].append(df["Alls"][i])

                if isbraut:
                    cursor.execute("INSERT INTO brautskraning (Year, Braut, tegund_nams, kk, kv, samtals) VALUES (%s, %s, %s, %s, %s, %s)", 
                            (sheet, temp_deild, df["tegund_nams"][i], df["Karl"][i], df["Kona"][i], df["Alls"][i]))
                else:
                    cursor.execute("INSERT INTO skraning (Year, Braut, tegund_nams, kk, kv, samtals) VALUES (%s, %s, %s, %s, %s, %s)", 
                            (sheet, temp_deild, df["tegund_nams"][i], df["Karl"][i], df["Kona"][i], df["Alls"][i]))


    df_csv = pd.DataFrame(data=df_csv)
    if isbraut:
        df_csv.to_csv("braut_skra.csv", encoding="utf8")
    else:
        df_csv.to_csv("skraning_skra.csv", encoding="utf8")
    print("here")
    return cursor


if __name__ == '__main__':
    cursor, connection = connect_to_postgres()
    braut = open_brautskraning()
    skraning = open_skraning()
    cursor = make_tables(cursor)
    cursor = add_to_table(braut, cursor, True)
    cursor = add_to_table(skraning, cursor, False)
    connection.commit()

