from app import get_user_by_phone_number


def test_connection(mongo):
    found_users = get_user_by_phone_number('8800')
    assert len(found_users) > 1
