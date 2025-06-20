from config import INCORRECT_BEARER_TOKEN


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
