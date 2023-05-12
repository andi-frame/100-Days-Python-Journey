from turtle import Screen
from snack_body import Snack
from snack_food import Food
from snack_scoreboard import Scoreboard
import random
import time

screen = Screen()
screen.setup(width = 500, height = 500)
screen.bgcolor('black')
screen.listen()
screen.tracer(0)

snack = Snack(3)
food = Food()
score = 0
scoreboard = Scoreboard(score)

game_is_on = True
food_exist = True
while game_is_on:
    
    if not food_exist:
        food = Food()
    if snack.all_snack[0].distance(food) <= 15 :
        snack.len_plus()
        score += 1
        scoreboard.clear()
        scoreboard = Scoreboard(score)
        food.goto(x = random.randint(-230, 230), y = random.randint(-230, 230))
    
    time.sleep(0.1)
    screen.update()
    snack.move()
    screen.onkey(key = "Up", fun = snack.up)
    screen.onkey(key = "Down", fun = snack.down)
    screen.onkey(key = "Right", fun = snack.right)
    screen.onkey(key = "Left", fun = snack.left)

screen.exitonclick()