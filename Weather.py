#DONE import PYOWM or use OpenWeatherData, getting the data in JSON format and then parsing it with Python
#DONE make a method for current weather data
#TODO make a method for 5 day forecast
#TODO possibly make weather alerts

import pyowm
from settings import OWM_API_KEY
from discord import Client

class Weather:

    def __init__(self):
        self.owm = pyowm.OWM(OWM_API_KEY)


    # TODO may refactor this to return all the weather data and have the caller pick out what they want to increase reusability
    def get_weather(self, latitude, longitude):
        observation = self.owm.weather_at_coords(latitude, longitude)
        weather = observation.get_weather()

        return 'Current Temperature: {} F\N{DEGREE SIGN}\n' \
               'Temperature High: {} F\N{DEGREE SIGN}\n' \
               'Temperature Low: {} F\N{DEGREE SIGN}\n' \
               'Wind Speed: {}mph\n' \
               'Cloudiness: {}%\n' \
               'Humidity: {}\n' \
               'Status: {}'.format(weather.get_temperature('fahrenheit')['temp'],
                                   weather.get_temperature('fahrenheit')['temp_max'],
                                   weather.get_temperature('fahrenheit')['temp_min'],
                                   weather.get_wind()['speed'],
                                   weather.get_clouds(),
                                   weather.get_humidity(),
                                   weather.get_status(),
                                      )