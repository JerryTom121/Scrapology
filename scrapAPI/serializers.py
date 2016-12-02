'''
Created on Dec 2, 2016

@author: Nidhalios
'''
from rest_framework import serializers
from scrapAPI.models import Twitter_User
from collections import OrderedDict


class Twitter_User_Serializer(serializers.ModelSerializer):
    
    def to_representation(self, instance):
        ret = OrderedDict()
        ret['id'] = instance.id
        ret['username'] = instance.username
        ret['full_name'] = instance.full_name
        ret['img_url'] = instance.img_url
        ret['bio'] = instance.bio
        ret['location'] = instance.location
        ret['joined_date'] = instance.joined_date
        ret['personal_url'] = instance.personal_url
        ret['nbTweets'] = instance.nbTweets
        ret['nbFollowers'] = instance.nbFollowers
        ret['nbFollowing'] = instance.nbFollowing
        ret['nbLikes'] = instance.nbLikes
        ret['created_date'] = instance.created_date
        ret['updated_date'] = instance.updated_date
        return ret
    
    class Meta:
        model = Twitter_User
        fields = ('id', 'username', 'full_name', 'img_url', 'bio', 'location', 'joined_date', 'personal_url', 'nbTweets', 'nbFollowers', 'nbFollowing', 'nbLikes', 'created_date', 'updated_date')

        
        

         
        