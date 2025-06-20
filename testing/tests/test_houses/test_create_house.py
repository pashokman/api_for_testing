from testing.utils.expected_objects_generator.expected_house_object_generator import expected_house_obj

import pytest

pytestmark = pytest.mark.house


def test_create_house_successful(setup):
    user, house = setup
    response = house.create_house(user)

    expected_status_code = 200
    expected_response = expected_house_obj(house=house, user=user)

    assert expected_status_code == response.status_code
    assert expected_response == response.json()
