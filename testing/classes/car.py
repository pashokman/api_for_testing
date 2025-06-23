from testing.classes.base_api import BaseAPI
from testing.classes.user import User
from testing.utils.generators.car_generator import generate_car


class Car(BaseAPI):

    def __init__(self, headers=None, request=None):
        super().__init__(headers=headers, request=request)
        self.car_obj = generate_car()
        self.car_id = None
        self.garage_id = None

    def create_car(self, user: User, garage_id=None):
        # set garage_id if a new car should be related to a garage
        response = None
        try:
            self.car_obj["garage_id"] = garage_id
            car_model = self.car_obj.get("model")
            if self.logger:
                if car_model is not None:
                    self.logger.info(f"Creating car: {car_model}")
                else:
                    self.logger.info("Creating car without model field")
            response = self.post(endpoint="cars", json=self.car_obj, headers=user.headers)
            if response.status_code == 200:
                self.car_id = response.json()["id"]
                self.logger.info(f"Creating car: {car_model}, response json: {response.json()}")
            else:
                self.logger.error(f"Creating car: {car_model}, response json: {response.json()}")
        except Exception as e:
            self.logger.error(f"Error in create_car: {e}")
        finally:
            return response

    def get_my_cars(self, user: User):
        response = None
        try:
            if self.logger:
                self.logger.info(f"Getting all cars.")
            response = self.get(endpoint="cars", headers=user.headers)
            if response.status_code == 200:
                self.logger.info(f"Getting all cars, response json: {response.json()}")
            else:
                self.logger.error(f"Getting all cars, response json: {response.json()}")
        except Exception as e:
            self.logger.error(f"Error in get_my_cars: {e}")
        finally:
            return response

    def delete_car(self, user: User, car_id=None):
        # set garage_id if you want to delete another current user garage or another user garage
        response = None
        try:
            car_model = self.car_obj.get("model")
            if self.logger:
                if car_id is None:
                    car_id = self.car_id
                self.logger.info(f"Deleting car: {car_model}")
            response = self.delete(endpoint=f"cars/{car_id}", headers=user.headers)
            if response.status_code == 200:
                self.logger.info(f"Deleting car: {car_model}, response json: {response.json()}")
            else:
                self.logger.error(f"Deleting car: {car_model}, response json: {response.json()}")
        except Exception as e:
            self.logger.error(f"Error in delete_car: {e}")
        finally:
            return response
