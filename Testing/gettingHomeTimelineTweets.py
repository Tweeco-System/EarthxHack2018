from tweepy import Cursor
from twitter_client import get_twitter_client
import json

if __name__ == '__main__':
    client = get_twitter_client()
    
    with open('home_timeline_out.json', 'w') as file:
        for page in Cursor(client.home_timeline, count = 10).pages(4):
            for status in page:
                file.write(json.dumps(status._json)+"\n")
                print(status.text)
                print()