# complete_api_for_testing
I created this API to practice testing it


# Steps to run an API first
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
uvicorn main:app
```
6. To open local API documentation, visit:
```
http://127.0.0.1:8000/docs#/
```
7. Start using API.

# To run tests, do previous steps and then run command in a new terminal (5 is a number of threads to run tests in parallel):
```
pytest -n 5
```


Every time on pull/push request, test should run in GitHub Actions.