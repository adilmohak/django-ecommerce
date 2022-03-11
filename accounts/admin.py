from django.contrib import admin
from django.contrib.auth.models import Group

from .models import *


class UserAdmin(admin.ModelAdmin):
    list_display = ['get_full_name', 'username', 'email', 'is_active', 'is_customer', 'is_staff']
    search_fields = ['get_full_name', 'username', 'first_name', 'last_name', 'email', 'is_active', 'is_customer', 'is_staff']

    class Meta:
        managed = True
        verbose_name = 'User'
        verbose_name_plural = 'Users'

admin.site.register(User, UserAdmin)
# admin.site.register(Student)

admin.site.unregister(Group)
