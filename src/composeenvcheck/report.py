"""Generate reports and templates."""
from pathlib import Path

def generate_report(referenced: set[str], defined: dict[str, str]):
    """Return (missing, unused) sets.

    *missing* – variables referenced in the compose file but not defined in
    the .env file.
    *unused* – variables defined in the .env file but not referenced.
    """
    defined_keys = set(defined.keys())
    missing = referenced - defined_keys
    unused = defined_keys - referenced
    return missing, unused

def generate_template(referenced: set[str], output_path: Path):
    """Write a template .env file with placeholders.

    Each referenced variable is written as ``VAR=PLACEHOLDER``.
    """
    lines = [f"{var}=PLACEHOLDER" for var in sorted(referenced)]
    output_path.write_text("\n".join(lines) + "\n", encoding="utf-8")
