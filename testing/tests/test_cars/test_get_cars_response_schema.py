from testing.utils.assertions.status_ok_and_schema_validation import status_ok_and_schema_validation_check
from testing.response_schemas.cars_get import CARS_WITHOUT_GARAGE, CAR_WITH_GARAGE

import pytest

pytestmark = [pytest.mark.car, pytest.mark.schema]


def test_get_car_successful_without_garage_relation_response_schema(setup):
    user, house, garage, car = setup
    car.create_car(user)

    expected_schema = CARS_WITHOUT_GARAGE

    response = car.get_my_cars(user)
    status_ok_and_schema_validation_check(response=response, expected_schema=expected_schema)


def test_get_car_successful_with_garage_relation_response_schema(setup):
    user, house, garage, car = setup
    garage.create_garage(user)
    car.create_car(user, garage.garage_id)

    expected_schema = CAR_WITH_GARAGE

    response = car.get_my_cars(user)
    status_ok_and_schema_validation_check(response=response, expected_schema=expected_schema)
