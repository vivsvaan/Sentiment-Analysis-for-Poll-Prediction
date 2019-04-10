"""
@author: Abhinav Khetarpal
"""
import requests
import base64

# these are the access keys associated with my twitter app
# TODO - find a way to make them not appear in the source code

# add keys accordingly
consumer_key = 'CQGMKF5imQ7J6Cyl85Bh9mILN'
consumer_secret_key = 'eslhOxns82F4uNSzTwbFIiTTqixX2Ekimmbk3E4DMYsv2s8MoH'
base_url = 'https://api.twitter.com/'


def create_key():
    """
     The twitter API requires a single key that is a string of a base64 encoded version of the two keys
     separated by a colon.

    :return: encoded key in required format
    """
    keys = f'{consumer_key}:{consumer_secret_key}'.encode('ascii')
    b64_encoded_keys = base64.b64encode(keys)
    b64_encoded_keys = b64_encoded_keys.decode('ascii')

    return b64_encoded_keys


def get_bearer_token():

    """
    creates a url to make a POST request to the api end-point to obtain a Bearer Token to be included in
    subsequent API requests
    :return: Bearer token
    """

    # create a url to send POST  request
    auth_url = f'{base_url}oauth2/token'

    key = create_key()

    auth_headers = {
        'Authorization': f'Basic {key}',
        'Content-Type': 'application/x-www-form-urlencoded;charset=UTF-8'
    }

    auth_data = {
        'grant_type': 'client_credentials'
    }

    # request
    auth_response = requests.post(auth_url, headers=auth_headers, data=auth_data)

    # this the bearer token that we obtain and can now use in subsequent API calls
    access_token = auth_response.json()['access_token']

    return access_token


def premium_search_for_tweets(hashtag=None, maxResults=None, fromdate=None, todate=None, geocode = None):
    """
    searches for tweets matching the given criteria using premium search API endpoint
    :paramss: hastag, maxResults (10-100), fromdate, todate, geocode
    :return: tweet data
    """

    #Search url for full-archive
    premium_search_url = f'{base_url}1.1/tweets/search/fullarchive/electionTweets.json'

    # generating authorization header
    access_token = get_bearer_token()
    search_headers = {
        'Authorization': f'Bearer {access_token}'
    }

    
    # getting longitude latitude and radius values from the geocode
    longitude = geocode['longitude']
    latitude = geocode['latitude']
    radius = geocode['radius']

    search_params = {
        'query': f'#{hashtag} AND -is:retweet AND -is:reply AND point_radius:[{longitude} {latitude} {radius}]',
        'maxResults': maxResults,
        'fromDate': fromdate,
        'toDate': todate
    }

    return requests.get(url=premium_search_url, headers=search_headers, params=search_params)


def standard_search_for_tweets(hashtag = None, result_type = None, count = None, geocode = None):

    """
    searches for tweets matching the given criteria using standard search API endpoint
    :paramss: hastag, result_type, count, geocode
    :return: tweet data
    """
    
    #search url for standard search api
    standard_search_url = f'{base_url}1.1/search/tweets.json'

    # generating authorization header
    access_token = get_bearer_token()
    search_headers = {
        'Authorization': f'Bearer {access_token}'
    }

    # query parameters

    longitude = geocode['longitude']
    latitude = geocode['latitude']
    radius = geocode['radius']

    search_params = {
        'q': f'#{hashtag}',
        'geocode': f'{latitude},{longitude},{radius}',
        'result_type': result_type,
        'count': count
    }

    return requests.get(standard_search_url, headers=search_headers, params=search_params)
