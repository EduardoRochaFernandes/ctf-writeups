# SOC L1 Alert Reporting

**Platform:** TryHackMe
**Path:** SOC Level 1 — Section 02: SOC Team Internals
**Difficulty:** Easy
**Type:** Walkthrough
**Status:** Complete

---

## Overview

Once triage is complete, the analyst's work is not finished — the findings must be documented in a report that serves as the permanent record of the investigation and, if required, the basis for escalation. This room covers report structure, escalation criteria, and the communication decisions that arise in edge cases.

---

## Why Reporting Matters

A well-written alert report serves three purposes:

1. **Handoff context** — when an alert is escalated to L2, the report is the entire briefing. An L2 analyst who receives a clear, structured report can continue the investigation without starting over.

2. **Audit record** — organisations operating under regulatory frameworks (PCI DSS, HIPAA, NIS2) are required to demonstrate that security events were handled appropriately. The report is the evidence.

3. **Knowledge development** — writing forces clarity. If the investigation cannot be explained clearly, it was not fully understood.

---

## Report Structure — The Five Ws

| Question | What to address |
|----------|----------------|
| Who | All accounts and systems involved. User type (admin, service account, standard user), organisational context. |
| What | Specific technical event. What action occurred, what system performed it, what data was involved. |
| When | Precise chronological sequence of events. Start, each step, end. Use UTC timestamps. |
| Where | Affected systems, network segments, IP addresses, and their role in the environment. |
| Why | Your classification and the evidence that supports it. Why is this a true positive and not a false positive? What would convince a sceptical reader? |

---

## Standard Report Fields

```
Time of first activity:
Time alert fired:
Affected entities (users, systems, IPs):
Observed behaviour:
Reason for True Positive / False Positive classification:
Supporting evidence:
Recommended remediation actions:
Indicators of Compromise (if applicable):
Escalation recommendation:
```

---

## When to Escalate

Not all true positives require L2 involvement, but escalate when:

- The incident is beyond L1's scope or authority to resolve
- Malware removal, system reimaging, or forensic acquisition is required
- External communication is involved — clients, partners, regulators, or law enforcement
- The investigation has reached a point where further progress requires deeper access or specialised knowledge
- You are uncertain whether the classification is correct — escalating an ambiguous alert is better than incorrectly closing a true breach

---

## Communication Edge Cases

**L2 is unresponsive for an extended period during an active incident:**
Escalate upward through the chain — L3, then manager. Document every escalation attempt with timestamp. Do not allow a critical incident to stall because one person is unavailable.

**The account that needs verification is the compromised channel:**
If a Slack or Teams account is potentially compromised, do not contact the user through that application. The attacker may be reading the messages. Use an alternative channel — phone, in-person, personal email.

**High alert volume during a potential attack:**
Process alerts normally but immediately notify L2 of the volume. High alert volume can itself be an attack pattern — either a DDoS generating noise, or a distraction while the real attack occurs elsewhere.

**A misclassification is discovered days later:**
Contact L2 immediately and disclose the error. Every hour of delay is additional attacker dwell time if the incident was genuine. Document the error and how it was caught — this information improves the team's process.

**SIEM logs are malformed or unsearchable:**
Investigate with whatever data is available. Document the data quality limitation explicitly in the report. Report the parsing issue to the SOC engineering team. Do not skip or close the alert because investigation is difficult.

---

## Key Takeaways

The quality of an alert report reflects the quality of the analyst who wrote it. A report that L2 can act on immediately — with clear evidence, a defensible classification, and actionable next steps — is the standard to work toward on every case. Brevity is a virtue, but not at the cost of completeness.

---

## References

- [SANS Incident Handler's Handbook](https://www.sans.org/white-papers/33901/)
