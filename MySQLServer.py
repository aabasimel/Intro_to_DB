# File: MySQLServer.py
# Description: Script to create the database alx_book_store in MySQL using .env for credentials

import pymysql
from dotenv import load_dotenv
import os

# Load environment variables from .env
load_dotenv()

HOST = os.getenv("DB_HOST")
USER = os.getenv("DB_USER")
PASSWORD = os.getenv("DB_PASSWORD")

connection = None
cursor = None

try:
    # Connect to MySQL server
    connection = pymysql.connect(
        host=HOST,
        user=USER,
        password=PASSWORD
    )

    cursor = connection.cursor()

    # SQL query to create the database
    create_db_query = "CREATE DATABASE IF NOT EXISTS alx_book_store"
    cursor.execute(create_db_query)

    print("Database 'alx_book_store' created successfully!")

except pymysql.MySQLError as e:
    print(f"Error while connecting to MySQL: {e}")

finally:
    if cursor is not None:
        cursor.close()
    if connection is not None:
        connection.close()
