import discord
from discord.ext import commands
import asyncio
import TweetCollector
import CalendarIntegration
import Weather
import UnitConversion
import random
import os
from settings import BOT_TOKEN

#bot = commands.Bot(command_prefix='The Good Boy', description='Posts doggo videos or something')
description = 'Posts doggo videos or something'


bot = commands.Bot(command_prefix='?', description=description)

#WeRateDogs twitter
weRateDogs = TweetCollector.TweetCollector(4196983835)

#DailyDose of Puppies twitter
theDailyPuppy = TweetCollector.TweetCollector(2357252378)

calendar = CalendarIntegration.CalendarIntegration()

owm = Weather.Weather()

units = UnitConversion.UnitConversion()

@bot.event
async def on_ready():
    print('Logged in as')
    print(bot.user.name)
    print(bot.user.id)
    print('--------')


"""
Commands
"""
@bot.command()
async def hello():
    """Says Hello"""
    await bot.say('Hello')

@bot.command()
async def calc(left : int, right : int):
    """"Adds two numbers together"""
    await bot.say(left + right)

@bot.command()
async def randomPupper():
    """Tweepy test. Prints a tweet from the user's timeline"""
    await bot.say(theDailyPuppy.getTweetsFromTimeline(100)[random.randint(0,100)])

from datetime import date
@bot.command()
async def add_event_to_calendar(title, day='{}'.format(date.today()), description = ''):
    """Add an event to the calendar. Events need a Title, a day
        Example usage: ?add_event_to_calendar Event1 2018-09-22
        Date MUST be in the format of YYYY-MM-DD to be accepted
        If no date is provided, it will default to today's date
    """

    await bot.say(calendar.create_event(title, day, description))

@bot.command()
async def get_events_on_date(day='{}'.format(date.today())):
    """Get a list of all events on the calendar for a specified day
            Example usage: ?get_events_on_date 2018-09-22
            Date MUST be in the format of YYYY-MM-DD to be accepted
            If no date is provided, it will default to today's date
    """
    await bot.say('Here are the events on: {}'.format(day))
    for event in calendar.check_day(day):
        await bot.say(event['summary'])

@bot.command()
async def delete_event_on_date(event_name, day='{}'.format(date.today())):
    """Delete the first occurence of an event for the specified day.
        First occurence means if there are multiple evetnts with the same name on the same day, this must be run once
        for each of those events.
        Example usage: ?delete_event_on_date Event1 2018-09-22
        Date MUST be in the format of YYYY-MM-DD to be accepted
        If no date is provided, it will default to today's date
    """
    await bot.say(calendar.delete_event(event_name, day))

from geopy.geocoders import Nominatim
@bot.command()
async def get_weather(location):
    """
    Provide a location and receive relatively up to date weather information. You can either be highly specific, such as
    an exact address, or you can be more broad, such as a city and country.
    :param location:
    :return:
    """
    geolocator = Nominatim()
    geocoded_location = geolocator.geocode(location)
    weather_data = owm.get_weather(geocoded_location.latitude, geocoded_location.longitude)
    await bot.say("**Weather data for {}:**".format(location))
    await bot.say(weather_data)

@bot.command()
async def convert_units(amount, input_units, output_units):
    """
    Converts any number of one unit to another as long as it makes sense to convert them
    Usage: ?convert_units 200 inches feet
    The original unit is the first unit, and what you want that converted to is the second unit
    :param amount:
    :param input_units:
    :param output_units:
    :return: 
    """
    await bot.say(units.convert_units(amount, input_units, output_units))


"""
Background Tasks
"""
#TODO set this up to print out a weather update to a specific channel every x amount of hours
client = discord.Client()
async def weather_update():
    pass

bot.run(BOT_TOKEN)


