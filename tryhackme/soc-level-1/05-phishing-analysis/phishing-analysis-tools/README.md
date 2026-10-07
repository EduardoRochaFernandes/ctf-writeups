# Phishing Analysis Tools

**Platform:** TryHackMe
**Path:** SOC Level 1 — Section 05: Phishing Analysis
**Difficulty:** Easy
**Type:** Walkthrough
**Status:** Complete

---

## Overview

Tools and platforms used in practical phishing analysis. The room covers the analyst toolkit for each phase of investigation — from header parsing to sandbox execution — and introduces PhishTool as an integrated platform.

---

## What to Extract from a Suspicious Email

**From headers:**
- Sender address and display name
- Originating IP (`X-Originating-IP`)
- Reply-To address
- SMTP relay chain (Received headers, read bottom-to-top)
- SPF / DKIM / DMARC authentication results

**From body and attachments:**
- All URLs (raw and expanded)
- Attachment filenames
- Attachment SHA256 hashes

---

## Tool Reference by Phase

### Header Analysis

| Tool | URL | Use |
|------|-----|-----|
| Google Admin Toolbox | toolbox.googleapps.com/apps/messageheader | Parses headers, visualises SMTP routing |
| MXToolbox Header Analyzer | mxtoolbox.com/EmailHeaders.aspx | Authentication results, delivery chain |
| mailheader.org | mailheader.org | Clean, fast header parsing |

### IP and Domain Reputation

| Tool | Use |
|------|-----|
| IPinfo.io | Geolocation, ASN, ISP for originating IP |
| AbuseIPDB | Crowdsourced abuse reports, confidence score (0-100) |
| Talos Intelligence | Cisco's IP/domain reputation (email reputation score) |
| VirusTotal | Aggregates 80+ vendor results for IPs, domains, URLs, files |
| URLScan.io | Sandboxed browser visit — screenshots, DNS, HTTP requests |

### File and Hash Analysis

| Tool | Use |
|------|-----|
| VirusTotal | Submit hash or file — vendor detection rate |
| Talos File Reputation | Hash lookup against Cisco threat intelligence |
| Hybrid Analysis | Free automated sandbox — static and dynamic analysis |
| Any.Run | Interactive sandbox — watch malware execute in real time |
| Joe Security | Advanced sandbox with ATT&CK mapping (paid/free tier) |

### URL Extraction

| Tool | Use |
|------|-----|
| CyberChef "Extract URLs" | Extract all URLs from pasted email content |
| URL2PNG | Screenshot a URL without visiting it |
| URLExpander | Follow redirect chains to find final destination |

---

## PhishTool

PhishTool is an all-in-one phishing analysis platform that aggregates header analysis, IP reputation, URL scanning, and file hashing into a single interface. It has a community edition (free) that can be linked to a VirusTotal API key.

Key features:
- Automatically parses all header fields
- Performs IP reverse DNS lookup
- Extracts and submits attachments for hash lookup
- Classifies phishing type (credential harvesting, malware delivery, BEC)
- Supports case management workflow — classify, note, resolve

---

## Investigation Workflow

```
1. Open raw email source (never click links in the client)
2. Copy headers to header analyser tool
3. Note originating IP — check AbuseIPDB and Talos
4. Extract all URLs with CyberChef
5. Check each URL with URLScan.io (never click directly)
6. Extract and hash attachments
7. Submit hashes to VirusTotal
8. If attachment unknown or low detection: sandbox in Any.Run
9. Document all findings with defanged indicators
10. Classify and report
```

---

## Key Takeaways

URLScan.io is the single most valuable tool for URL investigation. It visits the link in an isolated browser and produces a screenshot, full HTTP request log, and screenshot of the final page — providing everything needed to classify a URL without any risk to the analyst's system. Developing the habit of checking every suspicious URL there before any other investigation step saves time and maintains a consistent evidence trail.

---

## References

- [URLScan.io](https://urlscan.io/)
- [Any.Run](https://any.run/)
- [PhishTool](https://www.phishtool.com/)
- [CyberChef](https://gchq.github.io/CyberChef/)
