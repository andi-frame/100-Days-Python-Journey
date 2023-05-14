import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard


screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
player = Player()
level = int(screen.numinput("Choose Level", "Insert a number from 1 to 10: ")) # type: ignore
car_manager = CarManager()
scoreboard = Scoreboard(level)


# collision with car => done
# winning condition => done
# next stage
# leveling => done


game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    screen.listen()
    screen.onkey(key = "space", fun = player.up)
    car_manager.create_car(level)
    car_manager.move_car()

    for car in car_manager.all_car:
        if car.distance(player) <= 25:
            game_is_on = False
            scoreboard.game_over()
    
    if player.ycor() >= 280:
        scoreboard.winning()

        if screen.textinput("Next Stage?", "Want to continue? 'y' or 'n'") == 'y':
            for car in car_manager.all_car:
                car.reset()
            level += 1
            scoreboard.play_again(level)
            player.play_again()

        elif screen.textinput("Next Stage?", "Want to continue? 'y' or 'n'") == 'n': 
            game_is_on = False



screen.exitonclick()


