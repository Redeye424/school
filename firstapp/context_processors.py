from .utils import get_daily_code, get_weekly_code, get_monthly_code
from .models import Notification

def today_str(request):
    return {
        "today_str": get_daily_code()
        }

def week_str(request):
    return {
        "week_str": get_weekly_code()
        }

def month_str(request):
    return {
        "month_str": get_monthly_code()
        }


def notifications_context(request):
    if request.user.is_authenticated:
        unread = Notification.objects.filter(user=request.user, read=False).count()
    else:
        unread = 0

    return {
        "unread_notifications": unread
    }
