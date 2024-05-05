from django.urls import path
from messanger import views


urlpatterns = [
    path('',views.base,name='home'),

]

