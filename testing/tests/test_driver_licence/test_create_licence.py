from testing.utils.expected_objects_generator.expected_driver_licence_generator import expected_driver_licence_obj

import pytest

pytestmark = pytest.mark.licence


def test_create_licence_with_valid_credentials(setup):
    user, driver_licence = setup
    response = driver_licence.create_licence(user)
    expected_response = expected_driver_licence_obj(user, driver_licence)

    assert expected_response == response.json()
