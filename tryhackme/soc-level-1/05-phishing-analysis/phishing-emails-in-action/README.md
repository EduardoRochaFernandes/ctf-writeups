# Phishing Emails in Action

**Platform:** TryHackMe
**Path:** SOC Level 1 — Section 05: Phishing Analysis
**Difficulty:** Easy
**Type:** Walkthrough
**Status:** Complete

---

## Overview

Six real phishing email samples analysed in detail. Each case study presents a different attack technique, building pattern recognition that theoretical study cannot develop. The objective is to identify what makes each email dangerous and what indicator is most actionable.

---

## Case Study Analysis

### Case 1 — Fake PayPal (URL Shortener Concealment)

A spoofed PayPal email with a "verify your account" call to action. The link uses a URL shortener, hiding the true destination.

**Key technique:** URL shorteners prevent reputation checks and make visual inspection meaningless. The destination could be a credential harvester, a malware download, or a redirect chain.

**Analysis action:** Extract the URL, expand it through urlexpander.com or URLScan.io (which follows redirects in a sandboxed browser), and check the final destination.

**Indicator:** Shortened URL in an unsolicited account verification email. The combination of urgency ("your account will be limited"), spoofed sender, and obfuscated destination is a complete phishing profile.

---

### Case 2 — Fake Shipping Notification (Tracking Pixel)

An email appearing to be from a courier company, with a legitimate tracking number. No malicious link, no attachment. Yet still dangerous.

**Key technique:** A 1x1 pixel transparent image embedded in the HTML body. The image is hosted on the attacker's server. When the email client renders the HTML, it fetches the image — sending the victim's IP address, email client, and confirmation that the email was opened to the attacker.

**Analysis action:** Examine the raw HTML source. Look for `<img>` tags with `width="1" height="1"` or unusual external domains hosting images. Note: this is why email clients default to blocking remote image loading.

**Indicator:** External image from an unrelated domain. Legitimate courier emails do not need to load images from random hosting providers.

---

### Case 3 — Fake OneDrive (Credential Harvesting)

A Microsoft-branded email with a "view shared document" link. Multiple HTTP redirects lead to a pixel-perfect OneDrive login page hosted on a compromised domain.

**Key technique:** Credential harvesting — the page collects whatever credentials the victim enters, including incorrect ones, before passing them to Microsoft's actual login. The victim sees a login failure and tries their actual password, which is also captured.

**Analysis action:** Use URLScan.io to follow the redirect chain without clicking. Check the final URL domain — if it is not `microsoft.com` or `live.com`, it is fraudulent regardless of how the page looks.

**Critical lesson:** Visual design means nothing. The browser address bar domain is the only reliable indicator.

---

### Case 4 — Fake Netflix (Malicious PDF Attachment)

A "payment failed" email from Netflix with a PDF attachment. The PDF contains a link rather than a script, allowing it to bypass email gateways that scan for executable content.

**Key technique:** PDF as a link delivery vehicle. PDFs can contain clickable links, JavaScript, and executable content. They are treated as documents by users but require the same scrutiny as executables.

**Analysis action:** Hash the PDF and check VirusTotal. If clean or low detection, submit to a sandbox. Any.Run will open the PDF and show what URLs it tries to load.

---

### Case 5 — Fake Apple (BCC + Uncommon File Type)

The victim was placed in BCC, not the To field. The attachment is a `.DOT` file — a Word document template. Less scrutinised than `.docm` or `.xlsm`.

**Key technique:** BCC placement means the victim's address does not appear in the message headers visible to the email gateway's standard inspection. The attachment extension is chosen specifically because it is less commonly blocked.

**Analysis action:** When examining raw headers, look for your address in the BCC field rather than To or CC. Treat `.DOT`, `.XLT`, `.OTT`, `.POTM`, and similar template extensions with the same caution as macro-enabled documents.

---

### Case 6 — Fake DHL (Excel Macro — No Links)

No URLs anywhere in the email. The entire attack surface is a single `.xlsm` Excel file with a VBA macro that executes automatically when the user enables content.

**Key technique:** Auto-executing macro. The "Enable Content" button in Office applications executes the VBA code immediately. The file typically displays a convincing document — invoice, tracking sheet — while the macro runs silently in the background.

**Analysis action:** Hash and submit to sandbox. In Any.Run, disable network connection and watch what processes the macro spawns. Look for PowerShell execution, network connections, or file drops.

**Organisational control:** Macros should be disabled organisation-wide via Group Policy (`HKCU\Software\Policies\Microsoft\Office\16.0\Excel\Security\VBAWarnings = 4`). "Enable Content" should never be clicked.

---

## Indicators to Extract from Every Phishing Email

```
Sender display name and email address
Reply-To address (if different from From)
Originating IP (X-Originating-IP or bottom Received header)
SPF / DKIM / DMARC result
Subject line
All URLs (defanged)
Redirect chain if applicable
Final landing page URL
All attachment filenames
Attachment SHA256 hashes
VirusTotal detection results
```

---

## Key Takeaways

Real phishing campaigns do not rely on technical sophistication — they rely on creating just enough pressure and visual credibility that the victim acts before examining the details. After reviewing enough samples, the pattern recognition that makes anomalies visible becomes instinctive: something about the sender domain looks wrong, the redirect chain is too long, the urgency is disproportionate. This instinct is developed through volume of practice, not theory.

---

## References

- [MITRE ATT&CK — T1566.001 Spearphishing Attachment](https://attack.mitre.org/techniques/T1566/001/)
- [MITRE ATT&CK — T1566.002 Spearphishing Link](https://attack.mitre.org/techniques/T1566/002/)
