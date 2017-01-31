#!/usr/bin/python -tt
# -*- coding: utf-8 -*-
import sys,os,time
import tweepy
from Analizador.secrets import consumer_key, consumer_secret, access_token, access_token_secret
from Analizador.fwhibbit_analyzer import limpiar_pantalla
from Analizador.fwhibbit_analyzer import color

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
twitter_api = tweepy.API(auth)

class CustomStreamListener(tweepy.StreamListener):
    def on_status(self, status):
        print(">----------------------------------------------------<")
        print color.INFO + "Usuario: " + color.ENDC + str(status.user.screen_name)
        if(status.geo is not None):
            print color.INFO + "Geolocalizacion: " + color.ENDC + str(status.coordinates["coordinates"])
        print status.text
        print(">----------------------------------------------------<\n")
        time.sleep(1)

    def on_error(self, status_code):
        print >> sys.stderr, 'Encountered error with status code:', status_code
        return True # Don't kill the stream

    def on_timeout(self):
        print >> sys.stderr, 'Timeout...'
        return True # Don't kill the stream

def main():
    sapi = tweepy.streaming.Stream(auth, CustomStreamListener())
    #sapi.filter(locations=[-180,-90,180,90]))
    limpiar_pantalla()

    list_key_word=raw_input("Especifique alguna palabra/s para el filtro (separadas por comas): ").split(", ")

    print(color.FAIL + "Comenzando streaming de tweets por parametros..." + color.ENDC)
    #Pausa dramatica
    time.sleep(3)

    sapi.filter(track=list_key_word)
