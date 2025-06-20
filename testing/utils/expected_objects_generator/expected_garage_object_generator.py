from testing.classes.garage import Garage
from testing.classes.house import House
from testing.classes.user import User
from typing import Any


def expected_garage_obj(user: User, house: House, garage: Garage):
    """
    Add an id field to previous generated garage_object and set house_id into house_id field if a garage is relative to a house
    """

    new_garage_obj: dict[str, Any] = garage.garage_obj
    new_garage_obj["id"] = str(garage.garage_id)
    if house.house_id != None:
        new_garage_obj["house_id"] = str(house.house_id)
    else:
        new_garage_obj["house_id"] = None
    new_garage_obj["owners"] = []
    new_garage_obj["owners"].append(user.get_me().json())
    return new_garage_obj
