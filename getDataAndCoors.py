from tweepy import Cursor
from twitter_client import get_twitter_client
from twitter_client import getAPI
import json
from textblob import TextBlob
import json
from geopy.geocoders import Nominatim
geolocator = Nominatim()

from getSearchData import getSearchDataFunc
from getTXTlocations import getCoorsFunc

#print("inside geo data and cors")
getSearchDataFunc(300)
getCoorsFunc()