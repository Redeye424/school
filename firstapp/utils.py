import hashlib
from django.conf import settings
from datetime import date

def get_daily_code():
    today = date.today().isoformat()

    # combine date with secret key
    raw = today + settings.SECRET_KEY

    # hash it
    hash_value = hashlib.sha256(raw.encode()).hexdigest()

    # convert part of hash into a 6 digit number
    code = int(hash_value, 16) % 1000000

    return str(code).zfill(6)

def get_monthly_code():
    month = str(date.today().month)
    raw_month = month + settings.SECRET_KEY
    hash_value_month = hashlib.sha256(raw_month.encode()).hexdigest()
    code_month = int(hash_value_month, 16) % 1000000
    return str(code_month).zfill(6)

def get_weekly_code():
    week = str(date.today().isocalendar().week)
    raw_week = week + settings.SECRET_KEY
    hash_value_week = hashlib.sha256(raw_week.encode()).hexdigest()
    code_week = int(hash_value_week, 16) % 1000000
    return str(code_week).zfill(6)

