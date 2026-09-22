---
title: "Autonomy Levels for Governed AI Agents"
subtitle: "Levels, required controls, and promotion criteria"
author: "Christian Johannsen"
version: "0.2.0"
date: "2026-09-22"
---

# Autonomy Levels for Governed AI Agents

**Version 0.2.0 (draft), 2026-09-22.** Licensed under CC BY 4.0.

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
6. **Instructions are not controls.** A rule written into a prompt, a policy document or a code-freeze notice constrains nothing. Of nine coding-agent data-loss incidents recorded between June 2025 and July 2026, guardrails were switched on in four and were bypassed anyway [11]; removing an explicit consent instruction from an agent harness raised its out-of-scope action rate from 0.0% to 17.1% in a controlled study [12]. Evidence for a level is gathered on the deployed harness and its enforcement layer, never on the model alone.

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
| AL-16 | Revocation: the agent identity, its tokens and any tokens derived from them can be cut off within 60 seconds of the decision, and this has been tested | L5 | ASI10 |
| AL-17 | Level integrity: the level, the policy and the credentials live in a layer the agent cannot reach; the model never holds credentials; the agent cannot change its own level | L1 | ASI03, ASI10 |

AL-16 adopts the revocation target of the IETF Agent Authorization Profile draft, 60 seconds from request to enforcement at every resource server, with revocation of the whole token family [13]. AL-17 follows the CSA requirement that the autonomy configuration be "stored and enforced at an architectural layer that the agent's execution context cannot reach" [14] and the IETF agent identity draft's rule that the model "MUST NOT have access to an agent's credentials" [15]. Numbering is by order of adoption, not by level; AL-17 is required from L1.

ASI05 (unexpected code execution) and ASI07 (inter-agent communication) need controls inside the agent runtime and between agents. They are out of scope for version 0.2; ASI07 is planned for version 0.3 (section 10).

## 5. Choosing the maximum level

Score each question 0 (low risk) to 2 (high risk). The total caps the level for the use case.

| # | Question | 0 | 1 | 2 |
|---|---|---|---|---|
| Q1 | Are the agent's actions reversible in effect, not only technically? | Fully | Technically, but the effect persists (a refund, a recalled message) | No |
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

Two rules override the total:

- A score of 2 on both Q1 and Q7 (irreversible actions on people) caps the use case at L3.
- A score of 2 on Q7 (the agent acts directly on people) requires, at any level, a staffed channel through which an affected person can obtain human review of the outcome, and the reviewer must have authority to overturn it. Colorado's SB 189 [16], the US federal guidance for high-impact AI [17] and the reading of GDPR Article 22 by EU regulators all turn on this point.

Q1 scores the effect, not the mechanism: a database row can be restored, but a payment that reached a supplier or a message that reached a customer has been acted on. CSA's framework draws the same distinction between technical and real-world reversibility [14]. Thresholds are starting values to be calibrated against real deployments.

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

The windows are minimums. Promotion also requires that rolling metrics over the window meet thresholds, and the thresholds tighten with the risk score: for a score of 0 to 6, no policy violation in the last 30 days and a human override rate that is stable or falling; for a score of 7 or more, additionally at least 95% of sampled agent actions over 60 days judged correct on review. Practitioner schemes use similar figures [18], and Singapore's IMDA framework recommends monitoring override rates and response times as the signal for automation bias [19]. Certificates are valid for at most twelve months, and the controls are re-tested at least every three months.

**Demotion triggers** (drop at least one level, pending review):

- Audit-log integrity failure (AL-02)
- Tool definition change or poisoned description detected (AL-03)
- Refusal spike: three consecutive refusals, or twenty in one session, for one rule or identity. These are the escalation counts used in production by Anthropic's auto mode [20] and are starting values.
- Confirmed incident attributable to the agent
- Expired or missing autonomy certificate
- A material change to the agent: a new model version, a new tool or connector, a widened scope, or a removed approval gate. The certificate lists what counts as material; until it is re-issued the use case drops one level.

**Retirement.** A use case that is no longer needed is retired, not left running: its certificate is marked retired, its identity is revoked (AL-16) and its tools are removed from the enforcement layer. An agent without a named owner is retired by default.

