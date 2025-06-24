from app.auth.auth_handler import create_access_token
from app.main import app
from datetime import timedelta
from fastapi.testclient import TestClient
from testing.classes.driver_licence import DriverLicence
from testing.classes.user import User

import pytest
import time


client = TestClient(app)


@pytest.mark.expired_token
@pytest.mark.licence
def test_get_driver_licence_expired_token(request):
    user = User(request=request)
    licence = DriverLicence(request=request)
    user.create_user()
    token = create_access_token(user.user_id, expires_delta=timedelta(seconds=2))  # expires_delta in seconds
    user.headers = {"Authorization": f"Bearer {token}"}
    licence.create_licence(user)

    # Wait for token to expire
    time.sleep(3)

    # Try to access a protected endpoint
    response = licence.get_my_licence(user)

    expected_status_code = 401
    expected_error_message = "Token has expired"
    assert response.status_code == expected_status_code
    assert response.json()["detail"] == expected_error_message
