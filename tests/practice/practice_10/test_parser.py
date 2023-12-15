from src.practice.practice_10.parser import parse, ParseTree, pretty_print
import pytest


@pytest.mark.parametrize(
    "tokens,expected",
    [
        (
            ["5"],
            ParseTree(
                "START",
                [
                    ParseTree(
                        "T",
                        [
                            ParseTree("TOKEN", [ParseTree("id(5)", None)]),
                            ParseTree("PROD", [ParseTree("eps", None)]),
                        ],
                    ),
                    ParseTree("SUM", [ParseTree("eps", None)]),
                ],
            ),
        ),
        (
            ["5", "+", "3", "*", "8"],
            ParseTree(
                "START",
                [
                    ParseTree(
                        "T",
                        [
                            ParseTree("TOKEN", [ParseTree("id(5)", None)]),
                            ParseTree("PROD", [ParseTree("eps", None)]),
                        ],
                    ),
                    ParseTree(
                        "SUM",
                        [
                            ParseTree("+", None),
                            ParseTree(
                                "T",
                                [
                                    ParseTree("TOKEN", [ParseTree("id(3)", None)]),
                                    ParseTree(
                                        "PROD",
                                        [
                                            ParseTree("*", None),
                                            ParseTree(
                                                "TOKEN", [ParseTree("id(8)", None)]
                                            ),
                                            ParseTree("PROD", [ParseTree("eps", None)]),
                                        ],
                                    ),
                                ],
                            ),
                            ParseTree("SUM", [ParseTree("eps", None)]),
                        ],
                    ),
                ],
            ),
        ),
    ],
)
def test_parse(tokens, expected):
    actual = parse(tokens)
    assert actual == expected


@pytest.mark.parametrize(
    "parse_tree,expected",
    [
        (
            parse(["5"]),
            "START\n"
            "....T\n"
            "........TOKEN\n"
            "............id(5)\n"
            "........PROD\n"
            "............eps\n"
            "....SUM\n"
            "........eps\n",
        ),
        (
            parse(["5", "+", "3", "*", "8"]),
            "START\n"
            "....T\n"
            "........TOKEN\n"
            "............id(5)\n"
            "........PROD\n"
            "............eps\n"
            "....SUM\n"
            "........+\n"
            "........T\n"
            "............TOKEN\n"
            "................id(3)\n"
            "............PROD\n"
            "................*\n"
            "................TOKEN\n"
            "....................id(8)\n"
            "................PROD\n"
            "....................eps\n"
            "........SUM\n"
            "............eps\n",
        ),
    ],
)
def test_pretty_print(parse_tree, expected, capfd):
    pretty_print(parse_tree)
    out, err = capfd.readouterr()
    assert out == expected


@pytest.mark.parametrize(
    "tokens", [["5", "+", "+"], ["5", "9"], ["(", "3", "*", "4", "+", "6"]]
)
def test_raise_exception(tokens):
    with pytest.raises(ValueError):
        parse(tokens)
