from app import get_user_by_phone_number


def test_search_user_by_phone_number(mongo):
    found_users = get_user_by_phone_number('555')
    assert len(found_users) > 1
