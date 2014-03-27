#!/usr/bin/python

import twitter # https://github.com/bear/python-twitter
from OAuthSettings import settings

api_key = settings['api_key']
api_secret = settings['api_secret']
access_token = settings['access_token']
access_token_secret = settings['access_token_secret']

# Code to compose tweet from runaway ads will go here
# print tweet at end for local testing

    # Get one of the ad files from an input "new" directory.
	# Move file to "old" directory so next pass won't tweet it.

    # Excerpt the largest number of words from the beginning of the
    # ad that ads up to no more than 117 characters (including spaces
	# and an ellipsis and quotation marks to indicate that it's an excerpt)
    # Links will be shortened by Twitter API to 22 characters

	# Recompose permalink to PoTH from ad filename, setting zoom to 5

	# Put together the excerpt and the permalink and assign to `tweet` var

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
