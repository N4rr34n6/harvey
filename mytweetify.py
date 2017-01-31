import tweepy

CONSUMER_KEY = "hdyzjgfz0d57YXSzBVcJdq3DA"
CONSUMER_SECRET = "6Q1DxSMimXvbbCGkFtLD9M6cTLNLUHfwNye3HAg0nbQKYO1m81"

OAUTH_TOKEN = "66974627-XtR8BenoHqiiOugflsflpwNXIW93eY8OlOqcP5KXj"
OAUTH_TOKEN_SECRET = "QFznAX2XBxajZOmSlLnNBUbxEnFLQlPJtUlvWyAaTx7CL"

auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(OAUTH_TOKEN, OAUTH_TOKEN_SECRET)

api = tweepy.API(auth)

tweets = api.user_timeline("djurado9", count = "5")

class MyCustomStreamListener(tweepy.StreamListener):
	def on_status(self,status):
		print("User:", tweet.user.screen_name)
		print("Created:", tweet.created_at)
		print("Text:", tweet.text)

	def on_error(self,status_code):
		print("ERROR", status_code)
		return True

	def on_timeout(self):
		print("Timeout: (")
		return True

stream = tweepy.streaming.Stream(auth = auth , listener = MyCustomStreamListener())

stream.filter(follow=["tamarahueso"])


