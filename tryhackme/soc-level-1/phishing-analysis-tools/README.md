# Room: Phishing Analysis Tools

**Platform:** TryHackMe
**Path:** SOC Level 1
**Category:** Phishing Analysis
**Difficulty:** Easy
**Type:** Walkthrough
**Cost:** Premium
**Room Link:** https://tryhackme.com/room/phishingemails2rytmuv

---

## What is this room about?

Knowing the theory of phishing is one thing. This room gives you the practical toolkit — the specific tools analysts use to pull apart a suspicious email and determine whether it's malicious.

---

## What to Collect from a Suspicious Email

**From the headers:**
- Sender address and display name (are they different?)
- Originating IP address (`X-Originating-IP`)
- Reply-To address (does it match From?)
- SMTP hop chain (`Received` headers — read bottom to top for true origin)
- Authentication results (SPF/DKIM/DMARC pass/fail)

**From the body and attachments:**
- URLs (expand all shortened links)
- Attachment names and SHA256 hashes
- Any embedded images (potential tracking pixels)

---

## The Analyst's Toolkit

### Header Analysis
| Tool | URL | Use |
|------|-----|-----|
| Google Messageheader Analyser | Via Google Workspace toolbox | Parse SMTP routing and authentication |
| MXToolbox Header Analyser | mxtoolbox.com/EmailHeaders.aspx | Visual header breakdown |
| mailheader.org | mailheader.org | Simple, clean header parsing |

### IP and Domain Reputation
| Tool | URL | Use |
|------|-----|-----|
| IPinfo.io | ipinfo.io | Geolocation and ASN info |
| Talos Intelligence | talosintelligence.com | IP/domain reputation (Cisco's threat intel) |
| URLScan.io | urlscan.io | Visits the URL safely and screenshots it — **never click the link yourself** |
| VirusTotal | virustotal.com | Check URL, IP, or domain against 80+ security vendors |

### File and Hash Analysis
| Tool | URL | Use |
|------|-----|-----|
| VirusTotal | virustotal.com | Submit file or SHA256 hash |
| Talos File Reputation | talosintelligence.com/talos_file_reputation | Hash lookup |
| Hybrid Analysis | hybrid-analysis.com | Free sandbox analysis |
| Any.Run | any.run | **Interactive sandbox** — watch the malware execute in real time |
| Joe Security | joesecurity.org | Advanced sandbox with MITRE ATT&CK mapping |

### All-in-One
**PhishTool** (phishtool.com) — aggregates header analysis, IP reputation, URL scanning, and file hashing in a single interface. Has a community edition you can connect to your VirusTotal API key.

---

## Workflow for a Suspicious Email

```
1. Open the raw email source (never click links)
2. Copy headers → paste into header analyser
3. Note the originating IP → check reputation (IPinfo, Talos)
4. Extract all URLs → URLScan.io for each
5. Extract attachment → hash it → check VirusTotal
6. If still unclear → run in sandbox (Any.Run, Hybrid Analysis)
7. Document all findings
8. Classify and report
```

---

## Key Takeaways

> URLScan.io is your best friend. It visits the suspicious link in an isolated browser and takes a screenshot — you see exactly what the victim would see without putting your machine at risk.

The combination of PhishTool + VirusTotal + URLScan.io handles 90% of phishing investigations. Any.Run is the tool to reach for when you have an attachment you need to understand in depth — watching malware execute and seeing its process tree, network connections, and registry changes in real time is one of the most educational things you can do as a new analyst.

---

## References

- [URLScan.io](https://urlscan.io/)
- [Any.Run](https://any.run/)
- [PhishTool](https://www.phishtool.com/)
- [Talos Intelligence](https://talosintelligence.com/)
