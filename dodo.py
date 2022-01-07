"""
doit tasks.

Most tasks employ nox to create a virtual session for testing.
"""
import re
from itertools import chain
from pathlib import Path
from time import strftime

from doit import task_params

PACKAGE_NAME = "fractopo"
CITATION_CFF_PATH = Path("CITATION.cff")
DEV_REQUIREMENTS_PATH = Path("requirements.txt")
DOCS_REQUIREMENTS_PATH = Path("docs_src/requirements.txt")
PYPROJECT_PATH = Path("pyproject.toml")
PRE_COMMIT_CONFIG_PATH = Path(".pre-commit-config.yaml")
DOCS_SRC_PATH = Path("docs_src")
COVERAGE_SVG_PATH = DOCS_SRC_PATH / Path("imgs/coverage.svg")
POETRY_LOCK_PATH = Path("poetry.lock")
NOXFILE_PATH = Path("noxfile.py")
DATE_RELEASED_STR = "date-released"
UTF8 = "utf-8"
TESTS_NAME = "tests"
DOCS_EXAMPLES = "examples"

VERSION_GLOBS = [
    "*/__init__.py",
    "CITATION.cff",
    "pyproject.toml",
]

VERSION_PATTERN = r"(^_*version_*\s*[:=]\s\").*\""

ACTIONS = "actions"
FILE_DEP = "file_dep"
TASK_DEP = "task_dep"
TARGETS = "targets"
NAME = "name"
PARAMS = "params"
PACKAGE_INIT_PATH = Path(PACKAGE_NAME) / "__init__.py"
CHANGELOG_PATH = Path("CHANGELOG.md")
DODO_PATH = Path("dodo.py")

PYTHON_SRC_FILES = [
    path for path in Path(PACKAGE_NAME).rglob("*.py") if "__init__" not in path.name
]
PYTHON_TEST_FILES = list(Path(TESTS_NAME).rglob("*.py"))

PYTHON_UTIL_FILES = [
    *list(Path(DOCS_EXAMPLES).rglob("*.py")),
    *list(Path(".").glob("*.py")),
]
PYTHON_ALL_FILES = [*PYTHON_SRC_FILES, *PYTHON_TEST_FILES, *PYTHON_UTIL_FILES]
NOTEBOOKS = [
    *list(Path("notebooks").rglob("*.ipynb")),
    *list(Path("docs_src").rglob("*.ipynb")),
]
DOCS_FILES = list(Path("docs_src").rglob("*.rst"))

PYTHON_VERSIONS = ["3.7", "3.8", "3.9"]
DEFAULT_PYTHON_VERSION = "3.8"

# Define default tasks
DOIT_CONFIG = {
    "default_tasks": [
        "requirements",
        "format",
        "lint",
        "update_version",
        "ci_test",
        "docs",
        "notebooks",
        "build",
        "citation",
        "changelog",
        "codespell",
    ]
}


def resolve_task_name(func) -> str:
    """
    Resolve name of task without ``task_`` prefix.
    """
    return func.__name__.replace("task_", "")


def task_requirements():
    """
    Sync requirements from poetry.lock.
    """
    command = "nox --session requirements"
    return {
        FILE_DEP: [POETRY_LOCK_PATH, PYPROJECT_PATH, NOXFILE_PATH, DODO_PATH],
        ACTIONS: [command],
        TARGETS: [DEV_REQUIREMENTS_PATH, DOCS_REQUIREMENTS_PATH],
    }


def task_pre_commit():
    """
    Verify that pre-commit is installed, install its hooks and run them.
    """
    return {
        ACTIONS: [
            "pre-commit install",
            "pre-commit install --hook-type commit-msg",
            "pre-commit run --all-files",
        ],
        FILE_DEP: [
            *PYTHON_ALL_FILES,
            PYPROJECT_PATH,
            POETRY_LOCK_PATH,
            PRE_COMMIT_CONFIG_PATH,
            DODO_PATH,
        ],
    }


