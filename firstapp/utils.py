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