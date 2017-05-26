from flask import render_template
from flask_bootstrap import Bootstrap
from app import app
import tweepy
import urllib
from Secrets.secrets import consumer_key, consumer_secret, access_token, access_token_secret

import Analyzer.target_analyzer as analyzer

@app.route('/')
@app.route('/index')
def index():

    # Connection with twitter
    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)
    twitter_api = tweepy.API(auth, wait_on_rate_limit_notify=True,
        wait_on_rate_limit=True)

    # Saving important informations
    username_target = analyzer.get_user()
    last_tweet = analyzer.get_last_tweet(twitter_api, username_target)

    # Getting data on account
    user_info = twitter_api.get_user(screen_name=username_target)
    image_url = user_info.profile_image_url_https
    path_image_for_html = "/static/img/users_photo/"+username_target+".png"
    path_image = "app"+path_image_for_html
    urllib.urlretrieve(str(image_url), path_image)

    user = {'nickname': username_target, 'last_tweet': last_tweet, 'total_tweets':user_info.statuses_count, 'description': user_info.description, 'profile_image':path_image_for_html}  # fake user
    account_info = {'lang':user_info.lang, 'geo_enabled':user_info.geo_enabled, 'time_info':user_info.time_zone, 'utc_offset':user_info.utc_offset}
    return render_template('index.html', title='Home', user=user, account_info=account_info)
