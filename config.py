from dotenv import load_dotenv
import os

import pytest
import shutil

load_dotenv()

SECRET_KEY = os.environ.get("SECRET_KEY")
ALGORITHM = os.environ.get("ALGORITHM")
ACCESS_TOKEN_EXPIRE_MINUTES = int(os.environ.get("ACCESS_TOKEN_EXPIRE_MINUTES", "1440"))
ADMIN_PASSWORD = os.environ.get("ADMIN_PASSWORD")
INCORRECT_BEARER_TOKEN = os.environ.get("INCORRECT_BEARER_TOKEN")


@pytest.hookimpl(tryfirst=True)
def pytest_sessionstart(session):
    # Before each pytest run, clear "allure-results", "report" folders and "automation.log" file
    allure_dir = os.path.join(os.getcwd(), "allure-results")
    if os.path.exists(allure_dir):
        shutil.rmtree(allure_dir)
        os.makedirs(allure_dir)

    html_report = os.path.join(os.getcwd(), "report")
    if os.path.exists(html_report):
        shutil.rmtree(html_report)
        os.makedirs(html_report)

    # This functionality should be added next
    # log_file = os.path.join(os.getcwd(), "automation.log")
    # if os.path.exists(log_file):
    #     with open(log_file, "w"):
    #         pass
