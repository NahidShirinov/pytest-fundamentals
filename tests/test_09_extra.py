# Əlavə tasklar 1, 2, 4, 5 + Task 3-ün birinci istifadəsi
import pytest
from app import utils
from app.bank import BankAccount
from app.calculator import divide
from tests.conftest import SESSION_CALLS


# --- Əlavə Task 1: mənfi deposit ValueError atmalıdır ---
@pytest.mark.parametrize("amount", [-10, 0])
def test_deposit_non_positive_raises(account, amount):
    with pytest.raises(ValueError, match="müsbət"):
        account.deposit(amount)
    assert account.balance == 100   # balans dəyişməməlidir


# --- Əlavə Task 2: divide() üçün 5 hal ---
@pytest.mark.parametrize("a, b, expected", [
    (10, 2, 5),
    (-9, 3, -3),
    (-8, -2, 4),
    (7.5, 2.5, 3),
    (10**12, 10**6, 10**6),
], ids=["musbet", "menfi", "iki-menfi", "float", "boyuk"])
def test_divide_cases(a, b, expected):
    assert divide(a, b) == pytest.approx(expected)


# --- Əlavə Task 3: session fixture (2-ci istifadə test_10_session.py-dadır) ---
def test_session_config_here(app_config):
    assert app_config["currency"] == "AZN"
    assert len(SESSION_CALLS) == 1


# --- Əlavə Task 4: monkeypatch.setattr ---
def test_patch_get_env_mode(monkeypatch):
    monkeypatch.setattr(utils, "get_env_mode", lambda: "mocked")
    assert utils.get_env_mode() == "mocked"


def test_patch_is_restored():
    # monkeypatch əvvəlki testdən sonra orijinal funksiyanı geri qaytarıb
    assert utils.get_env_mode() != "mocked"


# --- Əlavə Task 5: parametrize olunmuş fixture ---
@pytest.fixture(params=[0, 50, 1000], ids=lambda b: f"balans={b}")
def any_account(request):
    return BankAccount("Test", balance=request.param)


def test_deposit_any_balance(any_account):
    start = any_account.balance
    any_account.deposit(25)
    assert any_account.balance == start + 25


def test_withdraw_all(any_account):
    any_account.withdraw(any_account.balance)
    assert any_account.balance == 0
