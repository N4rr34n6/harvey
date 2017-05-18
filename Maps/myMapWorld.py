from mpl_toolkits.basemap import Basemap
import matplotlib.pyplot as plt
import time, os, tweepy
from Secrets.secrets import consumer_key, consumer_secret, access_token, access_token_secret
from Options.options import color as color
from Options.options import clear_window

lista_coordenadas=[]

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
            lista_coordenadas.append((x,y))


def main():
    clear_window()
    print(color.BLUE + "[+] " + color.ENDC + color.INFO + "Comenzando streaming de tweets en el mundo..." + color.ENDC)
    time.sleep(1)
    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)
    twitter_api = tweepy.API(auth,retry_count=10, retry_delay=5,retry_errors=5)

    streamListener = TwitterStreamListener(400)
    myStream = tweepy.streaming.Stream(auth, streamListener)
    myStream.filter(locations=[-180, -90, 180, 90])

    # Size of the map
    fig = plt.figure(figsize=(18, 4), dpi=250)

    # Set a title
    plt.title("Geoposicionamiento Mundial")

    m = Basemap(projection='merc', lat_0=50, lon_0=-100,
                         resolution = 'h', area_thresh = 5000.0,
                         llcrnrlon=-140, llcrnrlat=-55,
                         urcrnrlon=160, urcrnrlat=70)

    # draw elements onto the world map
    #m.drawcountries()
    #my_map.drawstates()
    #m.drawcoastlines(antialiased=False,linewidth=0.005)
    m.bluemarble(scale=0.3)

    print(color.BLUE + "[+] " + color.ENDC + color.INFO + "Generando mapa para geoposicionamiento mundial..." + color.ENDC)
    for i in lista_coordenadas:
        x = i[0]
        y = i[1]
        # convert to map projection coords.
        # Note that lon,lat can be scalars, lists or numpy arrays.
        xpt,ypt = m(x,y)
        # convert back to lat/lon
        lonpt, latpt = m(xpt,ypt,inverse=True)
        m.plot(xpt,ypt, 'ro', markersize=3, alpha=0.5)

    plt.show()
