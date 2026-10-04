# Əlavə Task 3: eyni session fixture başqa faylda — yenidən YARADILMIR
from tests.conftest import SESSION_CALLS


def test_session_config_other_file(app_config):
    assert app_config["env"] == "test"
    assert len(SESSION_CALLS) == 1
