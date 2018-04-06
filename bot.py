import discord
from discord.ext import commands
import TweetCollector
import CalendarIntegration
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

@bot.event
async def on_ready():
    print('Logged in as')
    print(bot.user.name)
    print(bot.user.id)
    print('--------')

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

@bot.command()
async def calendarAdd(title, day, description = ''):
    """Add an event to the calendar. Events need a Title, a day
        Example usage: ?calendarAdd Event1 2018-09-22
        Date MUST be in the format of YYYY-MM-DD to be accepted
    """

    await bot.say(calendar.create_event(title, day, description))

@bot.command()
async def get_events_on_date(day):
    await bot.say('Here are the events on: {}'.format(day))
    for event in calendar.check_day(day):
        await bot.say(event)


bot.run(BOT_TOKEN)


