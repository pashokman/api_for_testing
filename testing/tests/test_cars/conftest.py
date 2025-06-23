from testing.classes.car import Car
from testing.classes.garage import Garage
from testing.classes.house import House
from testing.classes.user import User

import pytest


@pytest.fixture()
def setup(request):
    user = User(request=request)
    house = House(request=request)
    garage = Garage(request=request)
    car = Car(request=request)
    user.create_user()
    user.auth()
    yield user, house, garage, car


@pytest.fixture()
def setup_not_auth(request):
    user = User(request=request)
    house = House(request=request)
    garage = Garage(request=request)
    car = Car(request=request)
    user.create_user()
    yield user, house, garage, car
