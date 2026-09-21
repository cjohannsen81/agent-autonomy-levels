# Mapping: OWASP Top 10 for Agentic Applications 2026

Which framework controls address each OWASP Agentic risk, and from which level.

| OWASP risk | Title | Framework controls | Covered from |
|---|---|---|---|
| ASI01 | Agent Goal Hijack | AL-03, AL-07 | L1 (partial), L2 |
| ASI02 | Tool Misuse and Exploitation | AL-04, AL-05, AL-09, AL-10 | L1 (partial), L3 |
| ASI03 | Identity and Privilege Abuse | AL-01, AL-04, AL-12 | L1 (partial), L4 |
| ASI04 | Agentic Supply Chain Vulnerabilities | AL-03, AL-15 | L1 (tool pinning), L5 (signed components) |
| ASI05 | Unexpected Code Execution | none in v0.1 | Out of scope: needs runtime sandboxing |
| ASI06 | Memory and Context Poisoning | AL-06, AL-07 | L2 (partial) |
| ASI07 | Insecure Inter-Agent Communication | none in v0.1 | Out of scope: needs agent-to-agent authentication |
| ASI08 | Cascading Failures | AL-08, AL-13 | L2 (partial), L4 |
| ASI09 | Human-Agent Trust Exploitation | AL-11 | L4 |
| ASI10 | Rogue Agents | AL-02, AL-09, AL-13, AL-14, AL-16 | L1 (detection), L5 |

"Partial" means the control reduces the risk but does not cover every attack pattern OWASP lists for it.

Source: https://genai.owasp.org/resource/owasp-top-10-for-agentic-applications-for-2026/
