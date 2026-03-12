from django.urls import path, include
from django.contrib.auth import views as auth_views
from . import views
from .utils import get_daily_code

today_str = get_daily_code()
print(today_str)
urlpatterns = [
    path("", views.orders, name="orders"),
    path('home<str:today_str>/', views.home, name="home"),
    path("sandpainting<str:today_str>/", views.sandpainting, name="sandpainting"),
    path("cookieclicker<str:today_str>/", views.cookie, name="cookie"),
    path("burrito<str:today_str>/", views.burrito, name="burrito"),
    path("web<str:today_str>/", views.web, name="web"),
    path("dash<str:today_str>/", views.dash, name="dash"),
    path("test<str:today_str>/", views.test, name="test"),
    path("minecraft<str:today_str>/", views.minecraft, name="minecraft"),
    path("RetroBowl<str:today_str>/", views.RetroBowl, name="RetroBowl"),
    path("ships3d<str:today_str>/", views.ships3d, name="ships3d"),
    path("code403022/", views.code, name="code"),
]