from app.config import INCORRECT_BEARER_TOKEN

import pytest

pytestmark = pytest.mark.garage


def test_get_garage_without_authorization_header(setup_not_auth):
    user, house, garage = setup_not_auth
    garage.create_garage(user)
    user.headers = {}
    response = garage.get_my_garages(user)

    expected_status_code = 401
    assert expected_status_code == response.status_code


def test_get_garage_with_incorrect_authorization_header(setup_not_auth):
    user, house, garage = setup_not_auth
    garage.create_garage(user)
    user.headers = {"Authorization": f"Bearer {INCORRECT_BEARER_TOKEN}"}
    response = garage.get_my_garages(user)

    expected_status_code = 401
    assert expected_status_code == response.status_code
