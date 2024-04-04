import requests
from twilio.rest import Client
from dotenv import find_dotenv, load_dotenv
import os

dotenv_path = find_dotenv()
load_dotenv(dotenv_path)

ACCOUNT_SID = os.getenv("ACCOUNT_SID")
AUTH_TOKEN = os.getenv("AUTH_TOKEN")
API_KEY = os.getenv("API_KEY")
latitude = 35.143379
longitude = -90.052139


weather_codes = []

parameters = {
    "lat": latitude,
    "lon": longitude,
    "appid": API_KEY,
    "cnt": 4,
}

response = requests.get('https://api.openweathermap.org/data/2.5/forecast', params=parameters)
response.raise_for_status()
data = response.json()

will_rain = False
for i in range(len(data['list'])):
    if int(data['list'][i]['weather'][0]['id']) < 700:
        will_rain = True

if will_rain:
    client = Client(ACCOUNT_SID, AUTH_TOKEN)

    message = client.messages \
        .create(
        body="It is going to rain today. Remember to bring an umbrella",
        from_='+14159385334',
        to='+817014610143'
    )
    print(message.status)
