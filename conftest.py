import os
import pytest
import shutil


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

    log_file = os.path.join(os.getcwd(), "automation.log")
    if os.path.exists(log_file):
        with open(log_file, "w"):
            pass
