from testing.classes.house import House
from testing.classes.user import User

import pytest


@pytest.fixture()
def setup(request):
    user = User(request=request)
    house = House(request=request)
    user.create_user()
    user.auth()
    yield user, house


@pytest.fixture()
def setup_not_auth(request):
    user = User(request=request)
    house = House(request=request)
    user.create_user()
    yield user, house
