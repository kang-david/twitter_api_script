import tweepy
import os
from dotenv import load_dotenv


# Read from .env file.
load_dotenv()

env = os.environ.get

CONSUMER_KEY=env("TWITTER_CONSUMER_KEY")
CONSUMER_SECRET=env("TWITTER_CONSUMER_SECRET")
ACCESS_TOKEN=env("TWITTER_ACCESS_TOKEN")
ACCESS_TOKEN_SECRET=env("TWITTER_ACCESS_TOKEN_SECRET")


# Authenticate to Twitter.
auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)


# Create API object.
api = tweepy.API(auth, wait_on_rate_limit=True)


# Search for the 10 most recent tweets about Trudeau from within a 20-mile radius around the White House.
cursor = tweepy.Cursor(api.search_tweets, q="Trudeau", geocode="38.8977,-77.0365,20mi").items(10)

for i in cursor:
    print(i.text)
    print("--------------------------------------------------")
