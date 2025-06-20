from faker import Faker

fake = Faker()


def generate_house():
    title = fake.company()
    address = fake.address()

    house_obj = {"title": title, "address": address}

    return house_obj
