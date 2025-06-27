import pytest


@pytest.mark.admin
@pytest.mark.house
def test_2_users_created_houses_admin_get_all_houses(setup_house):
    admin, user1, user2, house = setup_house
    h1 = house.create_house(user1)
    h2 = house.create_house(user1)

    h3 = house.create_house(user2)
    h4 = house.create_house(user2)

    user1_and_user2_houses = [x.json() for x in [h1, h2, h3, h4]]

    all_houses = house.get_my_houses(admin)
    assert all(elem in all_houses.json() for elem in user1_and_user2_houses)
