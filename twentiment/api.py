"""Twitter API wrapper - low-level
"""


import tweepy
from twentiment import secrets


def authenticate() -> tweepy.OAuthHandler:
    auth = tweepy.OAuthHandler(secrets.CONSUMER_API_KEY, secrets.CONSUMER_API_SECRET)
    auth.set_access_token(secrets.TWENTIMENT_ACCESS_TOKEN, secrets.TWENTIMENT_ACCESS_SECRET)
    return auth


def get_api():
    auth = authenticate()
    api = tweepy.API(auth)
    return api


def get_home_tweets():
    api = get_api()
    return api.home_timeline()


