import re
from .models import User


def get_user_by_phone_number(phone_number: str):
    phone_regex = re.compile(f'.*{phone_number}.*')
    return User.objects(phoneNumber=phone_regex).select_related()
