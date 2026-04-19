# Room: Detecting Web Shells

**Platform:** TryHackMe
**Path:** SOC Level 1
**Category:** Web Security
**Difficulty:** Easy
**Type:** Walkthrough
**Cost:** Premium
**Room Link:** https://tryhackme.com/room/detectingwebshells

---

## What is this room about?

Web shells are one of the most common persistence mechanisms after initial web server compromise. This room covers what web shells are, how they work, how to detect them in logs and on the file system, and how to investigate them in Splunk using IIS logs.

---

## What is a Web Shell?

A web shell is a malicious script (typically `.php`, `.aspx`, `.jsp`) uploaded to a compromised web server that gives the attacker remote command execution through a browser.

**Two purposes:**
1. **Initial access** — exploit a file upload vulnerability to get onto the server
2. **Persistence** — maintain access long-term, survive reboots, require only a web browser

**Requirements:** The attacker needs either a file upload vulnerability, a server misconfiguration, or prior access.

---

## How Web Shells Work (PHP Example)

```php
<?php
if(isset($_GET['cmd'])) {
    $cmd = $_GET['cmd'];
    echo shell_exec($cmd);
}
?>
```

The attacker visits `http://target.com/uploads/shell.php?cmd=whoami` and the server executes `whoami` and returns the output. Functions commonly abused: `shell_exec()`, `exec()`, `system()`, `passthru()`.

---

## Where to Find Web Shells

Default web root directories to check:
- Apache: `/var/www/html/`
- Nginx: `/usr/share/nginx/html/`
- IIS: `C:\inetpub\wwwroot\`

High-risk subdirectories:
- `/uploads/`, `/images/`, `/temp/`, `/admin/`
- `/aspnet_client/` (IIS — should never contain application code)

---

## File System Detection

```bash
# Find PHP files modified in July 2025
find /var/www -type f -name "*.php" -newerct "2025-07-01" ! -newerct "2025-08-01"

# Search for dangerous PHP functions in files
grep -r "eval(" wp-content/
grep -r "shell_exec(" /var/www/html/
```

**Suspicious file indicators:**
- Random-looking filenames
- Executable extensions in upload directories (`.php`, `.jsp`, `.aspx`)
- Double extensions to bypass validation (`image.jpg.php`)
- Files in directories that should only contain static content

---

## Log-Based Detection

**In Apache/Nginx access logs:**
```bash
# POST requests to PHP files in upload directories
grep '"POST.*uploads.*\.php' access.log

# Unusual user agents (web shells often use curl or no agent)
grep "curl/0" access.log

# Mix of 200 and 404/500 responses from same IP (testing phase)
grep "SUSPICIOUS_IP" access.log | awk '{print $9}' | sort | uniq -c
```

**In Wireshark:**
```
http.request.method == "POST"           # Upload attempt
http.request.uri contains ".php"        # PHP file access
http.user_agent                         # Check for unusual agents
```

---

## Advanced Detection with Splunk (IIS Logs)

**Step 1 — Find scanning (burst of 404s from one IP):**
```splunk
index=iis sc_status=404
| stats count by c_ip
| sort - count
```

**Step 2 — Find successful requests from suspicious IP:**
```splunk
index=iis c_ip=SUSPICIOUS_IP sc_status=200
| stats count by cs_uri_stem
| sort - count
```

**Step 3 — Find web shell activity (w3wp spawning child processes):**
```splunk
index=win EventCode=1 ParentImage="*\w3wp.exe"
| table _time, ParentImage, CommandLine
| sort _time
```

`w3wp.exe` is the IIS worker process. In a clean environment it should never spawn `cmd.exe`, `powershell.exe`, or other shells. When it does, you have a web shell.

**Step 4 — Find when the shell was deployed:**
```splunk
index=win EventCode=11 TargetFilename="*shell.aspx"
| table _time, Image, TargetFilename
```

---

## Real-World Examples

- **HAFNIUM (March 2021):** Exploited four Exchange Server zero-days (ProxyLogon) and deployed China Chopper web shells in `C:\inetpub\wwwrootspnet_client\` on tens of thousands of Exchange servers globally.
- **CISA 2023:** Reported `.aspx` web shells on US government IIS servers via a Telerik UI vulnerability.

---

## Key Takeaways

> `w3wp.exe` spawning PowerShell is not normal. It is always worth investigating.

The combination of IIS access logs (to see what was requested) and Sysmon Event ID 1 (to see what processes ran) gives a complete picture of web shell activity. Neither source alone tells the full story.

---

## References

- [MITRE ATT&CK — T1505.003 Web Shell](https://attack.mitre.org/techniques/T1505/003/)
- [CISA — Web Shells](https://www.cisa.gov/sites/default/files/publications/AA21-310A-Iranian-APT-Actors.pdf)
