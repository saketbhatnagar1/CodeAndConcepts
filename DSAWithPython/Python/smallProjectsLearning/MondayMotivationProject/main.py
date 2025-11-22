import sys
import datetime as dt
import random

# Add folder containing emailsmtp
sys.path.append(r"C:\Users\saket\OneDrive\Desktop\MastersItaly\JSIA\DSA\UdemyCourses\DSAWithPython\Python")

from emailsmtp.sendingemailusingpython import sendEmail

now = dt.datetime.now()

def pickQuotes():
    with open("money_motivation_hustle_quotes.txt", "r", encoding="utf-8") as f:
        quotes = f.readlines()
        return random.choice(quotes).strip()

if now.weekday() == 5:  # Saturday
    message = f"Subject: Monday Motivation\n\n{pickQuotes()}"
    sendEmail(message=message)
#################SEND EMAIL IMPLEMENTATION #############################################
# def sendEmail(message="Subject: testing email from python\n\nHELLO FROM PYTHON"):
#     email = os.environ.get("sender_email")
#     destination = os.environ.get("receiver_email")
#     app_password = os.environ.get("app_password") #
#     with smtplib.SMTP("smtp.gmail.com") as connection:
#             connection.starttls()
#             connection.login(user=email,password = app_password)
#             connection.sendmail(from_addr=email,to_addrs=destination,msg=message)
#             connection.close()