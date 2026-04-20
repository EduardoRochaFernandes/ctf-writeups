# Snapped Phish-ing Line

**Platform:** TryHackMe
**Path:** SOC Level 1 — Section 05: Phishing Analysis
**Difficulty:** Medium
**Type:** Challenge
**Status:** Pending

---

## Overview

An advanced phishing analysis challenge. The scenario: multiple employees at SwiftSpend Financial have received suspicious emails and some have already submitted credentials. The task is to investigate a set of `.eml` files, analyse a phishing kit retrieved from the attacker's infrastructure, and extract threat intelligence about the campaign.

This room applies phishing analysis, CTI tooling, and basic command-line techniques to reconstruct a complete phishing campaign.

---

## Topics Covered

- Analysing `.eml` files using a Linux VM (Thunderbird, command line)
- Extracting and decoding Base64-encoded HTML attachments
- Identifying redirect URLs and defanging them with CyberChef
- Downloading and analysing a phishing kit (ZIP archive with PHP, HTML)
- Reading PHP source code to find data collection mechanisms
- Using `grep` to extract email addresses and credential destinations from a phishing kit
- CTI enrichment of the adversary infrastructure

---

## Key Commands

```bash
# Find .eml with PDF attachment
grep -rl "application/pdf" phish-emails/

# Extract embedded HTML content
cat email.eml | grep -A5 "Content-Transfer-Encoding: base64" | base64 -d

# Search phishing kit for credential submission endpoint
grep -r "send\|mail\|submit" Update365/ --include="*.php"

# Find email addresses in PHP files
grep -oE "[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}" Update365/
```

---

## Placeholder

Full writeup to be added upon room completion.
