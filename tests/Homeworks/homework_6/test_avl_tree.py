from src.Homeworks.homework_6 import avl_tree
import pytest


def create_dummy_tree(elements):
    new_tree = avl_tree.create_tree()
    for element in elements:
        avl_tree.put(new_tree, element[0], element[1])
    return new_tree


def test_create_tree():
    new_tree = avl_tree.create_tree()
    assert new_tree.size == 0 and new_tree.root is None


def test_delete_tree():
    new_tree = create_dummy_tree([(10, 10), (20, 20), (5, 5)])
    avl_tree.delete_tree(new_tree)
    assert new_tree.size == 0 and new_tree.root is None


@pytest.mark.parametrize(
    "elements,expected,size",
    [
        (
            ((10, 10), (20, 20), (5, 5), (30, 30), (15, 15)),
            [(5, 5), (10, 10), (15, 15), (20, 20), (30, 30)],
            5,
        ),
        (((55, 55), (60, 60), (50, 50)), [(50, 50), (55, 55), (60, 60)], 3),
        (((1, 1), (2, 2), (3, 3)), [(1, 1), (2, 2), (3, 3)], 3),
        (
            ((20, 20), (40, 40), (10, 10), (50, 50), (30, 30), (25, 25)),
            [(10, 10), (20, 20), (25, 25), (30, 30), (40, 40), (50, 50)],
            6,
        ),
    ],
)
def test_put(elements, expected, size):
    new_tree = create_dummy_tree(elements)
    values = avl_tree.traverse(new_tree, "inorder")
    assert values == expected
    assert new_tree.size == size


@pytest.mark.parametrize(
    "elements,key_element,value_element",
    [
        (((20, 20), (30, 30), (10, 10)), 10, 10),
        (((1, 1), (2, 2), (3, 3), (4, 4)), 3, 3),
        (((20, 20), (10, 10), (40, 40), (30, 30), (50, 50)), 40, 40),
    ],
)
def test_remove(elements, key_element, value_element):
    new_tree = create_dummy_tree(elements)
    remove_value = avl_tree.remove(new_tree, key_element)
    assert not avl_tree.has_key(new_tree, key_element)
    assert remove_value == value_element


def test_exception_raise_remove():
    new_tree = create_dummy_tree(((20, 20), (10, 10), (30, 30)))
    with pytest.raises(ValueError):
        avl_tree.remove(new_tree, 35)


@pytest.mark.parametrize(
    "elements,expected",
    [
        (((1, 1), (2, 2), (3, 3), (4, 4), (5, 5)), 1),
        (((100, 100), (200, 200), (99, 99)), 99),
    ],
)
def test_get_minimum(elements, expected):
    new_tree = create_dummy_tree(elements)
    actual = avl_tree.get_minimum(new_tree)
    assert actual == expected


def test_exception_raise_get_minimum():
    first_tree = avl_tree.create_tree()
    with pytest.raises(ValueError):
        avl_tree.get_minimum(first_tree)


@pytest.mark.parametrize(
    "elements, expected",
    [
        (((1, 1), (2, 2), (3, 3), (4, 4), (5, 5)), 5),
        (((100, 100), (200, 200), (99, 99)), 200),
    ],
)
def test_get_maximum(elements, expected):
    new_tree = create_dummy_tree(elements)
    actual = avl_tree.get_maximum(new_tree)
    assert actual == expected


def test_exception_raise_get_maximum():
    first_tree = avl_tree.create_tree()
    with pytest.raises(ValueError):
        avl_tree.get_maximum(first_tree)


@pytest.mark.parametrize(
    "elements,key,expected",
    [
        (((30, "f"), (40, "f"), (20, "test")), 20, "test"),
        (((30, "test"), (40, "f"), (20, "f")), 30, "test"),
        (((30, "f"), (40, "test"), (20, "f")), 40, "test"),
    ],
)
def test_get(elements, key, expected):
    new_tree = create_dummy_tree(elements)
    actual = avl_tree.get(new_tree, key)
    assert actual == expected


