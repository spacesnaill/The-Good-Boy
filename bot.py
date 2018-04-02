import discord
import tweepy
from discord.ext import commands
import json
import subprocess
import shlex

#bot = commands.Bot(command_prefix='The Good Boy', description='Posts doggo videos or something')
#override tweepy.StreamListener
class MyStreamListener(tweepy.StreamListener):
    def on_status(self, status):
        print(status.text)

    def on_data(self, data):
        tweet = json.loads(data)
        #for x in tweet:
         #   print(tweet[x])
        sTweet = 'http://twitter.com/{}/status/{}'.format(tweet['id'], tweet['id_str'])

    def on_error(self, status_code):
        print(status_code)

description = 'Posts doggo videos or something'
auth = tweepy.OAuthHandler('djOUfbU4YXBoDZL0ZeLnPqGX6', 'shSx1lVShE0wrZ6rDURQhtORNoCFhQYqwWnQYhyL4M9CMljqCv')
auth.set_access_token('3044253956-GqacM6MLHi3zuAkqhBTzaHkJCXQdDm1ZSPzC8RN', 'BVIbFYWck2oB9MOqmLqxzcowHEoTCVmP2tItbh1HiEYFd')
tweepy_api = tweepy.API(auth)

bot = commands.Bot(command_prefix='?', description=description)

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
async def tweets():
    """Gathers tweets"""
    # myStreamListener = MyStreamListener()
    # myStream = tweepy.Stream(auth = api.auth, listener = myStreamListener)
    # myStream.filter(follow=["4196983835", "575930104"])
    user1 = tweepy_api.get_user('dog_rates')
    print('http://twitter.com/{}/status/{}'.format(user1.id, user1.status.id))
    await bot.say('http://twitter.com/{}/status/{}'.format(user1.id, user1.status.id))


bot.run('NDIyMTMyODY3NTI3NjA2Mjgy.DYXbUA.0o1GzCytBr8DJcdUU7WvXOgKAts')


