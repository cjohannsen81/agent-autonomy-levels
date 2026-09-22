# Changelog

This project uses semantic versioning. Changes to level definitions or control IDs are major; new controls or mappings are minor; wording and corrections are patch.

## 0.2.0 (2026-09-22)

Informed by the research in `docs/research-2026-09.md`.

- New control AL-17 level integrity (from L1): level, policy and credentials outside the agent's reach; no self-promotion
- AL-16 revocation target set at 60 seconds, including derived tokens
- Principle 6: instructions are not controls
- Q1 scores real-world reversibility; Q7 = 2 requires a human-review and appeal channel at any level
- Promotion windows are minimums; rolling thresholds tighten with the score; certificates valid at most twelve months
- Refusal-spike demotion trigger quantified; material-change trigger and retirement stage added
- Certificate schema: `owner` required; `material_changes`, `retired` and the `material_change` trigger added; validator checks the twelve-month limit
- Section 9 replaced by a crosswalk to CSA, Gartner, Morris et al. and Mitchell et al., with the EU AI Act Article 14(3) hook
- Section 10 answers open questions 1 and 3, and states the plan for 2 and 4
- Four worked examples in `examples/`, checked in CI
- ROADMAP.md and docs/

## 0.1.2 (2026-09-22)

- Worked example of an autonomy certificate in section 7

## 0.1.1 (2026-09-22)

- Introduction on the origin of the centaur principle (Kasparov's Advanced Chess, 1998) and whether it still holds

## 0.1.0 (2026-09-21)

Initial draft.

- Five levels (L1 to L5) based on Feng, McDonald and Zhang
- Sixteen controls AL-01 to AL-16 with OWASP Agentic mapping
- Eight-question scoring worksheet with maximum-level thresholds
- Promotion evidence and demotion triggers
- Autonomy certificate JSON Schema, example, and validator
- ISO/IEC 42001 Annex A mapping (38 controls)
- Aggrete reference implementation mapping
