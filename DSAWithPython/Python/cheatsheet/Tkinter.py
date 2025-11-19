"""
===========================
   TKINTER CHEAT SHEET
 Full Code + Full Explanation
===========================

This file explains:
- Tkinter window creation
- Variables (StringVar, IntVar, BooleanVar)
- Labels, Buttons, Entry, Checkboxes, Radiobuttons
- Listbox, Combobox, Scale, Canvas
- Frames, Menus, Toplevel windows
- MessageBoxes
- Event binding (keyboard + mouse)
- Using images with Tkinter (PIL)
- Using .after() / timers
"""

import tkinter as tk                 # Main Tkinter module
from tkinter import messagebox, ttk  # Message dialogues + themed widgets
from PIL import Image, ImageTk       # To display images

# -----------------------------------------------------------
# 1. MAIN WINDOW
# -----------------------------------------------------------

root = tk.Tk()                       # Create the main application window
root.title("Tkinter Full Cheat Sheet")  # Window title
root.geometry("900x700")                # Window size (width x height)

# -----------------------------------------------------------
# 2. TKINTER VARIABLE TYPES
# -----------------------------------------------------------

str_var = tk.StringVar()              # Stores text
int_var = tk.IntVar()                 # Stores integers
bool_var = tk.BooleanVar(value=True)  # Stores True/False values

# -----------------------------------------------------------
# 3. FUNCTIONS (EVENT HANDLERS)
# -----------------------------------------------------------

def on_button_click():
    """Triggered when the main button is clicked."""
    value = entry.get() or "User"     # If empty → use "User"
    label.config(text=f"Hello, {value}!")  # Update the label
    messagebox.showinfo("Info", f"Hello, {value}!")  # Popup message

def check_status():
    """Triggered when checkbox is clicked."""
    print("Checkbox value:", bool_var.get())

def radio_selected():
    """Triggered when a radiobutton is selected."""
    print("Selected option:", str_var.get())

def slider_changed(val):
    """Triggered when slider moves."""
    print("Slider value:", val)

def listbox_selected(event):
    """Triggered when listbox item is selected."""
    selected = listbox.get(listbox.curselection())
    print("Listbox selected:", selected)

def open_new_window():
    """Creates a new small popup window."""
    top = tk.Toplevel(root)             # New window
    top.title("Toplevel Window")
    top.geometry("300x100")
    tk.Label(top, text="This is a new window").pack(pady=20)

# -----------------------------------------------------------
# 4. WIDGETS
# -----------------------------------------------------------

# LABEL — used to display text
label = tk.Label(root, text="This is a Label", font=("Arial", 18), fg="blue")
label.pack(pady=10)

# ENTRY — single-line text input
entry = tk.Entry(root, width=30)
entry.pack(pady=5)
entry.insert(0, "Type here")            # Pre-filled text

# BUTTON — triggers a function when clicked
btn = tk.Button(root, text="Click Me", command=on_button_click,
                bg="green", fg="white")
btn.pack(pady=10)

# CHECKBUTTON — toggle ON/OFF
check = tk.Checkbutton(root, text="Accept Terms",
                       variable=bool_var, command=check_status)
check.pack()

# RADIOBUTTONS — multiple options but only ONE can be selected
radio1 = tk.Radiobutton(root, text="Option 1",
                        variable=str_var, value="Option 1",
                        command=radio_selected)
radio2 = tk.Radiobutton(root, text="Option 2",
                        variable=str_var, value="Option 2",
                        command=radio_selected)
radio1.pack()
radio2.pack()

# LISTBOX — displays a list of selectable items
listbox = tk.Listbox(root, height=4)
for item in ["Apple", "Banana", "Cherry"]:
    listbox.insert(tk.END, item)        # END = add at bottom
listbox.pack(pady=5)
listbox.bind("<<ListboxSelect>>", listbox_selected)  # Bind selection event

# COMBOBOX — drop-down menu (from ttk: modern widgets)
combo = ttk.Combobox(root, values=["Red", "Green", "Blue"])
combo.current(0)                       # Set default item
combo.pack(pady=5)

# SCALE (Slider)
scale = tk.Scale(root, from_=0, to=100,
                 orient=tk.HORIZONTAL, command=slider_changed)
scale.pack(pady=5)

# CANVAS — drawing area (shapes, text, images)
canvas = tk.Canvas(root, width=250, height=120, bg="lightgray")
canvas.pack(pady=10)
canvas.create_rectangle(50, 20, 180, 80, fill="blue")   # Draw rectangle
canvas.create_text(120, 50, text="Canvas Text", fill="white")  # Add text

# FRAME — used to group widgets in a container
frame = tk.Frame(root, bg="pink", padx=10, pady=10)
frame.pack(pady=10, fill="x")
tk.Label(frame, text="Inside Frame").pack(side="left", padx=5)
tk.Button(frame, text="Frame Button").pack(side="right", padx=5)

# -----------------------------------------------------------
# 5. MENUS
# -----------------------------------------------------------

menu = tk.Menu(root)      # Main menu bar
root.config(menu=menu)

file_menu = tk.Menu(menu, tearoff=0)  # "tearoff=0" removes dashed line
menu.add_cascade(label="File", menu=file_menu)

file_menu.add_command(label="New", command=lambda: print("New File"))
file_menu.add_command(label="Open", command=lambda: print("Open File"))
file_menu.add_separator()             # Horizontal separator line
file_menu.add_command(label="Exit", command=root.quit)

# -----------------------------------------------------------
# 6. BUTTON TO OPEN TOPLEVEL WINDOW
# -----------------------------------------------------------

tk.Button(root, text="Open New Window", command=open_new_window).pack(pady=5)

# -----------------------------------------------------------
# 7. MESSAGE BOX BUTTON
# -----------------------------------------------------------

tk.Button(root, text="Show Message",
          command=lambda: messagebox.showwarning("Warning", "This is a warning")
          ).pack(pady=5)

# -----------------------------------------------------------
# 8. LOADING IMAGES WITH PIL
# -----------------------------------------------------------

try:
    img = Image.open("example.png")     # Replace with your file
    img = img.resize((120, 120))
    photo = ImageTk.PhotoImage(img)
    tk.Label(root, image=photo).pack(pady=5)

except Exception:
    tk.Label(root, text="Image not found (place example.png)").pack(pady=5)

# -----------------------------------------------------------
# 9. EVENT BINDING
# -----------------------------------------------------------

def key_pressed(event):
    """Triggered when a key is typed."""
    print("Key pressed:", event.char)

def mouse_clicked(event):
    """Triggered when left mouse button is clicked."""
    print(f"Mouse clicked at x={event.x}, y={event.y}")

root.bind("<Key>", key_pressed)        # Key press event
root.bind("<Button-1>", mouse_clicked) # Left mouse click

# -----------------------------------------------------------
# 10. AFTER() — TIMER / DELAY
# -----------------------------------------------------------

root.after(3000, lambda: print("3 seconds passed"))  # Executes after 3 sec

# -----------------------------------------------------------
# 11. START GUI LOOP
# -----------------------------------------------------------

root.mainloop()    # Keeps window running until manually closed
