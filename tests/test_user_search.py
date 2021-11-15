from app import get_user_by_phone_number


def test_search_user_by_phone_number(users_with_phone_numbers_mock):
    found_users = get_user_by_phone_number('555')
    assert len(found_users) > 0
