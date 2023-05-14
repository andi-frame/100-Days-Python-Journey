from turtle import Turtle, Screen

tur = Turtle()
screen = Screen()
screen.listen()

def move_forward():
    tur.forward(10)

def move_backward():
    tur.backward(10)

def rotate_right():
    tur.right(10)

def rotate_left():
    tur.left(10)

screen.onkey(key = "w", fun = move_forward)
screen.onkey(key = "s", fun = move_backward)
screen.onkey(key = "d", fun = rotate_right)
screen.onkey(key = "a", fun = rotate_left)
screen.onkey(key = "c", fun = screen.resetscreen)

screen.exitonclick()