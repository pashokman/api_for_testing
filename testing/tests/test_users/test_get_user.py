from testing.classes.user import User
from testing.utils.expected_objects_generator.expected_user_object_generator import expected_user_obj


def test_get_user_successfuly():
    user = User()
    user.create_user()
    user.auth()
    response = user.get_me()

    expected_response = expected_user_obj(user)

    assert expected_response == response.json()


def test_get_user_without_authorization_header():
    user = User()
    user.create_user()
    response = user.get_me()

    expected_status_code = 401
    assert expected_status_code == response.status_code


def test_get_user_with_incorrect_authorization_header():
    user = User()
    user.create_user()
    user.headers = {"Authorization": f"Bearer somesortoftoken123!@#"}
    response = user.get_me()

    expected_status_code = 401
    assert expected_status_code == response.status_code
