from jsonschema import FormatChecker, validate


def status_ok_and_schema_validation_check(response, expected_schema):
    assert response.ok, f"Unexpected status code: {response.status_code}, body: {response.text}"
    validate(instance=response.json(), schema=expected_schema, format_checker=FormatChecker())
