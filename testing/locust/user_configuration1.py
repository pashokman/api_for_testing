from locust import SequentialTaskSet, events
from locust.argument_parser import LocustArgumentParser
import urllib3


@events.init_command_line_parser.add_listener
def _(parser: LocustArgumentParser):
    parser.add_argument(
        "--house_count", type=int, env_var="HOUSE_COUNT", default=2, help="How many houses each user should create."
    )

    parser.add_argument(
        "--total_garage_count",
        type=int,
        env_var="TOTAL_GARAGE_COUNT",
        default=4,
        help="How many garages each user should create in total. Default = 4",
    )
    parser.add_argument(
        "--house1_related_garage_count",
        type=int,
        env_var="HOUSE1_RELATED_GARAGE_COUNT",
        default=1,
        help="How many garages each user should create, related to house1 (Value should be less or equal to total_garage_count). Default = 1. house1_related_garage_count + house2_related_garage_count <= total_garage_count",
    )
    parser.add_argument(
        "--house2_related_garage_count",
        type=int,
        env_var="HOUSE2_RELATED_GARAGE_COUNT",
        default=1,
        help="How many garages each user should create, related to house2 (Value should be less or equal to total_garage_count). Default = 1. house1_related_garage_count + house2_related_garage_count <= total_garage_count",
    )

    parser.add_argument(
        "--total_car_count",
        type=int,
        env_var="TOTAL_CAR_COUNT",
        default=4,
        help="How many cars each user should create in total. Default = 4",
    )
    parser.add_argument(
        "--garage1_related_car_count",
        type=int,
        env_var="GARAGE1_RELATED_CAR_COUNT",
        default=1,
        help="How many cars each user should create, related to garage1 (Value should be less or equal to total_car_count). Default = 1. garage1_related_car_count + garage2_related_car_count <= total_car_count",
    )
    parser.add_argument(
        "--garage2_related_car_count",
        type=int,
        env_var="GARAGE2_RELATED_CAR_COUNT",
        default=1,
        help="How many cars each user should create, related to garage2 (Value should be less or equal to total_car_count). Default = 1. garage1_related_car_count + garage2_related_car_count <= total_car_count",
    )

    parser.add_argument(
        "--certificate_verification_enabled",
        type=str,
        env_var="CERTIFICATE_VERIFICATION_ENABLED",
        default="True",
        help="Enable certificate verification or not.",
    )


@events.test_start.add_listener
def _(environment, **kw):
    print(f"House count supplied for one user: {environment.parsed_options.house_count}")

    print(f"Total garage count supplied for one user: {environment.parsed_options.total_garage_count}")
    print(
        f"Garages count related to house1 supplied for one user: {environment.parsed_options.house1_related_garage_count}"
    )
    print(
        f"Garages count related to house2 supplied for one user: {environment.parsed_options.house2_related_garage_count}"
    )

    print(f"Total car count supplied for one user: {environment.parsed_options.total_car_count}")
    print(
        f"Cars count related to garage1 supplied for one user: {environment.parsed_options.garage1_related_car_count}"
    )
    print(
        f"Cars count related to garage2 supplied for one user: {environment.parsed_options.garage2_related_car_count}"
    )

    print(f"Certificate verification enabled: {environment.parsed_options.certificate_verification_enabled}")


class UserConfiguration(SequentialTaskSet):
    # class for configure different user scenario properties

    def on_start(self):
        parsed = self.user.environment.parsed_options

        self.house_count = parsed.house_count

        self.total_garage_count = parsed.total_garage_count
        self.house1_related_garage_count = parsed.house1_related_garage_count
        self.house2_related_garage_count = parsed.house2_related_garage_count

        self.total_car_count = parsed.total_car_count
        self.garage1_related_car_count = parsed.garage1_related_car_count
        self.garage2_related_car_count = parsed.garage2_related_car_count

        self.certificate_verification_enabled = parsed.certificate_verification_enabled

        self.user_obj = None
        self.user_id = None
        self.user_token = None
        self.house_ids = []
        self.garage_ids = []
        self.car_ids = []

        # turn on/off SSL certificates verification
        if self.certificate_verification_enabled == "True":
            self.certificate_verification_enabled = True
        elif self.certificate_verification_enabled == "False":
            self.certificate_verification_enabled = False
            urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

        self.client.verify = self.certificate_verification_enabled

    def on_stop(self):
        self.house_count = None

        self.total_garage_count = None
        self.house1_related_garage_count = None
        self.house2_related_garage_count = None

        self.total_car_count = None
        self.garage1_related_car_count = None
        self.garage2_related_car_count = None

        self.certificate_verification_enabled = None

        self.user_obj = None
        self.user_id = None
        self.user_token = None
        self.house_ids = []
        self.garage_ids = []
        self.car_ids = []
