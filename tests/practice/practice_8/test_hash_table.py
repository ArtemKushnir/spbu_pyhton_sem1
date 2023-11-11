from src.practice.practice_8 import hash_table
import pytest
from collections import Counter


def dummy_hash_table(elements):
    hashtable = hash_table.create_hash_table()
    for i in elements:
        hash_table.put(hashtable, i[0], i[1])
    return hashtable


def test_create_hash_table():
    new_hash_table = hash_table.create_hash_table()
    assert (
        new_hash_table.total_buckets == hash_table.DEFAULT_HASH_SIZE
        and len(new_hash_table.buckets) == hash_table.DEFAULT_HASH_SIZE
        and new_hash_table.size == 0
    )


def test_delete_hash_table():
    new_hash_table = hash_table.create_hash_table()
    hash_table.delete_hash_table(new_hash_table)
    assert len(new_hash_table.buckets) == 0


@pytest.mark.parametrize(
    "elements, put_element, expected",
    [
        (((1, 1), (2, 2), (3, 3)), (15, 15), [(1, 1), (2, 2), (3, 3), (15, 15)]),
        (
            (("a", 1), ("c", 2), ("e", 3)),
            ("g", 4),
            [("a", 1), ("c", 2), ("e", 3), ("g", 4)],
        ),
    ],
)
def test_put(elements, put_element, expected):
    new_hash_table = dummy_hash_table(elements)
    hash_table.put(new_hash_table, *put_element)
    all_items = hash_table.items(new_hash_table)
    assert Counter(all_items) == Counter(expected)


@pytest.mark.parametrize(
    "elements, remove_key, expected",
    [
        (((1, 1), (2, 2), (3, 3), (15, 15)), 15, 15),
        (((1, "a"), (2, "b"), (3, "C"), (15, "Test")), 15, "Test"),
    ],
)
def test_remove(elements, remove_key, expected):
    new_hash_table = dummy_hash_table(elements)
    assert hash_table.remove(new_hash_table, remove_key) == expected


@pytest.mark.parametrize(
    "elements, find_key, expected",
    [
        (((1, 1), (2, 2), (3, 3), (15, 15)), 15, True),
        ((("Germany", "Berlin"), ("Russia", "Moscow")), "Germany", True),
        (((1, "Mathematics"), (2, "History")), 15, False),
    ],
)
def test_has_key(elements, find_key, expected):
    new_hash_table = dummy_hash_table(elements)
    assert hash_table.has_key(new_hash_table, find_key) == expected


@pytest.mark.parametrize(
    "elements, get_key, expected",
    [
        (((1, 1), (2, 2), (3, 3), (99, 99)), 99, 99),
        ((("M", 70), ("D", 80)), "D", 80),
        (((20, "Goodbye"), (30, "Hello"), (19, "Hi, world!")), 19, "Hi, world!"),
    ],
)
def test_get(elements, get_key, expected):
    new_hash_table = dummy_hash_table(elements)
    assert hash_table.get(new_hash_table, get_key) == expected


@pytest.mark.parametrize(
    "elements, expected",
    [
        (((1, 1), (2, 2), (3, 3)), [(1, 1), (2, 2), (3, 3)]),
        (
            (("Russia", "Moscow"), ("Spain", "Madrid")),
            [("Russia", "Moscow"), ("Spain", "Madrid")],
        ),
        (((20, 20), (30, 30)), [(20, 20), (30, 30)]),
    ],
)
def test_items(elements, expected):
    new_hash_table = dummy_hash_table(elements)
    all_items = hash_table.items(new_hash_table)
    assert Counter(all_items) == Counter(expected)


def test_remove_error():
    test_hash_table = hash_table.create_hash_table()
    with pytest.raises(ValueError):
        hash_table.remove(test_hash_table, 2)


def test_get_error():
    test_hash_table = hash_table.create_hash_table()
    with pytest.raises(ValueError):
        hash_table.get(test_hash_table, 15)
