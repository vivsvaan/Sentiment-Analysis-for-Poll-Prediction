# """
# @author: Abhinav Khetarpal
# """
# import search_twitter

# tweet_data = search_twitter.search_for_tweets('IndianElection2014', 10, 201404011200, 201405121200).json()

# texts = []

# for result in tweet_data['results']:
#     print(result['text'])
#     texts.append(result['text'])

 
import csv

text = ['text', ' ']
comp = ['comp', ' ']
pos = ['pos', ' ']
neg = ['neg', ' ']
neut = ['neutral', ' ']

for _ in range(10):
    text.append("ab")



with open('data.csv', 'w', newline='') as outfile:
    rowlists = zip(text, comp, pos, neg, neut)
    spamwriter = csv.writer(outfile)
    for row in rowlists:
        spamwriter.writerow(row)
