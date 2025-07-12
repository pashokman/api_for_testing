from locust import task
from testing.locust.user_behavior2 import UserBehavior


class UserScenario(UserBehavior):
    # class describes only user scenarios

    @task
    def test_scenario1(self):
        """
        Scenario description:
        001. Create user account
        002. Authorize user account
        003. Create N houses with user account token (N >= 2, default = 2)
        004. Get all houses.
        005. Create M garages with user account token (M >= 2, default = 4)
         - K garages belongs to house1 (K >= 1, default = 1)
         - L garages belongs to house2 (L >= 1, default = 1)
         - P garages without house relation (P = M - K - L). If M = 2, K = 1 and L = 1, P = 0. If M = 4, K = 1 and L = 1, P = 2
        006. Get all garages.
        007. Create W cars with user account token (W >= 2, default = 4)
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
        self.create_houses()
        self.get_houses()
        self.create_garages()
        self.get_garages()
        self.create_cars()
        self.get_cars()
        self.create_driver_licence()
        self.get_driver_licence()
        self.delete_driver_licence()
        self.delete_cars()
        self.delete_garages()
        self.delete_houses()

        # this line needs to end user scenario and clear self properties
        self.interrupt()
