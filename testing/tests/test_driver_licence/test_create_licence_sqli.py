from app.config import SQLI_DATA
from testing.utils.generators.driver_licence_generator import generate_driver_licence

import pytest

pytestmark = [pytest.mark.licence, pytest.mark.xfail, pytest.mark.sqli]


def test_create_licence_sqli(setup):
    user, driver_licence = setup
    driver_licence.licence_obj = generate_driver_licence()
    driver_licence.licence_obj["licence_number"] = SQLI_DATA

    response = driver_licence.create_licence(user)
    expected_status_code = 401

    assert expected_status_code == response.status_code
