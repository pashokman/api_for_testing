import pytest


def test_create_car_with_model_int(setup):
    user, house, garage, car = setup
    car.car_obj["model"] = 12645
    response = car.create_car(user)

    expected_status_code = 422

    assert expected_status_code == response.status_code


def test_create_car_with_garage_id_list(setup):
    user, house, garage, car = setup
    response = car.create_car(user, [1, "one"])

    expected_status_code = 422

    assert expected_status_code == response.status_code


def test_create_car_without_model(setup):
    user, house, garage, car = setup
    del car.car_obj["model"]
    response = car.create_car(user)

    expected_status_code = 422

    assert expected_status_code == response.status_code


@pytest.mark.xfail
def test_create_car_with_2_letters_model(setup):
    """
    This test should failed if API have this condition
    """
    user, house, garage, car = setup
    car.car_obj["model"] = "WB"
    response = car.create_car(user)

    expected_status_code = 422

    assert expected_status_code == response.status_code
