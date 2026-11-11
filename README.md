# doc-qa-cli

Answer questions about a folder of Markdown and text files with an injected LLM, lexical retrieval, escaped excerpts and citations whose verbatim quotes are verified.

[![PyPI version](https://img.shields.io/pypi/v/trysac-doc-qa-cli)](https://pypi.org/project/trysac-doc-qa-cli/)
[![Python versions](https://img.shields.io/pypi/pyversions/trysac-doc-qa-cli)](https://pypi.org/project/trysac-doc-qa-cli/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)

## Features

- Load paragraphs from `.md` and `.txt` files with size, encoding and symlink safety.
- Lexical retrieval using casefolded token overlap and IDF scoring.
- Injected LLM through a tiny `LLMPort` protocol (bring your own provider).
- Every citation quote is verified against the excerpt before a result is marked verified.
- NOT_FOUND handling when no excerpt matches the question or the model says so.
- Zero runtime dependencies.

## Installation

```bash
pip install trysac-doc-qa-cli
```

## Usage

### Library

```python
from doc_qa_cli import load_folder, answer, RecordedLLM

corpus = load_folder("docs")
llm = RecordedLLM(['It listens on port 8080 [README.md#2: "listens on port 8080"].'])
result = answer("Which port?", corpus, llm)
print(result.text, result.verified)
```

### CLI

```bash
doc-qa-cli search docs "port"
doc-qa-cli ask docs "Which port?" --llm my_provider:make
```

`search` prints one chunk id per line. `ask` prints the model answer followed by all extracted citations, and returns exit code 0 when every quotation is verified, 1 otherwise, 2 for usage/IO errors.

See `docs/` for architecture, security and testing information.
