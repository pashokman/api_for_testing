from jsonschema import FormatChecker, validate

import pytest

pytestmark = [pytest.mark.garage, pytest.mark.schema]


def test_create_garage_successful_without_house_relation_response_schema(setup):
    user, house, garage = setup
    expected_schema = {
        "type": "object",
        "properties": {
            "title": {"type": "string"},
            "id": {"type": "string", "format": "uuid"},
            "house_id": {"type": "null"},
            "owners": {
                "type": "array",
                "items": {
                    "type": "object",
                    "properties": {
                        "username": {"type": "string"},
                        "email": {"type": "string", "format": "email"},
                        "id": {"type": "string", "format": "uuid"},
                        "is_admin": {"type": "boolean"},
                    },
                    "required": ["username", "email", "id", "is_admin"],
                },
            },
        },
        "required": ["title", "id", "house_id", "owners"],
    }

    response = garage.create_garage(user)
    assert response.ok, f"Unexpected status code: {response.status_code}, body: {response.text}"
    validate(instance=response.json(), schema=expected_schema, format_checker=FormatChecker())


def test_create_garage_successful_with_house_relation_response_schema(setup):
    user, house, garage = setup
    house.create_house(user)

    expected_schema = {
        "type": "object",
        "properties": {
            "title": {"type": "string"},
            "id": {"type": "string", "format": "uuid"},
            "house_id": {"type": "string", "format": "uuid"},
            "owners": {
                "type": "array",
                "items": {
                    "type": "object",
                    "properties": {
                        "username": {"type": "string"},
                        "email": {"type": "string", "format": "email"},
                        "id": {"type": "string", "format": "uuid"},
                        "is_admin": {"type": "boolean"},
                    },
                    "required": ["username", "email", "id", "is_admin"],
                },
            },
        },
        "required": ["title", "id", "house_id", "owners"],
    }

    response = garage.create_garage(user, house.house_id)
    assert response.ok, f"Unexpected status code: {response.status_code}, body: {response.text}"
    validate(instance=response.json(), schema=expected_schema, format_checker=FormatChecker())
