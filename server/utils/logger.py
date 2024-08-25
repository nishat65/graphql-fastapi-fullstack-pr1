import logging
import sys


class Logger(object):
    """
    Class following Singleton design pattern
    """

    _logger = logging.getLogger()
    _logger.setLevel(logging.INFO)

    _handler = logging.StreamHandler(sys.stdout)
    _handler.setLevel(logging.INFO)

    _formatter = logging.Formatter(
        "%(asctime)s - %(name)s - %(levelname)s - %(message)s"
    )
    _handler.setFormatter(_formatter)
    _logger.handlers = [_handler]

    def __new__(cls):
        if not hasattr(cls, "instance"):
            cls.instance = super(Logger, cls).__new__(cls)
        return cls.instance

    def get_logger(self):
        return self._logger
