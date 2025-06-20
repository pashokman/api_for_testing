from faker import Faker

fake = Faker()


def generate_driver_licence():
    licence_number = fake.license_plate()

    house_obj = {"licence_number": licence_number}

    return house_obj
