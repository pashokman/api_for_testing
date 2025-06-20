from testing.classes.user import User
from testing.utils.expected_objects_generator.expected_user_object_generator import expected_user_obj

import pytest

pytestmark = pytest.mark.user


def test_create_user_with_username_none():
    user = User()
    user.user_obj["username"] = None
    response = user.create_user()

    expected_status_code = 422

    assert expected_status_code == response.status_code


def test_create_user_with_empty_username():
    user = User()
    user.user_obj["username"] = ""
    response = user.create_user()

    expected_status_code = 400
    expected_response_message = "Username field is required"

    assert expected_status_code == response.status_code
    assert expected_response_message == response.json()["detail"]


def test_create_user_without_username_field():
    user = User()
    del user.user_obj["username"]
    response = user.create_user()

    expected_status_code = 422

    assert expected_status_code == response.status_code


def test_create_user_with_password_none():
    user = User()
    user.user_obj["password"] = None
    response = user.create_user()

    expected_status_code = 422

    assert expected_status_code == response.status_code


def test_create_user_with_empty_password():
    user = User()
    user.user_obj["password"] = ""
    response = user.create_user()

    expected_status_code = 400
    expected_response_message = "Password field is required"

    assert expected_status_code == response.status_code
    assert expected_response_message == response.json()["detail"]


def test_create_user_without_password_field():
    user = User()
    del user.user_obj["password"]
    response = user.create_user()

    expected_status_code = 422

    assert expected_status_code == response.status_code


def test_create_user_with_email_none():
    user = User()
    user.user_obj["email"] = None
    response = user.create_user()

    expected_response = expected_user_obj(user)
    expected_response["email"] = None

    assert expected_response == response.json()


def test_create_user_with_empty_email():
    user = User()
    user.user_obj["email"] = ""
    response = user.create_user()

    expected_response = expected_user_obj(user)
    # Server changes email to None when user try to send an empty string
    expected_response["email"] = None

    assert expected_response == response.json()


def test_create_user_without_email_field():
    user = User()
    del user.user_obj["email"]
    response = user.create_user()

    expected_response = expected_user_obj(user)
    # Server changes email to None when user omit email field
    expected_response["email"] = None

    assert expected_response == response.json()


"""
There where a few tests to check if registration worked.
List of tests that also should be added on a real project for registration operation:
1. Min length of username, password.
2. Max length of username, password.
3. Puncruation symbols in username, password (Allowed - "_.-", not allowed - "@#!").
4. Latin letters (a-z, A-Z) and numbers in usernam, password.
5. Kyrilic letters.
6. Unique username.
7. Unique email (if describe in documentation).
8. Email validation checks (format - without @, different domains, already existed).
9. Password difficulty check (if it should be).
10. Password like number or boolean instead of string.
11. Additional fields check.
"""
