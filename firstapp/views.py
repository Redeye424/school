from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.clickjacking import xframe_options_exempt
from .utils import get_daily_code, get_monthly_code, get_weekly_code
from .models import Profile, Notification
from django.http import HttpResponse
import os, csv
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.contrib.auth import logout
from django.shortcuts import redirect
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import User
from django.http import JsonResponse
from django.http import Http404


today_str = get_daily_code()
monthly_str = get_monthly_code()
weekly_str = get_weekly_code()

@xframe_options_exempt
def home(request, code_str):
    if (
        code_str != get_daily_code() and
        code_str != get_weekly_code() and
        code_str != get_monthly_code()
    ):
        raise Http404("Invalid code")
    return render(request, "home.html")
@xframe_options_exempt
def sandpainting(request, code_str):
    if (
        code_str != get_daily_code() and
        code_str != get_weekly_code() and
        code_str != get_monthly_code()
    ):
        raise Http404("Invalid code")
    return render(request, "sandpainting.html")
@xframe_options_exempt
def cookie(request, code_str):
    if today_str != get_daily_code():
        raise Http404("Invalid code")
    return render(request, "cookie.html")
@xframe_options_exempt
def burrito(request, code_str):
    if (
        code_str != get_daily_code() and
        code_str != get_weekly_code() and
        code_str != get_monthly_code()
    ):
        raise Http404("Invalid code")
    return render(request, "burrito.html")
@xframe_options_exempt
def web(request, code_str):
    if (
        code_str != get_daily_code() and
        code_str != get_weekly_code() and
        code_str != get_monthly_code()
    ):
        raise Http404("Invalid code")
    return render(request, "web.html")
@xframe_options_exempt
def dash(request, code_str):
    if (
        code_str != get_daily_code() and
        code_str != get_weekly_code() and
        code_str != get_monthly_code()
    ):
        raise Http404("Invalid code")
    return render(request, "dash.html")
@xframe_options_exempt
def test(request, code_str):
    if (
        code_str != get_daily_code() and
        code_str != get_weekly_code() and
        code_str != get_monthly_code()
    ):
        raise Http404("Invalid code")
    return render(request, "test.html")
@xframe_options_exempt
def orders(request):
    return render(request, "orders.html")
@xframe_options_exempt
def minecraft(request, code_str):
    if (
        code_str != get_daily_code() and
        code_str != get_weekly_code() and
        code_str != get_monthly_code()
    ):
        raise Http404("Invalid code")
    return render(request, "minecraft.html")
@xframe_options_exempt
def RetroBowl(request, code_str):
    if (
        code_str != get_daily_code() and
        code_str != get_weekly_code() and
        code_str != get_monthly_code()
    ):
        raise Http404("Invalid code")
    return render(request, "Retro Bowl.html")
@xframe_options_exempt
def ships3d(request, code_str):
    if (
        code_str != get_daily_code() and
        code_str != get_weekly_code() and
        code_str != get_monthly_code()
    ):
        raise Http404("Invalid code")
    return render(request, "ships3d.html")
@xframe_options_exempt
def pizza(request, code_str):
    if (
        code_str != get_daily_code() and
        code_str != get_weekly_code() and
        code_str != get_monthly_code()
    ):
        raise Http404("Invalid code")
    return render(request, "pizza.html")
@xframe_options_exempt
def code(request):
    return render(request, "code.html")




class signup_view(CreateView):
  form_class = UserCreationForm
  success_url = reverse_lazy("login")
  template_name = "registration/signup.html"

@login_required
def logout_view(request, today_str):
    logout(request)
    return redirect("home", today_str=today_str)

def login_redirect(request):
    return redirect('home', today_str=today_str)

@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)

@login_required

@login_required
def notify_view(request, today_str):
    roles = list(Profile.objects.values_list('role', flat=True).distinct()) + ["A"]
    users = User.objects.all()
    notifications = Notification.objects.filter(user=request.user).order_by('-created_at')

    # mark as read
    for notification in notifications:
        notification.read = True
        notification.save()

    if request.method == "POST":
        role = request.POST.get("role")
        user_selected = request.POST.get("User")
        message = request.POST.get("message")

        if message:

            # ONE USER
            if user_selected and user_selected != "all":
                user = User.objects.get(username=user_selected)
                Notification.objects.create(
                    user=user,
                    sender=request.user,
                    message=message
                )

            # ALL USERS
            elif role == "A":
                for user in users:
                    Notification.objects.create(
                        user=user,
                        sender=request.user,
                        message=message
                    )

            # ROLE
            elif role:
                profiles = Profile.objects.filter(role=role)
                for profile in profiles:
                    Notification.objects.create(
                        user=profile.user,
                        sender=request.user,
                        message=message
                    )

            return render(request, "notify.html", {
                "roles": roles,
                "Users": users,
                "notifications": notifications,
                "success": "Notifications sent!"
            })

    return render(request, "notify.html", {
        "roles": roles,
        "Users": users,
        "notifications": notifications
    })

@login_required
def notifications_view(request, today_str):
    notifications = Notification.objects.filter(user=request.user).order_by('-created_at')
    for notification in notifications:
        notification.read = True
        notification.save()
    return render(request, 'notifications.html', {'notifications': notifications})

@login_required
def mark_read_view(request, today_str, notification_id):
    notification = Notification.objects.get(id=notification_id, user=request.user)
    notification.read = True
    notification.save()
    return redirect('notifications', today_str=today_str)

def unread_count(request):
    if request.user.is_authenticated:
        count = Notification.objects.filter(user=request.user, read=False).count()
    else:
        count = 0

    return JsonResponse({"count": count})