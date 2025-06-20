"""
If I delete the house, which is associated with the garage, which is associated with the car, the garage and the car should also be deleted.
"""

import pytest

pytestmark = [pytest.mark.car, pytest.mark.garage, pytest.mark.house]


def test_cascade_deletion_house_is_associated_to_garage_is_associated_to_car(setup):
    user, house, garage, car = setup
    house.create_house(user)
    garage.create_garage(user, house.house_id)
    car.create_car(user, garage.garage_id)
    house.delete_house(user)

    response = car.get_my_cars(user)
    expected_response = []

    assert expected_response == response.json()


def test_cascade_deletion_garage_is_not_associated_to_car(setup):
    user, house, garage, car = setup
    garage.create_garage(user)
    expected_response = car.create_car(user)
    garage.delete_garage(user)

    response = car.get_my_cars(user)

    assert expected_response.json() in response.json()
