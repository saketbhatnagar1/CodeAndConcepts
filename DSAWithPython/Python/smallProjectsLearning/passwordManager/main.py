from tkinter import *
from tkinter import messagebox
import pyperclip
import random, string, os, json
from dotenv import load_dotenv

load_dotenv()

# ---------------------------- PASSWORD GENERATOR ------------------------------- #
numbers = [str(n) for n in range(10)]
alphabets = [chr(letter) for letter in range(97,123)] + [chr(x) for x in range(97, 123)]
symbols  = list(string.punctuation)

def passwordGenerator(length=12):
    if length < 4:
        raise ValueError("Password length should be at least 4 characters.")
    password = [
        random.choice(numbers),
        random.choice(alphabets),
        random.choice(symbols),
        random.choice(alphabets)
    ]
    all_chars = numbers + alphabets + symbols
    password += random.choices(all_chars, k=length-4)
    random.shuffle(password)
    password = "".join(password)
    password_entry.delete(0, END)
    password_entry.insert(0, password)
    pyperclip.copy(password)
    return password

# ---------------------------- SAVE PASSWORD ------------------------------- #
def validate(email,password,website):
    return True

def save_password():
    folder = os.environ.get("password_path")
    website = website_entry.get()
    email = email_entry.get()
    password = password_entry.get()

    new_data = {website: {"email": email, "password": password}}

    if not website or not email or not password:
        messagebox.showwarning(title="Oops", message="Please don't leave any fields empty!")
        return

    is_ok = messagebox.askokcancel(
        title=website,
        message=f"Confirm Details\nEmail: {email}\nPassword: {password}"
    )

    if is_ok:
        os.makedirs(folder, exist_ok=True)
        actual_file_path = os.path.join(folder, "data.json")

        try:
            with open(actual_file_path, "r") as file:
                data = json.load(file)
        except FileNotFoundError:
            data = {}

        data.update(new_data)

        with open(actual_file_path, "w") as file:
            json.dump(data, file, indent=4)

        website_entry.delete(0, END)
        password_entry.delete(0, END)

# ---------------------------- SEARCH PASSWORD ------------------------------- #
def find_password():
    folder = os.environ.get("password_path")
    actual_file_path = os.path.join(folder, "data.json")
    website = website_entry.get()

    if not website:
        messagebox.showwarning(title="Oops", message="Please enter a website to search.")
        return

    try:
        with open(actual_file_path, "r") as file:
            data = json.load(file)
            details = data.get(website)
            if details:
                email = details.get("email")
                password = details.get("password")
                messagebox.showinfo(title=website, message=f"Email: {email}\nPassword: {password}")
            else:
                messagebox.showinfo(title="Error", message="No details found for this website.")
    except FileNotFoundError:
        messagebox.showinfo(title="Error", message="No Data File Found / No passwords saved yet.")

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager")
window.config(padx=40, pady=40, bg="#f5f5f5")

# --- Logo ---
canvas = Canvas(window, height=200, width=200, bg="#f5f5f5", highlightthickness=0)
logo_img = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo_img)
canvas.grid(row=0, column=1, pady=(0,20))

# --- Labels ---
website_label = Label(window, text="Website:", bg="#f5f5f5")
website_label.grid(row=1, column=0, sticky="e", pady=5)
email_label = Label(window, text="Email/Username:", bg="#f5f5f5")
email_label.grid(row=2, column=0, sticky="e", pady=5)
password_label = Label(window, text="Password:", bg="#f5f5f5")
password_label.grid(row=3, column=0, sticky="e", pady=5)

# --- Entries ---
website_entry = Entry(window, width=35)
website_entry.grid(row=1, column=1, columnspan=2, sticky="w")
website_entry.focus()

email_entry = Entry(window, width=35)
email_entry.grid(row=2, column=1, columnspan=2, sticky="w")
email_entry.insert(0, "saketbhatnagar2@gmail.com")

password_entry = Entry(window, width=21)
password_entry.grid(row=3, column=1, sticky="w")

# --- Buttons ---
search_button = Button(window, text="Search", width=14, command=find_password)
search_button.grid(row=1, column=2, padx=5)

generate_password_button = Button(window, text="Generate Password", command=passwordGenerator)
generate_password_button.grid(row=3, column=2, padx=5)

add_button = Button(window, text="Add", width=36, command=save_password)
add_button.grid(row=4, column=1, columnspan=2, pady=20)

window.mainloop()
