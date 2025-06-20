from testing.classes.base_api import BaseAPI
from testing.classes.user import User
from testing.utils.generators.car_generator import generate_car


class Car(BaseAPI):

    def __init__(self):
        super().__init__()
        self.car_obj = generate_car()
        self.car_id = None
        self.garage_id = None

    def create_car(self, user: User, garage_id=None):
        # set garage_id if a new car should be related to a garage
        self.car_obj["garage_id"] = garage_id
        result = self.post(endpoint="cars", json=self.car_obj, headers=user.headers)
        if result.status_code == 200:
            self.car_id = result.json()["id"]
        return result

    def get_my_cars(self, user: User):
        result = self.get(endpoint="cars", headers=user.headers)
        return result

    def delete_car(self, user: User, car_id=None):
        # set garage_id if you want to delete another current user garage or another user garage
        if car_id is None:
            car_id = self.car_id
        result = self.delete(endpoint=f"cars/{car_id}", headers=user.headers)
        return result
