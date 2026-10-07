# CTF Writeups and Study Notes

[![CI](https://github.com/EduardoRochaFernandes/ctf-writeups/actions/workflows/ci.yml/badge.svg)](https://github.com/EduardoRochaFernandes/ctf-writeups/actions/workflows/ci.yml)
[![License: CC BY 4.0](https://img.shields.io/badge/text-CC%20BY%204.0-lightgrey.svg)](LICENSE)
[![Code: MIT](https://img.shields.io/badge/code-MIT-blue.svg)](scripts/LICENSE)

Blue-team study notes and writeups from the TryHackMe SOC Level 1 path and related rooms, completed during the first year of my degree. Each note maps the room to SOC work: what to look for, which log source or tool shows it, and how it relates to MITRE ATT&CK or OWASP where that genuinely applies.

## Why this exists

I am a cybersecurity student aiming at security architecture in regulated finance. These notes are my record of building SOC fundamentals (triage, phishing analysis, network and web detection, Windows logging) and a reference I use when building detections in my [SOC home lab](https://github.com/EduardoRochaFernandes/soc-home-lab). Most entries are concept-focused study notes rather than lab transcripts.

## How to browse

There is nothing to install: open the index tables below and click a room. Every note follows the same header (platform, path, difficulty, type, status). New writeups should start from [`templates/writeup-template.md`](templates/writeup-template.md) (objective, data sources, analysis, detection and remediation ideas, ATT&CK/OWASP mapping, lessons learned).

To run the repository checks locally (redaction, metadata and index consistency):

```bash
python scripts/check_writeups.py
```

## Index: TryHackMe SOC Level 1 (33 of 67 rooms documented)

| Room | Category | Difficulty | Type | Skills / tools demonstrated | ATT&CK / OWASP | Status |
|---|---|---|---|---|---|---|
| [Blue Team Introduction](tryhackme/soc-level-1/01-blue-team-introduction/blue-team-introduction/README.md) | Blue Team Introduction | Easy | Walkthrough | Blue team structure, SOC hierarchy, MSSPs | — | Complete |
| [Humans as Attack Vectors](tryhackme/soc-level-1/01-blue-team-introduction/humans-as-attack-vectors/README.md) | Blue Team Introduction | Easy | Walkthrough | Social engineering, phishing, deepfakes, insider threat | T1566, T1598 | Complete |
| [Junior Security Analyst Intro](tryhackme/soc-level-1/01-blue-team-introduction/junior-security-analyst-intro/README.md) | Blue Team Introduction | Easy | Walkthrough | L1 analyst role, alert lifecycle, SIEM/EDR/threat-intel toolchain | — | Complete |
| [SOC Role in Blue Team](tryhackme/soc-level-1/01-blue-team-introduction/soc-role-in-blue-team/README.md) | Blue Team Introduction | Easy | Walkthrough | SOC models, blue team roles, career progression | — | Complete |
| [Systems as Attack Vectors](tryhackme/soc-level-1/01-blue-team-introduction/systems-as-attack-vectors/README.md) | Blue Team Introduction | Easy | Walkthrough | System attack categories from a SOC perspective | T1190, T1195 | Complete |
| [Introduction to Phishing](tryhackme/soc-level-1/02-soc-team-internals/introduction-to-phishing/README.md) | SOC Team Internals | Easy | Walkthrough | Email anatomy, SPF/DKIM/DMARC, defanging | T1566 | Complete |
| [SOC L1 Alert Reporting](tryhackme/soc-level-1/02-soc-team-internals/soc-l1-alert-reporting/README.md) | SOC Team Internals | Easy | Walkthrough | Alert reports, escalation criteria | — | Complete |
| [SOC L1 Alert Triage](tryhackme/soc-level-1/02-soc-team-internals/soc-l1-alert-triage/README.md) | SOC Team Internals | Easy | Walkthrough | Event-to-alert pipeline, queue prioritisation, triage process | — | Complete |
| [SOC Metrics and Objectives](tryhackme/soc-level-1/02-soc-team-internals/soc-metrics-and-objectives/README.md) | SOC Team Internals | Easy | Walkthrough | SOC performance metrics and SLAs | — | Complete |
| [SOC Workbooks and Lookups](tryhackme/soc-level-1/02-soc-team-internals/soc-workbooks-and-lookups/README.md) | SOC Team Internals | Easy | Walkthrough | Identity/asset inventories, network diagrams, workbooks | — | Complete |
| [Introduction to EDR](tryhackme/soc-level-1/03-core-soc-solutions/introduction-to-edr/README.md) | Core SOC Solutions | Easy | Walkthrough | EDR telemetry, EDR vs antivirus, limitations | T1055, T1059 | Complete |
| [Introduction to SIEM](tryhackme/soc-level-1/03-core-soc-solutions/introduction-to-siem/README.md) | Core SOC Solutions | Easy | Walkthrough | Log sources, Windows Event IDs, ingestion, detection rules; Splunk/Elastic/Sentinel concepts | — | Complete |
| [Cyber Kill Chain](tryhackme/soc-level-1/04-cyber-defence-frameworks/cyber-kill-chain/README.md) | Cyber Defence Frameworks | Easy | Walkthrough | Lockheed Martin kill chain, defender actions per phase | — | Complete |
| [Eviction](tryhackme/soc-level-1/04-cyber-defence-frameworks/eviction/README.md) | Cyber Defence Frameworks | Easy | Walkthrough | Unified Kill Chain mapping, detection source per phase, Sysmon | T1566.001, T1204.002, T1059.005, T1547.001, T1071.001, T1550.002, T1048.002 | Complete |
| [MITRE](tryhackme/soc-level-1/04-cyber-defence-frameworks/mitre/README.md) | Cyber Defence Frameworks | Medium | Walkthrough | ATT&CK, CAR, D3FEND, Sigma/Splunk detection analytics | T1003.001, T1059.001, T1110 | Complete |
| [Pyramid of Pain](tryhackme/soc-level-1/04-cyber-defence-frameworks/pyramid-of-pain/README.md) | Cyber Defence Frameworks | Easy | Walkthrough | IOC value model; YARA, TShark, VirusTotal, urlscan | — | Complete |
| [Summit](tryhackme/soc-level-1/04-cyber-defence-frameworks/summit/README.md) | Cyber Defence Frameworks | Easy | Challenge | Applying the Pyramid of Pain to build durable detections | — | Complete |
| [Unified Kill Chain](tryhackme/soc-level-1/04-cyber-defence-frameworks/unified-kill-chain/README.md) | Cyber Defence Frameworks | Easy | Walkthrough | UKC stages, alert triage with attack-chain thinking | — | Complete |
| [Phishing Analysis Fundamentals](tryhackme/soc-level-1/05-phishing-analysis/phishing-analysis-fundamentals/README.md) | Phishing Analysis | Easy | Walkthrough | Header analysis, defanging, CyberChef, URLScan, Any.Run, VirusTotal | T1566 | Complete |
| [Phishing Analysis Tools](tryhackme/soc-level-1/05-phishing-analysis/phishing-analysis-tools/README.md) | Phishing Analysis | Easy | Walkthrough | PhishTool, header analysers, reputation lookups, sandboxing | — | Complete |
| [Phishing Emails in Action](tryhackme/soc-level-1/05-phishing-analysis/phishing-emails-in-action/README.md) | Phishing Analysis | Easy | Walkthrough | Six phishing case studies: shorteners, tracking pixels, credential harvesting, macros | T1566.001, T1566.002 | Complete |
| [Phishing Prevention](tryhackme/soc-level-1/05-phishing-analysis/phishing-prevention/README.md) | Phishing Analysis | Easy | Walkthrough | SPF, DKIM, DMARC, S/MIME, secure email gateways | T1566 | Complete |
| [The Greenholt Phish](tryhackme/soc-level-1/05-phishing-analysis/the-greenholt-phish/README.md) | Phishing Analysis | Easy | Challenge | Phishing investigation workflow and report template | T1566 | Complete |
| [Network Traffic Basics](tryhackme/soc-level-1/06-network-traffic-analysis/network-traffic-basics/README.md) | Network Traffic Analysis | Easy | Walkthrough | Traffic flows, capture methods, NetFlow/IPFIX; Wireshark, Zeek, Suricata | T1040 | Complete |
| [NetworkMiner](tryhackme/soc-level-1/06-network-traffic-analysis/networkminer/README.md) | Network Traffic Analysis | Easy | Walkthrough | PCAP artefact extraction with NetworkMiner (in progress) | — | In Progress |
| [Wireshark: Packet Operations](tryhackme/soc-level-1/06-network-traffic-analysis/wireshark-packet-operations/README.md) | Network Traffic Analysis | Easy | Walkthrough | Display filters; port scan, ARP, DHCP, DNS, HTTP, FTP analysis | T1046, T1557 | Complete |
| [Wireshark: The Basics](tryhackme/soc-level-1/06-network-traffic-analysis/wireshark-the-basics/README.md) | Network Traffic Analysis | Easy | Walkthrough | Wireshark interface, capture vs display filters, streams (in progress) | — | In Progress |
| [Wireshark: Traffic Analysis](tryhackme/soc-level-1/06-network-traffic-analysis/wireshark-traffic-analysis/README.md) | Network Traffic Analysis | Medium | Walkthrough | TLS, SSL stripping, ICMP tunnelling, Log4Shell, beaconing, exfiltration in Wireshark | T1572, CVE-2021-44228 | Complete |
| [Man-in-the-Middle Detection](tryhackme/soc-level-1/07-network-security-monitoring/man-in-the-middle-detection/README.md) | Network Security Monitoring | Easy | Walkthrough | Wireshark detection of ARP poisoning, SSL stripping, DNS spoofing | T1557, T1557.002 | Complete |
| [Detecting Web Attacks](tryhackme/soc-level-1/08-web-security-monitoring/detecting-web-attacks/README.md) | Web Security Monitoring | Easy | Walkthrough | Splunk/log detection of SQLi, XSS, command injection, traversal, brute force, scanners | OWASP A01/A03:2021; T1110 | Complete |
| [Detecting Web DDoS](tryhackme/soc-level-1/08-web-security-monitoring/detecting-web-ddos/README.md) | Web Security Monitoring | Easy | Walkthrough | Access-log and Splunk detection of application-layer DoS | T1499 | Complete |
| [Detecting Web Shells](tryhackme/soc-level-1/08-web-security-monitoring/detecting-web-shells/README.md) | Web Security Monitoring | Easy | Walkthrough | Web shell detection with IIS logs, Sysmon, Splunk | T1505.003 | Complete |
| [Web Security Essentials](tryhackme/soc-level-1/08-web-security-monitoring/web-security-essentials/README.md) | Web Security Monitoring | Easy | Walkthrough | HTTPS/TLS, sessions, XSS, CSRF, CSP | OWASP A03:2021 (XSS); CWE-352 (CSRF) | Complete |

## Index: TryHackMe supplementary rooms (21 rooms)

Rooms completed outside the main path to reinforce foundations (logging, Windows internals, web basics).

| Room | Category | Difficulty | Type | Skills / tools demonstrated | ATT&CK / OWASP | Status |
|---|---|---|---|---|---|---|
| [Careers in Cyber](tryhackme/supplementary/foundations/careers-in-cyber/README.md) | Foundations | — | — | Cyber career landscape and certifications | — | Complete |
| [Defensive Security Intro](tryhackme/supplementary/foundations/defensive-security-intro/README.md) | Foundations | Easy | — | Blue team objectives, DFIR phases, simulated SIEM alert | — | Complete |
| [Offensive Security Intro](tryhackme/supplementary/foundations/offensive-security-intro/README.md) | Foundations | Easy | — | Directory brute-forcing with Gobuster and how it shows in logs | T1083 | Complete |
| [Advanced Log Detection](tryhackme/supplementary/log-analysis/advanced-log-detection/README.md) | Log Analysis | Medium | — | Splunk: IIS web shell, OWA and VPN (RADIUS/NPS) brute force | T1505.003, T1110 | Complete |
| [Intro to Log Analysis](tryhackme/supplementary/log-analysis/intro-to-log-analysis/README.md) | Log Analysis | — | — | Command-line log analysis (cut/sort/uniq/grep), attack patterns in logs | — | Complete |
| [Intro to Logs](tryhackme/supplementary/log-analysis/intro-to-logs/README.md) | Log Analysis | — | — | Log sources, formats, storage tiers, parsing/correlation pipeline | — | Complete |
| [Log Operations](tryhackme/supplementary/log-analysis/log-operations/README.md) | Log Analysis | — | — | Windows Event IDs, Linux log locations, CLI tooling | — | Complete |
| [Log Universe](tryhackme/supplementary/log-analysis/log-universe/README.md) | Log Analysis | — | — | Web, auth, Windows and network log sources | — | Complete |
| [Logless Hunt](tryhackme/supplementary/log-analysis/logless-hunt/README.md) | Log Analysis | — | — | Investigating after Security log clearing: Sysmon, PowerShell history, Prefetch | T1070.001 | Complete |
| [Carnage](tryhackme/supplementary/network-forensics/carnage/README.md) | Network Forensics | — | — | PCAP forensics in Wireshark: macro delivery, C2, exfiltration | T1204.002, T1048.003 | Complete |
| [HTTP in Detail](tryhackme/supplementary/web/http-in-detail/README.md) | Web | Easy | — | HTTP methods, status-code patterns, security headers, cookie flags | — | Complete |
| [Web Application Basics](tryhackme/supplementary/web/web-application-basics/README.md) | Web | — | — | Client-server model, URL structure, response headers | — | Complete |
| [Web Application Security](tryhackme/supplementary/web/web-application-security/README.md) | Web | — | — | OWASP Top 10 in practice: SQLi, IDOR, authentication failures | OWASP A01, A03, A07:2021 | Complete |
| [Core Windows Processes](tryhackme/supplementary/windows/core-windows-processes/README.md) | Windows | Easy | — | Normal Windows process tree, masquerading, lsass.exe monitoring | T1036, T1003.001 | Complete |
| [Evading Logging and Monitoring](tryhackme/supplementary/windows/evading-logging-and-monitoring/README.md) | Windows | Medium | — | ETW architecture, log clearing, ETW patching, Script Block Logging | T1562.006, T1070.001 | Complete |
| [Windows Basics](tryhackme/supplementary/windows/windows-basics/README.md) | Windows | — | — | Windows filesystem, key directories, analyst CMD commands, ADS | T1564.004 | Complete |
| [Windows CLI Basics](tryhackme/supplementary/windows/windows-cli-basics/README.md) | Windows | — | — | PowerShell for analysts: connections, event logs, scheduled tasks, Run keys | — | Complete |
| [Windows Fundamentals 1](tryhackme/supplementary/windows/windows-fundamentals-1/README.md) | Windows | — | — | NTFS, alternate data streams, UAC, accounts | T1564.004 | Complete |
| [Windows Fundamentals 2](tryhackme/supplementary/windows/windows-fundamentals-2/README.md) | Windows | — | — | MSConfig, Resource Monitor, registry Run keys | T1547.001 | Complete |
| [Windows Fundamentals 3](tryhackme/supplementary/windows/windows-fundamentals-3/README.md) | Windows | — | — | Defender events, BitLocker, Volume Shadow Copy | T1490 | Complete |
| [Windows Internals](tryhackme/supplementary/windows/windows-internals/README.md) | Windows | — | — | Processes/threads, process injection, Sysmon Event IDs 8/10 | T1055 | Complete |

## Status and roadmap

- **SOC Level 1:** 34 of the 67 rooms are not yet documented here: Splunk, Elastic Stack and SOAR basics (section 03); Phishing Unfolding and Snapped Phish-ing Line (05); Network Security Essentials, Network Discovery Detection, Data Exfiltration Detection, IDS Fundamentals and Snort (07); sections 09 to 13 (Windows and Linux monitoring, malware concepts, threat intelligence, SIEM triage); and the section 14 capstones (Boogeyman 1 to 3, Tempest). Two documented rooms (NetworkMiner, Wireshark: The Basics) are marked In Progress.
- **SOC Level 2 and 3:** planned, not started.
- **Blue Team Labs Online:** planned; no BTLO writeups yet.

## Repository layout

```text
.
├── tryhackme/
│   ├── soc-level-1/<NN-section>/<room>/README.md
│   └── supplementary/<category>/<room>/README.md
├── templates/writeup-template.md   # structure for new writeups
├── scripts/check_writeups.py       # flag redaction, metadata and index checks (run by CI)
└── .github/                        # CI workflow, issue and PR templates
```

## Content policy

Platforms ask users not to publish flags, answers or paid walkthrough material, so this repository does not include them. Notes explain concepts, methods and detection ideas; flags and final answers are redacted (`THM{REDACTED}`, `[redacted]`). If you spot a spoiler, please open an issue (see [SECURITY.md](SECURITY.md)).

## Related projects

- [soc-home-lab](https://github.com/EduardoRochaFernandes/soc-home-lab): a SOC home lab built on local virtual machines (Wazuh, Elasticsearch, Kibana, Suricata, TheHive, MISP) with detection rules, Sigma coverage and runbooks.

## License

Text and notes: [CC BY 4.0](LICENSE). Code in `scripts/`: [MIT](scripts/LICENSE). Copyright 2026 Eduardo Fernandes.

Author: [@EduardoRochaFernandes](https://github.com/EduardoRochaFernandes)
