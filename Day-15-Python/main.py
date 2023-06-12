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


<<<<<<< HEAD
# collision with car => done
# winning condition => done
# next stage
# leveling => done


=======
>>>>>>> f07363d (first commit to local file of 100python)
game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    screen.listen()
    screen.onkey(key = "space", fun = player.up)
    car_manager.create_car(level)
    car_manager.move_car()

    for car in car_manager.all_car:
<<<<<<< HEAD
        if car.distance(player) <= 25:
            game_is_on = False
            scoreboard.game_over()
    
=======
        if car.distance(player) <= 24:
            game_is_on = False
            scoreboard.game_over()

>>>>>>> f07363d (first commit to local file of 100python)
    if player.ycor() >= 280:
        scoreboard.winning()

        if screen.textinput("Next Stage?", "Want to continue? 'y' or 'n'") == 'y':
<<<<<<< HEAD
            for car in car_manager.all_car:
                car.reset()
            level += 1
            scoreboard.play_again(level)
            player.play_again()
=======
            level += 1
            scoreboard.play_again(level)
            player.play_again()
            car_manager.disappear_car()
>>>>>>> f07363d (first commit to local file of 100python)

        elif screen.textinput("Next Stage?", "Want to continue? 'y' or 'n'") == 'n': 
            game_is_on = False


<<<<<<< HEAD

=======
>>>>>>> f07363d (first commit to local file of 100python)
screen.exitonclick()


