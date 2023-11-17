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
        ("g2H3G7k1", "ggHHHGGGGGGGk"),
        ("q1w2E3ю4ь1", "qwwEEEююююь"),
        ("ы6ъ2э1", "ыыыыыыъъэ"),
    ],
)
def test_decode_string(string, expected):
    actual = dna_compress.decode_string(string)
    assert actual == expected


@pytest.mark.parametrize("string", ["dhd7", "x[sxc", "djjf ", "dkc.ckc"])
def test_validate_input_encode(string):
    with pytest.raises(ValueError):
        dna_compress.validate_input_encode(string)


@pytest.mark.parametrize("string", ["gf7", "x[sxc", "djjf ", "dkc.ckc", "g3g4", "g34h"])
def test_validate_input_decode(string):
    with pytest.raises(ValueError):
        dna_compress.validate_input_decode(string)
