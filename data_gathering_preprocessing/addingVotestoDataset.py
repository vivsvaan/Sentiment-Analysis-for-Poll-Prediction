import pandas as pd
import csv

dataset = pd.read_csv('state_wise_results_14.csv')
state_names = dataset.iloc[1:,0].values
party_names = dataset.iloc[1:,2].values
polled_state = dataset.iloc[1:,3].values
polled_party = dataset.iloc[1:,6].values

state_names = list(state_names)
party_names = list(party_names)
polled_state = list(polled_state)
polled_party = list(polled_party)

dataset2 = pd.read_csv('2014_bjp_sentiment.csv')
location = dataset2.iloc[:,0]
location = list(location)
party = []
state = []
poll_state = []
poll_party = []
for i in range(len(party_names)):
    if party_names[i] == 'Bharatiya Janata Party':
        party.append(str(1))
        state.append(state_names[i])
        poll_state.append(polled_state[i])
        poll_party.append(polled_party[i])
    elif party_names[i] == 'Indian National Congress':
        state.append(state_names[i])
        party.append(str(0))
        poll_state.append(polled_state[i])
        poll_party.append(polled_party[i])
        
for i in range(len(state)):
    temp = str(state[i]) + str(party[i])
    state[i] = temp
    

location3 = dataset2.iloc[1:,0].values
party3 = dataset2.iloc[1:,1].values
followers3 = dataset2.iloc[1:,2].values
sentiment3 = dataset2.iloc[1:,3].values
location3 = list(location3)
party3 = list(party3)
followers3 = list(followers3)
sentiment3 = list(sentiment3)
poll_state3 = []
poll_party3 = []

for i in range(len(location3)):
    temp = str(location3[i]) + str(party3[i])
    index = state.index(temp)
    poll_state3.append(str(poll_state[index]))
    poll_party3.append(str(poll_party[index]))

location3[:] = ["location"] + location3[:]
party3[:] = ["party"] + party3[:]
followers3[:] = ["followers"] + followers3[:]
sentiment3[:] = ["sentiment"] + sentiment3[:]
poll_state3[:] = ["Total Valid Votes Polled in the State"] + poll_state3[:]
poll_party3[:] = ["TOTAL VALID VOTES POLLED BY PARTY"] + poll_party3

with open('2014_bjp_trainingSet.csv', 'a') as outfile:
    rowlists = zip(location3,party3,followers3,sentiment3,poll_state3,poll_party3)
    spamwriter = csv.writer(outfile)
    for row in rowlists:
        spamwriter.writerow(row)
        
        
    
    