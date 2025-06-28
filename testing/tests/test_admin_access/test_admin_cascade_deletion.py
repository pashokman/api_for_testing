import pytest


@pytest.mark.admin
@pytest.mark.house
@pytest.mark.garage
@pytest.mark.car
def test_admin_deletes_house_related_to_garage_related_to_car(setup_house_garage_car):
    admin, user1, user2, house, garage, car = setup_house_garage_car
    admin_house = house.create_house(admin)
    admin_garage = garage.create_garage(admin, house.house_id)
    admin_car = car.create_car(admin, garage.garage_id)
    admin_house_id = admin_house.json()["id"]
    admin_garage_id = admin_garage.json()["id"]
    admin_car_id = admin_car.json()["id"]

    house.delete_house(admin)

    admin_houses = house.get_my_houses(admin)
    admin_house_ids = [h["id"] for h in admin_houses.json()]
    assert admin_house_id not in admin_house_ids

    admin_garages = garage.get_my_garages(admin).json()
    updated_garage = next((g for g in admin_garages if g["id"] == admin_garage.json()["id"]), None)
    assert updated_garage is not None
    assert updated_garage["house_id"] is None

    admin_cars = car.get_my_cars(admin).json()
    updated_car = next((c for c in admin_cars if c["id"] == admin_car.json()["id"]), None)
    assert updated_car is not None
    assert updated_car["garage_id"] is None
