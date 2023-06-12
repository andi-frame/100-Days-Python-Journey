from turtle import Turtle
FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):
    def __init__(self, level):
        super().__init__()
        self.penup()
        self.hideturtle()
        self.goto(-220, 250)
        self.write(f"Level: {level}", align = "center", font = FONT)

    def game_over(self):
        self.home()
        self.write("Game Over.", align = "center", font = FONT)
    
    def winning(self):
        self.goto(0, 200)
        self.write("You Win!", align = "center", font = FONT)

    def play_again(self, level):
        self.clear()
        self.goto(-220, 250)
        self.write(f"Level: {level}", align = "center", font = FONT)