## 7. Autonomy certificate

Feng et al. propose autonomy certificates for governing agents [3]. This framework defines a minimal machine-readable form, one per use case, with a JSON Schema in `templates/certificate.schema.json` and an example in `templates/certificate.example.yaml`. A certificate records the level, the score behind the maximum level, the scope (identity, data domains, write tools), the controls in place, the evidence, the owner, the reviewer, an expiry date and what counts as a material change. Further worked examples are in `examples/`.

### Example

A support team runs an agent that reads incoming tickets and the public knowledge base, then comments on tickets and moves them between statuses. Its certificate:

```yaml
framework_version: 0.2.0
certificate: support-triage-agent/ticket-updates
level: L4
max_level: L4                 # from tools/score.py
score: 6
owner: support-lead@example.com
scope:
  identity: svc-triage-agent@example.com
  domains: [ticketing-support, kb-public]
  writes: [ticketing__create_comment, ticketing__update_status]
controls:
  in_place: [AL-01, AL-02, AL-03, AL-04, AL-06, AL-07, AL-08, AL-09, AL-10, AL-11, AL-12, AL-13, AL-17]
  enforcement: aggrete 0.11
  policy: policies/support-triage.L4.yaml
  verification_report: reports/conformance-2026-10-02.md
  approvals_owner: support-lead@example.com
evidence:
  - reports/red-team-2026-10-02.md
  - reports/alert-review-2026-09-30.md
issued: 2026-10-05
expires: 2027-01-05
reviewer: security-architecture@example.com
demotion_triggers: [audit_integrity_failure, tool_change, refusal_spike, incident, certificate_expired, material_change]
material_changes: [model_version, new_tool, scope_widened, approval_gate_removed]
```

Reading it top to bottom:

- **`certificate`** names the agent and the use case. The same agent handling payroll queries would need a second certificate with its own score and level (principle 3).
- **`owner`** is the person accountable for the use case. A certificate without an owner is retired (section 6).
- **`score` and `max_level`** come from the worksheet in section 5. The team scored 6: actions reversible with effort (Q1 = 1), internal data (Q2 = 1), blast radius of one team (Q3 = 1), not regulated (Q4 = 0), external replies reviewed before sending (Q5 = 1), two systems (Q6 = 1), no actions on people (Q7 = 0), some operating experience (Q8 = 1). A score of 4 to 6 caps the use case at L4. The worksheet answers are in `templates/answers.example.yaml`.
- **`level`** is the level actually granted. It may be lower than `max_level`, never higher. Here the use case has been promoted to its maximum after starting at L2 (section 6).
- **`scope`** is what the enforcement layer allows: one non-shared identity (AL-01), two data domains (AL-04) and exactly two write tools. Any other write is refused. At L1 the `writes` list must be empty (AL-05).
- **`controls.in_place`** lists thirteen controls. L4 requires AL-01 to AL-13 and AL-17, except AL-05, which applies at L1 only; AL-14 to AL-16 are L5 controls and are not required yet. `enforcement` names the layer that enforces them (principle 5), `policy` the rule file it runs, and `verification_report` the automated test run showing the controls hold. `approvals_owner` is the person whose approval AL-11 records for high-risk actions.
- **`evidence`** points at the artifacts that justified promotion to L4: the red-team exercise against ASI01 to ASI03 and the review of alerts from the 30 days at L2 and L3.
- **`issued`, `expires`, `reviewer`** make the certificate an accountable, time-boxed decision. This one is valid for three months. When it expires, the last demotion trigger fires and the agent drops a level until renewed.
- **`demotion_triggers`** lists the signals from section 6 that the monitoring layer watches for this use case.
- **`material_changes`** lists what invalidates the certificate until re-issue. A retired use case adds `retired: <date>`.

`tools/validate.py` checks the certificate against the schema and then against the framework rules: the level does not exceed the maximum, every control required at the level is in place, the expiry is after the issue date, the certificate is valid for at most twelve months, and L1 lists no write tools. Removing AL-11 from the list above, for example, fails validation with `controls required at L4 but not in place: AL-11`.

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

