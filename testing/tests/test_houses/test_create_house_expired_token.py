from auth.auth_handler import create_access_token
from datetime import timedelta
from fastapi.testclient import TestClient
from main import app
from testing.classes.user import User
from testing.utils.generators.house_generator import generate_house

import pytest
import time


client = TestClient(app)


@pytest.mark.expired_token
@pytest.mark.house
def test_create_house_expired_token():
    user = User()
    user.create_user()
    token = create_access_token(user.user_id, expires_delta=timedelta(seconds=2))  # expires_delta in seconds
    headers = {"Authorization": f"Bearer {token}"}

    # Wait for token to expire
    time.sleep(3)

    # Try to access a protected endpoint
    response = client.post("houses", json=generate_house(), headers=headers)
    expected_status_code = 401
    assert response.status_code == expected_status_code
