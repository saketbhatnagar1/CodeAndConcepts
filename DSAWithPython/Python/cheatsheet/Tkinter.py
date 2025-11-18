# Tkinter Cheat Sheet - All in One
import tkinter as tk
from tkinter import messagebox, ttk
from PIL import Image, ImageTk  # for images

# ----------------- Main Window -----------------
root = tk.Tk()
root.title("Tkinter Cheat Sheet")
root.geometry("800x600")

# ----------------- Variables -----------------
str_var = tk.StringVar()
int_var = tk.IntVar()
bool_var = tk.BooleanVar(value=True)

# ----------------- Functions -----------------
def on_button_click():
    label.config(text=f"Hello, {entry.get() or 'User'}!")
    messagebox.showinfo("Info", f"Hello, {entry.get() or 'User'}!")

def check_status():
    print("Checkbox value:", bool_var.get())

def radio_selected():
    print("Selected option:", str_var.get())

def slider_changed(val):
    print("Slider value:", val)

def listbox_selected(event):
    selected = listbox.get(listbox.curselection())
    print("Listbox selected:", selected)

def open_new_window():
    top = tk.Toplevel(root)
    top.title("Toplevel Window")
    top.geometry("300x100")
    tk.Label(top, text="This is a new window").pack(pady=20)

# ----------------- Widgets -----------------
# Label
label = tk.Label(root, text="This is a Label", font=("Arial", 16), fg="blue")
label.pack(pady=10)

# Entry
entry = tk.Entry(root, width=30)
entry.pack(pady=5)
entry.insert(0, "Type here")

# Button
btn = tk.Button(root, text="Click Me", command=on_button_click, bg="green", fg="white")
btn.pack(pady=10)

# Checkbutton
check = tk.Checkbutton(root, text="Accept Terms", variable=bool_var, command=check_status)
check.pack()

# Radiobuttons
radio1 = tk.Radiobutton(root, text="Option 1", variable=str_var, value="Option 1", command=radio_selected)
radio2 = tk.Radiobutton(root, text="Option 2", variable=str_var, value="Option 2", command=radio_selected)
radio1.pack()
radio2.pack()

# Listbox
listbox = tk.Listbox(root, height=4)
for item in ["Apple", "Banana", "Cherry"]:
    listbox.insert(tk.END, item)
listbox.pack(pady=5)
listbox.bind("<<ListboxSelect>>", listbox_selected)

# Combobox
combo = ttk.Combobox(root, values=["Red", "Green", "Blue"])
combo.current(0)
combo.pack(pady=5)

# Scale / Slider
scale = tk.Scale(root, from_=0, to=100, orient=tk.HORIZONTAL, command=slider_changed)
scale.pack(pady=5)

# Canvas
canvas = tk.Canvas(root, width=200, height=100, bg="lightgray")
canvas.pack(pady=10)
canvas.create_rectangle(50, 20, 150, 80, fill="blue")
canvas.create_text(100, 50, text="Canvas Text", fill="white")

# Frame with widgets inside
frame = tk.Frame(root, bg="pink", padx=5, pady=5)
frame.pack(pady=10, fill="x")
tk.Label(frame, text="Inside Frame").pack(side="left", padx=5)
tk.Button(frame, text="Frame Button").pack(side="right", padx=5)

# Menu
menu = tk.Menu(root)
root.config(menu=menu)
file_menu = tk.Menu(menu, tearoff=0)
menu.add_cascade(label="File", menu=file_menu)
file_menu.add_command(label="New", command=lambda: print("New File"))
file_menu.add_command(label="Open", command=lambda: print("Open File"))
file_menu.add_separator()
file_menu.add_command(label="Exit", command=root.quit)

# Toplevel Window Button
tk.Button(root, text="Open New Window", command=open_new_window).pack(pady=5)

# Message Box Button
tk.Button(root, text="Show Message", command=lambda: messagebox.showwarning("Warning", "This is a warning")).pack(pady=5)

# ----------------- Image Example -----------------
try:
    img = Image.open("example.png")  # Replace with your image file
    photo = ImageTk.PhotoImage(img)
    tk.Label(root, image=photo).pack(pady=5)
except:
    tk.Label(root, text="Image not found (place example.png)").pack(pady=5)

# ----------------- Event Binding -----------------
def key_pressed(event):
    print("Key pressed:", event.char)

def mouse_clicked(event):
    print(f"Mouse clicked at ({event.x}, {event.y})")

root.bind("<Key>", key_pressed)
root.bind("<Button-1>", mouse_clicked)  # left click

# ----------------- After / Timer Example -----------------
root.after(3000, lambda: print("3 seconds passed"))

# ----------------- Start GUI -----------------
root.mainloop()
