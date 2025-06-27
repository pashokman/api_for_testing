"""
If I delete the house, which is associated with the garage, which is associated with the car, the garage and the car should also be deleted.
"""

import pytest

pytestmark = [pytest.mark.car, pytest.mark.garage, pytest.mark.house]


def test_cascade_deletion_house_is_associated_to_garage_is_associated_to_car(setup):
    user, house, garage, car = setup
    user_house = house.create_house(user)
    user_garage = garage.create_garage(user, house.house_id)
    user_car = car.create_car(user, garage.garage_id)

    house.delete_house(user)

    # response = car.get_my_cars(user)
    # expected_response = []

    # assert expected_response == response.json()

    user_houses = house.get_my_houses(user)
    assert user_house.json() not in user_houses.json()

    user_garages = garage.get_my_garages(user).json()
    updated_garage = next((g for g in user_garages if g["id"] == user_garage.json()["id"]), None)
    assert updated_garage is not None
    assert updated_garage["house_id"] is None

    user_cars = car.get_my_cars(user).json()
    updated_car = next((c for c in user_cars if c["id"] == user_car.json()["id"]), None)
    assert updated_car is not None
    assert updated_car["garage_id"] is None


def test_cascade_deletion_garage_is_not_associated_to_car(setup):
    user, house, garage, car = setup
    garage.create_garage(user)
    expected_response = car.create_car(user)
    garage.delete_garage(user)

    response = car.get_my_cars(user)

    assert expected_response.json() in response.json()
