import tkinter as tk

# Create a Tkinter window
root = tk.Tk()
root.title("Multiple Labels Example")

# Define a list of label texts
label_texts = ["Label 1", "Label 2", "Label 3", "Label 4", "Label 5"]

# Create and display labels using a loop
i = 1
while i <= 10:

    label = tk.Label(root, text="Hello World", background='red', fg = 'white')
    i = i + 1
    label.pack()

# Start the Tkinter main loop
root.mainloop()
