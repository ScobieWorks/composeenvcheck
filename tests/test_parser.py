import re
from pathlib import Path
from composeenvcheck.parser import find_env_vars_in_compose

def test_find_env_vars(tmp_path):
    compose = tmp_path / "docker-compose.yml"
    compose.write_text("services:\n  app:\n    environment:\n      - DB_HOST=${DB_HOST}\n      - API_KEY=${API_KEY}\n")
    vars = find_env_vars_in_compose(compose)
    assert vars == {"DB_HOST", "API_KEY"}
