from pytest import fixture
from mongoengine import connect

from gateways.models import User


@fixture
def mongo_mock():
    return connect('mongoenginetest', host='mongomock://localhost')


@fixture
def users_with_phone_numbers_mock(mongo_mock):
    user_tosin = User(
        name='Tosin',
        surname='Abasi',
        phoneNumber='88005553535',
        workPhoneNumber='88003590000'
    )
    user_linus = User(
        name='Linus',
        surname='Torvalds',
        phoneNumber='8(800)1110000',
        workPhoneNumber='+79991112233'
    )
    user_tosin.save()
    user_linus.save()

    return mongo_mock
