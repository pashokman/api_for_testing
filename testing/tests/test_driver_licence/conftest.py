from testing.classes.driver_licence import DriverLicence
from testing.classes.user import User

import pytest


@pytest.fixture()
def setup(request):
    user = User(request=request)
    licence = DriverLicence(request=request)
    user.create_user()
    user.auth()
    yield user, licence


@pytest.fixture()
def setup_not_auth(request):
    user = User(request=request)
    license = DriverLicence(request=request)
    user.create_user()
    yield user, license
