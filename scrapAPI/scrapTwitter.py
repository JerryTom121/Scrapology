'''
Created on Dec 2, 2016

@author: Nidhalios
'''

from lxml import etree
import urllib.request
import urllib.parse
import urllib.error
from scrapAPI.models import Twitter_User

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
        return Twitter_User(username=username.lower(), full_name=full_name, img_url=img_url,  bio=bio, location=location,
                             joined_date=joined_date, personal_url=personal_url, nbTweets=convToInteger(nbTweets), 
                             nbFollowers=convToInteger(nbFollowers), nbFollowing=convToInteger(nbFollowing), 
                             nbLikes=convToInteger(nbLikes))