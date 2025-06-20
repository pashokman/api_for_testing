from faker import Faker

fake = Faker()


def generate_car(garage_id=None):
    model = fake.company()

    car_obj = {"model": model, "garage_id": garage_id}

    return car_obj
