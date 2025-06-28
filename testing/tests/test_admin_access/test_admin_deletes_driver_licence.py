import pytest


@pytest.mark.admin
@pytest.mark.licence
@pytest.mark.xfail(strict=False)
def test_admin_deletes_own_driver_licence(setup_driver_licence):
    admin, user1, user2, licence = setup_driver_licence
    licence.create_licence(admin)
    licence.delete_licence(admin)
    response = licence.get_my_licence(admin)

    expected_status_code = 404
    expected_error_message = "Driver licence not found"

    assert expected_status_code == response.status_code
    assert expected_error_message == response.json()["detail"]
