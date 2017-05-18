#!/usr/bin/python -tt
# -*- coding: utf-8 -*-
import sys,os,time,tweepy
from Secrets.secrets import consumer_key, consumer_secret, access_token, access_token_secret
from Options.options import color as color
from Options.options import clear_window

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
twitter_api = tweepy.API(auth)

class CustomStreamListener(tweepy.StreamListener):

    def __init__(self,time_limit):
        self.start_time = time.time()
        self.limit = time_limit
        super(CustomStreamListener,self).__init__()

    def on_status(self, status):
        if(time.time() - self.start_time) < self.limit:
            print(">----------------------------------------------------<")
            print color.INFO + "Usuario: " + color.ENDC + color.BLUE + str(status.user.screen_name) + color.ENDC
            if(status.geo is not None):
                print color.INFO + "Geolocalizacion: " + color.ENDC + str(status.coordinates["coordinates"])
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

def main():
    clear_window()
    list_key_word=raw_input(color.GREEN + "[+] " + color.ENDC + color.INFO +  "Especifique alguna palabra/s para el filtro (separadas por comas): " + color.ENDC).split(", ")
    time.sleep(1)
    print(color.BLUE + "[+] " + color.ENDC + color.INFO + "Comenzando vigilancia digital a nivel mundial por keyword..." + color.ENDC)
    print("\n")
    #Pausa dramatica
    time.sleep(3)
    sapi = tweepy.streaming.Stream(auth, CustomStreamListener(20))
    sapi.filter(track=list_key_word)
