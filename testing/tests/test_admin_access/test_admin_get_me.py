import pytest


@pytest.mark.admin
def test_admin_get_me(setup_house):
    admin, user1, user2, house = setup_house
    response = admin.get_me()
    expected_obj = {"username": "admin", "email": "admin@example.com", "id": response.json()["id"], "is_admin": True}

    assert expected_obj == response.json()
