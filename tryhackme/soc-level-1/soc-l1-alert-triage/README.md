# Room: SOC L1 Alert Triage

**Platform:** TryHackMe
**Path:** SOC Level 1
**Category:** SOC Fundamentals
**Difficulty:** Easy
**Type:** Walkthrough
**Cost:** Free
**Room Link:** https://tryhackme.com/room/socl1alerttriage

---

## What is this room about?

This room teaches the systematic approach to triaging SOC alerts — from the moment an alert lands in your queue to classifying it as a true positive or false positive. It covers the tools used, the properties of an alert, how to prioritise, and the step-by-step investigation process.

---

## The Alert Lifecycle

Every alert starts as an **event** — something that happened on a system. The flow is:

```
Event occurs on system
    → System logs it
    → SIEM aggregates and correlates logs
    → Detection rule fires → Alert generated
    → Alert lands in analyst queue
    → Analyst triages
```

---

## Tools in the SOC Stack

| Tool | Role |
|------|------|
| **SIEM** (Splunk, Elastic, Sentinel) | Aggregates logs, correlates events, fires alerts |
| **SOAR** | Automates response actions for common alert types |
| **EDR/NDR** | Endpoint and network visibility and response |
| **ITSM** (ticketing) | Manages alert cases — similar to GitHub Issues |

---

## Anatomy of an Alert

Every alert has structured properties that guide your investigation:

| Field | Meaning |
|-------|---------|
| **Alert Time** | When the event occurred — critical for building a timeline |
| **Alert Name** | Type of alert — defined by SOC Engineers, can be updated |
| **Alert Severity** | Low / Medium / High / Critical |
| **Alert Status** | New → In Progress → Closed |
| **Alert Verdict** | True Positive or False Positive |
| **Alert Signee** | Which team/analyst owns this case |
| **Alert Description** | Context, why it's suspicious, recommended next steps |
| **Alert Fields** | Specific data involved — username, IP, command line, file |

---

## Prioritisation

When multiple alerts are in your queue, filter first — skip anything already "In Progress" (someone else has it). Then within your severity tier, start with the **oldest** alert. This prevents SLA breaches on alerts that have been waiting.

---

## The Triage Process (Step-by-Step)

**Step 1 — Claim the alert:**
- Assign it to yourself in the ITSM
- Change status to "In Progress"
- Read the full alert description carefully before doing anything else

**Step 2 — Investigate:**
- Who was affected? What system, what user?
- What happened exactly? What triggered this rule?
- Cross-reference with external sources (threat intel, IP reputation)
- Document every step — if you escalate, L2 needs your notes

**Step 3 — Classify:**
- **True Positive** — the alert represents real malicious or suspicious activity
- **False Positive** — the activity is legitimate, the rule fired incorrectly

---

## Key Takeaways

> Alert triage is not just technical — it's structured thinking under time pressure. A clear head and a consistent process beat raw technical knowledge every time.

The thing this room really hammered home is that **documentation during investigation is not optional**. When you escalate to L2, your notes are the handoff. Bad notes = L2 starting from scratch = wasted time = longer attacker dwell time.

---

## References

- [TryHackMe SOC L1 Alert Triage](https://tryhackme.com/room/socl1alerttriage)
- [MITRE ATT&CK](https://attack.mitre.org/)