def test_exception_raise_get():
    new_tree = create_dummy_tree(((20, 20), (10, 10), (30, 30)))
    with pytest.raises(ValueError):
        avl_tree.get(new_tree, 35)


@pytest.mark.parametrize(
    "elements,key,expected",
    [
        (((10, 10), (20, 20), (30, 30)), 30, True),
        (((10, 10), (20, 20), (30, 30)), 31, False),
    ],
)
def test_has_key(elements, key, expected):
    new_tree = create_dummy_tree(elements)
    actual = avl_tree.has_key(new_tree, key)
    assert actual == expected


@pytest.mark.parametrize(
    "elements,key,expected",
    [
        (
            ((50, 50), (60, 60), (40, 40), (30, 30), (45, 45), (55, 55), (65, 65)),
            44,
            45,
        ),
        (
            ((50, 50), (60, 60), (40, 40), (30, 30), (45, 45), (55, 55), (65, 65)),
            45,
            45,
        ),
        (
            ((50, 50), (60, 60), (40, 40), (30, 30), (45, 45), (55, 55), (65, 65)),
            60,
            60,
        ),
    ],
)
def test_get_lower_bound(elements, key, expected):
    new_tree = create_dummy_tree(elements)
    actual = avl_tree.get_lower_bound(new_tree, key)
    assert actual == expected


def test_exception_raise_get_lower_bound():
    first_tree = avl_tree.create_tree()
    second_tree_tree = create_dummy_tree(((20, 20), (10, 10), (30, 30)))
    with pytest.raises(ValueError):
        avl_tree.get_lower_bound(first_tree, 5)
    with pytest.raises(ValueError):
        avl_tree.get_lower_bound(second_tree_tree, 31)


@pytest.mark.parametrize(
    "elements,key,expected",
    [
        (
            ((50, 50), (60, 60), (40, 40), (30, 30), (45, 45), (55, 55), (65, 65)),
            44,
            45,
        ),
        (
            ((50, 50), (60, 60), (40, 40), (30, 30), (45, 45), (55, 55), (65, 65)),
            45,
            50,
        ),
        (
            ((50, 50), (60, 60), (40, 40), (30, 30), (45, 45), (55, 55), (65, 65)),
            59,
            60,
        ),
    ],
)
def test_get_upper_bound(elements, key, expected):
    new_tree = create_dummy_tree(elements)
    actual = avl_tree.get_upper_bound(new_tree, key)
    assert actual == expected


def test_exception_raise_get_upper_bound():
    first_tree = avl_tree.create_tree()
    second_tree_tree = create_dummy_tree(((20, 20), (10, 10), (30, 30)))
    with pytest.raises(ValueError):
        avl_tree.get_upper_bound(first_tree, 5)
    with pytest.raises(ValueError):
        avl_tree.get_upper_bound(second_tree_tree, 30)


@pytest.mark.parametrize(
    "elements,oder,expected",
    [
        (
            ((50, 50), (60, 60), (40, 40), (30, 30), (45, 45), (55, 55), (65, 65)),
            "preorder",
            [(50, 50), (40, 40), (30, 30), (45, 45), (60, 60), (55, 55), (65, 65)],
        ),
        (
            ((50, 50), (60, 60), (40, 40), (30, 30), (45, 45), (55, 55), (65, 65)),
            "inorder",
            [(30, 30), (40, 40), (45, 45), (50, 50), (55, 55), (60, 60), (65, 65)],
        ),
        (
            ((50, 50), (60, 60), (40, 40), (30, 30), (45, 45), (55, 55), (65, 65)),
            "postorder",
            [(30, 30), (45, 45), (40, 40), (55, 55), (65, 65), (60, 60), (50, 50)],
        ),
    ],
)
def test_traverse(elements, oder, expected):
    new_tree = create_dummy_tree(elements)
    actual = avl_tree.traverse(new_tree, oder)
    assert actual == expected
