from django.contrib import admin
from django import forms
from django.contrib.auth.models import User
from .models import Profile, Notification

admin.site.register(Profile)
admin.site.register(Notification)