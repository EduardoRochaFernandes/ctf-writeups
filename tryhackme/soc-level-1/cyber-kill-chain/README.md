# Room: Cyber Kill Chain

**Platform:** TryHackMe
**Path:** SOC Level 1
**Category:** Threat Intelligence
**Difficulty:** Easy
**Type:** Walkthrough
**Cost:** Free
**Room Link:** https://tryhackme.com/room/cyberkillchainzmt

---

## What is this room about?

The Cyber Kill Chain is a framework developed by Lockheed Martin that models a cyberattack as a sequence of phases an attacker must complete to achieve their objective. Understanding each phase helps defenders identify where they can intervene and what evidence to look for.

---

## The 7 Phases

| Phase | What the attacker does | Defender's opportunity |
|-------|----------------------|----------------------|
| **1. Reconnaissance** | Research target — OSINT, scanning, social media | Brand monitoring, detecting port scans |
| **2. Weaponisation** | Build malware, create exploit, prepare payload | Threat intel feeds, malware sandbox |
| **3. Delivery** | Phishing email, USB drop, watering hole | Email gateway, web proxy |
| **4. Exploitation** | Execute the exploit on the target | EDR alerts, Sysmon Event ID 1 |
| **5. Installation** | Install backdoor, establish persistence | FIM alerts, new services, registry changes |
| **6. Command & Control** | Maintain comms with the implant | DNS anomalies, outbound connection monitoring |
| **7. Actions on Objectives** | Steal data, encrypt, pivot | DLP alerts, large outbound transfers |

---

## Deep Dive on Each Phase

### Reconnaissance
Two types: **passive** (no contact with target — WHOIS, social media scraping, searching leaked data — nearly impossible to detect) and **active** (direct contact — port scanning, banner grabbing — leaves traces). Tools: **theHarvester** for bulk email/subdomain collection, **Hunter.io** for targeted company intel.

### Weaponisation
Attacker profiles range from script kiddies (buy off-the-shelf malware from darknet) to APTs (write fully custom malware to evade all signatures). Common weapons: malicious Office macros (VBA), infected USB drives, C2 server infrastructure with backdoors, phishing templates.

### Delivery
The most common delivery mechanisms: **spear phishing** (targeted, convincing — uses info gathered in recon), **USB drops** (left in car parks, lobbies), **watering hole attacks** (compromise a website the target visits regularly — inject a drive-by download or fileless malware).

### Installation
Persistence techniques: **web shells** (PHP/ASPX scripts on a compromised server allowing remote command execution), **Run keys** in the Windows registry, **startup folder** entries, **Windows services** modification, **Meterpreter** sessions. **Timestomping** — modifying file timestamps to make malware appear to have always been there — complicates forensic analysis.

### Actions on Objectives
The endgame: credential harvesting, data exfiltration, ransomware deployment (encrypt + delete backups + demand ransom), defacement, or maintaining quiet long-term access (APT style).

---

## The Defender's Advantage

> An attacker must complete **every** phase. A defender only needs to catch them **once**.

Breaking the chain at phases 1-3 is ideal — before any code runs on your network. But breaking it at phase 6 (C2) is still a win — the attacker has access but can't use it. Multiple detection layers mean multiple chances to catch the attack.

In my SOC Home Lab: Suricata catches scanning (Recon), Wazuh FIM catches file drops (Installation), Sigma rules catch C2 patterns. Each layer is independent.

---

## Limitations of the Model

The original Kill Chain assumes a linear, external attack. It doesn't model well:
- **Insider threats** (already past the delivery phase)
- **Attacks that start inside the network** (no perimeter crossing)
- **Multi-stage attacks** that cycle through phases multiple times

The **Unified Kill Chain** and **MITRE ATT&CK** address these gaps.

---

## References

- [Lockheed Martin — Intelligence-Driven Computer Network Defense](https://lockheedmartin.com/content/dam/lockheed-martin/rms/documents/cyber/LM-White-Paper-Intel-Driven-Defense.pdf)
- [MITRE ATT&CK](https://attack.mitre.org/)
