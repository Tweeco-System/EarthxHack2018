from tweepy import Cursor
from twitter_client import get_twitter_client
from twitter_client import getAPI
import json

searchTerm = "earth"
numOfTweets = 800 
#geocode = 
#radius = 
client = get_twitter_client()
api = getAPI()
tweets = Cursor(client.search, q = searchTerm, geocode = ).items(numOfTweets)
for tweet in tweets:
    print(tweet.text)