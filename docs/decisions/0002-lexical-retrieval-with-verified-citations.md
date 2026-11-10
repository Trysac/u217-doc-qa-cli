# Lexical retrieval with verified citations

Status: accepted (generated, pending human review)

## Context

A full RAG stack with embeddings and a vector database is overkill for a few hundred text and Markdown files. The library must answer questions about such folders with an injected LLM, ensure every cited fact is backed by a verbatim quote, and stay dependency-free.

## Decision

Use lexical retrieval based on casefolded letter/digit runs and an IDF-style score over paragraph chunks. The LLM is injected via a minimal Protocol. Answers require bracketed citations with quoted text; each quote is whitespace-collapsed and checked as a substring of the cited chunk. A reply of NOT_FOUND is treated as verified when the retrieval returns no useful excerpt or the model explicitly says so.

## Consequences

The system is simple, inspectable, and has zero runtime dependencies. It will not capture semantic similarity that embeddings would, and the citation format is rigid; future work may add an embedding backend behind the same retrieval interface.
