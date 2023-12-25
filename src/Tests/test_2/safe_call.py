import functools
import traceback
import warnings
import sys


def safe_call(function):
    @functools.wraps(function)
    def inner(*args, **kwargs):
        try:
            return function(*args, **kwargs)
        except Exception:
            output_arguments = parse_traceback()
            warnings.warn(make_message(output_arguments), category=Warning)

    return inner


def make_message(output_arguments):
    return "\nfunction name: {}\nerror type: {}\nerror message: {}\nerror line: {}\nnumber error line: {}".format(
        *output_arguments
    )


def parse_traceback():
    error = traceback.extract_tb((sys.exc_info())[2])[-1]
    type_error, error_message = sys.exc_info()[:-1]
    type_error = str(type_error)[str(type_error).find("'") + 1 : -2]
    return error.name, type_error, error_message, error.line, error.lineno
