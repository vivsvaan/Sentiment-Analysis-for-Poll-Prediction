"""
@author: Abhinav Khetarpal
"""
import search_twitter

tweet_data = search_twitter.search_for_tweets('IndianElection2014', 10, 201404011200, 201405121200).json()

texts = []

for result in tweet_data['results']:
    print(result['text'])
    texts.append(result['text'])
