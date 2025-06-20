from testing.classes.driver_licence import DriverLicence
from testing.classes.user import User

import pytest


@pytest.fixture()
def setup():
    user = User()
    user.create_user()
    user.auth()
    licence = DriverLicence()
    yield user, licence


@pytest.fixture()
def setup_not_auth():
    user = User()
    user.create_user()
    license = DriverLicence()
    yield user, license
