from tkinter import * #type: ignore
import pandas as pd
import random

BACKGROUND_COLOR = "#B1DDC6"


#--------------------------SHOW NEW WORD--------------------------
df = pd.read_csv("Day-26-Python/flash-card-project/data/french_words.csv")
words =  df.to_dict(orient="records")
print(words)

def new_word():
    word = words[random.randrange(len(words))]["French"]
    canvas.itemconfig(origin_word, text = word)

#--------------------------UI SETUP--------------------------
window = Tk()
window.config(padx = 50, pady = 50, bg = BACKGROUND_COLOR)
window.title("Flash Card")

# Flash Card
canvas = Canvas(width = 800, height = 526, bg = BACKGROUND_COLOR, highlightthickness = 0)
photo_card_front = PhotoImage(file = "Day-26-Python/flash-card-project/images/card_front.png")
card_front = canvas.create_image(400, 263, image = photo_card_front)
language = canvas.create_text(400, 150, text = "French", font = ("Ariel", 40, "italic"))
origin_word = canvas.create_text(400, 263, text = "trouve", font = ("Ariel", 60, "bold"))
canvas.grid(row = 1, column = 1, columnspan = 2)

photo_right = PhotoImage(file = "Day-26-Python/flash-card-project/images/right.png")
photo_wrong = PhotoImage(file = "Day-26-Python/flash-card-project/images/wrong.png")

cross_button = Button(image = photo_wrong, command = new_word, highlightbackground = BACKGROUND_COLOR, highlightthickness = 0)
cross_button.grid(row = 2, column = 1)
check_button = Button(image = photo_right, command = new_word, highlightbackground = BACKGROUND_COLOR, highlightthickness = 0)
check_button.grid(row = 2, column = 2)


window.mainloop()