from src.Tests.final_test import sprites
import pytest
import random
from math import ceil
from io import StringIO


def create_dummy_matrix(size):
    return [[random.randint(0, 1) for j in range(size)] for i in range(size)]


@pytest.mark.parametrize("size", [3, 4, 5, 6, 7])
def test_create_horizontal_symmetry(size):
    matrix = create_dummy_matrix(size)
    matrix = sprites.create_horizontal_symmetry(matrix, size)
    for string in range(size):
        for column in range(size):
            assert matrix[string][column] == matrix[size - string - 1][column]


@pytest.mark.parametrize("size", [3, 4, 5, 6, 7])
def test_create_vertical_symmetry(size):
    matrix = create_dummy_matrix(size)
    matrix = sprites.create_vertical_symmetry(matrix, size)
    for string in matrix:
        assert string[: size // 2] == string[-(size // 2) :][::-1]


@pytest.mark.parametrize("size", [3, 4, 5, 6, 7])
def test_create_vertical_and_horizontal(size):
    matrix = create_dummy_matrix(size)
    matrix = sprites.create_horizontal_and_vertical_symmetry(matrix, size)
    for string in matrix:
        assert string[: size // 2] == string[-(size // 2) :][::-1]
    for string in range(size):
        for column in range(size):
            assert matrix[string][column] == matrix[size - string - 1][column]


@pytest.mark.parametrize(
    "sprite,expected",
    [
        (
            [[1, 0, 1, 0], [1, 1, 0, 0], [1, 1, 0, 0], [1, 0, 1, 0]],
            "■□■□\n■■□□\n■■□□\n■□■□\n",
        ),
        (
            [
                [1, 1, 0, 1, 1],
                [0, 1, 1, 1, 0],
                [0, 0, 1, 0, 0],
                [0, 1, 1, 1, 0],
                [1, 1, 0, 1, 1],
            ],
            "■■□■■\n□■■■□\n□□■□□\n□■■■□\n■■□■■\n",
        ),
        (
            [[1, 0, 0, 1], [0, 1, 1, 0], [0, 1, 1, 0], [1, 0, 0, 1]],
            "■□□■\n□■■□\n□■■□\n■□□■\n",
        ),
    ],
)
def test_pretty_print_sprite(monkeypatch, sprite, expected):
    monkeypatch.setattr("builtins.input", lambda _: "")
    fake_output = StringIO()
    monkeypatch.setattr("sys.stdout", fake_output)
    sprites.pretty_print_sprite(sprite)
    output = fake_output.getvalue()
    assert output.split() == expected.split()


@pytest.mark.parametrize("size", ["1", "0", "-1", "-1000"])
def test_main_scenario(monkeypatch, size):
    monkeypatch.setattr("builtins.input", lambda _: size)
    fake_output = StringIO()
    monkeypatch.setattr("sys.stdout", fake_output)
    sprites.main()
    output = fake_output.getvalue()
    assert output == "error sprite size\n"
