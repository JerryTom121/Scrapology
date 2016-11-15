from django.shortcuts import render
from .forms import TwForm
from .models import Twitter_User
from .scrapTwitter import scrapTwProfile
from django.contrib import messages

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