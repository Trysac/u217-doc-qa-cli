"""Behavior tests for the public API of doc_qa_cli."""

from __future__ import annotations

import pytest

import doc_qa_cli


def test_normalize_trims_and_lowercases() -> None:
    assert doc_qa_cli.normalize("  Hello World ") == "hello world"


@pytest.mark.parametrize("value", ["", "   ", "\t\n"])
def test_normalize_rejects_blank_input(value: str) -> None:
    with pytest.raises(ValueError, match="must not be empty"):
        doc_qa_cli.normalize(value)


def test_version_is_semver() -> None:
    parts = doc_qa_cli.__version__.split(".")
    assert len(parts) == 3
    assert all(part.isdigit() for part in parts)
