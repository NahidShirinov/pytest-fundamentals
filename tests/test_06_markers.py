# TASK 6: Marker-lər — skip, skipif, xfail, custom
import sys
import pytest
from app.calculator import add


@pytest.mark.smoke
def test_smoke_add():
    assert add(1, 1) == 2


@pytest.mark.skip(reason="Hələ implement olunmayıb")
def test_future_feature():
    assert False


@pytest.mark.skipif(sys.platform == "win32", reason="Windows-da işləmir")
def test_unix_only():
    assert True


@pytest.mark.xfail(reason="Float dəqiqliyi — bilinən problem")
def test_float_bug():
    assert 0.1 + 0.2 == 0.3


@pytest.mark.slow
def test_slow_operation():
    assert sum(range(1_000_000)) == 499999500000
