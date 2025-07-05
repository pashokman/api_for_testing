from app.config import XSS_DATA
from testing.utils.generators.user_generator import generate_user

import pytest


pytestmark = [pytest.mark.user, pytest.mark.xfail, pytest.mark.xss]


def test_create_user_with_username_xss(setup_user):
    user = setup_user
    user.user_obj = generate_user(password_length=8)
    user.user_obj["username"] = XSS_DATA

    response = user.create_user()
    expected_status_code = 401

    assert expected_status_code == response.status_code


def test_create_user_with_password_xss(setup_user):
    user = setup_user
    user.user_obj = generate_user(password_length=8)
    user.user_obj["password"] = XSS_DATA

    response = user.create_user()
    expected_status_code = 401

    assert expected_status_code == response.status_code


def test_create_user_with_email_xss(setup_user):
    user = setup_user
    user.user_obj = generate_user(password_length=8)
    user.user_obj["email"] = XSS_DATA

    response = user.create_user()
    expected_status_code = 401

    assert expected_status_code == response.status_code
