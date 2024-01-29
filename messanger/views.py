from django.shortcuts import render
from django.db.models import Q
from messanger.models import *
from messanger.forms import *
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.http import HttpResponse
from django.shortcuts import redirect 
from django.contrib.auth import get_user_model

name="katana"


def authorization(request):
    
    if request.method == 'POST':
        

        auth=Authorization(request.POST)

        if auth.is_valid():
            global name
            name =auth.cleaned_data['name']
            return redirect('home')

    else:
        auth=Authorization()
    return render(request,'messanger/authorization.html',{'form':auth})




def base(request):
    user=get_user_model().objects.get(username=name)

    messages=Message.objects.filter(Q(sender_id=user) | Q(receiver_id=user))
    return render(request, 'messanger/base.html',{'title':'Главная страница','user':user,'messages':messages})