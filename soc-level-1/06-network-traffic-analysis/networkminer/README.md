# NetworkMiner

**Platform:** TryHackMe
**Path:** SOC Level 1 — Section 06: Network Traffic Analysis
**Difficulty:** Easy
**Type:** Walkthrough
**Status:** In Progress

---

## Overview

NetworkMiner is a Network Forensic Analysis Tool (NFAT) that automatically extracts useful intelligence from PCAP files — hosts, credentials, files, images, DNS queries — without requiring manual filter construction. It is a first-pass triage tool used before Wireshark deep-dives.

---

## NetworkMiner vs Wireshark

| Capability | NetworkMiner | Wireshark |
|-----------|-------------|-----------|
| OS fingerprinting | Automatic (Satori, p0f) | Manual |
| File extraction | Automatic | Manual |
| Credential extraction | Automatic | Manual |
| Protocol deep-dive | Limited | Full |
| Statistical analysis | Limited | Full |
| First-pass triage | Excellent | Time-consuming |
| Investigation depth | Limited | Comprehensive |

**Workflow:** NetworkMiner first for triage and extraction, Wireshark for detailed investigation.

---

## Tab Reference

| Tab | What You Get |
|-----|-------------|
| Hosts | All detected hosts — IP, MAC, OS fingerprint, hostname, open ports |
| Sessions | All sessions with timestamps, IPs, ports, protocol |
| DNS | All DNS queries and responses |
| Credentials | Automatically extracted credentials — Kerberos, NTLM, FTP, HTTP Basic, SMTP, IMAP |
| Files | All files extracted from traffic with metadata |
| Images | All images extracted — preview with hover |
| Parameters | URL parameters and POST data |
| Keywords | Full-text search across entire capture |
| Anomalies | Auto-detected anomalies (EternalBlue signatures, ARP spoofing) |

---

## Credentials Automatically Extracted

- Kerberos hashes (ready for Hashcat or John the Ripper)
- NTLM hashes
- RDP cookies
- HTTP Basic authentication
- FTP credentials (cleartext)
- SMTP credentials
- IMAP credentials
- MS SQL credentials

---

## Version Differences (1.6 vs 2.7)

| Feature | v1.6 | v2.7 |
|---------|------|------|
| Frame-level detail | Better | Limited |
| Cleartext in single tab | Yes | Split |
| MAC vendor correlation | No | Yes |
| Parameter processing | Limited | Better |

Use v1.6 when needing frame details or consolidated cleartext. Use v2.7 for MAC correlation.

---

## Placeholder

Full notes and additional sections to be added upon room completion.
