from app.config import INCORRECT_BEARER_TOKEN

import pytest

pytestmark = pytest.mark.garage


def test_delete_garage_without_authorization_header(setup):
    user, house, garage = setup
    garage.create_garage(user)
    user.headers = {}
    response = garage.delete_garage(user)

    expected_status_code = 401
    assert expected_status_code == response.status_code


def test_delete_garage_with_incorrect_authorization_header(setup):
    user, house, garage = setup
    garage.create_garage(user)
    user.headers = {"Authorization": f"Bearer {INCORRECT_BEARER_TOKEN}"}
    response = garage.delete_garage(user)

    expected_status_code = 401
    assert expected_status_code == response.status_code