## 9. Relation to other schemes

Several level schemes are in use. They scale different things: the user's role (this framework, Feng et al.), decision authority and oversight intensity (CSA, Gartner), the societal role of the AI (Morris et al.), or who controls program flow (Mitchell et al.). The crosswalk is indicative.

| This framework | Feng et al. [3] | CSA Autonomy Levels v2.0 [14] | Gartner [21] | Morris et al. [22] | Mitchell et al. [23] |
|---|---|---|---|---|---|
| L1 Operator | Operator | L0 No Autonomy, L1 Assisted | Observe, Advise | L1 AI as a Tool | Simple Processor, Router |
| L2 Collaborator | Collaborator | L1 Assisted | Advise | L2 AI as a Consultant | Tool Caller |
| L3 Consultant | Consultant | L2 Supervised | Advise | L3 AI as a Collaborator | Multi-step Agent |
| L4 Approver | Approver | L3 Conditional | Act with Approval | L4 AI as an Expert | Multi-step Agent |
| L5 Observer | Observer | L4 High Autonomy | Act Autonomously | L5 AI as an Agent | Fully Autonomous Agent, bounded |

CSA's L5 Full Autonomy, in which the agent sets its own goals and may modify its own behaviour, has no counterpart here; CSA itself does not recommend it for deployment, and AL-17 rules it out. Mitchell et al. argue that fully autonomous agents should not be developed; this framework's L5 differs from their top level in that scope, tools and level are fixed outside the agent. CSA's framework is the closest peer: it ties levels to controls, defines promotion authority and automatic demotion, and requires that an agent cannot change its own level. It leaves open how a claimed level is verified, which the certificate (section 7) addresses.

Two distinctions from the critical literature are worth stating. Safin and Balta separate autonomy (how much the agent acts unsupervised) from agency (what it can do), and argue that as autonomy rises, agency must be constrained [24]. Here the worksheet scores agency and the level sets autonomy; the cap in section 5 is that constraint. Anthropic's production data show that autonomy drifts upward as operators gain experience, with auto-approval rising from about 20% of new users' sessions to over 40% for experienced ones, and argue against mandating interaction patterns [25]. This framework prescribes controls enforced outside the agent, not interaction patterns; how the human and the agent converse within a level is left open.

The EU AI Act requires human oversight measures "commensurate with the risks, level of autonomy and context of use" of a high-risk system (Article 14(3)) and that the overseer be able to override, disregard and stop it (Article 14(4)) [26]. The level is that measure, and AL-11 and AL-16 are the override and the stop.

**Human working modes.** The BCG field study [1] found three ways professionals work with generative AI. As an interpretation: L1 corresponds to the Centaur, L2 to L3 to the Cyborg, L4 to a Cyborg with a governed hand-off, and L5 to the Self-Automator, bounded by enforced controls. The study found that full delegation fails when it is unbounded. The framework keeps L5 available, but only for work that scores low risk and only behind controls AL-01 to AL-17.

## 10. Open questions and roadmap

Version 0.1 asked four questions. The state of each:

1. **Should promotion windows scale with the risk score?** Answered in version 0.2: the windows are minimums, and the rolling thresholds tighten with the score (section 6).
2. **In a multi-agent chain, is the effective level the lowest level in the chain?** Planned for version 0.3. The research points to a two-sided rule: the chain is capped at the lowest level in it, and that cap only holds if each hop receives a credential whose capabilities are a subset of its parent's, treats messages from other agents as untrusted content under AL-07, and is re-authorized at the resource it calls. Without those, a low-privilege agent can steer a high-privilege one through its output, and the chain must be certified at the union of what any path can reach [27][28]. This will bring ASI07 into scope and add a delegation-depth limit per level.
3. **Can Q2, Q6 and Q7 be answered automatically from the enforcement layer's configuration?** Partly. Where the enforcement layer holds a declarative policy, the reachable tools, data domains and cross-system flows can be read from it, which answers Q2 and Q6 and flags Q1. Q3, Q7 and Q8 need a person. Planned for version 0.3 as a `tools/derive.py` that pre-fills an answers file from a policy.
4. **What must a third party verify for a certificate to be trusted outside the issuing organization?** Planned for version 1.0: a certificate bound to a digest of the agent specification (model, prompts, tool manifest, policy), signed by the reviewer with existing supply-chain tooling, with evidence as typed pointers that carry their own expiry, and a registry that answers "is this certificate current?" at request time. Each piece exists in an adjacent field; none has been assembled for agents.

