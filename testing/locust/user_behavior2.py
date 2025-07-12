import json
import os

from locust.exception import StopUser

from testing.utils.generators.car_generator import generate_car
from testing.utils.generators.driver_licence_generator import generate_driver_licence
from testing.utils.generators.garage_generator import generate_garage
from testing.utils.generators.user_generator import generate_user
from testing.utils.generators.house_generator import generate_house
from testing.utils.logs.locust_main_logger import Logger
from testing.utils.logs.locust_response_err_log import response_err_log

from testing.locust.user_configuration1 import UserConfiguration


# clear log files before each locust run from the command line
for log_file in ["locust_main.log", "locust_only_error.log"]:
    if os.path.exists(log_file):
        with open(log_file, "w"):
            pass


# connect logging
log = Logger(log_name="UserBehavior")
UserLog = log.get_logger()
UserLog.propagate = False


class UserBehavior(UserConfiguration):
    # class describes user behavior - all API methods that user can use

    def create_user(self):
        self.user_obj = generate_user(password_length=8)
        with self.client.post(
            "/users/register", data=json.dumps(self.user_obj), name="001. Create user", catch_response=True
        ) as response:
            if response.status_code == 200:
                self.user_id = response.json()["id"]
                UserLog.info(f'User created, id - "{self.user_id}"')
            elif response.status_code == 401 and "Username already taken" in response.text:
                UserLog.warning("Username already taken. Stopping this user.")
                raise StopUser()
            else:
                response_err_log(response)
                raise StopUser()

    def auth_user(self):
        json_data = {"username": f"{self.user_obj.get('username')}", "password": f"{self.user_obj.get('password')}"}
        with self.client.post(
            "/auth/login", data=json.dumps(json_data), name="002. Authorize user", catch_response=True
        ) as response:
            if response.status_code == 200:
                self.user_token = response.json()["access_token"]
                self.headers = {"Authorization": f"Bearer {self.user_token}"}
                UserLog.info(f'User authorized, id - "{self.user_id}", token - "{self.user_token}"')
            else:
                response_err_log(response)
                raise StopUser()

    def create_houses(self):
        for i in range(self.house_count):
            with self.client.post(
                "/houses",
                data=json.dumps(generate_house()),
                name="003. Create house",
                headers=self.headers,
                catch_response=True,
            ) as response:
                if response.status_code == 200:
                    house_id = response.json()["id"]
                    self.house_ids.append(house_id)
                    UserLog.info(f'House {i} created, house_id - "{house_id}", token - "{self.user_token}"')
                else:
                    response_err_log(response)

    def get_houses(self):
        with self.client.get(
            "/houses",
            name="004. Get houses",
            headers=self.headers,
            catch_response=True,
        ) as response:
            if response.status_code == 200:
                UserLog.info(f'Got houses - {response.text}, token - "{self.user_token}"')
            else:
                response_err_log(response)

    def create_garages(self):
        """
        Create garages.

        Args:
            total_garage_count (int): The total number of garages to create. Default = 4.
            house1_related_garage_count (int): How many garages should be created with house1 relation. Default = 1.
            house2_related_garage_count (int): How many garages should be created with house2 relation. Default = 1.

        Returns:
            None
        """
        if self.house1_related_garage_count + self.house2_related_garage_count > self.total_garage_count:
            raise ValueError(
                f"Invalid configuration: total_garage_count ({self.total_garage_count}) < house1_related_garage_count ({self.house1_related_garage_count}) + house2_related_garage_count ({self.house2_related_garage_count})"
            )

        def create_garage_request(index: int, house_id: str | None, relation: str):
            garage = generate_garage()
            if house_id:
                garage["house_id"] = house_id

            with self.client.post(
                "/garages",
                data=json.dumps(garage),
                name=f"005. Create garage {index} related to {relation}",
                headers=self.headers,
                catch_response=True,
            ) as response:
                if response.status_code == 200:
                    garage_id = response.json()["id"]
                    self.garage_ids.append(garage_id)
                    UserLog.info(
                        f'Garage {index} created, garage_id = {garage_id}, house_id - "{garage["house_id"]}", token - "{self.user_token}"'
                    )
                else:
                    response_err_log(response)

        for i in range(self.house1_related_garage_count):
            create_garage_request(i, self.house_ids[0], "house1")

        for j in range(self.house2_related_garage_count):
            create_garage_request(j, self.house_ids[1], "house2")

        rest = self.total_garage_count - self.house1_related_garage_count - self.house2_related_garage_count
        for k in range(rest):
            create_garage_request(k, None, "no house")

    def get_garages(self):
        with self.client.get(
            "/garages",
            name="006. Get garages",
            headers=self.headers,
            catch_response=True,
        ) as response:
            if response.status_code == 200:
                UserLog.info(f'Got garages - {response.text}, token - "{self.user_token}"')
            else:
                response_err_log(response)

    def create_cars(self):
        """
        Create cars.

        Args:
            total_car_count (int): The total number of cars to create. Default = 4.
            garage1_related_car_count (int): How many cars should be created with garage1 relation. Default = 1.
            garage2_related_car_count (int): How many cars should be created with garage2 relation. Default = 1.

        Returns:
            None
        """
        if self.garage1_related_car_count + self.garage2_related_car_count > self.total_car_count:
            raise ValueError(
                f"Invalid configuration: total_car_count ({self.total_car_count}) < garage1_related_car_count ({self.garage1_related_car_count}) + garage2_related_car_count ({self.garage2_related_car_count})"
            )

        def create_car_request(index: int, garage_id: str | None, relation: str):
            car = generate_car()
            if garage_id:
                car["garage_id"] = garage_id

            with self.client.post(
                "/cars",
                data=json.dumps(car),
                name=f"007. Create car {index} related to {relation}",
                headers=self.headers,
                catch_response=True,
            ) as response:
                if response.status_code == 200:
                    car_id = response.json()["id"]
                    self.car_ids.append(car_id)
                    UserLog.info(
                        f'Car {index} created, car_id = {car_id}, garage_id - "{car["garage_id"]}", token - "{self.user_token}"'
                    )
                else:
                    response_err_log(response)

        for i in range(self.garage1_related_car_count):
            create_car_request(i, self.garage_ids[0], "garage1")

        for j in range(self.garage2_related_car_count):
            create_car_request(j, self.garage_ids[1], "garage2")

        rest = self.total_car_count - self.garage1_related_car_count - self.garage2_related_car_count
        for k in range(rest):
            create_car_request(k, None, "no garage")

    def get_cars(self):
        with self.client.get(
            "/cars",
            name="008. Get cars",
            headers=self.headers,
            catch_response=True,
        ) as response:
            if response.status_code == 200:
                UserLog.info(f'Got cars - {response.text}, token - "{self.user_token}"')
            else:
                response_err_log(response)

    def create_driver_licence(self):
        with self.client.post(
            "/licences",
            data=json.dumps(generate_driver_licence()),
            name="009. Create driver licence",
            headers=self.headers,
            catch_response=True,
        ) as response:
            if response.status_code == 200:
                UserLog.info(
                    f'Driver licence created, licence id - {response.json()["id"]}, token - "{self.user_token}"'
                )
            else:
                response_err_log(response)

    def get_driver_licence(self):
        with self.client.get(
            "/licences",
            name="010. Get driver licence",
            headers=self.headers,
            catch_response=True,
        ) as response:
            if response.status_code == 200:
                UserLog.info(f'Got licence - {response.text}, token - "{self.user_token}"')
            else:
                response_err_log(response)

    def delete_driver_licence(self):
        with self.client.delete(
            "/licences",
            name="011. Delete driver licence",
            headers=self.headers,
            catch_response=True,
        ) as response:
            if response.status_code == 200:
                UserLog.info(f'Deleted licence - {response.text}, token - "{self.user_token}"')
            else:
                response_err_log(response)

    def delete_cars(self):
        for car_id in self.car_ids:
            with self.client.delete(
                f"/cars/{car_id}",
                name="012. Delete car",
                headers=self.headers,
                catch_response=True,
            ) as response:
                if response.status_code == 200:
                    UserLog.info(
                        f'Deleted car {self.car_ids.index(car_id)}, car_id - {car_id}, token - "{self.user_token}"'
                    )
                else:
                    response_err_log(response)

    def delete_garages(self):
        for garage_id in self.garage_ids:
            with self.client.delete(
                f"/garages/{garage_id}",
                name="013. Delete garage",
                headers=self.headers,
                catch_response=True,
            ) as response:
                if response.status_code == 200:
                    UserLog.info(
                        f'Deleted garage {self.garage_ids.index(garage_id)}, garage_id - {garage_id}, token - "{self.user_token}"'
                    )
                else:
                    response_err_log(response)

    def delete_houses(self):
        for house_id in self.house_ids:
            with self.client.delete(
                f"/houses/{house_id}",
                name="014. Delete house",
                headers=self.headers,
                catch_response=True,
            ) as response:
                if response.status_code == 200:
                    UserLog.info(
                        f'Deleted house {self.house_ids.index(house_id)}, house_id - {house_id}, token - "{self.user_token}"'
                    )
                else:
                    response_err_log(response)
