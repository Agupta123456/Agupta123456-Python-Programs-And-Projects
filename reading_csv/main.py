# with open("weather_data.csv") as data_file:
#     data = data_file.readlines()
#     print(data)
#
# # task: print temperature and its data type will be number not string
# import csv
#
# with open("weather_data.csv") as data_file:
#     data = csv.reader(data_file)
#     temperature = []
#
#     for row in data:
#         if row[1] != "temp":
#             temperature.append(int(row[1]))
#
#     print(temperature)

# using pandas library

import pandas

data = pandas.read_csv("weather_data.csv")

# print(data["temp"])

print(data[data.temp == data.temp.max()])

# create DataFrames from scratch

data_dict = {
    "student" : ["Amy", "ABC", "XYZ"],
    "scores" : [78, 56, 55]
}

data = pandas.DataFrame(data_dict)
print(data)

data.to_csv("new_list.csv")