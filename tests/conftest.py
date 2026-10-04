# conftest.py — buradakı fixture-lar bütün test fayllarında import etmədən görünür
import pytest
from app.bank import BankAccount


@pytest.fixture
def account():
    """Hər test üçün TƏZƏ hesab (function scope — default)."""
    return BankAccount("Nahid", balance=100)
