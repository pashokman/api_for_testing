from config import INCORRECT_BEARER_TOKEN


def test_delete_car_without_authorization_header(setup):
    user, house, garage, car = setup
    car.create_car(user)
    user.headers = {}
    response = car.delete_car(user)

    expected_status_code = 401
    assert expected_status_code == response.status_code


def test_delete_car_with_incorrect_authorization_header(setup):
    user, house, garage, car = setup
    car.create_car(user)
    user.headers = {"Authorization": f"Bearer {INCORRECT_BEARER_TOKEN}"}
    response = car.delete_car(user)

    expected_status_code = 401
    assert expected_status_code == response.status_code
