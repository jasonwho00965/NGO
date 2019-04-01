from django.contrib import admin
from .models import User


# Gives us access to this data within the Admin page. At least I think so - Ed.
@admin.register(User)
class AdminDisplay(admin.ModelAdmin):
	list_display = ['first_name', 'last_name', 'email', 'role']
