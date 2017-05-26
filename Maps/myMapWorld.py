#!/usr/bin/python
# -*- coding: utf-8 -*-
import time, os, tweepy
from Secrets.secrets import consumer_key, consumer_secret, access_token, access_token_secret
from Options.options import color as color
from Options.options import clear_window
from Options.options import deleteContent
from Maps import maps

coords_list=[]
user_list=[]

class TwitterStreamListener(tweepy.StreamListener):
    """ A listener handles tweets are the received from the stream.
    This is a basic listener that just prints received tweets to stdout.
    """

    def __init__(self,time_limit):
        self.start_time = time.time()
        self.limit = time_limit
        super(TwitterStreamListener,self).__init__()

    def on_status(self, status):
        if(time.time() - self.start_time) < self.limit:
            print(">----------------------------------------------------<")
            print color.INFO + "Usuario: " + color.ENDC + str(status.user.screen_name)
            if(status.geo is not None):
                user_list.append(status.user.screen_name)
                print color.INFO + "Geolocalizacion: " + color.ENDC + str(status.coordinates["coordinates"])
            print status.text
            print(">----------------------------------------------------<\n")
            time.sleep(0.5)
            self.get_tweet(status)
            return True
        else:
            return False

    def on_error(self, status_code):
        if status_code == 403:
            print("The request is understood, but it has been refused or access is not allowed. Limit is maybe reached")
            return False

    @staticmethod
    def get_tweet(tweet):
        if tweet.coordinates is not None:
            x = tweet.coordinates['coordinates'][0]
            y = tweet.coordinates['coordinates'][1]
            coords_list.append((x,y))


def StreamingMap(coords):
    clear_window()
    print(color.BLUE + "[+] " + color.ENDC + color.INFO + "Starting tweet streaming..." + color.ENDC)
    time.sleep(1)
    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)
    twitter_api = tweepy.API(auth, wait_on_rate_limit_notify=True,
        wait_on_rate_limit=True, retry_count=10, retry_delay=5,retry_errors=5)

    streamListener = TwitterStreamListener(300)
    myStream = tweepy.streaming.Stream(auth, streamListener)
    myStream.filter(locations=coords)

    print(color.BLUE + "[+] " + color.ENDC + color.INFO + "Generating map..." + color.ENDC)

    outfile = open('Maps/coordenadas.txt', 'w') # Write file
    deleteContent(outfile) # Delete everything inside
    outfile.write('NAME,LAT,LON\n')

    j=0 #To control name of users
    for i in coords_list:
        x = i[1]
        y = i[0]
        outfile.write("@"+user_list[j]+",")
        #'<a href="{link}">{text}</a>'
        #outfile.write("'<a href='www.twitter.com/"+user_list[j]+"'>" + "@" + user_list[j] + "</a>'"+ ",")
        outfile.write(str(x)+",")
        outfile.write(str(y)+"\n")
        j = j+1


    outfile.close()
    maps.mapaLeaflet()
