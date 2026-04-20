# Cyber Kill Chain

**Platform:** TryHackMe
**Path:** SOC Level 1 — Section 04: Cyber Defence Frameworks
**Difficulty:** Easy
**Type:** Walkthrough
**Status:** Complete

---

## Overview

The Cyber Kill Chain, developed by Lockheed Martin in 2011, models a cyberattack as a sequential chain of phases an adversary must complete from initial reconnaissance to achieving their objective. The framework's insight for defenders is that breaking the chain at any phase prevents the attacker from reaching their goal — and the earlier the break, the better.

---

## Phase 1 — Reconnaissance

The attacker researches the target before any offensive action begins. The quality of reconnaissance determines the quality of every subsequent phase.

**Passive reconnaissance** — no direct contact with target systems. Sources include:
- WHOIS and DNS records (registrant information, name servers, mail servers)
- Job postings (reveal technology stack, security tools, infrastructure details)
- LinkedIn and professional networks (employee names, roles, departments, technology skills)
- GitHub repositories (leaked credentials, infrastructure code, technology choices)
- Breach databases (previously compromised credentials that may still be valid)

**Active reconnaissance** — direct interaction with target systems, leaving traces:
- Port scanning (Nmap, Masscan)
- Service banner grabbing
- Web application fingerprinting
- Social engineering (calls, emails probing for information)

**Tools commonly used:** theHarvester (email and subdomain harvesting), Hunter.io (company email pattern discovery), Shodan (internet-connected device enumeration), OSINT Framework.

---

## Phase 2 — Weaponisation

The attacker selects and prepares tools for the specific target. Three profiles:

- **Script kiddies:** Purchase pre-built malware from darknet markets
- **Intermediate actors:** Modify open-source or purchased tools to evade signature detection
- **APT / nation-state actors:** Develop custom malware from scratch, designed to evade all known signatures and behave benignly until specific conditions are met

Weaponisation outputs: malicious document with embedded macro, infected executable, C2 infrastructure provisioned and configured, phishing templates crafted using reconnaissance data.

---

## Phase 3 — Delivery

The mechanism by which the payload reaches the target:

- **Spear phishing email** — most common. Targeted, uses reconnaissance data to appear credible.
- **USB drop** — infected drives left in target locations (car parks, lobbies, conference rooms)
- **Watering hole attack** — compromising a website the target is known to visit. The drive-by download or injected script executes when the target browses the site.
- **Supply chain** — compromising software or hardware before it reaches the target

---

## Phase 4 — Exploitation

The payload executes on the target system. This can occur via:
- Software vulnerability (browser exploit, document processing vulnerability, unpatched service)
- User action (opening a macro-enabled document, running a downloaded executable)
- Credentials (valid stolen credentials used to authenticate directly)

---

## Phase 5 — Installation

The attacker establishes persistence to survive reboots and maintain access:

- **Web shells** — scripts (.php, .aspx) uploaded to a web server, allowing command execution via HTTP. Popular because they communicate over standard web ports.
- **Registry Run keys** — `HKLM\SOFTWARE\Microsoft\Windows\CurrentVersion\Run` executes a payload at system boot; `HKCU\...` executes at user logon
- **Scheduled tasks** — malicious tasks created via `schtasks` or Task Scheduler (Event ID 4698)
- **Service installation** — malicious service registered to execute at startup
- **Timestomping** — modifying file creation/modification timestamps to make malware appear as though it has always been present, complicating forensic timeline analysis

---

## Phase 6 — Command and Control (C2)

The attacker establishes a persistent communication channel between their infrastructure and the implant on the compromised system. Communication patterns:

- **HTTP/HTTPS** — blends with normal web traffic, often uses legitimate-looking domains
- **DNS tunnelling** — encodes data in DNS queries and responses, bypasses many firewalls
- **Beaconing** — implant checks in at regular intervals (every 30s, 60s, 5min) to receive instructions. Detectable as regular outbound connections on an IO graph.

---

## Phase 7 — Actions on Objectives

The final phase: the attacker achieves what they came for. Common objectives:
- **Credential harvesting** — dumping hashes from LSASS, extracting browser credentials
- **Data exfiltration** — copying files to external storage or C2
- **Ransomware deployment** — encrypting files, deleting shadow copies, demanding ransom
- **Lateral movement** — expanding access to additional systems before executing the final objective
- **Persistent access** — some APTs aim to maintain long-term quiet access rather than causing immediate visible damage

---

## The Defender's Advantage

An attacker must complete every phase. A defender needs to detect and respond at only one.

The earlier in the chain detection occurs, the less damage results:
- Detecting at Reconnaissance: attacker has no foothold
- Detecting at Delivery: payload never executes
- Detecting at Installation: persistence not established
- Detecting at C2: attacker has access but cannot receive instructions
- Detecting at Actions on Objectives: attacker has achieved something but damage can still be limited

Layered detection coverage across multiple phases is the practical implementation of this principle.

---

## Limitations

The original Kill Chain assumes a single attacker executing phases linearly against an external target. It does not model:
- Insider threats (starting inside the network)
- Attacks that cycle back through phases (failed exploitation, retry with different technique)
- Highly automated attacks that complete multiple phases simultaneously

The Unified Kill Chain and MITRE ATT&CK address these limitations.

---

## References

- [Lockheed Martin — Intelligence-Driven Computer Network Defense](https://lockheedmartin.com/content/dam/lockheed-martin/rms/documents/cyber/LM-White-Paper-Intel-Driven-Defense.pdf)
- [MITRE ATT&CK](https://attack.mitre.org/)
