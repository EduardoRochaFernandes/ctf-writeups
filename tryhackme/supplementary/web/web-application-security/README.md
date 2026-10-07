# Web Application Security

**Platform:** TryHackMe
**Path:** Supplementary — web security foundations
**Status:** Complete

---

## Key Notes

OWASP Top 10 in practice. SQL injection: `' OR '1'='1` bypasses login, `UNION SELECT` extracts data. IDOR: changing `?user_id=123` to `?user_id=124` without server-side authorisation. Authentication failures: rate limiting, MFA. Detection: SQL keywords in URL params, systematic numeric ID increments in access logs.
