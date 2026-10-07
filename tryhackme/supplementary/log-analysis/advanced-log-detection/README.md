# Advanced Log Detection

**Platform:** TryHackMe
**Path:** Supplementary — advanced Splunk investigation techniques
**Difficulty:** Medium
**Status:** Complete

---

## Overview

Applied log analysis for three real-world attack scenarios using Splunk: web shell deployment via IIS, OWA brute force, and VPN credential attacks via RADIUS/NPS.

---

## IIS Web Shell Investigation

**Step 1 — Identify scanning (burst of 404s from one IP):**
```splunk
index=iis sc_status=404 | stats count by c_ip | sort - count
```

**Step 2 — Find what the IP accessed successfully:**
```splunk
index=iis c_ip=SUSPICIOUS_IP sc_status=200 | stats count by cs_uri_stem | sort - count
```

**Step 3 — Detect web shell execution (w3wp spawning processes):**
```splunk
index=win EventCode=1 ParentImage="*\w3wp.exe"
| table _time, ParentImage, Image, CommandLine | sort _time
```

---

## OWA Brute Force Investigation

OWA returns HTTP 302 for both successful and failed logins. The parameter `reason=2` in the redirect URL identifies a failure — checking the status code alone is insufficient.

```splunk
index=iis cs_uri_stem="/owa/auth.owa" cs_method=POST
| bin _time span=5m | stats count by _time, c_ip
| where count > 10 | sort - count
```

Correlate with Windows Event 4625 (failed logon, Logon_Type=8) to identify the targeted account.

---

## VPN Brute Force (RADIUS/NPS)

| Event ID | Meaning |
|----------|---------|
| 6272 | NPS granted access — VPN auth success |
| 6273 | NPS denied access — VPN auth failure |

Reason Code 16 on Event 6273 = wrong username or password (brute force indicator). Reason codes 48 and 65 are misconfigurations, not attacks.

---

## Key Takeaway

IIS logs reveal what was requested. Sysmon reveals what ran. Neither source alone tells the complete web shell story. Correlation between network-facing logs and host-level process telemetry is essential for web server attack investigation.

---

## References

- [MITRE ATT&CK — T1505.003 Web Shell](https://attack.mitre.org/techniques/T1505/003/)
