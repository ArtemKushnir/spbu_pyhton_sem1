import functools
from datetime import datetime
from os.path import exists
from inspect import getcallargs


def with_arguments(deco):
    @functools.wraps(deco)
    def wrapper(*dargs, **dkwargs):
        def decorator(func):
            result = deco(func, *dargs, **dkwargs)
            functools.update_wrapper(result, func)
            return result

        return decorator

    return wrapper


@with_arguments
def logger(func, file_name):
    print()

    @functools.wraps(func)
    def inner(*args, **kwargs):
        all_args = getcallargs(func, *args, **kwargs)
        all_args_str = [f"{i[0]}={i[1]}" for i in all_args.items()]
        current_date = datetime.now().strftime("%Y/%m/%d %H:%M:%S")
        result = func(*args, **kwargs)
        logs = " ".join([current_date, func.__name__, *all_args_str, str(result)])
        if not exists(file_name):
            with open(file_name, "w") as file:
                file.write(logs + "\n")
        else:
            with open(file_name, "a") as file:
                file.write(logs + "\n")
        return result

    return inner


@logger("test.txt")
def f(a, b):
    if a != 0:
        return f(a - 1, b - 1)
    return b


f(1, 1)
f(b=2, a=1)
