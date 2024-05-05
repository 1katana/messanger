from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.db.models import Q
from messanger.models import *
from messanger.forms import *
from user.models import *
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.http import HttpResponse
from django.shortcuts import redirect 
from django.contrib.auth import get_user_model

name="katana"





@login_required
def base(request):
    # if request.user.is_authenticated:
    user=request.user

    contacts=Contacts.objects.filter(user_id=user)

    img=User_File_Upload.objects.filter(user=user)

    avatar=0
    for i in img:
        if i.is_avatar==True:
            avatar=i

    # context={}

    messages={}

    k=0

    if request.method=='POST':
        form=change_contact(request.POST)
        if form.is_valid():
            pk=form.cleaned_data['pk']
            for i in contacts:
                if i.contact_user_id != None:
                    if i.contact_user_id.pk==pk:
                        pk_user = i.contact_user_id
                        messages = Message.objects.filter(Q(sender_id=pk_user) | Q(receiver_id=pk_user))

                        break

                else:
                    if i.group.pk == pk:
                        pk_group=i.group
                        messages=Message.objects.filter(group=pk_group)

            context = {
                'user': user,
                'avatar': avatar,
                'contacts': contacts,
                'messages_user': 1,
                'messages': messages
            }
            return render(request, 'messanger/index.html', context)

    context = {
        'user': user,
        'avatar': avatar,
        'contacts': contacts,
        'messages_user': 0,
        # 'messages': messages
    }
    return render(request, 'messanger/index.html',context)