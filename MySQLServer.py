import mysql.connector  # MUST be present
from mysql.connector import Error

def create_database():
    connection = None
    try:
        connection = mysql.connector.connect(
            host="localhost",
            user="root",
            password="Ant0ny@05TG!tee" 
        )

        if connection.is_connected():
            cursor = connection.cursor()
            cursor.execute("CREATE DATABASE IF NOT EXISTS alxbookstore")  
            print("Database 'alxbookstore' created successfully!")
            cursor.close()

    except Error as e:
        print(f"Error: {e}")

    finally:
        if connection and connection.is_connected():
            connection.close()

if __name__ == "__main__":
    create_database()

