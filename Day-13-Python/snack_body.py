from turtle import Turtle
class Snack():
    def __init__(self, snack_length):
        self.all_snack = []
        for i in range(snack_length):
            snack = Turtle(shape = 'square')
            snack.shapesize(1, 1)
            snack.penup()
            snack.color("white")
            snack.goto(x = -(i*20), y = 0)
            self.all_snack.append(snack)
            
    def len_plus(self, position):
        snack = Turtle(shape = 'square')
        snack.shapesize(1, 1)
        snack.penup()
        snack.color("white")
        snack.goto(position)
        self.all_snack.append(snack)
    
    def up(self):
        if self.all_snack[0].heading() != 270:
            self.all_snack[0].setheading(90)
    
    def down(self):
        if self.all_snack[0].heading() != 90:
            self.all_snack[0].setheading(270)

    def right(self):
        if self.all_snack[0].heading() != 180:
            self.all_snack[0].setheading(0)

    def left(self):
        if self.all_snack[0].heading() != 0:
            self.all_snack[0].setheading(180)
       
    def move(self):
        for i in range(len(self.all_snack)-1, 0, -1):
            self.all_snack[i].goto(self.all_snack[i-1].pos())
        self.all_snack[0].forward(20)
