import pandas as pd

data = pd.read_csv("Day-17-Python/squirrel-practice/2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")
# Primary fur color: "gray", "cinnamomn", "black"

# My version:
# gray_count = data["Primary Fur Color"].value_counts()["Gray"]
# cinnamon_count = data["Primary Fur Color"].value_counts()["Cinnamon"]
# black_count = data["Primary Fur Color"].value_counts()["Black"]

gray_count = len(data[data["Primary Fur Color"] == "Gray"])
cinnamon_count = len(data[data["Primary Fur Color"] == "Cinnamon"])
black_count = len(data[data["Primary Fur Color"] == "Black"])

squirrel_fur_color_count = {"Fur Color" : ["Gray", "Cinnamon", "Black"], 
                            "Count" : [gray_count, cinnamon_count, black_count]}

df_fur_count = pd.DataFrame(squirrel_fur_color_count)
df_fur_count.to_csv("Day-17-Python/squirrel-practice/squirrel-fur-count-data.csv")

print(df_fur_count)