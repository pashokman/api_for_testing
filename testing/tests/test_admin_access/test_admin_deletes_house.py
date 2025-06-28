import pytest

pytestmark = [pytest.mark.admin, pytest.mark.house]


def test_admin_deletes_own_house(setup_house):
    admin, user1, user2, house = setup_house
    admin_house = house.create_house(admin)
    admin_house_id = admin_house.json()["id"]

    house.delete_house(admin)

    all_houses = house.get_my_houses(admin)
    all_house_ids = [h["id"] for h in all_houses.json()]
    assert admin_house_id not in all_house_ids


def test_admin_deletes_user_house(setup_house):
    admin, user1, user2, house = setup_house
    user_house = house.create_house(user1)
    user_house_id = user_house.json()["id"]

    house.delete_house(admin)

    all_houses = house.get_my_houses(admin)
    all_house_ids = [h["id"] for h in all_houses.json()]
    assert user_house_id not in all_house_ids
