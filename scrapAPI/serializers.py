'''
Created on Dec 2, 2016

@author: Nidhalios
'''
from rest_framework import serializers
from scrapAPI.models import Twitter_User
from scrapAPI.models import Twitter_Tweet
from collections import OrderedDict


class Twitter_User_Serializer(serializers.ModelSerializer):
    
    def to_representation(self, instance):
        ret = OrderedDict()
        ret['username'] = instance.username
        ret['full_name'] = instance.full_name
        ret['img_url'] = instance.img_url
        ret['bio'] = instance.bio
        ret['location'] = instance.location
        ret['joined_at'] = instance.joined_at
        ret['personal_url'] = instance.personal_url
        ret['tweets_count'] = instance.tweets_count
        ret['followers_count'] = instance.followers_count
        ret['following_count'] = instance.following_count
        ret['likes_count'] = instance.likes_count
        ret['created_at'] = instance.created_at
        ret['updated_at'] = instance.updated_at
        return ret
    
    class Meta:
        model = Twitter_User
        fields = ('username', 'full_name', 'img_url', 'bio', 'location', 'joined_at', 'personal_url', 
                  'nbTweets', 'nbFollowers', 'nbFollowing', 'nbLikes', 'created_at', 'updated_at')

class Twitter_Tweet_Serializer(serializers.ModelSerializer):
    
    def to_representation(self, instance):
        ret = OrderedDict()
        ret['tweet_id'] = instance.tweet_id
        ret['username'] = instance.username.username
        ret['text'] = instance.text
        ret['truncated'] = instance.truncated
        ret['media_url'] = instance.media_url
        ret['lang'] = instance.lang
        ret['longitude'] = instance.longitude
        ret['latitude'] = instance.latitude
        ret['favorite_count'] = instance.favorite_count
        ret['retweet_count'] = instance.retweet_count
        ret['created_at'] = instance.created_at
        ret['updated_at'] = instance.updated_at
        return ret
    
    class Meta:
        model = Twitter_Tweet
        fields = ('tweet_id', 'username', 'text', 'truncated', 'media_url', 'lang', 'longitude', 'latitude', 'favorite_count', 
                  'retweet_count', 'created_at', 'updated_at')

        
        

         
        