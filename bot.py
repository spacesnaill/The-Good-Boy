import discord
from discord.ext import commands
import TweetCollector
import traceback
import random

#bot = commands.Bot(command_prefix='The Good Boy', description='Posts doggo videos or something')
description = 'Posts doggo videos or something'


bot = commands.Bot(command_prefix='?', description=description)

#WeRateDogs twitter
weRateDogs = TweetCollector.TweetCollector(4196983835)

#DailyDose of Puppies twitter
theDailyPuppy = TweetCollector.TweetCollector(2357252378)


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
async def add(left : int, right : int):
    """"Adds two numbers together"""
    await bot.say(left + right)

@bot.command()
async def randomPupper():
    """Tweepy test. Prints a tweet from the user's timeline"""
    await bot.say(theDailyPuppy.getTweetFromTimeline(100)[random.randint(0,100)])



bot.run('NDIyMTMyODY3NTI3NjA2Mjgy.DYXbUA.0o1GzCytBr8DJcdUU7WvXOgKAts')


