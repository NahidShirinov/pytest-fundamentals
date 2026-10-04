# TASK 8: Daxili fixture-lar — tmp_path, capsys, monkeypatch
from app.utils import greet, save_lines, read_lines, get_env_mode


def test_save_and_read(tmp_path):
    f = tmp_path / "data.txt"          # müvəqqəti qovluq, test bitəndə təmizlənir
    save_lines(f, ["a", "b", "c"])
    assert read_lines(f) == ["a", "b", "c"]


def test_greet_output(capsys):
    greet("Nahid")
    captured = capsys.readouterr()     # print çıxışını tutur
    assert captured.out == "Salam, Nahid!\n"


def test_env_default(monkeypatch):
    monkeypatch.delenv("APP_MODE", raising=False)
    assert get_env_mode() == "dev"


def test_env_prod(monkeypatch):
    monkeypatch.setenv("APP_MODE", "prod")   # test bitəndə avtomatik geri qaytarılır
    assert get_env_mode() == "prod"
