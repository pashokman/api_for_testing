import pytest


@pytest.mark.admin
@pytest.mark.garage
def test_admin_creates_and_gets_own_garage(setup_house_garage):
    admin, user1, user2, house, garage = setup_house_garage
    admin_garage = garage.create_garage(admin)
    admin_garage_id = admin_garage.json()["id"]

    all_garages = garage.get_my_garages(admin)
    all_garage_ids = [g["id"] for g in all_garages.json()]
    assert admin_garage_id in all_garage_ids


@pytest.mark.admin
@pytest.mark.house
@pytest.mark.garage
def test_admin_creates_and_gets_own_garage_related_to_house(setup_house_garage):
    admin, user1, user2, house, garage = setup_house_garage
    house.create_house(admin)
    admin_garage = garage.create_garage(admin, house.house_id)
    admin_garage_id = admin_garage.json()["id"]

    all_garages = garage.get_my_garages(admin)
    all_garage_ids = [g["id"] for g in all_garages.json()]
    assert admin_garage_id in all_garage_ids
