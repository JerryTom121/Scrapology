from django.db import models
from django.utils import timezone

# Twitter Data Models 

class Twitter_User(models.Model):
    
    username = models.CharField(max_length=200)
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    Bio = models.TextField()
    location = models.CharField(max_length=200)
    personal_url = models.URLField(max_length=300)
    nbtweets = models.PositiveIntegerField(default=0)
    nbFollowers = models.PositiveIntegerField(default=0)
    nbFollowing = models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.username
