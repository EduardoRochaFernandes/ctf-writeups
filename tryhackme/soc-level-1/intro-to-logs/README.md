# Room: Intro to Logs

**Platform:** TryHackMe
**Path:** SOC Level 1
**Category:** Log Analysis
**Difficulty:** Easy
**Type:** Walkthrough
**Cost:** Free
**Room Link:** https://tryhackme.com/room/introtologs

---

## What is this room about?

Before you can analyse logs, you need to understand what they are, where they come from, how they're formatted, and how to work with them. This room covers all the fundamentals — a solid foundation for everything else in the log analysis module.

---

## What is a Log?

A log is a structured record of an event that answers: what happened, when, where, who caused it, and what the outcome was. Every log entry should contain at minimum:
- **Timestamp** (with timezone — critical for correlation)
- **Source** (system, application, or device that generated it)
- **Event type** (what kind of event)
- **Severity** (Information → Warning → Error → Critical)
- **Details** (IP, username, error code, etc.)

---

## Log Sources

**Physical:** CCTV footage, door access logs, badge readers.

**Virtual:**
- Network devices (routers, switches, firewalls)
- Operating systems
- Security appliances (IDS/IPS, antivirus, DLP, VPN)
- Applications and frameworks (.NET, Java, PHP)
- Cloud platforms and databases
- Mobile devices and IoT

---

## Log Formats

### Unstructured (text-based, human-readable)
- **NCSA CLF (Apache):** `IP - user [timestamp] "method path" status bytes`
- **NCSA Combined (Nginx):** Adds Referer and User-Agent fields

### Semi-structured
- **Syslog** — widely used protocol for system and network logs
- **Windows EVTX** — Microsoft's proprietary binary format

### Structured (easy to parse programmatically)
- **CSV/TSV** — tabular data
- **JSON** — key-value pairs, most common in modern applications
- **XML** — verbose but structured

---

## Log Locations

| System | Log location |
|--------|-------------|
| Linux syslog | `/var/log/syslog` or `/var/log/messages` |
| Linux auth | `/var/log/auth.log` or `/var/log/secure` |
| Windows | `C:\Windows\System32\winevt\Logs\` |
| Apache | `/var/log/apache2/access.log` |
| Nginx | `/var/log/nginx/access.log` |
| MySQL | `/var/log/mysql/error.log` |
| Snort | `/var/log/snort/` |

---

## Timestamp Synchronisation

**NTP (Network Time Protocol)** is non-negotiable. Logs from different systems must have synchronised timestamps or correlation becomes impossible. A one-minute clock difference between a web server and a domain controller can make it look like authentication happened before the HTTP request — breaking your attack timeline completely.

---

## Storage Tiers

| Tier | Retention | Access speed |
|------|-----------|-------------|
| **Hot** | 0–6 months | Near real-time |
| **Warm** | 6 months–2 years | Slower, still accessible |
| **Cold** | 2–5 years | Archived, for retroactive analysis |

---

## The Log Analysis Pipeline

```
Raw logs
    → Parsing (break into fields)
    → Normalisation (standardise format)
    → Enrichment (add context — GeoIP, threat intel)
    → Correlation (link related events)
    → Visualisation (dashboards, graphs)
    → Reporting (summaries, compliance)
```

---

## Common Threats Visible in Logs

| Pattern | Likely attack |
|---------|--------------|
| Multiple failed logins, then success | Brute force succeeded |
| Logins at 3am from unknown IP | Compromised credentials |
| SQL keywords in access.log (`UNION`, `SELECT`, `--`) | SQL injection attempt |
| `../../../etc/passwd` in URI | Path traversal |
| `<script>` in GET parameters | XSS attempt |
| High volume same-second requests | DoS or brute force bot |

---

## Key Takeaways

> Logs are your evidence. They're only useful if they're complete, timestamped, and from the right sources.

The concept of **super timelines** stuck with me most — aggregating logs from a dozen sources into a single chronological view to reconstruct an attack. Tools like **Plaso (log2timeline)** automate this. Without a super timeline, you're solving a puzzle with half the pieces.

---

## References

- [SANS — Log Management](https://www.sans.org/white-papers/1168/)
- [OWASP — Logging Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/Logging_Cheat_Sheet.html)
