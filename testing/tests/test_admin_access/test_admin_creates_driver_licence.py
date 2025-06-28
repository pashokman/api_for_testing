import pytest

from testing.utils.expected_objects_generator.expected_driver_licence_generator import expected_driver_licence_obj


@pytest.mark.admin
@pytest.mark.licence
@pytest.mark.xfail(strict=False)
def test_admin_creates_own_driver_licence(setup_driver_licence):
    admin, user1, user2, licence = setup_driver_licence
    response = licence.create_licence(admin)

    assert expected_driver_licence_obj(admin, licence) == response.json()

    licence.delete_licence(admin)
