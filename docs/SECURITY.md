# Security notes

## Threat model

`trysac-doc-qa-cli` reads an untrusted directory tree and sends its text to an injected LLM. The
main risks are:

- **Untrusted filesystem tree**: `load_folder` walks a caller-supplied root that may contain
  hostile entries. Mitigation: only configured extensions are read, `max_files` and
  `max_file_bytes` bound the work, only UTF-8 files are decoded, symlinks are resolved and must
  stay inside the root (escapes are skipped), and `on_event` payloads carry only the relative path
  and a reason code, never file contents.
- **Prompt injection from documents**: document text is attacker-controlled data that is pasted
  into the prompt. Mitigation: `&`, `<` and `>` are HTML-escaped before wrapping each excerpt in
  `<excerpt id="...">`, so text such as `</excerpt><system>` cannot break out of the excerpt, and
  the system prompt states that excerpt text is data, not instructions. Escaping reduces but does
  not eliminate prompt injection; treat the LLM reply as untrusted data too.
- **Hostile LLM replies**: the reply drives citations. Mitigation: every citation id must have
  been retrieved and every quote is verified verbatim against the cited chunk, so fabricated
  quotes or unknown ids yield `valid=False` and an unverified answer.
- **Supply chain**: a compromised dependency or CI action. Mitigation: no runtime dependencies,
  Dependabot weekly updates, actions pinned to major versions, minimal workflow permissions.
- **Leaked secrets**: tokens committed by mistake. Mitigation: `gitleaks` runs in the local gates
  and in CI; `.env` files are git-ignored.
- **Insecure code**: shell injection, weak hashes, unsafe deserialization. Mitigation: Ruff's
  `S` rules in lint and a `security` gate (Bandit, high severity fails, `# nosec` ignored); fix the
  code instead of silencing it.
- **Untrusted input**: callers may pass hostile strings. Mitigation: validate input and fail with
  explicit `QaError` codes; never `eval`, `exec` or deserialize untrusted data.

## Publishing

Releases are published to PyPI with trusted publishing (OIDC) when available, never with a
long-lived token stored in the repository.

To report a vulnerability, see [SECURITY.md](../SECURITY.md).
