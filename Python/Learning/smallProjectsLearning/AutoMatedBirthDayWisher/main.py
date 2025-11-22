##################### Extra Hard Starting Project ######################

# 1. Update the birthdays.csv

# 2. Check if today matches a birthday in the birthdays.csv

# 3. If step 2 is true, pick a random letter from letter templates and replace the [NAME] with the person's actual name from birthdays.csv

# 4. Send the letter generated in step 3 to that person's email address.


import sys
import os

import smtplib
import datetime 
import pandas 
import random
today = (datetime.datetime.now().month,datetime.datetime.now().day)
data = pandas.read_csv("birthdays.csv")

import  os
from dotenv import load_dotenv

load_dotenv()
def sendEmail(message="Subject: testing email from python\n\nHELLO FROM PYTHON",destination = os.environ.get("receiver_email")):
    email = os.environ.get("sender_email")
    app_password = os.environ.get("app_password") #
    with smtplib.SMTP("smtp.gmail.com") as connection:
            connection.starttls()
            connection.login(user=email,password = app_password)
            connection.sendmail(from_addr=email,to_addrs=destination,msg=message)
            connection.close()

# birthdays_dict = {(birthday_month,birthday_day):data_row}
new_dict = {(data_row.month,data_row.date): data_row for (index,data_row) in data.iterrows()}
if today in new_dict:
    birthday_person = new_dict[today]
    file_path = f"letter_templates/letter_{random.randint(1,3)}.txt"
    with open(file_path) as letterfile:
        contents = letterfile.read()
        final_contents= contents.replace("[NAME]",birthday_person["name"])
        sendEmail(message=f"Subject:Happy Birthday!!\n\n{final_contents}",destination=birthday_person["email"])
        print(final_contents)
    #sendTheLetter

    #sendBirthdayWish():





###############TBC#####################################
# def getBirthDay(date):
#     data = pandas.read_csv("birthdays.csv")
#     Birthdate = data["date"]
#     BirthMonth = data["month"] 
#     if  Birthdate == now.date and   BirthMonth == now.month:
#         name = data[data[data.day == "Monday"]]
#         wishBirthday(name):


# year  = now.year
# now.month
# date = now.date()
#age = now - date_of_birth
# age_in_years = age//365
# print(age_in_years)
