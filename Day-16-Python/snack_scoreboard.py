from turtle import Turtle


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0

        with open("./Day-16-Python/snack_data.txt") as data:
            self.bestscore = int(data.read())
        
        self.color("white")
        self.penup()
        self.goto(0,220)
        self.write(f"Score = {self.score} Bestscore = {self.bestscore}", align= "center", font=("Arial", 18, "normal"))
        self.hideturtle()
    
    def add_score(self):
        self.clear()
        self.score += 1
        self.write(f"Score = {self.score} Bestscore = {self.bestscore}", align= "center", font=("Arial", 18, "normal"))

    def reset(self):
        
        if self.score > self.bestscore:
            self.bestscore = self.score

            with open("./Day-16-Python/snack_data.txt", mode = "w") as data:
                data.write(f"{self.bestscore}")

        self.clear()    
        self.score = 0
        self.write(f"Score = {self.score} Bestscore = {self.bestscore}", align= "center", font=("Arial", 18, "normal"))

    # def game_over(self):
    #     self.goto(0,0)
    #     self.write("Game Over!", align= "center", font=("Arial", 18, "normal"))