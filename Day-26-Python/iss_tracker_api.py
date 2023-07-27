import requests

response = requests.get(url = "http://api.open-notify.org/iss-now.json")
iss_data = response.json()
iss_latlong = (iss_data["iss_position"]["latitude"], iss_data["iss_position"]["longitude"])
print(iss_latlong)