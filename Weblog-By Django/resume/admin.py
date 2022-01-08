from django.contrib import admin

from .models import *

class UserProfileAdmin(admin.ModelAdmin):
    list_display = ['user','description']
admin.site.register(UserProfile,UserProfileAdmin)

admin.site.register(Category)
