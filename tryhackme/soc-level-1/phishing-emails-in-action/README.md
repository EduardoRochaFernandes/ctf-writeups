# Room: Phishing Emails in Action

**Platform:** TryHackMe
**Path:** SOC Level 1
**Category:** Phishing Analysis
**Difficulty:** Easy
**Type:** Walkthrough
**Cost:** Free
**Room Link:** https://tryhackme.com/room/phishingemails3tryoe

---

## What is this room about?

This room puts you in front of real phishing email samples and walks through the analysis of each one. Six different case studies, each with a different attack technique — building pattern recognition that you can't get from reading theory.

---

## Case Studies

### Case 1 — Fake PayPal (URL Shortener)
A convincing PayPal-branded email with a "confirm your account" link. The URL is shortened with bit.ly — hiding the real destination.

**Lesson:** Always expand shortened URLs before analysing. Tools like urlexpander.com or the URL preview in URLScan.io reveal the true destination. Never judge a URL by its display text.

### Case 2 — Fake Shipping Notification (Tracking Pixel)
An email claiming to be from a courier, with a legitimate-looking tracking number. No malicious link — but opening the email sends the victim's IP address back to the attacker via a 1×1 invisible image.

**Lesson:** Email clients disable images by default for exactly this reason. A tracking pixel confirms the email address is active and reveals your IP — useful for targeted follow-up attacks. In the raw email source, look for `<img src="http://attacker.com/track.gif" width="1" height="1">`.

### Case 3 — Fake OneDrive (Credential Harvesting)
A Microsoft-branded email with a "View Document" link. Multiple redirects lead to a pixel-perfect OneDrive login page hosted on a compromised domain. Even if the victim types wrong credentials, the page captures them.

**Lesson:** Always check the URL *before* entering credentials. The domain in the address bar is the truth — branding and logos are meaningless. The attacker controls the page content.

### Case 4 — Fake Netflix (Malicious PDF)
A "your payment failed" email with a PDF attachment. The PDF contains a clickable link to a phishing page — not a malicious script, which helps it bypass email gateway scanning.

**Lesson:** PDFs can be as dangerous as executables. Before opening any attachment, hash it and check VirusTotal. URLScan.io can analyse the URL embedded in the PDF.

### Case 5 — Fake Apple (BCC Targeting + .DOT Template)
The victim was added in BCC, not the To field — a technique to make the email harder to detect and analyse (no obvious targeted user in headers). The attachment is a `.DOT` file (Word template) — less recognised as dangerous than `.docm` or `.xlsm`.

**Lesson:** Check the BCC field in raw headers. Unusual attachment extensions (`.dot`, `.xlt`, `.xlam`) are often more dangerous precisely because they're less recognised.

### Case 6 — Fake DHL (Excel Macro)
No URL in the body at all — the entire attack vector is an Excel file with auto-executing VBA macros. When the user opens the file and enables content, the macro runs immediately.

**Lesson:** Macros should be disabled by default across the entire organisation via Group Policy. `EnableContent` is one of the most dangerous buttons a user can click. In the email, look for vague urgency ("see attached invoice") that provides no reason to question the source.

---

## Indicators to Extract from Every Phishing Email

```
Sender: name, email address, domain
Reply-To: (if different from sender)
Subject line
Originating IP
URLs: raw + expanded
Attachment names + SHA256 hashes
Redirect chain (if URL redirects)
Final landing page URL
```

---

## Key Takeaways

> Real phishing campaigns don't rely on technical sophistication — they rely on creating enough pressure and legitimacy that the victim acts before thinking.

Six case studies teach you something textbooks can't: pattern recognition. After seeing enough samples, you start noticing when something's slightly wrong before you even know exactly what it is. That intuition becomes instinct over time.

---

## References

- [MITRE ATT&CK — T1566.001 Spearphishing Attachment](https://attack.mitre.org/techniques/T1566/001/)
- [PhishTank — Real phishing URL database](https://www.phishtank.com/)
