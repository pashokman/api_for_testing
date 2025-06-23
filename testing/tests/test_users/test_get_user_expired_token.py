from auth.auth_handler import create_access_token
from datetime import timedelta
from fastapi.testclient import TestClient
from main import app
from testing.classes.user import User

import time
import pytest

client = TestClient(app)


@pytest.mark.expired_token
@pytest.mark.user
def test_create_user_expired_token(request):
    user = User(request=request)
    user.create_user()
    token = create_access_token(user.user_id, expires_delta=timedelta(seconds=1))  # expires_delta in seconds
    headers = {"Authorization": f"Bearer {token}"}
    user.headers = headers

    # Wait for token to expire
    time.sleep(2)

    # Try to access a protected endpoint
    response = user.get_me()

    expected_status_code = 401
    expected_error_message = "Token has expired"
    assert response.status_code == expected_status_code
    assert response.json()["detail"] == expected_error_message
