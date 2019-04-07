"""
@author: Abhinav Khetarpal
"""
import numpy as np
import pandas as pd
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer

# TODO: For each tweet text in the collection, add the values for - pos, neg, neu, compound under appropriate attribute in table.

# import this file and then use in your code.
def analyze(text):
    """
    Takes text to be analyzed as input
    :return: a dictionary with the scores for sentiments - pos, neg, neu, compound
    """
    analyzer = SentimentIntensityAnalyzer()
    
    sentiment = analyzer.polarity_scores(text)

    return sentiment

 
#input from data_new.csv files    
dataset = pd.read_csv('data_new.csv')
X = dataset.iloc[:, 1:2].values #input tweets in form of numpy ndarray
text = X.tolist() #changing numpy ndarray to list
l = len(text)

sentiment_list = []  #list to store sentiment analysis result for all tweets

for i in range(0,l):
    temp = text[i][0]  #accessing content of list text one by one
    sentiment = analyze(temp)
    sentiment_list.append(sentiment)  #storing result of sentiment analysis in sentiment_list


#name of the variables can be changed according to convinience
#Store the Conent of sentiment_list in excel or csv


