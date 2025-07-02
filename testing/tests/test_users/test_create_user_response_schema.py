from testing.utils.assertions.status_ok_and_schema_validation import status_ok_and_schema_validation_check
from testing.response_schemas.user import USER

import pytest


@pytest.mark.user
@pytest.mark.schema
def test_create_user_response_schema_validation(setup_user):
    user = setup_user

    expected_schema = USER

    response = user.create_user()
    status_ok_and_schema_validation_check(response=response, expected_schema=expected_schema)
