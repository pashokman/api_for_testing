from jsonschema import FormatChecker, validate

import pytest


@pytest.mark.house
@pytest.mark.schema
def test_create_house_response_schema_validation(setup):
    user, house = setup
    expected_schema = {
        "type": "object",
        "properties": {
            "title": {"type": "string"},
            "address": {"type": "string"},
            "id": {"type": "string", "format": "uuid"},
            "owner_ids": {"type": "array", "items": {"type": "string", "format": "uuid"}},
        },
        "required": ["title", "address", "id", "owner_ids"],
    }

    response = house.create_house(user)
    assert response.ok, f"Unexpected status code: {response.status_code}, body: {response.text}"
    validate(instance=response.json(), schema=expected_schema, format_checker=FormatChecker())
