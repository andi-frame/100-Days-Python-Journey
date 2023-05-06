text = """
==============================
WELCOME TO THE COFFEE MACHINE
==============================
--------------------------------------------------------------
• Choose the coffee that you want and don't forget to pay it 
• Type 'report' to see status of the coffee machine         
• Type 'off' to turn off the coffee machine
--------------------------------------------------------------
"""
menu = {
    'espresso':
    {
        'water' : 50.00,
        'milk' : 0.00,
        'coffee' : 18.00,
        'money' : 1.50
    },
    'latte': 
    {
        'water' : 200.00,
        'milk' : 150.00,
        'coffee' : 24.00,
        'money' : 2.50
    },
    'cappucino': {
        'water' : 250.00,
        'milk' : 100.00,
        'coffee' : 24.00,
        'money' : 3.00
    }
    }
    

water = 300.00
milk = 200.00
coffee = 100.00
money = 0.00
customer = 0

print(text)
is_continue = True
while is_continue:
    customer += 1
    print(f"\nWelcome, customer {customer}!")
    user_input = input("What would you like? (espresso/latte/cappucino): ").lower()

    if user_input == 'report':
        print("Current resource values:")
        print(f"Water: {water}ml")
        print(f"Milk: {milk}ml")
        print(f"Coffee: {coffee}g")
        print(f"Money: ${money}")

    elif user_input == 'off':
        print("Goodbye, have a nice code!")
        break

    elif user_input == 'espresso' or user_input == 'latte' or user_input == 'cappucino':
        if water < menu[user_input]['water']:
            print("Sorry there is not enough water\n")
            continue
        if milk < menu[user_input]['milk']:
            print("Sorry there is not enough milk\n")
            continue
        if coffee < menu[user_input]['coffee']:
            print("Sorry there is not enough coffee\n")
            continue

        print(f"You choose {user_input}, it cost ${menu[user_input]['money']}.")
        print("Please, insert your coin!")
        pennies = int(input("How many pennies: "))
        nickles = int(input("How many nickles: "))
        dimes = int(input("How many dimes: "))
        quarters = int(input("How many quarters: "))
        user_money = float((pennies*0.01) + (nickles*0.05) + (dimes*0.10) + (quarters*0.25))
            
        if user_money == menu[user_input]['money']:
            money += user_money
            print(f"Here is your {user_input} coffee. Enjoy!!\n")
            continue

        if user_money > menu[user_input]['money']:
            money += user_money
            print(f"Here is your {user_input} coffee. Enjoy!!")
            print(f"Here is ${user_money - menu[user_input]['money']} dollars in change.\n")
            continue

        if user_money < menu[user_input]['money']:
            print("Sorry that's not enough money. Money refunded.\n")
            continue

    else: 
        print("Please insert the available command!")