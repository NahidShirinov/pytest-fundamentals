# TASK 1: Sadə assert — add() və is_even() funksiyalarını yoxla
from app.calculator import add, is_even


def test_add_positive():
    assert add(2, 3) == 5


def test_add_negative():
    assert add(-1, -1) == -2


def test_is_even():
    assert is_even(4)
    assert not is_even(7)
