import json
import os

from locust import SequentialTaskSet, task
from locust.exception import StopUser

from testing.utils.generators.car_generator import generate_car
from testing.utils.generators.driver_licence_generator import generate_driver_licence
from testing.utils.generators.garage_generator import generate_garage
from testing.utils.generators.user_generator import generate_user
from testing.utils.generators.house_generator import generate_house
from testing.utils.logs.locust_main_logger import Logger
from testing.utils.logs.locust_response_err_log import response_err_log

# clear log files before each locust run from the command line
for log_file in ["locust_main.log", "locust_only_error.log"]:
    if os.path.exists(log_file):
        with open(log_file, "w"):
            pass

# connect logging
log = Logger(log_name="UserBehavior")
UserLog = log.get_logger()
UserLog.propagate = False


class UserBehavior(SequentialTaskSet):
    # class describes user behavior with all api methods and some testing scenarios
    def on_start(self):
        self.user_obj = None
        self.user_id = None
        self.user_token = None
        self.house_ids = []
        self.garage_ids = []
        self.car_ids = []

    def on_stop(self):
        self.user_obj = None
        self.user_id = None
        self.user_token = None
        self.house_ids = []
        self.garage_ids = []
        self.car_ids = []

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

    def create_houses(self, house_count: int = 2):
        for i in range(house_count):
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

    def create_garages(
        self, total_garage_count: int = 4, house1_related_garage_count: int = 1, house2_related_garage_count: int = 1
    ):
        """
        Create garages.

        Args:
            total_garage_count (int): The total number of garages to create. Default = 4.
            house1_related_garage_count (int): How many garages should be created with house1 relation. Default = 1.
            house2_related_garage_count (int): How many garages should be created with house2 relation. Default = 1.

        Returns:
            None
        """
        if house1_related_garage_count + house2_related_garage_count > total_garage_count:
            raise ValueError(
                f"Invalid configuration: total_garage_count ({total_garage_count}) < house1_related_garage_count ({house1_related_garage_count}) + house2_related_garage_count ({house2_related_garage_count})"
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

        for i in range(house1_related_garage_count):
            create_garage_request(i, self.house_ids[0], "house1")

        for j in range(house2_related_garage_count):
            create_garage_request(j, self.house_ids[1], "house2")

        rest = total_garage_count - house1_related_garage_count - house2_related_garage_count
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

    def create_cars(
        self, total_car_count: int = 4, garage1_related_car_count: int = 1, garage2_related_car_count: int = 1
    ):
        """
        Create cars.

        Args:
            total_car_count (int): The total number of cars to create. Default = 4.
            garage1_related_car_count (int): How many cars should be created with garage1 relation. Default = 1.
            garage2_related_car_count (int): How many cars should be created with garage2 relation. Default = 1.

        Returns:
            None
        """
        if garage1_related_car_count + garage2_related_car_count > total_car_count:
            raise ValueError(
                f"Invalid configuration: total_car_count ({total_car_count}) < garage1_related_car_count ({garage1_related_car_count}) + garage2_related_car_count ({garage2_related_car_count})"
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

        for i in range(garage1_related_car_count):
            create_car_request(i, self.garage_ids[0], "garage1")

        for j in range(garage2_related_car_count):
            create_car_request(j, self.garage_ids[1], "garage2")

        rest = total_car_count - garage1_related_car_count - garage2_related_car_count
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

    @task
    def test_scenario1(self):
        """
        Scenario description:
        001. Create user account
        002. Authorize user account
        003. Create N houses with user account token (N >= 2, default = 2)
        004. Get all houses.
        005. Create M garages with user account token (M >= 2, default = 3)
         - K garages belongs to house1 (K >= 1, default = 1)
         - L garages belongs to house2 (L >= 1, default = 1)
         - P garages without house relation (P = M - K - L). If M = 2, K = 1 and L = 1, P = 0. If M = 4, K = 1 and L = 1, P = 2
        006. Get all garages.
        007. Create W cars with user account token
         - X cars belongs to garage1 (X >= 1, default = 1)
         - Y cars belongs to garage2 (Y >= 1, default = 1)
         - Z cars without garage relation (Z = W - X - Y). If W = 2, X = 1 and Y = 1, Z = 0. If W = 4, X = 1 and Y = 1, Z = 2
        008. Get all cars.
        009. Create driver licence with user account token
        010. Get driver licence
        011. Delete driver licence.
        012. Delete each car.
        013. Delete each garage.
        014. Delete each house.
        """
        self.create_user()
        self.auth_user()
        self.create_houses()  # add getting variable from console
        self.get_houses()
        self.create_garages()  # add getting variables from console
        self.get_garages()
        self.create_cars()  # add getting variables from console
        self.get_cars()
        self.create_driver_licence()

        self.interrupt()
