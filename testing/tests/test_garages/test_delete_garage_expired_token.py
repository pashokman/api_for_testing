from app.auth.auth_handler import create_access_token
from app.main import app
from datetime import timedelta
from fastapi.testclient import TestClient
from testing.classes.garage import Garage
from testing.classes.user import User

import pytest
import time


client = TestClient(app)


@pytest.mark.expired_token
@pytest.mark.garage
def test_delete_garage_expired_token(request):
    user = User(request=request)
    garage = Garage(request=request)
    user.create_user()
    token = create_access_token(user.user_id, expires_delta=timedelta(seconds=2))  # expires_delta in seconds
    user.headers = {"Authorization": f"Bearer {token}"}
    garage.create_garage(user)

    # Wait for token to expire
    time.sleep(3)

    # Try to access a protected endpoint
    response = garage.delete_garage(user)

    expected_status_code = 401
    expected_error_message = "Token has expired"
    assert response.status_code == expected_status_code
    assert response.json()["detail"] == expected_error_message
