import smtplib
import requests
from datetime import datetime

my_latitude = -0.501617
my_longitude = 117.126472

# Sunrise Sunset API
def is_dark():
    now = datetime.now()
    now_hour = now.hour

    parameters = {
        "lat" : my_latitude,
        "lng" : my_longitude,
        "formatted" : 0,
    }
    response_1 = requests.get(url = "https://api.sunrise-sunset.org/json", params = parameters)
    response_1.raise_for_status()
    sun_data = response_1.json()
    sunrise_hour = int(sun_data["results"]["sunrise"].split("T")[1].split(":")[0])
    sunset_hour = int(sun_data["results"]["sunset"].split("T")[1].split(":")[0])
    if (now_hour < sunrise_hour) and (now_hour >= sunset_hour):
        return True
    else: return False


# ISS Tracker API
def iss_is_above():
    response_2 = requests.get(url = "http://api.open-notify.org/iss-now.json")
    response_2.raise_for_status()
    iss_data = response_2.json()
    iss_latitude = float(iss_data["iss_position"]["latitude"])
    iss_longitude = float(iss_data["iss_position"]["longitude"])
    if (my_latitude-5 <= iss_latitude <= my_latitude+5) and (my_longitude-5 <= iss_longitude <= my_longitude+5):
        return True
    else: return False


# Check condition
if is_dark() and iss_is_above():
    with smtplib.SMTP("smtp.gmail.com", 587) as connection:
        connection.login(user = "andifarhan1094@gmail.com", password = "abc")
        connection.starttls()
        connection.sendmail(
            from_addr = "andifarhan1094@gmail.com",
            to_addrs = "19623112@mahasiswa.itb.ac.id",
            msg = "Subject: Notification\n\nISS is above you right now! Go check it out!"
        )
else: print("There is no ISS above you")