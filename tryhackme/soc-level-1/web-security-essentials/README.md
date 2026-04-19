# Room: Web Security Essentials

**Platform:** TryHackMe
**Path:** SOC Level 1
**Category:** Web Security
**Difficulty:** Easy
**Type:** Walkthrough
**Cost:** Free
**Room Link:** https://tryhackme.com/room/websecurityessentials

---

## What is this room about?

Covers the security controls protecting web applications — HTTPS, secure session management, XSS, CSRF, and Content Security Policy.

---

## Session Management

After login, server sends a unique session token as a cookie. Browser returns it with every subsequent request. If stolen, the attacker impersonates the user without needing their password.

**Secure cookie flags:**
- `HttpOnly` — JavaScript cannot read the cookie (blocks XSS-based theft)
- `Secure` — only sent over HTTPS
- `SameSite` — prevents CSRF attacks

---

## XSS — Cross-Site Scripting

Attacker injects JavaScript that executes in the victim's browser, accessing cookies, the DOM, and making requests as the victim.

- **Reflected XSS** — payload in URL, executed when victim visits crafted link
- **Stored XSS** — payload saved to database, executed for every visitor (most dangerous)

**Mitigation:** Output encoding, Content Security Policy.

---

## CSRF — Cross-Site Request Forgery

Tricks logged-in user into making unintended requests. A malicious page auto-submits a form targeting the victim's bank.

**Mitigation:** CSRF tokens — unique per-session value included in every form, validated server-side.

---

## Content Security Policy

HTTP response header restricting which resource sources the browser can load:
```
Content-Security-Policy: default-src 'self'; script-src 'self' cdn.example.com
```

Injected scripts pointing to external servers are blocked if the source isn't whitelisted.

---

## Key Takeaways

> Session token theft bypasses all authentication. The attacker has a valid token — they look identical to a legitimate user. Detection requires behavioural analysis: same token from a completely different IP or User-Agent.
