# SOC Role in Blue Team

**Platform:** TryHackMe
**Path:** SOC Level 1 — Section 01: Blue Team Introduction
**Difficulty:** Easy
**Type:** Walkthrough
**Status:** Complete

---

## Overview

This room situates the SOC analyst within the full organisational security structure. It covers the security department hierarchy, the distinctions between in-house and managed SOC models, the specialised roles within a blue team, and what career progression from L1 looks like.

---

## The Security Hierarchy

At the top: **CISO** (Chief Information Security Officer) — responsible for the organisation's entire security programme and makes key cybersecurity decisions.

Below the CISO, specialised teams:

| Team | Focus |
|------|-------|
| SOC (Blue Team) | Monitoring, detection, response — L1, L2, L3, engineers |
| Red Team | Offensive testing, adversary simulation |
| GRC | Governance, Risk, Compliance |
| Threat Research | Proactive intelligence, hunting, adversary tracking |
| AppSec | Securing the software development lifecycle |
| Cloud Security | Securing cloud infrastructure |

---

## SOC Models

**In-house SOC:** The organisation employs its own security team. Has deep familiarity with the environment, business context, and internal systems. Higher cost.

**MSSP (Managed Security Service Provider):** An external company provides SOC services, typically monitoring multiple clients simultaneously. Lower cost, broader threat visibility across clients, but less organisational context.

Many companies use a hybrid model — an internal team handles the most sensitive monitoring while an MSSP supplements coverage outside business hours.

---

## Blue Team Roles

Beyond the standard L1/L2/L3 ladder:

**Threat Researcher** — Proactively hunts for threats, analyses adversary groups and their TTPs, and produces intelligence that feeds detection engineering. Often interfaces with threat intelligence platforms like MISP and VirusTotal.

**SOC Engineer** — Builds and maintains the tooling. Writes SIEM correlation rules, manages EDR configurations, builds SOAR playbooks, and continuously improves detection quality to reduce false positive rates.

**Incident Responder** — Engages when a confirmed breach occurs. Focuses on containment, eradication, forensic analysis, and recovery. Works under significant time pressure during active incidents.

**Forensics Analyst** — Performs deep post-incident analysis of disk images, memory dumps, and network captures to reconstruct attacker activity and support legal proceedings.

---

## Career Progression from L1

A typical progression path:

```
L1 SOC Analyst (0–2 years)
  Pattern recognition, alert triage, documentation, escalation

L2 SOC Analyst (2–4 years)
  Complex investigation, threat hunting, playbook development

SOC Engineer / Threat Researcher (3–6 years)
  Detection engineering, SIEM rule development, CTI

Incident Responder / Forensics (4+ years)
  Active incident management, forensic analysis

Security Architect / CISO (senior)
  Programme design, risk management, leadership
```

Certifications that support this path: CompTIA Security+, BTL1, CySA+, GCIH, GCIA, GREM, CISSP.

---

## Key Takeaways

The SOC is the operational core of the blue team, but blue team work extends well beyond alert triage. Understanding the full landscape of roles — and where they intersect — is important for planning a career trajectory. Every L1 analyst should be building skills that map to the role they want in three to five years, not just optimising for the work in front of them today.

---

## References

- [TryHackMe SOC Level 1](https://tryhackme.com/path/outline/soclevel1)
