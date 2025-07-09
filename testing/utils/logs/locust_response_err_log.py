from testing.utils.logs.locust_main_logger import Logger
from testing.utils.logs.locust_err_logget import ErrLogger


# Main log
main_log = Logger(log_name="ErrLog")
main_log_err = main_log.get_logger()
main_log_err.propagate = False


# Only error log
err_log = ErrLogger(log_name="OnlyErrLog")
only_err_log = err_log.get_logger()
only_err_log.propagate = False


def response_err_log(response):
    msg = f"""
Method - {response.request.method}
Response status - {response.status_code}
Failed with exception - {response.reason}
URL - {response.url}
Request auth token - {response.request.headers.get('Authorization', 'N/A')}
Request body - {response.request.body}
Response body - {response.text}"""

    main_log_err.error(f"{msg}")
    main_log_err.error("--------------------------------------------------------")

    only_err_log.error(f"{msg}")
    only_err_log.error("--------------------------------------------------------")
