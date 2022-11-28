from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User, UserProfile
# Register your models here.

class CustomUserAdmin(UserAdmin):
    list_display = ('username', 'first_name', 'last_name', 'email', 'phone_number', 'role', 'is_active')
    ordering = ('-date_joined',)
    filter_horizontal = ()
    list_filter = ()
    fieldsets = ()


# admin.site.register(User, UserAdmin)
admin.site.register(User, CustomUserAdmin)
admin.site.register(UserProfile)