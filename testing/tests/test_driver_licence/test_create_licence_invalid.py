from testing.utils.expected_objects_generator.expected_user_object_generator import expected_user_obj

import pytest

pytestmark = pytest.mark.licence


def test_create_user_with_licence_number_none(setup):
    user, licence = setup
    licence.licence_obj["licence_number"] = None
    response = licence.create_licence(user)

    expected_status_code = 422

    assert expected_status_code == response.status_code


def test_create_user_with_empty_licence_number(setup):
    user, licence = setup
    licence.licence_obj["licence_number"] = ""
    response = licence.create_licence(user)

    expected_status_code = 422

    assert expected_status_code == response.status_code


def test_create_user_without_licence_number_field(setup):
    user, licence = setup
    del licence.licence_obj["licence_number"]
    response = licence.create_licence(user)

    expected_status_code = 422

    assert expected_status_code == response.status_code
