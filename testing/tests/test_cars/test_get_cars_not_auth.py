from config import INCORRECT_BEARER_TOKEN


def test_get_car_without_authorization_header(setup_not_auth):
    user, house, garage, car = setup_not_auth
    car.create_car(user)
    user.headers = {}
    response = car.get_my_cars(user)

    expected_status_code = 401
    assert expected_status_code == response.status_code


def test_get_car_with_incorrect_authorization_header(setup_not_auth):
    user, house, garage, car = setup_not_auth
    car.create_car(user)
    user.headers = {"Authorization": f"Bearer {INCORRECT_BEARER_TOKEN}"}
    response = car.get_my_cars(user)

    expected_status_code = 401
    assert expected_status_code == response.status_code
