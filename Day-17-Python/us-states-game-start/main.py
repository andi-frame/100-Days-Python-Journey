import turtle
import pandas

screen = turtle.Screen()
screen.title("US States? Game")
bg_image = "Day-17-Python/us-states-game-start/blank_states_img.gif"
screen.addshape(bg_image)
turtle.shape(bg_image)
states_data = pandas.read_csv("Day-17-Python/us-states-game-start/50_states.csv")
correct_states = turtle.Turtle()
correct_states.hideturtle()
scoreboard = turtle.Turtle()
scoreboard.hideturtle()
screen.tracer(0)

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
    user_input = str(screen.textinput(title = "US States", prompt = "Input a states: ")).capitalize()
    guessed_state = states_data[states_data["state"] == user_input]
    
    if guessed_state.empty:
        live -= 1
        display_scoreboard()
    if not guessed_state.empty:
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
    if live == 0:
        scoreboard.home()
        scoreboard.write("Game Over.", align = "center", font = ("Arial", 14, "bold"))
        break
        


screen.exitonclick()