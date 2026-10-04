# TASK 5: yield fixture (setup/teardown) və scope
import pytest

events = []


@pytest.fixture(scope="module")
def db_connection():
    events.append("connect")      # SETUP — modul üçün 1 dəfə
    yield {"connected": True}
    events.append("disconnect")   # TEARDOWN — moduldakı son testdən sonra


def test_first(db_connection):
    assert db_connection["connected"]


def test_second(db_connection):
    # scope="module" olduğu üçün connect yalnız 1 dəfə çağırılıb
    assert events.count("connect") == 1
