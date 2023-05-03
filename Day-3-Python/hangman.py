import os
import random
from hangman_stages import stages
from hangman_words import word_list

# INIT
live = 6
print("WELCOME TO THE HANGMAN!")
print("•Guess it but don't die•")
print("•Live started at 6. live at 0 means die•")


# CHOOSE WORD
word = str(random.choice(word_list))
letters_guessed = []
for x in word:
    letters_guessed.append('_')

# CHECK GUESS
while True:
    print(stages[live])
    print(f"|{live} live left|")
    print(*letters_guessed)
    
    user_guess = input("Enter the letter you guess: ")
    
    if user_guess in word:
        index_guessed = [i for i in range(len(word)) if word[i] == user_guess]
        print(index_guessed)
        for i in range(len(index_guessed)):
            letters_guessed[index_guessed[i]] = user_guess
        print(*letters_guessed)
    
    else: live -= 1

    if live == 0 or '_' not in letters_guessed: break

    os.system('clear')

os.system('clear')
if live == 0:
    print(stages[live])
    print("You Lose!")
else:
    print(stages[live])
    print("You Win!")
