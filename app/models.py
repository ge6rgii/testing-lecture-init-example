from mongoengine import Document
from mongoengine.fields import StringField


class User(Document):
    meta = {'collection': 'testing_lecture'}

    name = StringField()
    surname = StringField()
    phoneNumber = StringField()
    workPhoneNumber = StringField()
