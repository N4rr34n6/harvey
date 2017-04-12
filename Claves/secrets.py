# Go to http://dev.twitter.com and create an app.
# The consumer key and secret will be generated for you after
# After the step above, you will be redirected to your app's page.
# Create an access token under the the "Your access token" section
import os
consumer_key = os.environ['CONSUMER_KEY']
consumer_secret = os.environ['CONSUMER_SECRET']
access_token = os.environ['ACCESS_TOKEN']
access_token_secret = os.environ['ACCESS_TOKEN_SECRET']
