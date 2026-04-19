# Room: SOC Role in Blue Team

**Platform:** TryHackMe
**Path:** SOC Level 1
**Category:** SOC Fundamentals
**Difficulty:** Easy
**Type:** Walkthrough
**Cost:** Free
**Room Link:** https://tryhackme.com/room/socroleblue

---

## What is this room about?

This room gives a broader view of where the SOC sits within the cybersecurity landscape — how it relates to other security roles, how career progression works from L1 to senior roles, and what the blue team ecosystem looks like beyond just the SOC.

---

## The Security Org Chart

Starting from the top of a typical enterprise:

```
CEO / Board
    └── CISO (Chief Information Security Officer)
            ├── SOC (Security Operations)
            │     ├── L1 Analysts (triage)
            │     ├── L2 Analysts (investigation)
            │     ├── SOC Engineers (tooling)
            │     └── SOC Manager
            ├── CIRT (Incident Response)
            ├── Red Team (offensive testing)
            └── Specialised Roles (forensics, threat intel, AppSec)
```

---

## Beyond the SOC — Other Blue Team Roles

| Role | What they do |
|------|-------------|
| **Digital Forensics Analyst** | Uncovers hidden threats in disk images and memory dumps |
| **Threat Intelligence Analyst** | Tracks emerging threat groups and their TTPs |
| **AppSec Engineer** | Secures the software development lifecycle (SDLC) |
| **AI Security Researcher** | Studies AI-specific attacks and defences |
| **CIRT Analyst** | Responds to major breaches beyond SOC capacity |

### Notable CIRT Teams
- **Mandiant** — private firm, responds to global incidents
- **JPCERT** — Japan's national CERT
- **AWS CIRT** — investigates incidents in AWS environments

---

## Career Progression from L1

A typical path looks like:

```
L1 SOC Analyst
    → L2 SOC Analyst (1-2 years)
    → L3 / SOC Engineer (2-4 years)
    → Threat Intelligence / Incident Response
    → Security Engineering / Architecture
    → CISO (long-term)
```

Certifications that accelerate this: CompTIA Security+, CySA+, BTL1, CEH, OSCP (for those moving toward red team), GCIH, GCIA.

---

## Key Takeaways

> The SOC is not a dead-end job — it's a launchpad. Every hour of triage builds pattern recognition that specialists spend years developing in other ways.

Starting in the SOC gives you exposure to the full attack lifecycle — phishing, malware, lateral movement, exfiltration — across dozens of incident types in your first year. That breadth is genuinely hard to replicate in any other entry-level security role.

---

## References

- [TryHackMe SOC Role in Blue Team](https://tryhackme.com/room/socroleblue)
