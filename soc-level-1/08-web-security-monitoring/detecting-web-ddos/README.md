# Detecting Web DDoS

**Platform:** TryHackMe
**Path:** SOC Level 1 — Section 08: Web Security Monitoring
**Difficulty:** Easy
**Type:** Walkthrough
**Status:** Complete

---

## Overview

Denial-of-Service and Distributed Denial-of-Service attacks aim to make a web application unavailable by overwhelming its resources. This room covers the attack types, log-based detection techniques, SIEM analysis, and the infrastructure defences that mitigate them.

---

## DoS vs DDoS

- **DoS** — single machine. Limited by the attacker's own bandwidth and CPU.
- **DDoS** — botnet of thousands of compromised devices, coordinated to amplify volume beyond what any single source could achieve.

---

## Web Application Layer Attack Types

| Attack | Mechanism |
|--------|-----------|
| HTTP Flood | Massive volume of legitimate-looking HTTP requests saturating the server's connection limit |
| Slowloris | Sends many incomplete HTTP requests, keeping connections open until the server's connection pool is exhausted |
| Cache Bypass | Appends random parameters (`?rand=abc`) to URLs, forcing origin server to respond for every request instead of serving cached content from CDN |
| Oversized Query | Requests with huge parameter values (`?limit=999999`) forcing expensive database operations |
| Login Abuse | Floods authentication endpoints, triggering DB queries and session creation on every attempt |
| Input Validation Exploitation | Submits inputs that trigger crashes or hangs in poorly validated application code |

---

## Detection in Access Logs

**Indicators:**

| Indicator | Description |
|-----------|-------------|
| High request rate per IP | >1000 GET /login in 60 seconds from one IP — not human |
| Burst of identical timestamps | Dozens of requests with the same second timestamp — automated tool |
| Automated User-Agents | `curl/7.x`, `Python-urllib`, `python-requests` |
| Geographic anomalies | Traffic simultaneously from dozens of countries |
| 5xx error spike | Server failing under load — 503 Service Unavailable surge |
| Cache bypass patterns | Random query parameters on static resource URLs |

**Shell analysis:**
```bash
# Request rate per IP per minute
awk '{print $4, $1}' access.log | cut -c1-17,19- | sort | uniq -c | sort -rn | head 20

# Top User-Agents
awk -F'"' '{print $6}' access.log | sort | uniq -c | sort -rn | head 10

# Requests to login endpoint
grep '"POST /login' access.log | cut -d' ' -f1 | sort | uniq -c | sort -rn
```

---

## SIEM Detection (Splunk)

```splunk
index=web_logs
| bin _time span=1m
| stats count by _time, src_ip
| where count > 100
| sort - count

index=web_logs uri_path="/login" status=429 OR status=503
| timechart count by src_ip

index=web_logs
| where match(useragent, "curl|python|bot|scanner")
| stats count by src_ip, useragent
| sort - count
```

---

## Defences

**Application layer:**
- Rate limiting — maximum N requests per minute per IP on sensitive endpoints
- CAPTCHA — prevents automated form submission
- Input validation — reject malformed or oversized inputs at the application boundary

**Infrastructure layer:**
- CDN — serves cached content from edge nodes close to users, removing load from the origin server
- WAF (Web Application Firewall) — inspects and filters malicious requests at the network edge
- Load balancing — distributes traffic across multiple server instances
- Auto-scaling — dynamically provisions additional capacity during traffic spikes

**How attackers bypass defences:**
- Cache bypass (`?rand=xyz`) — forces origin response
- Rotating User-Agents — evades UA-based blocking
- Distributed sources — evades single-IP rate limiting
- Randomised request patterns — evades pattern-matching rules

---

## Scale Reference

- **Google, 2023:** Mitigated a DDoS peaking at 398 million requests per second
- **Cloudflare:** Has mitigated attacks exceeding 11.5 Tbps

---

## Key Takeaways

The Cache Bypass technique is elegant in its simplicity: by appending a random query parameter, the attacker converts every request from a cached response (served instantly by CDN) to an origin request (requiring server processing, database queries, and application logic). This multiplies the effective load by orders of magnitude. WAF rules that detect random parameter patterns on normally parameter-free endpoints can catch this.
