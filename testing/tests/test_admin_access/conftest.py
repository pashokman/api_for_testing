import pytest

from testing.classes.admin import Admin
from testing.classes.car import Car
from testing.classes.driver_licence import DriverLicence
from testing.classes.garage import Garage
from testing.classes.house import House
from testing.classes.user import User


@pytest.fixture()
def setup_driver_licence(request):
    admin = Admin(request=request)
    user1 = User(request=request)
    user2 = User(request=request)
    licence = DriverLicence(request=request)
    admin.auth()
    user1.create_user()
    user2.create_user()
    user1.auth()
    user2.auth()
    yield admin, user1, user2, licence


@pytest.fixture()
def setup_house(request):
    admin = Admin(request=request)
    user1 = User(request=request)
    user2 = User(request=request)
    house = House(request=request)
    admin.auth()
    user1.create_user()
    user2.create_user()
    user1.auth()
    user2.auth()
    yield admin, user1, user2, house


@pytest.fixture()
def setup_house_garage(request):
    admin = Admin(request=request)
    user1 = User(request=request)
    user2 = User(request=request)
    house = House(request=request)
    garage = Garage(request=request)
    admin.auth()
    user1.create_user()
    user2.create_user()
    user1.auth()
    user2.auth()
    yield admin, user1, user2, house, garage


@pytest.fixture()
def setup_house_garage_car(request):
    admin = Admin(request=request)
    user1 = User(request=request)
    user2 = User(request=request)
    house = House(request=request)
    garage = Garage(request=request)
    car = Car(request=request)
    admin.auth()
    user1.create_user()
    user2.create_user()
    user1.auth()
    user2.auth()
    yield admin, user1, user2, house, garage, car


@pytest.fixture()
def setup_house_garage_car_licence(request):
    admin = Admin(request=request)
    user1 = User(request=request)
    user2 = User(request=request)
    house = House(request=request)
    garage = Garage(request=request)
    car = Car(request=request)
    license = DriverLicence(request=request)
    admin.auth()
    user1.create_user()
    user2.create_user()
    user1.auth()
    user2.auth()
    yield admin, user1, user2, house, garage, car, license
