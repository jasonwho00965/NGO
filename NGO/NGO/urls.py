"""NGO URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.views.generic.base import TemplateView


urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('django.contrib.auth.urls')),
    path('', TemplateView.as_view(template_name='home.html'), name='home'),
    path('user-view/', TemplateView.as_view(template_name='user_view.html'), name='event'),
    path('event-details/', TemplateView.as_view(template_name='event_details.html'), name='event-details'),
    path('register/', TemplateView.as_view(template_name='register.html'), name='register'),
    path('price/', TemplateView.as_view(template_name='total_price.html'), name='price'),
    path('conformation/', TemplateView.as_view(template_name='confirm.html'), name='conformation'),
]

admin.site.site_header = "NGO Admin"
admin.site.site_title = "NGO Admin Portal"
admin.site.index_title = "Welcome to NGO"
