import pytest


@pytest.mark.admin
@pytest.mark.house
@pytest.mark.garage
def test_2_users_created_garages_admin_get_all_garages(setup_house_garage):
    # user1 creats house and related garage, user2 creates only garage
    admin, user1, user2, house, garage = setup_house_garage

    h1 = house.create_house(user1)
    g1 = garage.create_garage(user1, house_id=h1.json().get("id"))
    g2 = garage.create_garage(user2)

    g1_id = g1.json()["id"]
    g2_id = g2.json()["id"]
    all_garages = garage.get_my_garages(admin)
    all_garage_ids = [g["id"] for g in all_garages.json()]

    assert {g1_id, g2_id}.issubset(set(all_garage_ids))
