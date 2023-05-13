from turtle import Turtle
import random


class Blade(Turtle):
    def __init__(self, xcor, ycor):
        super().__init__()
        self.penup()
        self.shape("square")
        self.shapesize(3, 1)
        self.color("white")
        self.xcor = xcor
        self.ycor = ycor
        self.goto(xcor, ycor)
    
    def up(self):
        self.goto(self.xcor, (self.ycor + 40)) # type: ignore
        self.ycor += 40 # type: ignore
    
    def down(self):
        self.goto(self.xcor, (self.ycor - 40)) # type: ignore
        self.ycor -= 40 # type: ignore


class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.shape("circle")
        self.shapesize(1, 1)
        self.color("white")
        self.random_heading()

    def move(self):
        self.forward(5)
    
    def random_heading(self):
        self.setheading(random.randint(0,360))
    
    def refresh(self):
        self.home()
        self.random_heading()


class Net(Turtle):
    def __init__(self, ycor):
        super().__init__()    
        self.penup()
        self.shape("square")
        self.shapesize(1.2, 0.3)
        self.color("white")
        self.goto(0, ycor)
    

class Scoreboard(Turtle):
    def __init__(self, score, xcor):
        super().__init__()
        self.penup()
        self.hideturtle()
        self.color("white")
        self.goto(xcor, 220)
        self.write(f"{score}", align= "center", font=("Arial", 40, "normal"))
        