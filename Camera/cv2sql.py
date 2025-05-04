import cv2
import mysql.connector
import numpy as np

# Connect to MySQL database
connection = mysql.connector.connect(
    host='localhost',
    user='root',
    password='',
    database='videocam'
)

# Sample image file path
image_file = 'image.jpg'

# Read the image using OpenCV
image = cv2.imread(image_file)

# Encode the image as a byte array
retval, buffer = cv2.imencode('.jpg', image)
image_bytes = buffer.tobytes()

# Insert image data into the database
try:
    cursor = connection.cursor()
    sql = "INSERT INTO video_data (video) VALUES (%s)"
    cursor.execute(sql, (image_bytes,))
    connection.commit()
    cursor.close()
except mysql.connector.Error as err:
    print("Error:", err)

# Retrieve image data from the database
try:
    cursor = connection.cursor()
    sql = "SELECT video FROM video_data"
    cursor.execute(sql)
    result = cursor.fetchone()
    cursor.close()
    image_data = result[0]
    print(b'{image_data}')
except mysql.connector.Error as err:
    print("Error:", err)

# Decode the image data
image_from_db = cv2.imdecode(np.frombuffer(image_data, np.uint8), cv2.IMREAD_COLOR)

# Display the retrieved image
cv2.imshow('Image from Database', image_from_db)
cv2.waitKey(0)
cv2.destroyAllWindows()

# Close the database connection
connection.close()
