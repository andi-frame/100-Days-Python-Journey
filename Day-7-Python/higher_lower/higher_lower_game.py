import os
import random
import game_data

text = """
=============================================
!! WELCOME TO THE HIGHER-LOWER !!            
=============================================
• Compare which account have more followers |
=============================================
"""
score = 0
is_continue = True

while is_continue:
    print(text)
    if score > 0:
        print(f"You're correct! Your score: {score}")
    while True:
        data_A = game_data.data[random.randrange(len(game_data.data))]
        data_B = game_data.data[random.randrange(len(game_data.data))]
        if data_A != data_B:
            break
        
    print(f"Compare A: {data_A['name']}, a {data_A['description']}, from {data_A['country']}")
    print("VS")
    print(f"Compare B: {data_B['name']}, a {data_B['description']}, from {data_B['country']}")
    user_answer = input("Who do you think have more followers? Type 'a' or 'b': ").lower()
    if data_A['follower_count'] > data_B['follower_count'] and user_answer == 'a':
        score += 1
    elif data_B['follower_count'] > data_A['follower_count'] and user_answer == 'b':
        score += 1
    else:
        print(f"You're incorrect! Your final score is {score}")
        play_again = input("Do you want to play again? Type 'yes' or 'no': ")
        if play_again == 'yes':
            score = 0
            is_continue = True
        elif play_again == 'no':
            is_continue = False
        else: break
    os.system('clear')