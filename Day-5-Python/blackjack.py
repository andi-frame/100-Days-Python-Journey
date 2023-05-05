import os
import random
print('''
===============================
!! WELCOME TO THE BLACKJACK !!
===============================
---------------------------------
• Get as close as possible to 21
=================================
''')
      
def end_detail(user_num, dealer_num):
    print(f"Your final cards: {user_num}, current score = {sum(user_num)}")
    print(f"Dealer's final cards: {dealer_num}, current score = {sum(dealer_num)}")

def start_again():
    is_continue = True if input("Do you want to play The Blackjack again ('y' or 'n'): ") == "y" else False
    os.system('clear')
    return is_continue

num = [1,2,3,4,5,6,7,8,9,10]
user_num = [random.choice(num) for i in range(1)]
dealer_num = [random.choice(num) for i in range(1)]


is_continue = True if input("Do you want to play The Blackjack ('y' or 'n'): ") == "y" else False
while is_continue:
    user_num += [random.choice(num) for i in range(1)]
    if sum(user_num) > 21:
        end_detail(user_num, dealer_num)
        print("You went over, you lose!")
        if start_again():
            user_num = [random.choice(num) for i in range(1)]
            dealer_num = [random.choice(num) for i in range(1)]
            continue
        break
    dealer_num += [random.choice(num) for i in range(1)]
    if sum(dealer_num) > 21:
        end_detail(user_num, dealer_num)
        print("The dealer went over, you win!")
        if start_again():
            user_num = [random.choice(num) for i in range(1)]
            dealer_num = [random.choice(num) for i in range(1)]
            continue 
        break 

    print(f"Your cards: {user_num}, current score = {sum(user_num)}")
    print(f"Dealer's first card: {dealer_num[0]}")
      
    is_continue = True if input("Type 'y' to get another card, type 'n' to pass: ").lower() == "y" else False
    os.system('clear')

    if not is_continue:
        if sum(user_num) == sum(dealer_num):
            end_detail(user_num, dealer_num)
            print("Tie!")
        if sum(user_num) > sum(dealer_num):
            end_detail(user_num, dealer_num)
            print("You win!")
        else:
            end_detail(user_num, dealer_num)
            print("You lose!")

        if start_again():
            user_num = [random.choice(num) for i in range(1)]
            dealer_num = [random.choice(num) for i in range(1)]
            continue