from testing.classes.garage import Garage
from testing.classes.user import User
from testing.utils.expected_objects_generator.expected_garage_object_generator import expected_garage_obj


def test_get_garage_without_house_relation_successful(setup):
    user, house, garage = setup
    garage.create_garage(user)
    response = garage.get_my_garages(user)

    expected_response = expected_garage_obj(user, house, garage)
    assert expected_response in response.json()


def test_get_garage_with_house_relation_successful(setup):
    user, house, garage = setup
    house.create_house(user)
    garage.create_garage(user, house.house_id)
    response = garage.get_my_garages(user)

    expected_response = expected_garage_obj(user, house, garage)
    assert expected_response in response.json()


def test_get_few_garages_successful(setup, garages_create_count=5):
    user, house, garage = setup
    expected_response = []
    response = None
    for i in range(garages_create_count):
        garage_name = f"garage{i}"
        garage_name = Garage()
        g = garage_name.create_garage(user)
        expected_response.append(g.json())
        response = garage_name.get_my_garages(user)

    assert expected_response == response.json()


def test_get_other_user_garages():
    # Create 2 users
    user1 = User()
    user1.create_user()
    user1.auth()

    user2 = User()
    user2.create_user()
    user2.auth()

    # User1 creates a garage
    garage1 = Garage()
    garage1.create_garage(user1)

    # User2 tries to get garage1, should get en empty response
    garage2 = Garage()
    response = garage2.get_my_garages(user2)

    expected_response = []
    assert expected_response == response.json()
