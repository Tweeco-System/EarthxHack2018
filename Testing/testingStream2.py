import os
import sys
from tweepy import API
from tweepy import OAuthHandler

def get_twitter_auth():
    ''' set up twitter authentication
    return: tweety.OAuthHandler object '''
    file = open("keys.txt","r")
    consumer_key = file.readline().rstrip('\n')
    consumer_secret = file.readline().rstrip('\n')
    access_token = file.readline().rstrip('\n')
    access_secret = file.readline().rstrip('\n')
    file.close()
    auth = OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_secret)
    