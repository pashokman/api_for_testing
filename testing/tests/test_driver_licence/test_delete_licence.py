import pytest

pytestmark = pytest.mark.licence


def test_delete_driver_licence_successfuly(setup):
    user, licence = setup
    licence.create_licence(user)
    licence.delete_licence(user)

    response = licence.get_my_licence(user)

    expected_status_code = 404
    expected_error_message = "Driver licence not found"

    assert expected_status_code == response.status_code
    assert expected_error_message == response.json()["detail"]
