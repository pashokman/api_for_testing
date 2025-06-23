from testing.classes.base_api import BaseAPI
from testing.classes.user import User
from testing.utils.generators.driver_licence_generator import generate_driver_licence


class DriverLicence(BaseAPI):

    def __init__(self, headers=None, request=None):
        super().__init__(headers=headers, request=request)
        self.licence_obj = generate_driver_licence()
        self.licence_id = None
        self.user_id = None

    def create_licence(self, user: User):
        response = None
        try:
            user_name = user.user_obj.get("username")
            if self.logger:
                if self.licence_obj.get("licence_number") is not None:
                    self.logger.info(f"Creating driver licence for user: {user_name}")
                else:
                    self.logger.info(f"Creating driver licence for user: {user_name} without licence_number field")
            response = self.post(endpoint="licences", json=self.licence_obj, headers=user.headers)
            if response.status_code == 200:
                self.licence_id = response.json()["id"]
                self.logger.info(f"Creating driver licence for user: {user_name}, response json: {response.json()}")
            else:
                self.logger.error(f"Creating driver licence for user: {user_name}, response json: {response.json()}")
        except Exception as e:
            self.logger.error(f"Error in create_licence: {e}")
        finally:
            return response

    def get_my_licence(self, user: User):
        response = None
        try:
            user_name = user.user_obj.get("username")
            if self.logger:
                self.logger.info(f"Getting driver licence for user: {user_name}.")
            response = self.get(endpoint="licences", headers=user.headers)
            if response.status_code == 200:
                self.logger.info(f"Getting driver licence for user: {user_name}, response json: {response.json()}")
            else:
                self.logger.error(f"Getting driver licence for user: {user_name}, response json: {response.json()}")
        except Exception as e:
            self.logger.error(f"Error in get_my_licence: {e}")
        finally:
            return response

    def delete_licence(self, user: User):
        response = None
        try:
            user_name = user.user_obj.get("username")
            if self.logger:
                self.logger.info(f"Deleting driver licence for user: {user_name},")
            response = self.delete(endpoint=f"licences", headers=user.headers)
            if response.status_code == 200:
                self.logger.info(f"Deleting driver licence for user: {user_name}, response json: {response.json()}")
            else:
                self.logger.error(f"Deleting driver licence for user: {user_name}, response json: {response.json()}")
        except Exception as e:
            self.logger.error(f"Error in delete_licence: {e}")
        finally:
            return response
