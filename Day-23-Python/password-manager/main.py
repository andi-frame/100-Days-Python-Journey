from tkinter import * #type: ignore
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
canvas = Canvas(width = 200, height = 200, bg = "white", highlightthickness = 0)
file_logo = PhotoImage(file = "Day-22-Python/password-manager/logo.png")
photo_logo = canvas.create_image(100, 100, image = file_logo)
canvas.grid(row = 1, column = 2)


# Labels
website_label = Label(text = "Website: ", bg = "white", fg = "black")
website_label.grid(row = 2, column = 1)

user_identity_label = Label(text = "Email/Username: ", bg = "white", fg = "black")
user_identity_label.grid(row = 3, column = 1)

password_label = Label(text = "Password: ", bg = "white", fg = "black")
password_label.grid(row = 4, column = 1)


# Entries
website_input = Entry(width = 35, bg = "white", fg = "black", highlightthickness = 0, insertbackground='black')
website_input.grid(row = 2, column = 2, columnspan = 2)
website_input.focus()

user_identity_input = Entry(width = 35, bg = "white", fg = "black", highlightthickness = 0, insertbackground='black')
user_identity_input.grid(row = 3, column = 2, columnspan = 2)
user_identity_input.insert(0, "andifarhan1094@gmail.com")

password_input = Entry(width = 21, bg = "white", fg = "black", highlightthickness = 0, insertbackground='black')
password_input.grid(row = 4, column = 2)


# Buttons
search_button = Button(text = "Search", width = 10, command = search, bg = "white", fg = "black", highlightbackground = "white")
search_button.grid(row = 2, column = 3)

generate_password_button = Button(text = "Generate Password", width = 10, command = generate_password, bg = "white", fg = "black", highlightbackground = "white")
generate_password_button.grid(row = 4, column = 3)

add_button = Button(text = "Add", width = 32, command = add, bg = "white", fg = "black", highlightbackground = "white")
add_button.grid(row = 5, column = 2, columnspan = 2)


window.mainloop()