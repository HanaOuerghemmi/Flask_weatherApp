
from dotenv import load_dotenv
import os

import requests

from dataclasses import dataclass
  
load_dotenv()
api_key = os.getenv('API_KEY')


@dataclass
class WeatherData:
    main: str
    desscription: str
    icon: str
    temperature: float

def get_lan_lon(city_name, state_code, country_code, API_key):
    res = requests.get(
        f'http://api.openweathermap.org/geo/1.0/direct?q={city_name},{state_code},{country_code}&appid={API_key}').json()
    data =res[0]
    lat, lon = data.get('lat'), data.get('lon')

    return lat, lon


def get_current_weather(lat, lon, API_key):
    res = requests.get(
        f'https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={API_key}&units=metric').json()

    data = WeatherData(
        main=res.get('weather')[0].get('main'),
        desscription= res.get('weather')[0].get('description'),
        icon= res.get('weather')[0].get('icon'),
        temperature=res.get('main').get('temp'),
    )
    return data


def main(city_name, state_code, country_code):
     lat, lon = get_lan_lon('Toronto', 'ON', 'Canada', api_key)
     weather_data=get_current_weather(lat, lon, api_key)
     return weather_data


if __name__ =="__main__":

    lat, lon = get_lan_lon('Toronto', 'ON', 'Canada', api_key)
    print(get_current_weather(lat, lon, api_key))