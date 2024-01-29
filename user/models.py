from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    temp=models.CharField(max_length=200)
