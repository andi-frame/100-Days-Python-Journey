import turtle
<<<<<<< HEAD
import pandas
=======
import pandas as pd
>>>>>>> f07363d (first commit to local file of 100python)

screen = turtle.Screen()
screen.title("US States? Game")
bg_image = "Day-17-Python/us-states-game-start/blank_states_img.gif"
screen.addshape(bg_image)
turtle.shape(bg_image)
<<<<<<< HEAD
states_data = pandas.read_csv("Day-17-Python/us-states-game-start/50_states.csv")
=======
states_data = pd.read_csv("Day-17-Python/us-states-game-start/50_states.csv")
>>>>>>> f07363d (first commit to local file of 100python)
correct_states = turtle.Turtle()
correct_states.hideturtle()
scoreboard = turtle.Turtle()
scoreboard.hideturtle()
screen.tracer(0)
<<<<<<< HEAD
=======
known_states = []
>>>>>>> f07363d (first commit to local file of 100python)

live = 5
score = 0

def display_scoreboard():
    scoreboard.clear()
    scoreboard.penup()
    scoreboard.goto(-60, 200)
    scoreboard.write(f"Score: {score}\nLives: {live}", align = "center", font = ("Arial", 14, "bold"))
display_scoreboard()

game_is_on = True
while game_is_on:
    screen.update()
<<<<<<< HEAD
    user_input = str(screen.textinput(title = "US States", prompt = "Input a states: ")).capitalize()
    guessed_state = states_data[states_data["state"] == user_input]
    
    if guessed_state.empty:
        live -= 1
        display_scoreboard()
    if not guessed_state.empty:
=======
    user_input = str(screen.textinput(title = "US States", prompt = "Input a states: ")).title()
    guessed_state = states_data[states_data["state"] == user_input]
    
    if user_input == "Exit":
        break
    
    if guessed_state.empty:
        live -= 1
        display_scoreboard()

    if not guessed_state.empty:
        known_states.append(user_input)
>>>>>>> f07363d (first commit to local file of 100python)
        score += 1
        
        # My code version (no future error):
        # guessed_state_x = int(guessed_state.iloc[0]["x"])
        # guessed_state_y = int(guessed_state.iloc[0]["y"])
        # guessed_state_xy = (guessed_state_x, guessed_state_y)

        display_scoreboard()

        # The code solution (terminal said there will be an error in the future) (now the code fixed, just add '.item()' at the end):
        correct_states.penup()
        correct_states.goto(int(guessed_state["x"].item()), int(guessed_state["y"].item())) 
        correct_states.write(f"{user_input}", align = "center", font = ("Arial", 10, "normal"))
<<<<<<< HEAD
=======

>>>>>>> f07363d (first commit to local file of 100python)
    if live == 0:
        scoreboard.home()
        scoreboard.write("Game Over.", align = "center", font = ("Arial", 14, "bold"))
        break
<<<<<<< HEAD
        

=======

unknown_states = []
for states in states_data["state"]:
    if states not in known_states:
        unknown_states.append(states)

df_states_to_learn = pd.DataFrame({"state" : unknown_states})
df_states_to_learn.to_csv("Day-17-Python/us-states-game-start/states_to_learn.csv")
>>>>>>> f07363d (first commit to local file of 100python)

screen.exitonclick()