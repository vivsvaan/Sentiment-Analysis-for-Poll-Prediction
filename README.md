# Sentiment Analysis of Twitter Data for Poll Prediction
Based on data from Twitter, we predict the results of the 2019 Lok Sabha Elections.

## Steps



#### Data Collection
The Twitter Developer platform's Search API was used to collect the tweets. The tweets had to be originated from Indian citizens located within India. Twitter data for two parties - namely BJP (Bharatiya Janata Party) and Congress (Indian National Congress) were collected.

#### Data Processing
The collected raw data was transformed into an understandable format, and stored in CSV files. It included the following steps:
- Data Cleaning - This process included filling in missing
values, smoothing the noisy data (all the tweets were stripped
off special characters like ‘@’ and URLs to overcome noise),
resolving inconsistencies in data.
- Data Integration - Data with different representation are
put together and conflicts were resolved.
- Data Transformation and reduction - Data is normalized,
aggregated and generalized. Then it is represented in a
reduced form and stored in DataSet.

