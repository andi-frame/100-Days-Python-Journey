from tkinter import * #type: ignore
from tkinter import messagebox
import secrets
import string
import random
import pyperclip


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


    # Checking
    if website == "" or user_identity == "" or password == "":
        messagebox.showinfo(title = "Empty Data", message = "Please don't leave any fields empty!")
        return

    is_ok = messagebox.askokcancel(title="Please Make Sure", message = f"These are the details you've entered: \nWebsite: {website} \nEmail: {user_identity} \nPassword: {password}")
    if not is_ok:
        return


    # Write Data
    with open("Day-22-Python/password-manager/data_pass.txt", "a") as password_data:
        password_data.write(f"{website} | {user_identity} | {password}\n")
        password_data.close()


    # Reset UI
    website_input.delete(0, END)
    user_identity_input.delete(0, END)
    user_identity_input.insert(0, "andifarhan1094@gmail.com")
    password_input.delete(0, END)


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.geometry('400x300')
window.config(bg = "white")
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
website_input.grid(row = 2, column = 2, columnspan = 3)
website_input.focus()

user_identity_input = Entry(width = 35, bg = "white", fg = "black", highlightthickness = 0, insertbackground='black')
user_identity_input.grid(row = 3, column = 2, columnspan = 3)
user_identity_input.insert(0, "andifarhan1094@gmail.com")

password_input = Entry(width = 21, bg = "white", fg = "black", highlightthickness = 0, insertbackground='black')
password_input.grid(row = 4, column = 2)


# Buttons
generate_password_button = Button(text = "Generate Password", command = generate_password, bg = "white", fg = "black", highlightbackground = "white")
generate_password_button.grid(row = 4, column = 3)

add_button = Button(text = "Add", width = 32, command = add, bg = "white", fg = "black", highlightbackground = "white")
add_button.grid(row = 5, column = 2, columnspan = 3)

window.mainloop()