from tkinter import *
from PIL import Image, ImageTk

# Function to create a rounded rectangle on the canvas
def create_rounded_rectangle(canvas, x1, y1, x2, y2, radius, **kwargs):
    """Draw a rounded rectangle."""
    # Draw the four corners
    canvas.create_oval(x1, y1, x1 + 2 * radius, y1 + 2 * radius, **kwargs)
    canvas.create_oval(x2 - 2 * radius, y1, x2, y1 + 2 * radius, **kwargs)
    canvas.create_oval(x1, y2 - 2 * radius, x1 + 2 * radius, y2, **kwargs)
    canvas.create_oval(x2 - 2 * radius, y2 - 2 * radius, x2, y2, **kwargs)
    # Draw the four rectangles
    canvas.create_rectangle(x1 + radius, y1, x2 - radius, y2, **kwargs)
    canvas.create_rectangle(x1, y1 + radius, x2, y2 - radius, **kwargs)

# Function to handle the start button click
def start_button_click():
    root.withdraw()  # Hide the main window
    open_calculator()  # Open the compound interest calculator

# Function to open the compound interest calculator window
def open_calculator():
    calculator_window = Toplevel(root)
    calculator_window.title("Compound Interest Calculator")
    photo = PhotoImage(file = "Python Project/Black and Teal Modern Letter C Technology Logo Design (1).png")
    calculator_window.iconphoto(False, photo)

    # Set the size of the calculator window to match the main window
    width = root.winfo_width()
    height = root.winfo_height()
    calculator_window.geometry(f"{width}x{height}")
    calculator_window.configure(background="black")

    # Make the calculator window not resizable
    calculator_window.resizable(False, False)
    # icon phot
    # calculator_window.iconphoto(False, icon)

    # Create a frame for the labels and entry fields
    frame = LabelFrame(calculator_window, text="Enter Value Here", padx=50, pady=60, bg="black", fg='white')
    frame.pack(padx=10, pady=30, expand=True, fill=BOTH)

    # Define a font for the labels
    label_font = ("Albertus", 14)

    # Create labels
    label1 = Label(frame, text="Principal Amount (Rs):", fg='white', bg='#008c87', font=label_font)
    label2 = Label(frame, text="Rate (%):", fg='white', bg='#008c87', font=label_font)
    label3 = Label(frame, text="Time (years):", fg='white', bg='#008c87', font=label_font)
    label4 = Label(frame, text="Compound Interest:", fg='white', bg='#008c87', font=label_font)
    # Define a font for the entry fields
    entry_font = ("Arial", 14)
    entry_width = 15
    # Create entry fields
    principal_field = Entry(frame, font=entry_font, width=entry_width)
    rate_field = Entry(frame, font=entry_font, width=entry_width)
    time_field = Entry(frame, font=entry_font, width=entry_width)
    compound_field = Entry(frame, font=entry_font, width=entry_width)

    # Define a font and padding for the buttons
    button_font = ("Arial", 14)
    button_padx = 5
    button_pady = 5

    # Create buttons
    button1 = Button(frame, text="Submit", bg="#008c87", fg="black",
                     font=button_font, padx=button_padx, pady=button_pady,
                     command=lambda: calculate_ci(principal_field, rate_field, time_field, compound_field))
    button2 = Button(frame, text="Clear", bg="#008c87", fg="black",
                     font=button_font, padx=button_padx, pady=button_pady,
                     command=lambda: clear_all(principal_field, rate_field, time_field, compound_field))

    # Layout the widgets in the frame
    label1.grid(row=0, column=0, padx=10, pady=10, sticky=W)
    principal_field.grid(row=0, column=1, padx=10, pady=10)
    
    label2.grid(row=1, column=0, padx=10, pady=10, sticky=W)
    rate_field.grid(row=1, column=1, padx=10, pady=10)
    
    label3.grid(row=2, column=0, padx=10, pady=10, sticky=W)
    time_field.grid(row=2, column=1, padx=10, pady=10)
    
    label4.grid(row=4, column=0, padx=10, pady=10, sticky=W)
    compound_field.grid(row=4, column=1, padx=10, pady=10)
    
    button1.grid(row=3, column=1, pady=5, sticky=E)
    button2.grid(row=5, column=1, pady=5, sticky=E)

# Function to clear the contents of all entry boxes
def clear_all(principal_field, rate_field, time_field, compound_field):
    principal_field.delete(0, END)
    rate_field.delete(0, END)
    time_field.delete(0, END)
    compound_field.delete(0, END)
    principal_field.focus_set()

# Function to calculate compound interest
def calculate_ci(principal_field, rate_field, time_field, compound_field):
    try:
        principal = float(principal_field.get())
        rate = float(rate_field.get())
        time = int(time_field.get())
        CI = principal * (pow((1 + rate / 100), time))
        compound_field.delete(0, END)  # Clear previous results
        compound_field.insert(0, f"{CI:.2f}")
    except ValueError:
        compound_field.delete(0, END)
        compound_field.insert(0, "Invalid Input")

# Create the main window
root = Tk()
root.title("Main Window")
photo = PhotoImage(file = "Python Project/Black and Teal Modern Letter C Technology Logo Design (1).png")
root.iconphoto(False, photo)

# Load the image
image_path = "Python Project/Black and Teal Modern Letter C Technology Logo Design (1).png"
original_image = Image.open(image_path)
photo_image = ImageTk.PhotoImage(original_image)

# Set the size of the main window to match the image size
root.geometry(f"{photo_image.width()}x{photo_image.height()}")
root.configure(background="#008080")

# Make the calculator window not resizable
root.resizable(False, False)

# Create a canvas to display the image
canvas = Canvas(root, width=photo_image.width(), height=photo_image.height())
canvas.pack(fill=BOTH, expand=YES)



# Add the image to the canvas
canvas.create_image(0, 0, anchor=NW, image=photo_image)

# Button properties
button_width = 150
button_height = 50
border_radius = 25
button_color = "#008c87"
text_color = "white"
font_size = 16

# Draw the rounded rectangle button on the canvas
button_x = photo_image.width() // 2 - button_width // 2
button_y = photo_image.height() - button_height - 30

create_rounded_rectangle(canvas, button_x, button_y, button_x + button_width, button_y + button_height, border_radius,
                         fill=button_color, outline=button_color)

# Add the button text on top of the rounded rectangle
canvas.create_text(button_x + button_width // 2, button_y + button_height // 2, text="Start", fill=text_color,
                   font=("Arial", font_size))

# Function to handle clicks on the canvas
def on_canvas_click(event):
    if (button_x <= event.x <= button_x + button_width and
        button_y <= event.y <= button_y + button_height):
        start_button_click()

# Bind the click event to the function
canvas.bind("<Button-1>", on_canvas_click)

# Start the Tkinter event loop
root.mainloop()
