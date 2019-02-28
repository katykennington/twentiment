"""
This module is about authentication
"""


import tweepy
try:
    from twentiment import secrets
except ImportError:
    secrets = None


class AuthenticationError(ValueError):
    pass


def authenticate(consumer_key=None, consumer_secret=None, access_token=None, access_secret=None) -> tweepy.OAuthHandler:
    if secrets:
        consumer_key, consumer_secret = secrets.CONSUMER_API_KEY, secrets.CONSUMER_API_SECRET
        access_token, access_secret = secrets.TWENTIMENT_ACCESS_TOKEN, secrets.TWENTIMENT_ACCESS_SECRET

    if any(x is None for x in (consumer_key, consumer_secret, access_token, access_secret)):
        raise AuthenticationError('Must either use secrets module or specify authentication parameters.')

    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_secret)
    return auth