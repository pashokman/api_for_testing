# 🏗️ Advanced Python Automation Testing Framework
This repository implements a robust and maintainable testing framework for `REST APIs` in `Python`, demonstrating best practices from real-world automation projects:  
💻 `Custom API` implementation (`FastAPI` + seed data via `seed.py`) used as a controllable target for testing.  
🧰 `Pytest-based` testing framework featuring fixtures, test categorization (smoke, regression, etc.), and advanced configuration via `pytest.ini`.  
⚡ Parallel test execution with `pytest-xdist` and retries for flaky tests using `pytest-rerunfailures`.  
🧬 Test data generation using `Faker` for dynamic, realistic inputs.  
✅ API response validation via status code checks and schema validation with `jsonschema`.  
🎭 Auth & role-based tests covering valid/invalid/expired tokens and roles (admin/user).  
🛡️ Security tests for common vulnerabilities including `SQL Injection (SQLi)` and `Cross-site Scripting (XSS)` — tested via crafted malicious payloads.  
📊 `Reporting: Allure & HTML reports` with artifact integration.   
📝 `Centralized logging` into a single file and optional separate logging server.  
📩 `Telegram notifications`: Instant alerts about test results (passed or failed) are sent to a private chat via a custom bot using `GitHub Actions`.   
📈 Load testing with `Locust`: Scenarios for performance, with parametrized user behavior and token-based auth support.  
🚀 `Dockerized setup` for reproducible environments: includes both API server and testing suite.  
🔁 CI/CD integration with `GitHub Actions` to run tests on every push or pull request.  
⚙️ Environment configuration via `environment variables` and structured Docker Compose setup.  


## Steps to setup environment, API, logging
1. Create virtual environment:
```
python -m venv venv
```
2. Activate virtual environment:
```
.\venv\Scripts\activate
```
3. Install dependencies:
```
pip install -r requirements.txt
```
4. Create tables and admin account:
```
python seed.py
```
5. Run API:
```
uvicorn app.main:app
```
6. To open local API documentation, visit:
```
http://127.0.0.1:8000/docs#/
```
7. Start using API.
8. In a new terminal, start logging server for saving logs into a single file.
```
python .\testing\utils\logs\log_server.py
```

## To run tests, do previous steps and then run command in a new terminal (to configure pytest run, use pytest.ini):
```
pytest
```

## To see the allure-report, user command (after test run):
```
allure serve allure-results
```

## To see the html-report, just open myreport.html in any browser (after test run)

## To setup project in docker, run:
```
docker-compose up --build
```

## To run Locust testing, made steps 1-5 and then run command and open Web UI for test configuration:
Load test scenario for current API:
1. Create user account.
2. Authorize user account.
3. Create A houses with user account token (A >= 2, default = 2).
4. Get all houses.
5. Create B garages with user account token (B >= 2, default = 4):
    - C garages belongs to house1 (C >= 1, default = 1),
    - D garages belongs to house2 (D >= 1, default = 1),
    - E garages without house relation (E = B - C - D). If B = 2, C = 1 and D = 1, E = 0. If B = 4, C = 1 and D = 1, E = 2.
6. Get all garages.
7. Create F cars with user account token (F >= 2, default = 4):
    - G cars belongs to garage1 (G >= 1, default = 1),
    - H cars belongs to garage2 (H >= 1, default = 1),
    - I cars without garage relation (I = F - G - H). If F = 2, G = 1 and H = 1, I = 0. If F = 4, G = 1 and H = 1, I = 2.
8. Get all cars.
9. Create driver licence with user account token.
10. Get driver licence.
11. Delete driver licence.
12. Delete each car.
13. Delete each garage.
14. Delete each house.

To run Locust and configure all scenario parameters in WebUI, run command: 
```
python -m locust -f testing/locust/user_start4.py
```
WebUI address - `http://localhost:8089`  

Also you can configure test run directly from command line when run Locust:  
- `--house_count` - (A) number of houses created by one user;
- `--total_garage_count` - (B) total number of garages created by one user;
- `--house1_related_garage_count` - (C) number of garages with relation to first user house;
- `--house2_related_garage_count` - (D) number of garages with relation to second user house;
- `--total_car_count` - (F) total number of cars created by one user;
- `--garage1_related_car_count` - (G) number of cars with relation to first user garage;
- `--garage2_related_car_count` - (H) number of cars with relation to second user garage;
- `--certificate_verification_enabled` - enable or disable certificate verification - hide warnings from the console, while test is running (True/Enabled by default);
- `-u`/`--users` - defines the number of users (load) to create during the test;
- `-r`/`--spawn-rate` - defines the rate at which new users are spawned (number of users per second);
- `-t`/`--run-time` - specifies the duration of the test (e.g., 1h30m, 10s).

Command to run testing without using WebUI, only CLI:
```
python -m locust -f testing/locust/user_start4.py --headless --house_count=5 --total_garage_count=6 --house1_related_garage_count=2 --house2_related_garage_count=3 --total_car_count=7 --garage1_related_car_count=2 --garage2_related_car_count=2 --certificate_verification_enabled=True -u 10 -r 1 -t 60s
```