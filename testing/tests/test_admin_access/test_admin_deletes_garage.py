import pytest

pytestmark = [pytest.mark.admin, pytest.mark.garage]


def test_admin_deletes_own_garage(setup_house_garage):
    admin, user1, user2, house, garage = setup_house_garage
    admin_garage = garage.create_garage(admin)
    garage.delete_garage(admin)
    all_garages = garage.get_my_garages(admin)
    assert admin_garage.json() not in all_garages.json()


@pytest.mark.house
def test_admin_deletes_own_garage_related_to_house(setup_house_garage):
    admin, user1, user2, house, garage = setup_house_garage
    h = house.create_house(admin)
    house_id = h.json().get("id")
    admin_garage = garage.create_garage(admin, house_id)
    garage.delete_garage(admin)
    all_garages = garage.get_my_garages(admin)
    assert admin_garage.json() not in all_garages.json()


def test_admin_deletes_user_garage(setup_house_garage):
    admin, user1, user2, house, garage = setup_house_garage
    user_garage = garage.create_garage(user1)
    garage.delete_garage(admin)
    all_garages = garage.get_my_garages(admin)
    assert user_garage.json() not in all_garages.json()
