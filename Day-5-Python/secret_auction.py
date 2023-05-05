import os
print('''
===============================================
!! WELCOME TO THE UNDERGROUND SECRET AUCTION !!
===============================================
------------------------------
===================
• Bid Secretly   ||
• Use Dictionary ||
===================
''')
is_continue = True
secret_bid = dict({})
while is_continue:
    user_name = input("What is your name:\n").capitalize()
    user_bid = int(input("What is your bid:\n$"))
    secret_bid.update({user_name : user_bid})
    is_continue = True if input("Are there any other bidders? (Type 'Yes' or 'No')\n").lower() == 'yes' else False
    os.system('clear')

winner_bid = max(secret_bid.values())
winner_name = list(secret_bid.keys())[list(secret_bid.values()).index(winner_bid)]
print(f"The winner is {winner_name} with a bid of ${winner_bid}.")