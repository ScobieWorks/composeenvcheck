"""Load .env files into a dictionary."""
from pathlib import Path

def load_env_file(env_path: Path) -> dict[str, str]:
    """Parse a .env file.

    Lines starting with ``#`` or empty lines are ignored. The first ``=`` is
    used to split the key and value. Leading/trailing whitespace is stripped.
    """
    env = {}
    for line in env_path.read_text(encoding="utf-8").splitlines():
        line = line.strip()
        if not line or line.startswith("#"):
            continue
        if "=" not in line:
            continue
        key, value = line.split("=", 1)
        env[key.strip()] = value.strip()
    return env
