# ComposeEnvCheck

ComposeEnvCheck is a lightweight, offline command‑line tool that validates the environment variables referenced in a `docker‑compose.yml` file against a `.env` file. It reports missing or unused variables, can generate a template `.env` file, and outputs a concise Markdown or JSON report.

## Features

- Parse `${VAR}` references from `docker‑compose.yml` without external dependencies.
- Compare against a `.env` file and report:
  - **Missing** variables (referenced but not defined).
  - **Unused** variables (defined but not referenced).
- Generate a template `.env` file with placeholders.
- Output reports in **Markdown** or **JSON**.
- Dry‑run mode for CI pipelines.

## Installation

```bash
pip install git+https://github.com/ScobieWorks/composeenvcheck.git
```

## Usage

```bash
# Validate current configuration
composeenvcheck --compose docker-compose.yml --env .env

# Generate a template .env file
composeenvcheck --generate-template --compose docker-compose.yml --output .env.example
```

## Options

```
--compose PATH          Path to docker‑compose.yml (default: docker-compose.yml)
--env PATH              Path to .env file (default: .env)
--generate-template     Generate a template .env file instead of validating.
--output PATH           Output path for the generated template.
--format {md,json}      Output format for the report (default: md).
--dry-run               Exit with status 0 even if missing variables are found.
--help                  Show help message.
```

## License

MIT License


<!-- ORION-MONETIZATION:START -->
## Support

Donate to support continued maintenance: https://paypal.me/Damonwill
<!-- ORION-MONETIZATION:END -->
