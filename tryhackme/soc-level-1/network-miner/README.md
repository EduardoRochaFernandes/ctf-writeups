# Room: Network Miner

**Platform:** TryHackMe
**Path:** SOC Level 1
**Category:** Network Security
**Difficulty:** Easy
**Type:** Walkthrough
**Cost:** Free
**Room Link:** https://tryhackme.com/room/networkminer

---

## What is this room about?

NetworkMiner is a Network Forensic Analysis Tool (NFAT) that extracts useful intelligence from PCAP files automatically — hosts, credentials, files, images, DNS queries — without requiring manual Wireshark filters. It's the fastest way to get an overview of a PCAP before drilling into details.

---

## NetworkMiner vs Wireshark

These tools are **complementary**, not competing:

| | NetworkMiner | Wireshark |
|--|-------------|-----------|
| Best for | Quick overview, automatic extraction | Deep investigation, custom filters |
| OS fingerprinting | ✅ Automatic | ❌ |
| File extraction | ✅ Automatic | ✅ Manual only |
| Credential extraction | ✅ Automatic | ✅ Manual |
| Protocol filtering | Limited | Full |
| Statistical analysis | Limited | Full |
| Beaconing detection | ❌ | ✅ |

**Workflow:** NetworkMiner first for triage → Wireshark for investigation.

---

## Modes of Operation

- **Sniffer Mode** — live capture (Windows only, unreliable — use Wireshark for live capture)
- **Packet Parsing Mode** — load an existing PCAP and extract everything automatically (this is where NetworkMiner shines)

---

## Tab Reference

| Tab | What you get |
|-----|-------------|
| **Hosts** | All hosts detected — IP, MAC, OS fingerprint, hostname, sessions, ports |
| **Sessions** | All network sessions with timestamps, IPs, ports, protocol |
| **DNS** | All DNS queries and responses with TTL, timestamps |
| **Credentials** | Automatically extracted credentials — Kerberos hashes, NTLM, FTP, SMTP, HTTP, IMAP |
| **Files** | All files extracted from the traffic with full metadata |
| **Images** | All images extracted — hover for details |
| **Parameters** | URL parameters and POST data |
| **Keywords** | Full-text search across the entire capture |
| **Messages** | Emails and chat messages |
| **Anomalies** | Auto-detected anomalies — EternalBlue signatures, ARP spoofing |

---

## Credentials Extracted Automatically

NetworkMiner pulls these without any manual effort:
- Kerberos hashes
- NTLM hashes
- RDP cookies
- HTTP Basic Auth credentials
- FTP username/password (cleartext)
- SMTP credentials
- IMAP credentials
- MS SQL credentials

To crack extracted NTLM/Kerberos hashes: **Hashcat** or **John the Ripper**.

---

## Version Differences (1.6 vs 2.7)

| Feature | v1.6 | v2.7 |
|---------|------|------|
| Frame-level detail | ✅ Better | Limited |
| Cleartext all in one tab | ✅ | Split across tabs |
| MAC address vendor correlation | ❌ | ✅ |
| Parameter processing | Limited | ✅ Better |

**Rule:** Need frame details or cleartext in one tab → use v1.6. Need MAC correlation or more parameter processing → use v2.7.

---

## Pros and Cons

**Pros:**
- OS fingerprinting via Satori and p0f
- Automatic credential and file extraction
- Fast initial overview of any PCAP
- No filter knowledge required for basics

**Cons:**
- Poor scalability with large PCAPs
- Limited filtering capability
- No protocol deep-dive
- Not useful as a primary live capture tool

---

## Key Takeaways

> NetworkMiner turns the first 5 minutes of a PCAP investigation from "what is even in here?" to a structured overview of every host, file, and credential in the traffic.

The Credentials tab alone makes NetworkMiner worth having in your toolkit. Seeing Kerberos and NTLM hashes appear automatically from a PCAP — ready to copy into Hashcat — is a reminder of how much sensitive information flows in plaintext or weakly-protected protocols on real networks.

---

## References

- [NetworkMiner Official Site](https://www.netresec.com/?page=NetworkMiner)
- [MITRE ATT&CK — T1040 Network Sniffing](https://attack.mitre.org/techniques/T1040/)
