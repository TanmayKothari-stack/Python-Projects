import mysql.connector
import tkinter as tk

# Connect to MySQL database
conn = mysql.connector.connect(
    host='localhost',
    user='root',
    password='',
    database='shopping'
)
cursor = conn.cursor()

# Execute a SELECT query
cursor.execute('SELECT * FROM customer_login')
data = cursor.fetchall()

# Close the database connection
conn.close()

# Create Tkinter window
root = tk.Tk()

# Create Tkinter canvas
canvas = tk.Canvas(root, width=400, height=300)
canvas.place(x=50, y=50)  # Adjust the coordinates based on your preference

# Display data on canvas with proper spacing on the y-axis
y_offset = 20  # Adjust this value based on your spacing needs

for row in data:
    # Assuming row[1] contains the data you want to display
    canvas.create_text(200, y_offset, text=str(row[1]), anchor='w')
    y_offset += 30  # Adjust the spacing between items

root.mainloop()
