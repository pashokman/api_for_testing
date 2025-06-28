import os
import pytest
import shutil


@pytest.hookimpl(tryfirst=True)
def pytest_sessionstart(session):
    # Before each pytest run, clear "allure-results", "report" folders and "automation.log" file
    # allure_dir = os.path.join(os.getcwd(), "allure-results")
    # if os.path.exists(allure_dir):
    #     shutil.rmtree(allure_dir)
    #     os.makedirs(allure_dir)
    allure_dir = "allure-results"
    if os.path.exists(allure_dir):
        for filename in os.listdir(allure_dir):
            file_path = os.path.join(allure_dir, filename)
            try:
                if os.path.isfile(file_path) or os.path.islink(file_path):
                    os.unlink(file_path)
                elif os.path.isdir(file_path):
                    shutil.rmtree(file_path)
            except Exception as e:
                print(f"Failed to delete {file_path}. Reason: {e}")

    # html_report = os.path.join(os.getcwd(), "report")
    # if os.path.exists(html_report):
    #     shutil.rmtree(html_report)
    #     os.makedirs(html_report)
    report_dir = "report"
    if os.path.exists(report_dir):
        for filename in os.listdir(report_dir):
            file_path = os.path.join(report_dir, filename)
            try:
                if os.path.isfile(file_path) or os.path.islink(file_path):
                    os.unlink(file_path)
                elif os.path.isdir(file_path):
                    shutil.rmtree(file_path)
            except Exception as e:
                print(f"Failed to delete {file_path}. Reason: {e}")

    log_file = os.path.join(os.getcwd(), "automation.log")
    if os.path.exists(log_file):
        with open(log_file, "w"):
            pass
