# Room: The Greenholt Phish

**Platform:** TryHackMe
**Path:** SOC Level 1
**Category:** Phishing Analysis
**Difficulty:** Easy
**Type:** Challenge
**Cost:** Premium
**Room Link:** https://tryhackme.com/room/thegreenholtphish

---

## What is this room about?

Practical phishing analysis challenge. You receive a suspicious email and must fully analyse it using all the tools and techniques from the phishing analysis series.

---

## Investigation Workflow

### Step 1 — Header Analysis

Extract from raw email source:
- Sender display name vs actual email (do they match?)
- `X-Originating-IP` — real sending IP
- `Reply-To` — different from From = major red flag
- `Received` headers — read bottom to top for real origin
- Authentication results — SPF/DKIM/DMARC pass or fail?

### Step 2 — IP and Domain Reputation

- Originating IP: AbuseIPDB, Talos Intelligence
- Sender domain: VirusTotal
- URLs found: URLScan.io (never click the link yourself)

### Step 3 — Attachment Analysis

```bash
sha256sum attachment    # Get the hash
```
Submit hash to VirusTotal. If unknown: Any.Run or Hybrid Analysis sandbox.

### Step 4 — Document Findings

```
Time of activity: [email timestamp]
Sender: [display name] <[email address]>
Originating IP: [IP] — [reputation result]
SPF/DKIM/DMARC: [pass/fail]
Attachment: [filename] — SHA256: [hash] — VT: [X/Y vendors]
URLs: [defanged URLs]
Verdict: True Positive
Recommended action: Block sender domain, quarantine hash in EDR
```

---

## Defanging URLs Before Sharing

Always defang before putting in reports or chat:
```
http://evil.example.com  ->  hxxp[://]evil[.]example[.]com
```

CyberChef does this automatically with the "Defang URL" recipe.

---

## Key Takeaways

> A phishing analysis is only as good as its documentation. If you found the smoking gun but didn't document it clearly, the L2 analyst who picks up your case starts from scratch.

---

## References

- [PhishTool](https://www.phishtool.com/)
- [URLScan.io](https://urlscan.io/)
- [CyberChef](https://gchq.github.io/CyberChef/)
