import tweepy
import pandas as pd
import nltk
from nltk.sentiment.vader import SentimentIntensityAnalyzer
from IPython.display import display

#authentication of twitter API

consumer_key = 'xxxxxxxxxxxxxxxxxxxxx'
consumer_secret = 'xxxxxxxxxxxxxxxxxxxxx'
access_token = 'xxxxxxxxxxxxxxxxxxxxx'
access_token_secret = 'xxxxxxxxxxxxxxxxxxxxx'

auth = tweepy.OAuthHandler(consumer_key,consumer_secret)
auth.set_access_token(access_token,access_token_secret)

api = tweepy.API(auth)

#getting Tweets from the tweeter 
tweets = api.search('Twitter_keyword', count=200)

#creating Dataframes of the result
data =  pd.DataFrame(data=[tweet.text for tweet in tweets], columns=['Tweets'])

#displaying tweets from data frame
display(data.head(10))

#creating object of SentimentIntensityAnalyzer
sid = SentimentIntensityAnalyzer()

#empty list to add polarity score
list = []

for index, row in data.iterrows():
    ss = sid.polarity_scores(row["Tweets"])
    list.append(ss)

#adding polarity to new column named "polarity"
se = pd.Series(list)
data['polarity'] = se.values

display(data.head(100))
