import tweepy
import os
from settings import TWITTER_API_KEY, TWITTER_API_SECRET, TWITTER_ACCESS_TOKEN, TWITTER_ACCESS_TOKEN_SECRET

class TweetCollector:

    #Set up to use the twitter api through Tweepy
    auth = tweepy.OAuthHandler(TWITTER_API_KEY, TWITTER_API_SECRET)
    auth.set_access_token(TWITTER_ACCESS_TOKEN, TWITTER_ACCESS_TOKEN_SECRET)
    tweepy_api = tweepy.API(auth)

    def __init__(self, twitterID):
        self.twitterID = twitterID
        self.user = self.tweepy_api.get_user(twitterID)
   #     self.timeLine = self.tweepy_api.user_timeline(self.user)

    def getUserName(self):
        return self.user.screen_name

    def getTimeline(self):
        return self.timeLine

    def getTweetsFromTimeline(self, amountOfTweets):
        #output is a List
        outputList = []

        #get the timeline for the user
        timeLine = self.tweepy_api.user_timeline(screen_name = self.getUserName(), count = amountOfTweets)

        #go through each status in the timeline and check for two things: is the tweet NOT a status? does the tweet have media associated with it?
        #print the URL of the media if both are true
        for status in timeLine:
            if status.in_reply_to_status_id == None:
                if 'media' in status.entities:
                    for image in status.entities['media']:
                        outputList.append(image['media_url'])

        return outputList

