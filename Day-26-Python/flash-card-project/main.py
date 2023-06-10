from tkinter import * #type: ignore
import pandas as pd
import random

BACKGROUND_COLOR = "#B1DDC6"


#--------------------------SHOW NEW WORD--------------------------
df = pd.read_csv("Day-26-Python/flash-card-project/data/french_words.csv")
words = df.to_dict(orient="records")

def back_card():
    canvas.itemconfig(card, image = photo_card_back)
    canvas.itemconfig(language, text = "English", fill = "white")
    word = words[random.randrange(len(words))]["English"]
    canvas.itemconfig(origin_word, text = word, fill = "white")

def front_card():
    canvas.itemconfig(card, image = photo_card_front)
    canvas.itemconfig(language, text = "French", fill = "black")
    word = words[random.randrange(len(words))]["French"]
    canvas.itemconfig(origin_word, text = word, fill = "black")
    canvas.after(3000, back_card)

def right():
    
    front_card()

def wrong():

    front_card()



#--------------------------UI SETUP--------------------------
window = Tk()
window.config(padx = 50, pady = 50, bg = BACKGROUND_COLOR)
window.title("Flash Card")

# Flash Card
canvas = Canvas(width = 800, height = 526, bg = BACKGROUND_COLOR, highlightthickness = 0)
photo_card_front = PhotoImage(file = "Day-26-Python/flash-card-project/images/card_front.png")
photo_card_back = PhotoImage(file = "Day-26-Python/flash-card-project/images/card_back.png")
card = canvas.create_image(400, 263)
language = canvas.create_text(400, 150, font = ("Ariel", 40, "italic"))
origin_word = canvas.create_text(400, 263, font = ("Ariel", 60, "bold"))
front_card()
canvas.grid(row = 1, column = 1, columnspan = 2)

photo_right = PhotoImage(file = "Day-26-Python/flash-card-project/images/right.png")
photo_wrong = PhotoImage(file = "Day-26-Python/flash-card-project/images/wrong.png")

cross_button = Button(image = photo_wrong, command = right, highlightbackground = BACKGROUND_COLOR, highlightthickness = 0)
cross_button.grid(row = 2, column = 1)
check_button = Button(image = photo_right, command = wrong, highlightbackground = BACKGROUND_COLOR, highlightthickness = 0)
check_button.grid(row = 2, column = 2)



window.mainloop()
