from app.config import XSS_DATA
from testing.utils.generators.house_generator import generate_house

import pytest

pytestmark = [pytest.mark.house, pytest.mark.xfail, pytest.mark.xss]


def test_create_house_with_title_xss(setup):
    user, house = setup
    house.house_obj = generate_house()
    house.house_obj["title"] = XSS_DATA

    response = house.create_house(user)
    expected_status_code = 401

    assert expected_status_code == response.status_code


def test_create_house_with_address_xss(setup):
    user, house = setup
    house.house_obj = generate_house()
    house.house_obj["address"] = XSS_DATA

    response = house.create_house(user)
    expected_status_code = 401

    assert expected_status_code == response.status_code
