from testing.utils.generators.garage_generator import generate_garage

import pytest

pytestmark = pytest.mark.garage


def test_create_garage_with_title_int(setup):
    user, house, garage = setup
    garage.garage_obj = generate_garage()
    garage.garage_obj["title"] = 12645
    response = garage.create_garage(user)

    expected_status_code = 422

    assert expected_status_code == response.status_code


def test_create_garage_with_house_id_list(setup):
    user, house, garage = setup
    response = garage.create_garage(user, [1, "one"])

    expected_status_code = 422

    assert expected_status_code == response.status_code


def test_create_garage_without_title(setup):
    user, house, garage = setup
    garage.garage_obj = generate_garage()
    del garage.garage_obj["title"]
    response = garage.create_garage(user)

    expected_status_code = 422

    assert expected_status_code == response.status_code


@pytest.mark.xfail
def test_create_garage_with_2_letters_title(setup):
    """
    This test should failed if API have this condition
    """
    user, house, garage = setup
    garage.garage_obj = generate_garage()
    garage.garage_obj["title"] = "WB"
    response = garage.create_garage(user)

    expected_status_code = 422

    assert expected_status_code == response.status_code
