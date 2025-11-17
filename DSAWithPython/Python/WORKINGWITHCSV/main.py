

# with open("weather_data.csv") as data_file:
#     data = data_file.readlines()
# print(data)

# import csv

# with open("weather_data.csv") as datafile:
#     data = csv.reader(datafile)
#     print(f"data is {data}")
#     tempreatures = []
#     for row in data:
#         if row[1]!="temp":
#             tempreatures.append(int(row[1]))
#         print(row)
# print(f"Tempreatures are {tempreatures}")
    
#pandas

import pandas
data = pandas.read_csv("weather_data.csv")
print(f"{data} is the data")
print(f"temp {data["temp"]} ")

print(type(data))
print(f"temp {type(data["temp"])} ")

#Data frame and series

data_dict = data.to_dict() #Convert data to dictionary 
print(data_dict)

temp_list = data["temp"].to_list()
print(temp_list)
print(len(temp_list))
print(sum(temp_list))
print(data["temp"].mean())
print(f"max is {data["temp"].max()}")