from testing.classes.car import Car
from testing.classes.user import User


def test_delete_car_successful(setup):
    user, house, garage, car = setup
    car.create_car(user)
    car.delete_car(user)

    response = car.get_my_cars(user)
    expected_response = []

    assert expected_response == response.json()


def test_delete_other_user_cars():
    # Create 2 users
    user1 = User()
    user1.create_user()
    user1.auth()

    user2 = User()
    user2.create_user()
    user2.auth()

    # User1 creates a house
    car1 = Car()
    car1.create_car(user1)

    # User2 tries to delete house1, should get an error message
    car2 = Car()
    response = car2.delete_car(user2, car1.car_id)

    expected_error_message = "Not allowed to delete this car"
    assert expected_error_message == response.json()["detail"]
