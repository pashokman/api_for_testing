from testing.utils.assertions.status_ok_and_schema_validation import status_ok_and_schema_validation_check
from testing.response_schemas.garage_create import GARAGE_WITH_HOUSE, GARAGE_WITHOUT_HOUSE

import pytest

pytestmark = [pytest.mark.garage, pytest.mark.schema]


def test_create_garage_successful_without_house_relation_response_schema(setup):
    user, house, garage = setup
    expected_schema = GARAGE_WITHOUT_HOUSE

    response = garage.create_garage(user)
    status_ok_and_schema_validation_check(response=response, expected_schema=expected_schema)


def test_create_garage_successful_with_house_relation_response_schema(setup):
    user, house, garage = setup
    house.create_house(user)

    expected_schema = GARAGE_WITH_HOUSE

    response = garage.create_garage(user, house.house_id)
    status_ok_and_schema_validation_check(response=response, expected_schema=expected_schema)
