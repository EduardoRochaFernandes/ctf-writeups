# Unified Kill Chain

**Platform:** TryHackMe
**Path:** SOC Level 1 — Section 04: Cyber Defence Frameworks
**Difficulty:** Easy
**Type:** Walkthrough
**Status:** Complete

---

## Overview

The Unified Kill Chain (UKC), created by Paul Pols in 2017 and updated in 2022, addresses the limitations of the original Cyber Kill Chain by modelling 18 phases of a complete attack across three macro-stages. It explicitly recognises that attacks are non-linear — adversaries revisit phases, adapt when blocked, and cycle through portions of the chain multiple times.

---

## The Three Macro-Stages

### Stage 1 — IN: Initial Foothold

The objective of this stage is to gain a presence on the target network or system.

| Phase | Description |
|-------|-------------|
| Reconnaissance | OSINT, active scanning, social media intelligence |
| Weaponisation | Build C2 infrastructure, prepare payloads, craft phishing materials |
| Delivery | Email, USB, watering hole, supply chain |
| Social Engineering | Impersonation, urgency manipulation, deepfakes, fake OAuth prompts |
| Exploitation | Code executes on the target system |
| Persistence | Backdoors, Run keys, scheduled tasks, modified services |
| Defence Evasion | Code obfuscation, Living-off-the-Land (LotL), log tampering, timestomping, token impersonation |
| Command and Control | Establishing the communication channel — HTTP beaconing, DNS tunnelling |

### Stage 2 — THROUGH: Network Propagation

With an initial foothold, the attacker moves through the environment toward their real target.

| Phase | Description |
|-------|-------------|
| Pivoting | Using a compromised host as a jump point to reach internal systems inaccessible from the internet |
| Discovery | Internal reconnaissance — mapping the network, finding high-value systems, enumerating users and permissions |
| Privilege Escalation | Elevating from standard user to local admin, from local admin to domain admin, from domain admin to Domain Controller |
| Execution | Running malicious code on newly compromised systems |
| Credential Access | Keylogging, LSASS dumping, browser credential extraction, DCSync |
| Lateral Movement | Moving between systems using valid credentials or exploits |

### Stage 3 — OUT: Action on Objectives

The attacker executes their final objective.

| Phase | Description |
|-------|-------------|
| Collection | Gathering data from drives, email, audio/video recording, browser history |
| Exfiltration | Moving collected data out of the network — encrypted channels, cloud storage, slow/staged transfers |
| Impact | Ransomware, disk wipe, DoS, defacement, operational disruption |
| Objectives | The strategic goal: financial gain, espionage, hacktivism, sabotage, silent long-term access |

---

## Exfiltration Techniques

Exfiltration is designed to evade Data Loss Prevention (DLP) controls:

- **Encryption before exfil** — DLP cannot inspect encrypted archives
- **Using the C2 channel** — exfil blends with existing C2 traffic
- **Slow exfiltration** — sending small amounts over days or weeks to avoid volume threshold alerts
- **Cloud storage** — HTTPS uploads to legitimate services (OneDrive, Dropbox, Google Drive) that are rarely blocked
- **DNS tunnelling** — encoding data in DNS query subdomains

---

## Why the UKC Improves on the Original Kill Chain

| Aspect | Original Kill Chain | Unified Kill Chain |
|--------|--------------------|--------------------|
| Phases | 7 | 18 |
| Linearity assumed | Yes | No — explicitly non-linear |
| Internal movement | Not modelled | Stage 2 (THROUGH) |
| Insider threats | Not modelled | Starts at Stage 2 |
| ATT&CK compatibility | Limited | Designed to complement ATT&CK |

---

## Practical Application — Alert Triage

The UKC provides context for interpreting alerts:

**Privilege Escalation alert** → attacker is in Stage 2 (THROUGH). This means:
- Initial foothold already established — look backwards in the timeline for Stage 1 activity
- Persistence mechanisms may already be in place
- Check for lateral movement to other hosts
- The compromise may be older than the alert suggests

**Unusual DNS query volume** → possible exfiltration (Stage 3, OUT). This means:
- Collection phase may have already completed
- Look for large file access events or archive creation earlier in the timeline
- Identify what data was accessible from the compromised system

---

## Key Takeaways

When an alert fires, it represents a single event in what is almost certainly a longer attack chain. The UKC provides the map for working backwards (what did the attacker do to get here?) and forwards (where are they going?). An analyst who thinks in kill chain terms will always ask both questions before closing a case.

---

## References

- [Unified Kill Chain — official documentation](https://www.unifiedkillchain.com/)
- [Paul Pols — original research](https://www.unifiedkillchain.com/assets/The-Unified-Kill-Chain.pdf)
- [MITRE ATT&CK Navigator](https://mitre-attack.github.io/attack-navigator/)
