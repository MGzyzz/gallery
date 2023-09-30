from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from accounts.models import User, Profile

# Register your models here.


class ProfileInLine(admin.StackedInline):
    model = Profile
    fields = []


class UserProfileAdmin(UserAdmin):
    list_display = ['id', 'username']
    inlines = [ProfileInLine]


admin.site.register(User, UserProfileAdmin)
