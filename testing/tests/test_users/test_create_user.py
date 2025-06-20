from testing.classes.user import User
from testing.utils.expected_objects_generator.expected_user_object_generator import expected_user_obj

import pytest

pytestmark = pytest.mark.user


def test_create_user_with_valid_credentials():
    user = User()
    response = user.create_user()
    expected_response = expected_user_obj(user)

    assert expected_response == response.json()
