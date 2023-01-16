import sys
import os
from os.path import join, dirname
from dotenv import load_dotenv
import pandas as pd
import mysql.connector
from mysql.connector import Error


def connectToDatabase(HOST, PORT, USER, PASSWORD, DATABASE):
    try:
        conn = mysql.connector.connect(
            host=HOST,
            port=PORT,
            user=USER,
            password=PASSWORD,
            database=DATABASE
        )

        if conn.is_connected():
            cursor = conn.cursor()
            cursor.execute("select database()")
            
            print("Connected to database: " + cursor.fetchone()[0])

        return conn
            
    except Error as e:
        print("Error while connecting to database: ", e)


def uploadCSV(dbConn, f, tbl, cols):
    cursor = dbConn.cursor()
    for i,row in f.iterrows():
        
        #print(tuple(row))
        sqlStatement = "insert into " + tbl + "(" + cols + ") values (%s,%s,%s)"
        cursor.execute(sqlStatement, tuple(row))

if __name__=="__main__":
    dotenv_path = join(dirname(__file__), '.env')
    load_dotenv(dotenv_path)

    HOST = os.environ.get("HOST")
    PORT = os.environ.get("PORT")
    USER = os.environ.get("USER")
    PASSWORD = os.environ.get("PASSWORD")
    DATABASE = os.environ.get("DATABASE")
    LANDING_TABLE_NAME = os.environ.get("LANDING_TABLE_NAME")
    LANDING_COLUMNS = os.environ.get("LANDING_COLUMNS")
    
    csvPath = sys.argv[1]
    print("File Path: " + csvPath)
    csvFile = pd.read_csv(csvPath, header=None)

    databaseConnection = connectToDatabase(HOST, PORT, USER, PASSWORD, DATABASE)
    uploadCSV(databaseConnection, csvFile, LANDING_TABLE_NAME, LANDING_COLUMNS)


    
