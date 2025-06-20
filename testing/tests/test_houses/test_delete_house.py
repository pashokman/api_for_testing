from testing.classes.house import House
from testing.classes.user import User

import pytest

pytestmark = pytest.mark.house


def test_delete_house_successful(setup):
    user, house = setup
    house.create_house(user)
    house.delete_house(user)

    response = house.get_my_houses(user)
    expected_response = []

    assert expected_response == response.json()


def test_delete_other_user_house():
    # Create 2 users
    user1 = User()
    user1.create_user()
    user1.auth()

    user2 = User()
    user2.create_user()
    user2.auth()

    # User1 creates a house
    house1 = House()
    house1.create_house(user1)

    # User2 tries to delete house1, should get an error message
    house2 = House()
    response = house2.delete_house(user2, house1.house_id)

    expected_error_message = "Not your house"
    assert expected_error_message == response.json()["detail"]
