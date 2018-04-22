from tweepy import Cursor
from twitter_client import get_twitter_client
from twitter_client import getAPI
import json
from textblob import TextBlob

blacklistFile = open("wordsToAvoid.txt", 'r')
wordsToAvoid = blacklistFile.readlines()
blacklistFile.close()

def wordsNotInStr(wordsList, s):
    for word in wordsList:
        if word in s:
            return False
    return True

searchTermsFile = open("searchTerms.txt", "r")
searchTerms = []

for line in searchTermsFile:
    searchTerms+= [line.rstrip()]
    
tweetsList = []

numOfTweets = 100
#code = 
#rad = 
client = get_twitter_client()
api = getAPI()
for word in searchTerms:   
    tweets = Cursor(client.search, q = word, lang = 'en').items(numOfTweets)
    for tweet in tweets:
        if (TextBlob(tweet.text).polarity < .5):
            if tweet not in tweetsList:
                if wordsNotInStr(wordsToAvoid, tweet.text):
                    tweetsList += [[tweet.text, tweet.user.location]]
        
for item in tweetsList:
    print(item[0])
    print(item[1])
    print()