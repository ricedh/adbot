#!/usr/bin/python

import os, random, sys
import twitter # https://github.com/bear/python-twitter
from datetime import date
from OAuthSettings import settings

api_key = settings['api_key']
api_secret = settings['api_secret']
access_token = settings['access_token']
access_token_secret = settings['access_token_secret']

old_ads_path = '/Users/wcm1/programming/ricedh/adbot/old/'
new_ads_path = '/Users/wcm1/programming/ricedh/adbot/new/'
log_file = '/Users/wcm1/programming/ricedh/adbot/twitter.log'

# Check for ads that have today's date in file name
ads = os.listdir(new_ads_path) + os.listdir(old_ads_path)
day = str(date.today())[4:].replace('-','') + '_'
otd = [ad for ad in ads if day in ad]

# Abort script if there are no ads on this day
if len(otd) == 0:
    sys.exit()

# Randomly choose a matching ad and get metadata
ad_file = random.choice(otd)
metadata = ad_file.split('_')
year = metadata[1][0:4]
cities = {'Gazette':['#Austin','#ATX'], 'Telegraph':['#Houston', '#HTown']}
city = cities[metadata[2]]

# Recompose the URL to the ad from filename metadata
ad_url_parts = ad_file.split('_')[-1].rstrip('.txt')
ad_url_parts = ad_url_parts.split('-')
ad_url = 'http://texashistory.unt.edu/ark:/' + '/'.join(ad_url_parts[0:4]) + '/zoom/?zoom=5&lat=' + ad_url_parts[4] + '&lon=' + ad_url_parts[5]

# Compose the tweet using hashtags and metadata from above.
# Links will be shortened by Twitter API to 22 characters.

tweet = '#OnThisDay in ' + year + ', this ad appeared in ' + city[0] + ' #Texas ' + ad_url + ' #OTD ' + city[1]

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
