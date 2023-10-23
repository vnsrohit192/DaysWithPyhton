import requests
from datetime import datetime, timedelta
STOCK = "TSLA"
COMPANY_NAME = "Tesla Inc"
from datetime import date
from datetime import timedelta
from twilio.rest import Client

url = f"https://www.alphavantage.co/query?function=TIME_SERIES_DAILY_ADJUSTED&symbol={STOCK}&apikey=Q5E1L4I95NW8C221"
r = requests.get(url)
data = r.json()

today = date.today()
yesterday =today - timedelta(days = 1)
day_bef_yestd=yesterday-timedelta(days=1)

yester_data=data["Time Series (Daily)"][f"{yesterday}"]['4. close']
day_before_yester_data=data["Time Series (Daily)"][f'{day_bef_yestd}']['4. close']
difference=float(yester_data)-float(day_before_yester_data)
percent_change=(difference/float(day_before_yester_data))*100
x=int(percent_change)
symbol=""
if difference>0:
    symbol="🔺"
else:
    symbol="🔻"      

if difference>=5 or difference<=-5:
    news_api_key="20331b165d544bb380269222aafe2667"
    url = f'https://newsapi.org/v2/everything?q={COMPANY_NAME}&from=2023-04-13&sortBy=popularity&apiKey={news_api_key}'

    response = requests.get(url)
    news_data=response.json()
    artical_title1=news_data['articles'][0]["title"]
    artical_description1=news_data['articles'][0]["description"]
    artical_title2=news_data['articles'][1]["title"]
    artical_description2=news_data['articles'][1]["description"]
    message=f"Headline: {artical_title1}\nBrief :{artical_description1}\nHeadline: {artical_title2}\nBrief: {artical_description2}"
  
    account_sid ='ACf4a7881035b41ebd9ed8717281e208fe'
    auth_token = 'b5c0020cd96b8b44eb2f142aa04439a7'
    client = Client(account_sid, auth_token)

    message = client.messages \
                    .create(
                        body=f"\nTSLA: {symbol}{x}%\n{message} ",
                        from_='+15076773832',
                        to='+919695759830'
                    )
    print(message.sid)
