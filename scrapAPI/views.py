from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from tweepy import TweepError

from .models import Twitter_Tweet
from .models import Twitter_User
from .scrapTwitter import getLatestTweets
from .scrapTwitter import scrapTwProfile
from .serializers import Twitter_Tweet_Serializer
from .serializers import Twitter_User_Serializer


@api_view(['GET'])
def twusers_list(request, format=None):
    """
    List all scrapped Twitter Users.
    """
    if request.method == 'GET':
        users = Twitter_User.objects.all()
        serializer = Twitter_User_Serializer(users, many=True)
        return Response({'data':serializer.data}, status=status.HTTP_200_OK)

@api_view(['GET', 'POST'])
def twuser_detail(request, username, format=None):
    """
    Scrap Twitter user with Username and save it in DB if he wasn't scrapped already
    else try to retrieve from DB.
    """
    if request.method == 'GET':
        try:
            user = Twitter_User.objects.get(username__iexact=username)
            serializer = Twitter_User_Serializer(user)
            return Response({'data':serializer.data}, status=status.HTTP_200_OK)
        except Twitter_User.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
   
    elif request.method == 'POST':
        try:
            user = Twitter_User.objects.get(username__iexact=username)
            if(user):
                serializer = Twitter_User_Serializer(user)
                return Response({'message' : 'User exists already in the database.',
                                 'data':serializer.data},
                                  status=status.HTTP_200_OK)
        except Twitter_User.DoesNotExist:
            user =  scrapTwProfile(username)
            if(user):
                serializer = Twitter_User_Serializer(user)
                return Response({'message' : 'Profile scrapped and saved successfuly in the database.',
                                 'data':serializer.data},
                                  status=status.HTTP_201_CREATED)
            else:
                return Response(status=status.HTTP_404_NOT_FOUND)
        
        return Response(status=status.HTTP_500_INTERNAL_ERROR)

@api_view(['GET', 'POST'])
def twuser_tweets(request, username, format=None):
    
    if request.method == 'GET':
        try:
            user = Twitter_User.objects.get(username__iexact=username)
            if(user != None):
                try:
                    tweets = Twitter_Tweet.objects.filter(username=username.lower())
                    serializer = Twitter_Tweet_Serializer(tweets, many=True)
                    return Response({'data':serializer.data}, status=status.HTTP_200_OK)
                except Twitter_Tweet.DoesNotExist:
                    return Response({'message' : 'No Tweets found in DB by this Username'},
                            status=status.HTTP_404_NOT_FOUND)
        except Twitter_User.DoesNotExist:
            return Response({'message' : 'Username does not exist in DB, Please scrap User Profile First'},
                            status=status.HTTP_404_NOT_FOUND)
   
    elif request.method == 'POST':
        try:
            user = Twitter_User.objects.get(username__iexact=username)
            if(user != None):
                try:
                    Twitter_Tweet.objects.filter(username=username.lower()).delete()
                    tweets = getLatestTweets(user,[],0)
                    if(len(tweets)>0):
                        serializer = Twitter_Tweet_Serializer(tweets, many=True)
                        return Response({'tweets retrieved':len(tweets),
                                        'oldest tweet':tweets[-1].created_at,
                                        'newest tweet':tweets[0].created_at,
                                        'data':serializer.data}, 
                                        status=status.HTTP_200_OK)
                    else:
                        return Response({'message' : 'No Tweets posted by this Username'},
                            status=status.HTTP_404_NOT_FOUND)
        
                    
                except Twitter_Tweet.DoesNotExist:
                    return Response({'message' : 'No Tweets found in DB by this Username'},
                            status=status.HTTP_404_NOT_FOUND)
        except Twitter_User.DoesNotExist:
            return Response({'message' : 'Username does not exist in DB, Please scrap User Profile First'},
                            status=status.HTTP_404_NOT_FOUND)