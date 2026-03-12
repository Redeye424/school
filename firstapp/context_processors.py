from .utils import get_daily_code

def today_str(request):
    return {
        "today_str": get_daily_code()
    }