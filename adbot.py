#!/usr/bin/python

import os
import random
import twitter # https://github.com/bear/python-twitter
from OAuthSettings import settings

api_key = settings['api_key']
api_secret = settings['api_secret']
access_token = settings['access_token']
access_token_secret = settings['access_token_secret']

old_ads_path = 'old/'
new_ads_path = 'new/'

# Code to compose tweet from runaway ads will go here
# print tweet at end for local testing

# Open one of the ad files from an input "new" directory
new_ads = os.listdir(new_ads_path)
ad_file = random.choice(new_ads)
ad_text = open(new_ads_path + ad_file, 'r').read()

# Recompose the URL to the ad from filename metadata
ad_url_parts = ad_file.split('_')[-1].rstrip('.txt')
ad_url_parts = ad_url_parts.split('-')
ad_url = 'http://texashistory.unt.edu/ark:/' + '/'.join(ad_url_parts[0:4]) + '/zoom/?zoom=5&lat=' + ad_url_parts[4] + '&lon=' + ad_url_parts[5]

# Move ad file to archived "old" directory
os.rename(new_ads_path + ad_file, old_ads_path + ad_file)

    # Excerpt the largest number of words from the beginning of the
    # ad that ads up to no more than 117 characters (including spaces
    # and an \u2026 ellipsis and quotation marks to show that it's an excerpt)
    # Links will be shortened by Twitter API to 22 characters

    # Recompose permalink to PoTH from ad filename, setting zoom to 5

    # Put together the excerpt and the permalink and assign to `tweet` var

# print tweet

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
