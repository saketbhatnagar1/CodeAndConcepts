import requests
from datetime import datetime
import os
import smtplib
time_now = datetime.now().hour

def is_iss_overhead(MYLONG=-0.127758,MYLAT=51.507351):
    parametres = {
        "lat": MYLAT,
        "lng": MYLONG,
        "formatted":0,
    }
    response = requests.get(url="http://api.open-notify.org/iss-now.json")
    data = response.json()
    iss_longitude = float(data.get("iss_position").get("longitude"))
    iss_latitude = float(data.get("iss_position").get("latitude"))
    if (MYLAT-5 <= iss_latitude <= MYLAT+5) and (MYLONG-5 <= iss_longitude <= MYLONG):
        return True
def isNight():
    sun_response = requests.get("https://api.sunrise-sunset.org/json",params=parametres)
    data = sun_response.json()
    sunrisetime = data.get("results").get("sunrise")
    sunsettime = data.get("results").get("sunset")
    sunrise = int(data["result"]["sunrise"].spllit("T")[1].split(":")[0])
    sunset = int(data["result"]["sunset"].spllit("T")[1].split(":")[0])
    if time_now >= sunrisetime or time_now<= sunrise:
        return True
while True:
    time.sleep(60)
    if is_iss_overhead() and isNight():
        email = os.environ.get("sender_email")
        app_password = os.environ.get("app_password") #
        destination = os.environ.get("sender_email")
        with smtplib.SMTP("smtp.gmail.com") as connection:
                connection.starttls()
                connection.login(user=email,password = app_password)
                connection.sendmail(from_addr=email,to_addrs=destination,msg=f"Subject: Look up ISS is OverHead at sky")
                connection.close()