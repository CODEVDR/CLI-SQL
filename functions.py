#import Modules
from IPython.display import display
import mysql.connector
from mysql.connector import Error
import pandas as pd


def create_server_connection(hostname, username, userpassword):
    connection = None
    try:
        connection = mysql.connector.connect(
            host=hostname,
            user=username,
            password=userpassword
        )
        print("Database Login Sucessfull")
    except:
        print("Sucess")
    return connection


def create_db_connection(host_name, user_name, userpassword, db_name):
    connection = None
    try:
        connection = mysql.connector.connect(
            host=host_name,
            user=user_name,
            password=userpassword,
            database=db_name
        )
    except:
        print("Sucess")
    return connection


def create_database(connection, query):
    cursor = connection.cursor()
    try:
        cursor.execute(query)
    except:
        print(f"Sucess")


def exe_query(connection, query):
    cursor = connection.cursor()
    try:
        cursor.execute(query)
        connection.commit()
    except Error as err:
        print(f"Error: {err}")


def read_query(connection, query):
    cursor = connection.cursor()
    result = None
    try:
        cursor.execute(query)
        result = cursor.fetchall()
        return result
    except Error as err:
        print(f"Error: '{err}'")
