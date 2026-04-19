# Room: SOC L1 Alert Reporting

**Platform:** TryHackMe
**Path:** SOC Level 1
**Category:** SOC Fundamentals
**Difficulty:** Easy
**Type:** Walkthrough
**Cost:** Free
**Room Link:** https://tryhackme.com/room/socl1alertreporting

---

## What is this room about?

After triage comes documentation. This room covers how to write proper SOC alert reports, when and how to escalate, and how to communicate effectively during incidents — including some tricky edge cases that trip up junior analysts.

---

## The Post-Triage Workflow

```
Triage complete
    → Reporting (document everything)
    → Escalation (pass to L2 if needed)
    → Communication (talk to the right people, the right way)
```

---

## Why Write Reports?

Three reasons that matter in practice:

1. **Context for L2** — when you escalate, L2 needs to understand what you found without starting from zero
2. **Permanent audit record** — organisations need documented evidence for compliance and legal purposes
3. **Your own development** — writing forces clarity. If you can't explain what happened, you don't fully understand it yet

---

## Report Structure — The 5 Ws

A well-written alert report answers:

| Question | What to include |
|----------|----------------|
| **Who** | Users involved, account types (admin/regular), affected systems |
| **What** | What happened, what was affected, how it happened |
| **When** | Timeline of events in chronological order |
| **Where** | Affected device, IP addresses, URLs, network location |
| **Why** | Your verdict — True Positive or False Positive, and the evidence that supports it |

---

## Standard Report Template

```
Time of activity: [timestamp]
List of Affected Entities: [users, hosts, IPs]
Reason for Classifying as True/False Positive: [your evidence]
Reason for Escalating: [why L2 needs to handle this]
Recommended Remediation Actions: [what should happen next]
List of Attack Indicators: [IoCs — IPs, hashes, domains]
```

---

## When to Escalate

Not every True Positive needs escalation, but escalate when:

- The attack is too sophisticated or damaging for L1 to handle
- Malware removal or system cleaning is required
- External communication is needed (clients, partners, law enforcement)
- You simply don't understand what you're looking at — that's not weakness, that's good judgment

---

## Communication Edge Cases (Real Scenarios)

**Scenario 1 — L2 not responding for 30 minutes:**
Don't wait. Escalate upward — L3, then manager. Document every escalation attempt with timestamps.

**Scenario 2 — Need to verify with a user whose Slack account was compromised:**
Never use the compromised channel. The attacker might be reading it. Use an alternative — phone, in-person, email to a personal address.

**Scenario 3 — Flood of critical alerts simultaneously:**
Follow normal process but immediately notify L2 about the volume. High alert volume can itself be an attack (distraction technique).

**Scenario 4 — Realised days later that you misclassified an alert:**
Contact L2 immediately. Do not try to quietly fix it. Every hour of delay is potentially more attacker dwell time.

**Scenario 5 — SIEM logs are badly parsed and you can't fully investigate:**
Don't skip the alert. Investigate with what's available, document the limitations explicitly, and report the parsing issue to L2/engineers.

---

## Key Takeaways

> A report that L2 can act on immediately is more valuable than a technically perfect investigation with poor documentation.

Communication is a skill that takes practice. The structured 5W approach gives you a framework so you're never staring at a blank page when you need to write a report quickly.

---

## References

- [TryHackMe SOC L1 Alert Reporting](https://tryhackme.com/room/socl1alertreporting)
