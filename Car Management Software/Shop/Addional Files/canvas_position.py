import tkinter as tk

def print_position(event):
    # Get the coordinates of the clicked point
    x, y = event.x, event.y
    
    # Check if the coordinates are within the range of the printed numbers
    for number, (text_x, text_y) in number_positions.items():
        if text_x - 10 <= x <= text_x + 10 and text_y - 10 <= y <= text_y + 10:
            print(f"Clicked on number {number} at position X: {text_x}, Y: {text_y}")
            break

root = tk.Tk()

canvas = tk.Canvas(root, width=300, height=200)
canvas.pack()

number_positions = {}

# Using a for loop to print numbers from 1 to 10 from top to bottom
for i in range(1, 11):
    y_position = (i - 1) * 20  # Adjust the spacing between numbers
    text_item = canvas.create_text(150, y_position, text=str(i), font=("Arial", 12))
    
    # Store the coordinates of each number
    number_positions[i] = canvas.coords(text_item)

# Bind a mouse click event to print the position
canvas.bind("<Button-1>", print_position)

root.mainloop()
