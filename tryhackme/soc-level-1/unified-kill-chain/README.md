# Room: Unified Kill Chain

**Platform:** TryHackMe
**Path:** SOC Level 1
**Category:** Threat Intelligence
**Difficulty:** Easy
**Type:** Walkthrough
**Cost:** Free
**Room Link:** https://tryhackme.com/room/unifiedkillchain

---

## What is this room about?

The Unified Kill Chain (UKC) was created by Paul Pols in 2017 (updated 2022) as a more comprehensive and realistic evolution of the Cyber Kill Chain. It defines 18 attack phases grouped into 3 macro-stages, and acknowledges that real attacks are non-linear — attackers loop back, adapt, and cycle through phases multiple times.

---

## The Three Macro-Stages

### Stage 1 — IN (Gaining Initial Foothold)

| Phase | What happens |
|-------|-------------|
| Reconnaissance | OSINT, social media, WHOIS, data leaks |
| Weaponisation | Build C2 infrastructure, payloads, maldocs |
| Delivery | USB, phishing URL, infected server, watering hole |
| Social Engineering | Phishing emails (fear/urgency), deepfakes, fake OAuth |
| Exploitation | Code executes on the target machine |
| Persistence | Backdoors, run keys, modified services |
| Defense Evasion | Code obfuscation, Living-off-the-Land (LotL), log tampering, timestomping, token impersonation |
| Command & Control | HTTP/HTTPS/DNS beaconing — malware phones home constantly |

### Stage 2 — THROUGH (Network Propagation)

| Phase | What happens |
|-------|-------------|
| Pivoting | Compromised host used as a jump point to reach internal systems |
| Discovery | Internal recon — active user accounts, network topology, installed software, browser history |
| Privilege Escalation | From user → local admin → domain admin → SYSTEM |
| Execution | Run the malicious code across the environment |
| Credential Access | Keylogging, browser credential extraction, LSASS dumping |
| Lateral Movement | Jump between systems using valid credentials |

### Stage 3 — OUT (Action on Objectives)

| Phase | What happens |
|-------|-------------|
| Collection | Data from drives, email, audio/video recording |
| Exfiltration | Extract data via encrypted channels, cloud storage (OneDrive/Dropbox), slow exfil over days/weeks |
| Impact | Ransomware, disk wipe, DoS, defacement |
| Objectives | The strategic goal — financial, espionage, hacktivism, sabotage, silent persistence |

---

## Why the UKC Matters More Than the Original Kill Chain

The original Kill Chain implies a single attacker going through 7 phases linearly. Reality is messier:
- Attackers **cycle** — they may fail at Exploitation and try Delivery again differently
- Internal threats start at Stage 2 directly
- APTs stay in Stage 2 for months before reaching Stage 3

The UKC maps much better to **MITRE ATT&CK** — ATT&CK gives you the individual techniques, and the UKC tells you *where in the attack* those techniques fit.

---

## Practical Application for SOC Work

When you see a **Privilege Escalation** alert, the UKC tells you: the attacker is already in Stage 2. That means:
- They already have a foothold — look backwards in your SIEM for the initial compromise
- Check for persistence mechanisms that might have already been established
- Investigate lateral movement — other hosts may already be compromised

> The UKC changed how I approach alert triage. A single alert is never just that one event — it's a window into a larger attack chain.

---

## References

- [Unified Kill Chain — official site](https://www.unifiedkillchain.com/)
- [Paul Pols — original thesis (PDF)](https://www.unifiedkillchain.com/assets/The-Unified-Kill-Chain.pdf)
- [MITRE ATT&CK Navigator](https://mitre-attack.github.io/attack-navigator/)
