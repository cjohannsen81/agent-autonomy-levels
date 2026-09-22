---
title: "Autonomy Levels for Governed AI Agents"
subtitle: "Levels, required controls, and promotion criteria"
author: "Christian Johannsen"
version: "0.1.1"
date: "2026-09-22"
---

# Autonomy Levels for Governed AI Agents

**Version 0.1.1 (draft), 2026-09-22.** Licensed under CC BY 4.0.

A framework for deciding how much autonomy an AI agent gets for a given use case, which controls must be in place at each level, and what evidence earns promotion to the next level.

## Introduction: an old principle

The idea behind this framework is older than generative AI. After losing to Deep Blue in 1997, Garry Kasparov proposed playing with the machine instead of against it. The first "Advanced Chess" match, Kasparov against Veselin Topalov, each with a PC at hand, took place in León, Spain, in June 1998 and ended 3–3 [7][8]. In the freestyle tournaments that followed, a human-computer team was called a centaur [8].

The 2005 freestyle tournament on Playchess.com was won not by a grandmaster with a state-of-the-art machine but by two American amateurs running three computers at once. Kasparov's conclusion:

> Weak human + machine + better process was superior to a strong computer alone and, more remarkably, superior to a strong human + machine + inferior process. [7]

The term reached knowledge work through the 2023 Harvard/BCG field experiment with 758 consultants, which described Centaurs, who divide tasks between themselves and the AI, and Cyborgs, who interleave their work with it [9]. The study in section 1 builds on that experiment [1]. The autonomy levels used here come from a separate line of work that does not draw on chess [3]; the two meet in the question of how work is divided between human and machine.

**Is the principle still valid?** In chess, only in part. By 2013 observers already saw the centaur's edge over engines alone disappearing [10], and engines have grown far stronger since. What aged is the claim that a human must stay in every loop. What held is the claim about process. The 2023 experiment found the same pattern in knowledge work: on tasks within the AI's capabilities, consultants using it completed 12.2% more tasks, 25.1% faster and with more than 40% higher quality; on a task outside them, they were 19 percentage points less likely to reach a correct answer [9]. The tool was the same in both cases. The difference lay in how it was used.

This framework reads both results the same way. As machines improve, less human involvement per action is needed, which is why the levels run up to L5. What does not become optional is the process that decides how much involvement a use case needs and checks that the decision holds. Here, that process is the controls (section 4), the scoring (section 5) and the promotion and demotion rules (section 6).

## 1. Why this exists

A field study of 244 Boston Consulting Group consultants found three ways professionals work with generative AI: Centaurs keep control of both what to do and how; Cyborgs decide what to do and let the AI shape how; Self-Automators hand both to the AI [1]. Self-Automators were 27% of participants. They finished fastest and produced the weakest work, and gained neither domain nor AI expertise [1][2].

Agents raise the same question at system level: how much should run without a human, and how do we show it is safe to do so? Existing work defines autonomy levels [3] and lists agent-specific risks [4]. What is missing is the link between a level, the controls that make it safe, and the evidence that justifies it. This framework provides that link.

## 2. Principles

1. **Autonomy is a design decision, separate from capability.** A capable agent can still run at low autonomy if it must consult its user before each action [3].
2. **Least agency.** Autonomy is earned, not granted by default [4][5].
3. **Per use case, not per agent.** The same agent can run at L4 for ticket triage and L1 for payroll.
4. **Earned and revocable.** Promotion requires evidence; defined signals trigger demotion.
5. **Enforced, not declared.** A level only counts if a control layer outside the agent enforces it and keeps an audit trail.

## 3. The five levels

The levels follow Feng, McDonald and Zhang, who define autonomy by the role the user plays: operator, collaborator, consultant, approver, observer [3].

| Level | User role | The agent may | Typical use |
|---|---|---|---|
| **L1** | Operator | Suggest; the human performs every action | Regulated decisions; first deployment of any agent |
| **L2** | Collaborator | Read and draft; human and agent share execution | Research, drafting |
| **L3** | Consultant | Plan and execute reads across systems; consult the human on preferences | Analysis across several data sources |
| **L4** | Approver | Execute, including writes; high-risk actions are held for approval | Ticket updates, CRM notes, internal posts |
| **L5** | Observer | Act fully within scope; the human monitors and can revoke | Routine, reversible, low-sensitivity work |

