from dotenv import load_dotenv
from testing.classes.house import House
from testing.classes.user import User

import pytest
import os

load_dotenv()

INCORRECT_BEARER_TOKEN = os.environ.get("INCORRECT_BEARER_TOKEN")


@pytest.fixture()
def setup_not_auth():
    user = User()
    user.create_user()
    house = House()
    yield user, house


def test_create_house_without_authorization_header(setup_not_auth):
    user, house = setup_not_auth
    response = house.create_house(user)

    expected_status_code = 401
    assert expected_status_code == response.status_code


def test_create_house_with_incorrect_authorization_header(setup_not_auth):
    user, house = setup_not_auth
    user.headers = {"Authorization": f"Bearer {INCORRECT_BEARER_TOKEN}"}
    response = house.create_house(user)

    expected_status_code = 401
    assert expected_status_code == response.status_code
