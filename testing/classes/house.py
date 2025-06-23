from testing.classes.base_api import BaseAPI
from testing.classes.user import User
from testing.utils.generators.house_generator import generate_house


class House(BaseAPI):

    def __init__(self, headers=None, request=None):
        super().__init__(headers=headers, request=request)
        self.house_obj = generate_house()
        self.house_id = None

    def create_house(self, user: User):
        response = None
        try:
            housetitle = self.house_obj.get("title")
            if self.logger:
                if housetitle is not None:
                    self.logger.info(f"Creating house: {housetitle}")
                else:
                    self.logger.info("Creating house without title field")
            response = self.post(endpoint="houses", json=self.house_obj, headers=user.headers)
            if response.status_code == 200:
                self.house_id = response.json()["id"]
                self.logger.info(f"Creating house: {housetitle}, response json: {response.json()}")
            else:
                self.logger.error(f"Creating house: {housetitle}, response json: {response.json()}")
        except Exception as e:
            self.logger.error(f"Error in create_house: {e}")
        finally:
            return response

    def get_my_houses(self, user: User):
        response = None
        try:
            if self.logger:
                self.logger.info(f"Getting all houses.")
            response = self.get(endpoint="houses", headers=user.headers)
            if response.status_code == 200:
                self.logger.info(f"Getting all houses, response json: {response.json()}")
            else:
                self.logger.error(f"Getting all houses, response json: {response.json()}")
        except Exception as e:
            self.logger.error(f"Error in get_my_houses: {e}")
        finally:
            return response

    def delete_house(self, user: User, house_id=None):
        # set house_id if you want to delete another current user house or another user house
        response = None
        try:
            housetitle = self.house_obj.get("title")
            if self.logger:
                if house_id is None:
                    house_id = self.house_id
                self.logger.info(f"Deleting house: {housetitle}")
            response = self.delete(endpoint=f"houses/{house_id}", headers=user.headers)
            if response.status_code == 200:
                self.logger.info(f"Deleting house: {housetitle}, response json: {response.json()}")
            else:
                self.logger.error(f"Deleting house: {housetitle}, response json: {response.json()}")
        except Exception as e:
            self.logger.error(f"Error in delete_house: {e}")
        finally:
            return response
