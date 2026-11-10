# Project record

## Objective

Answer questions about a folder of Markdown and text files with an injected LLM, lexical retrieval, escaped excerpts and citations whose verbatim quotes are verified

## Scope

- In scope: the public API documented in [README.md](../README.md), typed and tested.
- Out of scope: anything that needs runtime dependencies or I/O without an accepted ADR.

## Timeline

| Date | Event |
|---|---|
| 2026 | Repository created from the factory utility template. |

## Effort metrics

Measured values only; a value that has not been measured stays "pending measurement".

| Metric | Value |
|---|---|
| Tokens (input / output) | 800128 / 66366 |
| Hours (human) | pending measurement |
| Cost (USD) | 0.0926 |

## Factory run u217 (measured from API usage)

| Date (UTC) | Phase | Model | Batch | Input | Output | Cache write | Cache read | Cost (USD) |
|---|---|---|---|---|---|---|---|---|
| 2026-11-10 | generation | deepseek-v4-pro | yes | 1876 | 18999 | 0 | 3200 | 0.0389 |
| 2026-11-10 | fix-1 | deepseek-flash | no | 12165 | 3564 | 0 | 113664 | 0.0043 |
| 2026-11-10 | fix-2 | deepseek-flash | no | 8469 | 1661 | 0 | 48768 | 0.0024 |
| 2026-11-10 | audit | deepseek-flash | no | 22035 | 24009 | 0 | 436864 | 0.0190 |
| 2026-11-10 | fix-3 | deepseek-flash | no | 9309 | 2133 | 0 | 40064 | 0.0028 |
| 2026-11-10 | docs | deepseek-flash | no | 103458 | 16000 | 0 | 256 | 0.0251 |

Total: $0.0926. Prices: deepseek line, as measured by its adapter. Providers serve the current version of each model id, so the date tells which version answered; versions, launch stages and price sources per line are in the factory's model register (docs/MODELS.md).
