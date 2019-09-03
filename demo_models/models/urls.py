from django.contrib import admin
from django.urls import path, include
from . import views
urlpatterns = [
    path('', views.HomePage.as_view(), name='home'),
   path('users/', views.Users.as_view(), name = 'users'),

    path('roles/', views.RolesToShow.as_view(), name='roles'),



]
