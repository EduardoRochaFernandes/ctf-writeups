# Offensive Security Intro

**Platform:** TryHackMe
**Path:** Supplementary — completed to understand attacker perspective
**Difficulty:** Easy
**Status:** Complete

---

## Overview

A brief introduction to offensive security and why blue teamers benefit from understanding it. Includes a hands-on exercise using Gobuster to discover hidden directories on a fictional bank website.

---

## Key Concepts

**Gobuster** — directory and file brute-force tool:
```bash
gobuster dir -u http://fakebank.thm -w /usr/share/wordlists/dirb/common.txt
```
Tests directory names from a wordlist, identifying paths that exist but are not publicly linked.

**Security through obscurity** — hiding a resource (such as an admin panel) rather than securing it. Gobuster trivially defeats this — if a path exists, it will be found.

**SOC application:** Directory scanning appears in access logs as rapid 404 sequences from a single IP, often with known scanner User-Agent strings (`gobuster/`, `DirBuster`). A burst of 404 responses from the same source within seconds is the key detection indicator.

---

## References

- [MITRE ATT&CK — T1083 File and Directory Discovery](https://attack.mitre.org/techniques/T1083/)
