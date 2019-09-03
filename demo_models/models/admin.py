from django.contrib import admin

# Register your models here.
from .models import  *


class UserAdmin(admin.ModelAdmin):

    search_fields = ('firstName', 'lastName')

admin.site.register(User, UserAdmin)

admin.site.register(UserRole)

