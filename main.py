import json
import tweepy

with open('config.json', 'r') as config_file:
    config = json.load(config_file)

with open('keywords.txt', 'r') as keywords_file:
    keywords = keywords_file.read().splitlines()


def check_keyword_in_tweet(tweet):
    isMatch = [True for x in keywords if x.lower() in tweet.lower()]
    return isMatch


class StreamListener(tweepy.Stream):
    def __init__(self, consumer_key, consumer_secret, access_token,
                 access_token_secret, **kwargs):
        super().__init__(consumer_key, consumer_secret, access_token, access_token_secret, kwargs)
        self.rules = None

    def on_status(self, status):
        self.rules = [status.retweeted_status.retweet_count > 10,
                      check_keyword_in_tweet(status.text),
                      status.lang == 'en']
        if all(self.rules):
            ...
        else:
            ...
