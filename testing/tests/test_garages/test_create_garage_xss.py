from app.config import XSS_DATA
from testing.utils.generators.garage_generator import generate_garage

import pytest

pytestmark = [pytest.mark.garage, pytest.mark.xfail, pytest.mark.xss]


def test_create_garage_successful_without_house_relation_title_xss(setup):
    user, house, garage = setup

    garage.garage_obj = generate_garage()
    garage.garage_obj["title"] = XSS_DATA

    response = garage.create_garage(user)
    expected_status_code = 401

    assert expected_status_code == response.status_code


def test_create_garage_successful_with_house_relation_house_id_xss(setup):
    user, house, garage = setup

    garage.garage_obj = generate_garage()
    garage.garage_obj["house_id"] = XSS_DATA

    response = garage.create_garage(user)
    expected_status_code = 401

    assert expected_status_code == response.status_code
