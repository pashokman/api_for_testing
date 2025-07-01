from jsonschema import validate

import pytest


@pytest.mark.user
@pytest.mark.schema
def test_get_user_response_schema_validation(setup_user_create):
    user = setup_user_create
    user.auth()

    expected_schema = {
        "type": "object",
        "properties": {
            "username": {"type": "string"},
            "email": {"type": "string"},
            "id": {"type": "string", "format": "uuid"},
            "is_admin": {"type": "boolean"},
        },
        "required": ["username", "email", "id", "is_admin"],
    }

    response = user.get_me()

    validate(instance=response.json(), schema=expected_schema)
