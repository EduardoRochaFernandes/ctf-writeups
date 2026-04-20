# Pyramid of Pain

**Platform:** TryHackMe
**Path:** SOC Level 1 — Section 04: Cyber Defence Frameworks
**Difficulty:** Easy
**Type:** Walkthrough
**Status:** Complete

---

## Overview

The Pyramid of Pain, created by David Bianco in 2013, is a threat intelligence model that describes different categories of indicators of compromise and quantifies how much difficulty blocking each category imposes on an attacker. The model reframes detection strategy from "what can we block?" to "what costs the attacker the most to replace?"

---

## The Six Levels

```
        [TTPs]             Maximum pain — attacker must retool entirely
       [Tools]             High pain — requires new software or framework
    [Network Artifacts]    Moderate — attacker must adapt C2 patterns
    [Host Artifacts]       Moderate — attacker must redesign dropper behaviour
    [Domain Names]         Low-moderate — requires new domain registration
    [IP Addresses]         Low — changed in seconds
    [Hash Values]          Trivial — one byte change = new hash
```

---

## Level 1 — Hash Values (Trivial)

A hash is a fixed-length fingerprint produced by a mathematical function applied to a file. Common algorithms:
- **MD5** — 128-bit output, not collision-resistant, avoid for security applications
- **SHA-1** — 160-bit output, legacy, deprecated
- **SHA-256** — 256-bit output, current standard for file identification

EDR and antivirus platforms use hashes to identify known malware. The limitation is severe: modifying a single byte in a file — adding a space, changing a string — produces an entirely different hash. Attackers rebuild their tools routinely for exactly this reason.

**Fuzzy hashing** (SSDeep, TLSH) addresses this partially by generating hashes based on file structure rather than exact content, detecting near-identical files even after minor modifications. SSDeep generates a signature that can be compared against other signatures with a similarity score.

---

## Level 2 — IP Addresses (Easy)

Blocking individual IP addresses is among the most common defensive measures and among the least effective against a prepared attacker. Techniques attackers use to rotate IPs:

- **Fast Flux DNS** — a domain rotates through hundreds of IP addresses within minutes, all pointing to compromised hosts acting as proxies. The real C2 server is hidden behind this constantly changing facade.
- **Bulletproof hosting** — providers in permissive jurisdictions that resist takedown requests
- **Residential proxies** — traffic routed through legitimate home ISP connections

An IP block buys minutes to hours of protection at most.

---

## Level 3 — Domain Names (Annoying)

Domain registration requires some investment of time and, in some cases, identity verification or money. Attackers use several techniques to complicate detection:

- **Punycode / homograph attacks** — Unicode characters that visually resemble standard ASCII (`wlndows.com` with an uppercase i instead of lowercase L, `аpple.com` with Cyrillic 'а')
- **URL shorteners** — services like bit.ly or TinyURL hide the real destination. Always expand shortened URLs before investigation.
- **Lookalike domains** — `microsoft-support.com`, `paypa1.com`, `amazon.account-verify.net`

Tools for detection: Any.Run sandbox (shows DNS requests made by malware), VirusTotal passive DNS, urlscan.io.

---

## Level 4 — Host Artifacts (Annoying)

The traces an attacker leaves inside a compromised system, tied to the specific tools and techniques used:

- **Registry keys** — persistence mechanisms such as Run keys, service registrations
- **Suspicious process relationships** — Word spawning PowerShell, cmd.exe spawning from an unusual parent
- **Dropped files** — payloads, staging files, tools deployed on the host
- **Attack pattern signatures** — specific sequences of actions that are characteristic of a tool or technique

Changing host artifacts requires the attacker to redesign their dropper and post-exploitation behaviour, not just swap an IP or recompile a binary.

---

## Level 5 — Network Artifacts (Annoying)

Patterns in network traffic tied to specific tools or C2 frameworks:

- **User-Agent strings** — many implants use hardcoded User-Agent strings that appear in HTTP requests. Detection: TShark filter `tshark -Y http.request -T fields -e http.user_agent -r capture.pcap`
- **Beaconing intervals** — C2 check-ins at regular intervals create distinctive IO Graph patterns in Wireshark or Kibana
- **URI patterns** — specific path structures, parameter names, or encoding schemes used by C2 frameworks
- **JA3 fingerprints** — TLS client fingerprints that can identify specific tools even over encrypted traffic

---

## Level 6 — Tools (Painful)

Detecting and blocking the attacker's actual tools — Mimikatz, Cobalt Strike, Metasploit, custom RATs. At this level, the attacker must invest in new tooling, which costs time and money.

Detection approaches:
- **YARA rules** — pattern matching rules that identify specific strings, byte sequences, or structural characteristics within files, even across variants
- **AV/EDR signatures** — vendor detection of known tool signatures
- **Behavioural patterns** — identifying what tools do, not just what they are (e.g., any process reading LSASS memory with certain access flags)

Resources: MalwareBazaar (malware samples), Malshare (shared malware repository), SOC Prime Threat Detection Marketplace (community detection rules).

---

## Level 7 — TTPs (Maximum Pain)

Tactics, Techniques, and Procedures — the how and why of an adversary's operations:
- **Tactics** — the goal of each phase (credential access, lateral movement, exfiltration)
- **Techniques** — the method used to achieve the tactic (Pass-the-Hash for lateral movement)
- **Procedures** — the specific implementation (using Mimikatz's sekurlsa::pth against domain admin)

All TTPs are documented in the MITRE ATT&CK framework. An attacker can change an IP in seconds and a domain in hours, but changing their TTPs requires retraining, retooling, and rethinking the entire attack methodology. Many threat actors abandon a target rather than invest in this level of change.

**Practical example — Pass-the-Hash detection:**
If the SOC can detect Pass-the-Hash attempts via Windows Event Log monitoring (Event ID 4624 with Logon Type 9 and unusual source), the attacker loses their lateral movement capability without being able to simply swap an indicator. They must either abandon the technique or accept the detection risk.

---

## Key Takeaways

Every Sigma rule and detection rule in a well-engineered SOC should map to a MITRE ATT&CK technique — not to a specific hash or IP. A rule that detects "PowerShell downloading and executing a script" will catch an attacker regardless of the specific malware variant. A hash blocklist will not survive the attacker's next recompile.

---

## References

- [David Bianco — Pyramid of Pain (original)](http://detect-respond.blogspot.com/2013/03/the-pyramid-of-pain.html)
- [MITRE ATT&CK](https://attack.mitre.org/)
- [SSDeep fuzzy hashing](https://ssdeep-project.github.io/ssdeep/)
- [MalwareBazaar](https://bazaar.abuse.ch/)
