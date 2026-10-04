# TASK 4: Fixture — `account` conftest.py-dan gəlir
import pytest
from app.bank import InsufficientFunds


def test_initial_balance(account):
    assert account.balance == 100


def test_deposit(account):
    account.deposit(50)
    assert account.balance == 150


def test_withdraw_too_much(account):
    with pytest.raises(InsufficientFunds):
        account.withdraw(500)


def test_fixture_is_fresh(account):
    # Əvvəlki testdə deposit olsa da, burada balans yenə 100-dür
    assert account.balance == 100
