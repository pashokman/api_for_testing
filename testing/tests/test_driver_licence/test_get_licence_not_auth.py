from config import INCORRECT_BEARER_TOKEN

import pytest

pytestmark = pytest.mark.licence


def test_get_driver_licence_without_authorization_header(setup_not_auth):
    user, licence = setup_not_auth
    licence.create_licence(user)
    response = licence.get_my_licence(user)

    expected_status_code = 401
    assert expected_status_code == response.status_code


def test_get_driver_licence_with_incorrect_authorization_header(setup_not_auth):
    user, licence = setup_not_auth
    user.headers = {"Authorization": f"Bearer {INCORRECT_BEARER_TOKEN}"}
    licence.create_licence(user)
    response = licence.get_my_licence(user)

    expected_status_code = 401
    assert expected_status_code == response.status_code
