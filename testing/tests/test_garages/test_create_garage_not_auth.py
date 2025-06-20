from config import INCORRECT_BEARER_TOKEN
from testing.classes.garage import Garage
from testing.classes.user import User

import pytest

pytestmark = pytest.mark.garage


@pytest.fixture()
def setup_not_auth():
    user = User()
    user.create_user()
    garage = Garage()
    yield user, garage


def test_create_garage_without_authorization_header(setup_not_auth):
    user, garage = setup_not_auth
    response = garage.create_garage(user)

    expected_status_code = 401
    assert expected_status_code == response.status_code


def test_create_garage_with_incorrect_authorization_header(setup_not_auth):
    user, garage = setup_not_auth
    user.headers = {"Authorization": f"Bearer {INCORRECT_BEARER_TOKEN}"}
    response = garage.create_garage(user)

    expected_status_code = 401
    assert expected_status_code == response.status_code
