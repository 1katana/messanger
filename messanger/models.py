from django.db import models
from django.contrib.auth import get_user_model


# Create your models here.
# class User(models.Model):
#     name = models.CharField(blank=True, null=True, max_length=200)
#     surname = models.CharField(blank=True, null=True, max_length=200)
#     patronymic = models.CharField(blank=True, null=True, max_length=200)
#     email = models.EmailField(blank=True, null=True)
#     password = models.CharField(blank=True, null=True, max_length=200)



class Group(models.Model):
    group_name = models.CharField(blank=True, null=True, max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)
    admin_id = models.ForeignKey(get_user_model(), models.SET_NULL, blank=True, null=True)

class Contacts(models.Model):
    user_id = models.ForeignKey(get_user_model(), models.SET_NULL, blank=True, null=True, related_name='contacts')
    contact_user_id = models.ForeignKey(get_user_model(), models.SET_NULL, blank=True, null=True, related_name='contact_of')
    group=models.ForeignKey(Group,models.SET_NULL,blank=True, null=True)

class GroupMembers(models.Model):
    joined_at = models.DateField(auto_now_add=True)
    user_id = models.ForeignKey(get_user_model(), models.SET_NULL, blank=True, null=True)
    group_id = models.ForeignKey(Group, models.SET_NULL, blank=True, null=True)

class Message(models.Model):
    content = models.TextField(blank=True, null=True)
    timestamp = models.DateTimeField(auto_now_add=True)
    sender_id = models.ForeignKey(get_user_model(), models.SET_NULL, blank=True, null=True, related_name='sent_messages')
    receiver_id = models.ForeignKey(get_user_model(), models.SET_NULL, blank=True, null=True, related_name='received_messages')
    group = models.ForeignKey(Group, models.SET_NULL, blank=True, null=True)
