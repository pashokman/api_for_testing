from testing.classes.user import User

import pytest


@pytest.fixture()
def setup_user_create(request):
    user = User(request=request)
    user.create_user()
    yield user


@pytest.fixture()
def setup_user(request):
    user = User(request=request)
    yield user
