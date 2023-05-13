from turtle import Screen
from pong_tool import Blade, Ball, Net, Scoreboard


# Make the blade
# Make the ball
# Make the net
# Make Scoreboard
# Collision with upper-lower wall
# Collision with the blade
# Make score
# End game


screen = Screen()
screen.bgcolor("black")
screen.setup(width = 800, height = 600)
screen.listen()


# Tool
left_blade = Blade(-390, 0)
right_blade = Blade(380, 0)
for i in range(15):
    net = Net(-280 + i*40)
left_score = 0
right_score = 0
left_scoreboard = Scoreboard(score = left_score, xcor = -180)
right_scoreboard = Scoreboard(score = right_score, xcor = 180)
ball = Ball()



game_is_on = True
while game_is_on:
    # Blade move
    screen.onkeypress(key = "w", fun = left_blade.up)
    screen.onkeypress(key = "s", fun = left_blade.down)
    screen.onkeypress(key = "Up", fun = right_blade.up)
    screen.onkeypress(key = "Down", fun = right_blade.down)

    # Ball Move
    ball.move()

    # Collision with upper-lower wall
    if ball.ycor() >= 280 or ball.ycor() <= -280:
        ball.setheading(-ball.heading())

    # Collision with blade
    if ball.distance(left_blade.pos()) <= 25 or ball.distance(right_blade.pos()) <= 25:
        ball.setheading(-ball.heading() - 180)
        ball.forward(8)
    
    # Make Score
    if ball.xcor() <= -410:
        left_score += 1
        left_scoreboard.clear()
        left_scoreboard = Scoreboard(score = left_score, xcor = -180)
        ball.refresh()
    if ball.xcor() >= 400:
        right_score += 1
        right_scoreboard.clear()
        right_scoreboard = Scoreboard(score = right_score, xcor = 180)
        ball.refresh()



screen.exitonclick()