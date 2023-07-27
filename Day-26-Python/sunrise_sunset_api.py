import smtplib
import requests
from datetime import datetime

my_latitude = -0.501617
my_longitude = 117.126472

# Sunrise Sunset API
now = datetime.now()
now_hour = now.hour

parameters = {
    "lat" : my_latitude,
    "lng" : my_longitude,
    "date" : now.strftime('%Y-%m-%d'),
    "formatted" : 0,
}
response_1 = requests.get(url = "https://api.sunrise-sunset.org/json", params = parameters)
response_1.raise_for_status()
sun_data = response_1.json()
sunrise_hour = int(sun_data["results"]["sunrise"].split("T")[1].split(":")[0])
sunset_hour = int(sun_data["results"]["sunset"].split("T")[1].split(":")[0])

sunrise_day = int(sun_data["results"]["sunrise"].split("T")[0].split("-")[2])
sunset_day = int(sun_data["results"]["sunset"].split("T")[0].split("-")[2])


# ISS Tracker API
response_2 = requests.get(url = "http://api.open-notify.org/iss-now.json")
response_2.raise_for_status()
iss_data = response_2.json()
iss_latitude = float(iss_data["iss_position"]["latitude"])
iss_longitude = float(iss_data["iss_position"]["longitude"])


# Check condition
if (my_latitude >= iss_latitude - 5) and (my_latitude <= iss_latitude + 5) and (my_longitude >= iss_longitude - 5) and (my_longitude <= iss_longitude + 5) and (now_hour < sunrise_hour) and (now_hour >= sunset_hour):
    with smtplib.SMTP("smtp.gmail.com", 587) as connection:
        connection.login(user = "andifarhan1094@gmail.com", password = "abc")
        connection.starttls()
        connection.sendmail(
            from_addr = "andifarhan1094@gmail.com",
            to_addrs = "19623112@mahasiswa.itb.ac.id",
            msg = "Subject: Notification\n\nISS is above you right now! Go check it out!"
        )
else: print("There is no ISS above you")