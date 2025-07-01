from jsonschema import validate, FormatChecker

import pytest

pytestmark = [pytest.mark.garage, pytest.mark.schema]


def test_get_garage_without_house_relation_successful_response_schema(setup):
    user, house, garage = setup
    garage.create_garage(user)

    expected_schema = {
        "type": "array",
        "items": {
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
        },
    }

    response = garage.get_my_garages(user)
    assert response.ok, f"Unexpected status code: {response.status_code}, body: {response.text}"
    validate(instance=response.json(), schema=expected_schema, format_checker=FormatChecker())


def test_get_garage_with_house_relation_successful_response_schema(setup):
    user, house, garage = setup
    house.create_house(user)
    garage.create_garage(user, house.house_id)

    expected_schema = {
        "type": "array",
        "items": {
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
        },
    }

    response = garage.get_my_garages(user)
    assert response.ok, f"Unexpected status code: {response.status_code}, body: {response.text}"
    validate(instance=response.json(), schema=expected_schema, format_checker=FormatChecker())
