from django.contrib import admin
from .models import UserManagement
from .models import EventManagement
from django.contrib.auth.models import User, Group
from django.utils.html import format_html



admin.site.unregister(User)
admin.site.unregister(Group)

# Gives us access to this data within the Admin page. At least I think so - Ed.

class AdminDisplay(admin.ModelAdmin):

	list_display = ['first_name', 'last_name','email','role']


class EventDisplay(admin.ModelAdmin):
	list_display = ['Event','Category','Location','Start_date','End_date']



admin.site.register(EventManagement,EventDisplay)
admin.site.register(UserManagement, AdminDisplay)

