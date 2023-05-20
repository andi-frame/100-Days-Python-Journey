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
timer = None
time_num = 0

# ---------------------------- TIMER RESET ------------------------------- # 
def reset_timer():
    global timer, reps
    window.after_cancel(timer) #type: ignore
    text_timer.config(text = "Timer", fg = GREEN)
    canvas.itemconfig(time_remain, text = "00:00")

# ---------------------------- TIMER MECHANISM ------------------------------- # 

 
# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 
def countdown():
    global time_num
    time_num = int(input_num.get())
    minute = int(time_num / 60)
    second = time_num % 60
    if minute == 0:
        minute = "00"
    elif minute < 10:
        minute = f"0{minute}"

    if second == 0:
        second = "00"
    elif second < 10:
        second = f"0{second}"

    if time_num >= 0:
        canvas.itemconfig(time_remain, text = f"{minute}:{second}")
        window.after(1000, countdown, time_num-1)
    

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Pomodoro Timer")
window.config(padx = 100, pady = 50, bg = YELLOW)

text_timer = Label(text = "Alarm", font = (FONT_NAME, 40, "bold"), bg = YELLOW, fg = RED)
text_timer.grid(row = 1, column = 2)

canvas = Canvas(width = 240, height = 350, bg = YELLOW, highlightthickness = 0)
tomato_img = PhotoImage(file = "Day-21-Python/alarm-bangun-pagi-oey/bangun_pic.png")
canvas.create_image(120, 180, image = tomato_img)
time_remain = canvas.create_text(125, 90, text = f"00:00", font = (FONT_NAME, 35, "bold"))
canvas.grid(row = 2, column = 2)

input_num = Entry(width=6)
input_num.grid(row = 3, column = 2)
start_button = Button(text = "Start", highlightbackground = YELLOW, command = countdown)
start_button.grid(row = 4, column = 2)
reset_button = Button(text = "Reset", highlightbackground = YELLOW, command = reset_timer)
reset_button.grid(row = 5, column = 2)

window.mainloop()