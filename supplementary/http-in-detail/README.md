# HTTP in Detail

**Platform:** TryHackMe
**Path:** Supplementary — web protocol foundations
**Difficulty:** Easy
**Status:** Complete

---

## Overview

HTTP is the protocol underlying every web-based attack. This room covers request/response mechanics, methods, status codes, headers, and cookies — foundations for web log analysis and network traffic investigation.

---

## HTTP Request Structure

```
GET /page HTTP/1.1
Host: example.com
User-Agent: Mozilla/5.0 Firefox/87.0
```

Method + path + HTTP version on line 1. Blank line signals end of headers.

---

## HTTP Methods

| Method | Normal use | Attack relevance |
|--------|-----------|-----------------|
| GET | Retrieve resources | Directory scanning, enumeration |
| POST | Submit data | Credential brute force, SQLi |
| PUT | Create/replace | Web shell upload |
| DELETE | Remove resources | Data destruction |

---

## Status Code SOC Patterns

| Pattern | Indicates |
|---------|----------|
| Many 401s then 200 from same IP | Brute force succeeded |
| Many 404s in rapid sequence | Directory/file enumeration |
| 500 after POST with SQL keywords | Injection causing server error |

Full ranges: 200-299 Success, 300-399 Redirect, 400-499 Client error, 500-599 Server error.

---

## Security-Relevant Headers

**Request:** `User-Agent` (tool fingerprinting), `Cookie` (session token), `Authorization` (credentials).

**Response:** `Server` (version disclosure), `Set-Cookie` (session creation), `Content-Security-Policy` (XSS mitigation).

**Cookie flags:** `HttpOnly` prevents JavaScript access. `Secure` HTTPS-only transmission. `SameSite` CSRF mitigation.

---

## References

- [MDN HTTP Documentation](https://developer.mozilla.org/en-US/docs/Web/HTTP)
