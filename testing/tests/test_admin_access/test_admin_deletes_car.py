import pytest

pytestmark = [pytest.mark.admin, pytest.mark.car]


def test_admin_deletes_own_car(setup_house_garage_car):
    admin, user1, user2, house, garage, car = setup_house_garage_car
    admin_car = car.create_car(admin)
    admin_car_id = admin_car.json()["id"]

    car.delete_car(admin)

    all_cars = car.get_my_cars(admin)
    all_car_ids = [c["id"] for c in all_cars.json()]
    assert admin_car_id not in all_car_ids


@pytest.mark.garage
def test_admin_deletes_own_car_related_to_garage(setup_house_garage_car):
    admin, user1, user2, house, garage, car = setup_house_garage_car
    g = garage.create_garage(admin)
    garage_id = g.json().get("id")
    admin_car = car.create_car(admin, garage_id)
    admin_car_id = admin_car.json()["id"]

    car.delete_car(admin)

    all_cars = car.get_my_cars(admin)
    all_car_ids = [c["id"] for c in all_cars.json()]
    assert admin_car_id not in all_car_ids


@pytest.mark.house
@pytest.mark.garage
def test_admin_deletes_own_car_related_to_garage_related_to_house(setup_house_garage_car):
    admin, user1, user2, house, garage, car = setup_house_garage_car
    h = house.create_house(admin)
    house_id = h.json().get("id")
    g = garage.create_garage(admin, house_id)
    garage_id = g.json().get("id")
    admin_car = car.create_car(admin, garage_id)
    admin_car_id = admin_car.json()["id"]

    car.delete_car(admin)

    all_cars = car.get_my_cars(admin)
    all_car_ids = [c["id"] for c in all_cars.json()]
    assert admin_car_id not in all_car_ids


def test_admin_deletes_user_car(setup_house_garage_car):
    admin, user1, user2, house, garage, car = setup_house_garage_car
    user_car = car.create_car(user1)
    car_id = user_car.json()["id"]

    car.delete_car(admin, car_id)

    all_cars = car.get_my_cars(admin)
    all_car_ids = [c["id"] for c in all_cars.json()]
    assert car_id not in all_car_ids
