from django.conf.urls import include, url, patterns
from django.contrib import admin
from . import views

urlpatterns = [
	url(r'^home/$', views.home, name='home'),
]