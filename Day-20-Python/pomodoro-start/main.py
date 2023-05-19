from tkinter import * #type: ignore
import time
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20

# ---------------------------- TIMER RESET ------------------------------- # 

# ---------------------------- TIMER MECHANISM ------------------------------- # 
def start_timer():
    countdown(5)
    countdown(WORK_MIN * 60)

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 
def countdown(num):
    minute = int(num / 60)
    second = num % 60
    if minute == 0:
        minute = "00"
    elif minute < 10:
        minute = f"0{minute}"

    if second == 0:
        second = "00"
    elif second < 10:
        second = f"0{second}"

    if num >= 0:
        canvas.itemconfig(time_remain, text = f"{minute}:{second}")
    window.after(1000, countdown, num-1)

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Pomodoro Timer")
window.config(padx = 100, pady = 50, bg = YELLOW)

text_timer = Label(text = "Timer", font = (FONT_NAME, 40, "bold"), bg = YELLOW, fg = GREEN)
text_timer.grid(row = 1, column = 2)

canvas = Canvas(width = 200, height = 224, bg = YELLOW, highlightthickness = 0)
tomato_img = PhotoImage(file = "Day-20-Python/pomodoro-start/tomato.png")
canvas.create_image(100, 112, image = tomato_img)
time_remain = canvas.create_text(100, 135, text = f"00:00", font = (FONT_NAME, 35, "bold"))
canvas.grid(row = 2, column = 2)

start_button = Button(text = "Start", highlightbackground = YELLOW, command = start_timer)
start_button.grid(row = 3, column = 1)
reset_button = Button(text = "Reset", highlightbackground = YELLOW)
reset_button.grid(row = 3, column = 3)

checkmark = Label(text = "✔", font = (FONT_NAME, 20, "bold"), fg = GREEN, bg = YELLOW)
checkmark.grid(row = 4, column = 2)

window.mainloop()