from testing.classes.house import House
from testing.classes.user import User
from typing import Any


def expected_house_obj(house: House, user: User):
    """
    Add id field to previous generated house_object and append user_id into owner_ids list
    """

    new_house_obj: dict[str, Any] = house.house_obj
    new_house_obj["id"] = str(house.house_id)
    new_house_obj["owner_ids"] = []
    new_house_obj["owner_ids"].append(user.user_id)
    return new_house_obj
