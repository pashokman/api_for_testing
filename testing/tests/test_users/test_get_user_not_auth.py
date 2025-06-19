from dotenv import load_dotenv
from testing.classes.user import User

import pytest
import os

load_dotenv()

INCORRECT_BEARER_TOKEN = os.environ.get("INCORRECT_BEARER_TOKEN")


@pytest.fixture()
def setup():
    user = User()
    user.create_user()
    yield user


def test_get_user_without_authorization_header(setup):
    user = setup
    response = user.get_me()

    expected_status_code = 401
    assert expected_status_code == response.status_code


def test_get_user_with_incorrect_authorization_header(setup):
    user = setup
    user.headers = {"Authorization": f"Bearer {INCORRECT_BEARER_TOKEN}"}
    response = user.get_me()

    expected_status_code = 401
    assert expected_status_code == response.status_code
