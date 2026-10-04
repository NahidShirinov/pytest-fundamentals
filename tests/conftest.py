# conftest.py — buradakı fixture-lar bütün test fayllarında import etmədən görünür
import pytest
from app.bank import BankAccount


@pytest.fixture
def account():
    """Hər test üçün TƏZƏ hesab (function scope — default)."""
    return BankAccount("Nahid", balance=100)


# Əlavə Task 3: session scope — bütün test sessiyası üçün 1 dəfə yaradılır
SESSION_CALLS = []


@pytest.fixture(scope="session")
def app_config():
    SESSION_CALLS.append(1)
    yield {"env": "test", "currency": "AZN"}
    SESSION_CALLS.clear()
