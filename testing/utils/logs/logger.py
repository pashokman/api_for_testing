import logging
import logging.handlers


class Logger:
    def __init__(self, log_level=logging.DEBUG):
        self.logger = logging.getLogger()
        self.logger.setLevel(log_level)

        if not any(isinstance(h, logging.handlers.SocketHandler) for h in self.logger.handlers):
            sh = logging.handlers.SocketHandler("localhost", 9020)
            self.logger.addHandler(sh)

    def get_logger(self):
        return self.logger

    def get_adapter(self, test_context=""):
        return logging.LoggerAdapter(self.logger, {"test_context": test_context})
