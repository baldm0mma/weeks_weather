import csv
import pandas
from functools import reduce
from operator import add

# Getting just the "temps" as integers
# With lambda map
with open("./weather_data.csv") as f:
    data = f.read().splitlines()[1:]
    temps = list(map(lambda item: int(item.split(",")[1]), data))
    print(temps, "lambda")
# Will print the following -> `[12, 14, 15, 14, 21, 22, 24] lambda`

# With csv module
with open("./weather_data.csv") as f:
    data = csv.reader(f)
    next(data, None)
    temps = list(map(lambda item: int(item[1]), data))
    print(temps, "csv")
# Will print the following -> `[12, 14, 15, 14, 21, 22, 24] csv`

# With pandas module
pandas_data = pandas.read_csv("./weather_data.csv")
temps = pandas_data["temp"].to_list()
print(temps, "pandas list temps")
# Will print the following -> `[12, 14, 15, 14, 21, 22, 24] pandas list temps`

# Get mean temp
# With functools
ave_temp = reduce(add, temps) / len(temps)
# With sum()
ave_temp = sum(temps) / len(temps)
# With series.mean()
ave_temp = pandas_data["temp"].mean()
print(ave_temp, "pandas ave temp")
# Will print the following -> `17.428571428571427 pandas ave temp`

# Get max temp
max_temp = pandas_data["temp"].max()
print(max_temp, "pandas max temp")

# Map to python data types
data_to_dict = pandas_data.to_dict()
print(data_to_dict)
# Will print the following ->
# {
#     'day':
#         {0: 'Monday', 1: 'Tuesday', 2: 'Wednesday', 3: 'Thursday',
#             4: 'Friday', 5: 'Saturday', 6: 'Sunday'},
#     'temp': {0: 12, 1: 14, 2: 15, 3: 14, 4: 21, 5: 22, 6: 24},
#     'condition':
#         {0: 'Sunny', 1: 'Rain', 2: 'Rain', 3: 'Cloudy',
#             4: 'Sunny', 5: 'Sunny', 6: 'Sunny'}
# }

data_to_list = pandas_data["day"].to_list()
print(data_to_list, "days")
# Will print the following -> `['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday'] days`

# Grab rows
highest_temp_row = pandas_data[pandas_data["temp"]
                               == pandas_data["temp"].max()]
print(highest_temp_row, "pandas row with filter")

# Create Dataframe from scratch
data_dict = {
    "students": ["biff", "jeff", "meff"],
    "scores": [58, 69, 99]
}
built_dataframe = pandas.DataFrame(data_dict)
print(built_dataframe, "pandas built dataframe")
built_dataframe.to_csv("./new_data.csv")
