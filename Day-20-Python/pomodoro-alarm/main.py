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
reps = 0
timer = None

# ---------------------------- TIMER RESET ------------------------------- # 
def reset_timer():
    global timer, reps
    window.after_cancel(timer) #type: ignore
    text_timer.config(text = "Timer", fg = GREEN)
    canvas.itemconfig(time_remain, text = "00:00")
    checkmark.config(text="")
    reps = 0

# ---------------------------- TIMER MECHANISM ------------------------------- # 
def start_timer():
    global reps
    reps += 1

    work_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60
    
    if reps == 1 or reps == 3 or reps == 5 or reps == 7:
        text_timer.config(text = "Work", fg = GREEN)
        countdown(work_sec)
    elif reps == 2 or reps == 4 or reps == 6:
        text_timer.config(text = "Break", fg = PINK)
        countdown(short_break_sec)
    elif reps == 8:
        text_timer.config(text = "Break", fg = RED)
        countdown(long_break_sec)
    
    if reps % 2 == 0:
        checkmark_amount = int(reps/2)
        checkmark.config(text = ("✔"*checkmark_amount))

 
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
        global timer
        canvas.itemconfig(time_remain, text = f"{minute}:{second}")
        timer = window.after(1000, countdown, num-1)
    else:
        start_timer()
    

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Pomodoro Timer")
window.config(padx = 100, pady = 50, bg = YELLOW)

text_timer = Label(text = "Timer", font = (FONT_NAME, 40, "bold"), bg = YELLOW, fg = GREEN)
text_timer.grid(row = 1, column = 2)

canvas = Canvas(width = 200, height = 224, bg = YELLOW, highlightthickness = 0)
tomato_img = PhotoImage(file = "Day-20-Python/pomodoro-alarm/tomato.png")
canvas.create_image(100, 112, image = tomato_img)
time_remain = canvas.create_text(100, 135, text = f"00:00", font = (FONT_NAME, 35, "bold"))
canvas.grid(row = 2, column = 2)

start_button = Button(text = "Start", highlightbackground = YELLOW, command = start_timer)
start_button.grid(row = 3, column = 1)
reset_button = Button(text = "Reset", highlightbackground = YELLOW, command = reset_timer)
reset_button.grid(row = 3, column = 3)

checkmark = Label(text = "", font = (FONT_NAME, 20, "bold"), fg = GREEN, bg = YELLOW)
checkmark.grid(row = 4, column = 2)

window.mainloop()