from testing.classes.base_api import BaseAPI
from testing.classes.user import User
from testing.utils.generators.driver_licence_generator import generate_driver_licence


class DriverLicence(BaseAPI):

    def __init__(self):
        super().__init__()
        self.licence_obj = generate_driver_licence()
        self.licence_id = None
        self.user_id = None

    def create_licence(self, user: User):
        result = self.post(endpoint="licences", json=self.licence_obj, headers=user.headers)
        if result.status_code == 200:
            self.licence_id = result.json()["id"]
        return result

    def get_my_licence(self, user: User):
        result = self.get(endpoint="licences", headers=user.headers)
        return result

    def delete_licence(self, user: User):
        result = self.delete(endpoint=f"licences", headers=user.headers)
        return result
