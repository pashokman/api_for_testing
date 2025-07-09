import logging


class Logger:

    def __init__(self, log_level=logging.DEBUG, log_name=None):
        self.logger = logging.getLogger(log_name)
        self.logger.setLevel(log_level)

        if not self.logger.handlers:
            fh = logging.FileHandler("locust_main.log")
            formatter = logging.Formatter(
                "%(asctime)s - %(levelname)s - %(name)s : %(message)s",
                datefmt="%d.%m.%Y %H:%M:%S",
            )
            fh.setFormatter(formatter)
            self.logger.addHandler(fh)

    def get_logger(self):
        return self.logger
