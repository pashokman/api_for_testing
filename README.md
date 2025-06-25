# api_for_testing
I created this API to practice testing it and adding the most useful functionality, like:
- environment variables;
- pytest run configuration in pytest.ini;
- pytest marks;
- rerun functionality to avoid flacky tests;
- logging;
- reporting - Allure, html-report;
- GitHub Actions run;
- Docker build and run.


## Steps to run an API first
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


Every time on pull/push request, test should run in GitHub Actions.