import pytest


@pytest.mark.admin
@pytest.mark.garage
@pytest.mark.car
def test_2_users_created_cars_admin_get_all_cars(setup_house_garage_car):
    # user1 creats house and related garage, user2 creates only garage
    admin, user1, user2, house, garage, car = setup_house_garage_car

    g1 = garage.create_garage(user1)
    c1 = car.create_car(user1, garage_id=g1.json().get("id"))
    c2 = car.create_car(user2)

    c1_id = c1.json()["id"]
    c2_id = c2.json()["id"]
    all_cars = car.get_my_cars(admin)
    all_car_ids = [c["id"] for c in all_cars.json()]

    assert {c1_id, c2_id}.issubset(set(all_car_ids))
