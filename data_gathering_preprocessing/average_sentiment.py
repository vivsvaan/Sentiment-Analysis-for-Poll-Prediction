"""
:@author: Abhinav Khetarpal
"""
import matplotlib.pyplot as plt
import pandas as pd

data_set_1 = pd.read_csv('2014_trainingSet.csv')
data_set_2 = pd.read_csv('state_wise_results_14.csv')

state_wise_sentiment_bjp = {
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

state_wise_sentiment_congress = {
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

total_sentiment = {
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

for index, row in data_set_1.iterrows():
    # Congress
    if row['party'] == 0:
        if row['sentiment'] > 0:
            state_wise_sentiment_congress[row['location']]['positive'] = state_wise_sentiment_congress[row['location']]['positive'] + 1
        elif row['sentiment'] < 0:
            state_wise_sentiment_congress[row['location']]['negative'] = state_wise_sentiment_congress[row['location']]['negative'] + 1
    
    # BJP
    if row['party'] == 1:
        if row['sentiment'] > 0:
            state_wise_sentiment_bjp[row['location']]['positive'] = state_wise_sentiment_bjp[row['location']]['positive'] + 1
        elif row['sentiment'] < 0:
            state_wise_sentiment_bjp[row['location']]['negative'] = state_wise_sentiment_bjp[row['location']]['negative'] + 1

for state in total_sentiment.keys():
    total_sentiment[state]['positive'] = state_wise_sentiment_bjp[state]['positive'] + state_wise_sentiment_congress[state]['positive']
    total_sentiment[state]['negative'] = state_wise_sentiment_bjp[state]['negative'] + state_wise_sentiment_congress[state]['negative']
    print(total_sentiment[state])
