from faker import Faker

fake = Faker()


def generate_house():
    title = fake.company()
    address = fake.address()

    house_obj = {"title": f"{title}", "address": f"{address}"}

    return house_obj
