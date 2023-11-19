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
        ("gghhssssss", "1"),
        ("qqqqqqqqqqqqq", "1"),
        ("g1h1j1k1l1", "2"),
        ("g100h20", "2"),
        ("gg1j2", ""),
        ("1h2g", ""),
    ],
)
def test_validate_input(string, expected):
    actual = dna_compress.validate_input(string)
    assert actual == expected
