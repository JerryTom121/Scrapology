'''
Created on Dec 2, 2016

@author: Nidhalios
'''

import tweepy #https://github.com/tweepy/tweepy
from time import sleep
from lxml import etree
import urllib.request
import urllib.parse
import urllib.error
import time
from scrapAPI.models import Twitter_User
from scrapAPI.models import Twitter_Tweet

#Twitter API credentials
CONSUMER_KEY = '2rRBjvp6FmqmcQjL7MGGzuKt9'
CONSUMER_SECRET = 'dF2G8LW68VbNkT5lrlxEZlgZEIGCUKlbb4TeCS2wfQNXDnPv3L'
ACCESS_TOKEN = '561381031-0AH3RUErmhNlTYJ1ArxdX7usnKAQ0zpuDyOl0cKs'
ACCESS_TOKEN_SECRET = 'IglJ6F06uss8Gct12cA6bCpR173vrKvtGpv2LcArpPU6o'

def convToInteger(x):
    if not x.isdigit():
       if(x.find(',') != -1): x = x.replace(',','')
       if(x.find('K') != -1): 
           x = x.replace('K','')
           i = float(x)
           i *= 1000
           return int(i)
       if(x.find('M') != -1): 
           x = x.replace('M','')
           i = float(x)
           i *= 1000000 
           return int(i)
       return int(x)
    else:
        return int(x)

def scrapTwProfile(username):
    
    url = "https://twitter.com/"+username
    req = urllib.request.Request(url)
    
    try:
        resp = urllib.request.urlopen(req)
    except urllib.error.HTTPError as e:
        print("HTTPError : "+str(e.code))
    except urllib.error.URLError as e:
        print("URLError : "+str(e.code))
    else:
        respData = resp.read()
        html = etree.HTML(respData)
        txt = html.xpath('//*[@id="page-container"]/div[2]/div/div/div[1]/div/div/div/div[1]/h1/a')[0].text
        full_name = txt.strip() if (txt and txt.strip()!="") else "N/A"
        txt = html.xpath('//*[@id="page-container"]/div[1]/div/div[1]/div[2]/div[1]/div/a/img/@src')[0]
        img_url = txt.strip() if (txt and txt.strip()!="") else "N/A"
        txt = html.xpath('//*[@id="page-container"]/div[2]/div/div/div[1]/div/div/div/div[1]/p')[0].text
        bio = txt.strip() if (txt and txt.strip()!="") else "N/A"
        txt = html.xpath('//*[@id="page-container"]/div[2]/div/div/div[1]/div/div/div/div[1]/div[1]/span[2]')[0].text
        location = txt.strip() if (txt and txt.strip()!="") else "N/A"
        txt = html.xpath('//*[@id="page-container"]/div[2]/div/div/div[1]/div/div/div/div[1]/div[3]/span[2]')[0].text
        joined_date = txt.strip() if (txt and txt.strip()!="") else "N/A"
        txt = html.xpath('//*[@id="page-container"]/div[2]/div/div/div[1]/div/div/div/div[1]/div[2]/span[2]/a')[0].text
        personal_url = txt.strip() if (txt and txt.strip()!="") else "N/A"
        txt = html.xpath('//*[@id="page-container"]/div[1]/div/div[2]/div/div/div[2]/div/div/ul/li[1]/a/span[2]')[0].text
        nbTweets = txt.strip() if (txt and txt.strip()!="") else "N/A"
        txt = html.xpath('//*[@id="page-container"]/div[1]/div/div[2]/div/div/div[2]/div/div/ul/li[3]/a/span[2]')[0].text
        nbFollowers = txt.strip() if (txt and txt.strip()!="") else "N/A"
        txt = html.xpath('//*[@id="page-container"]/div[1]/div/div[2]/div/div/div[2]/div/div/ul/li[2]/a/span[2]')[0].text
        nbFollowing = txt.strip() if (txt and txt.strip()!="") else "N/A"
        txt = html.xpath('//*[@id="page-container"]/div[1]/div/div[2]/div/div/div[2]/div/div/ul/li[4]/a/span[2]')[0].text
        nbLikes = txt.strip() if (txt and txt.strip()!="") else "N/A"
        user = Twitter_User(username=username.lower(), full_name=full_name, img_url=img_url,  bio=bio, location=location,
                             joined_at=joined_date, personal_url=personal_url, tweets_count=convToInteger(nbTweets), 
                             followers_count=convToInteger(nbFollowers), following_count=convToInteger(nbFollowing), 
                             likes_count=convToInteger(nbLikes))
        user.created_at=user.updated_at =  time.strftime("%d-%m-%Y")
        user.save()
        return user

def getLatestTweets(twuser, alltweets=[], max_id=0):
    #Twitter only allows access to a users most recent 3240 tweets with this method
    #authorize twitter, initialize tweepy
    auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
    auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)
    api = tweepy.API(auth)
    #make initial request for most recent tweets (200 is the maximum allowed count)
    if max_id is 0:
        new_tweets = api.user_timeline(screen_name=twuser.username, count=200)
    else:
        # new new_tweets
        new_tweets = api.user_timeline(screen_name=twuser.username, count= 200, max_id=max_id)

    if len(new_tweets) > 0:
        #save most recent tweets
        tab = []
        for tweet in new_tweets:
            tweet_model = Twitter_Tweet(username=twuser, tweet_id=tweet.id_str, created_at=tweet.created_at,
                                        updated_at=tweet.created_at, text=tweet.text.encode("utf-8"),
                                        truncated=tweet.truncated)
            try:
                tweet_model.media_url = tweet.entities['media'][0]['media_url']
            except (NameError, KeyError):
                tweet_model.media_url = "N/A"
            if(tweet.coordinates != None):
                tweet_model.longitude = tweet.coordinates['coordinates'][0]
                tweet_model.latitue = tweet.coordinates['coordinates'][1]
            else:
                tweet_model.longitude = "N/A" 
                tweet_model.latitue = "N/A" 
            if(tweet.lang != None):
                tweet_model.lang = tweet.lang
            else:
                tweet_model.lang = "N/A"
            if(tweet.favorite_count != None):
                tweet_model.favorite_count = tweet.favorite_count
            else:
                tweet_model.favorite_count = 0
            if(tweet.retweet_count != None):
                tweet_model.retweet_count = tweet.retweet_count
            else:
                tweet_model.retweet_count = 0
            
            tab.append(tweet_model)
        
        #Save the current bulk of tweets
        Twitter_Tweet.objects.bulk_create(tab)
        alltweets.extend(tab)
        # security
        sleep(2)
        #update the id of the oldest tweet less one
        oldest = int(alltweets[-1].tweet_id) - 1
        return getLatestTweets(twuser, alltweets=alltweets, max_id=oldest)

    #final tweets
    return alltweets