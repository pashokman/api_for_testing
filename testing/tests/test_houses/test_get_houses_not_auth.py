from config import INCORRECT_BEARER_TOKEN

import pytest

pytestmark = pytest.mark.house


def test_get_house_without_authorization_header(setup):
    user, house = setup
    house.create_house(user)
    user.headers = {}
    response = house.get_my_houses(user)

    expected_status_code = 401
    assert expected_status_code == response.status_code


def test_get_house_with_incorrect_authorization_header(setup):
    user, house = setup
    house.create_house(user)
    user.headers = {"Authorization": f"Bearer {INCORRECT_BEARER_TOKEN}"}
    response = house.get_my_houses(user)

    expected_status_code = 401
    assert expected_status_code == response.status_code
