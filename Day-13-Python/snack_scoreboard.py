from turtle import Turtle

class Scoreboard(Turtle):
    def __init__(self, score):
        super().__init__()
        self.score = score
        self.color("white")
        self.penup()
        self.goto(0,220)
        self.write(f"Score = {self.score}", align= "center", font=("Arial", 18, "normal"))
        self.hideturtle()
        