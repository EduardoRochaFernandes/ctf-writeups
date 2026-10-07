# Detecting Web Attacks

**Platform:** TryHackMe
**Path:** SOC Level 1 — Section 08: Web Security Monitoring
**Difficulty:** Easy
**Type:** Walkthrough
**Status:** Complete

---

## Overview

Hands-on detection of web application attacks in access logs and SIEM — SQL injection, XSS, command injection, path traversal, and brute force. The room uses both command-line log analysis and Splunk queries.

---

## SQL Injection Detection

SQL injection occurs when user input is incorporated into a database query without sanitisation. Detection focuses on identifying SQL syntax in HTTP request parameters.

**Command-line detection:**
```bash
grep -iE "union|select|insert|drop|--|%27|sleep\(|waitfor delay" access.log

# Extract IPs making SQL injection attempts
grep -iE "union.*select|select.*from" access.log | cut -d' ' -f1 | sort | uniq -c | sort -rn
```

**Splunk:**
```splunk
index=web_logs
| search uri_path="*union*" OR uri_path="*select*" OR uri_path="*--*" OR uri_path="*%27*"
| table _time, src_ip, uri_path, status
| sort _time
```

**Common payload patterns:**
- `' OR '1'='1` — authentication bypass
- `UNION SELECT null,username,password FROM users--` — data extraction
- `'; WAITFOR DELAY '0:0:5'--` — time-based blind SQLi
- `%27`, `%3D`, `%20` — URL-encoded SQL metacharacters

---

## XSS Detection

Cross-site scripting attacks inject HTML/JavaScript into web pages viewed by other users.

```bash
grep -iE "<script|javascript:|onerror=|onload=|alert\(|%3Cscript" access.log

# URL-encoded XSS
grep -iE "%3Cscript|%22.*%3E|%27.*%3E" access.log
```

---

## Command Injection Detection

Attackers attempt to execute OS commands through web application inputs:

```bash
grep -iE ";.*(whoami|id|ls|cat|uname)|%7C.*(id|whoami)|&&.*ls" access.log

# Common payloads targeting Linux
grep -iE "; cat /etc/passwd|; id; |; whoami;" access.log
```

---

## Path Traversal Detection

Attackers attempt to access files outside the web root:

```bash
grep -iE "\.\./|%2E%2E%2F|%252E%252E|etc/passwd|win.ini|boot.ini" access.log

# Double URL-encoding bypass
grep -iE "%252E%252E|%255c" access.log
```

---

## Brute Force Detection

High volume of authentication failures from a single source:

```bash
# Count 401 responses per IP
awk '$9 == 401 {print $1}' access.log | sort | uniq -c | sort -rn | head -10

# Find IPs that succeeded after many failures
awk '$9 == 401 {fail[$1]++} $9 == 200 && fail[$1] > 5 {print $1, "succeeded after", fail[$1], "failures"}' access.log
```

**Splunk:**
```splunk
index=web_logs uri_path="/login" status=401
| bin _time span=1m
| stats count by _time, src_ip
| where count > 10
| sort - count
```

---

## Web Scanner Detection

Automated scanners generate characteristic patterns:

```bash
# Known scanner User-Agents
grep -iE "nikto|sqlmap|burpsuite|dirbuster|gobuster|nmap|masscan|openvas" access.log

# Directory enumeration: rapid 404 sequence from same IP
awk '$9 == 404 {print $1}' access.log | sort | uniq -c | sort -rn | head -5
```

---

## Key Takeaways

Automated attack tools are far easier to detect than skilled manual attackers. SQLMap, Nikto, and directory busters generate patterns of User-Agent strings, request rates, and 404 sequences that no human produces. The harder detection problem is the patient, low-volume manual attacker who spaces requests over hours and uses legitimate-looking User-Agents. Anomaly-based detection and baseline deviation analysis address these more sophisticated cases.