def task_format():
    """
    Format everything.
    """
    command = "nox --session format"
    return {
        FILE_DEP: [
            *PYTHON_ALL_FILES,
            *NOTEBOOKS,
            *DOCS_FILES,
            DEV_REQUIREMENTS_PATH,
            NOXFILE_PATH,
            DODO_PATH,
        ],
        ACTIONS: [command],
        TASK_DEP: [resolve_task_name(task_pre_commit)],
    }


def task_lint():
    """
    Lint everything.
    """
    command = "nox --session lint"
    return {
        FILE_DEP: [
            *PYTHON_ALL_FILES,
            *NOTEBOOKS,
            *DOCS_FILES,
            DEV_REQUIREMENTS_PATH,
            NOXFILE_PATH,
            DODO_PATH,
        ],
        ACTIONS: [command],
        TASK_DEP: [resolve_task_name(task_pre_commit), resolve_task_name(task_format)],
    }


def task_update_version():
    """
    Update pyproject.toml and package/__init__.py version strings.
    """
    command = "nox --session update_version"
    return {
        FILE_DEP: [
            *PYTHON_SRC_FILES,
            PYPROJECT_PATH,
            POETRY_LOCK_PATH,
            NOXFILE_PATH,
            DODO_PATH,
        ],
        TASK_DEP: [resolve_task_name(task_format)],
        ACTIONS: [command],
    }


def task_ci_test():
    """
    Test suite for continous integration testing.

    Installs with pip, tests with pytest and checks coverage with coverage.
    """
    # python_version = "" if len(python) == 0 else f"-p {python}"
    for python_version in PYTHON_VERSIONS:
        command = f"nox --session tests_pip -p {python_version}"
        yield {
            NAME: python_version,
            FILE_DEP: [
                *PYTHON_SRC_FILES,
                *PYTHON_TEST_FILES,
                DEV_REQUIREMENTS_PATH,
                PYPROJECT_PATH,
                DODO_PATH,
            ],
            TASK_DEP: [resolve_task_name(task_format)],
            ACTIONS: [command],
            **(
                {TARGETS: [COVERAGE_SVG_PATH]}
                if python_version == DEFAULT_PYTHON_VERSION
                else dict()
            ),
        }


def task_docs():
    """
    Make documentation to docs using nox.
    """
    command = f"nox --session docs"
    return {
        ACTIONS: [command],
        FILE_DEP: [
            *PYTHON_ALL_FILES,
            *DOCS_FILES,
            DOCS_REQUIREMENTS_PATH,
            NOXFILE_PATH,
            DODO_PATH,
        ],
        TASK_DEP: [
            resolve_task_name(task_format),
            resolve_task_name(task_lint),
            resolve_task_name(task_update_version),
        ],
        TARGETS: ["docs"],
    }


def task_notebooks():
    """
    Execute and fill notebooks.
    """
    command = "nox --session notebooks"
    return {
        FILE_DEP: [
            *PYTHON_SRC_FILES,
            *NOTEBOOKS,
            DEV_REQUIREMENTS_PATH,
            NOXFILE_PATH,
            DODO_PATH,
        ],
        TASK_DEP: [resolve_task_name(task_format)],
        ACTIONS: [command],
    }


def task_build():
    """
    Build package with poetry.
    """
    command = "nox --session build"
    return {
        ACTIONS: [command],
        FILE_DEP: [
            *PYTHON_SRC_FILES,
            PYPROJECT_PATH,
            POETRY_LOCK_PATH,
            NOXFILE_PATH,
            DODO_PATH,
        ],
        TASK_DEP: [resolve_task_name(task_format)],
    }


def task_typecheck():
    """
    Typecheck ``[[ package ]]`` with ``mypy``.
    """
    command = "nox --session typecheck"
    # command = "nox --session build"
    return {
        ACTIONS: [command],
        FILE_DEP: [
            *PYTHON_SRC_FILES,
            DEV_REQUIREMENTS_PATH,
            NOXFILE_PATH,
            DODO_PATH,
        ],
        TASK_DEP: [resolve_task_name(task_format)],
    }


def task_performance_profile():
    """
    Profile [[ package ]] performance with ``pyinstrument``.
    """
    command = "nox --session profile_performance"
    # command = "nox --session build"
    return {
        ACTIONS: [command],
        FILE_DEP: [
            *PYTHON_SRC_FILES,
            *PYTHON_TEST_FILES,
            DEV_REQUIREMENTS_PATH,
            NOXFILE_PATH,
            DODO_PATH,
        ],
    }


