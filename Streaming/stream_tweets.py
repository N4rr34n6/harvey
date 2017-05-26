#!/usr/bin/python -tt
# -*- coding: utf-8 -*-
import sys,os,time,tweepy
from Secrets.secrets import consumer_key, consumer_secret, access_token, access_token_secret
from Options.options import color as color
from Options.options import clear_window

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
twitter_api = tweepy.API(auth, wait_on_rate_limit_notify=True,wait_on_rate_limit=True)

class CustomStreamListener(tweepy.StreamListener):

    def __init__(self,time_limit):
        self.start_time = time.time()
        self.limit = time_limit
        super(CustomStreamListener,self).__init__()

    def on_status(self, status):
        if(time.time() - self.start_time) < self.limit:
            print(">----------------------------------------------------<")
            print color.INFO + "User: " + color.ENDC + color.BLUE + str(status.user.screen_name) + color.ENDC
            if(status.geo is not None):
                print color.INFO + "Geo-positioning: " + color.ENDC + str(status.coordinates["coordinates"])
            print status.text
            print(">----------------------------------------------------<\n")
            time.sleep(1)
            return True
        else:
            return False

    def on_error(self, status_code):
        print >> sys.stderr, 'Encountered error with status code:', status_code
        return True # Don't kill the stream

    def on_timeout(self):
        print >> sys.stderr, 'Timeout...'
        return True # Don't kill the stream

def launchStream(languages_choosen = None, locations_choosen = None, track_choosen = None):
    clear_window()
    time.sleep(1)
    print(color.BLUE + "[+] " + color.ENDC + color.INFO + "Starting digital vigilance..." + color.ENDC)
    print("\n")
    #Pausa dramatica
    time.sleep(3)
    sapi = tweepy.streaming.Stream(auth, CustomStreamListener(20))
    sapi.filter(languages = languages_choosen, locations = locations_choosen, track = track_choosen)
