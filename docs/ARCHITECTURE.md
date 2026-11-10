# Architecture

## Purpose

`trysac-doc-qa-cli` is a small, dependency-free Python library: Answer questions about a folder of Markdown and text files with an injected LLM, lexical retrieval, escaped excerpts and citations whose verbatim quotes are verified

## Shape

```text
caller code --> doc_qa_cli (public API in __init__.py)
                    |
                    +-- load_folder: bounded filesystem reads
                    +-- retrieve/answer: pure scoring and prompt building
```

- **Public API**: the names listed in `__all__` of `src/doc_qa_cli/__init__.py`. Anything else is
  internal and may change without a major version.
- **I/O**: `load_folder` walks the directory tree under `root`, reads and decodes file bytes and
  calls the optional `on_event` callback. The walk is bounded by `max_files` and `max_file_bytes`,
  only UTF-8 files are accepted, symlinks are resolved and must stay inside `root`, and skipped
  files are reported through `on_event` with a path and a reason code (never file contents).
  `retrieve` and `answer` perform no I/O; `answer` only calls the injected LLM.
- **Errors**: invalid input raises `QaError` with `code` in
  `{'too_many_files', 'invalid_question', 'invalid_root'}`, for example a missing root, a question
  outside the 1-2000 character range or too many eligible files. Exceptions from the injected LLM
  propagate unchanged. The library never prints or exits; that is the CLI's job.
- **Side effects**: none beyond the filesystem reads and `on_event` calls in `load_folder`; there is
  no global mutable state and no printing from the library.

## Quality contract

`scripts/check.py` is the single definition of the gates; `fabrica.json` tells the factory and CI
how to run it. See [TESTING.md](TESTING.md).

## Decisions

Architecture decisions are recorded in [decisions/](decisions/) as numbered ADRs.
