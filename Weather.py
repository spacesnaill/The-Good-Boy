#TODO import PYOWM or use OpenWeatherData, getting the data in JSON format and then parsing it with Python
#TODO make a method for current weather data
#TODO make a method for 5 day forecast
#TODO possibly make weather alerts

import pyowm
from settings import OWM_API_KEY

class Weather:

    def __init__(self):
        self.owm = pyowm.OWM(OWM_API_KEY)

    def get_weather(self, city, country):
        observation = self.owm.weather_at_place('{},{}'.format(city, country))
        weather = observation.get_weather()
        return weather