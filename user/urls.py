from django.urls import path
from user import views
from django.contrib.auth.views import LogoutView

app_name="user"

urlpatterns = [
    path('',views.user,name='user'),
    path('login/',views.LoginUser.as_view(),name='login'),
    path('logout/', views.logout_user, name='logout'),
    path('register/', views.register, name='register'),

]