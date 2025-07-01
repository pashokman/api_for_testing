from jsonschema import validate
import pytest


@pytest.mark.user
@pytest.mark.schema
def test_create_user_response_schema_validation(setup_user):
    user = setup_user
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

    response = user.create_user()
    validate(instance=response.json(), schema=expected_schema)
