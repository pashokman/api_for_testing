import pytest


def test_create_house_with_title_int(setup):
    house, user = setup
    house.house_obj["title"] = 12645
    response = house.create_house(user)

    expected_status_code = 422

    assert expected_status_code == response.status_code


def test_create_house_with_address_list(setup):
    house, user = setup
    house.house_obj["address"] = [1, "one"]
    response = house.create_house(user)

    expected_status_code = 422

    assert expected_status_code == response.status_code


def test_create_house_without_title(setup):
    house, user = setup
    del house.house_obj["title"]
    response = house.create_house(user)

    expected_status_code = 422

    assert expected_status_code == response.status_code


def test_create_house_without_address(setup):
    house, user = setup
    del house.house_obj["address"]
    response = house.create_house(user)

    expected_status_code = 422

    assert expected_status_code == response.status_code


@pytest.mark.xfail
def test_create_house_with_2_letters_title(setup):
    """
    This test should failed if API have this condition
    """
    house, user = setup
    house.house_obj["title"] = "WB"
    response = house.create_house(user)

    expected_status_code = 422

    assert expected_status_code == response.status_code


@pytest.mark.xfail
def test_create_house_with_50_letters_address(setup):
    """
    This test should failed if API have this condition
    """
    house, user = setup
    house.house_obj["address"] = 50 * "t"
    response = house.create_house(user)

    expected_status_code = 422

    assert expected_status_code == response.status_code
