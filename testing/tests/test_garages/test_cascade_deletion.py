"""
If I delete the house, which is associated with the garage, the garage should also be deleted.
"""

import pytest

pytestmark = [pytest.mark.garage, pytest.mark.house]


def test_cascade_deletion_house_is_associated_to_garage(setup):
    user, house, garage = setup
    house.create_house(user)
    garage.create_garage(user, house.house_id)
    house.delete_house(user)

    response = garage.get_my_garages(user)
    expected_response = []

    assert expected_response == response.json()


def test_cascade_deletion_house_is_not_associated_to_garage(setup):
    user, house, garage = setup
    house.create_house(user)
    expected_response = garage.create_garage(user)
    house.delete_house(user)

    response = garage.get_my_garages(user)

    assert expected_response.json() in response.json()
