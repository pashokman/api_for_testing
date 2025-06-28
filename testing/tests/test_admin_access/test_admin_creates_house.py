import pytest


@pytest.mark.admin
@pytest.mark.house
def test_admin_creates_and_gets_house(setup_house):
    admin, user1, user2, house = setup_house
    admin_house = house.create_house(admin)
    admin_house_id = admin_house.json()["id"]

    all_houses = house.get_my_houses(admin)
    all_house_ids = [h["id"] for h in all_houses.json()]
    assert admin_house_id in all_house_ids
