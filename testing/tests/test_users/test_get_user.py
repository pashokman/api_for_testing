from testing.utils.expected_objects_generator.expected_user_object_generator import expected_user_obj

import pytest

pytestmark = pytest.mark.user


def test_get_user_successfuly(setup):
    user = setup
    user.auth()
    response = user.get_me()

    expected_response = expected_user_obj(user)

    assert expected_response == response.json()
