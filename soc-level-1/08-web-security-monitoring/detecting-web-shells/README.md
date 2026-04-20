# Detecting Web Shells

**Platform:** TryHackMe
**Path:** SOC Level 1 — Section 08: Web Security Monitoring
**Difficulty:** Easy
**Type:** Walkthrough
**Status:** Complete

---

## Overview

Web shells are malicious scripts uploaded to compromised web servers that provide the attacker with remote command execution through a browser. This room covers how web shells work, where they hide, how to find them in file system scans and access logs, and how to investigate them using Splunk with IIS logs.

---

## What a Web Shell Is

A web shell is a script — typically PHP, ASP, ASPX, or JSP — placed on a web server by an attacker. When accessed via a URL, it executes operating system commands and returns the output.

**Minimal PHP example:**
```php
<?php if(isset($_GET['cmd'])){ echo shell_exec($_GET['cmd']); } ?>
```

Accessed as: `http://target.com/uploads/shell.php?cmd=whoami`

**Why web shells are effective for persistence:**
- Survive reboots (file on disk)
- Communicate over standard HTTP/HTTPS ports
- Blend with legitimate web traffic
- Require only web access — no separate C2 infrastructure

---

## Requirements for Deployment

An attacker needs one of:
- A file upload vulnerability (web application accepts executable files)
- Write access to web directories via another vulnerability
- Compromised server credentials

**Common vulnerable upload patterns:** profile picture uploads without type validation, document management systems without server-side extension checking, admin panels with misconfigured file handling.

---

## Where to Look

**Web root directories by platform:**
| Server | Default web root |
|--------|-----------------|
| Apache | `/var/www/html/` |
| Nginx | `/usr/share/nginx/html/` |
| IIS | `C:\inetpub\wwwroot\` |
| IIS aspnet_client | `C:\inetpub\wwwroot\aspnet_client\` |

High-risk subdirectories:
- `/uploads/`, `/images/`, `/temp/`, `/admin/`, `/assets/`
- `/aspnet_client/` — IIS creates this directory for ASP.NET client scripts. It should never contain application code. HAFNIUM (March 2021) dropped web shells here across tens of thousands of Exchange Servers.

**File system scan:**
```bash
# Find PHP files modified in the last 7 days in web root
find /var/www/html -name "*.php" -newer /var/www/html/index.php -type f

# Find PHP files containing dangerous functions
grep -r "shell_exec\|exec\|system\|passthru\|eval" /var/www/html --include="*.php" -l

# Find files with double extensions
find /var/www/html -name "*.jpg.php" -o -name "*.png.asp"
```

---

## Log-Based Detection

**Access log patterns:**
```bash
# POST requests to PHP files in upload directories
grep '"POST.*uploads.*\.php' access.log

# Unusual User-Agents (web shells often use curl or custom agents)
grep -iE "curl/0|python-requests|go-http-client" access.log | grep "200"

# Mix of responses suggesting reconnaissance phase
# (many 404, then 200 on found shell)
```

**Wireshark:**
```
http.request.method == "POST" and http.request.uri contains ".php"
http.user_agent contains "curl"
```

---

## Splunk Investigation — IIS Web Shells

**Step 1 — Find scanning (burst of 404s from single IP):**
```splunk
index=iis sc_status=404
| stats count by c_ip
| sort - count
| head 10
```

**Step 2 — Find successful responses from suspicious IP:**
```splunk
index=iis c_ip=SUSPICIOUS_IP sc_status=200
| stats count by cs_uri_stem
| sort - count
```

The `/aspnet_client/` path in results is a critical indicator — this directory should not serve application requests.

**Step 3 — Detect web shell execution (w3wp spawning processes):**
```splunk
index=win EventCode=1 ParentImage="*\\w3wp.exe"
| table _time, ParentImage, Image, CommandLine
| sort _time
```

`w3wp.exe` is the IIS worker process. In a clean environment it never spawns `cmd.exe`, `powershell.exe`, or other shells. When it does, a web shell is in use.

**Step 4 — Timestamp the deployment:**
```splunk
index=win EventCode=11 TargetFilename="*aspnet_client*"
| table _time, Image, TargetFilename
```

---

## Notable Real-World Cases

**HAFNIUM — March 2021:** Exploited four Exchange Server zero-days (ProxyLogon). Deployed China Chopper web shells in `C:\inetpub\wwwroot\aspnet_client\`. Affected approximately 250,000 Exchange Servers globally. Shells were used for credential harvesting and persistent access.

---

## Key Takeaways

`w3wp.exe` spawning PowerShell is not normal. It is not a false positive candidate. It is a web shell executing commands. The combination of IIS access logs showing unusual POST requests to unexpected paths, and Sysmon Event ID 1 showing `w3wp.exe` as a parent process, provides the complete detection picture — neither source alone is sufficient.