## 4. Required controls

Controls are cumulative: a level requires its own controls and all controls of lower levels. Control IDs are stable and referenced by the certificate schema.

| ID | Control | From level | OWASP Agentic [4] |
|---|---|---|---|
| AL-01 | Agent acts under an individual identity from the organization's IdP; no shared credentials | L1 | ASI03 |
| AL-02 | Tamper-evident log of every tool call and decision | L1 | ASI10 |
| AL-03 | Tool integrity: tool definitions pinned; changes and poisoned descriptions detected | L1 | ASI01, ASI04 |
| AL-04 | Scope limits: tools outside the use case are hidden or refused | L1 | ASI02, ASI03 |
| AL-05 | No writes: every state-changing tool is hidden or refused | L1 only | ASI02 |
| AL-06 | Sensitive data redacted from results; secrets blocked from tool arguments | L2 | ASI06 |
| AL-07 | Prompt-injection containment: no write after reading untrusted content in the same session | L2 | ASI01 |
| AL-08 | Rate and cost limits per identity | L2 | ASI08 |
| AL-09 | Aggregation limits: combining data across systems or about many individuals is refused where policy forbids it | L3 | ASI02, ASI10 |
| AL-10 | Argument-level rules: the same tool is allowed or refused by the scope of the request | L3 | ASI02 |
| AL-11 | Human approval for defined high-risk actions, with the approver recorded | L4 | ASI09 |
| AL-12 | End-user identity carried through to downstream systems | L4 | ASI03 |
| AL-13 | Real-time forwarding of decisions to security monitoring | L4 | ASI08, ASI10 |
| AL-14 | Continuous verification: control tests run automatically and block release on failure | L5 | ASI10 |
| AL-15 | Supply chain: the enforcement layer and agent components are signed, with SBOM and provenance | L5 | ASI04 |
| AL-16 | Revocation: the agent identity can be cut off within minutes, and this has been tested | L5 | ASI10 |

ASI05 (unexpected code execution) and ASI07 (inter-agent communication) need controls inside the agent runtime and between agents. They are out of scope for version 0.1.

## 5. Choosing the maximum level

Score each question 0 (low risk) to 2 (high risk). The total caps the level for the use case.

| # | Question | 0 | 1 | 2 |
|---|---|---|---|---|
| Q1 | Are the agent's actions reversible? | Fully | With effort | No |
| Q2 | Most sensitive data reached | Public | Internal | Personal, financial, health or legal |
| Q3 | Blast radius of one bad action | One record | One team | Customers or the public |
| Q4 | Is the domain regulated? | No | Indirectly | Yes |
| Q5 | Does output reach external parties? | No | After review | Directly |
| Q6 | Can the agent combine data across systems? | No | Two systems | Many |
| Q7 | Does it act on people (hiring, pay, access)? | No | Indirectly | Directly |
| Q8 | Experience of the team operating it | Established | Some | New |

| Score | Maximum level |
|---|---|
| 0 to 3 | L5 |
| 4 to 6 | L4 |
| 7 to 9 | L3 |
| 10 to 12 | L2 |
| 13 to 16 | L1 |

A score of 2 on both Q1 and Q7 (irreversible actions on people) caps the use case at L3, whatever the total. Thresholds are starting values to be calibrated against real deployments.

`tools/score.py` computes the maximum level from an answers file.

## 6. Promotion and demotion

Every use case starts at L1 or L2, whatever its maximum.

**Promotion evidence** (starting values):

| To | Evidence |
|---|---|
| L2 | Controls for L2 verified by automated tests; policy owners named |
| L3 | 30 days at L2 with new rules in alert-only mode; alerts reviewed; no open policy violations |
| L4 | Red-team exercise against ASI01 to ASI03 passed; aggregation rules enforcing; approval workflow tested end to end |
| L5 | 90 days at L4; approval outcomes stable; no audit-log integrity failures; incident response rehearsed |

**Demotion triggers** (drop at least one level, pending review):

- Audit-log integrity failure (AL-02)
- Tool definition change or poisoned description detected (AL-03)
- Unexplained spike in refusals for one rule or identity
- Confirmed incident attributable to the agent
- Expired or missing autonomy certificate

