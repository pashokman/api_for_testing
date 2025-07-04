from testing.utils.assertions.status_ok_and_schema_validation import status_ok_and_schema_validation_check
from testing.response_schemas.car_create import CAR_WITH_GARAGE, CAR_WITHOUT_GARAGE

import pytest

pytestmark = [pytest.mark.car, pytest.mark.schema]


def test_create_car_successful_without_garage_relation_response_schema(setup):
    user, house, garage, car = setup

    expected_schema = CAR_WITHOUT_GARAGE

    response = car.create_car(user)
    status_ok_and_schema_validation_check(response=response, expected_schema=expected_schema)


def test_create_car_successful_with_garage_relation_response_schema(setup):
    user, house, garage, car = setup
    garage.create_garage(user)

    expected_schema = CAR_WITH_GARAGE

    response = car.create_car(user, garage.garage_id)
    status_ok_and_schema_validation_check(response=response, expected_schema=expected_schema)
