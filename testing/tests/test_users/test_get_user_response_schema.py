from testing.utils.assertions.status_ok_and_schema_validation import status_ok_and_schema_validation_check
from testing.response_schemas.user import USER

import pytest


@pytest.mark.user
@pytest.mark.schema
def test_get_user_response_schema_validation(setup_user_create):
    user = setup_user_create
    user.auth()

    expected_schema = USER

    response = user.get_me()
    status_ok_and_schema_validation_check(response=response, expected_schema=expected_schema)
