import tweepy
from tweepy import Stream
from tweepy.streaming import StreamListener 
from tweepy import OAuthHandler
import json
consumer_key = "Qh6n4AzZC7qiiT4GsmPI1YRNc"
consumer_secret = "yVAzkGovZVDZXxhuOa8pdAxWlNKskraKIaaeK7TKExi7GdBpUe"
access_token = "810603802395025408-gW5zHWbwnWJ9WbiOtMuquXhNLLB4ldA"
access_secret = "B4kCA5wsaybzHBLEppwo3AwfhsnCKUWThdg9x8FFEBBnY"
 
auth = OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_secret)
 
api = tweepy.API(auth)
@classmethod
def parse(cls, api, raw):
    status = cls.first_parse(api, raw)
    setattr(status, 'json', json.dumps(raw))
    return status
 
# Status() is the data model for a tweet
tweepy.models.Status.first_parse = tweepy.models.Status.parse
tweepy.models.Status.parse = parse
class MyListener(StreamListener):
 
    def on_data(self, data):
        try:
            with open('FILENAME.json', 'a') as f:
                f.write(data)
                return True
        except BaseException as e:
            print("Error on_data: %s" % str(e))
        return True
 
    def on_error(self, status):
        print(status)
        return True
 
#Set the hashtag to be searched
twitter_stream = Stream(auth, MyListener())
twitter_stream.filter(track=['#EarthDay'])