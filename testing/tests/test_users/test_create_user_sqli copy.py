from app.config import SQLI_DATA
from testing.utils.generators.user_generator import generate_user

import pytest


pytestmark = [pytest.mark.user, pytest.mark.xfail, pytest.mark.sqli]


def test_create_user_with_username_sqli(setup_user):
    user = setup_user
    user.user_obj = generate_user(password_length=8)
    user.user_obj["username"] = SQLI_DATA

    response = user.create_user()
    expected_status_code = 401

    assert expected_status_code == response.status_code


def test_create_user_with_password_sqli(setup_user):
    user = setup_user
    user.user_obj = generate_user(password_length=8)
    user.user_obj["password"] = SQLI_DATA

    response = user.create_user()
    expected_status_code = 401

    assert expected_status_code == response.status_code


def test_create_user_with_email_sqli(setup_user):
    user = setup_user
    user.user_obj = generate_user(password_length=8)
    user.user_obj["email"] = SQLI_DATA

    response = user.create_user()
    expected_status_code = 401

    assert expected_status_code == response.status_code
