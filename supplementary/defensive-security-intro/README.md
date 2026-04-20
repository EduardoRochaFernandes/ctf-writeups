# Defensive Security Intro

**Platform:** TryHackMe
**Path:** Supplementary — completed to build foundational context
**Difficulty:** Easy
**Status:** Complete

---

## Overview

A broad introduction to defensive security: what it is, who does it, and what the SOC's day-to-day looks like. This room was completed to establish foundational context before starting the SOC Level 1 path.

---

## Key Concepts

**Blue team objectives:** Prevention (stop attacks before they happen) and detection and response (catch and contain attacks in progress).

**Core defensive activities:** asset management, patch management, user awareness training, threat intelligence, log collection and monitoring.

**DFIR (Digital Forensics and Incident Response):** when the SOC detects a breach, DFIR takes over for deep investigation and remediation. Incident response phases: Preparation, Detection and Analysis, Containment/Eradication/Recovery, Post-Incident Activity.

**Malware types:** Virus (spreads by attaching to programs), Trojan Horse (appears legitimate, hides malicious function), Ransomware (encrypts files, demands payment for decryption key).

**Practical SIEM exercise:** Analysed a suspicious login alert in a simulated SIEM at a fictional bank. Steps: identify source IP, check reputation via threat intelligence tool (confirmed malicious), escalate to SOC lead, block IP via firewall rule. Flag: `THM{THREAT-BLOCKED}`.

---

## References

- [MITRE ATT&CK](https://attack.mitre.org/)
