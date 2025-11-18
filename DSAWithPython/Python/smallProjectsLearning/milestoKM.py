# Import all classes and functions from the tkinter module
from tkinter import *

# Function to convert miles to kilometers
def miles_to_km():
    # Get the value from the input box, convert it to float
    miles = float(miles_input.get())
    # Convert miles to kilometers
    km = miles * 1.609
    # Update the result label with the calculated kilometers
    Kilometer_result_label.config(text=f"{km}")

# Create the main window
window = Tk()
# Set the window title
window.title("Miles To Km Converter")
# Add padding around the window (20 pixels on each side)
window.config(padx=20, pady=20)

# Create an Entry widget for user to input miles
miles_input = Entry(width=7)
# Place the input box in the grid (column 1, row 0)
miles_input.grid(column=1, row=0)

# Create a label that says "Miles" next to the input box
miles_label = Label(text="Miles")
miles_label.grid(column=2, row=0)

# Create a label that says "is equal to" in the result row
is_equal_label = Label(text="is equal to")
is_equal_label.grid(column=0, row=1)

# Create a label to display the conversion result, initially "0"
Kilometer_result_label = Label(text="0")
Kilometer_result_label.grid(column=1, row=1)

# Create a label for the unit "Km" next to the result
Kilometer_Label = Label(text="Km")
Kilometer_Label.grid(column=2, row=1)

# Create a button that calls the miles_to_km function when clicked
calculate_button = Button(text="Convert", command=miles_to_km)
calculate_button.grid(column=1, row=2)

# Start the Tkinter event loop (keeps the window open)
window.mainloop()
