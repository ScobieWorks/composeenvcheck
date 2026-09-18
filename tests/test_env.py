from pathlib import Path
from composeenvcheck.env import load_env_file

def test_load_env(tmp_path):
    env_file = tmp_path / ".env"
    env_file.write_text("# comment\nFOO=foo\nBAR=bar\n")
    env = load_env_file(env_file)
    assert env == {"FOO": "foo", "BAR": "bar"}
