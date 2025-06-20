from testing.utils.expected_objects_generator.expected_car_object_generator import expected_car_obj


def test_create_car_successful_without_garage_relation(setup):
    user, house, garage, car = setup
    response = car.create_car(user)

    expected_status_code = 200
    expected_response = expected_car_obj(user=user, garage=garage, car=car)

    assert expected_status_code == response.status_code
    assert expected_response == response.json()


def test_create_car_successful_with_garage_relation(setup):
    user, house, garage, car = setup
    garage.create_garage(user)
    response = car.create_car(user, garage.garage_id)

    expected_status_code = 200
    expected_response = expected_car_obj(user=user, garage=garage, car=car)

    assert expected_status_code == response.status_code
    assert expected_response == response.json()
