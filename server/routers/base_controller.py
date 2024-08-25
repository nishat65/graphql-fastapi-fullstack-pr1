from typing import Callable
from functools import wraps
from utils.logger import Logger


class BaseController:

    def get_logger(self):
        return Logger().get_logger()

    def method_logger(function_pointer: Callable):
        @wraps(function_pointer)
        def wrapper(*args, **kwargs):
            _logger = Logger().get_logger()
            _logger.info(f"{function_pointer.__name__} invoked")
            _logger.info(f"args: {args}")
            result = function_pointer(*args, **kwargs)
            _logger.info(f"End invoke: {function_pointer.__name__}")
            return result

        return wrapper
