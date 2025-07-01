from jsonschema import FormatChecker, validate

import pytest

pytestmark = [pytest.mark.car, pytest.mark.schema]


def test_get_car_successful_without_garage_relation_response_schema(setup):
    user, house, garage, car = setup
    car.create_car(user)

    expected_schema = {
        "type": "array",
        "items": {
            "type": "object",
            "properties": {
                "model": {"type": "string"},
                "garage_id": {"type": "null"},
                "id": {"type": "string", "format": "uuid"},
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
            "required": ["model", "garage_id", "id", "owners"],
        },
    }

    response = car.get_my_cars(user)
    assert response.ok, f"Unexpected status code: {response.status_code}, body: {response.text}"
    validate(instance=response.json(), schema=expected_schema, format_checker=FormatChecker())


def test_get_car_successful_with_garage_relation_response_schema(setup):
    user, house, garage, car = setup
    garage.create_garage(user)
    car.create_car(user, garage.garage_id)

    expected_schema = {
        "type": "array",
        "items": {
            "type": "object",
            "properties": {
                "model": {"type": "string"},
                "garage_id": {"type": "string", "format": "uuid"},
                "id": {"type": "string", "format": "uuid"},
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
            "required": ["model", "garage_id", "id", "owners"],
        },
    }

    response = car.get_my_cars(user)
    assert response.ok, f"Unexpected status code: {response.status_code}, body: {response.text}"
    validate(instance=response.json(), schema=expected_schema, format_checker=FormatChecker())
