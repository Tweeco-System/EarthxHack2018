import tweepy
from uszipcode import ZipcodeSearchEngine
search = ZipcodeSearchEngine()

consumer_key = "5MHvbP574EVZBZCJDIrEe0uIz"
consumer_secret = "EL0CemRUgh4FT6DJ9cCfVrQ1vPoKp54mqCtfxbPdVfD2rP3gGD"


access_token = "3388298238-9x8av1YuGTBXhOto3DaiKLBe4QI6RFfywBzZXTZ"
access_token_secret = "3O3uu1s7smQe7npGhL7utHtft5soNsl10z07eoYCBSyzR"

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)

public_tweets = api.home_timeline()
print ("test")
for tweet in public_tweets:
    print(tweet.text)



tweets = tweepy.Cursor(api.search, q='earthx', show_user="true").items(10)

for tweet in tweets:
  #  print(tweet.user.location)
    cityState = str(tweet.user.location).split(', ')
  #  print(cityState)
    if len(cityState) == 2:
        try:
            results = search.by_city_and_state(cityState[0], cityState[1])
            print(results[0].Latitude, results[0].Longitude)
        except:
            print("invalid city name", cityState)
            