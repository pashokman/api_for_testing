from testing.classes.car import Car
from testing.classes.garage import Garage
from testing.classes.user import User
from typing import Any


def expected_car_obj(user: User, garage: Garage, car: Car):
    """
    Add an id field to previous generated car_object and set garage_id into garage_id field if a car is relative to a garage
    """

    new_car_obj: dict[str, Any] = car.car_obj
    new_car_obj["id"] = str(car.car_id)
    if garage.garage_id != None:
        new_car_obj["garage_id"] = str(garage.garage_id)
    else:
        new_car_obj["garage_id"] = None
    new_car_obj["owners"] = []
    new_car_obj["owners"].append(user.get_me().json())
    return new_car_obj
