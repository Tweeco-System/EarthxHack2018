from tweepy import Cursor
from twitter_client import get_twitter_client
from twitter_client import getAPI
import json

searchTerm = ["earth", "nature", "water"]
numOfTweets = 800 
#code = 
#rad = 
client = get_twitter_client()
api = getAPI()
tweets = Cursor(client.search, q = searchTerm).items(numOfTweets)
for tweet in tweets:
    print(tweet.text)