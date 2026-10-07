# SOC L1 Alert Triage

**Platform:** TryHackMe
**Path:** SOC Level 1 — Section 02: SOC Team Internals
**Difficulty:** Easy
**Type:** Walkthrough
**Status:** Complete

---

## Overview

Alert triage is the core daily activity of an L1 SOC analyst. This room covers the complete triage workflow: the event-to-alert pipeline, the properties of a structured alert, how to prioritise a queue with competing demands, and the step-by-step investigation process that leads to a well-documented classification.

---

## The Event-to-Alert Pipeline

Every alert originates from an event — something that happened on a system or the network. The pipeline:

```
Event occurs
    System generates a log entry
    Log shipped to SIEM via agent, syslog, or API
    SIEM normalises and indexes the log
    Correlation rule evaluates the log against defined conditions
    Rule fires — alert created
    Alert enters analyst queue
```

The gap between event time and alert arrival can range from seconds (real-time correlation) to minutes (batch ingestion). This gap is measured as MTTD (Mean Time To Detect) and is a key SOC performance metric.

---

## The SOC Toolstack

| Tool | Role |
|------|------|
| SIEM | Log aggregation, correlation, alerting, investigation interface |
| SOAR | Automated response for defined alert types |
| EDR/NDR | Endpoint and network telemetry, response capabilities |
| ITSM | Ticketing system for case management and SLA tracking |
| Threat Intel | IoC enrichment, reputation lookups |

The SIEM is the analyst's primary workspace. All alerts are reviewed here, investigations are run through its query interface, and context from other tools is pulled in to supplement the analysis.

---

## Anatomy of a Structured Alert

Every well-designed alert carries structured metadata:

| Field | Purpose |
|-------|---------|
| Alert Time | When the triggering event occurred — essential for timeline construction |
| Alert Name | The type of detection — defined by the detection engineering team |
| Alert Severity | Low / Medium / High / Critical — guides prioritisation |
| Alert Status | New / In Progress / Closed — tracks handling state |
| Alert Verdict | True Positive / False Positive — the analyst's classification |
| Alert Signee | Which analyst owns this case |
| Alert Description | What the rule detected, why it is suspicious, recommended investigation steps |
| Alert Fields | Specific data involved — username, source IP, process name, command line, file hash |

---

## Queue Prioritisation

When multiple alerts are waiting, the analyst should:

1. Filter out alerts already marked "In Progress" by another analyst
2. Within the remaining alerts, sort by severity — address Critical first
3. Within the same severity tier, address the oldest alert first

This prevents SLA breaches on alerts that have been waiting without attention and ensures the most serious threats receive earliest attention.

---

## The Triage Process — Step by Step

**Step 1 — Claim and read**
Assign the alert to yourself in the ITSM. Set status to "In Progress". Read the full alert description before taking any investigative action. The description often contains the detection engineer's reasoning and recommended first steps.

**Step 2 — Investigate**

Key questions to answer:
- Who is affected? What user account, what system, what network segment?
- What happened? What specific behaviour triggered the rule?
- When? What is the precise timeline? Are there related events before or after?
- Where? What system generated this? What is its role in the environment?
- Is this isolated or widespread? Are other systems showing the same behaviour?

Cross-reference with:
- Identity inventory (Active Directory / LDAP) — is this a privileged account?
- Asset inventory — what is this system used for? Is it critical infrastructure?
- Threat intelligence — is the source IP / hash / domain known malicious?

Document each step of the investigation as you go. Do not wait until the end to write notes.

**Step 3 — Classify**

- **True Positive** — the activity is genuinely malicious or constitutes a policy violation
- **False Positive** — the activity is legitimate; the rule fired incorrectly
- **Benign Positive** — the rule fired correctly on an activity that is technically within its scope but is authorised (e.g., a pentest, an approved maintenance task)

---

## Key Takeaways

Documentation during investigation is not optional. When an alert is escalated to L2, the L2 analyst should be able to reconstruct the entire investigation from the notes left by L1 — without having to re-examine the same evidence. Poor documentation does not just slow the handoff; it can result in missed context that leads to an incorrect classification at the next level.

---

## References

- [NIST SP 800-61 Computer Security Incident Handling Guide](https://csrc.nist.gov/publications/detail/sp/800-61/rev-2/final)
