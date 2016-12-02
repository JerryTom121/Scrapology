from django.contrib import messages
from django.shortcuts import render
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from .forms import TwForm
from .models import Twitter_User
from .scrapTwitter import scrapTwProfile
from .serializers import Twitter_User_Serializer
import time


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
                user.created_date=user.updated_date =  time.strftime("%d-%m-%Y")
                user.save()
                serializer = Twitter_User_Serializer(user)
                return Response({'message' : 'Profile scrapped and saved successfuly in the database.',
                                 'data':serializer.data},
                                  status=status.HTTP_201_CREATED)
            else:
                return Response(status=status.HTTP_404_NOT_FOUND)
        
        return Response(status=status.HTTP_500_INTERNAL_ERROR)

def tw_form(request):
    if request.method == "POST":
        form = TwForm(request.POST)
        if form.is_valid(): 
            name = form.cleaned_data.get('username')
            obj = Twitter_User.objects.filter(username=name)
            print(obj != None)
            if (obj != None):
                if len(obj) == 0:
                    user =  scrapTwProfile(name)
                    if(user):
                        user.save()
                        messages.add_message(request, messages.SUCCESS, 'Profile scrapped and saved successfuly in the database.')
                        return render(request, 'scrapAPI/twUserDetails.html', {'user': user})
                    else:
                        messages.add_message(request, messages.ERROR, 'Username not found or HTTP/URL error has occured')
                        return render(request, 'scrapAPI/twForm.html', {'form': form})
                else:
                    messages.add_message(request, messages.INFO, 'User exists already in the database.')
                    return render(request, 'scrapAPI/twUserDetails.html', {'user': obj[0]})
            else:
                messages.add_message(request, messages.ERROR, 'An Error has occured')
                return render(request, 'scrapAPI/twForm.html', {'form': form})
        else:
            return render(request, 'scrapAPI/twForm.html', {'form': form})
    else:
        form = TwForm()
        return render(request, 'scrapAPI/twForm.html', {'form': form})
    
