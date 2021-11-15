from mongoengine import Q
from models import User


def get_user_by_phone_number(phone_number: str):
    return User.objects(phoneNumber__contains=phone_number).select_related()

def get_user_by_phone_number(phone_number: str):
    return User.objects(
        Q(phoneNumber__contains=phone_number) | Q(workPhoneNumber__contains=phone_number)
        ).select_related()
