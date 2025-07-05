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
🚀 `Dockerized setup` for reproducible environments: includes both API server and testing suite.  
🔁 CI/CD integration with `GitHub Actions` to run tests on every push or pull request.  
⚙️ Environment configuration via environment variables and structured Docker Compose setup.  


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


Every time on pull/push request, test expected to run GitHub Actions.