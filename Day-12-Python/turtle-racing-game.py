from turtle import Turtle, Screen
import random

screen = Screen()
screen.setup(width=500, height=500, startx=0, starty=0)

user_bet = screen.textinput(title = "Predict The Winner", prompt = "Which turtle will win the race?\nEnter a color: ")
color = ["red", "orange", "yellow", "green", "blue", "purple"]

for i in range(len(color)):
    tur = Turtle(shape = "turtle")
    tur.speed(0)
    tur.fillcolor(color[i])
    tur.penup()
    x_position = 170 - (i*70)
    tur.goto(-210, x_position)

flag = False
winner = str()
while True:
    rand_obj = random.randrange(len(screen.turtles()))
    rand_move = random.randrange(20)
    screen.turtles()[rand_obj].forward(rand_move)
    for i in screen.turtles():
        if i.xcor() >= 230:
            winner = i.fillcolor()
            flag = True
            break
    if flag: break

if user_bet == winner:
    print("Your guess is right!")
else:
    print(f"Your guess is wrong, the winner is {winner}!")

screen.exitonclick()