# Worked examples

Four use cases from 2025-2026 deployments and incidents, scored with the worksheet in FRAMEWORK.md section 5 and written up as certificates (section 7). Each `<scope>.answers.yaml` reproduces the score in the matching `<scope>.certificate.yaml`; `tools/test_levels.py` checks that they agree and that every certificate validates.

Scores are the author's estimates for a fictional organization and are meant to be calibrated. The pattern they show is not: most real deployments need two certificates for one agent, a read-or-triage scope that reaches L4 and a write scope that stops at L3.

| Use case | Scope | Score | Level | What the level means here |
|---|---|---|---|---|
| [coding-agent](coding-agent/) | sandbox | 4 | L4 | Edits, tests and pushes to a branch without asking; the pull request is the approval |
| | prod-reachable | 8 | L3 | Not certified. The answers show why a reachable production credential has to go first |
| [sre-agent](sre-agent/) | diagnosis | 5 | L4 | Reads across logs, metrics and traces; posts findings and a proposed runbook step |
| | remediation | 7 | L3 | Prepares the exact restart, scale or rollback; the responder confirms each one |
| [saas-integration](saas-integration/) | as-deployed | 13 | L1 | Not certifiable. An organization-wide CRM read grant, the configuration behind the Salesloft Drift breach, fails the worksheet |
| | narrowed | 8 | L3 | One-contact lookup and lead creation with allowlisted fields, short-lived token, revocation drilled |
| [support-agent](support-agent/) | informational | 6 | L4 | Answers customers directly and updates tickets |
| | refunds | 8 | L3 | Proposes a refund within a cap; a lead confirms each one; demoted on CSAT or reopen-rate drift |

## Reading the levels in these examples

- **L4:** the agent executes writes on its own; only the actions the policy marks high-risk wait for approval (AL-11).
- **L3:** the agent plans and executes reads; every state change is confirmed by a person before it runs. This is the PagerDuty pattern: the agent presents the remediation, the responder clicks.
- **Not certified** rows have an answers file and no certificate. They are the useful ones: the worksheet says no before the incident does.

## Run them

```bash
pip install pyyaml jsonschema
python tools/score.py examples/saas-integration/as-deployed.answers.yaml
python tools/validate.py examples/*/*.certificate.yaml
```

## Sources

- Coding agent: Replit's production database deletion (July 2025), Google Antigravity drive wipe (2025), Adversa's tally of nine coding-agent incidents; permission modes in Claude Code, Codex and Cursor.
- SRE agent: PagerDuty SRE Agent and Datadog Bits, which propose and let a human execute; the Amazon Kiro outage (December 2025).
- SaaS integration: Salesloft Drift breach (August 2025), 700+ Salesforce organizations, Unit 42 threat brief.
- Support agent: Klarna's reversal (May 2025), Salesforce Agentforce and Intercom Fin self-resolution figures.

Details and links: `docs/research-2026-09.md`, use-case section.
