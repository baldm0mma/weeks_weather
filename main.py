import pandas as pd

# Read csv data with pandas
squirrel_data = pd.read_csv(
    "./2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")

# Get all possible colors
all_colors = squirrel_data["Primary Fur Color"].to_list()
# Remove dupes
non_duped_colors = list(set(all_colors))
# Remove non-string values with list comprehension
final_colors = [color for color in non_duped_colors if type(color) == str]
# Or, in one line ->
# colors = [color for color in list(set(squirrel_data["Primary Fur Color"].to_list())) if type(color) == str]
# print(final_colors)

# Create dataframe with fur colors and count of each
# Build dict to hold data
squirrel_color_dict = {"Fur Color": [], "Count": []}
# Loop over colors from above and get count
for color in final_colors:
    # Get count of particular color
    squirrel_color_count = len(
        squirrel_data[squirrel_data["Primary Fur Color"] == color])
    # Add color and count to dict
    squirrel_color_dict["Fur Color"].append(color)
    squirrel_color_dict["Count"].append(squirrel_color_count)

# Build dataframe from dict
squirrel_color_dataframe = pd.DataFrame(squirrel_color_dict)
print(squirrel_color_dataframe)
squirrel_color_dataframe.to_csv("squirrel_count.csv")
