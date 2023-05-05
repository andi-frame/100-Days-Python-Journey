import os
import random
text = '''
================================
!! WELCOME TO THE BLACKJACK !!
================================
• Get as close as possible to 21
================================
'''
as_card = [1,11]
num = [2,3,4,5,6,7,8,9,10,10,10,as_card]
user_num = [random.choice(num) for i in range(1)]
dealer_num = []

def end_detail(user_num, dealer_num):
    print(f"Your final cards: {user_num}, current score = {sum(user_num)}")
    print(f"Dealer's final cards: {dealer_num}, current score = {sum(dealer_num)}")

def start_again():
    is_continue = True if input("Do you want to play The Blackjack again ('y' or 'n'): ") == "y" else False
    os.system('clear')
    return is_continue

def as_card_function(user):
    if as_card in user:
        user.remove(as_card)
        if as_card[1] + sum(user) > 21:
            user.append(1)
        else: user.append(11)


is_continue = True if input("Do you want to play The Blackjack ('y' or 'n'): ") == "y" else False
os.system('clear')
while is_continue:
    print(text)
    user_num += [random.choice(num) for i in range(1)]
    as_card_function(user_num)
    if sum(user_num) > 21:
        end_detail(user_num, dealer_num)
        print("You went over, you lose!")
        if start_again():
            user_num = [random.choice(num) for i in range(1)]
            dealer_num = []
            continue
        break
    if sum(user_num) == 21:
        end_detail(user_num, dealer_num)
        print("BLACKJACK!!\n You!")
        if start_again():
            user_num = [random.choice(num) for i in range(1)]
            dealer_num = []
            continue
        break

    dealer_num = [random.choice(num) for i in range(2)]
    as_card_function(dealer_num)

    print(f"Your cards: {user_num}, current score = {sum(user_num)}")
    print(f"Dealer's first card: {dealer_num[0]}")
      
    is_continue = True if input("Type 'y' to get another card, type 'n' to pass: ").lower() == "y" else False
    os.system('clear')

    if not is_continue:
        while sum(dealer_num) < 17:
            dealer_num += [random.choice(num) for i in range(1)]
            as_card_function(dealer_num)
        
        if sum(dealer_num) > 21:
            end_detail(user_num, dealer_num)
            print("Dealer went over, you win!")
        elif sum(user_num) == sum(dealer_num):
            end_detail(user_num, dealer_num)
            print("Tie!")
        elif sum(user_num) > sum(dealer_num):
            end_detail(user_num, dealer_num)
            print("You win!")
        else:
            end_detail(user_num, dealer_num)
            print("You lose!")

        if start_again():
            user_num = [random.choice(num) for i in range(1)]
            dealer_num = []
            is_continue = True
