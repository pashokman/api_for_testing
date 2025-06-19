from dotenv import load_dotenv

import os

load_dotenv()

INCORRECT_BEARER_TOKEN = os.environ.get("INCORRECT_BEARER_TOKEN")


def test_delete_house_without_authorization_header(setup):
    house, user = setup
    house.create_house(user)
    user.headers = {}
    response = house.delete_house(user)

    expected_status_code = 401
    assert expected_status_code == response.status_code


def test_delete_house_with_incorrect_authorization_header(setup):
    house, user = setup
    house.create_house(user)
    user.headers = {"Authorization": f"Bearer {INCORRECT_BEARER_TOKEN}"}
    response = house.delete_house(user)

    expected_status_code = 401
    assert expected_status_code == response.status_code
