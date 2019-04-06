"""
@author: Abhinav Khetarpal
"""
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



# Sample code, delete when not required.
text = 'I wanna be a billionaire so fucking bad.'

sentiment = analyze(text)
print(sentiment)

