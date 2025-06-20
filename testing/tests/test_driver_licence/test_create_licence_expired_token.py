from auth.auth_handler import create_access_token
from datetime import timedelta
from fastapi.testclient import TestClient
from main import app
from testing.classes.user import User
from testing.utils.generators.driver_licence_generator import generate_driver_licence

import pytest
import time


client = TestClient(app)


@pytest.mark.expired_token
@pytest.mark.licence
def test_create_driver_licence_expired_token():
    user = User()
    user.create_user()
    token = create_access_token(user.user_id, expires_delta=timedelta(seconds=1))  # expires_delta in seconds

    # Wait for token to expire
    time.sleep(2)

    # Try to access a protected endpoint
    headers = {"Authorization": f"Bearer {token}"}
    response = client.post("licences", json=generate_driver_licence(), headers=headers)
    expected_status_code = 401
    assert response.status_code == expected_status_code
