from turtle import Turtle, Screen, colormode
import random
import colorgram

tur = Turtle()
screen = Screen()
tur.shape("turtle")
colormode(255)
tur.pensize(1)

def random_color():
    r = random.randint(0,255)
    g = random.randint(0,255)
    b = random.randint(0,255)
    return (r, g, b)
    

# Challange: Make Shapes
# for a in range(3, 9):
#     tur.color(tur_colors[a-3])
#     for b in range(a):
#         tur.forward(100)
#         tur.right(360/(a))

# # Challange: Draw a Random Walk
# while True:
#     tur.speed(0)
#     tur.color(random_color())
#     tur.forward(25)
#     tur.setheading(random.choice([0, 90, 180, 270]))

# Challange: Make a Spirograph
# def spirograph(gaps):
#     for i in range(int(360/gaps)):
#         tur.speed(0)
#         tur.color(random_color())
#         tur.circle(100)
#         tur.right(gaps)
# spirograph(7)

# Challange: Spot Paint Using Colorgram
# colors = colorgram.extract('/Users/andfrhn_/Documents/Python/Day-10-Python/hirst_spot_paint.jpg', 40)
# rgb_color = []
# for i in range(len(colors)):
#     rgb_color.append(tuple(colors[i].rgb))

rgb_color = [(233, 233, 232), (231, 233, 237), (236, 231, 233), (224, 233, 227), (207, 160, 82), (54, 88, 130),
            (145, 91, 40), (140, 26, 49), (221, 207, 105), (132, 177, 203), (158, 46, 83), (45, 55, 104),
            (169, 160, 39), (129, 189, 143), (83, 20, 44), (37, 43, 67), (186, 94, 107), (187, 140, 170),
            (85, 120, 180), (59, 39, 31), (88, 157, 92), (78, 153, 165), (194, 79, 73), (45, 74, 78), 
            (80, 74, 44), (161, 201, 218), (57, 125, 121), (219, 175, 187), (169, 206, 172), (219, 182, 169),
            (179, 188, 212), (48, 74, 73), (147, 37, 35), (43, 62, 61)]

tur.penup()
tur.hideturtle()
tur.speed(0)
tur.setheading(225)
tur.forward(350)
tur.setheading(0)
for a in range(10):
    for b in range(10):
        tur.dot(20, random.choice(rgb_color))
        tur.forward(50)
    tur.left(90)
    tur.forward(50)
    tur.left(90)
    tur.forward(500)
    tur.left(180)
    

screen = Screen()
screen.exitonclick()