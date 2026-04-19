# Room: Advanced Log Detection

**Platform:** TryHackMe
**Path:** SOC Level 1
**Category:** Log Analysis
**Difficulty:** Medium
**Type:** Walkthrough
**Cost:** Premium
**Room Link:** https://tryhackme.com/room/advancedlogdetection

---

## What is this room about?

Applied log analysis for three real-world attack scenarios: web shell deployment via IIS, brute force against Exchange OWA (Outlook Web Access), and credential attacks against VPN via RADIUS/NPS. All investigated using Splunk with real log data.

---

## Part 1 — IIS and Web Shell Detection

### IIS Log Fields

| Field | Meaning |
|-------|---------|
| `c-ip` | Client IP — potential attacker |
| `cs-uri-stem` | URI path requested |
| `cs-uri-query` | Query string — commands passed to web shells |
| `cs-method` | HTTP method |
| `sc-status` | Response code |
| `cs(User-Agent)` | Browser/tool identifier |

**All IIS timestamps are UTC regardless of server timezone.**

### Splunk Investigation Workflow

**Step 1 — Find scanning (bursts of 404 from one IP):**
```splunk
index=iis sc_status=404
| stats count by c_ip
| sort - count
```

**Step 2 — Find successful responses from suspicious IP:**
```splunk
index=iis c_ip=SUSPICIOUS_IP sc_status=200
| stats count by cs_uri_stem
| sort - count
```

The `/aspnet_client/` directory is critical: IIS creates it for ASP.NET client-side scripts. It should never contain application code. Web shells in this directory are a HAFNIUM signature.

**Step 3 — Find web shell execution (w3wp spawning processes):**
```splunk
index=win EventCode=1 ParentImage="*\w3wp.exe"
| table _time, ParentImage, CommandLine
| sort _time
```

**Step 4 — Find when the shell was dropped (Sysmon Event ID 11 — FileCreate):**
```splunk
index=win EventCode=11 TargetFilename="*shell.aspx"
| table _time, Image, TargetFilename
```

---

## Part 2 — OWA Brute Force Detection

Exchange OWA login behaviour in logs:
- **Successful login:** POST to `/owa/auth.owa` → HTTP 302 to `/owa/inbox`
- **Failed login:** POST to `/owa/auth.owa` → HTTP 302 back to `/owa/auth.owa?reason=2`

Both succeed and fail return HTTP 302 — you cannot distinguish them by status code alone. The `reason=2` parameter in the redirect URL identifies failure.

**Step 1 — Find brute force pattern:**
```splunk
index=iis cs_uri_stem="/owa/auth.owa" cs_method=POST
| bin _time span=5m
| stats count by _time, c_ip
| where count > 10
| sort - count
```

**Step 2 — Identify targeted account (Windows Event 4625):**
```splunk
index=win EventCode=4625
| stats count by user, Logon_Type
| sort - count
```
Logon_Type 8 (NetworkCleartext) = how IIS authenticates against AD.

**Step 3 — Correlate with Security logs:**
```splunk
index=win EventCode IN (4624, 4625) user="TARGETED_USER" Logon_Type=8
| table _time, EventCode, user, Process_Name
| sort _time
```
A cluster of 4625 followed by 4624 = brute force succeeded.

**Step 4 — Check post-authentication activity:**
```splunk
index=iis c_ip="ATTACKER_IP"
| stats count by cs_uri_stem
| sort - count
```
Access to `/ecp` (Exchange Control Panel) after OWA login = privilege escalation attempt.

---

## Part 3 — VPN Brute Force via RADIUS/NPS

Authentication flow: `User → VPN Gateway → RADIUS (NPS) → Active Directory`

NPS Event IDs (in Windows Security log on NPS server):

| Event ID | Meaning |
|----------|---------|
| **6272** | NPS granted access (VPN auth success) |
| **6273** | NPS denied access (VPN auth failure) |

**Event 6273 Reason Codes:**
| Code | Meaning |
|------|---------|
| 16 | Wrong username or password — brute force indicator |
| 48 | Account not permitted for VPN — misconfiguration, not attack |
| 65 | RADIUS secret mismatch — misconfiguration |

**Step 1 — Identify attack scope:**
```splunk
index=win EventCode=6273
| stats count by User_Account_Name, Client_IP_Address
| sort - count
```

**Step 2 — Confirm if attacker succeeded:**
```splunk
index=win EventCode IN (6273,6272) User_Account_Name=COMPROMISED_USER
| table _time, EventCode, User_Account_Name
```

**Step 3 — Check AD logon events:**
```splunk
index=win EventCode IN (4624, 4625) user=COMPROMISED_USER
| table _time, host, EventCode, Logon_Type
| sort _time
```

---

## Key Takeaways

> IIS logs tell you what was requested. Sysmon tells you what happened as a result. You need both to reconstruct a web shell attack.

The most important insight from this room: the OWA login page returns HTTP 302 for both success and failure. Relying on status codes alone would make this attack invisible. The `reason=2` parameter in the redirect URL is the actual indicator — a reminder that understanding application behaviour is as important as log analysis technique.

---

## References

- [MITRE ATT&CK — T1505.003 Web Shell](https://attack.mitre.org/techniques/T1505/003/)
- [HAFNIUM Exchange Server Compromise — Microsoft](https://www.microsoft.com/security/blog/2021/03/02/hafnium-targeting-exchange-servers/)
- [Akira Ransomware — CISA Advisory](https://www.cisa.gov/news-events/cybersecurity-advisories/aa24-109a)