## 7. Autonomy certificate

Feng et al. propose autonomy certificates for governing agents [3]. This framework defines a minimal machine-readable form, one per use case, with a JSON Schema in `templates/certificate.schema.json` and an example in `templates/certificate.example.yaml`. A certificate records the level, the score behind the maximum level, the scope (identity, data domains, write tools), the controls in place, the evidence, the reviewer and an expiry date.

## 8. Mapping to ISO/IEC 42001

Evidence produced at each level supports these Annex A controls of ISO/IEC 42001:2023 [6]. The mapping is indicative: Annex A controls are selected through a Statement of Applicability, and this framework covers runtime operation, not the full AI management system.

| Level | Annex A controls evidenced |
|---|---|
| L1 | A.6.2.8 event logs; A.9.4 intended use |
| L2 | A.7.2 data (runtime redaction) |
| L3 | A.5.4 impact on individuals (aggregation limits) |
| L4 | A.9.2 and A.9.3 responsible use (human approval); A.10.2 allocation of responsibilities |
| L5 | A.6.2.4 verification and validation; A.6.2.6 operation and monitoring; A.4.4 and A.10.3 tooling and suppliers |

Full table: `mappings/iso-42001.md`.

## 9. Relation to human working modes (interpretation)

| Level | Closest BCG mode [1] |
|---|---|
| L1 | Centaur |
| L2 to L3 | Cyborg |
| L4 | Cyborg with a governed hand-off |
| L5 | Self-Automator, bounded by enforced controls |

The study found that full delegation fails when it is unbounded. The framework keeps L5 available, but only for work that scores low risk and only behind controls AL-01 to AL-16.

## 10. Open questions

1. Should promotion windows scale with the risk score?
2. In a multi-agent chain, is the effective level the lowest level in the chain?
3. Can Q2, Q6 and Q7 be answered automatically from the enforcement layer's configuration?
4. What must a third party verify for a certificate to be trusted outside the issuing organization?

Feedback via GitHub issues is welcome.

## References

1. Randazzo, Lifshitz-Assaf, Kellogg, Dell'Acqua, Mollick, Candelon, Lakhani. *Cyborgs, Centaurs and Self-Automators: The Three Modes of Human-GenAI Knowledge Work and Their Implications for Skilling and the Future of Expertise.* SSRN, 2024. https://papers.ssrn.com/sol3/papers.cfm?abstract_id=4921696
2. Authors' summary. https://alphaleaders.co.uk/are-you-a-cyborg-a-centaur-or-a-self-automator-ai-creates-different-kinds-of-humans-in-the-loop/
3. Feng, McDonald, Zhang. *Levels of Autonomy for AI Agents.* Knight First Amendment Institute / arXiv:2506.12469, 2025. https://arxiv.org/abs/2506.12469
4. OWASP GenAI Security Project. *OWASP Top 10 for Agentic Applications 2026.* https://genai.owasp.org/resource/owasp-top-10-for-agentic-applications-for-2026/
5. Auth0. *Lessons from OWASP Top 10 for Agentic Applications.* https://auth0.com/blog/owasp-top-10-agentic-applications-lessons/
6. ISO/IEC 42001:2023, Annex A. Control list as summarized at https://mindsetcyber.com.au/iso-42001-controls-list/
7. Kasparov. *The Chess Master and the Computer.* The New York Review of Books, 11 February 2010. https://www.nybooks.com/articles/2010/02/11/the-chess-master-and-the-computer/
8. Wikipedia. *Advanced chess.* https://en.wikipedia.org/wiki/Advanced_chess
9. Dell'Acqua, McFowland, Mollick, Lifshitz-Assaf, Kellogg, Rajendran, Krayer, Candelon, Lakhani. *Navigating the Jagged Technological Frontier: Field Experimental Evidence of the Effects of AI on Knowledge Worker Productivity and Quality.* Harvard Business School Working Paper 24-013, 2023. https://papers.ssrn.com/sol3/papers.cfm?abstract_id=4573321
10. Cowen. *What are humans still good for? The turning point in Freestyle chess may be approaching.* Marginal Revolution, November 2013. https://marginalrevolution.com/marginalrevolution/2013/11/what-are-humans-still-good-for-the-turning-point-in-freestyle-chess-may-be-approaching.html
