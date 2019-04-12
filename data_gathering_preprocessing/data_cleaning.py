"""
@author: Vivsvaan Sharma
"""
import string
import pandas as pd
import numpy as np
import csv
import nltk
nltk.download('stopwords')
from nltk.corpus import stopwords

def text_cleaning(text):
    '''It removes punctuations and stopwords'''
    nopunc = [char for char in text if char not in string.punctuation]
    nopunc = ''.join(nopunc)
    
    return [word for word in nopunc.split() if word.lower() not in stopwords.words('english')]


dataset = pd.read_csv('2014_new_congress.csv')

#fetching data from csv file
hashtags = dataset.iloc[:,0].values
dates= dataset.iloc[:,1].values
tweets = dataset.iloc[:,2].values
location = dataset.iloc[:,3].values
followers= dataset.iloc[:,4].values
fav = dataset.iloc[:,5].values
reply = dataset.iloc[:,6].values
retweet = dataset.iloc[:,7].values

#converting nparray to lists
hashtags = list(hashtags)
dates = list(dates)
tweets = list(tweets)
location = list(location)
followers = list(followers)
fav = list(fav)
reply = list(reply)
retweet = list(retweet)
cleaned_tweets = []

#cleaning tweets
for text in tweets:
    cleaned_text = text_cleaning(text)
    cleaned_text = " ".join(cleaned_text)
    cleaned_tweets.append(cleaned_text)

#adding headings
hashtags = ['hashtags'] + hashtags
dates = ['dates'] + dates
cleaned_tweets = ['cleaned_tweets'] + cleaned_tweets
location = ['location'] + location
followers = ['followers'] + followers
fav = ['fav'] + fav
reply = ['reply'] + reply
retweet = ['retweet'] + retweet

#storing in csv file
with open('2014_new_congress_cleaned.csv', 'a',encoding="utf-8", newline='') as outfile:
    rowlists = zip(hashtags,dates,cleaned_tweets,location,followers,fav,reply,retweet)
    spamwriter = csv.writer(outfile)
    for row in rowlists:
          spamwriter.writerow(row)

