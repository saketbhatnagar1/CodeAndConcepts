

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
#Get data in row:

print(data[data.day == "Monday"])
maxtemp = data["temp"].max()
print(f"max tempreature's row is\n {data[data.temp == maxtemp]}")

#Create A dataframe from scratch:
data_dict_planes = {
    "Aircrafts":["SU30MKI","DASSAULT RAFALE","MIRAGE 2000"],
    "Strength":[270,36,60]
}
Aircraft_Data = pandas.DataFrame(data_dict_planes)
print(Aircraft_Data)
Aircraft_Data.to_csv("Aircraft_Data.csv")