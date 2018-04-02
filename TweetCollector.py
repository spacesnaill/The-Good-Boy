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

    def getUserName(self):
        return self.user.screen_name
