import re
import argparse

from gateways.models import User
from gateways.mongo import Mongo


def get_user_by_phone_number(phone_number: str) -> list:
    phone_regex = re.compile(f'.*{phone_number}.*')
    return User.objects(phoneNumber=phone_regex).select_related()


if __name__ == "__main__":
    Mongo().connection
    parser = argparse.ArgumentParser()
    parser.add_argument('--phone', dest='phone')
    phone_number = parser.parse_args().phone
    found_users = get_user_by_phone_number(phone_number)
    print([user.name for user in found_users])
