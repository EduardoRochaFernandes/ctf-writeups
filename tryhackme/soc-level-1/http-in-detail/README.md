# Room: HTTP in Detail

**Platform:** TryHackMe
**Path:** SOC Level 1
**Category:** Web Security
**Difficulty:** Easy
**Type:** Walkthrough
**Cost:** Free
**Room Link:** https://tryhackme.com/room/httpindetail

---

## What is this room about?

HTTP powers the web, and every web-based attack travels over it. Covers request/response mechanics, methods, status codes, headers, and cookies — essential context for web attack detection in logs and Wireshark.

---

## HTTP vs HTTPS

- **HTTP** — plaintext, everything visible on the wire
- **HTTPS** — HTTP wrapped in TLS. Encrypts data in transit. Does NOT protect against application-layer attacks.

---

## HTTP Request Structure

```
GET /page HTTP/1.1
Host: tryhackme.com
User-Agent: Mozilla/5.0 Firefox/87.0
Referer: https://tryhackme.com/

```

Method + path + version on line 1. Blank line signals end of request.

---

## HTTP Methods

| Method | Purpose | SOC relevance |
|--------|---------|---------------|
| **GET** | Retrieve resource | Directory scanning = many GETs, many 404s |
| **POST** | Send data | Brute force, credential submission |
| **PUT** | Create/replace | Web shell upload |
| **DELETE** | Remove resource | Data destruction |

---

## HTTP Status Code Patterns for SOC

| Pattern | What it indicates |
|---------|------------------|
| Many 401s then 200 | Brute force succeeded |
| Many 404s from same IP | Directory scanning |
| 500 after POST with SQL keywords | Injection attempt |
| 302 after POST to /login | Login attempt (success or failure) |

Full ranges: 200-299 Success, 300-399 Redirect, 400-499 Client error, 500-599 Server error.

---

## Key Headers

**Request headers analysts care about:**
- `User-Agent` — tool identification. sqlmap, Nmap, curl are recognisable.
- `Cookie` — session token. Theft = session hijacking without needing password.
- `Authorization` — credentials for protected endpoints.

**Response headers:**
- `Server` — software and version (fingerprinting target).
- `Set-Cookie` — session cookie creation.

---

## Cookies

HTTP is stateless. Server sends session token as cookie after login. Browser returns it with every request. Security flags: `HttpOnly` (blocks JS access), `Secure` (HTTPS only), `SameSite` (CSRF mitigation).

---

## Key Takeaways

> User-Agent strings are an underused detection channel. Most automated attack tools identify themselves. `grep "sqlmap" access.log` is one of the fastest triage actions you can do on a web log.

---

## References

- [MDN HTTP Documentation](https://developer.mozilla.org/en-US/docs/Web/HTTP)
- [OWASP Testing Guide](https://owasp.org/www-project-web-security-testing-guide/)
