from testing.classes.car import Car
from testing.classes.user import User
from testing.utils.expected_objects_generator.expected_car_object_generator import expected_car_obj

import pytest

pytestmark = pytest.mark.car


def test_get_car_without_garage_relation_successful(setup):
    user, house, garage, car = setup
    car.create_car(user)
    response = car.get_my_cars(user)

    expected_response = expected_car_obj(user, garage, car)
    assert expected_response in response.json()


def test_get_car_with_garage_relation_successful(setup):
    user, house, garage, car = setup
    garage.create_garage(user)
    car.create_car(user, garage.garage_id)
    response = car.get_my_cars(user)

    expected_response = expected_car_obj(user, garage, car)
    assert expected_response in response.json()


def test_get_few_cars_successful(setup, cars_create_count=5):
    user, house, garage, car = setup
    expected_response = []
    response = None
    for i in range(cars_create_count):
        car_name = f"car{i}"
        car_name = Car()
        c = car_name.create_car(user)
        expected_response.append(c.json())
        response = car_name.get_my_cars(user)

    assert expected_response == response.json()


def test_get_other_user_cars():
    # Create 2 users
    user1 = User()
    user1.create_user()
    user1.auth()

    user2 = User()
    user2.create_user()
    user2.auth()

    # User1 creates a garage
    car1 = Car()
    car1.create_car(user1)

    # User2 tries to get garage1, should get en empty response
    car2 = Car()
    response = car2.get_my_cars(user2)

    expected_response = []
    assert expected_response == response.json()
