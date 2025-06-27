import pytest


@pytest.mark.admin
@pytest.mark.house
def test_admin_creates_and_gets_house(setup_house):
    admin, user1, user2, house = setup_house
    admin_house = house.create_house(admin)

    all_houses = house.get_my_houses(admin)
    assert admin_house.json() in all_houses.json()
