from tkinter import * #type: ignore
import math
import pygame


# ---------------------------- CONSTANTS ------------------------------- #
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
timer = None


# ---------------------------- ALARM RESET ------------------------------- # 
def reset_timer():
    global timer
    window.after_cancel(timer) #type: ignore
    canvas.itemconfig(time_remain, text = "00:00")
    input_min.delete(0, "end")  # Delete the current value
    input_min.insert(0, '0')  # Insert the new value of 0
    input_sec.delete(0, "end")  # Delete the current value
    input_sec.insert(0, '0')  # Insert the new value of 0
    pygame.mixer.music.stop()


# ---------------------------- ALARM SOUND ------------------------------- #
pygame.mixer.init()
def play_sound():
    pygame.mixer.music.load("Day-21-Python/alarm-bangun-pagi-oey/classic-alarm.wav")
    pygame.mixer.music.play(loops=0)


# ---------------------------- ALARM START ------------------------------- #
def alarm_start():
    minute_set = int(input_min.get())
    second_set = int(input_sec.get())
    second_sum = (minute_set*60) + second_set
    print(minute_set, second_set, second_sum)
    countdown(second_sum)


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 
def countdown(second_sum):
    global timer
    minute = math.floor(second_sum / 60)
    second = second_sum % 60


    if minute == 0:
        minute = "00"
    elif minute < 10:
        minute = f"0{minute}"


    if second == 0:
        second = "00"
    elif second < 10:
        second = f"0{second}"


    if second_sum == 0:
        play_sound()
    if second_sum >= 0:
        canvas.itemconfig(time_remain, text = f"{minute}:{second}")
        timer = window.after(1000, countdown, second_sum-1)
    
    

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("ALARM")
window.config(padx = 100, pady = 50, bg = YELLOW)


text_timer = Label(text = "Alarm", font = (FONT_NAME, 40, "bold"), bg = YELLOW, fg = RED)
text_timer.grid(row = 1, column = 1)


canvas = Canvas(width = 240, height = 350, bg = YELLOW, highlightthickness = 0)
tomato_img = PhotoImage(file = "Day-21-Python/alarm-bangun-pagi-oey/bangun_pic.png")
canvas.create_image(120, 180, image = tomato_img)
time_remain = canvas.create_text(125, 90, text = f"00:00", font = (FONT_NAME, 35, "bold"))
canvas.grid(row = 2, column = 1, rowspan = 20)


input_min = Spinbox(from_ = 0, to = 9999, width = 5)
input_min.grid(row = 10, column = 2)


input_sec = Spinbox(from_ = 0, to = 60, width = 5)
input_sec.grid(row = 11, column = 2)


min_label = Label(text = "Minute", font = (FONT_NAME, 20, "bold"), bg = YELLOW, fg = GREEN)
min_label.grid(row = 10, column = 3)


sec_label = Label(text = "Second", font = (FONT_NAME, 20, "bold"), bg = YELLOW, fg = GREEN)
sec_label.grid(row = 11, column = 3)


start_button = Button(text = "Start", highlightbackground = YELLOW, command = alarm_start)
start_button.grid(row = 12, column = 2)


reset_button = Button(text = "Reset", highlightbackground = YELLOW, command = reset_timer)
reset_button.grid(row = 12, column = 3)


<<<<<<< HEAD
window.mainloop()
=======
window.mainloop()
>>>>>>> f07363d (first commit to local file of 100python)
