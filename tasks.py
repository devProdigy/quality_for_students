"""Management tasks."""
import sys
from pathlib import Path
from types import MappingProxyType
from typing import List

from invoke import Exit, Failure, Result, UnexpectedExit, task

SAFETY_IGNORE = ()

ROOT = Path(__file__).parent
README = ROOT / "README.md"

DIFF_HELP = MappingProxyType({"diff": "Check only the changed files."})


class _CollectFailures:
    def __init__(self, ctx):
        self._failed: List[Result] = []
        self._ctx = ctx

    def run(self, command: str, **kwargs):
        kwargs.setdefault("warn", True)
        cmd_result: Result = self._ctx.run(command, **kwargs)
        if cmd_result.ok:
            self._ctx.run("echo Ok")
        else:
            self._failed.append(cmd_result)

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        if self._failed:
            raise UnexpectedExit(self._failed[0])


def _get_changed_files(ctx, extension=".py"):
    output = ctx.run("git diff --name-only", hide=True).stdout
    return {f for f in output.splitlines() if extension and f.endswith(extension)}


@task
def test(ctx):
    """Run unit tests."""
    # Note: use commandline arguments instead of using `adopts` in `setup.cfg`,
    # since pytest-cov breaks Intellij IDEA debugger.
    ctx.run("poetry run pytest --cov=app -vv tests/unit", pty=True)


@task(help=DIFF_HELP)
def check(ctx, diff=False):
    """Run all static checks."""
    ok = True
    for check_task in (check_code, check_safety):
        print("+" * 10, "inv", check_task.name.replace("_", "-"), "+" * 10)
        try:
            check_task(ctx, diff=diff)
        except Failure:
            ok = False
        print()

    if ok:
        print("All checks passed.")
    else:
        raise Exit("One or more checks failed.")


@task(help=DIFF_HELP)
def check_code(ctx, diff=False):
    """Run static checks on Python code."""
    files_to_check = _join(_get_changed_files(ctx)) if diff else ""
    if diff and not files_to_check:
        print("No changed files, skipping.")
        return

    with _CollectFailures(ctx) as new_ctx:
        print("Checking Black formatting.")
        new_ctx.run(f"poetry run black  --check -- { files_to_check or '.' }")

        print("Checking the style.")
        new_ctx.run(f"poetry run flake8 -- { files_to_check }")

        print("Checking type safety.")
        new_ctx.run(f"poetry run mypy { files_to_check or '.' }")


@task
def check_safety(ctx, **_):
    """Check third-party dependencies for known security vulnerabilities."""
    print("Checking the libraries.")
    ignores = _join(f"--ignore { n }" for n in SAFETY_IGNORE)
    if SAFETY_IGNORE:
        print("WARNING: Ignored issues:", ", ".join(SAFETY_IGNORE), file=sys.stderr)
    ctx.run(f"poetry run safety check --full-report { ignores }")


@task(help=DIFF_HELP)
def fmt(ctx, diff=False):
    """Apply automatic code formatting."""
    files_to_check = _join(_get_changed_files(ctx)) if diff else "."
    if not files_to_check:
        print("No changed files, skipping.")
        return

    with _CollectFailures(ctx) as new_ctx:
        new_ctx.run(f"poetry run isort -rc { files_to_check }")
        new_ctx.run(f"poetry run black { files_to_check }")


@task
def run_app(ctx):
    """Run the app in development mode."""
    ctx.run("poetry run python3 app/user_bad_code.py", pty=True)


def _join(values_list):
    """Make space-separated list of values.

    This function exists to make flake8 happy.
    """
    return " ".join(values_list)
