"""ComposeEnvCheck package.

This file is executed when the package is imported.  The project uses a
``src`` layout, so the package lives in ``src/composeenvcheck``.  When the
tests run, the current working directory is the project root, which does
not contain a top‑level ``composeenvcheck`` package.  Importing
``composeenvcheck`` therefore fails unless the ``src`` directory is added
to ``sys.path``.

To make the package importable both when the project is installed (where
``src`` is on the import path) and when the tests run from the project
root, we expose the real implementation directly from this module.
"""

# Import the real implementation from the src layout.  The relative import
# works because this file resides in src/composeenvcheck.
from . import env, parser, report, main  # noqa: F401

# Re‑export the public API so that ``composeenvcheck.env`` etc. are
# available when the package is imported as a top‑level package.
__all__ = ["env", "parser", "report", "main"]
