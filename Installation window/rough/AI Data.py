import mysql.connector
import tkinter as tk

# Create the main GUI window
root = tk.Tk()
root.title("MySQL Data Display")

# Establish a database connection
db_connection = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Tanmay1@",
    database="chat_room"
)
cursor = db_connection.cursor()

# Execute an SQL query
query = "SELECT * FROM chat"
cursor.execute(query)

# Fetch and process data
data = cursor.fetchall()

# Display data in the GUI
for row_index, row_data in enumerate(data):
    for col_index, col_value in enumerate(row_data):
        label = tk.Label(root, text=col_value)
        label.grid(row=row_index, column=col_index)

# Close the database connection when done
cursor.close()
db_connection.close()

# Start the Tkinter main loop
root.mainloop()
