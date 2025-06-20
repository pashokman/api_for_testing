from testing.classes.garage import Garage
from testing.classes.user import User


def test_delete_garage_successful(setup):
    user, house, garage = setup
    garage.create_garage(user)
    garage.delete_garage(user)

    response = garage.get_my_garages(user)
    expected_response = []

    assert expected_response == response.json()


def test_delete_other_user_garage():
    # Create 2 users
    user1 = User()
    user1.create_user()
    user1.auth()

    user2 = User()
    user2.create_user()
    user2.auth()

    # User1 creates a house
    garage1 = Garage()
    garage1.create_garage(user1)

    # User2 tries to delete house1, should get an error message
    garage2 = Garage()
    response = garage2.delete_garage(user2, garage1.garage_id)

    expected_error_message = "Not allowed to delete this garage"
    assert expected_error_message == response.json()["detail"]
