from flask import render_template
from flask_bootstrap import Bootstrap
from app import app
import tweepy
import urllib
from Secrets.secrets import consumer_key, consumer_secret, access_token, access_token_secret
import Analyzer.target_analyzer as target_analyzer

@app.route('/')
@app.route('/index')
def index():

    limite_tweets = 500
    # Connection with twitter
    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)
    twitter_api = tweepy.API(auth, wait_on_rate_limit_notify=True,
        wait_on_rate_limit=True)

    # Saving important informations
    username_target = target_analyzer.get_user()
    last_tweet = target_analyzer.get_last_tweet(twitter_api, username_target)

    # Getting data on account

    # -- Profile picture
    user_info = twitter_api.get_user(screen_name=username_target)
    image_url = user_info.profile_image_url_https
    path_image_for_html = "/static/img/users_photo/"+username_target+".png"
    path_image = "app"+path_image_for_html
    urllib.urlretrieve(str(image_url), path_image)

    # -- Banner picture
    banner_url = user_info.profile_banner_url
    path_banner_for_html = "/static/img/users_photo/"+username_target+"BANNER.png"
    path_banner = "app"+path_banner_for_html
    urllib.urlretrieve(str(banner_url), path_banner)

    # -- Account date created
    date_created = user_info.created_at
    favorites_count = user_info.favourites_count
    followers_count = user_info.followers_count
    friends_count = user_info.friends_count
    list_member = user_info.listed_count
    location = user_info.location
    sms_notifications = user_info.notifications

    # -- From analyzer
    #list_tweets = target_analyzer.get_tweets(twitter_api, username_target, limit=limite_tweets)

    user = {'nickname': username_target, 'last_tweet': last_tweet,
    'total_tweets':user_info.statuses_count, 'description': user_info.description,
    'profile_image':path_image_for_html,'banner_image':path_banner_for_html,
    'date_created':date_created, 'favorites_count':favorites_count,
    'followers_count':followers_count,'friends_count': friends_count,
    'list_member':list_member,'location':location,'sms_notifications':sms_notifications}

    account_info = {'lang':user_info.lang, 'geo_enabled':user_info.geo_enabled, 'time_info':user_info.time_zone, 'utc_offset':user_info.utc_offset}

    #tweet_info = {'list_tweets':list_tweets}

    return render_template('index.html', title='Home', user=user, account_info=account_info) #tweet_info = tweet_info)
