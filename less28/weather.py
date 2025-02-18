"""
docs:
https://openweathermap.org/current
https://openweathermap.org/api/geocoding-api
"""
import requests
from enviroment import apid


class City:
    def __init__(self, name: str):
        self._name = name

    @property
    def name(self):
        return self._name


city = City('Izhevsk')
url = 'http://api.openweathermap.org/geo/1.0/direct?q={},RU&limit=5&appid={}'
resp = requests.get(url.format(city.name, apid)).json()
lat = resp[0]['lat']
lon = resp[0]['lon']
print(lat, lon)
url = 'https://api.openweathermap.org/data/2.5/weather?lat={}&lon={}&appid={}&units=metric'
resp = requests.get(url.format(lat, lon, apid)).json()
print(resp)
info = {
    'city_name': city.name,
    'temp': resp['main']['temp'],
    'icon': resp['weather'][0]['icon']
}
print(info)
