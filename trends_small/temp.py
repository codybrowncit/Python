from trends import *

sf = make_tweet("Welcome to San Francisco", None, 38, -122)
ny = make_tweet("Welcome to New York", None, 41, -74)
ca_tweets = group_tweets_by_state([sf, ny])['CA']
tweet_string(ca_tweets[0])

