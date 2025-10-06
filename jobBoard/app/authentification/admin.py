from django.contrib import admin

from .models import User

class UserAdmin(admin.ModelAdmin):
    list_display = ['username', 'last_name', 'email', 'date_joined', 'role']

admin.site.register(User, UserAdmin)