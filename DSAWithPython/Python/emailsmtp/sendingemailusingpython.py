#SMTP:
import smtplib
import  os
from dotenv import load_dotenv

load_dotenv()
email = os.environ.get("sender_email")
destination = os.environ.get("receiver_email")
app_password = os.environ.get("app_password") #
with smtplib.SMTP("smtp.gmail.com") as connection:
    connection.starttls()
    connection.login(user=email,password = app_password)
    connection.sendmail(from_addr=email,to_addrs=destination,msg="Subject: testing email from python\n\nHELLO FROM PYTHON")
    connection.close()