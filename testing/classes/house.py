from testing.classes.base_api import BaseAPI
from testing.classes.user import User
from testing.utils.generators.house_generator import generate_house


class House(BaseAPI):

    def __init__(self):
        super().__init__()
        self.house_obj = generate_house()
        self.house_id = None

    def create_house(self, user: User):
        result = self.post(endpoint="houses", json=self.house_obj, headers=user.headers)
        if result.status_code == 200:
            self.house_id = result.json()["id"]
        return result

    def get_my_houses(self, user: User):
        result = self.get(endpoint="houses", headers=user.headers)
        return result

    def delete_house(self, user: User, house_id=None):
        if house_id is None:
            house_id = self.house_id
        result = self.delete(endpoint=f"houses/{house_id}", headers=user.headers)
        return result
