import tempfile
from src.Homeworks.homework_6 import shopping, avl_tree
from test_avl_tree import create_dummy_tree
from io import StringIO
import pytest


@pytest.mark.parametrize(
    "elements,key,value, expected",
    [(((38, 4), (39, 5), (40, 10)), 39, 11, 16), (((1, 10), (2, 20), (3, 1)), 4, 7, 7)],
)
def test_process_add_request(elements, key, value, expected):
    new_tree = create_dummy_tree(elements)
    shopping.process_add_request(new_tree, key, value)
    actual = avl_tree.get(new_tree, key)
    assert actual == expected


@pytest.mark.parametrize(
    "elements,key,expected",
    [
        (((22, 10), (98, 11), (50, 12)), 98, 11),
        (((22, 10), (98, 11), (50, 12)), 99, 0),
    ],
)
def test_process_get_request(elements, key, expected):
    new_tree = create_dummy_tree(elements)
    actual = shopping.process_get_request(new_tree, key)
    assert actual == expected


@pytest.mark.parametrize(
    "elements,key,expected",
    [
        (((22, 10), (98, 11), (50, 12)), 22, 22),
        (((22, 10), (98, 11), (50, 12)), 55, 98),
        (((22, 10), (98, 11), (50, 12)), 99, "there is no suitable size"),
    ],
)
def test_process_select_request(elements, key, expected):
    new_tree = create_dummy_tree(elements)
    actual = shopping.process_select_request(new_tree, key)
    assert actual == expected


@pytest.mark.parametrize(
    "elements,string,expected",
    [
        (((22, 10), (98, 11), (50, 12)), "ADD 51 1", "instances added"),
        (((22, 10), (98, 11), (50, 12)), "GET 98", 11),
        (((22, 10), (98, 11), (50, 12)), "SELECT 96", 98),
    ],
)
def test_process_request(elements, expected, string):
    new_tree = create_dummy_tree(elements)
    actual = shopping.process_request(new_tree, string)
    assert actual == expected


@pytest.mark.parametrize(
    "string,expected",
    [
        ("ADD 44 5", True),
        ("ADD s 5", False),
        ("ADD46", False),
        ("GET 9", True),
        ("SELECT 99", True),
    ],
)
def test_validate_request(string, expected):
    actual = shopping.validate_request(string)
    assert actual == expected


def test_main_scenario(monkeypatch):
    results_file = tempfile.NamedTemporaryFile(mode="w+")
    balance_file = tempfile.NamedTemporaryFile(mode="w+")
    arguments = iter(["2", "/home/kush/python/SPBU_projects/spbu_python_sem1/src/Homeworks/homework_6/shop_logs.txt", f"{results_file.name}", f"{balance_file.name}", "3"])
    monkeypatch.setattr("builtins.input", lambda x: next(arguments, "\n"))
    shopping.main()
    with open("src/Homeworks/Homework_6/shop_results.txt") as result:
        with open(results_file.name) as actual_result:
            results_file.close()
            for expected in result:
                actual = actual_result.readline()
                assert expected == actual
