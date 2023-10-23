import requests
import datetime as dt
import smtplib
import time

def over_head():
    response=requests.get(url="http://api.open-notify.org/iss-now.json")
    response.raise_for_status()
    data=response.json()

    latitude=data["iss_position"]["latitude"]
    longitude=data["iss_position"]["longitude"]

    if my_lng-5<=longitude<=my_lng+5 and my_lat<=latitude<=my_lat+5:
        return True

my_lat=28.573839
my_lng=77.219391



def night():
    parameter={
        "lat":my_lat,
        "lng":my_lat,
        "formatted":0
    }

    response=requests.get(url="https://api.sunrise-sunset.org/json",params=parameter)
    response.raise_for_status()
    data=response.json()
    sunrise=data["results"]["sunrise"].split("T")[1].split(":")[0]
    sunset=data["results"]["sunset"].split("T")[1].split(":")[0]

    time_now=dt.datetime.now().hour
    if time_now>=sunset or time_now<=sunrise:
        return True
    

while True:
    time.sleep(3)
    if over_head and night:
        s=smtplib.SMTP("smtp.gmail.com")
        mail="jayamadhva@gmail.com"
        password_iss="umquyssrbypsckca"
        s.starttls()
        s.login(mail,password_iss)
        message="look up the iss is above you"
        s.sendmail(mail,"kathakmadhav@gmail.com",message)
        s.close()


#If the ISS is close to my current position
# and it is currently dark
# Then send me an email to tell me to look up.
# run the code every 60 seconds.
