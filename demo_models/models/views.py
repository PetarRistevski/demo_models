from django.shortcuts import render
from .models import User, UserRole
# Create your views here.
from django.views import generic


class HomePage(generic.ListView):
    template_name = 'index.html'


    def get_queryset(self):
        return User.objects.all()


class RolesToShow(generic.ListView):

    template_name = 'roles.html'

    def get_queryset(self):
        return UserRole.objects.all()


class Users(generic.ListView):
    template_name = 'users.html'

    def get_queryset(self):
        return User.objects.all()


