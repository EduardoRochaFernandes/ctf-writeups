# Room: Detecting Web Attacks

**Platform:** TryHackMe
**Path:** SOC Level 1
**Category:** Web Security
**Difficulty:** Easy
**Type:** Walkthrough
**Cost:** Free
**Room Link:** https://tryhackme.com/room/detectingwebattacks

---

## What is this room about?

Hands-on detection of web application attacks in log files and SIEM — SQL injection, XSS, command injection, directory traversal, and brute force.

---

## SQL Injection Detection

```bash
grep -iE "union|select|insert|drop|--|%27|sleep\(|waitfor" access.log
```

```splunk
index=web_logs | search uri_path="*union*" OR uri_path="*select*" OR uri_path="*--*"
| table _time, clientip, uri_path, status
```

---

## XSS Detection

```bash
grep -iE "<script|javascript:|onerror=|onload=|alert\(|%3Cscript" access.log
```

---

## Command Injection

```bash
grep -iE ";.*(whoami|id|ls|cat)|%7C.*(id|whoami)|&&.*ls" access.log
```

---

## Directory Traversal

```bash
grep -iE "\.\./|%2E%2E%2F|etc/passwd|win.ini" access.log
```

---

## Brute Force Detection

```bash
awk '$9 == 401 {print $1}' access.log | sort | uniq -c | sort -rn
```

```splunk
index=web_logs uri_path="/login" status=401
| bin _time span=1m
| stats count by _time, clientip
| where count > 10
```

---

## Scanner Detection

```bash
grep -iE "nikto|sqlmap|burpsuite|nmap|openvas|dirbuster" access.log
awk '$9 == 404 {print $1}' access.log | sort | uniq -c | sort -rn | head -5
```

---

## Key Takeaways

> Automated attack tools are much easier to detect than skilled manual attackers. They generate characteristic patterns — many 404s, known User-Agent strings, requests per second that no human produces.

---

## References

- [MITRE ATT&CK T1190 Exploit Public-Facing Application](https://attack.mitre.org/techniques/T1190/)
