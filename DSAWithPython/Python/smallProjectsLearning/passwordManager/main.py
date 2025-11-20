# ---------------------------- PASSWORD GENERATOR ------------------------------- #
import random
import string
import os
import json
import pyperclip
from dotenv import load_dotenv
load_dotenv()
import os 

numbers = [str(n) for n in range(10)]
alphabets = [chr(letter) for letter in range(97,123)] + [chr(x) for x in range(97, 123)]
symbols  = list(string.punctuation)
def passwordGenerator(length=8):
    """
    Generates a random password containing letters (upper & lower), numbers, and symbols.
    Default length is 12 characters.
    """
    if length < 4:
        raise ValueError("Password length should be at least 4 characters.")
    
    # Ensure password contains at least one character from each category
    password = [
        random.choice(numbers),
        random.choice(alphabets),
        random.choice(symbols),
        random.choice(alphabets)
    ]
    
    # Fill the remaining length with random choices from all categories
    all_chars = numbers + alphabets + symbols
    password += random.choices(all_chars, k=length - 4)
    
    # Shuffle to make the order random
    random.shuffle(password)
    
    password = "".join(password)
    password_entry.insert(0,password)
    pyperclip.copy(password)
    return password



# ---------------------------- SAVE PASSWORD ------------------------------- #
def validate(email,password,website):
    return True


def save_password():
    file_path = os.environ.get("password_path")
    website = website_entry.get()
    email = email_entry.get()
    password = password_entry.get()

    new_data = {
        website: {
            "email": email,
            "password": password,
        }
    }

    if not website or not email or not password:
        messagebox.showwarning(title="Oops", message="Please don't leave any fields empty!")
        return

    is_ok = messagebox.askokcancel(
        title=website,
        message=f"Confirm Details\nEmail: {email}\nPassword: {password}"
    )

    if is_ok:
        folder = file_path
        os.makedirs(folder, exist_ok=True)

        actual_file_path = os.path.join(folder, "data.json")

        # --- Load old data ---
        try:
            with open(actual_file_path, "r") as data_file:
                display_data = json.load(data_file)
        except FileNotFoundError:
            display_data = {}  # File doesn't exist yet
        else:
        # --- Update the data ---
            display_data.update(new_data)

        # --- Save updated data ---
            with open(actual_file_path, "w") as data_file:
                json.dump(display_data, data_file, indent=4)
        finally:
        # --- Clear input fields ---
            password_entry.delete(0, END)
            website_entry.delete(0, END)


# ---------------------------- UI SETUP ------------------------------- #
from tkinter import *
from tkinter import messagebox
window = Tk()
window.title("PASSWORD MANAGER")
window.config(padx=20,pady=20)

canvas = Canvas(height=200,width=200)

logo_img = PhotoImage(file="logo.png")
canvas.create_image(100,100,image=logo_img)



canvas.grid(row=0,column=1)#Middle

#labels:
website_label = Label(text="Website")
website_label.grid(row=1,column=0)
email_label = Label(text="Email/Username")
email_label.grid(row=2,column=0)
password_label = Label(text="password:")
password_label.grid(row=3,column=0)

#Entries
website_entry = Entry(width=35)
website_entry.focus()
website_entry.grid(row=1,column=1,columnspan=2)
email_entry = Entry(width=35)
email_entry.insert(index=0,string="saketbhatnagar2@gmail.com")
email_entry.grid(row=2,column=1,columnspan=2)
password_entry = Entry(width=21)
password_entry.grid(row=3,column=1)

#Buttons
generate_password_button = Button(text="Generate Password",command=passwordGenerator)
generate_password_button.grid(row=3,column=2)
add_button = Button(text="Add",width=36,command=save_password)
add_button.grid(row=4,column=1,columnspan=2)


window.mainloop()