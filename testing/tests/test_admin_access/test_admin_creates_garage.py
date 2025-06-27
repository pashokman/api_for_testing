import pytest


@pytest.mark.admin
@pytest.mark.garage
def test_admin_creates_and_gets_own_garage(setup_house_garage):
    admin, user1, user2, house, garage = setup_house_garage
    admin_garage = garage.create_garage(admin)

    all_garages = garage.get_my_garages(admin)
    assert admin_garage.json() in all_garages.json()


@pytest.mark.admin
@pytest.mark.house
@pytest.mark.garage
def test_admin_creates_and_gets_own_garage_related_to_house(setup_house_garage):
    admin, user1, user2, house, garage = setup_house_garage
    house.create_house(admin)
    admin_garage = garage.create_garage(admin, house.house_id)

    all_garages = garage.get_my_garages(admin)
    assert admin_garage.json() in all_garages.json()
