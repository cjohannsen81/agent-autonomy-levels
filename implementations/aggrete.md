# Reference implementation: Aggrete

[Aggrete](https://github.com/aggrete/aggrete) is an open-source (Apache 2.0) MCP proxy that enforces policy on every tool call. It covers most framework controls. Other gateways can implement the framework; this page shows one way.

Mechanisms refer to Aggrete 0.11. Check IDs (C01 to C16) refer to its conformance report, `aggrete conformance --format md`.

| Control | Aggrete mechanism | Conformance check |
|---|---|---|
| AL-01 Individual identity | `auth: jwt` identity from IdP; caller tokens never forwarded | C10 |
| AL-02 Tamper-evident log | Hash-chained audit rows, verified with `aggrete-audit` | C09 |
| AL-03 Tool integrity | `tool_integrity:` fingerprinting and poisoning scan | C07 |
| AL-04 Scope limits | `wall` rules; hidden tools | C01, C12 |
| AL-05 No writes | Write-verb classification; writes refused by policy (`applies: write`) | not a dedicated check |
| AL-06 Redaction and secrets | `redact:`, `scan_inbound:` | C05, C06 |
| AL-07 Injection containment | No write after untrusted read | C03 |
| AL-08 Rate limits | `rate_limit:` | C08 |
| AL-09 Aggregation limits | `domain_join`, `entity_budget`, `min_group` at `deny` | C02, C13 |
| AL-10 Argument-level rules | `arg_match` | C04 |
| AL-11 Human approval | `action: approve`; approver on the audit row | C11 |
| AL-12 End-user identity downstream | `per_user: true` upstreams, `obo:` | not yet a check |
| AL-13 Monitoring | `audit_forward:` (SIEM, OCSF), Prometheus, OTLP | C16 |
| AL-14 Continuous verification | `aggrete conformance` in CI | all |
| AL-15 Supply chain | Not yet: signed image with SBOM and provenance planned | gap |
| AL-16 Revocation | `wall` with `blocked_users` | C12 |

**Coverage:** 13 of 16 controls have a conformance check; AL-05 and AL-12 are implemented without a dedicated check; AL-15 is open.

## Per-level policy starting points

Suggested approach: one policy file per level (`coc.L1.yaml` to `coc.L5.yaml`), each enabling the rules for that level's controls, starting in `alert` mode and flipping to `deny` on promotion. Validate every file with `aggrete-lint` and its own allow and deny tests before use. Policy templates are not included in v0.1.
