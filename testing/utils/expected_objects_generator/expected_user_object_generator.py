from testing.classes.user import User
from typing import Any


def expected_user_obj(user: User):
    """
    Add id and is_admin fields to previous generated user_object and delete password field from it
    """

    new_user_obj: dict[str, Any] = user.user_obj
    del new_user_obj["password"]
    new_user_obj["id"] = str(user.user_id)
    new_user_obj["is_admin"] = False
    return new_user_obj
