import mysql.connector
import time

def connect_to_database(host, user, password, database):
    """Connect to the MySQL database."""
    connection = mysql.connector.connect(
        host='localhost',
        user='root',
        password='',
        database='chat_room'
    )
    return connection

def retrieve_data(connection):
    """Retrieve data from the MySQL database in real-time."""
    cursor = connection.cursor(dictionary=True)

    while True:
        # Execute your SQL query here
        cursor.execute("SELECT * FROM acoount")

        # Fetch all the rows
        rows = cursor.fetchall()

        # Process the data or print it
        for row in rows:
            print(row)

        # Wait for a certain interval (e.g., 1 second)
        time.sleep(1)

if __name__ == "__main__":
    # Replace these with your MySQL connection details
    db_host = 'localhost'
    db_user = 'root'
    db_password = ''
    db_name = 'chat_room'

    # Connect to the database
    db_connection = connect_to_database(db_host, db_user, db_password, db_name)

    try:
        # Retrieve and print data in real-time
        retrieve_data(db_connection)

    except KeyboardInterrupt:
        # Close the database connection when the program is interrupted (e.g., Ctrl+C)
        db_connection.close()
        print("Connection closed.")
