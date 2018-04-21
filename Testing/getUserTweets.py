import json
from tweepy import Cursor
from twitter_client import get_twitter_client

if __name__ == '__main__':
    user = "nerdia_nadia"
    client = get_twitter_client()
    
    fname = "user_timeline_{}.jsonl".format(user)
    
    with open(fname,'w') as file:
        for page in Cursor(client.user_timeline, screen_name = user, count = 10).pages(4):
            for status in page:
                file.write(json.dumps(status._json)+"\n")
                print(status.text)