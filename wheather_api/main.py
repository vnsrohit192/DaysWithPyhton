import requests
import json
from twilio.rest import Client
lattitude=28.573839
longitude=77.219391

api_key="a0526ebd69900c125e3fd8bd83174617"

weather_param={
    "lat":lattitude,
    "lon":longitude,
    "appid":api_key 
    
}
response=requests.get("https://api.openweathermap.org/data/2.5/weather",params=weather_param)
response.raise_for_status()
json_file=response.json()

condition_code=json_file["weather"][0]["id"]

will_haze=False

for data in json_file:
    if int(condition_code) <800:
            will_haze=True


if will_haze:

    account_sid ='ACf4a7881035b41ebd9ed8717281e208fe'
    auth_token = 'b5c0020cd96b8b44eb2f142aa04439a7'
    client = Client(account_sid, auth_token)

    message = client.messages \
                    .create(
                        body="there is haze hout side ",
                        from_='+15076773832',
                        to='+919695759830'
                    )

    print(message.sid)

