# Room: Eviction

**Platform:** TryHackMe
**Path:** SOC Level 1
**Category:** Endpoint & EDR
**Difficulty:** Easy
**Type:** Walkthrough
**Cost:** Premium
**Room Link:** https://tryhackme.com/room/eviction

---

## What is this room about?

Applied Unified Kill Chain room. An APT attack scenario where you identify UKC phases, map ATT&CK techniques, and determine detection and response at each step.

---

## Kill Chain Phase Mapping

| Phase observed | UKC Stage | Detection source |
|----------------|-----------|-----------------|
| OSINT on employees | IN - Reconnaissance | Brand monitoring |
| Spear phishing email | IN - Delivery | Email gateway, sandbox |
| Macro executes | IN - Exploitation | EDR, Sysmon EID 1 |
| Backdoor + Run key | IN - Persistence | Sysmon EID 13, FIM |
| C2 established | IN - Command & Control | DNS anomalies |
| Internal network mapping | THROUGH - Discovery | Unusual LDAP queries |
| Lateral movement | THROUGH - Lateral Movement | Auth anomalies |
| Data staged in archive | OUT - Collection | FIM, file creation |
| Data exfiltrated via HTTPS | OUT - Exfiltration | DLP, transfer size alerts |

---

## Defensive Responses by Phase

| Phase | Primary response |
|-------|----------------|
| Delivery | Email gateway, sandbox, user training |
| Persistence | FIM, Autoruns monitoring, scheduled task alerting |
| C2 | DNS monitoring, outbound firewall rules |
| Lateral Movement | Network segmentation, privileged access management |
| Exfiltration | DLP, large transfer alerting |

---

## Key Takeaways

> Detection depth matters. If you only catch attacks at Delivery, one missed email = full compromise. Detections at every phase mean the attacker must evade multiple independent controls.

---

## References

- [MITRE ATT&CK](https://attack.mitre.org/)
- [Unified Kill Chain](https://www.unifiedkillchain.com/)
