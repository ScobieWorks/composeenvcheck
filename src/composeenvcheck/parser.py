"""Parse docker‑compose.yml for ${VAR} references."""
import re
from pathlib import Path

ENV_VAR_PATTERN = re.compile(r"\$\{([^}]+)\}")

def find_env_vars_in_compose(compose_path: Path) -> set[str]:
    """Return a set of variable names referenced in the compose file.

    The function reads the file as plain text and extracts all occurrences of
    ``${VAR}`` using a regular expression. It does not attempt to parse YAML.
    """
    text = compose_path.read_text(encoding="utf-8")
    return set(ENV_VAR_PATTERN.findall(text))
