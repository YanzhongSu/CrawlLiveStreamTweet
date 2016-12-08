import tweepy
from tweepy import OAuthHandler
 
consumer_key = 'pXs0gGTUJjCzdwMdHBgqiDNH8'
consumer_secret = 'kCxahsg9geawMJsbJZfSm5YmYGEv78skOAGe8sIg9nfiXHez3Y'
access_token = '749621508-GbFmDTD9iLvc5IYABbkbkIOKelv0uHO3kGGJlzTp'
access_secret = 'LXzsE57IIDzpBJosBZ8gmW23EgdsCvvcl82gzzvHu9Mcg'
 
auth = OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_secret)
 
api = tweepy.API(auth)
