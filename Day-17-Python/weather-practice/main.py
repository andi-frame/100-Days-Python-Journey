import pandas as pd

# PROCESSING SCV FILE USING IMPORT CSV:
# import csv
# with open("Day-17-Python/weather-data.csv") as weather_data:
#     csv_data = csv.reader(weather_data)
#     temperatures = []
    
#     for value in csv_data:
#         if value[1] != 'temp':
#             temperatures.append(int(value[1]))
#     print(temperatures)

data = pd.read_csv("Day-17-Python/weather-practice/weather-data.csv")

# print(data["temp"].mean())
# max_temp = data["temp"].max()
# print(data[data["temp"] == max_temp])

monday = data[data["day"] == "Monday"]

monday.at[0,"temp"] = monday.at[0,"temp"]*(9/5) + 32
print(monday.at[0, "temp"])

