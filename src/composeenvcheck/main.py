"""Entry point for the composeenvcheck CLI."""
import argparse
import sys
from pathlib import Path

from .parser import find_env_vars_in_compose
from .env import load_env_file
from .report import generate_report, generate_template


def parse_args(argv=None):
    parser = argparse.ArgumentParser(description="Validate docker‑compose.yml environment variables against a .env file.")
    parser.add_argument("--compose", default="docker-compose.yml", help="Path to docker‑compose.yml (default: docker-compose.yml)")
    parser.add_argument("--env", default=".env", help="Path to .env file (default: .env)")
    parser.add_argument("--generate-template", action="store_true", help="Generate a template .env file instead of validating.")
    parser.add_argument("--output", help="Output path for the generated template.")
    parser.add_argument("--format", choices=["md", "json"], default="md", help="Output format for the report (default: md).")
    parser.add_argument("--dry-run", action="store_true", help="Exit with status 0 even if missing variables are found.")
    return parser.parse_args(argv)


def main(argv=None):
    args = parse_args(argv)
    compose_path = Path(args.compose)
    env_path = Path(args.env)

    if not compose_path.is_file():
        print(f"Error: compose file '{compose_path}' not found.", file=sys.stderr)
        sys.exit(1)

    if args.generate_template:
        if not args.output:
            print("Error: --output is required when generating a template.", file=sys.stderr)
            sys.exit(1)
        template_path = Path(args.output)
        referenced = find_env_vars_in_compose(compose_path)
        generate_template(referenced, template_path)
        print(f"Template written to {template_path}")
        sys.exit(0)

    if not env_path.is_file():
        print(f"Error: env file '{env_path}' not found.", file=sys.stderr)
        sys.exit(1)

    referenced = find_env_vars_in_compose(compose_path)
    defined = load_env_file(env_path)
    missing, unused = generate_report(referenced, defined)

    if args.format == "md":
        report = f"## Missing Variables\n{', '.join(sorted(missing)) if missing else 'None'}\n\n## Unused Variables\n{', '.join(sorted(unused)) if unused else 'None'}"
    else:
        import json
        report = json.dumps({"missing": sorted(missing), "unused": sorted(unused)}, indent=2)

    print(report)

    if missing and not args.dry_run:
        sys.exit(1)

    sys.exit(0)


if __name__ == "__main__":
    main()
