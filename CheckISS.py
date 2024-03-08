##API practice

import requests
import smtplib
from datetime import datetime

MY_LAT = 41.878
MY_LONG = 87.629

response1 = requests.get(url="http://api.open-notify.org/iss-now.json")
#Report request error
response1.raise_for_status()

long = float(response1.json()["iss_position"]["longitude"])
lat = float(response1.json()["iss_position"]["latitude"])

iss_position = (long, lat)

print(iss_position)

paramaters = {
    "lat": MY_LAT,
    "lng": MY_LONG,
    "formatted": 0
}

response = requests.get("https://api.sunrise-sunset.org/json", params=paramaters)
response.raise_for_status()
data = response.json()
sunrise = data["results"]["sunrise"]
sunset = data["results"]["sunset"].split("T")[1].split(":")[0]
sunset = int(sunset)

time = (sunrise,sunset)

time_now = datetime.now()
hour_now = datetime.now().hour
print(hour_now)

#If the ISS is close to my current position and it is dark,
#Then send me an email to tell me to look up

#Position is within +/-5 degrees of the ISS position

LatRange = (MY_LAT-5, MY_LAT+5)
LonRange = (MY_LONG-5, MY_LONG+5)

#Check to see if ISS within range of vision:
def checkISS():
    if lat > LatRange[0] and lat < LatRange[1] and long > LonRange[0] and long < LonRange[1]:
        return True
    else:
        return False


def checkNighttime():
    if hour_now > sunset:
        print("True")
        return True
    else:
        print("False")
        return False

my_email = "yj96throwaway@gmail.com"
password = "eanq qemm bevo zsls"

if checkISS() and checkNighttime():
    with smtplib.SMTP('smtp.gmail.com') as connection:
        connection.starttls()
        connection.login(user=my_email, password=password)
        connection.sendmail(from_addr=my_email,
                            to_addrs="yaseenj96@gmail.com",
                            msg=f"Subject:Check the ISS!\n\nLook up in the sky!")
else:
    with smtplib.SMTP('smtp.gmail.com') as connection:
        connection.starttls()
        connection.login(user=my_email, password=password)
        connection.sendmail(from_addr=my_email,
                            to_addrs="yaseenj96@gmail.com",
                            msg=f"Subject:Do not check the ISS!\n\nThe ISS is not visible!")
