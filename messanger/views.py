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






def base(request):
    user=get_user_model().objects.get(username=name)

    contacts=Contacts.objects.filter(user_id=user)

    context={}

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
                'contacts': contacts,
                'messages_user': 1,
                'messages': messages
            }
            return render(request, 'messanger/index.html', context)
    else:
        form = change_contact()
        context={
            'user': user,
            'contacts':  contacts ,
            'messages_user': 0,
            # 'messages': messages
        }
    return render(request, 'messanger/index.html',context)