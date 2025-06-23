from testing.classes.house import House
from testing.classes.user import User
from testing.utils.expected_objects_generator.expected_house_object_generator import expected_house_obj

import pytest

pytestmark = pytest.mark.house


def test_get_house_successful(setup):
    user, house = setup
    house.create_house(user)
    response = house.get_my_houses(user)

    expected_response = expected_house_obj(house, user)
    assert expected_response in response.json()


def test_get_few_houses_successful(setup, request, houses_create_count=5):
    user, house = setup
    expected_response = []
    response = None
    for i in range(houses_create_count):
        house_name = f"house{i}"
        house_name = House(request=request)
        h = house_name.create_house(user)
        expected_response.append(h.json())
        response = house_name.get_my_houses(user)

    assert expected_response == response.json()


def test_get_other_user_houses(request):
    # Create 2 users
    user1 = User(request=request)
    user1.create_user()
    user1.auth()

    user2 = User(request=request)
    user2.create_user()
    user2.auth()

    # User1 creates a house
    house1 = House(request=request)
    house1.create_house(user1)

    # User2 tries to get house1, should get en empty response
    house2 = House(request=request)
    response = house2.get_my_houses(user2)

    expected_response = []
    assert expected_response == response.json()
