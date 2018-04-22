import os
import sys
from tweepy import API
from tweepy import OAuthHandler
from tweepy import Cursor

def get_twitter_auth():
    ''' set up twitter authentication
    return: tweety.OAuthHandler object 
    
    responsible for authenticating 
    
    '''
    file = open("keys.txt","r")
    consumer_key = file.readline().rstrip('\n')
    consumer_secret = file.readline().rstrip('\n')
    access_token = file.readline().rstrip('\n')
    access_secret = file.readline().rstrip('\n')
    file.close()
    auth = OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_secret)
    return auth

def get_twitter_client():
    auth = get_twitter_auth()
    client = API(auth)
    return client

def getAPI():
    return API(get_twitter_auth())