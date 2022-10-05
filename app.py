import streamlit as st
import snscrape.modules.twitter as sntwitter 
import tweepy
import pandas as pd

consumerKey = "GIRhmCFPghzUU0lZTybf1AUCU"
consumerSecret = "vhp8MmfU2mjujSq46dkZFd8hHTbjXz6tJbhxP7hi4oQ9X1nEFo"
accessToken = "1252990856757460992-XUs2RSRrHgGnGpMsNIUZlhV5HXmwo4"
accessTokenSecret = "ND4VznKEPcGn9dP80cS6R3ysxvxAov6VsAocwLKde7qkh"

# Create Authentication Object
authenticate = tweepy.OAuthHandler(consumerKey,consumerSecret)
# set the access token and access token secret
authenticate.set_access_token(accessToken,accessTokenSecret)
# Create the API object while passing in the auth information
api = tweepy.API(authenticate)

st.title("Tweet Analyzer 😊")
st.markdown("Welcome to Twitter Sentiment Analyzer. Here you get to fetch live tweets from Twitter Hastags.")
st.write("1. Enter the keyword in Query field for which you wanna fetch tweets of")
st.write("2. In limit field, enter the number of tweets you wish to fetch.")
st.write("3. The app will sort the tweets based on their weights.")

twitter_user = st.text_input("Query:")
limit_of_tweets = st.text_input("How many recent Tweets you want to fetch?")
button = st.button("Fetch")

if button:
    st.success("Fetching the recent %d Tweets by the user, please wait..."%(int(limit_of_tweets)))
    query = twitter_user #"#Halloween" #Fetching Tweets related to Halloween as its Halloween season
    tweets = []
    limit = int(limit_of_tweets) # Fetching 2000 tweets


    for tweet in sntwitter.TwitterSearchScraper(query).get_items():
        if len(tweets) == limit:
            break
    else:
        tweets.append([tweet.date, tweet.username, tweet.content])
        
    df = pd.DataFrame(tweets, columns=['Date', 'User', 'Tweet'])
    st.write(df.head())