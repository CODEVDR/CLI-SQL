#importing Modules
import os
from IPython.display import display
import mysql.connector as sqlctr
from mysql.connector import Error
import pandas as pd

#server connection
def create_server_connection(userpassword):
    connection = None
    try:
        connection = sqlctr.connect(
            host="localhost",
            user="root",
            password=userpassword
        )
        print("Database Login Sucessfull")
    except:
        print("Incorrect Password")
        pass
    return connection


def create_db_connection(userpassword, db_name):
    connection = None
    try:
        connection = sqlctr.connect(
            host="localhost",
            user="root",
            password=userpassword,
            database=db_name
        )
    except:
        pass
    return connection


def create_database(connection, query):
    cursor = connection.cursor()
    try:
        cursor.execute(query)
    except:
        pass


def exe_query(connection, query):
    cursor = connection.cursor()
    try:
        cursor.execute(query)
        connection.commit()
    except:
       pass


def read_query(connection, query):
    cursor = connection.cursor()
    result = None
    try:
        cursor.execute(query)
        result = cursor.fetchall()
        return result
    except:
        pass
