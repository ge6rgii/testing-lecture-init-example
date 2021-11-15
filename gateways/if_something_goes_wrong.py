from mongoengine import Q
from models import User


def get_user_by_phone_number_ex1(phone_number: str):
    return User.objects(phoneNumber__contains=phone_number).select_related()


def get_user_by_phone_number_ex2(phone_number: str):
    return User.objects(
        Q(phoneNumber__contains=phone_number) | Q(workPhoneNumber__contains=phone_number)
        ).select_related()


"""
db.testing_lecture.insertOne({"name": "Linus", "surname": "Torvalds", "phoneNumber": "8(800)1110000", "workPhoneNumber": "+79991112233"})
db.testing_lecture.insertOne({"name": "Tosin", "surname": "Abasi", "phoneNumber": "88005553535", "workPhoneNumber": "88003590000"})

{
	"_id" : ObjectId("61919da77d749c25333e607f"),
	"name" : "Tosin",
	"surname" : "Abasi",
	"phoneNumber" : "88005553535",
	"workPhoneNumber" : "88003590000"
}
{
	"_id" : ObjectId("6191b6bbe8673a7f375d096c"),
	"name" : "Linus",
	"surname" : "Torvalds",
	"phoneNumber" : "8(800)1110000",
	"workPhoneNumber" : "+79991112233"
}
"""