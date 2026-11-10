# doc-qa-cli

[![PyPI version](https://img.shields.io/pypi/v/trysac-doc-qa-cli)](https://pypi.org/project/trysac-doc-qa-cli/)
[![License: MIT](https://img.shields.io/pypi/l/trysac-doc-qa-cli)](LICENSE)
[![CI](https://github.com/Trysac/u217-doc-qa-cli/actions/workflows/ci.yml/badge.svg)](https://github.com/Trysac/u217-doc-qa-cli/actions/workflows/ci.yml)

Answer questions about a folder of Markdown and text files with an injected LLM, lexical retrieval, escaped excerpts and citations whose verbatim quotes are verified

## Problem

Describe in two or three sentences the concrete problem this utility solves, who hits it, and what
they do today without it. Replace this paragraph when the first real feature lands.

## Install

```sh
pip install trysac-doc-qa-cli
# or
uv add trysac-doc-qa-cli
```

Requires Python 3.10 or newer. No runtime dependencies.

## Usage

```python
import doc_qa_cli

# normalize() trims surrounding whitespace and lower-cases the text.
print(doc_qa_cli.normalize("  Hello World "))  # -> "hello world"

# Blank input is rejected explicitly instead of returning an empty string.
try:
    doc_qa_cli.normalize("   ")
except ValueError as exc:
    print(f"rejected: {exc}")
```

## Documentation

- [Architecture](docs/ARCHITECTURE.md) and [decisions](docs/decisions/)
- [Testing](docs/TESTING.md) and [security](docs/SECURITY.md)
- [Project record](docs/PROJECT.md) and [stack](docs/STACK.md)
- [Changelog](CHANGELOG.md) and [contributing guide](CONTRIBUTING.md)

## License

[MIT](LICENSE) (c) 2026 Miguel Gomez
