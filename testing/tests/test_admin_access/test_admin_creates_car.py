import pytest


@pytest.mark.admin
@pytest.mark.car
def test_admin_creates_and_gets_own_car(setup_house_garage_car):
    admin, user1, user2, house, garage, car = setup_house_garage_car
    admin_car = car.create_car(admin)
    admin_car_id = admin_car.json()["id"]

    all_cars = car.get_my_cars(admin)
    all_car_ids = [c["id"] for c in all_cars.json()]
    assert admin_car_id in all_car_ids


@pytest.mark.admin
@pytest.mark.house
@pytest.mark.garage
@pytest.mark.car
def test_admin_creates_and_gets_own_car_related_to_garage_related_to_house(setup_house_garage_car):
    admin, user1, user2, house, garage, car = setup_house_garage_car
    house.create_house(admin)
    garage.create_garage(admin, house.house_id)
    admin_car = car.create_car(admin, garage.garage_id)
    admin_car_id = admin_car.json()["id"]

    all_cars = car.get_my_cars(admin)
    all_car_ids = [c["id"] for c in all_cars.json()]
    assert admin_car_id in all_car_ids


@pytest.mark.admin
@pytest.mark.house
@pytest.mark.garage
@pytest.mark.car
def test_admin_creates_and_gets_own_car_related_to_garage_not_related_to_house(setup_house_garage_car):
    admin, user1, user2, house, garage, car = setup_house_garage_car
    garage.create_garage(admin)
    admin_car = car.create_car(admin, garage.garage_id)
    admin_car_id = admin_car.json()["id"]

    all_cars = car.get_my_cars(admin)
    all_car_ids = [c["id"] for c in all_cars.json()]
    assert admin_car_id in all_car_ids
