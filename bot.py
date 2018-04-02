import discord
from discord.ext import commands
import TweetCollector

#bot = commands.Bot(command_prefix='The Good Boy', description='Posts doggo videos or something')
description = 'Posts doggo videos or something'


bot = commands.Bot(command_prefix='?', description=description)
twitterAPI = TweetCollector.TweetCollector(4196983835)


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

#TODO
#https://stackoverflow.com/questions/32022845/get-the-last-tweet-with-tweepy
@bot.command()
async def tweepyScreenName():
    """Tweepy test. Prints Screen name"""
    await bot.say(twitterAPI.getUserName())


bot.run('NDIyMTMyODY3NTI3NjA2Mjgy.DYXbUA.0o1GzCytBr8DJcdUU7WvXOgKAts')


