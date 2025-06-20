from testing.utils.expected_objects_generator.expected_garage_object_generator import expected_garage_obj


def test_create_garage_successful_without_house_relation(setup):
    user, house, garage = setup
    response = garage.create_garage(user)

    expected_status_code = 200
    expected_response = expected_garage_obj(user=user, house=house, garage=garage)

    assert expected_status_code == response.status_code
    assert expected_response == response.json()


def test_create_garage_successful_with_house_relation(setup):
    user, house, garage = setup
    house.create_house(user)
    response = garage.create_garage(user, house.house_id)

    expected_status_code = 200
    expected_response = expected_garage_obj(user=user, house=house, garage=garage)

    assert expected_status_code == response.status_code
    assert expected_response == response.json()
