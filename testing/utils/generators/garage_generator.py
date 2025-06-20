from faker import Faker

fake = Faker()


def generate_garage(house_id=None):
    title = fake.company()

    garage_obj = {"title": title, "house_id": house_id}

    return garage_obj
