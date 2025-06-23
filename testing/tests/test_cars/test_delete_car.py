from testing.classes.car import Car
from testing.classes.user import User

import pytest

pytestmark = pytest.mark.car


def test_delete_car_successful(setup):
    user, house, garage, car = setup
    car.create_car(user)
    car.delete_car(user)

    response = car.get_my_cars(user)
    expected_response = []

    assert expected_response == response.json()


def test_delete_other_user_cars(request):
    # Create 2 users
    user1 = User(request=request)
    user1.create_user()
    user1.auth()

    user2 = User(request=request)
    user2.create_user()
    user2.auth()

    # User1 creates a house
    car1 = Car(request=request)
    car1.create_car(user1)

    # User2 tries to delete house1, should get an error message
    car2 = Car(request=request)
    response = car2.delete_car(user2, car1.car_id)

    expected_status_code = 403
    expected_error_message = "Not allowed to delete this car"
    assert response.status_code == expected_status_code
    assert response.json()["detail"] == expected_error_message
