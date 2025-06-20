from testing.classes.base_api import BaseAPI
from testing.classes.user import User
from testing.utils.generators.garage_generator import generate_garage


class Garage(BaseAPI):

    def __init__(self):
        super().__init__()
        self.garage_obj = generate_garage()
        self.garage_id = None
        self.house_id = None

    def create_garage(self, user: User, house_id=None):
        # set house_id if a new garage should be related to a house
        self.garage_obj["house_id"] = house_id
        result = self.post(endpoint="garages", json=self.garage_obj, headers=user.headers)
        if result.status_code == 200:
            self.garage_id = result.json()["id"]
        return result

    def get_my_garages(self, user: User):
        result = self.get(endpoint="garages", headers=user.headers)
        return result

    def delete_garage(self, user: User, garage_id=None):
        # set garage_id if you want to delete another current user garage or another user garage
        if garage_id is None:
            garage_id = self.garage_id
        result = self.delete(endpoint=f"garages/{garage_id}", headers=user.headers)
        return result
