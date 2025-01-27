"""
:@author: Abhinav Khetarpal
"""
import pandas as pd
import numpy as np
from textblob import TextBlob
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer

state_wise_sentiment = {
    'Andhra Pradesh':               {'positive': 0, 'negative': 0},
    'Arunachal Pradesh':            {'positive': 0, 'negative': 0},
    'Assam':                        {'positive': 0, 'negative': 0},
    'Bihar':                        {'positive': 0, 'negative': 0},
    'Chhattisgarh':                 {'positive': 0, 'negative': 0},
    'Goa':                          {'positive': 0, 'negative': 0},
    'Gujarat':                      {'positive': 0, 'negative': 0},
    'Haryana':                      {'positive': 0, 'negative': 0},
    'Himachal Pradesh':             {'positive': 0, 'negative': 0},
    'Jammu & Kashmir':              {'positive': 0, 'negative': 0},
    'Jharkhand':                    {'positive': 0, 'negative': 0},
    'Karnataka':                    {'positive': 0, 'negative': 0},
    'Kerala':                       {'positive': 0, 'negative': 0},
    'Madhya Pradesh':               {'positive': 0, 'negative': 0},
    'Maharashtra':                  {'positive': 0, 'negative': 0},
    'Manipur':                      {'positive': 0, 'negative': 0},
    'Meghalaya':                    {'positive': 0, 'negative': 0},
    'Mizoram':                      {'positive': 0, 'negative': 0},
    'Nagaland':                     {'positive': 0, 'negative': 0},
    'Odisha':                       {'positive': 0, 'negative': 0},
    'Punjab':                       {'positive': 0, 'negative': 0},
    'Rajasthan':                    {'positive': 0, 'negative': 0},
    'Sikkim':                       {'positive': 0, 'negative': 0},
    'Tamil Nadu':                   {'positive': 0, 'negative': 0},
    'Tripura':                      {'positive': 0, 'negative': 0},
    'Uttar Pradesh':                {'positive': 0, 'negative': 0},
    'Uttarakhand':                  {'positive': 0, 'negative': 0},
    'West Bengal':                  {'positive': 0, 'negative': 0},
    'Andaman & Nicobar Islands':    {'positive': 0, 'negative': 0},
    'Chandigarh':                   {'positive': 0, 'negative': 0},
    'Dadra & Nagar Haveli':         {'positive': 0, 'negative': 0},
    'Daman & Diu':                  {'positive': 0, 'negative': 0},
    'Lakshadweep':                  {'positive': 0, 'negative': 0},
    'NCT OF Delhi':                 {'positive': 0, 'negative': 0},
    'Puducherry':                   {'positive': 0, 'negative': 0}
}

# read csv file here
data_set = pd.read_csv('dummy.csv')

# Insertname of Party Here
name_of_party = ''

list_of_analysis = []
analyzer = SentimentIntensityAnalyzer()

for index, row in data_set.iterrows():

    #sentiment analyze the text of the row
     
    # tweet = TextBlob(row['tweets'])

    # polarity, subjectivity = tweet.sentiment

    # if polarity > 0.1:
    #     state_wise_sentiment[row['location']]['positive'] = state_wise_sentiment[row['location']]['positive'] + 1
    # elif polarity < -0.1:
    #     state_wise_sentiment[row['location']]['negative'] = state_wise_sentiment[row['location']]['negative'] + 1

    tweet = analyzer.polarity_scores(row['tweets'])
    
    if not tweet['neg'] > 0.1:
        if tweet['pos'] - tweet['neg'] > 0:
            state_wise_sentiment[row['location']]['positive'] = state_wise_sentiment[row['location']]['positive'] + 1
            list_of_analysis.append([row['location'], name_of_party, row['followers'], tweet['pos'] - tweet['neg']])
    
    elif not tweet['pos'] > 0.1:
        if tweet['pos'] - tweet['neg'] <= 0:
            state_wise_sentiment[row['location']]['negative'] = state_wise_sentiment[row['location']]['negative'] + 1
            list_of_analysis.append([row['location'], name_of_party, row['followers'], tweet['pos'] - tweet['neg']])

# for state, sentiment in state_wise_sentiment.items():
#     print(state, sentiment, sep='  ')

for row in list_of_analysis:
    print(row)
