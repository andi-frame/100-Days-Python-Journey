import random
import string
print('''
=========================================
!! WELCOME TO THE GUESSING GAME !!      |
=========================================
• Guess the right number.               |
• Easy = 10 attempts, Hard = 5 attempts |
=========================================
''')

print("Can you guess the number that I thinking? It's between 1 and 100")
secret_num = int(random.choice(list(range(1,101))))
difficulty = input("Choose the difficulty, 'easy' or 'hard': ")
if difficulty == 'easy':
    attempts = 10
elif difficulty == 'hard':
    attempts = 5
else: attempts = 0

for i in range(attempts):
    print(f"You have {attempts - i} attempts remaining")
    guess = int(input("Make a guess: "))
    if guess > secret_num:
        print("Too high.")
    if guess < secret_num:
        print("Too low.")  
    if guess == secret_num:
        print(f"Your guess is right! The number is {secret_num}")
        break

    if i == attempts-1:
        print("You've run out of attempts, you lose")
        break

    print("Guess again.")