import pathlib
from cookiecutter.main import cookiecutter

TEMPLATE_DIRECTORY = str(pathlib.Path(__file__).parent.parent)


def test_generated_files(tmpdir):
    generate(
        tmpdir,
        {
            "plugin_name": "chercher-plugin-ingest-foo",
            "description": "don't panic.",
        },
    )
    assert set(paths(tmpdir)).issuperset(
        {
            "chercher-plugin-ingest-foo",
            "chercher-plugin-ingest-foo/pyproject.toml",
            "chercher-plugin-ingest-foo/README.md",
            "chercher-plugin-ingest-foo/LICENSE",
            "chercher-plugin-ingest-foo/.gitignore",
            "chercher-plugin-ingest-foo/chercher_plugin_ingest_foo",
            "chercher-plugin-ingest-foo/chercher_plugin_ingest_foo/__init__.py",
            "chercher-plugin-ingest-foo/.github",
            "chercher-plugin-ingest-foo/.github/workflows",
            "chercher-plugin-ingest-foo/.github/workflows/.gitkeep",
            "chercher-plugin-ingest-foo/tests",
            "chercher-plugin-ingest-foo/tests/__init__.py",
            "chercher-plugin-ingest-foo/tests/test_chercher_plugin_ingest_foo.py",
        }
    )


def generate(directory, context):
    cookiecutter(
        template=TEMPLATE_DIRECTORY,
        output_dir=str(directory),
        no_input=True,
        extra_context=context,
    )


def paths(directory):
    paths = list(pathlib.Path(directory).glob("**/*"))
    paths = [r.relative_to(directory) for r in paths]
    return {str(f) for f in paths if str(f) != "."}
