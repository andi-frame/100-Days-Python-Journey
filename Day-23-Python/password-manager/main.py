from tkinter import * #type: ignore
from tkinter import ttk
from tkinter import messagebox
import secrets
import string
import random
import pyperclip
import json

# ---------------------------- SEARCH ------------------------------- #
def search():
    website = website_input.get()
    try:
        with open("Day-23-Python/password-manager/data_file.json") as data_file:
            data = json.load(data_file)
    except FileNotFoundError:
        messagebox.showinfo(title = "FileNotFoundError", message = "No Data File Found")
    else:
        try:
            email = data[website]["email"]
        except KeyError:
            messagebox.showinfo(title = "KeyError", message = f"No details for the {website} exist")
        else:
            password = data[website]["password"]
            messagebox.showinfo(title = website, message = f"Email: {email}\nPassword: {password}")


# ---------------------------- PASSWORD GENERATOR ------------------------------- #
# MEMO
letters = list(string.ascii_letters)
numbers = list(string.digits)
symbols = list(string.punctuation)

def generate_password():
    letters_amount = random.randint(8, 10)
    numbers_amount = random.randint(2, 4)
    symbols_amount = random.randint(2, 4)

    # FETCH
    pass_letters = ''.join(secrets.choice(letters) for i in range(letters_amount))
    pass_numbers = ''.join(secrets.choice(numbers) for i in range(numbers_amount))
    pass_symbols = ''.join(secrets.choice(symbols) for i in range(symbols_amount))

    # THE_PASSWORD
    password_generated = ''.join(list(set(pass_letters + pass_numbers + pass_symbols)))
    password_input.delete(0, END)
    password_input.insert(0, password_generated)

    # COPY TO CLIPBOARD
    pyperclip.copy(password_generated)



# ---------------------------- SAVE PASSWORD ------------------------------- #
def add():
    # Get Data
    website = website_input.get()
    user_identity = user_identity_input.get()
    password = password_input.get()
    dict_data = {
        website : {
            "email" : user_identity,
            "password" : password,
        }
    }


    # Checking
    if website == "" or user_identity == "" or password == "":
        messagebox.showinfo(title = "Empty Data", message = "Please don't leave any fields empty!")
        return


    # Write Data
    try:
        with open("Day-23-Python/password-manager/data_file.json", "r") as data_file:
            data = json.load(data_file)
    except FileNotFoundError:
        with open("Day-23-Python/password-manager/data_file.json", "w") as data_file:
            json.dump(dict_data, data_file, indent = 4)
    else:
        data.update(dict_data)
        with open("Day-23-Python/password-manager/data_file.json", "w") as data_file:
            json.dump(data, data_file, indent = 4)


    # Reset UI
    website_input.delete(0, END)
    user_identity_input.delete(0, END)
    user_identity_input.insert(0, "andifarhan1094@gmail.com")
    password_input.delete(0, END)


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.config(padx = 50, pady = 50, bg = "white")
window.title("Password Manager")


# Image
canvas = Canvas(master = window, width = 200, height = 200, bg = "white", highlightthickness = 0)
file_logo = PhotoImage(file = "Day-22-Python/password-manager/logo.png")
photo_logo = canvas.create_image(100, 100, image = file_logo)
canvas.grid(row = 1, column = 2)


# Labels
website_label = Label(master = window, text = "Website: ", bg = "white", fg = "black")
website_label.grid(row = 2, column = 1)

user_identity_label = Label(master = window, text = "Email/Username: ", bg = "white", fg = "black")
user_identity_label.grid(row = 3, column = 1)

password_label = Label(master = window, text = "Password: ", bg = "white", fg = "black")
password_label.grid(row = 4, column = 1)


# Entries
# Input frame
input_frame = ttk.Frame(master = window)
website_input = Entry(master = input_frame, width = 29, bg = "white", fg = "black", highlightthickness = 0, insertbackground='black')
website_input.pack(side = 'left')
website_input.focus()
search_button = Button(master = input_frame, text = "Search", font=('Arial', 7), command = search, bg = "white", fg = "black", highlightbackground = "white")
search_button.pack(side = 'right')
input_frame.grid(row = 2, column = 2, columnspan = 3)

user_identity_input = Entry(master = window, width = 35, bg = "white", fg = "black", highlightthickness = 0, insertbackground='black')
user_identity_input.grid(row = 3, column = 2, columnspan = 2)
user_identity_input.insert(0, "andifarhan1094@gmail.com")

# Password frame
password_frame = ttk.Frame(master = window)
password_input = Entry(master = password_frame, width = 20, bg = "white", fg = "black", highlightthickness = 0, insertbackground='black')
password_input.pack(side='left')
generate_password_button = Button(master = password_frame, text = "Generate Password", font=('Arial', 7), command = generate_password, bg = "white", fg = "black", highlightbackground = "white")
generate_password_button.pack(side ='right')
password_frame.grid(row = 4, column = 2, columnspan = 3)

# Buttons
add_button = Button(master = window, text = "Add", width = 29, command = add, bg = "white", fg = "black", highlightbackground = "white")
add_button.grid(row = 5, column = 2, columnspan = 2)


window.mainloop()