# TASK 2: Exception yoxlama — pytest.raises
import pytest
from app.calculator import divide


def test_divide_by_zero():
    with pytest.raises(ZeroDivisionError):
        divide(10, 0)


def test_divide_by_zero_message():
    # match= regex ilə mesajı yoxlayır
    with pytest.raises(ZeroDivisionError, match="bölmək olmaz"):
        divide(1, 0)
