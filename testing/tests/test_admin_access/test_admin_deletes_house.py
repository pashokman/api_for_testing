import pytest

pytestmark = [pytest.mark.admin, pytest.mark.house]


def test_admin_deletes_own_house(setup_house):
    admin, user1, user2, house = setup_house
    admin_house = house.create_house(admin)
    house.delete_house(admin)
    all_houses = house.get_my_houses(admin)
    assert admin_house.json() not in all_houses.json()


def test_admin_deletes_user_house(setup_house):
    admin, user1, user2, house = setup_house
    user_house = house.create_house(user1)
    house.delete_house(admin)
    all_houses = house.get_my_houses(admin)
    assert user_house.json() not in all_houses.json()
