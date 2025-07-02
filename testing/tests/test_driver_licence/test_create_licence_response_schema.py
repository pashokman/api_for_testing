from testing.utils.assertions.status_ok_and_schema_validation import status_ok_and_schema_validation_check
from testing.response_schemas.driver_licence import DRIVER_LICENCE
import pytest

pytestmark = [pytest.mark.licence, pytest.mark.schema]


def test_create_licence_response_schema(setup):
    user, driver_licence = setup
    expected_schema = DRIVER_LICENCE

    response = driver_licence.create_licence(user)
    status_ok_and_schema_validation_check(response=response, expected_schema=expected_schema)
