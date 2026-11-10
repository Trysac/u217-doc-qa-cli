from __future__ import annotations

import importlib
import sys
from typing import Any

from . import QaError, answer, load_folder, retrieve


def _import_callable(spec: str) -> Any:
    if ":" not in spec:
        raise ValueError("LLM spec must be 'module:attr'")
    module_name, attr_name = spec.split(":", 1)
    if not module_name or not attr_name:
        raise ValueError("LLM spec must be 'module:attr'")
    module = importlib.import_module(module_name)
    obj = getattr(module, attr_name)
    if not callable(obj):
        raise TypeError(f"{spec!r} is not callable")
    return obj()


def _print_usage() -> None:
    print(
        "usage: doc-qa-cli search <folder> <question> [-k N]\n"
        "       doc-qa-cli ask <folder> <question> --llm <module:attr> [-k N]",
        file=sys.stderr,
    )


def main(argv: list[str] | None = None) -> int:
    """CLI entry point. Exit 0 ok, 1 not verified, 2 usage or IO error."""
    if argv is None:
        argv = sys.argv[1:]
    if len(argv) < 3 or argv[0] not in {"search", "ask"}:
        _print_usage()
        return 2

    command, folder, question = argv[0], argv[1], argv[2]
    rest = argv[3:]
    k = 4
    llm_spec: str | None = None

    i = 0
    while i < len(rest):
        arg = rest[i]
        if arg == "-k":
            if i + 1 >= len(rest):
                _print_usage()
                return 2
            try:
                k = int(rest[i + 1])
            except ValueError:
                _print_usage()
                return 2
            i += 2
        elif arg.startswith("--llm=") and command == "ask":
            llm_spec = arg.split("=", 1)[1]
            i += 1
        elif arg == "--llm" and command == "ask":
            if i + 1 >= len(rest):
                _print_usage()
                return 2
            llm_spec = rest[i + 1]
            i += 2
        else:
            _print_usage()
            return 2

    if command == "ask" and llm_spec is None:
        _print_usage()
        return 2

    try:
        corpus = load_folder(folder)
        if command == "search":
            chunks = retrieve(corpus, question, k)
            for chunk in chunks:
                print(chunk.id)
            return 0
        else:
            if llm_spec is None:
                _print_usage()
                return 2
            llm = _import_callable(llm_spec)
            result = answer(question, corpus, llm, k=k)
            print(result.text)
            for citation in result.citations:
                print(f'[{citation.chunk_id}] "{citation.quote}"')
            return 0 if result.verified else 1
    except QaError as exc:
        print(f"error: {exc.code}", file=sys.stderr)
        return 2
    except (OSError, ValueError, TypeError) as exc:
        print(f"error: {exc}", file=sys.stderr)
        return 2
    except Exception:
        # Unexpected error (e.g., from the LLM) is treated as an IO failure.
        print("error: unexpected failure", file=sys.stderr)
        return 2


if __name__ == "__main__":
    raise SystemExit(main())
