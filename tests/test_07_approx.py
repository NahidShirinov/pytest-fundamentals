# TASK 7: Float müqayisəsi — pytest.approx
import pytest
from app.calculator import divide


def test_float_sum():
    assert 0.1 + 0.2 == pytest.approx(0.3)


def test_divide_float():
    assert divide(1, 3) == pytest.approx(0.3333, rel=1e-3)
