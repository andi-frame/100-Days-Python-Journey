import random
AI_game = ["scissors", "rock", "paper"]
user_game = ["scissors", "rock", "paper"]

while 1==1:
    print("\nWelcome to the scissors rock paper game")
    user_answer = int(input("Press 1 for scissors, 2 for rock, and 3 for paper: "))
    user_answer = user_game[user_answer - 1]
    rand_AI = random.choice((AI_game))

    print("Your answer: ", user_answer)
    print("AI's answer: ", rand_AI)

    if ((user_answer == "scissors" and rand_AI == "paper") or (user_answer == "rock" and rand_AI == "scissors") or (user_answer == "paper" and rand_AI == "rock")):
        print("You win!")
    if ((rand_AI == "scissors" and user_answer == "paper") or (rand_AI == "rock" and user_answer == "scissors") or (rand_AI == "paper" and user_answer == "rock")):
        print("You lose!")
    if (user_answer == rand_AI):
        print("TIE")
    
    a = int(input("\nContinue? 1 for yes, 2 for no: "))
    if a == 1:
        continue
    if a == 2:
<<<<<<< HEAD
        break
=======
        break
>>>>>>> f07363d (first commit to local file of 100python)