The full roadmap, with sources, is in `ROADMAP.md`. The research behind version 0.2 is in `docs/research-2026-09.md`. Feedback via GitHub issues is welcome.

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
11. Adversa AI. *AI Coding Agent Incidents.* 2026. https://adversa.ai/blog/ai-coding-agent-incidents/
12. *Overeager Coding Agents: Measuring Out-of-Scope Actions on Benign Tasks.* arXiv:2605.18583, May 2026. https://arxiv.org/abs/2605.18583
13. IETF. *Agent Authorization Profile for OAuth 2.0.* draft-aap-oauth-profile-00, February 2026. https://www.ietf.org/archive/id/draft-aap-oauth-profile-00.html
14. Cloud Security Alliance. *Agentic AI Autonomy Levels and Control Framework, v2.0.* March 2026. https://labs.cloudsecurityalliance.org/research/agentic-ai-autonomy-levels-control-framework-v2-csa-styled/
15. IETF. *Authentication and Authorization for AI Agents.* draft-klrc-aiagent-auth-03, 2026. https://datatracker.ietf.org/doc/html/draft-klrc-aiagent-auth-03
16. Skadden. *Colorado Repeals and Replaces Its AI Act.* June 2026. https://www.skadden.com/insights/publications/2026/06/colorado-repeals-and-replaces-its-ai-act
17. US Office of Management and Budget. Memorandum M-25-21, *Accelerating Federal Use of AI through Innovation, Governance, and Public Trust.* 3 April 2025. https://www.whitehouse.gov/wp-content/uploads/2025/02/M-25-21-Accelerating-Federal-Use-of-AI-through-Innovation-Governance-and-Public-Trust.pdf
18. Marreddy. *Trust Score Architecture.* May 2026. https://poojithamarreddy.substack.com/p/trust-score-architecture-the-framework
19. IMDA Singapore. *Model AI Governance Framework for Agentic AI.* January 2026, updated May 2026. https://www.imda.gov.sg/-/media/imda/files/about/emerging-tech-and-research/artificial-intelligence/mgf-for-agentic-ai.pdf
20. Anthropic. *Building auto mode for Claude Code.* March 2026. https://www.anthropic.com/engineering/claude-code-auto-mode
21. Gartner press release, 26 May 2026, as summarized at https://securitypointbreak.com/2026/05/26/gartner-ai-agent-governance-enterprise-failure/
22. Morris, Sohl-Dickstein, Fiedel, Warkentin, Dafoe, Faust, Farabet, Legg. *Levels of AGI for Operationalizing Progress on the Path to AGI.* ICML 2024. https://arxiv.org/abs/2311.02462
23. Mitchell, Ghosh, Luccioni, Pistilli. *Fully Autonomous AI Agents Should Not be Developed.* arXiv:2502.02649, 2025. https://arxiv.org/abs/2502.02649
24. Safin, Balta. *Autonomy and Agency in Agentic AI: Architectural Tactics for Regulated Contexts.* arXiv:2605.12105, May 2026. https://arxiv.org/abs/2605.12105
25. Anthropic. *Measuring AI agent autonomy in practice.* February 2026. https://www.anthropic.com/research/measuring-agent-autonomy
26. Regulation (EU) 2024/1689 (AI Act), Article 14. https://artificialintelligenceact.eu/article/14/
27. *Bounded Agents: Delegation Security for Multi-Agent AI Systems.* arXiv:2608.15888, August 2026. https://arxiv.org/abs/2608.15888
28. *Delegation Without Trust: An Empirical Gap Analysis of Identity, Authorization, and Runtime Governance in Multi-Agent LLM Systems.* arXiv:2609.00267, August 2026. https://arxiv.org/abs/2609.00267
