# The Greenholt Phish

**Platform:** TryHackMe
**Path:** SOC Level 1 — Section 05: Phishing Analysis
**Difficulty:** Easy
**Type:** Challenge
**Status:** Complete

---

## Overview

A practical phishing analysis challenge. An employee has forwarded a suspicious email to the security team. Using all tools and techniques from the phishing analysis series, the task is to fully investigate the email and document findings in a structured report.

---

## Investigation Process

### Step 1 — Header Analysis

Open the raw email source and extract:
- Sender display name and actual email address — do they match?
- `X-Originating-IP` — the real sending IP
- `Reply-To` — does it differ from From?
- `Received` chain — trace path from origin to destination (read bottom-to-top)
- `Authentication-Results` — SPF / DKIM / DMARC outcomes

### Step 2 — IP and Domain Enrichment

Run the originating IP through AbuseIPDB and Talos Intelligence. Note:
- Abuse confidence score (0-100)
- Geolocation and ISP
- Whether the IP is a known malicious sender or part of a shared hosting environment

Run the sender domain through VirusTotal — check DNS records, historical data, community comments.

### Step 3 — URL Investigation

Extract all URLs from the email body using CyberChef. For each URL:
- Submit to URLScan.io
- Review the screenshot and HTTP request chain
- Check the final destination domain for legitimacy

### Step 4 — Attachment Analysis

If attachment present:
- Calculate SHA256 hash (`sha256sum filename`)
- Submit to VirusTotal
- If detection rate is low or zero: submit to Any.Run sandbox

### Step 5 — Report

```
Time of activity: [email timestamp]
Sender: [display name] <[email address]>
Originating IP: [IP] — Abuse Score: [X/100] — Geolocation: [country, ISP]
SPF/DKIM/DMARC: [pass/fail/none]
Reply-To: [if different from From, note here]
Attachment: [filename] — SHA256: [hash] — VT: [X/Y vendors]
URLs found: [defanged URLs]
Verdict: True Positive — [brief justification]
Recommended action: [block sender domain / quarantine hash / user notification]
```

---

## Key Takeaways

A complete phishing investigation requires documenting the full chain of evidence: where the email originated, what authentication checks it failed, what it was trying to deliver, and what the recipient would have encountered if they had clicked. Partial documentation creates gaps that require re-investigation later. The habit of following the full checklist on every investigation, even when an indicator is obviously malicious early in the process, is what separates reliable analysts from fast but inconsistent ones.

---

## References

- [PhishTool](https://www.phishtool.com/)
- [AbuseIPDB](https://www.abuseipdb.com/)
- [URLScan.io](https://urlscan.io/)
