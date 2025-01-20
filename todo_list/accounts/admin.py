from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser

class CustomUserAdmin(UserAdmin):
    model = CustomUser
    list_display = [
        'username', 
        'email', 
        'avatar_img', 
        'level', 
        'xp', 
        'strength', 
        'intelligence', 
        'creativity', 
        'coins', 
        'is_active', 
        'is_staff'
    ]
    list_filter = ['is_active', 'is_staff', 'level']
    search_fields = ['username', 'email']
    ordering = ['username']
    

admin.site.register(CustomUser, CustomUserAdmin)