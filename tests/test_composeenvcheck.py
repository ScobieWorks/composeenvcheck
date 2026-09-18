import subprocess
import sys
import textwrap
from pathlib import Path

# Helper to run the CLI and capture output

def run_cli(args, cwd=None):
    cmd = [sys.executable, "-m", "composeenvcheck.main"] + args
    result = subprocess.run(cmd, cwd=cwd, capture_output=True, text=True)
    return result


def test_generate_template(tmp_path):
    compose = tmp_path / "docker-compose.yml"
    compose.write_text(textwrap.dedent("""
        version: "3"
        services:
          web:
            image: nginx
            environment:
              - DB_HOST=${DB_HOST}
              - API_KEY=${API_KEY}
    """))
    output = tmp_path / ".env.example"
    result = run_cli(["--generate-template", "--compose", str(compose), "--output", str(output)])
    assert result.returncode == 0
    assert output.read_text().strip() == "API_KEY=PLACEHOLDER\nDB_HOST=PLACEHOLDER"


def test_missing_and_unused(tmp_path):
    compose = tmp_path / "docker-compose.yml"
    compose.write_text(textwrap.dedent("""
        services:
          app:
            environment:
              - FOO=${FOO}
              - BAR=${BAR}
    """))
    env = tmp_path / ".env"
    env.write_text("FOO=foo\nBAZ=bar\n")
    result = run_cli(["--compose", str(compose), "--env", str(env), "--format", "json"])
    assert result.returncode == 1  # missing BAR
    import json
    data = json.loads(result.stdout)
    assert set(data["missing"]) == {"BAR"}
    assert set(data["unused"]) == {"BAZ"}


def test_dry_run(tmp_path):
    compose = tmp_path / "docker-compose.yml"
    compose.write_text("services:\n  app:\n    environment:\n      - FOO=${FOO}\n")
    env = tmp_path / ".env"
    env.write_text("BAR=bar\n")
    result = run_cli(["--compose", str(compose), "--env", str(env), "--dry-run"])
    assert result.returncode == 0
