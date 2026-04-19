# Room: Defensive Security Intro

**Platform:** TryHackMe
**Path:** SOC Level 1
**Category:** SOC Fundamentals
**Difficulty:** Easy
**Type:** Walkthrough
**Cost:** Free
**Room Link:** https://tryhackme.com/room/defensivesecurityintro

---

## What is this room about?

A broad introduction to defensive security — who does it, what it covers, and what the job looks like in practice. Covers the SOC and DFIR pillars, and ends with a hands-on SIEM simulation investigating a real alert at a fictional bank.

---

## Offensive vs Defensive Security

| | Offensive (Red Team) | Defensive (Blue Team) |
|--|---------------------|----------------------|
| Goal | Find and exploit vulnerabilities | Prevent, detect, respond |
| Output | Pentest reports | Hardened systems, playbooks |

Two objectives: **prevention** (stop attacks before they happen) and **detection & response** (catch attacks in progress).

---

## Core Defensive Tasks

- **Asset Management** — can't protect what you don't know exists
- **Patch Management** — most breaches exploit known, patchable vulnerabilities
- **User Awareness** — users are the most targeted attack surface
- **Threat Intelligence** — know who attacks you, why, and how
- **Log Management** — collect and centralise logs from every system

---

## The Two Pillars

### Security Operations Center (SOC)
Centralised team monitoring 24/7. Detects vulnerabilities, policy violations, unauthorised access, intrusions.

### DFIR — Digital Forensics and Incident Response
When the SOC detects an incident:

**Incident Response — 4 phases:**
1. **Preparation** — document procedures, train, deploy tools
2. **Detection & Analysis** — identify and validate
3. **Containment, Eradication & Recovery** — stop spread, remove attacker, restore
4. **Post-Incident** — report, fix what failed, improve defences

---

## Malware Types

| Type | Behaviour |
|------|-----------|
| **Virus** | Attaches to programs, spreads on execution |
| **Trojan Horse** | Appears legitimate, hides malicious function |
| **Ransomware** | Encrypts files, demands payment for key |

---

## The Hands-On Simulation

SIEM flags suspicious login from unknown IP at 3 AM. You investigate via threat intel tool (confirmed malicious), escalate to SOC lead, create firewall rule blocking the IP. Flag: `THM{THREAT-BLOCKED}`.

---

## Key Takeaways

> Defensive security is not reactive by nature. The best defenders constantly learn about attackers to anticipate what comes next.

---

## References

- [MITRE ATT&CK](https://attack.mitre.org/)
- [CISA Incident Response](https://www.cisa.gov/topics/cybersecurity-best-practices)
