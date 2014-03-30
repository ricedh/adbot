#!/usr/bin/python

import os, random
import twitter # https://github.com/bear/python-twitter
from OAuthSettings import settings

api_key = settings['api_key']
api_secret = settings['api_secret']
access_token = settings['access_token']
access_token_secret = settings['access_token_secret']

old_ads_path = 'old/'
new_ads_path = 'new/'
log_file = 'twitter.log'

# Open one of the ad files from an input "new" directory
new_ads = os.listdir(new_ads_path)
ad_file = random.choice(new_ads)
ad_text = open(new_ads_path + ad_file, 'r').read()

# Recompose the URL to the ad from filename metadata
ad_url_parts = ad_file.split('_')[-1].rstrip('.txt')
ad_url_parts = ad_url_parts.split('-')
ad_url = 'http://texashistory.unt.edu/ark:/' + '/'.join(ad_url_parts[0:4]) + '/zoom/?zoom=5&lat=' + ad_url_parts[4] + '&lon=' + ad_url_parts[5]

# Excerpt the largest number of words from the beginning of the
# ad that ads up to no more than 111 characters. 
# Links will be shortened by Twitter API to 22 characters

ad_as_list = ad_text.split()
word_count = 1
excerpt_length = 0

while excerpt_length < 111:
    excerpt = " ".join(ad_as_list[0:word_count])
    word_count = word_count + 1
    excerpt_length = len(excerpt)

while excerpt_length > 111:
    word_count = word_count - 1
    excerpt = " ".join(ad_as_list[0:word_count])
    excerpt_length = len(excerpt)

tweet = '"' + excerpt + '..." ' + ad_url

# print tweet
# print len(tweet)

# Try to post tweet to Twitter
# Comment out for local testing without posting

l = open(log_file, 'a')
try:
    api = twitter.Api(consumer_key = api_key, consumer_secret = api_secret, access_token_key = access_token, access_token_secret = access_token_secret)
    status = api.PostUpdate(tweet)
    # Move ad file to archived "old" directory
    os.rename(new_ads_path + ad_file, old_ads_path + ad_file)
except twitter.TwitterError:
    l.write('Error\t' + ad_file + '\n')
l.close()
