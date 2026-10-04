# TASK 3: Bir testi çoxlu data ilə işlət — @pytest.mark.parametrize
import pytest
from app.calculator import add, is_even


@pytest.mark.parametrize("a, b, expected", [
    (1, 2, 3),
    (0, 0, 0),
    (-5, 5, 0),
    (100, 200, 300),
])
def test_add(a, b, expected):
    assert add(a, b) == expected


@pytest.mark.parametrize("n, expected", [(2, True), (3, False), (0, True)],
                         ids=["iki", "uc", "sifir"])
def test_is_even(n, expected):
    assert is_even(n) is expected
