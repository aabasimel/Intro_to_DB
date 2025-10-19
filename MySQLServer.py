# File: MySQLServer.py
# Description: Script to create the database alx_book_store in MySQL using mysql.connector and .env

import mysql.connector
from mysql.connector import Error
from dotenv import load_dotenv
import os

# Load environment variables from .env
load_dotenv()

HOST = os.getenv("DB_HOST")
USER = os.getenv("DB_USER")
PASSWORD = os.getenv("DB_PASSWORD")

connection = None

try:
    # Connect to MySQL server
    connection = mysql.connector.connect(
        host=HOST,
        user=USER,
        password=PASSWORD
    )

    if connection.is_connected():
        cursor = connection.cursor()
        # Create the database if it does not exist
        cursor.execute("CREATE DATABASE IF NOT EXISTS alx_book_store")
        print("Database 'alx_book_store' created successfully!")

except Error as e:
    print(f"Error while connecting to MySQL: {e}")

finally:
    if connection is not None and connection.is_connected():
        cursor.close()
        connection.close()
