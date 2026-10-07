# Phishing Analysis Fundamentals

**Platform:** TryHackMe
**Path:** SOC Level 1 — Section 05: Phishing Analysis
**Difficulty:** Easy
**Type:** Walkthrough
**Status:** Complete

---

## Overview

The first dedicated phishing analysis room. It covers the technical components of a phishing email investigation — how to extract headers, identify the originating IP, analyse attachments, and determine the intent of a suspicious message.

---

## Investigation Methodology

Every phishing investigation follows a consistent order:

1. Obtain the raw email source (not just what the email client displays)
2. Extract and analyse headers
3. Identify and enrich the originating IP
4. Extract all URLs and expand shortened links
5. Extract and hash any attachments
6. Check reputation of all extracted indicators
7. Classify and report

---

## Header Analysis

The email headers tell the story of how the message travelled from sender to recipient. Key fields:

**From** — displays the sender name and address. Can be freely forged. Do not trust at face value.

**Reply-To** — where replies are directed. If different from From, this is a strong indicator of a Business Email Compromise (BEC) setup: the attacker spoofs a legitimate From address but redirects responses to their own inbox.

**X-Originating-IP** — the real IP address that injected the email into the SMTP infrastructure. This is harder to forge than From and is the primary indicator of sender location.

**Received** headers — a chain added by every SMTP server that handled the message. Reading from bottom to top gives the true delivery path from origin to destination.

**Authentication-Results** — the receiving server's evaluation of SPF, DKIM, and DMARC. A failing result does not guarantee malice (legitimate forwarded email often fails SPF), but a passing result does not guarantee legitimacy either (attackers can register domains with valid SPF/DKIM).

**Header analysis tools:** Google Admin Toolbox Messageheader, MXToolbox Header Analyzer, mailheader.org.

---

## Defanging Indicators

Before sharing any suspicious URL or email address in documentation, reports, or chat, defang it to prevent accidental clicks:

```
Original:   http://evil.example.com/payload
Defanged:   hxxp[://]evil[.]example[.]com/payload

Original:   phisher@malicious.org
Defanged:   phisher[@]malicious[.]org
```

CyberChef automates this with the "Defang URL" recipe.

---

## IP and Domain Reputation

Once the originating IP is identified:
- **IPinfo.io** — geolocation, ISP, ASN
- **AbuseIPDB** — historical abuse reports with confidence score
- **Talos Intelligence** — Cisco's reputation system for IPs and domains
- **VirusTotal** — aggregates results from 80+ security vendors

---

## Attachment Analysis

1. Do not open the attachment on your analysis machine
2. Extract the SHA256 hash: `sha256sum filename`
3. Submit the hash to VirusTotal — check vendor detection rate
4. If unknown or borderline: submit to Any.Run (interactive sandbox) or Hybrid Analysis
5. Note: PDFs, Office documents (.docx, .xlsx, .xlsm), and HTML files can all be malicious

---

## URL Analysis

**URLScan.io** — submits the URL to a sandboxed browser session, takes a screenshot, captures DNS queries and HTTP requests. View exactly what the victim would see without any risk.

**CyberChef "Extract URLs"** — extracts all URLs from pasted email content.

Always expand shortened URLs (bit.ly, TinyURL, etc.) before investigation. Never click a suspicious URL from your analysis machine.

---

## Phishing Attack Case Studies

**Case 1 — URL Shortener:** Email contains a bit.ly link. Always expand and check the actual destination.

**Case 2 — Tracking Pixel:** 1x1 transparent image in HTML body. Loading it confirms the email was opened and sends the victim's IP to the attacker. Email clients block remote images by default for this reason.

**Case 3 — Credential Harvesting Page:** Multi-redirect chain ending at a pixel-perfect login page. Even incorrect credentials are captured. Always verify the URL domain before entering any credentials.

**Case 4 — Malicious PDF:** PDF contains an embedded link to a phishing page. PDFs require the same scrutiny as executable files.

**Case 5 — BCC Targeting:** Victim added to BCC instead of To — makes the email harder to find in investigations. Attachment is a .DOT Word template, less commonly recognised as dangerous than .docm.

**Case 6 — Macro-Only:** No links in the body. Single vector is a .xlsm file with auto-executing VBA macros. Macros should be disabled org-wide via Group Policy.

---

## Key Takeaways

The Reply-To mismatch is the most frequently missed phishing indicator. Always check whether Reply-To matches the From address. In BEC attacks, a single Reply-To check is the difference between catching and missing the attack entirely.

---

## References

- [MITRE ATT&CK — T1566 Phishing](https://attack.mitre.org/techniques/T1566/)
- [CyberChef](https://gchq.github.io/CyberChef/)
- [URLScan.io](https://urlscan.io/)
- [Any.Run](https://any.run/)
