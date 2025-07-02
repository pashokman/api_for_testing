from testing.utils.assertions.status_ok_and_schema_validation import status_ok_and_schema_validation_check
from testing.response_schemas.houses_get import HOUSE

import pytest


@pytest.mark.house
@pytest.mark.schema
def test_get_house_response_schema_validation(setup):
    user, house = setup
    house.create_house(user)

    expected_schema = HOUSE

    response = house.get_my_houses(user)
    status_ok_and_schema_validation_check(response=response, expected_schema=expected_schema)
