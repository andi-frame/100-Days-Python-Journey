from turtle import Turtle
import random


class Blade(Turtle):
    def __init__(self, xcor, ycor):
        super().__init__()
        self.penup()
        self.shape("square")
        self.shapesize(4, 1)
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
        self.speed(3)
        self.x = random.randint(-10, 10)
        self.y = random.randint(-10, 10)
        self.ball_speed = 0.02

    def move(self):
        self.new_x = self.xcor() + self.x
        self.new_y = self.ycor() + self.y
        self.goto(self.new_x, self.new_y)

    def wall_collision(self):
        self.y = -self.y
    
    def blade_collision(self):
        self.x = -self.x
        self.ball_speed *= 0.9
    
    def refresh(self):
        self.goto(0,0)
        self.ball_speed = 0.01
        self.x = random.randint(-10,10)
        self.y = random.randint(-10,10)
        self.move()


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
    
    def winner(self, winner):
        self.home()
        self.write(f"The winner is {winner}", align= "center", font=("Arial", 40, "normal"))
<<<<<<< HEAD
        
=======
        
>>>>>>> f07363d (first commit to local file of 100python)
