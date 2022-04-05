import pandas as pd

squirrel_data = pd.read_csv(
    "./2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")
colors = [color for color in list(set(squirrel_data["Primary Fur Color"].to_list())) if type(color) == str]
print(colors)
