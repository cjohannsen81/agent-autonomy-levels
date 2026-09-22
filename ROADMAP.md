# Roadmap

What the next versions of the framework will add, in order, and why. The reasoning and sources are in [docs/research-2026-09.md](docs/research-2026-09.md). Versioning follows the CHANGELOG policy: new controls or schema fields are minor releases; changes to level definitions or control IDs are major.

The research changed one thing about the framework's positioning: **the certificate, not the levels, is the asset.** Level schemes are now common (CSA, Gartner, DeepMind, Hugging Face, Singapore IMDA, EU AI Act Article 14(3)). Nobody has published a signed, per-use-case, machine-readable record of level, scope, controls, evidence and demotion triggers that a counterpart agent, an insurer or an auditor can check without trusting the issuer's word. The roadmap works toward that.

## Done in 0.2.0

| # | Change | Anchor |
|---|---|---|
| 1 | Crosswalk to CSA v2.0, Gartner, Morris et al., Mitchell et al.; positioning against Safin and Balta and Anthropic's autonomy measurements; EU AI Act Art. 14(3) hook | Section 9 |
| 2 | AL-17 level integrity: level, policy and credentials outside the agent's reach; no self-promotion; the model never holds credentials | CSA v2.0, IETF AIMS draft |
| 3 | AL-16 sharpened to 60 seconds revoke-to-enforce, including derived tokens | IETF AAP draft, CSA May 2026 |
| 4 | Refusal-spike trigger quantified: 3 consecutive or 20 per session | Anthropic auto mode |
| 5 | Q1 scores real-world reversibility; Q7 = 2 requires a human-review and appeal channel at any level | CSA v2.0, Colorado SB 189, OMB M-25-21, GDPR Art. 22 |
| 6 | Principle 6, instructions are not controls; certificate `owner`, `retired`, `material_changes`; retirement stage | Adversa incident tally, OverEager-Bench, EDDOps, OWASP AST09 |
| 7 | Promotion windows are minimums; rolling thresholds tighten with the score; 12-month validity, 3-month re-test | Practitioner trust-score schemes, IMDA, AIUC-1 |
| 8 | Four worked examples in `examples/` | Replit, Kiro, PagerDuty, Salesloft Drift, Klarna |

## 0.3.0

| # | Change | Anchor |
|---|---|---|
| 9 | Multi-agent chain rule: chain level is at most the minimum in the chain, and only if each hop attenuates scope, treats agent output as untrusted (AL-07) and re-authorizes at the resource; otherwise certify at the union of reachable capabilities. Delegation depth per level: none at L1 and L2, one hop at L3, more with an attested runtime at L4 and L5. AL-12 capped at L3 across an A2A boundary. Brings ASI07 into scope | Bounded Agents, Delegation Without Trust, AAP `max_depth`, A2A spec |
| 10 | Scope as an action-class matrix (auto / ask / deny) inside the certificate, so promotion can target reversible writes first and demotion can target the class that failed | Anthropic auto mode, task-based access control |
| 11 | Evidence as typed pointers: regime, source system, hash, collected, expires; a named benchmark and metric per control that is certified by evaluation | DEMM-Bench, CycloneDX Attestations, validity audit of agent-safety benchmarks |
| 12 | `tools/derive.py`: pre-fill Q2 and Q6, and flag Q1, from a declarative policy (Cedar, OPA, Aggrete) | AgentCore Policy, FIDES, OPA |
| 13 | Regulatory mapping: EU AI Act Art. 6(3), 12, 14, 26; MAS SAFR; FINRA 2026; China's May 2026 opinions; NIST SP 800-53 families and the COSAiS agent overlays when published | see research, regulation section |

## 1.0.0

| # | Change | Anchor |
|---|---|---|
| 14 | Verifiable certificate: bound to a digest of the agent specification (model, prompts, tool manifest, policy); signed as an in-toto predicate in a Sigstore bundle and published as an A2A `AgentExtension`; a JWT claim profile compatible with AAP and transaction tokens; a registry and status list checked at request time; issuer accreditation field for ISO/IEC 42006 bodies and insurers | Feng et al., OpenSSF Model Signing, A2A, Visa and Mastercard agent directories, W3C Agent Identity Registry CG, Armilla |
| 15 | Per-action dynamic gate and information-flow control as optional advanced controls at L4 and L5 | Task-based access control, FIDES, CaMeL |

## Open

- Whether transparency-log inclusion is acceptable for certificates whose scope is confidential.
- Legal, e-discovery and warehouse-write analytics agents as further examples.
- Calibration of the worksheet thresholds and the promotion metrics against real deployments. Open an issue with yours.
