from mpl_toolkits.basemap import Basemap
import matplotlib.pyplot as plt
import tweepy

from secrets import consumer_key, consumer_secret, access_token, access_token_secret
from authentication import authentication  # Consumer and access token/key


class TwitterStreamListener(tweepy.StreamListener):
    """ A listener handles tweets are the received from the stream.
    This is a basic listener that just prints received tweets to stdout.
    """

    def on_status(self, status):
        self.get_tweet(status)

    def on_error(self, status_code):
        if status_code == 403:
            print("The request is understood, but it has been refused or access is not allowed. Limit is maybe reached")
            return False

    @staticmethod
    def get_tweet(tweet):

        if tweet.coordinates is not None:
            x, y = map(tweet.coordinates['coordinates'][0], tweet.coordinates['coordinates'][1])
            map.plot(x, y, 'ro', markersize=2)
            plt.draw()


if __name__ == '__main__':

    # Size of the map
    fig = plt.figure(figsize=(18, 4), dpi=250)

    # Set a title
    plt.title("Tweet's around the world")

    # Declare map projection, size and resolution
    map = Basemap(projection='merc',
                  llcrnrlat=-80,
                  urcrnrlat=80,
                  llcrnrlon=-180,
                  urcrnrlon=180,
                  lat_ts=20,
                  resolution='l')

    map.bluemarble(scale=0.3)

    # Set interactive mode ON
    plt.ion()

    # Display map
    plt.show()

    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)
    twitter_api = tweepy.API(auth)

    streamListener = TwitterStreamListener()
    myStream = tweepy.Stream(auth=api.auth, listener=streamListener)

    myStream.filter(locations=[-180, -90, 180, 90], async=True)
