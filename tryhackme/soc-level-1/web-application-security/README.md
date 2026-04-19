# Room: Web Application Security

**Platform:** TryHackMe
**Path:** SOC Level 1
**Category:** Web Security
**Difficulty:** Easy
**Type:** Walkthrough
**Cost:** Free
**Room Link:** https://tryhackme.com/room/webapplicationsecurity

---

## What is this room about?

Covers the most common web application vulnerabilities with practical examples — SQL injection, IDOR (broken access control), authentication failures, and cryptographic weaknesses. Understanding these from the attacker's perspective makes you a better defender.

---

## SQL Injection

User input passed to database without sanitisation:
```sql
' OR '1'='1       -- bypasses login for any user
' UNION SELECT username,password FROM users--   -- dumps credentials
```

**Detection:** SQL keywords in URL parameters or POST body: `UNION`, `SELECT`, `--`, `%27` (URL-encoded `'`). Unusual response times may indicate time-based SQLi.

---

## IDOR — Insecure Direct Object Reference

Changing `?user_id=123` to `?user_id=124` accesses another user's data. Broken access control — authorisation not enforced server-side.

**Detection:** Users accessing resources in systematic numeric increments. Users accessing objects they've never accessed before.

---

## Authentication Failures

No rate limiting on login = brute force. Weak passwords + no MFA = credential stuffing works.

**Detection:** Multiple 401 responses from same IP, then a 200. Multiple usernames from same IP (password spraying).

---

## Hands-On Exercise

The room provides a vulnerable web application:
- IDOR: changed user_id parameter to access another user's data without authorisation
- Login bypass: `' OR '1'='1'--` in username field bypassed authentication
- Error disclosure: database errors revealed schema information

---

## Key Takeaways

> IDOR doesn't look like an attack in logs — it's just a user making a GET request. Detecting it requires knowing which users should access which resources, not just looking for suspicious syntax.

---

## References

- [OWASP Top 10](https://owasp.org/www-project-top-ten/)
- [PortSwigger Web Security Academy](https://portswigger.net/web-security)
