# MITRE

**Platform:** TryHackMe
**Path:** SOC Level 1 — Section 04: Cyber Defence Frameworks
**Difficulty:** Medium
**Type:** Walkthrough
**Status:** Complete

---

## Overview

MITRE is a non-profit organisation that, since 2013, has maintained ATT&CK — the most widely used framework for understanding and communicating about adversary behaviour. This room covers the full MITRE ecosystem: ATT&CK, the Navigator, CAR (Cyber Analytics Repository), and D3FEND.

---

## ATT&CK — The Core Framework

**MITRE ATT&CK** (Adversarial Tactics, Techniques, and Common Knowledge) is a knowledge base of observed adversary behaviours, built from analysis of real-world attacks. It provides a common vocabulary for the cybersecurity community, enabling precise communication about techniques across tools, vendors, and organisations.

### The Three Levels

| Level | Definition | Example |
|-------|-----------|---------|
| Tactic | The *why* — the adversary's goal in a given phase | Credential Access |
| Technique | The *how* — the method used to achieve the tactic | T1110 — Brute Force |
| Procedure | The specific implementation in a real attack | Using Hydra against SSH with a domain user list |

### The ATT&CK Matrix

A grid with Tactics as columns and Techniques grouped beneath each tactic. The current Enterprise matrix covers 14 tactics:
Reconnaissance, Resource Development, Initial Access, Execution, Persistence, Privilege Escalation, Defense Evasion, Credential Access, Discovery, Lateral Movement, Collection, Command and Control, Exfiltration, Impact.

Each technique entry includes:
- Description of the technique
- Sub-techniques (specific variations)
- Procedure examples from real-world threat actors
- Detection guidance
- Mitigation recommendations

### ATT&CK Navigator

A web-based tool for annotating and exploring the ATT&CK matrix. Enables:
- Colour-coding techniques by coverage status (detected, partially detected, not covered)
- Creating layers showing which techniques are used by specific threat groups
- Comparing defence coverage against known adversary TTPs
- Exporting layers as JSON for sharing

---

## CAR — Cyber Analytics Repository

CAR complements ATT&CK by providing ready-to-use detection analytics. Where ATT&CK describes *what* attackers do, CAR provides the *queries* to detect it.

Each CAR analytic includes:
- Description of the behaviour being detected
- ATT&CK technique mapping
- Pseudocode logic description
- Concrete query implementations (Splunk SPL, EQL, Sigma)
- Unit tests where available

CAR has its own ATT&CK Navigator layer showing which techniques have published analytics, making it easy to identify detection gaps.

---

## D3FEND

D3FEND (Detection, Denial, and Disruption Framework Empowering Network Defense) is the defensive complement to ATT&CK. Where ATT&CK catalogues attack techniques, D3FEND catalogues defensive techniques — the specific countermeasures that address them.

D3FEND provides bidirectional mapping: given an ATT&CK technique, find the D3FEND countermeasure. Given a D3FEND countermeasure, see which ATT&CK techniques it addresses.

---

## Related MITRE Tools

| Tool | Purpose |
|------|---------|
| ATT&CK Navigator | Visualise and annotate ATT&CK matrix |
| Caldera | Automated adversary emulation using ATT&CK TTPs — for red/blue exercises |
| Adversary Emulation Library | Step-by-step plans to emulate known threat groups |
| ATLAS | ATT&CK for AI systems — covers ML model attacks |

---

## Why ATT&CK Changed Security Operations

Before ATT&CK, the same technique had different names in different tools, vendor reports, and internal documentation. A detection engineer calling something "credential dumping" might be using a completely different definition than a threat analyst at another organisation. ATT&CK created a universal identifier system — T1003.001 means LSASS Memory everywhere, unambiguously.

This shared language enables:
- Comparing detection coverage across tools and organisations
- Communicating threat intelligence precisely
- Mapping a SIEM alert to specific adversary TTPs
- Benchmarking detection capability against known threat group TTPs

---

## Key Takeaways

Every detection rule written in a mature SOC environment maps to an ATT&CK technique. When a Sigma rule fires on encoded PowerShell, the alert is tagged T1059.001 (Command and Scripting Interpreter: PowerShell). This makes it immediately possible to: identify related techniques commonly combined with it, look up other detections via CAR, and assess whether the organisation's coverage of the broader T1059 technique cluster is adequate.

---

## References

- [MITRE ATT&CK](https://attack.mitre.org/)
- [ATT&CK Navigator](https://mitre-attack.github.io/attack-navigator/)
- [MITRE CAR](https://car.mitre.org/)
- [MITRE D3FEND](https://d3fend.mitre.org/)
- [Caldera](https://caldera.mitre.org/)
