"""
@author: Abhinav Khetarpal
"""

import requests
import base64

# these are the access keys associated with my twitter app
# TODO - find a way to make them not appear in the source code

consumer_key = 'QOOW4lFGzOiLL6o6lfZZB2dlk'
consumer_secret_key = 'peJUPrdR1Co4jKkm37xDVFkeyqVt41bvYcvfoVDrjmezS1VRcQ'
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


def search_for_tweets(hashtag=None, maxResults=None, fromdate=None, todate=None):
    """
    searches for tweets matching the given criteria
    :paramss: hastag, maxResults (10-100), fromdate, todate
    :return: content of the tweets
    """

    search_url = f'{base_url}1.1/tweets/search/fullarchive/electionTweets.json'

    access_token = get_bearer_token()
    search_headers = {
        'Authorization': f'Bearer {access_token}'
    }

    search_params = {
        'query': f'#{hashtag}',
        'maxResults': maxResults,
        'fromDate': fromdate,
        'toDate': todate
    }
    return requests.get(url=search_url, headers=search_headers, params=search_params)
