'''
Created on Dec 3, 2016

@author: Nidhalios
'''

from django.db import models
from django.utils import timezone

# Twitter Data Models 

class Twitter_User(models.Model):
    
    username = models.CharField(max_length=200, primary_key=True)
    full_name = models.CharField(max_length=200)
    img_url = models.URLField(max_length=300, blank=True)
    bio = models.TextField()
    location = models.CharField(max_length=100)
    joined_at = models.CharField(max_length=100)
    personal_url = models.URLField(max_length=200)
    tweets_count = models.PositiveIntegerField(default=0)
    followers_count = models.PositiveIntegerField(default=0)
    following_count = models.PositiveIntegerField(default=0)
    likes_count = models.PositiveIntegerField(default=0) 
    created_at = models.CharField(max_length=100, blank=True)
    updated_at = models.CharField(max_length=100, blank=True)
    
    def __str__(self):
        return self.username

class Twitter_Tweet(models.Model):    
    
    username = models.ForeignKey('Twitter_User', on_delete=models.CASCADE)
    tweet_id = models.CharField(max_length=200, primary_key=True)
    media_url = models.URLField(max_length=300, blank=True)
    text = models.TextField()
    truncated = models.BooleanField(default=False)
    longitude = models.CharField(max_length=100, blank=True)
    latitude = models.CharField(max_length=100, blank=True)
    lang = models.CharField(max_length=10, blank=True)
    favorite_count = models.PositiveIntegerField(default=0)
    retweet_count = models.PositiveIntegerField(default=0)
    created_at = models.CharField(max_length=100, blank=True)
    updated_at = models.CharField(max_length=100, blank=True)
    
    def __str__(self):
        return self.username&" "&self.tweet_id&" "&self.created_at
