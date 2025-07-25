from app.auth.auth_handler import create_access_token
from datetime import timedelta
from fastapi.testclient import TestClient
from app.main import app
from testing.classes.house import House
from testing.classes.user import User
from testing.utils.generators.house_generator import generate_house

import pytest
import time


client = TestClient(app)


@pytest.mark.expired_token
@pytest.mark.house
def test_get_house_expired_token(request):
    user = User(request=request)
    house = House(request=request)
    user.create_user()
    house.create_house(user)

    token = create_access_token(user.user_id, expires_delta=timedelta(seconds=2))  # expires_delta in seconds
    user.headers = {"Authorization": f"Bearer {token}"}

    # Wait for token to expire
    time.sleep(3)

    # Try to access a protected endpoint
    response = house.get_my_houses(user)

    expected_status_code = 401
    expected_error_message = "Token has expired"
    assert response.status_code == expected_status_code
    assert response.json()["detail"] == expected_error_message
