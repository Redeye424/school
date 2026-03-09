from django.urls import path, include
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("sandpainting/", views.sandpainting, name="sandpainting"),
    path("cookieclicker/", views.cookie, name="cookie"),
    path("burrito/", views.burrito, name="burrito"),
    path("web/", views.web, name="web"),
    path("dash/", views.dash, name="dash"),
    path("test/", views.test, name="test"),
]