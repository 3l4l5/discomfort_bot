import tweepy

class TwitterSenderClass:
    def __init__(self, text, consumer_key, consumer_secret, access_token, access_token_secret):
        self.text = text
        self.consumer_key = consumer_key
        self.consumer_secret = consumer_secret
        self.access_token = access_token
        self.access_token_secret = access_token_secret
        pass
    def push(self):
        # Twitterオブジェクトの生成
        auth = tweepy.OAuthHandler(self.consumer_key, self.consumer_secret)
        auth.set_access_token(self.access_token, self.access_token_secret)
        api = tweepy.API(auth)
        #-------------------------------------------------------------------------
        # ツイートを投稿
        api.update_status(self.text)
