from testing.utils.expected_objects_generator.expected_driver_licence_generator import expected_driver_licence_obj

import pytest

pytestmark = pytest.mark.licence


def test_get_driver_licence_successfuly(setup):
    user, licence = setup
    licence.create_licence(user)
    response = licence.get_my_licence(user)

    expected_response = expected_driver_licence_obj(user, licence)

    assert expected_response == response.json()
