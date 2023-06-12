from turtle import Turtle
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager():
    def __init__(self):
        self.all_car = []
    
    def create_car(self, level):
        random_decision = random.randint(level, 10)
        if random_decision == 10:
            car = Turtle("square")
            car.penup()
            car.color(random.choice(COLORS))
            car.shape("square")
            car.shapesize(stretch_wid = 1, stretch_len = 2)
            self.rand_y = random.randint(-250, 250)
            car.goto(300-STARTING_MOVE_DISTANCE, self.rand_y)
            car.setheading(180)
            self.all_car.append(car)

    def move_car(self):
        for car in self.all_car:
            car.forward(MOVE_INCREMENT)
    
    def disappear_car(self):
        for car in self.all_car:
            car.forward(650)
