from django.urls import path, include
from django.contrib.auth import views as auth_views
from . import views
from .utils import get_daily_code, get_monthly_code, get_weekly_code

today_str = get_daily_code()
monthly_str = get_monthly_code()
weekly_str = get_weekly_code()

urlpatterns = [
    path("", views.orders, name="orders"),
    path('home<str:code_str>/', views.home, name="home"),
    path("sandpainting<str:code_str>/", views.sandpainting, name="sandpainting"),
    path("cookieclicker<str:code_str>/", views.cookie, name="cookie"),
    path("burrito<str:code_str>/", views.burrito, name="burrito"),
    path("web<str:code_str>/", views.web, name="web"),
    path("dash<str:code_str>/", views.dash, name="dash"),
    path("test<str:code_str>/", views.test, name="test"),
    path("minecraft<str:code_str>/", views.minecraft, name="minecraft"),
    path("RetroBowl<str:code_str>/", views.RetroBowl, name="RetroBowl"),
    path("ships3d<str:code_str>/", views.ships3d, name="ships3d"),
    path("pizza<str:code_str>/", views.pizza, name="pizza"),
    path("code42/", views.code, name="code"),
    path("notify<str:code_str>/", views.notify_view, name="notify"),
    path("notifications<str:code_str>/", views.notifications_view, name="notifications"),
    path("mark_read<str:code_str>/<int:notification_id>/", views.mark_read_view, name="mark_read"),
    path("account<str:code_str>/", include("django.contrib.auth.urls")),
    path("signup<str:code_str>/", views.signup_view.as_view(), name="signup"),
    path("logout<str:code_str>/", views.logout_view, name="logout"),
    path("account/login/", auth_views.LoginView.as_view(), name="login"),
    path("unread-count/", views.unread_count, name="unread_count"),
    path("login-redirect/", views.login_redirect, name="login_redirect"),
    path("obby<str:code_str>/", views.obby, name="obby"),
    path("Brotato<str:code_str>/", views.Brotato, name="Brotato"),
    path("Soap<str:code_str>/", views.Soap, name="Soap"),
]