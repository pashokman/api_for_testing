from testing.classes.driver_licence import DriverLicence
from testing.classes.user import User
from typing import Any


def expected_driver_licence_obj(user: User, driver_licence: DriverLicence):
    """
    Add id and user_id fields to previous generated driver_licence_object
    """

    new_dl_obj: dict[str, Any] = driver_licence.licence_obj
    new_dl_obj["id"] = str(driver_licence.licence_id)
    new_dl_obj["user_id"] = str(user.user_id)
    return new_dl_obj
