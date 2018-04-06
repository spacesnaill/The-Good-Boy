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
        return 'Current Temperature: {} ' \
               'Temperature High: {}' \
               'Temperature Low: {}' \
               'Wind Speed: {}' \
               'Cloudiness %: {}' \
               'Humidity: {}' \
               'Status: {}'.format(weather.get_temperature('fahrenheit')['temp'],
                                   weather.get_temperature('fahrenheit')['temp_max'],
                                   weather.get_temperature('fahrenheit')['temp_min'],
                                   weather.get_wind()['speed'],
                                   weather.get_clouds(),
                                   weather.get_humidity(),
                                   weather.get_status(),
                                   )