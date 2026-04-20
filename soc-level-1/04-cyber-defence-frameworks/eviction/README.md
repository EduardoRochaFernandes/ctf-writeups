# Eviction

**Platform:** TryHackMe
**Path:** SOC Level 1 — Section 04: Cyber Defence Frameworks
**Difficulty:** Easy
**Type:** Walkthrough
**Status:** Complete

---

## Overview

Eviction is an applied Unified Kill Chain room. An APT group has targeted the organisation in a multi-stage attack. The player must map each observed activity to a UKC phase, identify the corresponding ATT&CK techniques, determine what detection source would catch it, and determine the appropriate defensive response at each phase.

---

## Attack Chain Analysis

The room presents the attack sequentially and asks for analysis at each step:

| Observed Activity | UKC Stage | ATT&CK Technique | Detection Source |
|------------------|-----------|------------------|-----------------|
| Attacker researches employees via LinkedIn and company website | IN — Reconnaissance | T1589, T1593 | Brand monitoring, OSINT self-assessment |
| Crafted spear phishing email sent to finance department | IN — Delivery | T1566.001 | Email gateway, sandbox analysis |
| Employee opens malicious Word document, enables macros | IN — Exploitation | T1204.002 | EDR, Sysmon Event ID 1 |
| VBA macro drops and executes payload | IN — Execution | T1059.005 | EDR, Script Block Logging |
| Payload adds registry Run key for persistence | IN — Persistence | T1547.001 | Sysmon Event ID 13, FIM |
| Implant establishes HTTPS beaconing to C2 | IN — C2 | T1071.001 | DNS monitoring, firewall outbound |
| Attacker enumerates Active Directory | THROUGH — Discovery | T1087.002 | SIEM LDAP query monitoring |
| Pass-the-Hash to move to domain controller | THROUGH — Lateral Movement | T1550.002 | Event ID 4624 Logon Type 9 |
| Data staged in compressed archive | OUT — Collection | T1074.001 | FIM, archive creation monitoring |
| Archive exfiltrated via HTTPS to cloud service | OUT — Exfiltration | T1048.002 | DLP, large outbound transfer alert |

---

## Defensive Response by Phase

| Phase | Immediate Response | Longer-Term Improvement |
|-------|--------------------|------------------------|
| Initial Access | Isolate affected endpoint | Improve email gateway rules |
| Persistence | Remove Run key, scan for other persistence mechanisms | Add FIM coverage for Run keys |
| C2 | Block C2 domain/IP | Add beaconing detection rule |
| Lateral Movement | Reset compromised credentials, force re-authentication | Implement tiered privileged access |
| Exfiltration | Identify what data left the environment | Implement DLP for large cloud uploads |

---

## Key Lessons

**Detection depth is more important than detection width.** An organisation that only detects at the email delivery phase will be compromised every time a sophisticated phishing email bypasses the gateway. An organisation with detection at persistence, C2, and lateral movement catches the attacker even if initial delivery is missed.

**The timeline matters as much as the individual events.** An LDAP enumeration event alone might be legitimate IT activity. LDAP enumeration following an unusual logon, following a macro execution event, from an account that doesn't normally query AD — that is an attack. The UKC provides the framework for asking "does this event fit into a broader attack chain?"

---

## References

- [MITRE ATT&CK](https://attack.mitre.org/)
- [Unified Kill Chain](https://www.unifiedkillchain.com/)
