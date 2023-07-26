import smtplib
import random
import datetime as dt
from email.mime.text import MIMEText

my_email = "andifarhan1094@gmail.com"
password = "mmmbtchpwvufbnjj"

with open("Day-25-Python/motivational_mail/quotes.txt", encoding = "utf-8") as quotes:
    quotes_data = quotes.readlines()
    quote = quotes_data[random.randrange(0, len(quotes_data))]

now = dt.datetime.now()
day_now = now.weekday()
match day_now:
    case 0:
        day_now = "Monday"
    case 1:
        day_now = "Tuesday"
    case 2:
        day_now = "Wednesday"
    case 3:
        day_now = "Thursday"
    case 4:
        day_now = "Friday"
    case 5:
        day_now = "Saturday"
    case 6:
        day_now = "Sunday"

text = f"""\
Happy {day_now}!
{quote}"""

message = MIMEText(text, "plain")
message["Subject"] = "First long text email"
message["From"] = my_email
message["To"] = "19623112@mahasiswa.itb.ac.id"


with smtplib.SMTP("smtp.gmail.com", 587) as connection:
    connection.starttls()
    connection.login(user = my_email, password = password)
    connection.send_message(message)