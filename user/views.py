from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
import user.forms as forms
from django.shortcuts import redirect
from django.urls import reverse
from django.contrib.auth import authenticate,logout,login
# Create your views here.

def login_user(request):
    if request.method=='POST':
        form=forms.Authorization(request.POST)
        if form.is_valid():
            cd=form.cleaned_data
            user=authenticate(request, username=cd['username'],password=cd['password'])
            if user and user.is_active:
                login(request,user)
                return HttpResponseRedirect(reverse('home'))
    else:
        form=forms.Authorization()

    return render(request,'user/authorization.html',{'form':form})

def logout_user(request):
    logout(request)
    return HttpResponseRedirect(reverse('users:login'))