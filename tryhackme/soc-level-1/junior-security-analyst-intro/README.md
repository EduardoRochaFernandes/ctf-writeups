# Room: Junior Security Analyst Intro

**Platform:** TryHackMe
**Path:** SOC Level 1
**Category:** SOC Fundamentals
**Difficulty:** Easy
**Type:** Walkthrough
**Cost:** Free
**Room Link:** https://tryhackme.com/room/jrsecanalystintrouxo

---

## What is this room about?

This room gives you a realistic glimpse into what a day in the life of an L1 SOC analyst actually looks like — the tools you use, the decisions you make, and the kind of incidents you deal with on a daily basis. It walks through the structure of a Security Operations Center and introduces the different tiers of analysts.

---

## The SOC Hierarchy

Within the blue team, the SOC is your primary workplace as an entry-level analyst. The structure is typically:

- **L1 Analysts** — triage incoming alerts, classify them, and escalate complex cases to L2
- **L2 Analysts** — investigate more sophisticated incidents that L1 escalates
- **SOC Engineers** — build and maintain the tools (SIEM rules, EDR configs, dashboards)
- **SOC Manager** — oversees the whole operation and handles escalations to leadership

The broader security org beyond the SOC includes the **CIRT (Cyber Incident Response Team)**, which handles large-scale breaches that overwhelm the SOC — groups like Mandiant, JPCERT, and AWS CIRT. Large tech companies also have specialized roles like Digital Forensics Analysts, Threat Intelligence Analysts, AppSec Engineers, and AI Security Researchers.

---

## What L1 Actually Does Day-to-Day

The core loop of an L1 analyst is simple in theory but mentally demanding in practice:

1. An **event** happens on a system — a file is downloaded, a login fails, a process is spawned
2. The system logs it
3. The **SIEM** aggregates the log, compares it against detection rules, and fires an **alert** if it matches
4. The alert lands in your queue
5. You **triage** it — investigate, classify, document, escalate or close

The challenge isn't understanding the process — it's doing it well under volume and pressure.

---

## Tools You Work With

| Tool | Purpose |
|------|---------|
| **SIEM** (Splunk, Elastic, Sentinel) | Aggregates and correlates logs, fires alerts |
| **EDR/NDR** | Endpoint and network visibility |
| **ITSM** (ticketing system) | Manages cases — similar to GitHub Issues or Jira |
| **Threat Intel platforms** | IoC lookups, reputation checks |

---

## Key Takeaways

> The SOC is the first line of defence. Your job isn't to stop every attack — it's to make sure no attack goes unnoticed.

What struck me most about this room is how much of L1 work is about **context and communication**, not just technical skill. Knowing how to write a clear escalation note, when to involve L2, and how to document your investigation so others can follow your reasoning — these skills matter as much as knowing your Wireshark filters.

The room also made clear that alert fatigue is real. A well-tuned SIEM with good rules is the difference between a SOC that catches threats and one that drowns in noise.

---

## References

- [TryHackMe SOC Level 1 Path](https://tryhackme.com/path/outline/soclevel1)
- [MITRE ATT&CK](https://attack.mitre.org/)
