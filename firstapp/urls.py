from django.urls import path, include
from django.contrib.auth import views as auth_views
from . import views
from .utils import get_daily_code, get_monthly_code, get_weekly_code

today_str = get_daily_code()
monthly_str = get_monthly_code()
weekly_str = get_weekly_code()

print(today_str)
urlpatterns = [
    path("", views.orders, name="orders"),
    path('home<str:today_str>/', views.home, name="home"),
    path('home<str:monthly_str>/', views.home_month, name="home"),
    path('home<str:weekly_str>/', views.home_week, name="home"),
    path("sandpainting<str:today_str>/", views.sandpainting, name="sandpainting"),
    path("cookieclicker<str:today_str>/", views.cookie, name="cookie"),
    path("burrito<str:today_str>/", views.burrito, name="burrito"),
    path("web<str:today_str>/", views.web, name="web"),
    path("dash<str:today_str>/", views.dash, name="dash"),
    path("test<str:today_str>/", views.test, name="test"),
    path("minecraft<str:today_str>/", views.minecraft, name="minecraft"),
    path("RetroBowl<str:today_str>/", views.RetroBowl, name="RetroBowl"),
    path("ships3d<str:today_str>/", views.ships3d, name="ships3d"),
    path("pizza<str:today_str>/", views.pizza, name="pizza"),
    path("code42/", views.code, name="code"),
    path("notify<str:today_str>/", views.notify_view, name="notify"),
    path("notifications<str:today_str>/", views.notifications_view, name="notifications"),
    path("mark_read<str:today_str>/<int:notification_id>/", views.mark_read_view, name="mark_read"),
    path("account<str:today_str>/", include("django.contrib.auth.urls")),
    path("signup<str:today_str>/", views.signup_view.as_view(), name="signup"),
    path("logout<str:today_str>/", views.logout_view, name="logout"),
    path("account/login/", auth_views.LoginView.as_view(), name="login"),
    path("unread-count/", views.unread_count, name="unread_count"),
    path("login-redirect/", views.login_redirect, name="login_redirect"),
]