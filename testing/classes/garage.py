from testing.classes.base_api import BaseAPI
from testing.classes.user import User
from testing.utils.generators.garage_generator import generate_garage


class Garage(BaseAPI):

    def __init__(self, headers=None, request=None):
        super().__init__(headers=headers, request=request)
        self.garage_obj = None
        self.garage_id = None
        self.house_id = None

    def create_garage(self, user: User, house_id=None):
        # set house_id if a new garage should be related to a house
        response = None
        try:
            if self.garage_obj is None:
                self.garage_obj = generate_garage()
            self.garage_obj["house_id"] = house_id
            garage_title = self.garage_obj.get("title")
            if self.logger:
                if garage_title is not None:
                    self.logger.info(f"Creating garage: {garage_title}")
                else:
                    self.logger.info("Creating garage without title field")
            response = self.post(endpoint="garages", json=self.garage_obj, headers=user.headers)
            if response.status_code == 200:
                self.garage_id = response.json()["id"]
                self.logger.info(f"Creating garage: {garage_title}, response json: {response.json()}")
            else:
                self.logger.error(f"Creating garage: {garage_title}, response json: {response.json()}")
        except Exception as e:
            self.logger.error(f"Error in create_garage: {e}")
        finally:
            return response

    def get_my_garages(self, user: User):
        response = None
        try:
            if self.logger:
                self.logger.info(f"Getting all garages.")
            response = self.get(endpoint="garages", headers=user.headers)
            if response.status_code == 200:
                self.logger.info(f"Getting all garages, response json: {response.json()}")
            else:
                self.logger.error(f"Getting all garages, response json: {response.json()}")
        except Exception as e:
            self.logger.error(f"Error in get_my_garages: {e}")
        finally:
            return response

    def delete_garage(self, user: User, garage_id=None):
        # set garage_id if you want to delete another current user garage or another user garage
        response = None
        try:
            if self.logger:
                if garage_id is None:
                    garage_id = self.garage_id
                self.logger.info(f"Deleting garage with id: {garage_id}")
            response = self.delete(endpoint=f"garages/{garage_id}", headers=user.headers)
            if response.status_code == 200:
                self.logger.info(f"Deleting garage with id: {garage_id}, response json: {response.json()}")
            else:
                self.logger.error(f"Deleting garage with id: {garage_id}, response json: {response.json()}")
        except Exception as e:
            self.logger.error(f"Error in delete_garage: {e}")
        finally:
            return response
