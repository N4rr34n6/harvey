#!/usr/bin/python -tt
# -*- coding: utf-8 -*-
import sys,os,time
import tweepy
from Analizador.secrets import consumer_key, consumer_secret, access_token, access_token_secret
from Analizador.fwhibbit_analyzer import limpiar_pantalla
from Analizador.fwhibbit_analyzer import color
import stream_tweets

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
            print color.INFO + "Usuario: " + color.ENDC + str(status.user.screen_name)
            print color.INFO + "Pais: " + color.ENDC + str(status.place.country_code)
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
    limpiar_pantalla()
    print(color.FAIL + "Comenzando streaming de tweets por España..." + color.ENDC)
    #Pausa dramatica
    time.sleep(3)
    sapi = tweepy.streaming.Stream(auth, CustomStreamListener(5))
    SPAIN_GEOBOX = [-9.38,36.05,3.35,43.75]
    sapi.filter(languages=["es"], locations=SPAIN_GEOBOX)
