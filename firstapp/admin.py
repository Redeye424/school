from django.contrib import admin
from django import forms
from django.contrib.auth.models import User
from .models import shoe_todo, Profile, Notification


admin.site.register(shoe_todo)
admin.site.register(Profile)
admin.site.register(Notification)