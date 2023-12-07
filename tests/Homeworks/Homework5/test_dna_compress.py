from src.Homeworks.Homework5 import dna_compress
import pytest


@pytest.mark.parametrize(
    "string,expected",
    [
        ("ggfffds", "g2f3d1s1"),
        ("GGhfDDDDDdk", "G2h1f1D5d1k1"),
        ("qweйцу", "q1w1e1й1ц1у1"),
    ],
)
def test_encode_string(string, expected):
    actual = dna_compress.encode_string(string)
    assert actual == expected


@pytest.mark.parametrize(
    "string, expected",
    [
        ("g2H3G7k1$", "ggHHHGGGGGGGk"),
        ("q1w2E3ю4ь1$", "qwwEEEююююь"),
        ("q10h11j1$", "qqqqqqqqqqhhhhhhhhhhhj"),
    ],
)
def test_decode_string(string, expected):
    actual = dna_compress.decode_string(string)
    assert actual == expected


@pytest.mark.parametrize(
    "string,expected",
    [
        ("gghhssssss", True),
        ("qqqqqqqqqqqqq", True),
        ("g1h1j1k1l1", False),
        ("g100h20", False),
        ("gg1j2", False),
        ("1h2g", False),
        ("g", True),
    ],
)
def test_validate_input_for_encode(string, expected):
    actual = dna_compress.validate_input_for_encode(string)
    assert actual == expected


@pytest.mark.parametrize(
    "string,expected",
    [
        ("gfg", False),
        ("1h3j4", False),
        ("f4j5k", False),
        ("123", False),
        ("f01k4", False),
        ("h1j2k3", True),
    ],
)
def test_validate_input_for_decode(string, expected):
    actual = dna_compress.validate_input_for_decode(string)
    assert actual == expected
