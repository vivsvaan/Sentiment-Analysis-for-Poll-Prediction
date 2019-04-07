"""
@author: Abhinav Khetarpal, Vivsvaan Sharma
"""
import numpy as np
import pandas as pd
import csv
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer


def analyze(tweet):
    """
    Takes text to be analyzed as input
    :return: a dictionary with the scores for sentiments - pos, neg, neu, compound
    """
    analyzer = SentimentIntensityAnalyzer()
    
    sentiment = analyzer.polarity_scores(tweet)

    return sentiment

 
#input from cleaned_data_2019.csv files    
dataset = pd.read_csv('cleaned_data_2019.csv')
hashtags = dataset.iloc[:, 0].values
X = dataset.iloc[:, 1].values #don't reshape array X
all_tweets = list(X) #changing numpy array to list

hashtags = list(hashtags)
neg = ["neg"]
neu = ["neu"]
pos = ["pos"]
compound = ["compound"]


for i in range(0,len(all_tweets)):
    tweet = all_tweets[i]  #accessing content of list all_tweets one by one
    sentiment = analyze(tweet)
    #adding all values in their respective lists
    neg.append(sentiment['neg'])
    neu.append(sentiment['neu'])
    pos.append(sentiment['pos'])
    compound.append(sentiment['compound'])

#Storing sentiment values along with hashtags and tweets in sentiment_data_2019.csv file
hashtags[:] = ["hashtags"] + hashtags[:]
all_tweets[:] = ["tweets"] + all_tweets[:]
with open('sentiment_data_2019.csv', 'a',encoding="utf-8", newline='') as outfile:
    rowlists = zip(hashtags,all_tweets, neg, neu, pos, compound)
    spamwriter = csv.writer(outfile)
    for row in rowlists:
          spamwriter.writerow(row)

