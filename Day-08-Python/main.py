from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine


drink = Menu()
make_coffee = CoffeeMaker()
money = MoneyMachine()

is_continue = True
while is_continue:
    order = input(f"What would you like? ({drink.get_items()}): ").lower()
    if order == 'report':
        make_coffee.report()
        money.report()
    elif order == 'off':
        print("Goodbye, have a nice code!")
        break
    else:
        drink_ordered = drink.find_drink(order)
        if make_coffee.is_resource_sufficient(drink_ordered) and money.make_payment(drink_ordered.cost): #type: ignore
            make_coffee.make_coffee(drink_ordered)