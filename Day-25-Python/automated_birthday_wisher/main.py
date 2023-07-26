from email.mime.text import MIMEText
import datetime as dt
import pandas as pd
import smtplib
import random

my_email = "andifarhan1094@gmail.com"
password = "abc"

# Now Date
now = dt.datetime.now()
day_now = now.day
month_now = now.month

# Target
birthday = pd.read_csv("Day-25-Python/automated_birthday_wisher/birthdays.csv")
try:
    target = birthday[(birthday["month"]==month_now) & (birthday["day"]==day_now)]
    target_email = target.iloc[0]["email"]
    target_name = target.iloc[0]["name"]
except:
    raise SystemExit("None of your friend in the list are having a birthday")

# Open template
letter = ["letter_1.txt", "letter_2.txt", "letter_3.txt"]
letter = random.choice(letter)

# Message Text
with open(f"Day-25-Python/automated_birthday_wisher/letter_templates/{letter}", "rt") as letter_file:
    letter = letter_file.read()
    letter = letter.replace("[NAME]", target_name)

message = MIMEText(letter, "plain")
message["Subject"] = "Happy Birthday!"
message["From"] = my_email
message["To"] = target_email

with smtplib.SMTP("smtp.gmail.com", 587) as connection:
    connection.starttls()
    connection.login(user = my_email, password=password)
    connection.send_message(message)