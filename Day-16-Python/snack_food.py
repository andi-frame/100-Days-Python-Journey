from turtle import Turtle
import random

class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.color("orange")
        self.shape("circle")
        self.penup()
        self.shapesize(stretch_wid = 0.5, stretch_len = 0.5)
        self.speed("fastest")
        self.goto(x = random.randint(-230, 230), y = random.randint(-230, 230))

    def disappear(self):
        del self