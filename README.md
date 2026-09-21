# Autonomy Levels for Governed AI Agents

How much should an AI agent do without a human, and how do you prove it is safe?

This framework answers that per use case, in three parts:

1. **Five autonomy levels** (L1 Operator to L5 Observer), based on [Feng, McDonald and Zhang](https://arxiv.org/abs/2506.12469).
2. **Sixteen required controls** (AL-01 to AL-16), cumulative per level and mapped to the [OWASP Top 10 for Agentic Applications 2026](https://genai.owasp.org/resource/owasp-top-10-for-agentic-applications-for-2026/) and ISO/IEC 42001 Annex A.
3. **Promotion and demotion rules** plus a machine-readable **autonomy certificate**, so autonomy is earned with evidence and revoked on defined signals.

Read the framework: **[FRAMEWORK.md](FRAMEWORK.md)** (a PDF is attached to each [release](../../releases)).

## At a glance

| Level | Human role | Agent may | Key controls added |
|---|---|---|---|
| L1 | Operator | Suggest only | Identity, tamper-evident log, tool integrity, scope limits, no writes |
| L2 | Collaborator | Read and draft | Redaction, injection containment, rate limits |
| L3 | Consultant | Execute reads across systems | Aggregation limits, argument-level rules |
| L4 | Approver | Write, with approval for high-risk actions | Human approval, end-user identity, monitoring |
| L5 | Observer | Act within scope | Continuous verification, signed supply chain, tested revocation |

## Repository

| Path | Contents |
|---|---|
| [FRAMEWORK.md](FRAMEWORK.md) | The framework |
| [mappings/owasp-agentic.md](mappings/owasp-agentic.md) | OWASP ASI01 to ASI10 mapped to controls |
| [mappings/iso-42001.md](mappings/iso-42001.md) | All 38 ISO/IEC 42001 Annex A controls mapped |
| [implementations/aggrete.md](implementations/aggrete.md) | Reference implementation with the Aggrete MCP proxy |
| [templates/](templates/) | Certificate JSON Schema, example certificate, scoring worksheet |
| [tools/](tools/) | `score.py` (maximum level from worksheet), `validate.py` (certificate checks), tests |

## Try it

```bash
pip install pyyaml jsonschema
python tools/score.py templates/answers.example.yaml
python tools/validate.py templates/certificate.example.yaml
```

`validate.py` checks the schema and the framework rules: the level does not exceed the scored maximum, every control required at the level is in place, and L1 lists no write tools.

## Status

Version 0.1.0 is a draft for feedback. Thresholds, promotion windows and mappings are starting values. Open an issue with deployment experience, disagreements or mapping corrections.

## Implementations

The framework is vendor-neutral: any gateway or agent platform that enforces the controls can implement it. [Aggrete](https://github.com/aggrete/aggrete) is the first reference implementation. To list another, open a pull request adding `implementations/<name>.md` in the same format.

## Citation

See [CITATION.cff](CITATION.cff), or cite as:

> Johannsen, C. (2026). *Autonomy Levels for Governed AI Agents* (Version 0.1.0). https://github.com/cjohannsen81/autonomy-levels

## License

[CC BY 4.0](LICENSE) for the framework text and templates. Code in `tools/` is licensed under the [Apache License 2.0](tools/LICENSE).
