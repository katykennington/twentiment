"""
api
"""


import tweepy
from twentiment import auth

def get_api():
    handler = auth.authenticate()
    api = tweepy.API(handler)
    return api


def get_home_tweets():
    api = get_api()
    return api.home_timeline()