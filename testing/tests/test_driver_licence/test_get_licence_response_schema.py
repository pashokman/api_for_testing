from jsonschema import FormatChecker, validate
import pytest

pytestmark = [pytest.mark.licence, pytest.mark.schema]


def test_get_licence_response_schema(setup):
    user, licence = setup
    licence.create_licence(user)
    expected_schema = {
        "type": "object",
        "properties": {
            "licence_number": {"type": "string"},
            "user_id": {"type": "string", "format": "uuid"},
            "id": {"type": "string", "format": "uuid"},
        },
        "required": ["licence_number", "user_id", "id"],
    }

    response = licence.get_my_licence(user)
    assert response.ok, f"Unexpected status code: {response.status_code}, body: {response.text}"
    validate(instance=response.json(), schema=expected_schema, format_checker=FormatChecker())
