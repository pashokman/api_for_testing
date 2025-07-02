from testing.utils.assertions.status_ok_and_schema_validation import status_ok_and_schema_validation_check
from testing.response_schemas.garages_get import GARAGES_WITHOUT_HOUSE, GARAGES_WITH_HOUSE

import pytest

pytestmark = [pytest.mark.garage, pytest.mark.schema]


def test_get_garage_without_house_relation_successful_response_schema(setup):
    user, house, garage = setup
    garage.create_garage(user)

    expected_schema = GARAGES_WITHOUT_HOUSE

    response = garage.get_my_garages(user)
    status_ok_and_schema_validation_check(response=response, expected_schema=expected_schema)


def test_get_garage_with_house_relation_successful_response_schema(setup):
    user, house, garage = setup
    house.create_house(user)
    garage.create_garage(user, house.house_id)

    expected_schema = GARAGES_WITH_HOUSE

    response = garage.get_my_garages(user)
    status_ok_and_schema_validation_check(response=response, expected_schema=expected_schema)
