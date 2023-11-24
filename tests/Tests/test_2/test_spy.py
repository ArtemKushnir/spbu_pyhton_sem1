from io import StringIO
from src.Tests.test_2.spy import spy, print_usage_statistic
import pytest
from datetime import datetime


@spy
def foo(a, b):
    return a, b


@spy
def foo2():
    return True


foo3 = lambda x: x


@spy
def foo4(x):
    return x


def test_print_usage_statistic():
    value = [i for i in print_usage_statistic(foo)]
    assert "".join(value) == ""


def test_print_usage_exception() -> None:
    for _ in range(3):
        foo3("aaa")
    with pytest.raises(AttributeError):
        list(print_usage_statistic(foo3))
