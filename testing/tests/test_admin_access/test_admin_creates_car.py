import pytest


@pytest.mark.admin
@pytest.mark.car
def test_admin_creates_and_gets_own_car(setup_house_garage_car):
    admin, user1, user2, house, garage, car = setup_house_garage_car
    admin_car = car.create_car(admin)

    all_cars = car.get_my_cars(admin)
    assert admin_car.json() in all_cars.json()


@pytest.mark.admin
@pytest.mark.house
@pytest.mark.garage
@pytest.mark.car
def test_admin_creates_and_gets_own_car_related_to_garage_related_to_house(setup_house_garage_car):
    admin, user1, user2, house, garage, car = setup_house_garage_car
    house.create_house(admin)
    garage.create_garage(admin, house.house_id)
    admin_car = car.create_car(admin, garage.garage_id)

    all_cars = car.get_my_cars(admin)
    assert admin_car.json() in all_cars.json()


@pytest.mark.admin
@pytest.mark.house
@pytest.mark.garage
@pytest.mark.car
def test_admin_creates_and_gets_own_car_related_to_garage_not_related_to_house(setup_house_garage_car):
    admin, user1, user2, house, garage, car = setup_house_garage_car
    garage.create_garage(admin)
    admin_car = car.create_car(admin, garage.garage_id)

    all_cars = car.get_my_cars(admin)
    assert admin_car.json() in all_cars.json()
