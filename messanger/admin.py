from django.contrib import admin
from messanger import models

# Register your models here.
# admin.site.register(models.User)
admin.site.register(models.Contacts)
admin.site.register(models.Group)
admin.site.register(models.Message)
admin.site.register(models.GroupMembers)