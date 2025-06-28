import pytest

pytestmark = [pytest.mark.admin, pytest.mark.garage]


def test_admin_deletes_own_garage(setup_house_garage):
    admin, user1, user2, house, garage = setup_house_garage
    admin_garage = garage.create_garage(admin)
    admin_garage_id = admin_garage.json()["id"]

    garage.delete_garage(admin)

    all_garages = garage.get_my_garages(admin)
    all_garage_ids = [g["id"] for g in all_garages.json()]
    assert admin_garage_id not in all_garage_ids


@pytest.mark.house
def test_admin_deletes_own_garage_related_to_house(setup_house_garage):
    admin, user1, user2, house, garage = setup_house_garage
    h = house.create_house(admin)
    house_id = h.json().get("id")
    admin_garage = garage.create_garage(admin, house_id)
    admin_garage_id = admin_garage.json()["id"]

    garage.delete_garage(admin)

    all_garages = garage.get_my_garages(admin)
    all_garage_ids = [g["id"] for g in all_garages.json()]
    assert admin_garage_id not in all_garage_ids


def test_admin_deletes_user_garage(setup_house_garage):
    admin, user1, user2, house, garage = setup_house_garage
    user_garage = garage.create_garage(user1)
    user_garage_id = user_garage.json()["id"]

    garage.delete_garage(admin)
    all_garages = garage.get_my_garages(admin)
    all_garage_ids = [g["id"] for g in all_garages.json()]
    assert user_garage_id not in all_garage_ids