def task_citation():
    """
    Sync and validate CITATION.cff.
    """
    citation_text = CITATION_CFF_PATH.read_text(UTF8)
    citation_lines = citation_text.splitlines()
    if DATE_RELEASED_STR not in citation_text:
        raise ValueError(
            f"Expected to find {DATE_RELEASED_STR} str in {CITATION_CFF_PATH}."
            f"\nCheck & validate {CITATION_CFF_PATH}."
        )
    date = strftime("%Y-%m-%d")
    new_lines = [
        line if "date-released" not in line else f'date-released: "{date}"'
        for line in citation_lines
    ]
    CITATION_CFF_PATH.write_text("\n".join(new_lines), encoding=UTF8)

    command = "nox --session validate_citation_cff"
    return {
        ACTIONS: [command],
        FILE_DEP: [
            *PYTHON_SRC_FILES,
            PYPROJECT_PATH,
            POETRY_LOCK_PATH,
            NOXFILE_PATH,
            DODO_PATH,
        ],
        TARGETS: [CITATION_CFF_PATH],
    }


def task_changelog():
    """
    Generate changelog.
    """
    command = "nox --session changelog"
    return {
        ACTIONS: [command],
        FILE_DEP: [
            *PYTHON_SRC_FILES,
            PYPROJECT_PATH,
            POETRY_LOCK_PATH,
            NOXFILE_PATH,
            DODO_PATH,
        ],
        TARGETS: [CHANGELOG_PATH],
    }


def task_codespell():
    """
    Check code spelling.
    """
    command = "nox --session codespell"
    return {
        ACTIONS: [command],
        FILE_DEP: [
            *PYTHON_ALL_FILES,
            PYPROJECT_PATH,
            POETRY_LOCK_PATH,
            NOXFILE_PATH,
            DODO_PATH,
        ],
        TASK_DEP: [resolve_task_name(task_format)],
    }


def parse_tag(tag: str) -> str:
    return tag if "v" not in tag else tag[1:]


def tag(tag: str):
    """
    Setup new tag in
    """
    assert len(tag) != 0
    tag = parse_tag(tag)
    # Remove v at the start of tag

    def replace_version_string(path: Path, tag: str):
        """
        Replace version string in file at path.
        """
        # Collect new lines
        new_lines = []
        for line in path.read_text(UTF8).splitlines():

            # Substitute lines with new tag if they match pattern
            substituted = re.sub(VERSION_PATTERN, r"\g<1>" + tag + r'"', line)

            # Report to user
            if line != substituted:
                print(
                    f"Replacing version string:\n{line}\nin"
                    f" {path} with:\n{substituted}\n"
                )
                new_lines.append(substituted)
            else:
                # No match, append line anyway
                new_lines.append(line)

        # Write results to file
        path.write_text("\n".join(new_lines), encoding=UTF8)

    # Iterate over all files determined from VERSION_GLOBS
    for path in chain(*[Path(".").glob(glob) for glob in (VERSION_GLOBS)]):
        replace_version_string(path=path, tag=tag)

    cmds = (
        "# Run pre-commit to check files.",
        "pre-commit run --all-files",
        "git add .",
        "# Make sure only version updates are committed!",
        "git commit -m 'docs: update version'",
        "# Make sure tag is proper and add annotation as wanted.",
        f"git tag -a v{tag} -m 'Release {tag}.'",
    )
    print("Not running git cmds. See below for suggested commands:\n---\n")
    for cmd in cmds:
        print(cmd)


# def tag(c, tag="", annotation=""):
@task_params([{NAME: "tag", "default": "", "type": str, "long": "tag"}])
def task_tag(tag: str):
    """
    Make new tag and update version strings accordingly
    """
    # Create changelog with 'tag' as latest version
    create_changelog = "nox --session changelog -- %(tag)"
    return {
        # NAME: "create changelog for tag and update version strings",
        ACTIONS: [create_changelog, tag],
    }
