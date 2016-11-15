from django.db import models
from django.utils import timezone

# Twitter Data Models 

class Twitter_User(models.Model):
    
    username = models.CharField(max_length=200)
    full_name = models.CharField(max_length=200)
    bio = models.TextField()
    location = models.CharField(max_length=100)
    joined_date = models.CharField(max_length=100)
    personal_url = models.URLField(max_length=200)
    nbTweets = models.PositiveIntegerField(default=0)
    nbFollowers = models.PositiveIntegerField(default=0)
    nbFollowing = models.PositiveIntegerField(default=0)
    nbLikes = models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.username
