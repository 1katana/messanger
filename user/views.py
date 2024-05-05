from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect


import user.forms as forms
from django.shortcuts import redirect
from django.urls import reverse
from django.contrib.auth import authenticate,logout,login
# Create your views here.
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.views import LoginView
from user import forms
from django.contrib import messages

from user.models import User_File_Upload


class LoginUser(LoginView):
    form_class=forms.Authorization
    template_name='user/authorization.html'
    extra_context={}

@login_required
def user(request):
    return render(request, 'user/user.html')

def register(request):
    if request.method == 'POST':
        form = forms.RegisterUserForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data['password'])
            user.save()
            if len(request.FILES)>0:

                img = request.FILES['image_upload']
                user_file_upload = User_File_Upload(user=user, photo=img, is_avatar=True)
                user_file_upload.save()
            else:
                User_File_Upload.set_default_image(user)

            user = authenticate(request, username=form.cleaned_data['username'], password=form.cleaned_data['password'])


            # if img!=None:
            #      user_file_upload = User_File_Upload(user=user.id,photo=img,is_avatar=True)

            if user and user.is_active:
                login(request,user)
                return HttpResponseRedirect(reverse('home'))
    else:
        form = forms.RegisterUserForm()
    return render(request, 'user/register.html', {'form': form})

# def login_user(request):
#     if request.method=='POST':
#         form=forms.Authorization(request.POST)
#         if form.is_valid():
#             cd=form.cleaned_data
#             user=authenticate(request, username=cd['username'],password=cd['password'])
#             if user and user.is_active:
#                 login(request,user)
#                 return HttpResponseRedirect(reverse('home'))
#     else:
#         form=forms.Authorization()
#
#     return render(request,'user/authorization.html',{'form':form})

def logout_user(request):
    logout(request)
    return HttpResponseRedirect(reverse('user:login'))