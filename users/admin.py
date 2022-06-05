from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .forms import CustomUserCreation,CustomUserChange
from .models import CustomUser

class CustomUserAdmin(UserAdmin):
    form = CustomUserChange
    add_form = CustomUserCreation
    list_display = ['username','email','is_staff','last_login','user_logout_time']
    model = CustomUser

admin.site.register(CustomUser,CustomUserAdmin)

# Register your models here.

