import secrets
import string
import random

# MEMO
letters = list(string.ascii_letters)
numbers = list(string.digits)
symbols = list(string.punctuation)

# USER_AMOUNT_INPUT
print("Welcome to the Password Generator by Andi-Frame")
print("Please fill this specification on your password:")
letters_amount = int(input("How many letters: "))
numbers_amount = int(input("How many numbers: "))
symbols_amount = int(input("How many symbols: "))

# FETCH
pass_letters = ''.join(secrets.choice(letters) for i in range(letters_amount))
pass_numbers = ''.join(secrets.choice(numbers) for i in range(numbers_amount))
pass_symbols = ''.join(secrets.choice(symbols) for i in range(symbols_amount))

# THE_PASSWORD
password = list(pass_letters + pass_numbers + pass_symbols)
random.shuffle(password)
print(''.join(password))

# REGENERATE
regenerate = int(input("Do you want to regenerate your password (1 for yes, 0 for no)? "))
while regenerate == 1:
    pass_letters = ''.join(secrets.choice(letters) for i in range(letters_amount))
    pass_numbers = ''.join(secrets.choice(numbers) for i in range(numbers_amount))
    pass_symbols = ''.join(secrets.choice(symbols) for i in range(symbols_amount))
    password = list(pass_letters + pass_numbers + pass_symbols)
    random.shuffle(password)
    print(''.join(password))

    regenerate = int(input("Do you want to regenerate your password (1 for yes, 0 for no)? "))
    

# SHUFFLE
shuffle = int(input("Want to reshuffle (1 for yes, 0 for no)? "))
while shuffle == 1:
    random.shuffle(password)
    print(''.join(password))
    shuffle = int(input("Want to reshuffle (1 for yes, 0 for no)? "))