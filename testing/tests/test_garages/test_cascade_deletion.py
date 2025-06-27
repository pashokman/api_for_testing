"""
If I delete the house, which is associated with the garage, the garage should also be deleted.
"""

import pytest

pytestmark = [pytest.mark.garage, pytest.mark.house]


def test_cascade_deletion_house_is_associated_to_garage(setup):
    user, house, garage = setup
    house.create_house(user)
    user_garage = garage.create_garage(user, house.house_id)
    house.delete_house(user)

    garages = garage.get_my_garages(user).json()
    updated_garage = next((g for g in garages if g["id"] == user_garage.json()["id"]), None)
    assert updated_garage is not None
    assert updated_garage["house_id"] is None


def test_cascade_deletion_house_is_not_associated_to_garage(setup):
    user, house, garage = setup
    house.create_house(user)
    expected_response = garage.create_garage(user)
    house.delete_house(user)

    response = garage.get_my_garages(user)

    assert expected_response.json() in response.json()
