from tweepy import Cursor
from twitter_client import get_twitter_client
from twitter_client import getAPI
import json
from textblob import TextBlob

def getSearchDataFunc(num):
    blacklistFile = open("wordsToAvoid.txt", 'r')
    wordsToAvoid = []
    for line in blacklistFile:
        wordsToAvoid += [line.rstrip('\n')]
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
    searchTermsFile.close() 
    tweetsList = []
    
    
    numOfTweets = num
    #code = 
    #rad = 
    client = get_twitter_client()
    api = getAPI()
    for word in searchTerms:   
        tweets = Cursor(client.search, q = word, lang = 'en').items(numOfTweets)
        for tweet in tweets:
            if (TextBlob(tweet.text).polarity < .1):
                if tweet not in tweetsList:
                    if wordsNotInStr(wordsToAvoid, tweet.text):
                        tweetsList += [[tweet.text, tweet.user.location]]
    '''
    for tweet in tweetsList:
        print(tweet[0])
        print(tweet[1])
        print()
    '''        
    data = {}
    data['tweets'] = []
    
    
    for tweet in tweetsList:
        data['tweets'].append({
            'text': tweet[0],
            'location' : tweet[1]
        })
    
        
    with open('OUTPUTgetSearchData.json', 'w') as outfile:
        json.dump(data, outfile)
    
'''
blacklistFile = open("wordsToAvoid.txt", 'r')
wordsToAvoid = []
for line in blacklistFile:
    wordsToAvoid += [line.rstrip('\n')]
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
searchTermsFile.close() 
tweetsList = []


numOfTweets = 10
#code = 
#rad = 
client = get_twitter_client()
api = getAPI()
for word in searchTerms:   
    tweets = Cursor(client.search, q = word, lang = 'en').items(numOfTweets)
    for tweet in tweets:
        if (TextBlob(tweet.text).polarity < .1):
            if tweet not in tweetsList:
                if wordsNotInStr(wordsToAvoid, tweet.text):
                    tweetsList += [[tweet.text, tweet.user.location]]

for tweet in tweetsList:
    print(tweet[0])
    print(tweet[1])
    print()
        
data = {}
data['tweets'] = []


for tweet in tweetsList:
    data['tweets'].append({
        'text': tweet[0],
        'location' : tweet[1]
    })

    
with open('OUTPUTgetSearchData.json', 'w') as outfile:
    json.dump(data, outfile)

'''