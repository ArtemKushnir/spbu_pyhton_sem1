import functools
from datetime import datetime


def spy(function):
    @functools.wraps(function)
    def inner(*args, **kwargs):
        current_time = datetime.now()
        params = {"args": args, "kwargs": kwargs}
        inner.logs.append((current_time, params))
        result = function(*args, **kwargs)
        return result

    inner.logs = []
    return inner


def print_usage_statistic(function):
    try:
        for log in function.logs:
            yield log
    except AttributeError:
        raise AttributeError(
            "It is impossible to find out the parameters of an undecorated function"
        )
