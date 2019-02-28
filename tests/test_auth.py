import tweepy
import unittest
from twentiment import auth


class AuthTest(unittest.TestCase):
    @unittest.skipIf(not auth.secrets, 'This test is skipped if secrets module exists.')
    def test_authenticate_with_secrets(self):
        if auth.secrets:
            handler = auth.authenticate()
            self.assertIsInstance(handler, tweepy.OAuthHandler)

    @unittest.skipIf(auth.secrets, 'This test is skipped if secrets module does not exist.')
    def test_authenticate_no_secrets(self):
        with self.assertRaises(auth.AuthenticationError):
            auth.authenticate()