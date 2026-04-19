# Room: Web Application Basics

**Platform:** TryHackMe
**Path:** SOC Level 1
**Category:** Web Security
**Difficulty:** Easy
**Type:** Walkthrough
**Cost:** Free
**Room Link:** https://tryhackme.com/room/webapplicationbasics

---

## What is this room about?

Foundational knowledge about how web applications work — the client-server model, URL anatomy, HTTP request/response structure, and security-relevant headers.

---

## URL Structure

```
https://shop.example.com:443/products?category=shoes#results
scheme  domain              port path   query          fragment
```

The query string is the most common injection surface — SQL injection, XSS, and path traversal are frequently injected here.

---

## Client-Server Model

1. Browser sends HTTP request to web server
2. Web server forwards to application server
3. Application server runs logic, queries database
4. Response returned to browser

---

## Security-Relevant Response Headers

| Header | Protection |
|--------|-----------|
| `Content-Security-Policy` | Restricts resource loading — mitigates XSS |
| `X-Frame-Options` | Prevents clickjacking |
| `Strict-Transport-Security` | Forces HTTPS — prevents SSL stripping |
| `X-Content-Type-Options` | Prevents MIME type sniffing |

---

## Key Takeaways

> When you see `?id=1 UNION SELECT null,username,password FROM users--` in an access log, understanding URL structure lets you immediately recognise it as SQL injection injected into a query parameter.

---

## References

- [MDN How the Web Works](https://developer.mozilla.org/en-US/docs/Learn/Getting_started_with_the_web/How_the_Web_works)
- [OWASP Top 10](https://owasp.org/www-project-top-ten/)
