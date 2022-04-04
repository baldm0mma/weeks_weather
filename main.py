import csv
import pandas

# Getting just the "temps" as integers
# With lambda map
with open("./weather_data.csv") as f:
    data = f.read().splitlines()[1:]
    temps = list(map(lambda item: int(item.split(",")[1]), data))
    print(temps, "lambda")

# With csv module
with open("./weather_data.csv") as f:
    data = csv.reader(f)
    next(data, None)
    temps = list(map(lambda item: int(item[1]), data))
    print(temps, "csv")

# With pandas module
pandas_data = pandas.read_csv("./weather_data.csv")
temps = pandas_data["temp"].tolist()
print(temps, "pandas")
