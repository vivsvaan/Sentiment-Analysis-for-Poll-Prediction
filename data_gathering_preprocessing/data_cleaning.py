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


dataset = pd.read_csv('data_2019.csv')
hashtags = dataset.iloc[:,0].values
X = dataset.iloc[:, 1].values
#X = X.reshape((X.shape[0], 1))
hashs = list(hashtags)
tweets = list(X)
cleaned_tweets = []

for text in tweets:
    cleaned_text = text_cleaning(text)
    cleaned_text = " ".join(cleaned_text)
    cleaned_tweets.append(cleaned_text)

with open('cleaned_data_2019.csv', 'a',encoding="utf-8", newline='') as outfile:
    rowlists = zip(hashs,cleaned_tweets)
    spamwriter = csv.writer(outfile)
    for row in rowlists:
          spamwriter.writerow(row)

