import search_twitter

hashtags2019 =['bjp','modi','ModiLaoDeshBanao','hindu','ModiShah','NarendraModi','namo','amitshah','maibhichowkidar','chowkidarNarendraModi','ModiHaiToMumkinHai']
startdate2019 = ['201903011200','201903151200','201903291200']
endate2019=['201903141200','201903281200','201904061200']

hashtags2014 =['bjp','modi','ModiLaoDeshBanao','WeWantModi','AbKiBaarModiSarkaar','NarendraModi','namo','GharGharModi','AcheDinAaneWaleHai','RGForEducation','RGForIndia','RGTheBest','congress','rahulgandhi']
startdate2014 = ['201404011200','201404151200','201404291200']
endate2014=['201404141200','201404281200','201405121200']

tweets = []
hashs = []

for (sdate,edate) in zip(startdate2014,endate2014):
    for hash in hashtags2019:
        tweet_data = search_twitter.search_for_tweets(hash, 99,sdate,edate).json()
        for result in tweet_data['results']:
            hashs.append(hash)
            tweets.append(result['text'])


#print(text) 
import csv
with open('data_2019.csv', 'a',encoding="utf-8", newline='') as outfile:
    rowlists = zip(hashs,tweets)
    spamwriter = csv.writer(outfile)
    for row in rowlists:
          spamwriter.writerow(row)
