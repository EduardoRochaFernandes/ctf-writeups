# Blue Team Introduction

**Platform:** TryHackMe
**Path:** SOC Level 1 — Section 01: Blue Team Introduction
**Difficulty:** Easy
**Type:** Walkthrough
**Status:** Complete

---

## Overview

This introductory room establishes the organisational context for defensive security work. It covers the structure of security departments in enterprise environments, defines the role of the blue team within that structure, and explains how the SOC relates to adjacent teams such as red team, GRC, and incident response.

---

## Security Department Structure

In large organisations, the CISO sits below executive leadership and oversees multiple specialised security teams. The primary teams are:

| Team | Focus |
|------|-------|
| Red Team | Offensive security, penetration testing, adversary simulation |
| Blue Team | Defensive security — SOC analysts, engineers, incident responders |
| GRC | Governance, risk management, compliance with frameworks such as PCI DSS, ISO 27001 |
| Threat Research | Proactive hunting, adversary intelligence, emerging threat analysis |

In smaller organisations, a single "information security" team handles all of these responsibilities, which is why broad exposure across disciplines is valued early in a career.

---

## The Blue Team in Depth

The blue team is the defensive counterpart to the red team. Its primary responsibilities are:

- Continuous monitoring of systems and networks for indicators of compromise
- Detection, classification, and escalation of security alerts
- Incident response and containment when a breach is confirmed
- Maintenance and improvement of detection tooling
- Threat intelligence collection and operationalisation

Blue team work spans multiple specialisations. The SOC handles day-to-day detection and triage. A CIRT (Cyber Incident Response Team) handles major confirmed breaches, often working under significant time pressure. Threat researchers study adversary groups proactively to produce intelligence that informs detection engineering.

### Known CIRTs

- **Mandiant** — private firm, engaged globally for large-scale incident response
- **JPCERT** — Japan's national computer emergency response team, handles nation-state level incidents
- **AWS CIRT** — investigates security incidents within AWS customer environments

---

## The SOC Hierarchy

Within the blue team, the SOC is the operational core. A typical structure:

```
SOC Manager
  L3 Analyst / SOC Engineer     (detection engineering, tooling, escalation)
    L2 Analyst                  (investigation, threat hunting, escalation)
      L1 Analyst                (alert triage, initial classification, documentation)
```

**L1** — First responder to alerts. Triages the queue, classifies as true/false positive, documents findings, escalates to L2 when necessary. High volume, pattern recognition develops quickly.

**L2** — Deeper investigation. Handles escalations from L1, performs more complex analysis, may engage incident response procedures.

**L3 / SOC Engineer** — Builds and maintains the detection infrastructure. Writes SIEM rules, manages EDR configurations, develops playbooks, tunes detection to reduce false positives.

**SOC Manager** — Oversees operations, handles stakeholder communication, manages SLAs and team workload.

---

## Managed Security Service Providers

Many organisations, particularly those without the budget or staff for an internal SOC, contract a Managed Security Service Provider (MSSP) to provide SOC services externally. The room distinguishes between:

- **In-house SOC** — internal team, deep knowledge of the organisation's environment
- **MSSP** — external provider managing multiple clients, broader threat landscape visibility but less organisational context

---

## Key Takeaways

The blue team is not a single role but a collection of complementary specialisations. Starting as an L1 analyst provides exposure to the full attack lifecycle across every technology layer — a breadth that takes years to develop in more specialised roles. The skills built through alert triage, documentation, and escalation translate directly into every senior defensive role.

---

## References

- [MITRE ATT&CK](https://attack.mitre.org/)
- [CISA Blue Team Resources](https://www.cisa.gov/topics/cybersecurity-best-practices)
