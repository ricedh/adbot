#!/usr/bin/python

import twitter # https://github.com/bear/python-twitter
from OAuthSettings import settings

api_key = settings['api_key']
api_secret = settings['api_secret']
access_token = settings['access_token']
access_token_secret = settings['access_token_secret']

# Code to compose tweet from runaway ads will go here
# print tweet at end for local testing

tweet = 'Stay tuned for more!'
print tweet



# Try to post tweet variable to Twitter
# Commented out for local testing without posting
# try:
#     api = twitter.Api(consumer_key = api_key,
#     consumer_secret = api_secret,
#     access_token_key = access_token,
#     access_token_secret = access_token_secret)
# 
#     status = api.PostUpdate(tweet)
#     print ' post successful!'
# except twitter.TwitterError:
#     print ' error posting!'
