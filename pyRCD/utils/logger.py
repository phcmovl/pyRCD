"""
Logging defs/classes for pyRCD.

Usage will be via decorators.
"""

import logging
from functools import wraps


class CustomFormatter(logging.Formatter):
    def format(self, record):
        if hasattr(record, 'name_override'):
            record.funcName = record.name_override
        return super(CustomFormatter, self).format(record)


def log_and_call(statement):
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            logger.info(statement, extra={'name_override': func.__name__})
            return func(*args, **kwargs)
        return wrapper
    return decorator

# create class for this later, needs to support multi modules/formats
logger  = logging.getLogger(__file__)
handler = logging.StreamHandler()
logger.setLevel(logging.DEBUG)
handler.setLevel(logging.DEBUG)
handler.setFormatter(CustomFormatter('%(funcName)20s - %(message)s'))
logger.addHandler(handler)
