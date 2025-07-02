from testing.utils.assertions.status_ok_and_schema_validation import status_ok_and_schema_validation_check
from testing.response_schemas.house_create import HOUSE

import pytest


@pytest.mark.house
@pytest.mark.schema
def test_create_house_response_schema_validation(setup):
    user, house = setup
    expected_schema = HOUSE

    response = house.create_house(user)
    status_ok_and_schema_validation_check(response=response, expected_schema=expected_schema)
