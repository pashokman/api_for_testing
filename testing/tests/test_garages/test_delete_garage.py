from testing.classes.garage import Garage
from testing.classes.user import User

import pytest

pytestmark = pytest.mark.garage


def test_delete_garage_successful(setup):
    user, house, garage = setup
    garage.create_garage(user)
    garage.delete_garage(user)

    response = garage.get_my_garages(user)
    expected_response = []

    assert expected_response == response.json()


def test_delete_other_user_garage(request):
    # Create 2 users
    user1 = User(request=request)
    user1.create_user()
    user1.auth()

    user2 = User(request=request)
    user2.create_user()
    user2.auth()

    # User1 creates a house
    garage1 = Garage(request=request)
    garage1.create_garage(user1)

    # User2 tries to delete house1, should get an error message
    garage2 = Garage(request=request)
    response = garage2.delete_garage(user2, garage1.garage_id)

    expected_status_code = 403
    expected_error_message = "Not allowed to delete this garage"
    assert response.status_code == expected_status_code
    assert response.json()["detail"] == expected_error_message
