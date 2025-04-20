# chercher-plugin - Cookiecutter Template

A Cookiecutter template to simplify the process of building a new plugin for [Chercher](https://github.com/dnlzrgz/chercher).

## Installation

First, you'll need to have [cookiecutter](https://www.cookiecutter.io) installed, or at least a way to execute it. For example, you can install it using `uv` as follows:

```bash
uv tool install cookiecutter
```

Alternatively, you can just run it like this:

```bash
uvx cookiecutter
```

> [!NOTE]
> While I believe that `uv` and, consequently, `uvx` is a great way to run this project, you're totally free to use something like `poetry`, `pipx` or simply `pip`.

## Usage

To start building a plugin for Chercher, run the following command:

```bash
uvx cookiecutter gh:dnlzrgz/chercher-plugin
```

You will then be prompted to fill in the following fields:

```txt
[1/6] plugin_name ():
[2/6] description ():
[3/6] hyphenated ():
[4/6] underscored ():
[5/6] github_username ():
[6/6] author_name ():
```

> [!TIP]
> I strongly recommended to accept the suggested values for "hyphenated" and "underscored" by simply hitting enter at those prompts.

## Developing a Plugin

After creating the new plugin structure from the template, it's time to start working on your plugin.

> [!TIP]
> If you need examples, check out the [chercher-plugin-txt](https://github.com/dnlzrgz/chercher-plugin-txt) or the [chercher-plugin-epub](https://github.com/dnlzrgz/chercher-plugin-epub) repositories.

### A few things to keep in mind

Your plugin should not attempt to support every file extension available. Instead, focus on supporting a single file type or webpage type.

Note that the `ingest` hook receives a URI, as well as a dictionary object containing the `settings`, if needed. It is the responsibility of each plugin to filter out the documents that they cannot manage.

Lastly, keep in mind that Chercher is under active development. While it is unlikely that the `ingest` hook definition will change, the `Document` model may evolve, and new hooks may be defined in the future.

## GitHub workflows and PyPi

> [!NOTE]
> TODO
