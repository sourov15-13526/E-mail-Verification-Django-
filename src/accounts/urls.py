
from django.contrib import admin
from django.urls import path
from .views import *

urlpatterns = [
    path('' ,  home  , name="home"),
    path('register/' , register_attempt , name="register_attempt"),
    path('accounts/login/' , login_attempt , name="login_attempt"),
    path('token/' , token_send , name="token_send"),
    path('success/' , success , name='success'),
    path('verify/<auth_token>' , verify , name="verify"),
    path('error/' , error_page , name="error")

    
   
]




"""from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home' ),
    path('login/', views.login_attempt, name='login' ),
    path('register/', views.register_attempt, name='register' ),
    path('token/', views.token_send, name='token_send'),
    path('success/', views.success, name='success'),
]"""
