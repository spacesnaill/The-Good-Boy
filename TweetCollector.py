import tweepy

class TweetCollector:

    #Set up to use the twitter api through Tweepy
    auth = tweepy.OAuthHandler('djOUfbU4YXBoDZL0ZeLnPqGX6', 'shSx1lVShE0wrZ6rDURQhtORNoCFhQYqwWnQYhyL4M9CMljqCv')
    auth.set_access_token('3044253956-GqacM6MLHi3zuAkqhBTzaHkJCXQdDm1ZSPzC8RN',
                          'BVIbFYWck2oB9MOqmLqxzcowHEoTCVmP2tItbh1HiEYFd')
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

