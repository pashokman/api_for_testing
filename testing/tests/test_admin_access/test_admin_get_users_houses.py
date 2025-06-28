import pytest


@pytest.mark.admin
@pytest.mark.house
def test_2_users_created_houses_admin_get_all_houses(setup_house):
    admin, user1, user2, house = setup_house
    h1 = house.create_house(user1)
    h2 = house.create_house(user1)

    h3 = house.create_house(user2)
    h4 = house.create_house(user2)

    h1_id = h1.json()["id"]
    h2_id = h2.json()["id"]
    h3_id = h3.json()["id"]
    h4_id = h4.json()["id"]
    all_houses = house.get_my_houses(admin)
    all_house_ids = [h["id"] for h in all_houses.json()]

    assert {h1_id, h2_id, h3_id, h4_id}.issubset(set(all_house_ids))
